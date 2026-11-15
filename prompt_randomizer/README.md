# 🎲 prompt_randomizer — 미오 일상 피드 랜덤 프롬프트 생성기

`@_3io.log_` 미오의 인스타 일상 피드를 **매번 같은 앞머리·같은 포즈로 찍은 것처럼 보이지 않게** 뽑아주는 생성기입니다.

> 기운님 피드백 1: *"앞머리가 너무 일정하지 않나 ㅋㅋ 상황이랑. 좀 다양하게 하고 그냥 일상사진부터 올려야 하니까 그런 것도 기획해서, 옷도 다양하게 하고 이런 거 랜덤으로 뽑아주는 깃 레포 있으면 그런 거 쓰자"*
>
> 기운님 피드백 2: *"너무 ai 스럽거나 아이폰 너무예전꺼거나 구도자체가 ai 스러운거는 다시만들자"* → **v2.1 개정** (AI 티 제거 · 최신 아이폰 고정 · 현실적 일상 구도)

## 참고 오픈소스

카테고리 사전을 JSON으로 나눠 두고 시드로 뽑는 구조는 **[fairy-root/Flux-Prompt-Generator](https://github.com/fairy-root/Flux-Prompt-Generator)** (MIT License, 원작 [Aitrepreneur FLUX-Prompt-Generator](https://huggingface.co/Aitrepreneur/FLUX-Prompt-Generator)) 를 참고했습니다. 원본의 `data/*.json` 카테고리(Hairstyles · Clothing · Composition · Device · Lighting · Place · Pose · Expression 등)를 확인한 뒤, 미오 전용 풀로 재작성했습니다. 원본 앱은 ComfyUI 노드이므로 코드를 복사하지 않고 **구조만 참고**했습니다.

## 파일

| 파일 | 설명 |
| --- | --- |
| `generate_prompts.py` | 시드 고정 랜덤 조합 → 4:5 인스타 피드 프롬프트 출력 (+ `--check` 금지어 검사) |
| `pools.json` | 미오 전용 카테고리 풀 (한국어 라벨 + 영어 프롬프트 조각 + 금지어 목록) |
| `examples/seed_20261116.json` | v2.1 생성기로 뽑은 12컷 배치 (재현용) |
| `examples/seed_20261116.md` | 같은 배치의 표 형식 요약 |
| `examples/seed_20261116_glamour.json` / `.md` | v3 glamour 모드로 뽑은 8컷 배치 |

## v2.1에서 바뀐 것 (2026-11-16)

| 항목 | v2 | v2.1 |
| --- | --- | --- |
| AI 화보 키워드 | `cinematic`, `golden hour backlight`, `soft bokeh`, `8k`, `masterpiece`, `perfect skin` 등 잔존 | **풀에서 전면 삭제.** `meta.banned_keywords`에 목록을 박아두고 `--check`가 하나라도 걸리면 exit 2 |
| 카메라 | 아이폰 13 mini·2010년대 구형 디카·폴라로이드·후지 X100V | **최신 아이폰만** (15 Pro / 16 Pro / 양쪽 3배 망원 / 15 Pro 초광각). 구형 기기·폴라로이드·필름 제거 |
| 거울 셀카 | 구형 폰이 잡힘 | 거울 셀카 구도가 뽑히면 **자동으로 최신 Pro + "3구 카메라·티타늄 바디" 묘사 문장 삽입** |
| 구도 | 옆모습·머리 묶는 중·창밖 응시 등 화보형 | **친구가 맞은편·옆에서 찍어준 컷, 걸어가다 멈춘 순간, 진열대 구경, 벤치에서 기다리는 옆모습, 거울 셀카** 중심으로 재작성 |
| 장소 | 강변·세탁소·플랫폼 등 억지 상황 | **동네 식당·카페 창가·낮 공원 벤치·구제숍·지하철 벤치·서점 잡지 코너·엘리베이터** 등 실제로 사진이 남는 자리 |
| 불완전함 | 없음 | 모든 프롬프트에 **흔들린 프레이밍·피사체 비중앙·모공·폰 노이즈** 문장 강제 삽입 |
| 조합 정합성 | 실내/실외만 맞춤 | 구도별로 **가능한 장소를 명시**(`place_ids`) — 식탁 스냅이 서점에 붙는 식의 모순 차단 |

## 카테고리 풀

| 카테고리 | 개수 | 내용 |
| --- | --- | --- |
| `no_face_scenes` | 16 | 말차 디저트·서점 서가·밤 자판기 골목·아침 책상·전철 창밖·장바구니·신발 OOTD·동전 세탁소·비 오는 창가·식당 테이블·편의점 계산대 등 (장면마다 조명 고정) |
| `hairstyles` | 14 | 센터 가르마(앞머리 없음)·사이드 스웹트·높은 포니테일·로우 번·하프업·자연 웨이브·비니·베레모·볼캡·사이드 브레이드·단발 보브·샤워 후 물기 등 |
| `clothing` | 14 | 후드+조거·스트라이프 옥스포드·트렌치·데님 자켓·플로럴 원피스·가죽 자켓·파자마·가디건+롱스커트·오트밀 니트+와이드 연청·트레이닝·울코트 등 |
| `person_shots` | 12 | 친구가 식탁 맞은편에서 찍은 컷·한 입 먹기 직전·걸어가다 멈춘 순간·3/4 뒷모습·거울 셀카(최신 아이폰 노출)·진열대 구경·벤치에서 기다리기·폰 보는 옆모습·어깨너머·멀리서 찍은 스냅·창가 옆얼굴·자전거 오르기 |
| `places_person` | 14 | 동네 식당·카페 창가·낮 공원 벤치·구제숍·지하철 플랫폼 벤치·엘리베이터 거울·서점 잡지 코너·주택가 골목·편의점 앞·세탁소·전철 좌석·주방·횡단보도·레코드숍 (실내/실외 + 가능한 조명 목록 포함) |
| `expressions` | 7 | 나른함·옅은 미소·눈웃음·졸린 눈·생각하는 표정·삐죽·말하다 만 입 모양 |
| `devices` | 5 | 아이폰 15 프로·16 프로·15 프로 3배·16 프로 3배·15 프로 초광각 **(최신 기기만)** |
| `imperfections` | 8 | 기울어진 프레이밍·지나가는 사람 어깨가 프레임에 걸림·핀이 살짝 뒤로·손 모션블러·정수리가 프레임 끝·한쪽 과노출 등 |
| `lighting` | 8 | 형광등·흐린 날 확산광·창가+실내 혼합·아이폰 플래시·편의점 형광등·지하철 형광등·밤 가로등·카페 스탠드 (골든아워·네온·시네마틱 없음) |

## 핵심 규칙

1. **배치 내 중복 금지** — 헤어·의상·구도·장소는 한 배치(12컷) 안에서 서로 겹치지 않게 뽑습니다. 8컷이면 헤어 8종, 의상 8종이 전부 다릅니다.
2. **모순 조합 방지** — 조명은 장소에 맞는 후보 중에서만 뽑고, 구도에 `place_ids`가 있으면 그 장소 안에서만 고릅니다(식탁 스냅×서점, 거울 셀카×공원 같은 조합이 나오지 않음).
3. **최신 아이폰 고정** — 카메라 풀에 구형 기기·폴라로이드·필름이 없습니다. 거울 셀카는 `device_force`로 최신 Pro가 강제되고, 폰 뒷면 3구 카메라 묘사가 프롬프트에 붙습니다.
4. **불완전함 강제** — 모든 컷에 `Everyday and imperfect:` 문장(기울기·비중앙·모션블러 등)과 `Real skin with visible pores ... no beauty retouching, no skin smoothing, no glow`가 들어갑니다.
5. **AI 화보어 금지** — `meta.banned_keywords` 15개를 `--check`가 검사합니다. `cinematic`·`bokeh`·`8k`·`masterpiece`·`perfect skin` 같은 단어가 프롬프트에 남으면 exit code 2로 실패합니다.
6. **정면 응시 최소화** — 인물 구도 12종 중 정면 카메라 응시는 0종. 시선이 접시·폰·친구·진열대로 향합니다.
7. **얼굴만 유지** — 프롬프트 끝에 `Do not reproduce the reference pose, outfit, hairstyle or background.` 를 붙여 레퍼런스의 시스루 뱅·오프숄더 니트가 따라오지 않게 합니다.

## v3 glamour 모드 (2026-11-16)

노출·바이럴 컷 전용 모드입니다. 수영복·짐웨어·호텔/료칸/리조트 맥락 안에서만 노출을 다루고, 언더웨어·란제리 맥락은 쓰지 않습니다.

- **`--mode glamour`** — `pools.json`의 `glamour` 섹션(헤어 8 · 의상 8 · 구도 8 · 장소 8 · **룩 8**)에서 뽑습니다.
- **룩(look) 단위 추출** — 옷과 장소가 강하게 묶여 있어 `glamour.looks`가 `shot`·`place`·`clothing`·`hairstyles` id를 한 묶음으로 정의합니다. 수영복이 필라테스 거울에 붙는 식의 모순이 구조적으로 차단됩니다.
- **안전 검사** — `meta.safety_banned_keywords` 12개(`lingerie`·`underwear`·`panties`·`topless`·`nude`·`naked`·`nipple`·`cleavage`·`erotic`·`seductive`·`bedroom eyes`·`lingerie set`)를 `--check`가 함께 스캔하고, 하나라도 걸리면 exit 2.
- **새 룩 추가** — `pools.json`의 `glamour.looks`에 한 줄 넣으면 됩니다:

```json
{ "id": "g_look_pool_night", "ko": "야간 풀", "shot": "g_pool_step_laugh", "place": "g_pool_villa",
  "clothing": ["g_ivory_bikini_towel"], "hairstyles": ["g_wet_back"] }
```

```bash
python3 generate_prompts.py --mode glamour --person 8 --check \
    --json examples/seed_20261116_glamour.json --markdown examples/seed_20261116_glamour.md
# → check: clean (15 AI-gloss phrases + 12 safety phrases scanned)
```

## 사용법

```bash
# 기본: 노페이스 4 + 인물 8 = 12컷, 시드 20261116 (+ 금지어 검사)
python3 generate_prompts.py --check

# 시드·컷 수 지정, JSON/표로 저장
python3 generate_prompts.py --seed 20261116 --noface 4 --person 8 \
    --json out/prompts.json --markdown out/prompts.md --check

# 총 6컷만 (노페이스 2 + 인물 4)
python3 generate_prompts.py --seed 42 --count 6

# 여러 시드의 스타일 지문 미리 보기
python3 generate_prompts.py --list-seed 5
```

출력 예 (v2.1):

```
[05] (person) 베레모 착용 · 트레이닝 세트 + 스니커즈 · 어깨 너머로 부르는 듯한 클로즈업 · 도쿄 주택가 골목길
    A real amateur phone photo for an Instagram feed, taken on an iPhone 16 Pro 3x telephoto lens...
    Everyday and imperfect: there is slight motion blur on her hand. Real skin with visible pores ...
    Vertical 4:5. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark.
```

```
check: clean (15 AI-gloss phrases + 12 safety phrases scanned)
```

## 이미지 생성으로 이어 붙이기

- **노페이스 컷:** `images '<prompt>' --out work/mio_v2/raw/xx.jpg`
- **인물 컷:** `images '<prompt>' --edit downloads/mio_master_clean.jpg --out work/mio_v2/raw/xx.jpg`
  (`mio_master_clean.jpg` = `338.jpg` 정면 마스터 크롭본)
- 생성 후 **반드시 눈으로 검수**: ① AI/CG 광택이 나는지 ② 거울 셀카에 구형 아이폰이 잡혔는지 ③ 포즈가 억지스러운지 ④ 손가락·배경 글자가 깨졌는지. 걸리면 해당 컷만 프롬프트를 고쳐 재생성하고 최종 프롬프트를 `mio_feed_v2/README.md`에 남깁니다.
- 4:5가 아닌 결과는 1080×1350 크롭으로 통일합니다(피사체 머리·손이 잘리지 않는 위치에서 크롭).

## 새 카테고리 아이템 추가

`pools.json` 배열에 항목을 하나 더 넣으면 됩니다.

```json
{ "id": "bucket_hat", "ko": "버킷햇", "en": "a faded denim bucket hat pulled low, hair tucked behind the ears" }
```

`places_person`은 `io`(`in`/`out`)와 `lights`(가능한 조명 목록)를 함께 넣고, 인물 구도에 특정 장소가 필요하면 `place_ids`에 `places_person`의 id를 넣습니다. 카메라는 최신 아이폰만 추가하세요 — 구형 기기나 필름 카메라는 이 풀의 목적(AI 티 제거)과 반대입니다.
