# mio_batch2_beta — 10컷 v3 (1·2·4·5·6번은 v1 원본에 머리만 교체, 2026-11-17)

기운님 피드백 *"아니 원래꺼에서 머리스타일만 다이나믹 프롬프트 하란건데"*, *"그래도 3 7 8 9 10 은 좋다"* 반영본입니다.

v2에서 10컷을 마스터 컷에서 다시 뽑아 **구도·의상·배경까지 새로 그려지며 원본에서 벗어난 문제**를 바로잡았습니다.
이번 v3는 **v1 커밋 `9c5e0f3`의 원본 이미지를 그대로 입력(`--edit`)으로 삼아 머리스타일 한 곳만 바꾼 판**입니다.
v1 원본에서 이미 미오 얼굴·구도·의상·배경·조명이 잡혀 있으므로, 마스터 컷에서 처음부터 다시 그리지 않았습니다.

## 컷별 내역

| 파일 | 처리 | pools.json 헤어 | 내용 |
| --- | --- | --- | --- |
| `ig_ref_01.jpg` | **교체** | `center_part_no_bangs` | 앞머리 없는 5:5 센터 가르마, 양옆 귀 뒤로·이마 전체 노출 — 회색 트위드 자켓 실내 전신 |
| `ig_ref_02.jpg` | **교체** | `natural_waves` | 앞머리 없이 뒤로 넘긴 자연 웨이브 — 올리브 보머·크림 롱스커트, 벽돌담 앞 |
| `ig_ref_03.jpg` | v2(`75a0982`) 유지 | `low_loose_bun` | 목덜미 낮은 똥머리, 귀·목 노출 — 블랙 코트, 은행잎 위 |
| `ig_ref_04.jpg` | **교체** | `side_swept` | 소프트 사이드 파트 + 옆으로 넘긴 커튼 뱅 — 베이지 터틀넥, 감나무 테라스 |
| `ig_ref_05.jpg` | **교체** | `short_bob_wig` | 턱선 단발 보브, 센터 파트, **앞머리 없음** — 낙엽 위 톱다운 컷 |
| `ig_ref_06.jpg` | **교체** | `claw_clip_back` | 앞머리 위로 집게핀 고정, 이마 전체 노출 — 지하철 승강장 |
| `th_ref_03.jpg` | v2(`75a0982`) 유지 | `high_ponytail` | 정수리 높은 포니테일 — 원룸 거울 셀카, 강아지 |
| `th_ref_04.jpg` | v2(`75a0982`) 유지 | `side_braid` | 한쪽 어깨로 땋은 사이드 브레이드 — 카페 타일 벽 |
| `th_ref_05.jpg` | v2(`75a0982`) 유지 | `beanie` | 니트 비니 — 도로 연석에 앉은 컷 |
| `th_ref_06.jpg` | v2(`75a0982`) 유지 | `half_up` | 흑갈색 반묶음, 이마 일부 노출 — 피크닉 벤치 |

헤어 10종은 `prompt_randomizer/pools.json`의 `hairstyles`에서 서로 겹치지 않게 골랐고, 10컷 모두 **일자 시스루 뱅 0컷**입니다.

## 제작 방식 (교체 5컷)

- `git show 9c5e0f3:generated/mio_batch2_beta/<파일>`로 v1 원본을 꺼내 `--edit` 입력으로 사용.
- 프롬프트 구조 고정: `Keep everything in this image identical — exact same woman's face, eyes, nose, mouth, jawline, expression, pose, body proportions, outfit, props, lighting, camera angle, framing, and background. Change ONLY her hairstyle: {헤어}. Keep the same dark black-brown hair colour and the same photorealistic quality, skin texture and focus as the original photograph. Do not change the outfit, the background, the pose, the camera distance or anything else in the frame.`
  - v2에서 문제가 된 `Do not reproduce the reference pose, outfit, hairstyle or background.` 문구와 새 의상·새 장소 묘사는 **넣지 않았습니다**.
- 검수: 컷마다 v1과 나란히 놓고 얼굴·구도 대조, YuNet 얼굴 박스로 구도 드리프트 정량 확인(전 컷 얼굴 크기·위치 편차 2% 이내).
- 후처리: 1080×1350 리사이즈 → `Image.fromarray(np.array(img.convert("RGB")))` → `JPEG(quality=95, subsampling=0)`, APP0 제거.
  10컷 전부 `c2pa·caBX·jumb·xmp·Exif` raw 바이트 **0건**, `PIL.Image.info` **빈 dict**, 세그먼트는 DQT·SOF0·DHT·SOS만.

## 검수 시트

- `work/mio_b2/final_grid2.jpg` — 2×5 10컷 컨택트 시트
- `downloads/mio_batch2_beta_master_face_compare.jpg` — 마스터 + 10컷 얼굴 비교 시트
