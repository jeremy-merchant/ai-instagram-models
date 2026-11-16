from PIL import Image, ImageDraw, ImageFont

FONT = "../NotoSansKR.ttf"
TW, TH = 1080, 1350

# 1) 1080x1350 (4:5) 정규화
pairs = [
    ("raw/01_white_ruched_highbun.png", "01_white_ruched_highbun.jpg"),
    ("raw/02_checkerboard_robe_flash.png", "02_checkerboard_robe_flash.jpg"),
]
for src, dst in pairs:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target = TW / TH
    if abs((w / h) - target) > 0.0005:
        if w / h > target:  # 너무 넓음 -> 좌우 크롭
            nw = round(h * target)
            left = (w - nw) // 2
            im = im.crop((left, 0, left + nw, h))
        else:  # 너무 큼 -> 상하 크롭(머리 안 잘리게 상단 기준)
            nh = round(w / target)
            im = im.crop((0, 0, w, nh))
    im = im.resize((TW, TH), Image.LANCZOS)
    im.save(dst, quality=94, subsampling=1)
    print(dst, im.size)

# 2) 컨택트시트
W = 1680
M = 20
GAP = 20
IW = (W - 2 * M - 2 * GAP) // 2
IH = round(IW * TH / TW)
TOP = 60
H = TOP + IH + 150

items = [
    ("01_white_ruched_highbun.jpg", "01 · 화이트 셔링 캡소매 티 + 양갈래 하이 번",
     "실내 야간 폰 플래시 셀카 · 패턴 A(방 안 1인칭 플래시) — 킬러 컷 1"),
    ("02_checkerboard_robe_flash.jpg", "02 · 체커보드 플리스 로브 + 흰 봉제 인형",
     "침대 야간 플래시 셀카 · 도화살 치크 · 패턴 A — 킬러 컷 2"),
]

canvas = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(canvas)
f_title = ImageFont.truetype(FONT, 28)
f_c1 = ImageFont.truetype(FONT, 22)
f_c2 = ImageFont.truetype(FONT, 18)

d.text((M, 14), "Mio (@_3io.log_) · 스레드 떡상 벤치마킹 바이럴 2컷 · 2026-11-16",
       font=f_title, fill=(20, 20, 20))

x = M
for name, cap1, cap2 in items:
    im = Image.open(name).convert("RGB").resize((IW, IH), Image.LANCZOS)
    canvas.paste(im, (x, TOP))
    d.text((x, TOP + IH + 14), cap1, font=f_c1, fill=(25, 25, 25))
    d.text((x, TOP + IH + 48), cap2, font=f_c2, fill=(90, 90, 90))
    x += IW + GAP

canvas.save("mio_viral_grid.jpg", quality=92, subsampling=1)
print(canvas.size)
