# 🎬 미오(Mio) 릴스 15편 기획 & 베이스 이미지 팩

`@_3io.log_` · LoreMotion LTX 2.5 Image-to-Video (9:16 · 720p · 5초 루프) · 작성 2026-11-18

- **마스터 레퍼런스**: `work/reels_master_refs/mio_master_clean.jpg` (UI 제거 0도 클린 정면). 모든 컷은 이 이미지를 `--edit` 베이스로 생성.
- **프롬프트 생성기**: `work/reels_master_refs/prompt_randomizer/mio_reels_generator.py` (+ `gen_mio_reels.py`, `regen_mio.py`, `mio_reels_pack.py`)
- **팩 경로**: 원본 PNG `downloads/reels_30_pack/mio/raw/` · 영상 투입용 `downloads/reels_30_pack/mio/lore_ready/` (720×1280 · 183~214KB JPG · 메타데이터 없음)
- **컨택트시트**: `downloads/reels_30_pack/mio/mio_reels_15_sheet.jpg`
- **설계 근거**: 릴스는 15편이 이어지는 시나리오라서, 랜덤 시드 샘플링 대신 15개 룩(장소·헤어·의상·구도·조명)을 고정 배치하고 `mio_reels_generator.py --check`로 배치 내 중복·금지어를 검사했습니다. 같은 입력이면 언제든 같은 15컷이 재현됩니다.
- **브리프 예시 대체**: 예시에 있던 '서점'은 풀의 금지 피사체(책등·글자 혼입)와 충돌해 '레코드숍'으로 바꿨습니다. 나머지 14개 테마(자취방 아침/밤, 카페, 한강, 골목, 편의점, 마트, 지하철, 버스, 거울 OOTD, 비 우산, 혼밥, 디저트, 세탁실)는 브리프 그대로입니다.

## 1. 15편 한눈에 보기

| # | 제목 | 테마 | 장소 | 헤어 | 의상 |
| --- | --- | --- | --- | --- | --- |
| R01 | 아침은 이불 속에서 시작 | 자취방 아침 · 이불 정리 전 | 서울 원룸, 커튼 반쯤 내린 창가, 기와지붕 빌라 지붕, 나무 바닥 | 집게핀으로 대충 올린 헤어, 얼굴 옆으로 잔머리 | 연하늘 깅엄 파자마 (상의 단추 하나 열림, 소매가 손목으로 흘러내림) |
| R02 | 하루 끝, 방 안의 온도 | 자취방 밤 · 침대에 앉아 | 서울 원룸 밤, 벽에 붙은 침대, 협탁 위 머그, 빨래바구니, 바닥 충전 케이블 | 샤워 후 물기 있는 머리, 볼에 붙은 잔머리 | 오버사이즈 그레이 후디 (소매 팔꿈치까지) + 그레이 조거 |
| R03 | 창가 자리, 오후 세 시 | 서울 카페 창가 · 아이스 아메리카노 | 서울 골목 카페 창가 자리, 아이스 아메리카노, 종이냅킨, 유리 뒤로 낮은 골목 | 집게핀으로 반묶음, 나머지는 어깨 아래로 | 블루 스트라이프 옥스포드 셔츠 (소매 롤업, 앞단 느슨히 인) + 스트레이트 데님 |
| R04 | 노을 질 때쯤 한강 | 한강 노을 · 강변 산책 | 한강 강변길, 갈대, 멀리 다리 실루엣, 지나가는 조깅하는 사람들 | 앞머리 없는 자연 웨이브, 바람에 뒤로 넘어감 | 베이지 트렌치코트 (허리 벨트) + 그 아래 플로럴 스커트, 아이보리 플랫 |
| R05 | 골목 끝까지 걸어볼까 | 동네 골목 · 뒷모습 산책 | 서울 주택가 골목, 벽돌 담장, 화분, 타일 지붕 집, 전선 | 네이비 볼캡, 뒤로 낮게 묶은 포니테일 | 빈티지 데님 자켓 + 흰 티 + 블랙 미디 스커트, 흰 스니커즈 |
| R06 | 야식은 편의점에서 | 편의점 앞 밤 · 봉지 들고 나오기 | 서울 편의점 앞, 하얀 형광등이 쏟아지는 유리문, 창에 기댄 자전거, 뒤는 어두운 골목 | 네이비 니트 비니, 관자놀이로 삐져나온 흑발 | 네이비 트레이닝 세트 (재킷 반쯤 지퍼) + 화이트 탱크, 흰 스니커즈 |
| R07 | 장바구니 한 개 분량 | 동네 마트 장보기 | 동네 슈퍼, 금속 진열대, 타일 바닥, 라벨 없는 채소 | 집게핀으로 앞머리만 집어올린 롱 스트레이트 | 오트밀 청키 가디건 + 리브드 톱 + 차콜 플리츠 롱스커트 |
| R08 | 8시 40분의 플랫폼 | 지하철 플랫폼 아침 · 기다림 | 서울 지하철 승강장, 빈 벤치, 유리문 뒤로 흐릿한 열차, 타일 기둥 | 한쪽 어깨로 넘긴 사이드 브레이드, 앞머리는 이마에 얇게 | 그레이 울 코트 + 블랙 터틀넥, 목에 느슨한 머플러, 블랙 와이드 팬츠 |
| R09 | 버스 창에 기대어 | 버스 창가 좌석 | 서울 시내버스 좌석, 광고 없는 창, 지나가는 아파트와 앙상한 나무 | 얇은 시스루 뱅 + 센터 가르마 롱 헤어 (귀 뒤로) | 오트밀 크루넥 니트 (소매 손등까지) + 와이드 연청 |
| R10 | 나가기 전 마지막 확인 | 전신 거울 OOTD · 엘리베이터 | 오피스텔 엘리베이터 거울, 브러시드 메탈 도어, 발치에 캔버스 토트 | 목덜미 낮은 뭉치머리, 관자놀이 잔머리 | 블랙 크롭 레더 자켓 + 화이트 티 + 하이웨이스트 블랙 와이드 진 |
| R11 | 비 오는 날은 천천히 | 비 오는 날 우산 | 서울 주택가 횡단보도, 젖은 아스팔트, 신호등, 낮은 건물들 | 옆으로 넘긴 사이드 스웹트 앞머리, 끝이 살짝 젖음 | 올리브 퀼팅 패딩 + 그레이 스웨트셔츠 + 블랙 스트레이트 진 |
| R12 | 혼자 먹는 저녁도 괜찮아 | 저녁 혼밥 · 국밥집 | 동네 국밥집, 포미카 테이블, 반찬 세 접시, 스테인리스 물컵 | 정수리 높은 포니테일, 목덜미 드러남 | 크림 케이블 니트 (소매 팔꿈치까지) + 다크 스트레이트 진 |
| R13 | 케이크는 못 참지 | 디저트 카페 · 치즈케이크 | 서울 카페 구석 창가 테이블, 치즈케이크, 종이냅킨, 벽에 진 화분 그림자 | 단발 보브 (중앙 가르마, 끝은 안쪽으로) | 스몰 플로럴 원피스 + 얇은 니트 가디건 |
| R14 | 일요일 오후의 세탁실 | 코인세탁실 · 빨래 개기 | 골목 코인세탁실, 벽을 따라 늘어선 드럼 세탁기, 개는 테이블 | 고무줄로 낮게 묶은 포니테일, 앞머리는 양쪽 귀 뒤로 | 워시드 블랙 오버사이즈 스웨트셔츠 + 그레이 스웨트팬츠 |
| R15 | 오늘의 한 장 | 레코드숍 · LP 고르기 | 서울 레코드숍, 벽을 따라 늘어선 LP 크레이트, 카운터 위 램프 | 블랙 베레모, 한쪽 귀 뒤로 넘긴 롱 헤어 | 차콜 오버사이즈 블레이저 + 흰 티 + 블랙 스트레이트 팬츠 |

## 2. 편별 기획

### R01 · 아침은 이불 속에서 시작

**테마**: 자취방 아침 · 이불 정리 전 · **시간대**: 07:40 · 평일 아침

- **상황**: 원룸 침대 끝에 걸터앉아 이불을 반쯤 걷어내는 중. 아직 덜 깬 눈.
- **헤어**: 집게핀으로 대충 올린 헤어, 얼굴 옆으로 잔머리
- **의상**: 연하늘 깅엄 파자마 (상의 단추 하나 열림, 소매가 손목으로 흘러내림)
- **장소**: 서울 원룸, 커튼 반쯤 내린 창가, 기와지붕 빌라 지붕, 나무 바닥
- **조명/구도**: 흐린 아침 창가 빛 / 낮은 선반에 세워둔 폰, 살짝 기울고 인물은 오른쪽으로 치우침
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r01.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r01.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 16 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: hair carelessly twisted up and clipped with a plastic claw clip, messy strands falling around her face and neck. She is wearing loose pale-blue gingham cotton pajamas, the top button open, one sleeve slipping down her wrist. Action: She has just woken up and sits on the edge of the bed with her knees folded to one side, one hand still dragging the duvet back over the mattress, her head turned down towards the floor, sleepy half-lidded eyes, caught before she looks up. Place: a tiny Seoul one-room studio apartment in the morning, the white bed still rumpled behind her, a plain cotton curtain half drawn over the window, low-rise villa roofs with dark tiles outside, worn wooden floorboards, the walls plain and empty. Light: flat cool overcast morning daylight coming in from the window. Everyday and imperfect: the framing is slightly crooked and she is not centred. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, hair, pajamas and bedroom. She slowly lifts her head from the floor and blinks toward the window, breathing softly, and her hand slides the duvet a few centimetres and stops. Sleepy half-lidded eyes, very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 일어나자마자 이불부터 정리. 오늘은 좀 느리게 시작해도 되겠다.
- 🇯🇵 起きたらまず布団。今日はゆっくり始めよう。
- 태그: `#릴스 #서울일상 #자취일기 #아침루틴 #일본인 #일상기록 #朝のルーティン #ひとり暮らし #_3iolog`

### R02 · 하루 끝, 방 안의 온도

**테마**: 자취방 밤 · 침대에 앉아 · **시간대**: 23:10 · 평일 밤

- **상황**: 침대에 무릎 세우고 앉아 머그를 두 손으로 감싸고 있는 중. 시선은 스탠드 쪽.
- **헤어**: 샤워 후 물기 있는 머리, 볼에 붙은 잔머리
- **의상**: 오버사이즈 그레이 후디 (소매 팔꿈치까지) + 그레이 조거
- **장소**: 서울 원룸 밤, 벽에 붙은 침대, 협탁 위 머그, 빨래바구니, 바닥 충전 케이블
- **조명/구도**: 왼쪽 침대 스탠드 하나, 오른쪽 절반은 그림자 / 수건 더미 위에 세운 폰, 눈높이보다 살짝 위
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r02.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r02.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 15 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: damp hair pushed back from her face after a shower, a few strands still stuck to her cheek. She is wearing an oversized heather-grey hoodie with the sleeves pushed to the elbows and relaxed grey joggers. Action: She kneels on the bed with her knees drawn up, both hands around a plain white mug, her head turned towards the dim lamp on the nightstand instead of the camera, a faint closed-mouth smile, shoulders rising a little as she breathes. Place: a small Seoul studio apartment at night, the bed against the wall, a nightstand with a plain ceramic mug, a laundry basket, a charging cable across the floor, a plain wall with nothing on it. Light: one warm bedside lamp from the left, the right half of the frame in shadow, the wall slightly yellow. Everyday and imperfect: one corner is overexposed by the lamp. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, damp hair, grey hoodie and night bedroom. Both hands stay around the mug; she takes one slow small sip and lowers it again, her shoulders rising with a single breath, eyes drifting toward the lamp. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 하루 끝에 이 컵 하나. 방 온도가 딱 좋다.
- 🇯🇵 一日の終わりにこのカップ一杯。部屋の温度がちょうどいい。
- 태그: `#릴스 #서울일상 #자취일기 #밤루틴 #おうち時間 #일상기록 #夜のルーティン #ひとり暮らし #_3iolog`

### R03 · 창가 자리, 오후 세 시

**테마**: 서울 카페 창가 · 아이스 아메리카노 · **시간대**: 15:00 · 평일 오후

- **상황**: 창가 자리에 앉아 턱을 손에 괸 채 바깥을 보다가 고개를 돌리기 시작하는 순간.
- **헤어**: 집게핀으로 반묶음, 나머지는 어깨 아래로
- **의상**: 블루 스트라이프 옥스포드 셔츠 (소매 롤업, 앞단 느슨히 인) + 스트레이트 데님
- **장소**: 서울 골목 카페 창가 자리, 아이스 아메리카노, 종이냅킨, 유리 뒤로 낮은 골목
- **조명/구도**: 창가 자연광, 노출 살짝 불균일 / 맞은편 친구가 한 손으로, 인물은 프레임 밖으로 살짝 치우침
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r03.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r03.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 15 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: hair half up, the top section held by a tortoiseshell claw clip, the rest falling over her shoulders. She is wearing a loose blue-and-white striped oxford shirt with the sleeves rolled up, the front tucked loosely into straight jeans. Action: She sits with her chin propped on one hand, looking out of the window at the street, and is just starting to turn her head back towards the table, her hand still under her jaw. Place: the window seat of a small cafe down a Seoul back street, a tall glass of iced americano on a thin coaster, a crumpled paper napkin, the low-rise street behind the glass, no menu board and no posters. Light: plain daylight from the window, slightly uneven exposure. Everyday and imperfect: part of the table blocks the bottom corner. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, striped shirt, iced americano and cafe window seat. Her chin stays on her hand; her eyes move from the street back to the table while her head turns a few degrees toward the camera, then she blinks. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 창가 자리에 앉으면 시간이 좀 다르게 가는 것 같아.
- 🇯🇵 窓際の席だと、時間の流れが少し違う気がする。
- 태그: `#릴스 #서울일상 #서울카페 #카페투어 #アイスコーヒー #일상기록 #ソウルカフェ #カフェ巡り #_3iolog`

### R04 · 노을 질 때쯤 한강

**테마**: 한강 노을 · 강변 산책 · **시간대**: 17:50 · 주말 해질녘

- **상황**: 강변길을 걷다 멈춰 뒤를 돌아보고, 한 손으로 바람에 날린 머리를 넘기는 중.
- **헤어**: 앞머리 없는 자연 웨이브, 바람에 뒤로 넘어감
- **의상**: 베이지 트렌치코트 (허리 벨트) + 그 아래 플로럴 스커트, 아이보리 플랫
- **장소**: 한강 강변길, 갈대, 멀리 다리 실루엣, 지나가는 조깅하는 사람들
- **조명/구도**: 해 지기 직전 낮고 평평한 빛, 살짝 뿌연 공기 / 몇 걸음 뒤에서 친구가, 전신이 프레임에
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r04.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r04.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
Edit this photo of the same woman into a new situation without changing her face at all. The face must stay pixel-close to the reference: the same thin see-through bangs across her forehead, the same calm grey-tinted eyes and their exact size, the same soft nose, the same small mouth, the same face width and jaw. Do not beautify, do not retouch, do not enlarge the eyes. New scene: she walks along the Han river path in Seoul just before sunset and has stopped mid-step, turned back over her shoulder, one hand pushing her hair from her face while the other holds a long beige trench coat closed at her waist; dry reeds, the far bridge a thin silhouette, a couple of distant joggers on the path. Taken by a friend a few metres behind her, vertical 9:16 phone photo with the whole body in frame and space above her head, low flat pre-sunset light, slightly hazy, visible skin texture. No printed words, no signs, no lettering anywhere. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, trench coat and Han river path. She holds the turn over her shoulder, takes one slow step in place, lets her hand slide out of her hair and blinks into the low light while the wind lifts a few strands. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 노을 보러 나왔는데, 그냥 서 있기만 해도 좋네.
- 🇯🇵 夕焼けを見に来たけど、ただ立ってるだけでいい。
- 태그: `#릴스 #한강 #노을 #서울산책 #夕焼け #일상기록 #ソウル #秋の散歩 #_3iolog`

### R05 · 골목 끝까지 걸어볼까

**테마**: 동네 골목 · 뒷모습 산책 · **시간대**: 16:20 · 주말 오후

- **상황**: 골목을 걸어 올라가며 살짝 뒤를 돌아보는 3/4 후면.
- **헤어**: 네이비 볼캡, 뒤로 낮게 묶은 포니테일
- **의상**: 빈티지 데님 자켓 + 흰 티 + 블랙 미디 스커트, 흰 스니커즈
- **장소**: 서울 주택가 골목, 벽돌 담장, 화분, 타일 지붕 집, 전선
- **조명/구도**: 흐린 오후 확산광 / 뒤따라오는 친구가 초광각으로, 인물은 작게
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r05.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r05.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 15 Pro ultra-wide lens, slight edge distortion. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: a navy baseball cap worn low, hair tied in a low ponytail through the back of the cap. She is wearing a faded oversized denim jacket over a plain white t-shirt and a black midi skirt. Action: Seen from behind at a slight angle as she walks away up the alley, one foot mid-step, her head turned a little to the left as if she is about to look back, one hand in her jacket pocket. Place: a narrow residential alley in a Seoul neighborhood in the afternoon, low brick walls, potted plants on a concrete stoop, a stucco house with a tiled roof, overhead cables, no shop signs and no nameplates. Light: flat overcast afternoon light, slightly cool. Everyday and imperfect: the phone was tilted and the verticals lean a little. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, cap, denim jacket and alley. She takes two slow steps away up the alley, her head turning a little further back over her shoulder, then the step settles; the jacket hem and a few strands of hair move slightly. No exaggerated expression. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 골목 끝까지 걸어보는 중. 여기 진짜 조용하다.
- 🇯🇵 路地の端まで散歩中。ここ、ほんとに静か。
- 태그: `#릴스 #서울골목 #산책 #꾸안꾸 #お散歩 #일상기록 #ソウルの路地 #デニム #_3iolog`

### R06 · 야식은 편의점에서

**테마**: 편의점 앞 밤 · 봉지 들고 나오기 · **시간대**: 21:40 · 평일 밤

- **상황**: 유리문을 나와 봉지를 든 채 잠깐 멈춰 서서 봉지를 내려다보는 중.
- **헤어**: 네이비 니트 비니, 관자놀이로 삐져나온 흑발
- **의상**: 네이비 트레이닝 세트 (재킷 반쯤 지퍼) + 화이트 탱크, 흰 스니커즈
- **장소**: 서울 편의점 앞, 하얀 형광등이 쏟아지는 유리문, 창에 기댄 자전거, 뒤는 어두운 골목
- **조명/구도**: 편의점 형광등 하향광 / 보도에서 두 걸음 떨어진 친구가 살짝 낮게
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r06.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r06.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
Edit this photo of the same woman into a new situation without changing her face at all. The face must stay pixel-close to the reference: the same thin see-through bangs across her forehead, the same calm grey-tinted eyes and their exact size, the same soft nose, the same small mouth, the same face width and jaw. Do not beautify, do not retouch, do not enlarge the eyes. New scene: she steps out of a Seoul convenience store at night and pauses, a plain white plastic bag in one hand at her side, head tipped down towards it, shoulders pulled up against the cold; she wears a navy knit beanie and a navy tracksuit jacket half zipped over a white tank, a bicycle leaning against the clean glass behind her. Taken by a friend on the pavement two steps away, vertical 9:16 phone photo, whole figure in frame, harsh white fluorescent light spilling from the storefront, dark street around. The glass must be completely plain: no posters, no price stickers, no labels, no lettering of any kind anywhere in the frame. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, beanie, navy tracksuit and convenience store front. She lifts her head from the bag, blinks in the store light and shifts the bag to her other hand with a small shoulder movement. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 야식 사러 잠깐. 봉지 하나가 이렇게 무겁다니.
- 🇯🇵 夜食を買いにちょっと。袋一つがこんなに重いなんて。
- 태그: `#릴스 #편의점 #야식 #서울밤 #コンビニ #일상기록 #夜さんぽ #トラックパンツ #_3iolog`

### R07 · 장바구니 한 개 분량

**테마**: 동네 마트 장보기 · **시간대**: 11:00 · 주말 오전

- **상황**: 진열대 앞에서 에코백을 손목에 걸고 아래 칸으로 손을 뻗는 중.
- **헤어**: 집게핀으로 앞머리만 집어올린 롱 스트레이트
- **의상**: 오트밀 청키 가디건 + 리브드 톱 + 차콜 플리츠 롱스커트
- **장소**: 동네 슈퍼, 금속 진열대, 타일 바닥, 라벨 없는 채소
- **조명/구도**: 마트 형광등 / 두 걸음 떨어진 친구가 비스듬히, 앞쪽에 진열대 모서리
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r07.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r07.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 15 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: the front of her black hair pinned back with a claw clip above the ears, the rest long and straight. She is wearing a chunky oatmeal cardigan hanging open over a ribbed top and a long pleated charcoal skirt. Action: She stands at the shelf holding a folding canvas tote with a few loose vegetables in it, her head bowed slightly as she reaches for something on the lower shelf, the tote hanging off her wrist. Place: a small neighborhood supermarket in Seoul, plain metal shelving, a tiled floor, loose unpackaged vegetables on the shelves with no price labels and no printed packaging. Light: cool fluorescent supermarket lighting. Everyday and imperfect: the focus sits just behind her so her hands are a little soft. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, cardigan, tote bag and supermarket shelves. Her head stays bowed; her hand moves along the shelf edge, she lifts one item slightly and puts it back, breathing calmly. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 장보기는 늘 이만큼. 혼자 먹기 딱 좋은 양.
- 🇯🇵 買い物はいつもこのくらい。ひとり分にちょうどいい。
- 태그: `#릴스 #장보기 #동네마트 #서울일상 #買い物 #일상기록 #スーパー #ひとり暮らし #_3iolog`

### R08 · 8시 40분의 플랫폼

**테마**: 지하철 플랫폼 아침 · 기다림 · **시간대**: 08:40 · 평일 아침

- **상황**: 승강장에 서서 코트 주머니에 손을 넣고 선로 쪽을 바라보는 중.
- **헤어**: 한쪽 어깨로 넘긴 사이드 브레이드, 앞머리는 이마에 얇게
- **의상**: 그레이 울 코트 + 블랙 터틀넥, 목에 느슨한 머플러, 블랙 와이드 팬츠
- **장소**: 서울 지하철 승강장, 빈 벤치, 유리문 뒤로 흐릿한 열차, 타일 기둥
- **조명/구도**: 이른 아침 확산광 + 차가운 승강장 조명 / 한 걸음 뒤 옆에서 친구가, 인물은 작게
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r08.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r08.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
Edit this photo of the same woman into a new situation without changing her face at all. The face must stay pixel-close to the reference: the same thin see-through bangs across her forehead, the same calm grey-tinted eyes and their exact size, the same soft nose, the same small mouth, the same face width and jaw. Do not beautify, do not retouch, do not enlarge the eyes. New scene: she stands on a Seoul subway platform in the early morning in a long grey wool coat with a black turtleneck and a loose scarf, a loose side braid over one shoulder with bangs across her forehead, hands pushed into her coat pockets, looking down the track away from the camera, an empty bench and a blurred train behind the glass doors. Taken by a friend a step behind and to the side, vertical 9:16 phone photo, whole figure in frame, cool platform light, ordinary exposure. No route map, no departure board, no adverts, no lettering anywhere. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, grey coat, scarf and subway platform. She turns her head slowly from the camera toward the track and back, hands staying in her coat pockets, the scarf end lifting a little. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 8시 40분. 이 시간 플랫폼은 늘 이렇다.
- 🇯🇵 8時40分。この時間のホームはいつもこう。
- 태그: `#릴스 #출근길 #지하철 #서울아침 #通勤 #일상기록 #ソウル #冬コート #_3iolog`

### R09 · 버스 창에 기대어

**테마**: 버스 창가 좌석 · **시간대**: 16:10 · 평일 오후

- **상황**: 버스 창가 좌석에 앉아 관자놀이를 유리에 대고 바깥을 보는 중. 무릎 위 가방.
- **헤어**: 얇은 시스루 뱅 + 센터 가르마 롱 헤어 (귀 뒤로)
- **의상**: 오트밀 크루넥 니트 (소매 손등까지) + 와이드 연청
- **장소**: 서울 시내버스 좌석, 광고 없는 창, 지나가는 아파트와 앙상한 나무
- **조명/구도**: 흐린 날 차창 빛 / 옆 좌석 친구가 어깨 높이에서, 인물은 3/4로 돌아간 상태
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r09.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r09.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
Edit this photo of the same woman into a new situation without changing her face at all. The face must stay pixel-close to the reference: the same thin see-through bangs across her forehead, the same calm grey-tinted eyes and their exact size, the same soft nose, the same small mouth, the same face width and jaw. Do not beautify, do not retouch, do not enlarge the eyes. New scene: she sits on a seat of a Seoul city bus in the afternoon, temple resting against the plain window, looking out at bare trees and apartment blocks, a plain canvas bag on her lap, both sleeves of a soft oatmeal crew-neck knit pulled down over her hands. Shot by the friend in the seat beside her, waist-up vertical 9:16 phone photo, flat overcast daylight through the window, visible skin pores, ordinary exposure. No printed words, no adverts, no route map, no lettering anywhere. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, oatmeal knit and bus window. Her temple stays against the glass; she blinks twice, her head tilts a degree with the movement of the bus, and her sleeve-covered hands shift on the bag. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 버스 창에 기대면 잠깐 멍해지는 시간.
- 🇯🇵 バスの窓にもたれると、ちょっとぼんやりする時間。
- 태그: `#릴스 #버스 #서울일상 #차창 #バス #일상기록 #ソウル #ニット #_3iolog`

### R10 · 나가기 전 마지막 확인

**테마**: 전신 거울 OOTD · 엘리베이터 · **시간대**: 18:30 · 평일 저녁

- **상황**: 엘리베이터 전신 거울 앞에서 셀카. 폰이 턱과 입을 가리는 기본 구도.
- **헤어**: 목덜미 낮은 뭉치머리, 관자놀이 잔머리
- **의상**: 블랙 크롭 레더 자켓 + 화이트 티 + 하이웨이스트 블랙 와이드 진
- **장소**: 오피스텔 엘리베이터 거울, 브러시드 메탈 도어, 발치에 캔버스 토트
- **조명/구도**: 천장 패널 조명, 살짝 초록빛 / 전신이 다 들어오는 거울 프레임, 머리 위 여백
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r10.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r10.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 16 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: black hair gathered into a loose bun low at the nape of the neck, ears and neck visible, a few strands loose at the temples. She is wearing a cropped black leather biker jacket over a fitted white tee and high-waisted black wide-leg jeans. Action: A mirror selfie she is taking herself: she stands off-centre with her weight on one hip, the phone held at chest height so it covers her chin and mouth, her free hand pushed into her jacket pocket, about to shift her weight. Place: the full-length mirror inside a small Seoul officetel elevator, brushed metal doors, a plain tote bag at her feet, no notice sheets and no lettering on the walls. Light: flat ceiling panel light, slightly green and uneven. Everyday and imperfect: the mirror has a faint smudge near the bottom edge. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman, leather jacket, phone and elevator mirror. She keeps the phone at chest height, shifts her weight from one hip to the other and slides her free hand into her pocket, the phone and the mirror reflection staying sharp. No exaggerated expression. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 나가기 전 마지막 확인. 오늘은 이 정도면 됐다.
- 🇯🇵 出る前の最終確認。今日はこれで十分。
- 태그: `#릴스 #거울셀카 #오늘의코디 #레더자켓 #セルフィー #今日のコーデ #韓国ファッション #ootd #_3iolog`

### R11 · 비 오는 날은 천천히

**테마**: 비 오는 날 우산 · **시간대**: 18:20 · 비 오는 저녁

- **상황**: 횡단보도 앞에서 투명 우산을 들고 비를 올려다보는 중.
- **헤어**: 옆으로 넘긴 사이드 스웹트 앞머리, 끝이 살짝 젖음
- **의상**: 올리브 퀼팅 패딩 + 그레이 스웨트셔츠 + 블랙 스트레이트 진
- **장소**: 서울 주택가 횡단보도, 젖은 아스팔트, 신호등, 낮은 건물들
- **조명/구도**: 비 오는 날 회색 확산광, 젖은 노면 반사 / 우산 가장자리 바로 밖에서 친구가, 우산 테가 상단을 자름
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r11.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r11.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 15 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: black hair in a soft side part, long side-swept bangs across the forehead, the ends a little damp. She is wearing an olive quilted short puffer jacket over a grey sweatshirt and black straight jeans. Action: She stands under a clear plastic umbrella, one shoulder lifted, her head tipped up a little towards the falling rain, the umbrella handle held in one hand close to her chest. Place: a residential crossing in a Seoul neighborhood in the rain, wet asphalt with white stripes, plain low buildings behind with no shop signs, a traffic light on its pole. Light: grey rainy daylight, the wet road reflecting the pale sky. Everyday and imperfect: raindrops on the lens blur one corner. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, clear umbrella and rainy crossing. She holds the umbrella steady, raindrops run down the plastic, her head tips up a little, she blinks and her breath shows faintly. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 비 오는 날은 우산 챙기고 천천히.
- 🇯🇵 雨の日は傘を持って、ゆっくり。
- 태그: `#릴스 #비오는날 #투명우산 #서울거리 #雨の日 #일상기록 #ソウル #レインコート #_3iolog`

### R12 · 혼자 먹는 저녁도 괜찮아

**테마**: 저녁 혼밥 · 국밥집 · **시간대**: 19:20 · 평일 저녁

- **상황**: 국밥집 테이블에서 물컵을 두 손으로 감싸고 김이 오르는 그릇을 내려다보는 중.
- **헤어**: 정수리 높은 포니테일, 목덜미 드러남
- **의상**: 크림 케이블 니트 (소매 팔꿈치까지) + 다크 스트레이트 진
- **장소**: 동네 국밥집, 포미카 테이블, 반찬 세 접시, 스테인리스 물컵
- **조명/구도**: 식당 형광등 + 문가 자연광 / 맞은편 친구가 한 손으로, 김은 렌즈와 얼굴 사이
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r12.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r12.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 15 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: all of her black hair gathered into one high ponytail at the crown, the nape and ears bare. She is wearing a cream cable-knit sweater with the sleeves pushed up to the elbow and dark straight jeans. Action: She sits alone with both hands wrapped around the stainless water cup, leaning in a little over the steam, her eyes down on the bowl, her mouth half open as she says something to nobody. Place: a worn formica table in a small neighborhood gukbap diner in Seoul, a steaming bowl of soup with rice in front of her, three small side dishes, a stainless water cup, chairs pushed back, a plain tiled wall with no menu board. Light: one fluorescent tube overhead plus flat daylight from the door. Everyday and imperfect: the steam softens the lower part of the frame. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, cream knit and gukbap table. Her hands stay around the cup; the steam drifts up, she blinks and lowers her eyes to the bowl, her mouth closing after the half-spoken word. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 혼자 먹는 저녁도 나쁘지 않아. 국물이 뜨거워서 더 좋고.
- 🇯🇵 ひとりごはんも悪くない。スープが熱くて、それがいい。
- 태그: `#릴스 #혼밥 #국밥 #서울맛집 #ひとりごはん #일상기록 #ソウル #あったかい #_3iolog`

### R13 · 케이크는 못 참지

**테마**: 디저트 카페 · 치즈케이크 · **시간대**: 14:30 · 주말 오후

- **상황**: 카페 구석 테이블에서 바스크 치즈케이크를 내려다보며 냅킨을 집어 드는 중.
- **헤어**: 단발 보브 (중앙 가르마, 끝은 안쪽으로)
- **의상**: 스몰 플로럴 원피스 + 얇은 니트 가디건
- **장소**: 서울 카페 구석 창가 테이블, 치즈케이크, 종이냅킨, 벽에 진 화분 그림자
- **조명/구도**: 오후 창가 확산광 / 맞은편 1.5m에서 친구가, 앞쪽 접시는 살짝 아웃포커스
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r13.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r13.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 16 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: a chin-length black bob, middle part, the ends turned slightly inward. She is wearing a small-print floral long-sleeve dress with a thin knit cardigan open over it. Action: She sits with her head tilted, looking down at the cheesecake, one hand resting on the table beside the plate and the other lifting the napkin, a faint closed-mouth smile. Place: a corner table by the window in a small Seoul cafe, a slice of plain basque cheesecake on a cream plate, a small paper napkin, a plant casting a soft shadow on a plain plaster wall, an empty wooden chair across from her. Light: flat afternoon daylight through the window. Everyday and imperfect: the chair back blocks the bottom right corner. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, bob hair, floral dress and cake table. She looks down at the plate, blinks, and lifts the napkin slightly as her head tilts a little further; the plant's shadow stays still on the wall. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 케이크는 그냥 못 지나가. 오늘도 성공.
- 🇯🇵 ケーキはやっぱり通り過ぎられない。今日も勝ち。
- 태그: `#릴스 #디저트 #치즈케이크 #카페투어 #カフェ巡り #일상기록 #ソウルカフェ #スイーツ #_3iolog`

### R14 · 일요일 오후의 세탁실

**테마**: 코인세탁실 · 빨래 개기 · **시간대**: 15:40 · 일요일 오후

- **상황**: 코인세탁실 개는 테이블에서 수건을 반쯤 접고 있는 중.
- **헤어**: 고무줄로 낮게 묶은 포니테일, 앞머리는 양쪽 귀 뒤로
- **의상**: 워시드 블랙 오버사이즈 스웨트셔츠 + 그레이 스웨트팬츠
- **장소**: 골목 코인세탁실, 벽을 따라 늘어선 드럼 세탁기, 개는 테이블
- **조명/구도**: 차가운 형광등 / 세탁기 옆에서 친구가, 인물은 오른쪽 절반
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r14.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r14.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
A real amateur phone photo used as an Instagram Reels vertical video frame, shot on an iPhone 15 Pro main camera. Vertical 9:16 portrait, a tall full-height crop with a little space above her head. Keep the woman's face from the reference photo identical — same eyes, nose, mouth, face shape, skin tone and eye colour. She is a 21-year-old Japanese woman living alone in Seoul. Change everything else: black hair tied back in a loose low ponytail with a plain elastic, the front tucked behind both ears, a few short strands loose. She is wearing a washed-black oversized sweatshirt with the sleeves pushed up and loose grey sweatpants. Action: She stands at the folding table with a clean towel half folded in her hands, her head bowed over it, her shoulders relaxed, in the middle of the movement. Place: a coin laundry down a Seoul side street, front-loading washing machines along the wall, a folding table, plain unmarked machines and walls, no lettering anywhere. Light: cool fluorescent tube lighting, a little uneven on the wall. Everyday and imperfect: the machines behind her are slightly out of focus. Real skin with visible pores and small texture, light everyday makeup, no beauty retouching, no skin smoothing, no glow. No studio lighting, no bokeh, no cinematic colour grade, no HDR, no text, no watermark, no logo. No printed words anywhere in the frame: no book, no open book, no book spines, no menu board, no price sign, no receipt, no poster with lettering, no labels on packaging, no signage or nameplates on buildings. Absolutely no earbuds, no earbud case, no AirPods, no small electronics lying on surfaces, no fruit, no berries, no fork, no knife, no spoon, no cutlery. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, black sweatshirt and coin laundry. She finishes folding the towel and lays it flat on the table, then reaches for the next one while the drum of the machine behind her turns slowly. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 빨래는 모아두면 늘 이만큼. 오늘은 미리 끝냄.
- 🇯🇵 洗濯物はためるとこうなる。今日は早めに片付けた。
- 태그: `#릴스 #코인세탁실 #집안일 #일요일 #洗濯 #일상기록 #ひとり暮らし #ルーティン #_3iolog`

### R15 · 오늘의 한 장

**테마**: 레코드숍 · LP 고르기 · **시간대**: 17:10 · 주말 늦은 오후

- **상황**: 레코드 크레이트를 한 손으로 훑으면서 다른 손엔 슬리브를 가슴에 안고 있는 중.
- **헤어**: 블랙 베레모, 한쪽 귀 뒤로 넘긴 롱 헤어
- **의상**: 차콜 오버사이즈 블레이저 + 흰 티 + 블랙 스트레이트 팬츠
- **장소**: 서울 레코드숍, 벽을 따라 늘어선 LP 크레이트, 카운터 위 램프
- **조명/구도**: 따뜻하고 어두운 숍 조명 + 램프 하나 / 어깨 바로 뒤에서 친구가, 얼굴 3/4만 보임
- **파일**: `downloads/reels_30_pack/mio/raw/mio_r15.png` (원본 PNG, 941×1672) → `downloads/reels_30_pack/mio/lore_ready/mio_r15.jpg` (720×1280 JPG)

**베이스 이미지 프롬프트 (실제 생성문)**

```text
Edit this photo of the same woman into a new situation without changing her face at all. The face must stay pixel-close to the reference: the same thin see-through bangs across her forehead, the same calm grey-tinted eyes and their exact size, the same soft nose, the same small mouth, the same face width and jaw. Do not beautify, do not retouch, do not enlarge the eyes. New scene: she stands at a wooden crate of second-hand vinyl records in a cramped Seoul record shop, flipping slowly through the thin record sleeves with one hand, the other hand holding one plain sleeve against her chest, head bowed towards the crate; she wears a black wool beret and a charcoal oversized blazer over a white tee. Taken by a friend just behind her shoulder, vertical 9:16 phone photo, three-quarter over-shoulder framing, warm dim light from one lamp. The records are plain glossy cardboard sleeves with no writing, no price tags and no lettering anywhere in the frame. Keep the exact same face from the reference image, but do not reproduce the reference pose, outfit, hairstyle or background.
```

**LTX 2.5 I2V 모션 프롬프트 (영문)**

```text
Using the uploaded reference image, preserve the exact woman's face, beret, blazer and record crates. Her hand slides one sleeve a few centimetres along the crate and stops; she lifts her head slightly from the crate and blinks. Very slight natural smile, no exaggerated grin. Camera: locked-off handheld phone frame, no zoom, no push-in, no crop change. No text overlay, no watermark, no logo, no face morphing, no extra fingers. Vertical 9:16.
```

**캡션**

- 🇰🇷 오늘의 한 장. 표지 안 봐도 손에 들면 알아.
- 🇯🇵 今日の一枚。ジャケットを見なくても、手に取れば分かる。
- 태그: `#릴스 #레코드숍 #LP #서울주말 #レコード #일상기록 #ソウル #音楽のある暮らし #_3iolog`

## 3. 검수 결과 (2026-11-18)

| # | 판정 |
| --- | --- |
| R01 | 통과 — 얼굴·구도·파자마 정합. 재생성 없음. |
| R02 | 통과 — 손으로 머그 감싼 손가락 자연스러움. 재생성 없음. |
| R03 | 통과 — 아이스 아메리카노·냅킨에 글자 없음. 재생성 없음. |
| R04 | 재생성(1차 얼굴 드리프트: 눈 커짐·얼굴 갸름) → v2 채택. 2차에서 앞머리·눈 크기 일치. |
| R05 | 통과 — 원거리 후면 컷, 얼굴 왜곡 없음. 재생성 없음. |
| R06 | 재생성 — v1 유리문에 노란 가격 스티커 글자 혼입 → 글자 금지 문장 강화 후 v2 채택(유리면 클린). |
| R07 | 통과 — 에코백 손가락·채소 형태 정상. 재생성 없음. |
| R08 | 재생성 — v1 얼굴 갸름·앞머리 소실 → 앞머리 지정 + 얼굴 고정 문장으로 v2 채택. |
| R09 | 재생성 — v1은 다른 사람 수준으로 얼굴 변형 → '얼굴 픽셀 고정' 지시문으로 2안 생성 후 v2 채택. |
| R10 | 통과 — 폰 3구 카메라·전신 구도 확인. 재생성 없음. |
| R11 | 재생성(1차 얼굴 드리프트) → v2 채택. 투명 우산·비·횡단보도 확인. |
| R12 | 통과 — 반찬·김·손가락 정상. 재생성 없음. |
| R13 | 통과 — 커틀러리 없음, 단발 보브 유지. 재생성 없음. |
| R14 | 통과 — 세탁기 다이얼 글자 판독 불가 수준. 재생성 없음. |
| R15 | 재생성 — v1 크레이트가 종이 뭉치처럼 보임 → v2 채택. 좌상단 노란 가격 스티커는 국소 블러로 제거(픽셀 리터치). |

**재생성 5컷**: R04 · R06 · R08 · R09 · R11 (R15는 재생성 + 좌상단 가격 스티커 국소 블러). 1차 배치에서 얼굴이 아이돌체로 드리프트(눈 커짐·턱 갸름)되는 문제가 있어, 재생성분은 `Face fidelity is the top priority…` 문장을 프롬프트에 추가해 해결했다. 원본은 `raw/_v1/`·`raw/_v2/`에 보존.

**공통 확인**: ① 15장 모두 720×1280 · 183~214KB · EXIF/C2PA 없음 ② 프레임 내 한글/영문/가격표/라벨 0건(R15 스티커는 블러 처리) ③ 손가락 왜곡 없음 ④ 마스터의 오프숄더 니트·고정 포즈 미복제 ⑤ 얼굴 정체성 유지(가장 약한 컷은 R05 원거리 후면).

## 4. 업로드 운영 메모

- 릴스는 하루 1편, 피드 게시와 같은 날 겹치지 않게 (Day 9 · Day 12 · Day 14 릴스 슬롯과 맞물려 사용).
- LTX 2.5는 5초 후반부로 갈수록 자동 줌인·미소 강화 경향이 있으므로 **앞 2.5~3초 구간 위주로 컷**해서 붙이는 게 안전.
- 모든 모션 프롬프트에 `Camera: locked-off … no zoom, no push-in` 을 넣어 줌인 성향을 눌렀음. 그래도 잔여 줌이 보이면 재생성 또는 크롭 후 사용.
- 계정 톤 유지: 자막은 영상 안에 굽지 않고 후편집에서 얹기(프레임 내 글자 생성 금지 원칙).

## 5. 파일 목록

| 구분 | 경로 |
| --- | --- |
| 컨택트시트 (3×5) | `downloads/reels_30_pack/mio/mio_reels_15_sheet.jpg` |
| 원본 PNG 15장 | `downloads/reels_30_pack/mio/raw/mio_r01.png` ~ `mio_r15.png` |
| LTX 투입용 JPG 15장 | `downloads/reels_30_pack/mio/lore_ready/mio_r01.jpg` ~ `mio_r15.jpg` |
| 스펙 기록 | `downloads/reels_30_pack/mio/lore_ready/_spec.json` |
| 프롬프트 JSON | `downloads/reels_30_pack/mio/mio_reels_15_prompts.json` |
| 기획서 | `downloads/reels_30_pack/mio/MIO_REELS_15_PLAN.md` · `.json` |
