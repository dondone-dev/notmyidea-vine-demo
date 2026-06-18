title: 이미지 레이아웃 지원
date: 2026-03-12 19:30:00
lang: ko
slug: image-layouts
Category: Feature
Tags: 테마

이 글에서는 테마가 지원하는 재사용 가능한 이미지 레이아웃 클래스를 소개합니다.

### 나란히 배치한 쌍

<div class="media-pair">
  <img src="{static}/images/demo-01.webp" alt="샘플 01">
  <img src="{static}/images/demo-03.webp" alt="샘플 03">
</div>

<details>
<summary>코드 보기</summary>

```html
<div class="media-pair">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
</div>
```

</details>

<!--more-->

### 높이를 고정한 세로 이미지 행

`media-portrait-h-220 / 240 / 280 / 360 / 480` 으로 표시 높이를 맞출 수 있습니다. 이미지는 비율을 유지하며 축소되어 잘림이나 페이지 넘김이 발생하지 않습니다.

<div class="media-portrait-row media-portrait-h-240">
  <img src="{static}/images/demo-02.webp" alt="샘플 02">
  <img src="{static}/images/demo-04.webp" alt="샘플 04">
</div>

<details>
<summary>코드 보기</summary>

```html
<div class="media-portrait-row media-portrait-h-240">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
</div>
```

</details>

### 적응형 그리드

<div class="media-grid cols-3 masonry-js">
  <img src="{static}/images/demo-01.webp" alt="샘플 01">
  <img src="{static}/images/demo-02.webp" alt="샘플 02">
  <img src="{static}/images/demo-03.webp" alt="샘플 03">
  <img src="{static}/images/demo-04.webp" alt="샘플 04">
</div>

<details>
<summary>코드 보기</summary>

```html
<div class="media-grid cols-3 masonry-js">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
  <img src="image-url" alt="img 03">
</div>
```

</details>

### 너비를 지정한 단일 이미지

`media-w-100 / 95 / 90 …` 를 5% 단위로 지정합니다.

<div class="media-single media-w-65">
  <img src="{static}/images/demo-03.webp" alt="샘플 03">
</div>

### 이미지 왼쪽, 텍스트 오른쪽

<div class="media-split">
  <img src="{static}/images/demo-02.webp" alt="샘플 02">
  <div>
    <p>이미지 옆에 짧은 캡션, 메모 또는 단계를 배치할 수 있습니다.</p>
    <p>"핵심 이미지 1장 + 단락 1개" 레이아웃에 잘 어울립니다.</p>
  </div>
</div>

### 이미지 오른쪽, 텍스트 왼쪽

<div class="media-split reverse">
  <img src="{static}/images/demo-04.webp" alt="샘플 04">
  <div>
    <p><code>reverse</code> 를 추가하면 순서가 뒤바뀝니다. 모바일에서는 단일 컬럼으로 접힙니다.</p>
  </div>
</div>

### 캐러셀 (라이트박스 포함)

<div class="media-carousel">
  <img src="{static}/images/demo-01.webp" alt="샘플 01">
  <img src="{static}/images/demo-03.webp" alt="샘플 03">
  <img src="{static}/images/demo-05.webp" alt="샘플 05">
  <img src="{static}/images/demo-06.webp" alt="샘플 06">
</div>

---

### 갤러리 라이트박스

메인 이미지를 가운데에 배치하고 그 아래에 썸네일 줄을 표시합니다. 썸네일이나 화살표를 클릭해 이동하고, 메인 이미지를 클릭하면 전체 화면으로 표시됩니다.

<div class="media-gallery">
  <img src="{static}/images/demo-01.webp" alt="샘플 01">
  <img src="{static}/images/demo-03.webp" alt="샘플 03">
  <img src="{static}/images/demo-05.webp" alt="샘플 05">
  <img src="{static}/images/demo-06.webp" alt="샘플 06">
</div>
