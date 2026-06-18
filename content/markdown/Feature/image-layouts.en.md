title: Image Layout Support
date: 2026-03-12 19:30:00
lang: en
slug: image-layouts
Category: Feature
Tags: Theme

This article demonstrates reusable image layout classes supported by the theme.

### Side-by-side pair

<div class="media-pair">
  <img src="{static}/images/demo-01.jpg" alt="Sample 01">
  <img src="{static}/images/demo-03.jpg" alt="Sample 03">
</div>

<details>
<summary>View code</summary>

```html
<div class="media-pair">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
</div>
```

</details>

<!--more-->

### Portrait row with fixed height

Use `media-portrait-h-220 / 240 / 280 / 360 / 480` to constrain the display height. Images shrink proportionally — no cropping, no pagination.

<div class="media-portrait-row media-portrait-h-240">
  <img src="{static}/images/demo-02.jpg" alt="Sample 02">
  <img src="{static}/images/demo-04.jpg" alt="Sample 04">
</div>

<details>
<summary>View code</summary>

```html
<div class="media-portrait-row media-portrait-h-240">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
</div>
```

</details>

### Adaptive grid

<div class="media-grid cols-3 masonry-js">
  <img src="{static}/images/demo-01.jpg" alt="Sample 01">
  <img src="{static}/images/demo-02.jpg" alt="Sample 02">
  <img src="{static}/images/demo-03.jpg" alt="Sample 03">
  <img src="{static}/images/demo-04.jpg" alt="Sample 04">
</div>

<details>
<summary>View code</summary>

```html
<div class="media-grid cols-3 masonry-js">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
  <img src="image-url" alt="img 03">
</div>
```

</details>

### Single image with width control

Use `media-w-100 / 95 / 90 …` in 5% steps.

<div class="media-single media-w-65">
  <img src="{static}/images/demo-03.jpg" alt="Sample 03">
</div>

### Image left, text right

<div class="media-split">
  <img src="{static}/images/demo-02.jpg" alt="Sample 02">
  <div>
    <p>Place a short caption, note, or steps alongside the image.</p>
    <p>Works well for "one key image + one paragraph" layouts.</p>
  </div>
</div>

### Image right, text left

<div class="media-split reverse">
  <img src="{static}/images/demo-04.jpg" alt="Sample 04">
  <div>
    <p>Add <code>reverse</code> to flip the order. Collapses to single-column on mobile.</p>
  </div>
</div>

### Carousel (with lightbox)

<div class="media-carousel">
  <img src="{static}/images/demo-01.jpg" alt="Sample 01">
  <img src="{static}/images/demo-03.jpg" alt="Sample 03">
  <img src="{static}/images/demo-05.jpg" alt="Sample 05">
  <img src="{static}/images/demo-06.jpg" alt="Sample 06">
</div>

---

### Gallery lightbox

Main image centred, thumbnail strip below. Click thumbnails or arrows to navigate; click the main image for fullscreen.

<div class="media-gallery">
  <img src="{static}/images/demo-01.jpg" alt="Sample 01">
  <img src="{static}/images/demo-03.jpg" alt="Sample 03">
  <img src="{static}/images/demo-05.jpg" alt="Sample 05">
  <img src="{static}/images/demo-06.jpg" alt="Sample 06">
</div>
