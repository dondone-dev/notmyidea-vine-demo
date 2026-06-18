title: 画像レイアウトのサポート
date: 2026-06-18 19:30:00
lang: ja
slug: image-layouts
Category: Feature
Tags: テーマ

この記事では、テーマがサポートする再利用可能な画像レイアウトクラスを紹介します。

### 横並びのペア

<div class="media-pair">
  <img src="{static}/images/demo-01.webp" alt="サンプル 01">
  <img src="{static}/images/demo-03.webp" alt="サンプル 03">
</div>

<details>
<summary>コードを表示</summary>

```html
<div class="media-pair">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
</div>
```

</details>

<!--more-->

### 高さ固定の縦長画像の行

`media-portrait-h-220 / 240 / 280 / 360 / 480` を使って表示の高さを揃えられます。画像は比率を保って縮小され、切り抜きやページ送りは発生しません。

<div class="media-portrait-row media-portrait-h-240">
  <img src="{static}/images/demo-02.webp" alt="サンプル 02">
  <img src="{static}/images/demo-04.webp" alt="サンプル 04">
</div>

<details>
<summary>コードを表示</summary>

```html
<div class="media-portrait-row media-portrait-h-240">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
</div>
```

</details>

### 自動調整グリッド

<div class="media-grid cols-3 masonry-js">
  <img src="{static}/images/demo-01.webp" alt="サンプル 01">
  <img src="{static}/images/demo-02.webp" alt="サンプル 02">
  <img src="{static}/images/demo-03.webp" alt="サンプル 03">
  <img src="{static}/images/demo-04.webp" alt="サンプル 04">
</div>

<details>
<summary>コードを表示</summary>

```html
<div class="media-grid cols-3 masonry-js">
  <img src="image-url" alt="img 01">
  <img src="image-url" alt="img 02">
  <img src="image-url" alt="img 03">
</div>
```

</details>

### 幅を指定した単一画像

`media-w-100 / 95 / 90 …` を 5% 刻みで指定できます。

<div class="media-single media-w-65">
  <img src="{static}/images/demo-03.webp" alt="サンプル 03">
</div>

### 画像が左、テキストが右

<div class="media-split">
  <img src="{static}/images/demo-02.webp" alt="サンプル 02">
  <div>
    <p>画像の横に短いキャプションやメモ、手順を配置できます。</p>
    <p>「重要な画像1枚 + 段落1つ」のレイアウトに適しています。</p>
  </div>
</div>

### 画像が右、テキストが左

<div class="media-split reverse">
  <img src="{static}/images/demo-04.webp" alt="サンプル 04">
  <div>
    <p><code>reverse</code> を追加すると順序が反転します。モバイルでは1カラムに折りたたまれます。</p>
  </div>
</div>

### カルーセル（ライトボックス付き）

<div class="media-carousel">
  <img src="{static}/images/demo-01.webp" alt="サンプル 01">
  <img src="{static}/images/demo-03.webp" alt="サンプル 03">
  <img src="{static}/images/demo-05.webp" alt="サンプル 05">
  <img src="{static}/images/demo-06.webp" alt="サンプル 06">
</div>

---

### ギャラリーライトボックス

メイン画像を中央に配置し、その下にサムネイルの列を表示します。サムネイルや矢印をクリックして移動し、メイン画像をクリックすると全画面表示になります。

<div class="media-gallery">
  <img src="{static}/images/demo-01.webp" alt="サンプル 01">
  <img src="{static}/images/demo-03.webp" alt="サンプル 03">
  <img src="{static}/images/demo-05.webp" alt="サンプル 05">
  <img src="{static}/images/demo-06.webp" alt="サンプル 06">
</div>
