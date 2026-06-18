title: 博客新增图文布局和轮播图效果支持
date: 2026-03-12 19:30:00
id: 1773193856
Category: Feature
Tags: 博客配置

借助 AI Support，博客完善了图像显示，这篇 memo 用于记录可复用的图文布局。

### 并排 2 张图

<div class="media-pair">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="布局示例图 01">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="布局示例图 03">
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-pair">
  <img src="图片链接" alt="图 01">
  <img src="图片链接" alt="图 02">
</div>
```

</details>

<!--more-->

### 并排 2 张图（超过 2 张自动切换）

<div class="media-pair">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="布局示例图 01">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="布局示例图 03">
  <img src="https://images.yasking.org/memos/1773193856/05.jpg" alt="布局示例图 05">
  <img src="https://images.yasking.org/memos/1773193856/06.jpg" alt="布局示例图 06">
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-pair">
  <img src="图片链接" alt="图 01">
  <img src="图片链接" alt="图 02">
  <img src="图片链接" alt="图 03">
  <img src="图片链接" alt="图 04">
</div>
```

</details>

### 左对齐竖图排列（可设置高度）

下面这个布局适合竖图左对齐排列展示，可以通过 `media-portrait-h-220 / 240 / 280 / 360 / 480` 这几个类限制显示高度，图片会在固定高度内按比例缩小完整显示，不会被截取，也不会启用左右翻页。

<div class="media-portrait-row media-portrait-h-240">
  <img src="https://images.yasking.org/memos/1773193856/02.jpg" alt="布局示例图 02">
  <img src="https://images.yasking.org/memos/1773193856/04.jpg" alt="布局示例图 04">
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-portrait-row media-portrait-h-240">
  <img src="图片链接" alt="图 01">
  <img src="图片链接" alt="图 02">
</div>
```

</details>

### 自适应多图网格

<div class="media-grid cols-3 masonry-js">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="布局示例图 01">
  <img src="https://images.yasking.org/memos/1773193856/02.jpg" alt="布局示例图 02">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="布局示例图 03">
  <img src="https://images.yasking.org/memos/1773193856/04.jpg" alt="布局示例图 04">
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-grid cols-3 masonry-js">
  <img src="图片链接" alt="图 01">
  <img src="图片链接" alt="图 02">
  <img src="图片链接" alt="图 03">
</div>
```

</details>

### 单图宽度控制

下面这个单图布局适合只有一张重点图的场景，可以通过 `media-w-100 / 95 / 90 ...` 这类类名控制宽度，按 5% 为步进自己调。

<div class="media-single media-w-65">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="布局示例图 03">
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-single media-w-65">
  <img src="图片链接" alt="图片">
</div>
```

</details>

### 图左文右

<div class="media-split">
  <img src="https://images.yasking.org/memos/1773193856/02.jpg" alt="布局示例图 02">
  <div>
    <p>这里是图文混排文案区域。你可以放一段简短说明、心得、步骤、引用等。</p>
    <p>这种布局适合「一张重点图 + 一段解释」的场景，阅读节奏会更自然。</p>
  </div>
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-split">
  <img src="图片链接" alt="图片">
  <div>
    <p>文案内容</p>
  </div>
</div>
```

</details>

### 图右文左

<div class="media-split reverse">
  <img src="https://images.yasking.org/memos/1773193856/04.jpg" alt="布局示例图 04">
  <div>
    <p>给容器增加 <code>reverse</code> 即可反转左右顺序，移动端会自动改为单列堆叠。</p>
    <p>你后续只需要复制这一段结构，替换图片 URL 和文字内容就能复用。</p>
  </div>
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-split reverse">
  <img src="图片链接" alt="图片">
  <div>
    <p>文案内容</p>
  </div>
</div>
```

</details>

### 图片轮播（含灯箱）

<div class="media-carousel">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="布局示例图 01">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="布局示例图 03">
  <img src="https://images.yasking.org/memos/1773193856/05.jpg" alt="布局示例图 05">
  <img src="https://images.yasking.org/memos/1773193856/06.jpg" alt="布局示例图 06">
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-carousel">
  <img src="图片链接" alt="图 01">
  <img src="图片链接" alt="图 02">
  <img src="图片链接" alt="图 03">
</div>
```

</details>

---

### 画廊灯箱（media-gallery）

主图大图居中展示，下方缩略图条显示所有图片并高亮当前项，点击 < > 或缩略图切换，点击主图进入全屏灯箱。

<div class="media-gallery">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="布局示例图 01">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="布局示例图 03">
  <img src="https://images.yasking.org/memos/1773193856/05.jpg" alt="布局示例图 05">
  <img src="https://images.yasking.org/memos/1773193856/06.jpg" alt="布局示例图 06">
</div>

<details>
<summary>查看代码</summary>

```html
<div class="media-gallery">
  <img src="图片链接" alt="图 01">
  <img src="图片链接" alt="图 02">
  <img src="图片链接" alt="图 03">
</div>
```

</details>


顺带，支持了代码折叠显示功能。
