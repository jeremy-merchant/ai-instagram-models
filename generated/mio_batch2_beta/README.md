# mio_batch2_beta — 10컷 v2 (앞머리 다양화 · `th_ref_06` 대두 교정, 2026-11-17)

기운님 피드백 *"앞머리 너무 일정하고 마지막사진 대두인데 그 다이나믹 프롬프트 쓰면되지않나"* 반영본입니다.
레퍼런스 10장(인스타 `ig_ref_01~06` · 스레드 `th_ref_03~06`)의 구도·의상·장소는 유지하고, **헤어만 컷마다 다르게** 다시 뽑았습니다.

## 무엇이 바뀌었나

1. **앞머리 다양화** — 직전 배치는 마스터 컷의 일자 시스루 뱅이 10컷 전부에 복제되어 있었습니다. 이번에는 `prompt_randomizer/pools.json`의 `hairstyles` 풀에서 **컷마다 다른 헤어 1종**을 지정해 재생성했습니다(10컷 = 10종, 일자 뱅 0컷).
2. **`th_ref_06` 대두 교정** — 카메라를 뒤로 빼 `medium full-shot from slightly elevated angle`로 다시 잡고, `small petite head, slender neck, natural 1:7.5 adult body-to-head proportions`를 프롬프트에 명시했습니다. 머리 폭 대비 어깨 폭이 정상 비율로 돌아왔고, 무거운 일자 앞머리 대신 원본과 같은 **흑갈색 소프트 사이드 파트 반묶음(이마 일부 노출)** 으로 바꿨습니다.

## 컷별 헤어 구성

| 파일 | pools.json 헤어 | 내용 |
| --- | --- | --- |
| `ig_ref_01.jpg` | `center_part_no_bangs` | 앞머리 없는 5:5 센터 가르마, 양옆 귀 뒤로 — 회색 트위드 자켓 실내 전신 |
| `ig_ref_02.jpg` | `natural_waves` | 앞머리 없이 뒤로 넘긴 자연 웨이브 — 올리브 보머·크림 롱스커트, 벽돌담 앞 |
| `ig_ref_03.jpg` | `low_loose_bun` | 목덜미 낮은 똥머리, 귀·목 노출 — 블랙 코트, 은행잎 위 |
| `ig_ref_04.jpg` | `side_swept` | 소프트 사이드 파트 + 옆으로 넘긴 긴 앞머리 — 베이지 슬리브리스·블랙 니트 |
| `ig_ref_05.jpg` | `short_bob_wig` | 턱선 단발 보브, 센터 파트, **앞머리 없음** — 낙엽 위 톱다운 컷 |
| `ig_ref_06.jpg` | `claw_clip_back` | 앞머리 양옆 집게핀으로 넘겨 이마 전체 노출 — 지하철 승강장 |
| `th_ref_03.jpg` | `high_ponytail` | 정수리 높은 포니테일 — 원룸 거울 셀카, 강아지 |
| `th_ref_04.jpg` | `side_braid` | 한쪽 어깨로 땋은 사이드 브레이드 — 카페 타일 벽 |
| `th_ref_05.jpg` | `beanie` | 니트 비니 — 도로 연석에 앉은 컷 |
| `th_ref_06.jpg` | `half_up` (소프트 사이드 파트 반묶음) | 흑갈색 반묶음, 이마 일부 노출 — 피크닉 벤치, **비율 교정 컷** |

## 제작 방식

- `prompt_randomizer/generate_prompts.py`의 `PERSON_TEMPLATE` 규칙 준수: `Keep the woman's face from the reference photo identical (same eyes, nose, mouth, face shape, skin tone); change everything else: {hairstyle}.` … 프롬프트 끝에 `Do not reproduce the reference pose, outfit, hairstyle or background.` 고정.
- `meta.mandatory_realism` · `mandatory_negative` · `mandatory_no_text` · `mandatory_no_small_props` 전부 삽입, `--check`(`check_batch`) 결과 **금지어·금지 피사체 0건**.
- `images --edit work/mio_b2/master_clean.jpg` 로 얼굴 고정, 1080×1350 크롭.
- 후처리: `Image.fromarray(np.array(img.convert("RGB")))` → `JPEG(quality=95, subsampling=0)`, APP0 제거. 10컷 전부 `c2pa·caBX·jumb·xmp·Exif` raw 바이트 **0건**, `PIL.Image.info` **빈 dict**, 세그먼트는 DQT·SOF0·DHT·SOS만.
