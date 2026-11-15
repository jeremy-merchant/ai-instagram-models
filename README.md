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
