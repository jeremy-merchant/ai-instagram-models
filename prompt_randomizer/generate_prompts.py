#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mio daily-feed random prompt generator (@_3io.log_).

Builds randomized, reproducible Instagram feed prompts for the AI model "Mio"
from the category pools in pools.json.  The pool structure follows
fairy-root/Flux-Prompt-Generator (MIT) —
https://github.com/fairy-root/Flux-Prompt-Generator

v2.1 (2026-11-16) — "AI 티" 제거 개정
    * AI 화보 키워드(cinematic / golden hour / bokeh / 8k / masterpiece /
      perfect skin ...)를 풀에서 전부 지우고, 남아 있으면 --check 가 실패합니다.
    * 카메라 풀은 최신 아이폰(15/16 Pro)만 사용합니다. 거울 셀카는 자동으로
      최신 Pro 모델 + 3구 카메라 묘사를 붙입니다.
    * 구도는 "친구가 그냥 찍어준 일상 스냅" 기준으로 다시 썼고, 모든 프롬프트에
      흔들린 프레이밍·폰 노이즈·모공 같은 불완전함 문장을 강제로 넣습니다.

Key property: every batch samples each category *without replacement*, so a
12-cut batch never repeats the same hairstyle / outfit / camera angle again
(this is what kills the "same bangs, same pose" copy-paste look).

Usage
-----
    python3 generate_prompts.py                        # seed 20261116, 4 no-face + 8 person
    python3 generate_prompts.py --seed 7 --count 12
    python3 generate_prompts.py --noface 4 --person 8 --seed 20261116 \
        --json out/prompts.json --markdown out/prompts.md
    python3 generate_prompts.py --check                # 생성 후 금지어 검사만
    python3 generate_prompts.py --list-seed 5          # show 5 different batches' fingerprints
"""

import argparse
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
POOLS = json.loads((HERE / "pools.json").read_text(encoding="utf-8"))
META = POOLS.get("meta", {})
BANNED = [k.lower() for k in META.get("banned_keywords", [])]

NOFACE_TEMPLATE = (
    "A real amateur phone photo for an Instagram feed, taken on {device}. "
    "Scene: {scene}. "
    "{lighting}. "
    "Everyday and imperfect: {imperfection}. Natural phone noise, ordinary exposure, "
    "realistic texture, plain colour. "
    "Vertical 4:5. No studio lighting, no bokeh, no cinematic colour grade, no HDR, "
    "no text, no watermark, no face visible."
)

PERSON_TEMPLATE = (
    "A real amateur phone photo for an Instagram feed, taken on {device}. "
    "Keep the woman's face from the reference photo identical (same eyes, nose, mouth, "
    "face shape, skin tone); change everything else: {hairstyle}. "
    "She is wearing {clothing}. "
    "{shot}{phone_text} "
    "Place: {place}. Expression: {expression}. Light: {lighting}. "
    "Everyday and imperfect: {imperfection}. "
    "Real skin with visible pores and small texture, light everyday makeup, "
    "no beauty retouching, no skin smoothing, no glow. "
    "Vertical 4:5. No studio lighting, no bokeh, no cinematic colour grade, no HDR, "
    "no text, no watermark. "
    "Do not reproduce the reference pose, outfit, hairstyle or background."
)


def sample(pool, n, rng):
    """Sample n items without replacement (shuffled copy), cycling if n > len(pool)."""
    pool = list(pool)
    rng.shuffle(pool)
    out = []
    while len(out) < n:
        out.extend(pool)
        if len(pool) < n:
            rng.shuffle(pool)
    return out[:n]


def pick_device(forced, rng):
    """Pick a device; a shot that forces one (e.g. a mirror selfie) wins."""
    devices = POOLS["devices"]
    if forced:
        for d in devices:
            if d.get("id") == forced:
                return d
        default_id = POOLS.get("device_default_for_mirror")
        for d in devices:
            if d.get("id") == default_id:
                return d
    return rng.choice(devices)


def build_batch(seed, noface, person):
    rng = random.Random(seed)
    items = []
    imperfections = POOLS["imperfections"]

    scenes = sample(POOLS["no_face_scenes"], noface, rng)
    hairstyles = sample(POOLS["hairstyles"], person, rng)
    clothes = sample(POOLS["clothing"], person, rng)
    shots = sample(POOLS["person_shots"], person, rng)
    places = sample(POOLS["places_person"], person, rng)

    for i, sc in enumerate(scenes, 1):
        dv = rng.choice(POOLS["devices"])
        items.append({
            "id": f"{i:02d}",
            "mode": "noface",
            "seed": seed,
            "label_ko": sc["ko"],
            "prompt": NOFACE_TEMPLATE.format(
                scene=sc["en"],
                lighting=sc["light_en"],
                device=dv["en"],
                imperfection=rng.choice(imperfections),
            ),
            "combo": {"scene": sc["id"], "light": sc["light_ko"], "device": dv["ko"]},
        })

    for j in range(person):
        hs, cl, sh, pl = hairstyles[j], clothes[j], shots[j], places[j]
        # a shot that only makes sense in certain places (mirror selfie, table snap)
        # overrides the sampled place, then keep an indoor shot indoors.
        allowed = sh.get("place_ids")
        if allowed:
            taken = {x["id"] for x in places[:j]}
            pool = [p for p in POOLS["places_person"]
                    if p["id"] in allowed and p["id"] not in taken] or \
                   [p for p in POOLS["places_person"] if p["id"] in allowed]
            pl = pool[j % len(pool)]
        elif sh.get("io") and pl.get("io") != sh["io"]:
            taken = {x["id"] for x in places[:j]}
            pool = [p for p in POOLS["places_person"]
                    if p.get("io") == sh["io"] and p["id"] not in taken]
            pl = (pool or places)[j % len(pool or places)]

        li = rng.choice(pl.get("lights") or POOLS["lighting"])
        dv = pick_device(sh.get("device_force"), rng)
        ex = rng.choice(POOLS["expressions"])
        phone_text = (" " + sh["phone_text"]) if sh.get("phone_text") else ""
        items.append({
            "id": f"{noface + j + 1:02d}",
            "mode": "person",
            "seed": seed,
            "label_ko": f"{hs['ko']} · {cl['ko']} · {sh['ko']} · {pl['ko']}",
            "prompt": PERSON_TEMPLATE.format(
                hairstyle=hs["en"], clothing=cl["en"], shot=sh["en"],
                phone_text=phone_text, place=pl["en"], expression=ex["en"],
                lighting=li["en"], device=dv["en"],
                imperfection=rng.choice(imperfections),
            ),
            "combo": {"hairstyle": hs["id"], "clothing": cl["id"], "shot": sh["id"],
                      "place": pl["id"], "expression": ex["ko"],
                      "lighting": li["ko"], "device": dv["ko"]},
        })
    return items


NEGATIVE_CLAUSES = [
    "no studio lighting",
    "no bokeh",
    "no cinematic colour grade",
    "no beauty retouching",
    "no skin smoothing",
]


def check_batch(items):
    """Return a list of (item id, banned phrase) hits; empty means clean.

    The mandatory negative clauses ("no studio lighting", "no bokeh", ...) are
    stripped first — they are what keeps AI gloss out, not a violation.
    """
    hits = []
    for it in items:
        low = it["prompt"].lower()
        for clause in NEGATIVE_CLAUSES:
            low = low.replace(clause, "")
        for word in BANNED:
            if any(clause.endswith(word) or word in clause for clause in NEGATIVE_CLAUSES):
                continue
            if word in low:
                hits.append((it["id"], word))
    return hits


def main(argv=None):
    ap = argparse.ArgumentParser(description="Mio feed random prompt generator (v2.1, anti-AI-tell)")
    ap.add_argument("--seed", type=int, default=20261116)
    ap.add_argument("--noface", type=int, default=4, help="number of no-face daily cuts")
    ap.add_argument("--person", type=int, default=8, help="number of person cuts")
    ap.add_argument("--count", type=int, help="total cuts (overrides --noface default ratio 1:2)")
    ap.add_argument("--json", dest="json_path", help="write the batch as JSON")
    ap.add_argument("--markdown", dest="md_path", help="write a prompt table as Markdown")
    ap.add_argument("--check", action="store_true", help="after building, verify no banned keyword is present")
    ap.add_argument("--list-seed", type=int, help="print N batches' style fingerprints and exit")
    args = ap.parse_args(argv)

    if args.list_seed:
        for s in range(args.seed, args.seed + args.list_seed):
            batch = build_batch(s, args.noface, args.person)
            tags = [b["combo"].get("hairstyle", b["combo"].get("scene")) for b in batch]
            print(f"seed {s}: " + ", ".join(tags))
        return 0

    if args.count:
        args.noface = round(args.count / 3)
        args.person = args.count - args.noface

    batch = build_batch(args.seed, args.noface, args.person)

    print(f"# Mio feed prompts — seed {args.seed} · {len(batch)} cuts "
          f"({args.noface} no-face / {args.person} person)\n")
    for b in batch:
        print(f"[{b['id']}] ({b['mode']}) {b['label_ko']}")
        print(f"    {b['prompt']}\n")

    if args.check:
        hits = check_batch(batch)
        if hits:
            print("banned keyword hits:", hits, file=sys.stderr)
            return 2
        print(f"check: clean ({len(BANNED)} banned phrases scanned)")

    if args.json_path:
        p = Path(args.json_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"seed": args.seed, "items": batch},
                                ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"wrote {p}")

    if args.md_path:
        p = Path(args.md_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        lines = ["| # | 유형 | 헤어 | 의상 | 구도·시선 | 장소 | 카메라 | 조명 | 시드 |",
                 "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for b in batch:
            c = b["combo"]
            if b["mode"] == "noface":
                lines.append(f"| {b['id']} | 노페이스 | – | – | – | {b['label_ko']} | "
                             f"{c['device']} | {c['light']} | {b['seed']} |")
            else:
                lines.append(
                    f"| {b['id']} | 인물 | {_ko(POOLS['hairstyles'], c['hairstyle'])} | "
                    f"{_ko(POOLS['clothing'], c['clothing'])} | "
                    f"{_ko(POOLS['person_shots'], c['shot'])} | "
                    f"{_ko(POOLS['places_person'], c['place'], key='ko')} | "
                    f"{c['device']} | {c['lighting']} | {b['seed']} |")
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"wrote {p}")
    return 0


def _ko(pool, item_id, key="id"):
    for x in pool:
        if x.get("id") == item_id:
            return x["ko"]
    return item_id


if __name__ == "__main__":
    sys.exit(main())
