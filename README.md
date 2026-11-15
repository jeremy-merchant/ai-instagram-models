# 📸 AI Instagram Influencer Master Archive

인스타그램 AI 인플루언서 모델 프로젝트 마스터 아카이브

---

## 🌸 [계정 A] 메인 모델: 미오 (Mio)

- **Instagram ID:** `@_3io.log_`
- **프로필:** 21세, 일본 도쿄 거주
- **콘셉트:** 청순 도화살, 오프숄더 크림 니트, 흑발 시스루 뱅, 투명한 피부
- **오리지널 피팅룸 레퍼런스:** `1794742542230.jpg` (레포지토리 루트에 업로드 완료)

---

## 👑 4방향 마스터 턴어라운드 레퍼런스 팩 (Master Turnaround Pack)

### 1. [마스터 기준] 반신 정면 컷 (Front Half-Body - Master Key)
- **비주얼:** 피팅룸 컷의 몽환적인 도화살 눈매 50% + 후보 3번(맑은 사슴/강아지상) 50%의 황금 밸런스.
- **착장:** 쇄골과 어깨선이 드러나는 오프숄더 크림 루즈핏 니트.
- **프롬프트 (Master Face):**
  > `A clean front-facing medium portrait of a gorgeous 21-year-old Japanese woman, 50/50 blend between alluring eye shape, straight thin bangs, translucent porcelain skin and innocent doe eyes with gentler cheek contour, sweet warm smile. Cozy off-shoulder cream knit sweater revealing soft collarbone lines. Natural warm indoor lighting, authentic candid mobile camera aesthetic, high realism.`

### 2. 측면 반신 컷 (Side Profile 90°)
- **비주얼:** 오똑하고 부드러운 콧대와 턱선, 어깨로 자연스럽게 흐르는 흑발 라인.
- **프롬프트:**
  > `Side profile view (90-degree profile angle) medium half-body portrait of the exact same 21-year-old Japanese woman from the confirmed reference. Delicate nose bridge, soft feminine jawline, long straight black hair falling down gracefully, see-through bangs. Off-shoulder cozy cream knit sweater, clean neutral indoor studio background.`

### 3. 뒷모습 컷 (Back View)
- **비주얼:** 허리선까지 자연스럽게 떨어지는 레이어드 흑발 실루엣과 오프숄더 어깨선 뒷태.
- **프롬프트:**
  > `Back view (rear angle) medium half-body shot of the exact same 21-year-old Japanese woman. Long silky straight jet-black layered hair cascading down her back to mid-waist. Off-shoulder cozy cream knit sweater showing soft upper back, shoulders, and delicate silhouette.`

### 4. 전신 정면 컷 (Full Body Standing)
- **비주얼:** 슬림하고 비율 좋은 실루엣, 크림 오프숄더 니트에 하이웨이스트 연청 와이드 데님과 화이트 스니커즈 매치.
- **프롬프트:**
  > `Full body standing view of the exact same 21-year-old Japanese woman from the reference (sweet doe eyes, thin black bangs, fair glowing skin). Wearing off-shoulder cozy cream knit sweater paired with high-waisted wide-leg light blue denim jeans and white sneakers. Slender proportional figure, delicate collarbones, head-to-toe full-shot.`

---

## 🚀 3단계 소프트 런칭 피드 빌드업 전략
- **1단계 (게시물 1~3):** 얼굴 없는 감성 일상 (도쿄 카페 손/말차라떼, 침대 발끝/책, 뒷모습 OOTD)
- **2단계 (게시물 4~6):** 폰으로 얼굴 반쯤 가린 거울 셀카 티징 (호기심 극대화)
- **3단계 (게시물 7 이후):** 정면 침대 셀카 및 시그니처 킬러 비주얼 풀공개!

---

## 🆕 2026-11-16 업데이트 — 미오 단독 집중 확정

- **계정 B(리나) 트랙은 보류**합니다. 톤이 강해 이번 피드/계획에서 제외했습니다.
- **미오(`@_3io.log_`) 확정 피드 이미지 15컷**을 [`mio_feed/`](mio_feed/) 에 정리했습니다. (기존 확정 2컷 + 신규 생성 13컷, 전 컷 4:5)
- 각 컷의 컨셉·추천 용도는 [`mio_feed/README.md`](mio_feed/README.md) 참조.
- 2주차 14일 업로드 계획표·해시태그 전략은 노션 가이드 페이지 참조.

## 🎲 2026-11-16 v2 업데이트 — 랜덤 프롬프트 생성기 + 일상 피드 12컷

기운님 피드백("앞머리가 너무 일정하지 않나 ㅋㅋ … 랜덤으로 뽑아주는 깃 레포 있으면 그런 거 쓰자")에 따라
[`fairy-root/Flux-Prompt-Generator`](https://github.com/fairy-root/Flux-Prompt-Generator)(MIT) 구조를 참고한
미오 전용 생성기를 만들고, 그걸로 뽑은 12컷을 추가했습니다.

- **[`prompt_randomizer/`](prompt_randomizer/)** — `generate_prompts.py` + `pools.json`
  (노페이스 장면 14 / 헤어 14 / 의상 14 / 인물 구도 12 / 장소 12 / 표정 7 / 카메라 6).
  시드 고정·배치 내 중복 없는 추출·장소별 조명 매칭으로 "같은 앞머리, 같은 포즈"를 구조적으로 제거.
  사용법은 [`prompt_randomizer/README.md`](prompt_randomizer/README.md).
- **[`mio_feed_v2/`](mio_feed_v2/)** — 노페이스 4컷 + 인물 8컷 (전 컷 1080×1350, 4:5).
  헤어 8종·의상 8종·구도 8종 전부 상이, 정면 카메라 응시 0컷. 컨택트시트 [`mio_feed_v2/mio_v2_grid.jpg`](mio_feed_v2/mio_v2_grid.jpg),
  컷별 시드·프롬프트 표는 [`mio_feed_v2/README.md`](mio_feed_v2/README.md).
- 기존 `mio_feed/` 15컷은 스토리·릴스 커버용으로 그대로 유지합니다.

## 🔁 2026-11-16 v2.1 업데이트 — AI 티·구형 아이폰·인위적 구도 7컷 전면 재생성

기운님 피드백("너무 ai 스럽거나 아이폰 너무예전꺼거나 구도자체가 ai 스러운거는 다시만들자")에 따라
v2 12컷 중 **05·07·08·09·10·11·12 7컷을 폐기하고 다시 뽑았고, 06도 개선**했습니다(노페이스 01~04 유지).

- **AI 티 제거:** `cinematic`·`golden hour`·`bokeh`·`8k`·`masterpiece`·`perfect skin` 같은 화보 키워드를 풀에서 삭제하고
  `meta.banned_keywords` + `--check`로 재유입을 막습니다. 모든 프롬프트에 모공·플라이어웨이·기울어진 프레임·폰 노이즈를 강제.
- **최신 아이폰 고정:** 카메라 풀은 iPhone 15 Pro / 16 Pro 계열만. 거울 셀카(07)는 16 Pro 3구 카메라가 거울에 잡히도록 명시하고 확대 검수했습니다.
- **현실적 구도:** 식당에서 친구가 찍어준 컷(05) · 골목길 후면(10) · 구제숍 소품 구경(09) · 낮 공원 대화(08) · 지하철 대기(11) · 서점 잡지 코너(12).
- 컨택트시트·컷별 프롬프트·검수 노트는 [`mio_feed_v2/README.md`](mio_feed_v2/README.md),
  풀 변경 내역은 [`prompt_randomizer/README.md`](prompt_randomizer/README.md) 참조.

## 🌊 2026-11-16 v3 업데이트 — 3~4주차 바이럴·노출 8컷 + glamour 모드

기운님 지시("그리고 그뒤에이제 노출있는것도 만들어주고")로 v2 일상 피드 뒤에 붙일 **노출·바이럴 구간 8컷**을 추가했습니다.

- **[`mio_feed_v3/`](mio_feed_v3/)** — 풀빌라 수영장 · 필라테스 거울 셀카 · 호텔 가운 · 자취방 캐미솔 · 해질녘 해변 · 료칸 유카타 · 여름 도쿄 거리 · 리조트 선베드 (전 컷 1080×1350, 4:5).
  컨택트시트 [`mio_feed_v3/mio_v3_grid.jpg`](mio_feed_v3/mio_v3_grid.jpg), 컷별 프롬프트·검수 노트·캡션·태그는 [`mio_feed_v3/README.md`](mio_feed_v3/README.md).
- **생성기 확장:** `prompt_randomizer/generate_prompts.py --mode glamour` 추가. 옷과 장소가 강하게 묶인 노출 컷은 `pools.json`의 `glamour.looks` 단위로 짝지어 뽑고, `lingerie`·`underwear`·`topless` 등 12개 안전 금지어를 `--check`가 검사합니다.
- **섀도우밴 안전선:** 8컷 모두 수영복·짐웨어·호텔/료칸/리조트 맥락. 업로드는 3일에 1장 이하, 태그는 여행·운동 카테고리만 사용.
