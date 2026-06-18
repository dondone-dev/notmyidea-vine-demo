import path from "node:path";
import { promises as fs } from "node:fs";
import { createHighlighter } from "shiki";
import {
  transformerMetaHighlight,
  transformerNotationDiff,
  transformerNotationErrorLevel,
  transformerNotationFocus,
  transformerNotationHighlight,
  transformerNotationMap,
} from "@shikijs/transformers";

function transformerLineNumbers() {
  return {
    name: "line-numbers",
    pre(node) {
      const meta = this.options.meta?.__raw || "";
      if (/\bln\b/.test(meta)) {
        this.addClassToHast(node, "has-line-numbers");
      }
    },
  };
}

const ROOT = process.cwd();
const INPUT_DIR = path.join(ROOT, "content");
const OUTPUT_DIR = path.join(ROOT, ".cache", "shiki-content");
const SCRIPT_PATH = path.join(ROOT, "scripts", "build_shiki_content.mjs");
// 构建标记文件放在缓存目录外，避免被 Pelican 当作内容处理
const MARKER_FILE = path.join(ROOT, ".cache", ".shiki-build-marker");
const THEME = "solarized-light";

const LANGUAGE_ALIASES = new Map([
  ["golang", "go"],
  ["shell", "bash"],
  ["sh", "bash"],
  ["zsh", "bash"],
  ["plaintext", "text"],
]);

async function main() {
  await fs.mkdir(OUTPUT_DIR, { recursive: true });

  // 若脚本自身比上次构建标记更新，则强制重新处理所有 md 文件
  const scriptMtime = await getScriptMtimeIfNewer();

  const highlighter = await createHighlighter({
    themes: [THEME],
    langs: ["go", "bash", "python", "javascript", "typescript", "json", "yaml", "toml", "markdown", "sql", "html", "css", "xml", "rust", "java", "c", "cpp", "diff", "docker", "nginx", "ini", "text"],
  });

  await syncAndTransform(INPUT_DIR, OUTPUT_DIR, highlighter, scriptMtime);
  highlighter.dispose();

  // 更新构建标记，记录本次构建时间
  await fs.writeFile(MARKER_FILE, new Date().toISOString(), "utf8");
  console.log(`Shiki preprocessed content generated at: ${OUTPUT_DIR}`);
}

/**
 * 若脚本自身比构建标记文件更新，返回脚本的 mtime（触发全量 md 重处理）；
 * 否则返回 0（仅按文件 mtime 增量处理）。
 */
async function getScriptMtimeIfNewer() {
  try {
    const [scriptStat, markerStat] = await Promise.all([
      fs.stat(SCRIPT_PATH),
      fs.stat(MARKER_FILE),
    ]);
    return scriptStat.mtimeMs > markerStat.mtimeMs ? scriptStat.mtimeMs : 0;
  } catch {
    // 首次构建，标记文件不存在
    return Date.now();
  }
}

/** 获取文件 mtime（毫秒），文件不存在时返回 0 */
async function getFileMtime(filePath) {
  try {
    return (await fs.stat(filePath)).mtimeMs;
  } catch {
    return 0;
  }
}

/**
 * 增量同步：只更新比缓存更新的文件，删除缓存中已不存在于源的文件。
 * scriptMtime > 0 时，md 文件以 max(srcMtime, scriptMtime) 与缓存比较。
 */
async function syncAndTransform(srcDir, dstDir, highlighter, scriptMtime) {
  const srcEntries = await fs.readdir(srcDir, { withFileTypes: true });
  const srcNames = new Set(srcEntries.map(e => e.name));

  // 删除缓存目录中已不存在于源目录的文件
  try {
    const dstEntries = await fs.readdir(dstDir, { withFileTypes: true });
    for (const entry of dstEntries) {
      if (!srcNames.has(entry.name)) {
        await fs.rm(path.join(dstDir, entry.name), { recursive: true, force: true });
      }
    }
  } catch { /* dstDir 首次创建时可能为空，忽略 */ }

  for (const entry of srcEntries) {
    const srcPath = path.join(srcDir, entry.name);
    const dstPath = path.join(dstDir, entry.name);

    if (entry.isDirectory()) {
      await fs.mkdir(dstPath, { recursive: true });
      await syncAndTransform(srcPath, dstPath, highlighter, scriptMtime);
      continue;
    }

    if (!entry.isFile()) continue;

    const srcMtime = await getFileMtime(srcPath);
    const dstMtime = await getFileMtime(dstPath);

    if (srcPath.endsWith(".md")) {
      // 脚本更新时，视为所有 md 源文件都已变更
      if (Math.max(srcMtime, scriptMtime) > dstMtime) {
        const raw = await fs.readFile(srcPath, "utf8");
        await fs.writeFile(dstPath, transformMarkdownFences(raw, highlighter), "utf8");
      }
    } else if (srcMtime > dstMtime) {
      await fs.copyFile(srcPath, dstPath);
    }
  }
}

function transformMarkdownFences(markdown, highlighter) {
  const fenceRegex = /^```([^\n`]*)\n([\s\S]*?)\n```[ \t]*$/gm;

  return markdown.replace(fenceRegex, (fullMatch, info, code) => {
    const parts = (info || "").trim().split(/\s+/);
    const langToken = parts[0] || "text";
    const metaRaw = parts.slice(1).join(" ");
    const normalizedLang = LANGUAGE_ALIASES.get(langToken) || langToken;

    // 将 tab 展开为 4 个空格，避免 Python-Markdown expandtabs() 按 HTML
    // 字符串列位置展开时因类名长度差异产生不一致的空格数
    code = code.replaceAll("\t", "    ");

    const makeTransformers = () => [
      transformerLineNumbers(),
      transformerMetaHighlight(),
      transformerNotationHighlight(),
      transformerNotationDiff(),
      transformerNotationFocus(),
      transformerNotationErrorLevel(),
      transformerNotationMap({
        classMap: {
          error: "decoration-error",
          hover: "decoration-hover",
        },
        classActivePre: "has-decorations",
      }),
    ];

    const shikiOptions = (lang) => ({
      lang,
      theme: THEME,
      meta: { __raw: metaRaw },
      transformers: makeTransformers(),
    });

    try {
      return highlighter.codeToHtml(code, shikiOptions(normalizedLang));
    } catch (_error) {
      try {
        return highlighter.codeToHtml(code, shikiOptions("text"));
      } catch (__error) {
        return fullMatch;
      }
    }
  });
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
