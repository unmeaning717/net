from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = Path.home() / ".codex" / "generated_images" / "019e2e84-3832-7fd1-b89b-9d1173a29c94"
CARD_DIR = ROOT / "tongxin-calendar-cards"
OUT_DIR = CARD_DIR / "mobile-text-v3"


def zh(s: str) -> str:
    return s.encode("ascii").decode("unicode_escape")


ITEMS = [
    ("hanzu-chunjie", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u6b63\u6708\u521d\u4e00"), zh(r"\u6c49\u65cf / \u5171\u540c\u6587\u5316\u4e3b\u9898"), zh(r"\u6625\u8282"), zh(r"\u8f9e\u65e7\u8fce\u65b0\u7684\u706f\u706b\u91cc\uff0c\u56e2\u5706\u662f\u5171\u540c\u7684\u5e74\u5473\u3002")),
    ("qiangzu-qiangnian", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u5341\u6708\u521d\u4e00"), zh(r"\u7f8c\u65cf"), zh(r"\u7f8c\u5e74"), zh(r"\u7f8c\u5c71\u9f13\u58f0\u4e0e\u7f8c\u7ee3\u7eb9\u6837\uff0c\u8bb0\u5f55\u4e30\u6536\u540e\u7684\u65b0\u5e74\u795d\u798f\u3002")),
    ("tujia-gannian", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u814a\u6708\u524d\u540e"), zh(r"\u571f\u5bb6\u65cf"), zh(r"\u8d76\u5e74"), zh(r"\u5e74\u5473\u63d0\u524d\u62b5\u8fbe\uff0c\u6446\u624b\u821e\u91cc\u85cf\u7740\u56e2\u5706\u3002")),
    ("hanizu-shiyuenian", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u5341\u6708"), zh(r"\u54c8\u5c3c\u65cf"), zh(r"\u5341\u6708\u5e74"), zh(r"\u68af\u7530\u6536\u83b7\u4e4b\u540e\uff0c\u5bb6\u4eba\u56e2\u805a\u8fce\u6765\u65b0\u5c81\u3002")),
    ("huizu-kaizhaijie", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u4f0a\u65af\u5170\u6559\u5386\u5341\u6708\u521d\u4e00"), zh(r"\u56de\u65cf"), zh(r"\u5f00\u658b\u8282"), zh(r"\u4ece\u4e00\u53e5\u95ee\u5019\u5f00\u59cb\uff0c\u7406\u89e3\u4e0e\u5c0a\u91cd\u62b5\u8fbe\u8eab\u8fb9\u3002")),
    ("naxizu-sanduojie", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u4e8c\u6708\u521d\u516b"), zh(r"\u7eb3\u897f\u65cf"), zh(r"\u4e09\u6735\u8282"), zh(r"\u96ea\u5c71\u4e0e\u53e4\u57ce\u4e4b\u95f4\uff0c\u8282\u65e5\u5b88\u62a4\u7740\u5171\u540c\u8bb0\u5fc6\u3002")),
    ("jingpo-munaozongge", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u6b63\u6708\u5341\u4e94"), zh(r"\u666f\u9887\u65cf"), zh(r"\u76ee\u7459\u7eb5\u6b4c"), zh(r"\u4e07\u4eba\u540c\u821e\u7684\u8def\u7ebf\uff0c\u8d70\u5411\u540c\u5fc3\u7684\u8282\u65e5\u73b0\u573a\u3002")),
    ("lizu-sanyuesan", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u4e09\u6708\u4e09"), zh(r"\u9ece\u65cf"), zh(r"\u9ece\u65cf\u4e09\u6708\u4e09"), zh(r"\u5c71\u6d77\u4e4b\u95f4\u7684\u6b4c\u821e\uff0c\u5531\u51fa\u6625\u5929\u91cc\u7684\u76f8\u9022\u3002")),
    ("shezu-sanyuesan", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"\u519c\u5386\u4e09\u6708\u4e09"), zh(r"\u7572\u65cf"), zh(r"\u7572\u65cf\u4e09\u6708\u4e09"), zh(r"\u5c71\u6b4c\u4e0e\u6625\u8336\u76f8\u4f34\uff0c\u5728\u6b4c\u58f0\u4e2d\u76f8\u9047\u76f8\u77e5\u3002")),
    ("hasake-naurez", zh(r"\u4eca\u65e5\u540c\u5fc3\u65e5\u5386"), zh(r"3\u670821\u65e5\u524d\u540e"), zh(r"\u54c8\u8428\u514b\u65cf"), zh(r"\u7eb3\u543e\u70ed\u5b5c\u8282"), zh(r"\u6625\u98ce\u8d8a\u8fc7\u8349\u539f\uff0c\u628a\u65b0\u7684\u5e0c\u671b\u5e26\u5230\u6821\u56ed\u3002")),
]


def font(size: int, bold: bool = False):
    paths = [
        r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
    ]
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def cover(image, width=1080, height=720):
    image = image.convert("RGB")
    scale = max(width / image.width, height / image.height)
    resized = image.resize((int(image.width * scale), int(image.height * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - width) // 2
    top = (resized.height - height) // 2
    return resized.crop((left, top, left + width, top + height))


def measure(text, fnt):
    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def fit_font(text, max_width, start, bold=False, min_size=20):
    for size in range(start, min_size - 1, -2):
        fnt = font(size, bold)
        if measure(text, fnt)[0] <= max_width:
            return fnt
    return font(min_size, bold)


def shadow(draw, xy, text, fnt, fill=(255, 255, 255, 255), sw=2):
    x, y = xy
    for dx, dy in [(sw, sw), (sw, 0), (0, sw), (-sw, sw), (sw, -sw)]:
        draw.text((x + dx, y + dy), text, font=fnt, fill=(0, 0, 0, 170))
    draw.text((x, y), text, font=fnt, fill=fill)


def render():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(SRC_DIR.glob("*.png"), key=lambda p: p.stat().st_mtime)[-10:]
    outputs = []

    for src, item in zip(files, ITEMS):
        slug, brand, date, label, title, intro = item
        base = cover(Image.open(src)).convert("RGBA")
        overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        for y in range(720):
            od.line([(0, y), (1080, y)], fill=(0, 0, 0, int(90 * (y / 720) ** 1.5)))
        for x in range(650):
            od.line([(x, 0), (x, 720)], fill=(0, 0, 0, int(125 * (1 - x / 650) ** 1.2)))

        im = Image.alpha_composite(base, overlay)
        draw = ImageDraw.Draw(im)
        shadow(draw, (46, 42), brand, font(30, True), sw=2)

        date_font = fit_font(date, 270, 26, True, 18)
        tw, th = measure(date, date_font)
        pill = (1080 - 48 - tw - 46, 38, 1080 - 48, 38 + th + 30)
        draw.rounded_rectangle(pill, radius=24, fill=(255, 255, 255, 235))
        draw.text((pill[0] + 23, pill[1] + 12), date, font=date_font, fill=(30, 38, 52, 255))

        label_font = fit_font(label, 300, 22, True, 16)
        lw, _ = measure(label, label_font)
        draw.rounded_rectangle((48, 474, 48 + lw + 36, 514), radius=18, fill=(255, 211, 75, 235))
        draw.text((66, 482), label, font=label_font, fill=(45, 42, 30, 255))

        title_font = fit_font(title, 660, 58, True, 38)
        shadow(draw, (48, 526), title, title_font, sw=3)

        intro_font = fit_font(intro, 790, 27, True, 20)
        draw.text((50, 626), intro, font=intro_font, fill=(255, 255, 255, 245), stroke_width=2, stroke_fill=(0, 0, 0, 140))
        draw.text((880, 668), zh(r"\u4e2d\u5357\u6c11\u65cf\u5927\u5b66"), font=font(22, True), fill=(255, 255, 255, 230), stroke_width=2, stroke_fill=(0, 0, 0, 120))

        out = OUT_DIR / f"{slug}.jpg"
        rgb = im.convert("RGB")
        quality = 86
        while True:
            rgb.save(out, "JPEG", quality=quality, optimize=True, progressive=True)
            if out.stat().st_size <= 300 * 1024 or quality <= 58:
                break
            quality -= 4
        outputs.append(out)

    sheet = Image.new("RGB", (1170, 1160), (245, 246, 248))
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(outputs):
        thumb = Image.open(path).resize((360, 240), Image.Resampling.LANCZOS)
        x = (index % 3) * 390 + 15
        y = (index // 3) * 290 + 15
        sheet.paste(thumb, (x, y))
        draw.text((x, y + 246), path.name, font=font(18), fill=(25, 35, 50))
    sheet_path = CARD_DIR / "first-batch-contact-sheet.jpg"
    sheet.save(sheet_path, "JPEG", quality=88, optimize=True)

    for path in outputs:
        print(path.name, path.stat().st_size)
    print(sheet_path, sheet_path.stat().st_size)


if __name__ == "__main__":
    render()
