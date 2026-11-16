# 🇰🇷 미오(Mio) — 서울 사는 일본인 · 노페이스 일상 3컷 `@_3io.log_`

기운님 피드백 — *"근데 책은 좀 그렇지않나 글자 완벽하지않을거아냐 ai 생성이 그리고 일본인인데 한국사는게 요즘 유행같던데"*

→ **2026-11-16 v3.1**: 콘셉트를 **"도쿄 혼자 사는 일본인" → "한국(서울)에 거주하는 일본인 미오(Mio)"** 로 전환하고,
**펼친 책·책등·간판·메뉴판처럼 확대하면 AI 가짜 글자가 들통나는 피사체를 전면 배제**한 노페이스 일상 3컷을 새로 만들었습니다.

- **제작 방식:** `../prompt_randomizer/` (v3.1 풀) + `images` CLI. 순수 장면 생성(레퍼런스·사람 없음)
- **규격:** 전 컷 1080×1350 (4:5) · 텍스트·워터마크 없음
- **컨택트시트:** [`mio_seoul_grid.jpg`](mio_seoul_grid.jpg)

## 1. 왜 책·글자를 뺐나

v2의 `02_noface_bookstore`(책등 클로즈업)와 `04_noface_morning_desk`(펼친 책)는 축소하면 멀쩡하지만,
**인스타에서 두 번 탭해 확대하면 가짜 글자가 바로 드러납니다.** 페이지 위에 의미 없는 획이 빼곡히 박혀 있고
문장이 성립하지 않아서, 계정 신뢰에 치명적입니다. 그래서 v3.1부터는 아래를 **노페이스·인물 컷 전부에서** 제외했습니다.

| 배제 피사체 | 이유 |
| --- | --- |
| 펼친 책·노트·잡지·신문 | 본문 글자가 100% 가짜 글리프로 나옴 |
| 서가·책등 클로즈업 | 책등 제목이 전부 깨짐 |
| 간판·메뉴판·가격표·영수증 | 한글·일본어 획이 뭉개지고 오탈자처럼 보임 |
| 포장재 라벨·로고 | 브랜드 왜곡 + 가짜 글자 |

대신 **컵·접시·음식·가구·창밖 풍경·골목·가로등·자전거**처럼 글자가 원래 없는 피사체로 장면을 채웠습니다.
프롬프트에는 `No printed words anywhere in the frame ...` 문장이 강제로 들어가고, `--check`가 `meta.banned_subjects` 15개를 검사합니다.

## 2. 3컷 목록

| # | 파일 | 장면 | 핵심 소품 | 조명 | 카메라 |
| --- | --- | --- | --- | --- | --- |
| 01 | `01_seoul_morning_table.jpg` | 서울 원룸 창가 아침 테이블 (창밖 서울 빌라·아파트) | 아이스 아메리카노 머그 · 버터 토스트 · 딸기 반쪽 · 흰 이어폰 케이스 | 흐린 아침 창가 빛 | iPhone 15 Pro |
| 02 | `02_seoul_cafe_dessert.jpg` | 성수동 카페 창가 테이블 | 아이스 아메리카노 · 바스크 치즈케이크 · 선글라스 · 엎어둔 폰 · 물컵 | 늦은 오후 창가 빛 + 약한 전구 | iPhone 16 Pro |
| 03 | `03_seoul_evening_street.jpg` | 서울 주택가 골목 저녁 (기와 roof 집·벽돌 담장) | 골목 끝 지나가는 시내버스 · 가로등 · 자전거 · 파란 재활용함 | 해질녘 가로등 불빛 | iPhone 15 Pro |

- **01**은 Day 1 첫 게시물용. 얼굴 0컷으로 "서울에서 혼자 사는 사람"의 아침을 먼저 보여줍니다.
- **02**는 3일차 피드용. 성수·연남 감성 카페.
- **03**은 2일차 스토리·4일차 피드용. 간판이 하나도 없는 주택가라 확대해도 깨질 글자가 없습니다.

## 3. 프롬프트 원문 (재현용)

<details><summary><b>01</b> · 서울 원룸 창가 아침 테이블</summary>

```txt
A real amateur phone photo for an Instagram feed, taken on an iPhone 15 Pro main camera. Scene: a small round wooden table pushed against the window of a tiny Seoul one-room studio apartment, morning. On the table: a plain unbranded ribbed ceramic mug of iced americano with condensation and ice still visible, a plain white wireless earbud case with no logo lying beside it, a small white plate holding one slice of buttered toast and half a strawberry, a crumpled beige cotton napkin. Outside the window, seen through slightly dirty glass and a half-drawn blind, ordinary low-rise Seoul villa houses and a few pale apartment blocks in the middle distance with a bare tree; every building surface is plain concrete or brick with no shop signs, no banners, no lettering and no numbers anywhere. Flat cool overcast morning daylight from the window. Everyday and imperfect: the framing is slightly crooked, the mug sits off-centre and part of it is near the frame edge, the top right corner is overexposed by the window, there are a couple of water rings on the wood. Natural phone noise, ordinary exposure, realistic texture, plain muted colour. Vertical 4:5. Absolutely no text, no letters, no numbers, no signage, no logos, no labels, no book, no magazine, no paperwork, no screen content, no watermark, no face, no people, no hands.
```

</details>

<details><summary><b>02</b> · 성수동 카페 테이블 (1차본 폐기 후 재생성)</summary>

```txt
A real amateur phone photo for an Instagram feed, taken on an iPhone 16 Pro main camera. Scene: a worn wooden table for two in a small corner cafe in Seongsu-dong, Seoul, late afternoon. On the table: a tall clear glass of iced americano with ice and condensation, a small square slice of basque cheesecake sitting alone on a plain cream ceramic plate, a pair of folded black sunglasses, a smartphone lying face down so only its dark back and its camera bump are visible, a crumpled paper napkin, a small glass of water. No cutlery anywhere on the table. The wall behind is plain painted concrete with a faint shadow of a plant; a plain beige linen curtain at the side; no menu board, no posters, no price signs, no lettering on any surface, one bare bulb hanging far in the back room. Flat late-afternoon daylight from a large window on the left, mixed with the dim warm bulb. Everyday and imperfect: part of a chair back blocks the bottom corner, the glass leaves a wet ring on the wood, the verticals lean a little and the table sits off-centre. Natural phone noise, ordinary exposure, realistic texture, plain muted colour. Vertical 4:5. Absolutely no text, no letters, no numbers, no signage, no logos, no labels, no book, no magazine, no screen content, no watermark, no face, no people, no hands.
```

</details>

<details><summary><b>03</b> · 서울 주택가 골목 저녁</summary>

```txt
A real amateur phone photo for an Instagram feed, taken on an iPhone 15 Pro main camera. Scene: a quiet narrow residential alley in a Seoul neighborhood at dusk, photographed from several steps back at eye level. Low brick and concrete walls, a small stucco house with a tiled roof, a blue plastic recycling bin, a few potted plants on a concrete stoop, a parked city bicycle and a small delivery scooter leaning against a wall, one street lamp just switched on casting a small pool of light, damp patches on the asphalt, overhead cables. At the far end the alley opens onto a wider road where a city bus passes as a soft blur. Every wall, shutter and surface is plain and empty with no shop signs, no banners, no posters, no address plates, no lettering and no numbers anywhere in the frame. Dim blue-grey dusk light with the single street lamp, the sky still pale above the roofline. Everyday and imperfect: the framing is slightly tilted, a downpipe cuts the left edge, the top of a wall is close to the frame edge, the far end is a little soft. Natural phone noise, ordinary exposure, realistic texture, plain muted colour. Vertical 4:5. Absolutely no text, no letters, no numbers, no signage, no logos, no labels, no watermark, no people close to the camera, no face.
```

</details>

## 4. 검수 노트 (2026-11-16)

전 컷 `read_file`로 직접 열어 **원본 크기 + 부분 확대 크롭** 두 단계로 육안 검수했습니다.

| 컷 | 1차 결과 | 조치 |
| --- | --- | --- |
| 01 | 글자·책 0, 창밖 서울 빌라/벽돌집 자연스러움. 컵·이어폰 케이스 확대해도 로고·글자 없음 | **1차 통과** |
| 02 | 전체 인상은 좋으나 **포크가 접시와 케이크 사이에서 형체가 깨짐**(날과 자루가 따로 놀고, 자루가 하나 더 있는 것처럼 보임) | **폐기 → 재생성.** 테이블에서 **커틀러리 전면 제거**(`No cutlery anywhere on the table.`) 후 통과 |
| 03 | 간판 0, 기와 roof·벽돌 담장·파란 재활용함으로 서울 주택가 느낌 확실. 골목 끝 버스는 모션블러라 노선번호 판독 불가 | **1차 통과** |

**공통 확인**

- **가짜 글자:** 3컷 모두 프레임 안에 읽히는 글자 0. 창밖 건물(01)·골목 벽면(03)·카페 벽(02) 확대 크롭에서도 간판·주소판·포스터 없음.
- **책:** 0컷. 01의 테이블은 컵·접시·케이스·냅킨뿐.
- **AI 광택:** 3컷 모두 흐린 날 확산광·형광등 계열. 피부·금속 과광 없음, 화보 보케 없음, 폰 노이즈 유지.
- **카메라:** 02의 폰 뒷면을 확대해 삼각 배치 렌즈 + 카메라 플레이트 확인(구형 단일 렌즈 아님).
- **규격:** 전 컷 1080×1350 (4:5).

## 5. 사용 규칙

- 얼굴 컷을 만들 때는 `338.jpg`(0도 수평 정면 마스터) 크롭본 `mio_master_clean.jpg`를 `--edit` 베이스로 씁니다.
- **노페이스·인물 컷 모두 책·간판·메뉴판·영수증·라벨을 넣지 않습니다.** 프롬프트에는 `prompt_randomizer`의 `meta.mandatory_no_text` 문장을 그대로 붙이고 `--check`로 검사합니다.
- 새 컷은 `prompt_randomizer/generate_prompts.py`로 뽑고, 생성 후 **두 번 탭 확대** 기준으로 글자·손가락·소품을 확인합니다.
- 업로드 순서·캡션·해시태그는 노션 가이드의 **2일차~4일차 서울 계획표**를 따릅니다.
