title: Mise en page des images
date: 2026-03-12 19:30:00
Category: Feature
Tags: Thème

Cet article présente les classes de mise en page d'images disponibles dans ce thème.

### Deux images côte à côte

<div class="media-pair">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="Exemple 01">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="Exemple 03">
</div>

<!--more-->

### Rangée portrait avec hauteur fixe

Utilisez `media-portrait-h-220 / 240 / 280 / 360 / 480` pour limiter la hauteur d'affichage. Les images se réduisent proportionnellement sans recadrage.

<div class="media-portrait-row media-portrait-h-240">
  <img src="https://images.yasking.org/memos/1773193856/02.jpg" alt="Exemple 02">
  <img src="https://images.yasking.org/memos/1773193856/04.jpg" alt="Exemple 04">
</div>

### Grille adaptative

<div class="media-grid cols-3 masonry-js">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="Exemple 01">
  <img src="https://images.yasking.org/memos/1773193856/02.jpg" alt="Exemple 02">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="Exemple 03">
  <img src="https://images.yasking.org/memos/1773193856/04.jpg" alt="Exemple 04">
</div>

### Image à gauche, texte à droite

<div class="media-split">
  <img src="https://images.yasking.org/memos/1773193856/02.jpg" alt="Exemple 02">
  <div>
    <p>Placez une courte légende ou des notes à côté de l'image.</p>
  </div>
</div>

### Carrousel

<div class="media-carousel">
  <img src="https://images.yasking.org/memos/1773193856/01.jpg" alt="Exemple 01">
  <img src="https://images.yasking.org/memos/1773193856/03.jpg" alt="Exemple 03">
  <img src="https://images.yasking.org/memos/1773193856/05.jpg" alt="Exemple 05">
</div>
