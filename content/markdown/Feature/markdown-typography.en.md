title: Markdown Typography Showcase
date: 2026-06-18 12:00:00
lang: en
slug: markdown-typography
Category: Feature
Tags: Markdown, Typography

This article demonstrates how the theme renders common Markdown typography elements.

## Text Styles

Regular text, **bold**, *italic*, ~~strikethrough~~, `inline code`, and a [hyperlink](https://example.com).

Combined styles: **bold with ~~strikethrough~~**, and *italic with `inline code`*.

<!-- more -->

## Blockquotes

> A quoted passage, such as a maxim, excerpt, or piece of highlighted text.

> Multi-paragraph quotes are supported too.
>
> This is the second paragraph in the same blockquote.

## Lists

Unordered list:

- Apple
- Banana
- Orange
  - Nested item A
  - Nested item B

Ordered list:

1. Step one: prepare
2. Step two: run
3. Step three: verify

## Code Blocks

Inline code: use `git status` to inspect the working tree.

Fenced code block (Python):

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("world"))
```

Fenced code block (Shell):

```shell
# Install dependencies
pip install -r requirements.txt

# Start the development server
pelican content --autoreload --listen
```

## Table

| Feature       | Support | Note                |
|---------------|---------|---------------------|
| Bold          | yes     | `**text**`          |
| Italic        | yes     | `*text*`            |
| Strikethrough | yes     | `~~text~~`          |
| Code blocks   | yes     | Syntax highlighting |
| Tables        | yes     | GFM extension       |

## Separator

---

A separator creates visual spacing between sections.

## Image

![Example image]({static}/images/demo-03.jpg)

Images also support click-to-zoom lightbox behavior.
