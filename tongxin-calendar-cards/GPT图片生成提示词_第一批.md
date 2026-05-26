# GPT 图片生成提示词 第一批

用途：在 ChatGPT 图片功能中生成“无字背景图”，再由本地脚本统一叠加日期、节日名和简介。  
统一参数：横版 1080 x 720，真实质感文化海报背景，电影感自然光，主体在画面中上部或右侧，左下留出大块深色文字安全区，右上留出日期胶囊安全区。不要生成任何文字、汉字、logo、水印。

## 汉族｜春节

```text
Create a 1080x720 horizontal cultural poster background for Chinese Spring Festival. Warm lantern light, red paper-cuts, spring couplets as abstract red shapes without readable text, family reunion table atmosphere, soft bokeh, festive but elegant. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark, no distorted faces.
```

## 羌族｜羌年

```text
Create a 1080x720 horizontal cultural poster background for the Qiang New Year in western China. Mountain village stone watchtowers, embroidered Qiang patterns, warm evening light, subtle drum dance atmosphere, respectful documentary style. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark, no religious ritual close-up.
```

## 土家族｜赶年

```text
Create a 1080x720 horizontal cultural poster background for the Tujia “Gannian” New Year custom. Mountain village at dusk, handwoven brocade patterns, festive homecoming, subtle Baishou dance silhouettes in the distance, warm and lively but not crowded. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark.
```

## 哈尼族｜十月年节

```text
Create a 1080x720 horizontal cultural poster background for the Hani October New Year. Terraced rice fields at golden hour, village rooftops, gentle smoke from cooking, harvest and reunion atmosphere, refined documentary poster style. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark.
```

## 回族｜开斋节

```text
Create a 1080x720 horizontal cultural poster background for a Hui Eid celebration in a campus-friendly cultural context. Warm family and community gathering atmosphere, halal food such as youxiang and sanzi on a table, elegant geometric pattern details, respectful and non-ritual presentation. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark, no mosque interior worship scene.
```

## 纳西族｜三朵节

```text
Create a 1080x720 horizontal cultural poster background for the Naxi Sanduo Festival. Lijiang old town rooftops, Jade Dragon Snow Mountain in the distance, Dongba-inspired abstract patterns without readable symbols, people in festive dress as small distant silhouettes, fresh mountain light. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark.
```

## 景颇族｜目瑙纵歌

```text
Create a 1080x720 horizontal cultural poster background for the Jingpo Munao Zongge festival. Large outdoor dance field, colorful traditional pattern poles, people dancing in flowing lines as distant silhouettes, bright borderland festival atmosphere, cinematic daylight. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark, no distorted faces.
```

## 黎族｜三月三

```text
Create a 1080x720 horizontal cultural poster background for the Li ethnic Sanyuesan festival in Hainan. Tropical mountain landscape, Li brocade pattern inspiration, bamboo dance atmosphere, young people singing in the distance, fresh green and warm sunlight, elegant cultural documentary style. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark.
```

## 畲族｜三月三

```text
Create a 1080x720 horizontal cultural poster background for the She ethnic Sanyuesan festival. Misty green mountains, spring outing and folk song gathering atmosphere, colorful ribbon-like costume details, black rice and tea as subtle foreground objects, refined natural light. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark.
```

## 哈萨克族｜纳吾热孜节

```text
Create a 1080x720 horizontal cultural poster background for the Kazakh Nauryz festival. Spring grassland, yurt, distant snow mountains, festive meal table details, people greeting each other as small silhouettes, bright hopeful atmosphere. Leave a clean darkened safe area in the lower-left for title overlay and a clean light safe area in the upper-right for a date label. No text, no logo, no watermark, no close-up distorted faces.
```

## 下载后处理

1. 下载 PNG 原图。
2. 用统一脚本叠加文字：左上“今日同心日历”，右上日期，左下民族标签、节日名、1 句简介，右下“中南民族大学”。
3. 导出 JPG，宽度 1080，质量 70-82，保证单张小于 300KB。
4. 命名建议：

```text
hanzu-chunjie.jpg
qiangzu-qiangnian.jpg
tujia-gannian.jpg
hanizu-shiyuenian.jpg
huizu-kaizhaijie.jpg
naxizu-sanduojie.jpg
jingpo-munaozongge.jpg
lizu-sanyuesan.jpg
shezhu-sanyuesan.jpg
hasake-naurez.jpg
```
