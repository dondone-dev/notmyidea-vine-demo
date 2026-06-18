# notmyidea-vine 演示站

*[English](README.md) | 中文*

[notmyidea-vine](https://github.com/dondone-dev/notmyidea-vine) Pelican 主题的演示站点，部署于 Cloudflare Pages。

## 仓库结构

```
notmyidea-vine-demo/
├── themes/notmyidea-vine/   # 主题（git 子模块）
├── plugins/                 # Pelican 插件（i18n_subsites、sitemap）
├── scripts/
│   └── build_shiki_content.mjs  # Shiki 代码高亮预处理脚本
├── content/
│   ├── markdown/            # 文章（.md）
│   ├── pages/               # 独立页面（.md）
│   ├── images/              # 图片
│   └── extra/               # robots.txt、favicon.ico
├── .cache/shiki-content/    # 预处理后的内容（已 git 忽略）
├── Makefile                 # 构建目标：dev、build、shiki-content
├── package.json             # Node.js 依赖（shiki）
├── pelicanconf.py           # 基础配置（本地开发）
├── publishconf.py           # 生产配置（CF Pages）
├── requirements.txt
└── wrangler.toml            # Cloudflare Pages 配置
```

## 本地开发

构建分两步进行：Shiki 先对代码块做语法高亮预处理，Pelican 再基于预处理后的缓存生成站点。

```bash
# 带子模块克隆
git clone --recurse-submodules https://github.com/dondone-dev/notmyidea-vine-demo.git
cd notmyidea-vine-demo

# 安装 Node.js 依赖（用于 Shiki 代码高亮）
npm install

# 创建并激活 Python 虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装 Python 依赖
pip install -r requirements.txt

# 构建并启动本地服务（带代码高亮，使用本地主题）
make dev
# 打开 http://localhost:8000
```

`make dev` 会先执行 `npm run build:shiki-content`（将 `content/` 处理到 `.cache/shiki-content/`），再以 `--autoreload --listen` 启动 Pelican。

> **提示：** 每次新增或修改文章后，重新运行 `make shiki-content`，Pelican 的自动重载就会读取更新后的缓存。

## Cloudflare Pages 部署

### 通过 Dashboard（推荐）

1. 在 Cloudflare 控制台进入 **Workers & Pages → Create → Pages → Connect to Git**，选择本仓库。
2. 在 **Set up builds and deployments（构建与部署设置）** 页面填写：

   | 设置项 | 值 |
   |--------|----|
   | **Framework preset（框架预设）** | `None` |
   | **Build command（构建命令）** | `npm install && pip install -r requirements.txt && make build` |
   | **Build output directory（构建输出目录）** | `output` |
   | **Root directory（根目录）** | *（留空）* |

3. （推荐）在 **Environment variables（环境变量）** 中固定工具链版本，避免构建镜像默认版本过旧：

   | 变量 | 值 |
   |------|----|
   | `PYTHON_VERSION` | `3.12` |
   | `NODE_VERSION` | `20` |

4. 点击 **Save and Deploy**。Git 子模块（主题）会被自动检出。
5. 首次部署后，把 `publishconf.py` 里的 `SITEURL` 改成你真实的 CF Pages 域名（或自定义域名）并再次推送 —— RSS、sitemap 和图片绝对链接都由它推导。

> **为什么构建命令要写在 Dashboard 而不是 `wrangler.toml`：** Cloudflare Pages **不支持** `wrangler.toml` 里的 `[build]` 段（那是 Workers 专用语法），写了会导致配置校验失败。`wrangler.toml` 只承载项目 `name` 和 `pages_build_output_dir`，构建命令必须在 Dashboard 设置。

### 通过 Wrangler CLI

```bash
# 本地构建
make build

# 部署 output/ 目录
wrangler pages deploy output --project-name=notmyidea-vine-demo
```

## 自定义

编辑 `pelicanconf.py` 进行配置：
- `SITENAME`、`AUTHOR`、`SITESUBTITLE`
- `MENUITEMS` 导航菜单
- `INDEX_TITLE`、`INDEX_MESSAGE` 首页文案
- `GISCUS_*` 评论（取消相关行注释即可启用）
- 统计分析相关设置

## 许可证

MIT
