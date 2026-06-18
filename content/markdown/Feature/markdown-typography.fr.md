title: Mise en page Markdown
date: 2026-06-18 12:00:00
lang: fr
slug: markdown-typography
Category: Feature
Tags: Markdown, Typographie

Cet article présente le rendu des éléments typographiques Markdown courants dans ce thème.

## Styles de texte

Texte normal, **gras**, *italique*, ~~barré~~, `code en ligne`, [lien hypertexte](https://example.com).

Combinaisons : **gras avec ~~barré~~**, *italique avec `code en ligne`*.

<!-- more -->

## Citations

> Une citation, qu'il s'agisse d'une maxime, d'un extrait ou d'un contenu à mettre en valeur.

> Les citations multi-paragraphes sont aussi supportées.
>
> Deuxième paragraphe dans le même bloc de citation.

## Listes

Liste non ordonnée :

- Pomme
- Banane
- Orange
  - Sous-élément A
  - Sous-élément B

Liste ordonnée :

1. Étape 1 : Préparer
2. Étape 2 : Exécuter
3. Étape 3 : Vérifier

## Blocs de code

Code en ligne : utilisez `git status` pour vérifier l'état du dépôt.

Bloc de code avec coloration syntaxique (Python) :

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("world"))
```

Bloc de code (Shell) :

```shell
# Installer les dépendances
pip install -r requirements.txt

# Démarrer le serveur de développement
pelican content --autoreload --listen
```

## Tableau

| Fonctionnalité | Support | Remarque         |
|----------------|---------|------------------|
| Gras           | ✅      | `**texte**`      |
| Italique       | ✅      | `*texte*`        |
| Barré          | ✅      | `~~texte~~`      |
| Bloc de code   | ✅      | Coloration Shiki |
| Tableau        | ✅      | Extension GFM    |

## Séparateur

---

Un séparateur crée un espacement visuel entre les sections.

## Image

![Image exemple]({static}/images/demo-03.jpg)

Les images supportent aussi le zoom au clic (effet lightbox).
