title: Mise en page des images
date: 2026-03-12 19:30:00
lang: fr
slug: image-layouts
Category: Feature
Tags: Thème

Cet article présente les classes de mise en page d'images disponibles dans ce thème.

### Deux images côte à côte

<div class="media-pair">
  <img src="{static}/images/demo-01.webp" alt="Exemple 01">
  <img src="{static}/images/demo-03.webp" alt="Exemple 03">
</div>

<!--more-->

### Rangée portrait avec hauteur fixe

Utilisez `media-portrait-h-220 / 240 / 280 / 360 / 480` pour limiter la hauteur d'affichage. Les images se réduisent proportionnellement sans recadrage.

<div class="media-portrait-row media-portrait-h-240">
  <img src="{static}/images/demo-02.webp" alt="Exemple 02">
  <img src="{static}/images/demo-04.webp" alt="Exemple 04">
</div>

### Grille adaptative

<div class="media-grid cols-3 masonry-js">
  <img src="{static}/images/demo-01.webp" alt="Exemple 01">
  <img src="{static}/images/demo-02.webp" alt="Exemple 02">
  <img src="{static}/images/demo-03.webp" alt="Exemple 03">
  <img src="{static}/images/demo-04.webp" alt="Exemple 04">
</div>

### Image à gauche, texte à droite

<div class="media-split">
  <img src="{static}/images/demo-02.webp" alt="Exemple 02">
  <div>
    <p>Placez une courte légende ou des notes à côté de l'image.</p>
  </div>
</div>

### Carrousel

<div class="media-carousel">
  <img src="{static}/images/demo-01.webp" alt="Exemple 01">
  <img src="{static}/images/demo-03.webp" alt="Exemple 03">
  <img src="{static}/images/demo-05.webp" alt="Exemple 05">
</div>
