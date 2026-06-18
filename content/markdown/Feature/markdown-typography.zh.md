title: Markdown 排版展示
date: 2026-06-18 12:00:00
lang: zh
slug: markdown-typography
Category: Feature
Tags: Markdown, 排版

这篇文章展示主题对常见 Markdown 排版元素的渲染效果。

## 文字样式

普通文本、**加粗**、*斜体*、~~删除线~~、`行内代码`、[超链接](https://example.com)。

组合使用：**加粗配 ~~删除线~~**，*斜体配 `行内代码`*。

<!-- more -->

## 引用块

> 引用一段话，可以是名言、摘录，或者需要特别强调的内容。

> 多行引用也支持。
>
> 第二段在同一个引用块内。

## 列表

无序列表：

- 苹果
- 香蕉
- 橙子
  - 嵌套项 A
  - 嵌套项 B

有序列表：

1. 第一步：准备
2. 第二步：执行
3. 第三步：验证

## 代码块

行内代码：用 `git status` 查看工作区状态。

围栏代码块（Python）：

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("world"))
```

围栏代码块（Shell）：

```shell
# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
pelican content --autoreload --listen
```

## 表格

| 功能       | 支持 | 备注             |
|------------|------|------------------|
| 加粗       | ✅   | `**text**`       |
| 斜体       | ✅   | `*text*`         |
| 删除线     | ✅   | `~~text~~`       |
| 代码块     | ✅   | 支持语法高亮     |
| 表格       | ✅   | GFM 扩展         |

## 分隔线

---

分隔线上方内容与下方内容之间会有视觉间隔。

## 图片

![示例图片]({static}/images/demo-03.webp)

图片也支持点击放大（灯箱效果）。
