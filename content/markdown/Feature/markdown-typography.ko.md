title: Markdown 타이포그래피 소개
date: 2026-06-18 12:00:00
lang: ko
slug: markdown-typography
Category: Feature
Tags: Markdown, 타이포그래피

이 글에서는 테마가 일반적인 Markdown 타이포그래피 요소를 어떻게 렌더링하는지 보여줍니다.

## 텍스트 스타일

일반 텍스트, **굵게**, *기울임*, ~~취소선~~, `인라인 코드`, 그리고 [하이퍼링크](https://example.com).

조합 스타일: **굵게와 ~~취소선~~**, 그리고 *기울임과 `인라인 코드`*.

<!-- more -->

## 인용문

> 격언, 발췌, 강조하고 싶은 문장 등의 인용문.

> 여러 단락으로 된 인용문도 지원합니다.
>
> 이것은 같은 인용 블록의 두 번째 단락입니다.

## 목록

순서 없는 목록:

- 사과
- 바나나
- 오렌지
  - 중첩 항목 A
  - 중첩 항목 B

순서 있는 목록:

1. 1단계: 준비
2. 2단계: 실행
3. 3단계: 검증

## 코드 블록

인라인 코드: 작업 트리를 확인하려면 `git status` 를 사용합니다.

코드 블록 (Python):

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("world"))
```

코드 블록 (Shell):

```shell
# 의존성 설치
pip install -r requirements.txt

# 개발 서버 시작
pelican content --autoreload --listen
```

## 표

| 기능          | 지원  | 비고                |
|---------------|-------|---------------------|
| 굵게          | 지원  | `**text**`          |
| 기울임        | 지원  | `*text*`            |
| 취소선        | 지원  | `~~text~~`          |
| 코드 블록     | 지원  | 구문 강조           |
| 표            | 지원  | GFM 확장            |

## 구분선

---

구분선은 섹션 사이에 시각적 여백을 만듭니다.

## 이미지

![예시 이미지]({static}/images/demo-03.webp)

이미지는 클릭하여 확대하는 라이트박스 기능도 지원합니다.
