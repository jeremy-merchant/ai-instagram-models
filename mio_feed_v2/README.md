# 🌸 미오(Mio) v2 — 랜덤 일상 피드 12컷 `@_3io.log_`

기운님 피드백 — *"앞머리가 너무 일정하지 않나 ㅋㅋ 상황이랑. 좀 다양하게 하고 그냥 일상사진부터 올려야 하니까 그런 것도 기획해서, 옷도 다양하게 하고 이런 거 랜덤으로 뽑아주는 깃 레포 있으면 그런 거 쓰자"* — 를 반영한 2차 팩입니다.

- **생성 방식:** `../prompt_randomizer/generate_prompts.py` (시드 `20261116`)로 뽑은 12개 프롬프트 → `images` CLI
- **노페이스 4컷:** 순수 장면 생성 (레퍼런스 미사용, 사람 얼굴 없음)
- **인물 8컷:** `mio_master_clean.jpg`(= `338.jpg` 정면 마스터)를 `--edit` 베이스로 사용, 얼굴 특징만 유지하고 헤어·의상·구도·장소·조명은 전부 교체
- **규격:** 전 컷 1080×1350 (4:5) · 텍스트·워터마크·인스타 UI 없음
- **컨택트시트:** [`mio_v2_grid.jpg`](mio_v2_grid.jpg)

## 1. 이번 팩에서 달라진 점 (v1 대비)

| 항목 | v1 (`mio_feed/`) | v2 (`mio_feed_v2/`) |
| --- | --- | --- |
| 앞머리 | 흑발 시스루 뱅 고정 | 센터 가르마·사이드 스웨트·포니테일·보브·베레모·비니·하프업·로우번 — **8컷 전부 상이** |
| 의상 | 오프숄더 크림 니트 중심 | 옥스포드 셔츠·트렌치·플로럴 원피스·바시티·가죽 자켓·울코트·오트밀 니트 — 8종 전부 상이 |
| 구도·시선 | 정면 응시 다수 | 노페이스 4컷 + 어깨너머·뒷모습·거울 가림·시선 분산 — 정면 카메라 응시 0컷 |
| 장소 | 카페·침대·거리 반복 | 전철·편의점·세탁소·플랫폼·강변·서점·창가·주방 |
| 선정 방식 | 손으로 작성 | 시드 고정 랜덤 조합(카테고리 중복 없이 추출) |

## 2. 12컷 목록

| # | 파일 | 유형 | 헤어 | 의상 | 구도·시선 | 장소 | 조명 | 시드 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | `mio_v2_01_noface_dessert.jpg` | 노페이스 | – | – | – | 말차 디저트 테이블(스위트콘·팬케이크·아이스티) | 카페 실내 조명 | 20261116 |
| 02 | `mio_v2_02_noface_bookstore.jpg` | 노페이스 | – | – | – | 중고서점 서가에서 책 한 권 빼는 손 | 서점 실내 조명 | 20261116 |
| 03 | `mio_v2_03_noface_night_alley.jpg` | 노페이스 | – | – | – | 밤 도쿄 골목, 빨간 자판기 불빛 | 밤 자판기 불빛 | 20261116 |
| 04 | `mio_v2_04_noface_morning_desk.jpg` | 노페이스 | – | – | – | 아침 창가 책상, 검은 커피와 펼친 책 | 아침 창가 햇살 | 20261116 |
| 05 | `mio_v2_05_centerpart_train.jpg` | 인물 | 앞머리 없는 센터 가르마 흑발 | 스트라이프 옥스포드 셔츠 (허리 묶음) | 음식 먹기 직전, 시선은 접시로 | 전철 안 좌석 | 차창 확산광 | 20261116 |
| 06 | `mio_v2_06_sideswept_night.jpg` | 인물 | 옆으로 넘긴 사이드 스웹트 앞머리 | 베이지 트렌치코트 | 어깨 너머로 부르는 듯한 클로즈업 | 편의점 앞 | 편의점 형광등 + 가로등 | 20261116 |
| 07 | `mio_v2_07_bob_mirror_selfie.jpg` | 인물 | 단발 보브로 바꾼 날 | 플로럴 원피스 + 가디건 | 거울 셀카, 폰으로 얼굴 반쯤 가림 | 주방 카운터 | 아침 창가 햇살 | 20261116 |
| 08 | `mio_v2_08_ponytail_riverside.jpg` | 인물 | 높은 포니테일 | 가디건 + 롱 스커트 | 책 보며 고개 숙인 컷 | 강변 산책로 | 흐린 날 확산광 | 20261116 |
| 09 | `mio_v2_09_beret_laundromat.jpg` | 인물 | 베레모 착용 | 바시티 자켓 + 미니스커트 | 뒷모습에서 살짝 돌아보는 컷 | 동전 세탁소 | 해질녘 실내 조명 | 20261116 |
| 10 | `mio_v2_10_beanie_platform.jpg` | 인물 | 니트 비니 착용 | 블랙 가죽 자켓 + 크롭 티 | 골목을 걸어가는 뒷모습 전신 | 역 플랫폼 | 밤 플랫폼 조명 | 20261116 |
| 11 | `mio_v2_11_clawclip_window.jpg` | 인물 | 반묶음 (앞머리 올려 묶은 하프업) | 블랙 터틀넥 + 울 코트 | 창밖을 보는 옆얼굴 | 자취방 침대 | 아침 창가 햇살 | 20261116 |
| 12 | `mio_v2_12_lowbun_bookstore.jpg` | 인물 | 느슨한 로우 번 (똥머리) | 오트밀 니트 + 와이드 연청 | 머리 묶는 중, 팔 올린 자세 | 서점 통로 | 서점 실내 조명 | 20261116 |

## 3. 프롬프트 원문 (재현용)

시드 `20261116` · `pools.json` · `generate_prompts.py` 조합으로 재생성 가능합니다. 아래는 실제 생성에 사용한 최종 프롬프트입니다(프레이밍 보정분 포함).

<details><summary><b>01</b> · 노페이스 · 말차 디저트 테이블(스위트콘·팬케이크·아이스티)</summary>

```txt
Candid daily-life Instagram photo for the personal feed of a 21-year-old Japanese woman living alone in Tokyo. Scene: overhead shot of a matcha parfait and a small plate of dorayaki on a wooden cafe table, condensation on the iced glass, no face, no people. warm cafe indoor lighting. Shot on an iPhone 13 mini camera. Vertical 4:5, unposed amateur aesthetic, authentic everyday moment, realistic texture, natural color, slight grain, no text, no watermark, no face visible.
```

</details>

<details><summary><b>02</b> · 노페이스 · 중고서점 서가에서 책 한 권 빼는 손</summary>

```txt
Candid daily-life Instagram photo for the personal feed of a 21-year-old Japanese woman living alone in Tokyo. Scene: close-up inside a small secondhand bookstore in Tokyo, colorful spines on wooden shelves, a young woman hand pulling out one novel, no face, no people. warm indoor bookstore lighting. Shot on an iPhone 13 mini camera, slight film grain, soft shadow. Vertical 4:5 full-bleed photo, unposed amateur aesthetic, authentic everyday moment, realistic texture, natural color, no text, no watermark, no instant film border, no face visible.
```

</details>

<details><summary><b>03</b> · 노페이스 · 밤 도쿄 골목, 빨간 자판기 불빛</summary>

```txt
Candid daily-life Instagram photo for the personal feed of a 21-year-old Japanese woman living alone in Tokyo. Scene: a narrow Tokyo backstreet at night, a glowing red vending machine, wet asphalt reflections, tangled power lines overhead, no people, no face. night, lit by the vending machine glow and a distant street lamp. Shot on an old 2010s point-and-shoot digital camera with slight bloom. Vertical 4:5, unposed amateur aesthetic, authentic everyday moment, realistic texture, natural color, slight grain, no text, no watermark, no face visible.
```

</details>

<details><summary><b>04</b> · 노페이스 · 아침 창가 책상, 검은 커피와 펼친 책</summary>

```txt
Candid daily-life Instagram photo for the personal feed of a 21-year-old Japanese woman living alone in Tokyo. Scene: a quiet morning desk beside a sunlit window, a ceramic mug of black coffee, an open paperback with a bookmark, a small plant and a linen pouch, only a fingertips edge of the hand visible, no face. bright morning sunlight through a window, warm highlights. Shot on an iPhone 15 Pro main camera. Vertical 4:5, unposed amateur aesthetic, authentic everyday moment, realistic texture, natural color, slight grain, no text, no watermark, no face visible.
```

</details>

<details><summary><b>05</b> · 센터 가르마(앞머리 없음) · 스트라이프 옥스포드 셔츠 · 전철에서 도시락 · 시선 아래</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical (same eyes, nose, mouth, skin tone) but change everything else: long jet-black hair parted cleanly in the middle with NO bangs, tucked behind both ears, forehead fully exposed. She is wearing a loose blue-and-white striped oxford shirt with the sleeves rolled up, the hem knotted at the waist over straight jeans. Shot: sitting on a Tokyo commuter train seat, about to take the first bite of a bento, chopsticks lifted, eyes cast down toward the food instead of the lens. Expression: an unguarded open laugh. Lighting: cold blue early-morning light from the train window. Shot on an iPhone 15 Pro main camera. Vertical 4:5 candid Instagram feed photo, unposed and slightly imperfect, realistic skin texture, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

<details><summary><b>06</b> · 사이드 스웹트 · 베이지 트렌치코트 · 밤 편의점 앞 어깨너머</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical but change everything else: black hair swept to one side in a soft side-part, long side-swept bangs across the forehead to the temple, hair loose. She is wearing a long beige cotton trench coat over a fine cream turtleneck and dark straight trousers. Shot: over-the-shoulder close-up from behind, only part of the face visible in a three-quarter rear angle as she turns slightly toward the camera. Place: standing in front of a Japanese convenience store at night, glowing storefront glass behind her. Expression: a playful slight pout. Lighting: cool fluorescent spill from the storefront plus a warm street lamp. Shot on a Fujifilm X100V with classic chrome color. Vertical 4:5 candid Instagram feed photo, unposed and slightly imperfect, realistic skin texture, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

<details><summary><b>07</b> · 단발 보브 · 플로럴 원피스+얇은 가디건 · 거울 셀카(폰으로 얼굴 하반신 가림)</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical but change everything else: chin-length short bob haircut with a middle part, no long bangs, ends curling slightly inward. She is wearing a small-print floral long-sleeve dress in muted sage with a thin knit cardigan slipping off one shoulder. Shot: a mirror selfie in a small Tokyo apartment kitchen, she holds an iPhone in front of her face so it covers the lower half, her other hand in her pocket. Expression: eyes smiling, corners crinkled above the phone. Lighting: bright morning light from the kitchen window. Shot on an old 2010s point-and-shoot digital camera with slight bloom. Vertical 4:5 candid Instagram feed photo, realistic skin texture, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

<details><summary><b>08</b> · 높은 포니테일 · 오트밀 가디건+롱 스커트 · 강변에서 책 읽는 옆모습</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical but change everything else: sleek high ponytail tied at the crown of the head, no bangs, baby hairs at the temples, neck and ears fully visible. She is wearing a chunky oatmeal cardigan hanging open over a ribbed top and a long pleated charcoal skirt. Shot: standing on a riverside path at dusk, head lowered, eyes on an open book held in both hands, gaze completely off-camera, only part of the face visible. Lighting: grey overcast evening daylight. Shot on an iPhone 13 mini camera. Vertical 4:5 candid Instagram feed photo, unposed and slightly imperfect, realistic skin texture, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

<details><summary><b>09</b> · 베레모 · 바시티 자켓+체크 미니스커트 · 동전 세탁소에서 뒤돌아보는 컷</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical but change everything else: a black wool beret tilted slightly to one side, black hair loose and tucked behind one ear, no straight bangs. She is wearing a cream-and-black varsity jacket over a cropped tee and a plaid mini skirt with thigh socks. Shot: seen from behind inside a small Japanese coin laundry, body turned away, head half-turned back over the shoulder so only one eye and cheek are visible, hands resting on a folding table. Expression: sleepy half-lidded eyes. Lighting: dusk light mixed with fluorescent tubes and the glow of two washing machines. Shot on an iPhone 15 Pro main camera. Vertical 4:5 candid Instagram feed photo, unposed and slightly imperfect, realistic skin texture, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

<details><summary><b>10</b> · 니트 비니 · 가죽 자켓+블랙 와이드 데님 · 밤 플랫폼 뒷모습 전신</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical but change everything else: a soft ribbed knit beanie pulled down low over the head, a few strands of black hair escaping at the temples. She is wearing a cropped black leather biker jacket over a fitted white tee and high-waisted black wide-leg jeans, white sneakers. Shot: full body from behind, walking away down an open-air station platform at night, one foot mid-step, head turned slightly to the side, back to the camera. Lighting: night under the platform lamps, a train arriving out of focus in the distance. Shot on an old 2010s point-and-shoot digital camera with slight bloom. Vertical 4:5 candid Instagram feed photo, unposed and slightly imperfect, realistic texture, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

<details><summary><b>11</b> · 집게핀 하프업 · 블랙 터틀넥+그레이 울코트 · 창가 턱 괴고 옆얼굴</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical but change everything else: half-up half-down hairstyle, the top section gathered with a tortoiseshell claw clip, no bangs, forehead and face fully visible. She is wearing a black fine-gauge turtleneck under an oversized grey wool coat, hands deep in the pockets. Shot: just came home, still in her coat, sitting sideways on the window ledge of her small Tokyo bedroom with a rumpled duvet behind her, chin resting on her hand, watching the city outside instead of the camera, three-quarter profile. Expression: eyes smiling, corners crinkled. Lighting: soft morning window light on white bedding. Shot on a Polaroid SX-70 instant camera look with visible film grain, full-bleed image with no white instant-film border. Vertical 4:5 candid Instagram feed photo, unposed, realistic skin texture, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

<details><summary><b>12</b> · 로우 번(똥머리) · 오트밀 니트+와이드 연청 · 서점에서 머리 묶는 중</summary>

```txt
Using the reference photo only for the woman face, keep her facial features exactly identical but change everything else: loose low bun at the nape of the neck, no bangs, a few soft strands falling out around the face and ears. She is wearing a soft oatmeal crew-neck knit sweater with the sleeves pulled over her hands, wide-leg light denim and white sneakers. Shot: standing in a narrow aisle of a secondhand bookstore, both arms lifted as she ties her hair up, face partly hidden by her own raised arm, seen from the side. Expression: a playful slight pout. Lighting: warm indoor bookstore lighting with shelves of used books and stacked boxes behind her. Shot on a Fujifilm X100V with classic chrome color. Vertical 4:5 candid Instagram feed photo, unposed and slightly imperfect, realistic skin texture and knit detail, no text, no watermark. Do not reproduce the reference pose, outfit, hairstyle, off-shoulder knit or background.
```

</details>

## 4. 사용 규칙

- 얼굴 일관성 기준은 항상 `338.jpg`(0도 수평 정면 마스터) → 크롭본 `mio_master_clean.jpg`.
- 새 컷을 만들 때는 `prompt_randomizer`로 뽑고, **한 배치 안에서 헤어/의상/구도가 겹치지 않는지** 확인한 뒤 생성하세요.
- 업로드 순서·캡션·해시태그는 노션 가이드의 **2주차 14일 업로드 계획표(v2)** 를 따릅니다.
