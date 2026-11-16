# 🇰🇷 미오(Mio) — 서울 사는 일본인 · 노페이스 일상 3컷 `@_3io.log_`

기운님 피드백 ①(2026-11-16) — *"근데 책은 좀 그렇지않나 글자 완벽하지않을거아냐 ai 생성이 그리고 일본인인데 한국사는게 요즘 유행같던데"*
기운님 피드백 ②(2026-11-16) — *"에어팟이랑 토마토 둘다 이상하잖아 제대로 검수란하냐 그리고 한글로도써야지"*

→ **2026-11-16 v3.2**: 3컷을 **전부 다시 뽑았습니다.** ① 뭉개지기 쉬운 소품(에어팟 케이스·반쪽 과일·커틀러리·선글라스·근거리 자전거)을 장면에서 제거 ② 캡션·해시태그를 **한국어 우선 + 일본어 병기**로 교체.

- **제작 방식:** `../prompt_randomizer/` (v3.2 풀) + `images` CLI. 순수 장면 생성(레퍼런스·사람 없음)
- **규격:** 전 컷 1080×1350 (4:5) · 텍스트·워터마크 없음
- **컨택트시트:** [`mio_seoul_grid.jpg`](mio_seoul_grid.jpg)

## 1. 이번에 뭘 바꿨나 (v3.2)

| 컷 | 문제였던 것 | 확대해서 보면 | 조치 |
| --- | --- | --- | --- |
| 01 | 에어팟 케이스 + 접시 위 반쪽 딸기 | 케이스가 경첩 없는 **비누 덩어리**, 딸기가 **정체불명 붉은 덩어리**로 뭉개짐 | 소품 전면 배제 → 아이스 아메리카노(손잡이 없는 흰 컵) + 버터 토스트 한 조각 + 냅킨만 |
| 02 | 선글라스 | 브리지에 **렌즈가 하나 더 붙어** 세 눈처럼 보임 | 선글라스 제거 후 재생성 |
| 03 | 자전거·배달 스쿠터 | **프레임·포크·핸들 축이 어긋나** 형태가 성립하지 않음 | 근거리 자전거·스쿠터 제거 후 재생성 |

**금지 소품 (v3.2 신규)** — 손가락 다음으로 AI가 자주 망가뜨리는 것은 *작고 윤곽이 복잡한 사물*입니다.

| 배제 | 대체 |
| --- | --- |
| 무선 이어폰 케이스·에어팟 | 없음(테이블 비우기) |
| 폰·충전기·소형 전자기기(테이블 위) | 컵·접시·천 |
| 반쪽 딸기·토마토·베리류 | 통과일 1개 또는 과일 없이 |
| 포크·나이프·스푼 | 커틀러리 없이 |
| 선글라스 | 선글라스 없이 |
| 근거리 자전거·스쿠터 | 실루엣이 먼 배경이면 허용 |

프롬프트에는 아래 문장이 강제로 들어가고, `pools.json`의 `meta.mandatory_no_small_props` + `banned_subjects` 26개를 `--check`가 검사합니다.

```txt
Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces,
no fruit, no berries, no half-cut fruit, no fork, no knife, no spoon, no cutlery.
```

## 2. 3컷 목록

| # | 파일 | 장면 | 핵심 소품 | 조명 | 카메라 |
| --- | --- | --- | --- | --- | --- |
| 01 | `01_seoul_morning_table.jpg` | 서울 원룸 창가 아침 테이블 (창밖 서울 기와지붕·벽돌집·아파트) | 아이스 아메리카노(손잡이 없는 흰 컵) · 버터 토스트 한 조각 · 베이지 냅킨 | 흐린 아침 창가 빛 | iPhone 15 Pro |
| 02 | `02_seoul_cafe_dessert.jpg` | 성수동 카페 창가 테이블 | 아이스 아메리카노 · 바스크 치즈케이크 · 엎어둔 폰 · 종이냅킨 · 물컵 | 늦은 오후 창가 빛 + 약한 전구 | iPhone 16 Pro |
| 03 | `03_seoul_evening_street.jpg` | 서울 주택가 골목 저녁 (기와지붕 집·벽돌 담장) | 골목 끝 지나가는 시내버스 · 가로등 · 파란 재활용함 · 화분 | 해질녘 가로등 불빛 | iPhone 15 Pro |

- **01**은 Day 1 첫 게시물. 얼굴 0컷으로 "서울에서 혼자 사는 사람"의 아침을 먼저 보여줍니다.
- **02**는 Day 3 피드. 성수·연남 감성 카페.
- **03**은 Day 2 스토리·Day 4 피드. 간판이 하나도 없는 주택가라 확대해도 깨질 글자가 없습니다.

## 3. 프롬프트 원문 (v3.2 재생성분 · 재현용)

<details><summary><b>01</b> · 서울 원룸 창가 아침 테이블 (v3.2)</summary>

```txt
A real amateur phone photo for an Instagram feed, taken on an iPhone 15 Pro main camera. Scene: a small round wooden table pushed against the window of a tiny Seoul one-room studio apartment on an overcast winter morning. On the table there are only three things: a plain handleless white ceramic tumbler filled with iced americano, a few ice cubes floating at the top and light condensation on the outside; a plain white round ceramic plate holding one single square slice of buttered toast, nothing else on the plate; and a crumpled beige cotton napkin beside the plate. The wood surface is clean and dry with no stains, no rings and no marks. Outside the window, seen through slightly dirty glass and a half-drawn grey roller blind, ordinary low-rise Seoul villa houses with dark tiled roofs and a few pale apartment blocks in the middle distance, bare winter trees; every building surface is plain concrete or brick with no shop signs, no banners, no lettering and no numbers anywhere. Flat cool overcast morning daylight from the window, the sky white and blown out at the top of the frame. Everyday and imperfect: the framing is slightly crooked, the cup sits off-centre near the right frame edge. Natural phone noise, ordinary exposure, realistic texture, plain muted colour. Vertical 4:5. Absolutely no text, no letters, no numbers, no signage, no logos, no labels, no book, no magazine, no paperwork, no screen, no watermark, no face, no people, no hands, no earbuds, no earbud case, no electronics, no phone, no fruit, no berries, no fork, no knife, no spoon, no cutlery.
```

</details>

<details><summary><b>02</b> · 성수동 카페 테이블 (v3.2, 선글라스 제거)</summary>

```txt
A real amateur phone photo for an Instagram feed, taken on an iPhone 16 Pro main camera. Scene: a worn wooden table for two in a small corner cafe in Seongsu-dong, Seoul, late afternoon. On the table: a tall clear glass of iced americano with ice and light condensation and a thin cardboard coaster under it, a small square slice of plain basque cheesecake with a toasted dark top sitting alone on a plain cream ceramic plate, a smartphone lying face down so only its dark back and its square camera bump are visible, a crumpled paper napkin, a small plain glass of water. No sunglasses anywhere, no cutlery anywhere. The wall behind is plain painted concrete with a faint soft shadow of a plant; a plain beige linen curtain at the side; no menu board, no posters, no price signs, no lettering on any surface; one bare bulb hanging far in the back room. Flat late-afternoon daylight from a large window on the left, mixed with the dim warm bulb. Everyday and imperfect: part of a chair back blocks the bottom corner, the verticals lean a little and the table sits off-centre. Natural phone noise, ordinary exposure, realistic texture, plain muted colour. Vertical 4:5. Absolutely no text, no letters, no numbers, no signage, no logos, no labels, no book, no magazine, no screen content, no watermark, no face, no people, no hands.
```

</details>

<details><summary><b>03</b> · 서울 주택가 골목 저녁 (v3.2, 자전거·스쿠터 제거)</summary>

```txt
A real amateur phone photo for an Instagram feed, taken on an iPhone 15 Pro main camera. Scene: a quiet narrow residential alley in a Seoul neighbourhood at dusk, photographed from several steps back at eye level. Low brick and concrete walls, a small stucco house with a tiled roof, a blue plastic recycling bin, a few potted plants on a concrete stoop, one street lamp just switched on casting a small pool of light, damp patches on the asphalt, overhead cables. The alley is empty of people and vehicles except a city bus far away at the end, passing as a soft blur. Every wall, shutter and surface is plain and empty with no shop signs, no banners, no posters, no address plates, no lettering and no numbers anywhere in the frame. Dim blue-grey dusk light with the single street lamp, the sky still pale above the roofline. Everyday and imperfect: the framing is slightly tilted, a downpipe cuts the left edge, the far end is a little soft. Natural phone noise, ordinary exposure, realistic texture, plain muted colour. Vertical 4:5. Absolutely no text, no letters, no numbers, no signage, no logos, no labels, no watermark, no people close to the camera, no face, no bicycle, no scooter, no motorbike, no parked cars.
```

</details>

## 4. 캡션 & 해시태그 — 한국어 우선 + 일본어 병기 (v3.2)

| Day | 컷 | 캡션 (KR + JP) | 첫 댓글 태그 |
| --- | --- | --- | --- |
| 1 | `01_seoul_morning_table` | 서울에서 혼자 살고 있는 일본인 미오예요☕️<br />아침엔 보통 이 자리에서 커피 마셔요.<br />はじめまして。ソウルで暮らしている日本人、澪です☕️ | A′ |
| 2 | `01` 크롭 + `03` | 좋은 아침☀️ / 귀갓길 이 언덕, 꽤 좋아<br />おはよう☀️ / 帰り道のこの坂、けっこう好き | – |
| 3 | `02_seoul_cafe_dessert` | 서울 카페는 케이크가 커. 행복해🍰<br />ソウルのカフェ、ケーキが大きい。しあわせ🍰 | A′ |
| 4 | `mio_v2_01_noface_dessert`(말차) / 스토리 `02` 크롭 | 말차 계절, 아직 끝나지 않았으면 좋겠어🍵<br />抹茶の季節、まだ終わらないでほしい🍵 | A′ |

**SET A′ (Day 1~4 기본 · v3.2 한국어 태그 추가)**

```txt
#서울일상 #한국생활 #서울자취 #서울카페 #일본인 #일상기록 #ソウル生活 #韓国暮らし #_3iolog
```

한국어 태그 6개(서울일상·한국생활·서울자취·서울카페·일본인·일상기록)로 국내 유입을 열고, 일본어 태그 2개로 원래 타깃을 유지합니다. 계정 전용 태그 `#_3iolog`는 고정.

## 5. 검수 노트 (2026-11-16 v3.2)

전 컷 `read_file`로 **원본 전체 + 소품별 100% 확대 크롭** 두 단계로 육안 검수했습니다. 「확대 크롭」은 컵·접시·음식·냅킨·테이블 위 소품·창밖 풍경을 각각 잘라 1000px 이상으로 키워 확인한 것입니다.

| 컷 | 이번 검수 | 결과 |
| --- | --- | --- |
| 01 | 컵(1162px)·접시/토스트·냅킨·창밖 4개 크롭. 뭉개진 물체 0, 컵 손잡이 없음(형태 성립), 토스트·냅킨 결 정상, 창밖 기와지붕·벽돌집에 글자 0 | **통과** |
| 02 | 글래스·케이크·폰 카메라 범프·냅킨·창밖 크롭. 선글라스 없음, 케이크에 뭉개진 덩어리 없음, 폰 카메라 모듈 형태 유지 | **통과** |
| 03 | 재활용함·골목 끝 버스·기와지붕·담장 크롭. 자전거·스쿠터 없음, 버스는 모션블러로 노선번호 판독 불가, 벽면 글자 0 | **통과** |

**폐기한 후보(참고)** — 01 1차(에어팟 케이스 비누화 + 딸기 뭉개짐), 01 후보B(컵 손잡이가 납작한 날처럼 뭉개짐), 01 후보C·D(창틀 아래에 실내외가 겹쳐 보이는 기하 오류, 크루아상 버전은 창밖에 파란 물체가 떠 보임), 02 1차(선글라스 세 눈), 03 1차(자전거 프레임 어긋남). 모두 버리고 위 3컷으로 확정했습니다.

**공통 확인**

- **가짜 글자:** 3컷 모두 프레임 안에 읽히는 글자 0. 창밖 건물(01)·골목 벽면(03)·카페 벽(02) 확대 크롭에서도 간판·주소판·포스터 없음.
- **뭉개지는 소품:** 에어팟·소형 전자기기·작은 과일·커틀러리·선글라스·근거리 자전거 0.
- **책:** 0컷.
- **AI 광택:** 3컷 모두 흐린 날 확산광·형광등 계열. 피부·금속 과광 없음, 화보 보케 없음, 폰 노이즈 유지.
- **규격:** 전 컷 1080×1350 (4:5).

## 6. 사용 규칙

- 얼굴 컷을 만들 때는 `338.jpg`(0도 수평 정면 마스터) 크롭본 `mio_master_clean.jpg`를 `--edit` 베이스로 씁니다.
- **노페이스·인물 컷 모두 책·간판·메뉴판·영수증·라벨·뭉개지는 소품을 넣지 않습니다.** 프롬프트에는 `prompt_randomizer`의 `meta.mandatory_no_text` + `meta.mandatory_no_small_props` 문장을 그대로 붙이고 `--check`로 검사합니다.
- 새 컷은 `prompt_randomizer/generate_prompts.py`로 뽑고, 생성 후 **두 번 탭 확대** 기준으로 글자·손가락·소품을 확인합니다.
- 업로드 순서·캡션·해시태그는 노션 가이드의 **Day 1~4 교체본(v3.2)**을 따릅니다.
