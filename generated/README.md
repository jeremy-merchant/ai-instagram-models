# generated — 미오 제작 컷 인덱스

| 폴더 / 파일 | 내용 |
| --- | --- |
| `mio_batch2_all_21_grid.jpg` | **배치2 통합 컨택트시트 21컷** (4000×2596, 7×3, A1~A11 알파 + B1~B10 베타, 라벨·캡션 포함, 메타데이터 0) |
| `mio_batch2_alpha/` | 알파 몫 11컷 — `ref_02~10_clean.jpg`(당근 9), `th_01~02_clean.jpg`(스레드 2) + `alpha_11_grid.jpg`(4×3), `face_compare_grid.jpg` |
| `mio_batch2_beta/` | 베타 몫 10컷 — `ig_ref_01~06.jpg`(인스타 6), `th_ref_03~06.jpg`(스레드 4) |

## 공통 규격

- 인물: 미오 마스터 얼굴(`downloads/mio_master_clean.jpg`) 재합성, 흑발 통일, 문신 없음.
- 후처리: `JPEG(quality=95, subsampling=0)`, APP0 제거. `c2pa·caBX·jumb·xmp·Exif·ICC_PROFILE` raw 바이트 **0건** (2026-11-17 검증).
- 컨택트시트는 라벨·캡션을 PIL로 그린 뒤 같은 방식으로 저장 — 메타데이터 없음.

## 배치2 파일 목록 (21컷)

- 알파: `mio_batch2_alpha/ref_02_clean.jpg` ~ `ref_10_clean.jpg` (9), `th_01_clean.jpg`, `th_02_clean.jpg` (2)
- 베타: `mio_batch2_beta/ig_ref_01.jpg` ~ `ig_ref_06.jpg` (6), `th_ref_03.jpg` ~ `th_ref_06.jpg` (4)

raw URL: `https://raw.githubusercontent.com/jeremy-merchant/ai-instagram-models/main/generated/<path>`
