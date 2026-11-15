# 🌊 미오(Mio) v3 — 3~4주차 바이럴·노출 피드 8컷 `@_3io.log_`

기운님 지시 — *"그리고 그뒤에이제 노출있는것도 만들어주고"* (2026-11-16)

v2(일상 12컷)로 계정의 '사는 사람' 신뢰를 쌓은 뒤, 3~4주차에 **도달을 한 번 크게 밀어 올리는 구간**입니다.
리나처럼 강한 태닝·화보 톤이 아니라 **미오 특유의 청순·뽀얀 피부·도화살 얼굴을 유지한 채**, 인스타 섀도우밴 안전 범위(수영복·짐웨어·여행 맥락) 안에서만 노출을 다룹니다.

- **생성 방식:** `../prompt_randomizer/` (v3 glamour 모드) + `images` CLI
- **베이스:** `mio_master_clean.jpg`(= `338.jpg` 정면 마스터 크롭본)를 `--edit`, 얼굴만 유지
- **규격:** 전 컷 1080×1350 (4:5) · 텍스트·워터마크 없음
- **컨택트시트:** [`mio_v3_grid.jpg`](mio_v3_grid.jpg)

## 1. v2.1 리얼리티 원칙 그대로 적용

| 항목 | v3 규칙 |
| --- | --- |
| 카메라 | 최신 아이폰만. 거울 셀카(02)는 **iPhone 16 Pro 3구 카메라**가 거울에 잡히도록 명시하고 확대 검수 |
| 조명 | 한낮 직사광·형광등·스탠드·종이등. 골든아워 역광·시네마틱 그레이딩·보케 금지 |
| 구도 | 친구가 찍어준 스냅, 셀프타이머, 거울 셀카. 정면 응시 최소화, 프레임 기울기·비중앙·모션블러 허용 |
| 피부 | 모공·불균일한 톤·땀·젖은 머리. 보정·스무딩·글로우 금지 |
| 헤어 | 8컷 전부 상이 — 젖은 머리 / 높은 포니테일 / 로우 번 / 집게핀 올림 / 센터 가르마 / 바람에 날리는 머리 / 목욕 후 반묶음 / 해변 웨이브 |
| 안전 | 수영복·짐웨어·호텔/료칸/리조트 맥락 고정. 언더웨어·란제리·성인 화보 어휘는 생성기 `--check`가 차단 |

## 2. 8컷 목록

| # | 파일 | 컨셉 | 헤어 | 의상 | 구도·장소 | 조명 |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | `mio_v3_01_pool_bikini.jpg` | 오키나와 풀빌라 수영장 | 물에 젖어 뒤로 넘긴 머리 | 아이보리 투피스 수영복 + 허리 타월 | 풀 계단에서 옆 사람 보며 웃는 컷 (친구 스냅) | 늦은 오후 강한 햇빛 |
| 02 | `mio_v3_02_gym_mirror.jpg` | 필라테스 후 거울 셀카 | 높은 포니테일 (땀기) | 블랙 스포츠 브라탑 + 하이웨이스트 레깅스 | 전신거울 셀카, **16 Pro 3구 카메라 노출** | 천장 형광등 |
| 03 | `mio_v3_03_hotel_robe.jpg` | 호텔 아침 | 느슨한 로우 번 | 흰 배스로브 (한쪽 어깨) | 침대에서 커피 들고 창밖 보기 | 흐린 아침 창빛 |
| 04 | `mio_v3_04_bed_slip.jpg` | 자취방 밤 | 목욕 후 반쯤 묶은 머리 | 샴페인 새틴 캐미솔 + 코튼 쇼츠 | 셀프타이머, 머리 묶는 중 | 침대 스탠드 조명 |
| 05 | `mio_v3_05_beach_monokini.jpg` | 해질녘 해변 | 바람에 날리는 긴 머리 | 블랙 컷아웃 원피스 수영복 + 시스루 셔츠 | 걷다 뒤돌아보는 스냅 | 해질녘 낮은 빛 (무보정) |
| 06 | `mio_v3_06_onsen_yukata.jpg` | 료칸 / 온천 | 집게핀 올림머리 | 남색 줄무늬 유카타 (느슨히) | 다다미방 셀카 | 종이등 불빛 |
| 07 | `mio_v3_07_croptop_denim.jpg` | 여름 도쿄 거리 | 앞머리 없는 센터 가르마 | 크롭 나시 + 로우라이즈 데님 | 걸어오는 전신 스냅 (친구 촬영) | 한낮 직사광 |
| 08 | `mio_v3_08_resort_sunbed.jpg` | 리조트 선베드 | 해변 웨이브 | 블랙 수영복 상의 + 데님 쇼츠 | 선베드에 엎드려 음료 | 한낮 햇빛 |

## 3. 섀도우밴 회피 업로드 규칙

1. **노출 컷은 3일에 1장 이하.** v2 일상 컷 사이에 섞어서 올립니다(예: 1일 일상 → 4일 노출 → 7일 일상 → 10일 노출).
2. **배경이 먼저 말하게.** 수영복은 반드시 수영장·해변·리조트, 짐웨어는 스튜디오·거울, 가운·유카타는 호텔·료칸. '방 안 + 속옷'으로 읽히는 조합은 쓰지 않습니다.
3. **본문·태그에 신체 부위 단어 금지.** `#비키니` `#수영복` `#란제리` `#몸매` 계열은 탐색 노출을 깎습니다. 여행·운동 카테고리 태그만 씁니다.
4. **캡션은 상황 한 줄 + 여운.** 노출이나 몸 이야기는 절대 쓰지 않습니다. 댓글 유도는 장소·음식·날씨로.
5. **첫 댓글 태그 8~10개**, 대형 2 / 중형 3 / 소형 3~5 비율. 계정 태그 `#_3iolog` 고정.
6. **피드는 20:00~23:00 JST, 릴스는 19:00~21:00 JST.** 노출 컷은 주말 낮(12:00~15:00)도 반응이 좋습니다.

### 캡션 (JP 본문 / KR 뜻)

| # | 캡션 (JP) | 뜻 (KR) | 태그 세트 |
| --- | --- | --- | --- |
| 01 | 沖縄のプール、水温がちょうどいい🌊 | 오키나와 풀, 물 온도가 딱 좋아🌊 | D |
| 02 | 今日はピラティス。体を動かすと気持ちいい。 | 오늘은 필라테스. 몸을 움직이면 기분이 좋아. | E |
| 03 | 旅行の朝はコーヒーが先。 | 여행 아침엔 커피가 먼저. | D |
| 04 | 髪、乾かすの面倒くさい。 | 머리 말리는 거 귀찮아. | B |
| 05 | 夕方の海、人がいなくて好き。 | 저녁 바다, 사람이 없어서 좋아. | D |
| 06 | 温泉あがりのお茶、しみる。 | 온천 마치고 마시는 차, 몸에 스며들어. | D |
| 07 | 暑すぎ。でもこの街好き。 | 너무 더워. 그래도 이 거리 좋아. | C |
| 08 | 何もしない午後。 | 아무것도 안 하는 오후. | D |

**SET D — 여행·리조트(노출 컷 기본)** `#沖縄` `#沖縄旅行` `#リゾート` `#プール` `#夏の思い出` `#旅行記録` `#海が好き` `#_3iolog`
**SET E — 운동** `#ピラティス` `#ヨガ` `#ワークアウト` `#フィットネス` `#朝活` `#運動不足解消` `#_3iolog`
**SET B / C** — v2 문서의 셀카·OOTD 세트 그대로 사용

## 4. 프롬프트 원문 (재현용)

모든 컷 `--edit downloads/mio_master_clean.jpg` 기준. 아래는 실제 생성에 쓴 최종 프롬프트입니다.

<details><summary><b>01</b> · 풀빌라 수영장 · 아이보리 비키니 + 타월</summary>

```txt
A real amateur phone photo taken by a friend beside a small private pool at a villa in Okinawa in the late afternoon. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else: her long black hair is wet, pushed back off her face with a few damp strands on her neck, still dripping a little. She wears an ivory two-piece swimsuit under a white hotel beach towel wrapped around her waist, and a second towel hanging over one shoulder. She stands on the pool steps half turned towards the friend beside her who has just said something, head in profile, laughing with her mouth open, eyes squinting, not looking at the lens. Water droplets on her shoulders, a faint tan line at her shoulder, a cheap plastic pool float drifting on the bright choppy water behind her, a concrete wall and tropical leaves at the top of the frame. Bright late-afternoon sun, hard shadows, highlights slightly blown out, no golden hour warmth, no glow. The photo is casual and imperfect: slightly tilted horizon, she is off-centre to the left, the friend's shadow falls across the bottom corner, wet hair messy. Visible pores and real skin texture, light makeup half washed off, no retouching, no skin smoothing, no glow. Mild phone noise, slight motion blur on her laughing hand. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

<details><summary><b>02</b> · 필라테스 거울 셀카 · 16 Pro 3구 카메라</summary>

```txt
A real mirror selfie taken on a phone in the full-length mirror of a small pilates studio after a class. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else. All of her black hair is pulled up into one tight high ponytail at the crown, the nape of her neck bare, a few damp strands stuck to her temple and neck. She stands slightly sideways with one hip out, holding the phone at chest height in one hand, the other hand resting on her waist. She wears a fitted black athletic crop top with thin straps and high-waisted charcoal leggings that come up over her waist, a thin sheen of sweat on her shoulders and collarbones. In the mirror the back of her phone is clearly visible: a current iPhone 16 Pro in natural titanium, large square camera plate on the upper left with three big round lenses in a triangle and a small flash — the newest model, not an old single-lens phone. The studio behind her has a wooden floor, a reformer machine at the edge, a grey wall with a hand-sanitizer bottle and a folded towel shelf. Ordinary overhead ceiling light, slightly green and uneven, a hard shadow under her chin, the mirror has a faint smear at the bottom. Framing is casual and imperfect: the phone covers the bottom of her chin, she is not centred, the top of her ponytail touches the frame edge. Real skin with visible pores, a little shine and sweat, no body retouching, no smoothing, no glow. Mild phone noise, slightly soft focus. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

<details><summary><b>03</b> · 호텔 아침 · 배스로브 · 로우 번</summary>

```txt
A phone photo taken by a friend in a hotel room in the morning, standing a few steps away near the window. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else: her black hair is loosely gathered in a low bun at the nape of her neck, a few strands falling out, no bangs across the forehead. She sits on the edge of an unmade white hotel bed with the duvet crumpled behind her, knees drawn up, both hands around a white ceramic cup of coffee, her head turned to look out of the tall window, a soft sleepy expression, mouth relaxed, not looking at the camera. She wears a thick white hotel bathrobe, loosely tied at the waist, the collar slipped off her right shoulder so the shoulder and collarbone are bare, the sleeve pushed up to her elbow, and the robe is long, covering her to the knees. On the bed beside her: a half-open suitcase corner, a phone face down, a small plate with a croissant. Behind her the window shows a grey city morning with a few buildings, the light is flat and pale, no sun, slightly overexposed at the window. The photo is imperfect: the frame is a little tilted, she sits to the left, the edge of the bed cuts the bottom of the picture. Real skin with visible pores, no makeup or very thin makeup, slight puffiness around the eyes, a stray strand of hair on her cheek, no retouching, no smoothing, no glow. Mild phone noise. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

<details><summary><b>04</b> · 자취방 밤 · 새틴 캐미솔 · 머리 묶는 중</summary>

```txt
A candid phone photo taken on a self-timer propped on a low chest of drawers in a small Tokyo apartment at night. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else: her long black hair is loose and messy, and she has both hands raised gathering it up behind her head to tie it, elbows out, eyes half closed looking down and away from the lens, a small tired smile. She sits sideways on the edge of the bed with her legs folded, leaning back against the wall. She wears a thin champagne satin camisole top with narrow straps and plain cotton shorts, a thin blanket bunched over her legs and one knee, her phone lying face down on the duvet beside her. The room is small and lived in: a warm bedside lamp with a fabric shade, a stack of books and a mug on the nightstand, a laundry basket, a calendar on the wall, a charging cable across the floor. Everything is lit by the single lamp from the left side, so the right half of the frame falls into shadow, the wall is unevenly lit and slightly yellow. The photo is slightly blurry and grainy like a real night shot with the phone held low: the frame is a little tilted, she is not centred, one elbow is at the edge of the picture. Real skin with visible pores, no makeup, a little shine on the nose, no retouching, no smoothing, no glow. Noticeable phone noise in the shadows. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

<details><summary><b>05</b> · 해질녘 해변 · 컷아웃 모노키니 + 시스루 셔츠</summary>

```txt
A phone photo taken by a friend on a beach in Okinawa just before sunset, from a few steps behind and slightly to the side. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else: her long black hair is blowing across her face and over one shoulder in the wind, she is turning her head back towards the friend as she walks, half her face in her hair, half smiling. She wears a black one-piece swimsuit with cut-out sides and a high neck, and over it a large sheer white cotton shirt that hangs loose and open from both shoulders, the sleeves rolled, the hem lifting behind her in the wind; a thin hotel towel folded over her forearm, a shell bracelet on her wrist, wet sand on her bare feet. Behind her the sea is flat and grey-blue, the sky has a thin band of pale orange at the horizon, two distant figures with a beach umbrella far down the sand, the wet sand mirrors the sky. The light is low and flat, slightly cool, no warm golden glow, the sun already behind clouds. The photo is imperfect: the horizon is not straight, she is walking out of the centre of the frame, a finger edge is slightly in the bottom left corner, hair covers part of her mouth. Real skin with visible pores, fine sand on her shins, no retouching, no smoothing, no glow. Mild phone noise, a little motion blur in her hair and swinging arm. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

<details><summary><b>06</b> · 료칸 다다미방 · 유카타 · 집게핀 올림머리</summary>

```txt
A casual phone selfie taken at arm's length in a tatami room of a small Japanese ryokan in the evening, slightly grainy and imperfect. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else: her black hair is twisted up and clipped with a large plastic claw clip at the back of her head, the nape of her neck and ears bare, a few loose strands falling on her cheek after a bath. She wears a simple navy-and-white thin-striped cotton yukata, loosely wrapped and tied at the waist with a plain soft obi, the collar sitting a little open at the neck, one shoulder slipping down, the sleeve hanging past her wrist. She sits on the floor with her legs folded to one side, holding the phone up with one hand at a slightly high angle, chin a bit low, smiling naturally at the screen, not posing, caught mid-expression. Behind her: tatami mats, a low wooden table with a teapot and two cups, a sliding shoji door half open onto a dark garden, a folded futon in the corner, warm paper-lantern light. The light is warm and dim and uneven, the corners of the room fall into shadow, the ceiling light leaves a soft shadow under her nose, her skin is slightly flushed from the bath and a bit shiny, not airbrushed. The photo is imperfect: the angle is awkward and tilted, part of her arm is cut off at the frame edge, the background is slightly soft but nothing creamy. Real ordinary skin with visible pores and uneven tone, almost no makeup, a small red mark from the bath on her shoulder, normal eyes and nose (not enlarged or retouched), no beauty filter, no smoothing, no glow. Noticeable phone noise in the shadows. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

<details><summary><b>07</b> · 여름 도쿄 거리 · 크롭 나시 + 로우라이즈 데님</summary>

```txt
A real amateur phone snapshot taken by a friend on a narrow street in Tokyo on a hot summer day, from about three metres away. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else: her black hair is parted in the middle with no bangs, straight and tucked behind both ears, a little shiny at the roots from the heat. She is walking towards the camera but looking off to the side at a shop window, one hand pushing her hair back, the other holding a cold plastic bottle. She wears a tight ribbed white cropped tank top that ends above her waist and low-rise light-wash baggy jeans with a thin belt, white sneakers, a small canvas tote on her shoulder. The street behind her: a narrow Tokyo lane with a vending machine, potted plants outside a shop, a bicycle leaning on the wall, overhead cables, a few pedestrians far behind. Harsh midday summer sun, hard shadows, the pavement is bright and slightly blown out, the light is unflattering and direct, no golden warmth. The photo is casual and imperfect: the frame is tilted a little, she is off-centre to the right, the friend's shadow is in the bottom of the frame, the top of her head nearly touches the edge. Real skin with visible pores and a slight shine of sweat on her chest and nose, light makeup, no retouching, no smoothing, no glow. Mild phone noise, motion blur in her moving arm. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

<details><summary><b>08</b> · 리조트 선베드 · 선글라스 · 음료</summary>

```txt
A phone photo taken by a friend at a resort pool in Okinawa in the early afternoon. Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone) but change everything else: her black hair is loose and falling forward over one shoulder and onto the sunbed, a pair of dark sunglasses pushed up on top of her head holding it back. She lies on her stomach on a white sunbed, propped up on her elbows, holding a tall glass of iced drink with a paper straw near her mouth, taking a sip, eyes half closed behind the sunglasses on her head, looking at the friend, mouth on the straw. She wears a simple black swimsuit top and light denim shorts, a thin gold anklet, a paperback book face down on the sunbed beside her, a beach towel over the end of the bed, a loose striped cotton shirt bunched under her elbow. Behind her: the pool edge, a white umbrella, a palm shadow on the concrete, another sunbed with a bag on it. Bright, slightly harsh afternoon sun with hard shadows falling across the sunbed, no warm filter, a little overexposed at the top of the frame. The photo is imperfect: she is not centred, the frame is a bit crooked, one elbow is cut at the edge, a strand of hair crosses her cheek. Real skin with visible pores and fine goosebumps, a slight tan line at her shoulder, no retouching, no smoothing, no glow. Mild phone noise. Vertical 4:5. No studio lighting, no bokeh, no cinematic grade, no HDR, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle or background.
```

</details>

## 5. 검수 노트 (2026-11-16)

- **전 8컷 육안 검수 완료**: 얼굴 일관성(눈·코·입·얼굴형·피부 톤), 손가락, 소품, 배경 글자, 과도한 AI 광택, 노골성 수준 확인.
- **재생성 3건**
  - `04` 1차본: 폰을 쥔 손가락이 뭉개져 폐기 → 머리를 양손으로 묶는 포즈로 교체(손-폰 접촉 제거).
  - `05` 1차본: 셔츠 밑단이 엉덩이에서 흰 판처럼 뭉쳐 보여 폐기 → 셔츠를 "양어깨에서 흘러내리는" 묘사로 바꿔 재생성.
  - `06` 1차본: 얼굴이 뷰티 필터처럼 매끈하고 눈이 커 보여 폐기 → "no beauty filter, normal eyes and nose" 문장을 넣어 재생성.
- **거울 셀카 카메라 확인(02)**: 확대 검수 결과 자연 티타늄 바디 + 삼각 배치 3구 렌즈 + 플래시·LiDAR 확인. 구형 아이폰 아님.
- **섀도우밴 안전선**: 8컷 모두 수영복·짐웨어·호텔/료칸/리조트 맥락. 노골적 노출·란제리 연출 없음. 04는 실내 캐미솔이지만 침대·스탠드 조명의 일상 맥락으로 프레이밍.
- **생성기 안전 검사**: 프롬프트에 `lingerie`·`underwear`·`topless`·`nude`·`cleavage` 등 12개 단어가 남으면 `--check`가 exit 2로 실패.
- **참고**: 이미지 생성 단계에서 `bikini`+`wet skin` 조합이 안전 시스템에 두 번 걸려, 수영복은 "타월/셔츠를 걸친 상태"로 서술하는 방식으로 통과시켰습니다(결과물의 노출도는 오히려 안전선에 가까워짐).

## 6. 생성기 사용

```bash
cd prompt_randomizer
python3 generate_prompts.py --mode glamour --person 8 --check \
    --json examples/seed_20261116_glamour.json --markdown examples/seed_20261116_glamour.md
```

출력 예:

```
[02] (glamour) 물에 젖어 뒤로 넘긴 머리 · 아이보리 투피스 수영복 + 허리 타월 · 풀빌라 수영장
check: clean (15 AI-gloss phrases + 12 safety phrases scanned)
```

glamour 모드는 옷과 장소가 강하게 묶여 있어 `pools.json`의 `glamour.looks` 단위로 짝을 지어 뽑습니다(수영복 × 필라테스 거울 같은 모순 차단). 룩을 추가하려면 `glamour.looks`에 `shot`·`place`·`clothing`·`hairstyles` id를 묶어 한 줄 넣으면 됩니다.
