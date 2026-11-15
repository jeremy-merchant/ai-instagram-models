# 🎲 prompt_randomizer — 미오 일상 피드 랜덤 프롬프트 생성기

`@_3io.log_` 미오의 인스타 일상 피드를 **매번 같은 앞머리·같은 포즈로 찍은 것처럼 보이지 않게** 뽑아주는 생성기입니다.

> 기운님 피드백: *"앞머리가 너무 일정하지 않나 ㅋㅋ 상황이랑. 좀 다양하게 하고 그냥 일상사진부터 올려야 하니까 그런 것도 기획해서, 옷도 다양하게 하고 이런 거 랜덤으로 뽑아주는 깃 레포 있으면 그런 거 쓰자"*

## 참고 오픈소스

카테고리 사전을 JSON으로 나눠 두고 시드로 뽑는 구조는 **[fairy-root/Flux-Prompt-Generator](https://github.com/fairy-root/Flux-Prompt-Generator)** (MIT License, 원작 [Aitrepreneur FLUX-Prompt-Generator](https://huggingface.co/Aitrepreneur/FLUX-Prompt-Generator)) 를 참고했습니다. 원본의 `data/*.json` 카테고리(Hairstyles · Clothing · Composition · Device · Lighting · Place · Pose · Expression 등)를 확인한 뒤, 미오 전용 풀로 재작성했습니다. 원본 앱은 ComfyUI 노드라 이 레포에는 코드를 복사하지 않고 **구조만 참고**했습니다.

## 파일

| 파일 | 설명 |
| --- | --- |
| `generate_prompts.py` | 시드 고정 랜덤 조합 → 4:5 인스타 피드 프롬프트 출력 |
| `pools.json` | 미오 전용 카테고리 풀 (한국어 라벨 + 영어 프롬프트 조각) |
| `examples/seed_20261116.json` | v2 12컷에 실제로 쓴 배치 (재현용) |
| `examples/seed_20261116.md` | 같은 배치의 표 형식 요약 |

## 카테고리 풀

| 카테고리 | 개수 | 내용 |
| --- | --- | --- |
| `no_face_scenes` | 14 | 말차 디저트·서점 서가·밤 자판기 골목·아침 책상·전철 창밖·장바구니·신발 OOTD·동전 세탁소·비 오는 창가 등 (장면마다 조명 고정) |
| `hairstyles` | 14 | 센터 가르마(앞머리 없음)·사이드 스웹트·높은 포니테일·로우 번·하프업·자연 웨이브·비니·베레모·볼캡·사이드 브레이드·양갈래·단발 보브 등 |
| `clothing` | 14 | 후드+조거·스트라이프 옥스포드·트렌치·데님 자켓·플로럴 원피스·가죽 자켓·파자마·가디건+롱스커트·오트밀 니트+와이드 연청·트레이닝·울코트 등 |
| `person_shots` | 12 | 옆모습·뒷모습 돌아보기·거울 셀카(얼굴 가림)·멀리서 찍은 스냅·책 보는 시선·먹기 직전·걸어가는 뒷모습·창밖 응시·머리 묶는 중 등 |
| `places_person` | 12 | 도쿄 골목·카페 창가·전철 좌석·침대·세탁소·편의점 앞·서점·강변·공원·주방·레코드숍·플랫폼 (실내/실외 + 가능한 조명 목록 포함) |
| `expressions` | 7 | 나른함·옅은 미소·눈웃음·졸린 눈·생각하는 표정·삐죽·입 벌린 웃음 |
| `devices` | 6 | 아이폰 15 프로·13 미니·필름 카메라·폴라로이드·후지 X100V·2010년대 디카 |

## 핵심 규칙

1. **배치 내 중복 금지** — 헤어·의상·구도·장소는 한 배치(12컷) 안에서 서로 겹치지 않게 뽑습니다. 8컷이면 헤어 8종, 의상 8종이 전부 다릅니다.
2. **모순 조합 방지** — 조명은 장소에 맞는 후보 중에서만 뽑고(밤 골목에 골든아워가 붙지 않음), 실내 구도는 실내 장소, 실외 구도는 실외 장소와 짝지어집니다.
3. **정면 응시 최소화** — 인물 구도 12종 중 정면 카메라 응시는 0종. 시선이 접시·책·창밖으로 향하거나, 뒷모습·거울 가림으로 처리됩니다.
4. **얼굴만 유지** — 프롬프트 끝에 항상 `Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.` 를 붙여 레퍼런스의 시스루 뱅·오프숄더 니트가 따라오지 않게 합니다.

## 사용법

```bash
# 기본: 노페이스 4 + 인물 8 = 12컷, 시드 20261116
python3 generate_prompts.py

# 시드·컷 수 지정, JSON/표로 저장
python3 generate_prompts.py --seed 20261116 --noface 4 --person 8 \
    --json out/prompts.json --markdown out/prompts.md

# 총 6컷만 (노페이스 2 + 인물 4)
python3 generate_prompts.py --seed 42 --count 6

# 여러 시드의 스타일 지문 미리 보기
python3 generate_prompts.py --list-seed 5
```

출력 예:

```
[05] (person) 앞머리 없는 센터 가르마 흑발 · 스트라이프 옥스포드 셔츠 (허리 묶음) · 음식 먹기 직전, 시선은 접시로 · 전철 안 좌석
    Using the reference photo only for the woman face, keep her facial features exactly identical ...
```

## 이미지 생성으로 이어 붙이기

- **노페이스 컷:** `images '<prompt>' --out work/mio_v2/raw/xx.jpg`
- **인물 컷:** `images '<prompt>' --edit downloads/mio_master_clean.jpg --out work/mio_v2/raw/xx.jpg`
  (`mio_master_clean.jpg` = `338.jpg` 정면 마스터 크롭본)
- 생성 후 **반드시 눈으로 검수**: 앞머리가 또 같은지, 손가락이 뭉개졌는지, 배경 글자가 깨졌는지. 문제가 있으면 해당 컷만 프롬프트를 다듬어 재생성하고 `mio_feed_v2/manifest.json`에 최종 프롬프트를 남깁니다.
- 4:5가 아닌 결과는 1080×1350 중앙 크롭으로 통일합니다.

## 새 카테고리 아이템 추가

`pools.json` 배열에 항목을 하나 더 넣으면 됩니다.

```json
{ "id": "bucket_hat", "ko": "버킷햇", "en": "a faded denim bucket hat pulled low, hair tucked behind the ears" }
```

`places_person`은 `io`(`in`/`out`)와 `lights`(가능한 조명 목록)를 함께 넣어야 조합이 어긋나지 않습니다.
