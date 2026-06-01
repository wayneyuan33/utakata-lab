# Beacon GEO Site Update Technical PRD

## 顶部导航、Keyword Map 图片、示例报告下载 CTA

**Version:** 1.0  
**Date:** 2026-05-30  
**Status:** Implemented - verified against index.html (2026-06-01)  
**Owner:** UTAKATA LAB  
**Source PRD:** `beacon-geo-site-update-prd.md`

---

## 1. 技术结论

本次更新继续沿用当前静态站实现方式：

- 单页 `index.html`
- 内嵌 CSS / JavaScript
- 本地静态资源放在 `case-folder/`
- 不引入构建流程、后端、CMS 或依赖包

主要技术工作分为三类：

1. 修改顶部导航 HTML。
2. 替换或重新生成 Beacon GEO 第一张产品示意图。
3. 修改 Beacon GEO 模块次级 CTA 的文案和 PDF 下载链接，使用已提供的匿名样本 PDF。

---

## 2. Current State

### 2.1 Navigation

当前导航位于 `index.html` 的 `<nav class="site-nav">`：

```html
<nav class="site-nav" aria-label="Primary navigation">
  <a href="#portfolio">Work</a>
  <a href="#writing">Writing</a>
  <a href="#contact">Contact</a>
</nav>
```

需要新增：

```html
<a href="#beacon-geo">
  <span data-en>Beacon GEO</span>
  <span data-jp>Beacon GEO</span>
</a>
```

已确认放在顶部导航第一位，位于 `Work` 前面。

### 2.2 Beacon GEO Section

当前 Beacon GEO 模块锚点已存在：

```html
<section id="beacon-geo" class="section section--beacon beacon" aria-labelledby="beacon-geo-heading">
```

因此新增导航不需要创建新 section，只需要指向 `#beacon-geo`。

### 2.3 Current CTA

当前次级 CTA：

```html
<a href="#beacon-geo-measures" class="btn btn--secondary">
  <span data-en>What we measure</span>
  <span data-jp>測定内容を見る</span>
</a>
```

目标文案：

```html
<span data-en>Download Example Report</span>
<span data-jp>サンプルレポートをダウンロード</span>
```

目标 href 固定为示例报告 PDF 的静态发布路径：

```text
case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf
```

### 2.4 Current Image Asset

当前第一张 Beacon GEO carousel 图片：

```text
case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png
```

该图片内嵌文字 `PROMPT MAP`，需要改为 `KEYWORD MAP`。

---

## 3. Implementation Requirements

### TR-1: 新增顶部导航链接

修改 `index.html` 中的 `.site-nav`。

目标结构：

```html
<nav class="site-nav" aria-label="Primary navigation">
  <a href="#beacon-geo">
    <span data-en>Beacon GEO</span>
    <span data-jp>Beacon GEO</span>
  </a>
  <a href="#portfolio">
    <span data-en>Work</span>
    <span data-jp>作品</span>
  </a>
  <a href="#writing">
    <span data-en>Writing</span>
    <span data-jp>考えること</span>
  </a>
  <a href="#contact">
    <span data-en>Contact</span>
    <span data-jp>お問い合わせ</span>
  </a>
</nav>
```

No JavaScript changes required because anchor scrolling is already handled by native hash navigation and `html { scroll-behavior: smooth; }`.

### TR-2: 检查导航响应式宽度

当前 `.site-nav` 在 `min-width: 768px` 才显示：

```css
@media (min-width: 768px) {
  .site-nav {
    display: flex;
    align-items: center;
  }
}
```

新增菜单后需检查：

- 768px
- 820px
- 1024px
- 1440px

如果发生挤压，可优先调整：

```css
.site-nav {
  gap: var(--space-6);
}
```

或在较宽断点恢复 `var(--space-8)`：

```css
@media (min-width: 1024px) {
  .site-nav {
    gap: var(--space-8);
  }
}
```

### TR-3: 更新第一张 Beacon GEO 图片

默认方案：

- 使用现有资产生成流程或源文件重新生成第一张图片。
- 保持画面尺寸 `1600 x 1000`。
- 新增 Keyword Map 版本文件，避免浏览器或 CDN 缓存旧图。

```text
case-folder/beacon-geo-report/beacon-geo-ad-01-keyword-map.png
```

同时更新 `index.html` 第一张图片引用：

```html
<img src="case-folder/beacon-geo-report/beacon-geo-ad-01-keyword-map.png">
```

原文件 `case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png` 可作为源图或回滚参考，不作为上线引用。

### TR-4: 同步图片 alt 与 carousel metadata

产品已确认：从 Prompt Map 改为 Keyword Map 后，需同步更新与第一张 carousel 图片相关的 title、alt、caption、dot aria-label、JS metadata，包括英文和日文 metadata。

当前 alt：

```html
alt="Beacon GEO prompt strategy visual showing buyer prompts and model selection."
```

改为：

```html
alt="Beacon GEO keyword map visual showing buyer questions and model selection."
```

当前 carousel 初始标题：

```html
<p class="beacon-carousel__title" data-beacon-title>Prompt Strategy</p>
```

改为：

```text
Keyword Map
```

日文 carousel title 改为：

```text
キーワードマップ
```

当前 caption：

```html
Start from real buyer questions, not generic keywords.
```

caption 改为：

```text
Map the buyer questions AI will answer.
```

日文 caption 改为：

```text
AIが回答する購買者の質問をマッピングします。
```

以下旧文案不得残留在 `index.html` 的可见文案、aria-label、JS metadata 中：

```text
Prompt Strategy
Show Prompt Strategy visual
Prompt設計
Prompt Map
PROMPT MAP
```

### TR-5: 修改 Download Example Report CTA

示例报告 PDF 已提供。本次开发需要使用该样本作为源文件，并将其放入项目静态发布路径。

源文件：

```text
case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf
```

静态发布路径：

```text
case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf
```

目标实现为新标签页预览，并支持用户在浏览器 PDF viewer 中下载：

```html
<a
  href="case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf"
  class="btn btn--secondary"
  target="_blank"
  rel="noopener"
>
  <span data-en>Download Example Report</span>
  <span data-jp>サンプルレポートをダウンロード</span>
</a>
```

不使用强制 `download` 作为默认行为。

---

## 4. File Changes

### Required

```text
index.html
case-folder/beacon-geo-report/beacon-geo-ad-01-keyword-map.png
case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf
case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf
```

### Source / Reference Only

```text
case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png
```

---

## 5. QA Checklist

### Visual QA

- 顶部导航显示 `Beacon GEO`。
- `Beacon GEO` 导航点击后定位正确。
- 语言切换后，`Beacon GEO` 仍显示正常。
- 新增导航项没有与 logo 或语言切换按钮重叠。
- 第一张图片显示 `KEYWORD MAP`。
- 第一张 carousel 图片引用 `beacon-geo-ad-01-keyword-map.png`，不再引用 `beacon-geo-ad-01-prompt-strategy.png`。
- 图片没有因替换产生模糊、压缩异常或裁切问题。
- CTA 在英文和日文下都不换行溢出。

### Functional QA

- `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` 已复制/重命名到 `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf`。
- CTA href 指向 `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf`。
- 点击 CTA 在新标签页打开 PDF，浏览器 PDF viewer 支持下载。
- 浏览器控制台无资源 404。
- `index.html` 中没有残留可见文案 `What we measure`。
- 没有残留可见文案 `Prompt Map`。
- `index.html` 的可见文案、aria-label、JS metadata 中不得残留 `Prompt Strategy`。
- `index.html` 中不得残留 `Show Prompt Strategy visual`。
- `index.html` 中不得残留日文旧 metadata `Prompt設計`。

### Responsive QA

检查以下视口：

```text
375 x 812
768 x 1024
1024 x 768
1440 x 900
```

重点检查：

- header 不遮挡主要内容。
- Beacon GEO section 锚点跳转后标题没有被 fixed header 完全遮住。
- 按钮组在移动端可自然换行。
- carousel 图片比例正常。

---

## 6. Confirmed Review Decisions

### Decision 1: PDF 路径

已确认：

```text
PDF 样本已提供，源文件为 case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf
开发需将该 PDF 放入项目静态资源目录
最终发布路径固定为 case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf
```

技术要求：CTA href 必须指向 `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf`。不得指向 `outputs/`，因为 `outputs/` 不是页面静态资源目录。

### Decision 2: PDF 打开方式

已确认：

```text
new tab preview
support download through browser PDF viewer
```

技术实现：`target="_blank"` + `rel="noopener"`，不默认添加 `download`。

### Decision 3: 第一张图是否只改视觉大字

已确认同步更新：

- 文件名
- alt text
- carousel title
- carousel dot aria-label
- carousel JS metadata
- 文案中的 `Prompt Strategy`

技术要求：视觉大字、alt、carousel title、dot aria-label、JS metadata/caption 一起改，英文和日文 metadata 都要同步，避免前后口径不一致。

### Decision 4: `Keyword Map` 与 buyer questions 解释

已确认同步修改 caption，并保留 buyer questions 解释，避免被理解成传统 SEO keyword list。

技术要求 caption：

```text
Map the buyer questions AI will answer.
```

日文 caption：

```text
AIが回答する購買者の質問をマッピングします。
```

---

## 7. Technical Risks

### Risk 1: PNG 直接编辑质量不稳定

直接覆盖 PNG 文本可能造成字体或边缘不一致。

**Mitigation:** 使用源图生成流程重新导出；如不可行，至少在 1x 和 2x 显示下做视觉检查。

### Risk 2: PDF 链接上线时间与文件交付不同步

PDF 样本已存在，但如果只保留在 `outputs/`，页面发布时仍可能找不到该文件；CTA 指向错误目录也会出现 404。

**Mitigation:** 开发必须将 `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` 复制/重命名到 `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf`，CTA 只能指向后者，并在发布前检查该路径可访问。

### Risk 3: Header fixed 导航锚点遮挡

点击 `#beacon-geo` 后，fixed header 可能遮住 section 顶部。

**Mitigation:** 如实际发生，给目标 section 增加：

```css
#beacon-geo {
  scroll-margin-top: 72px;
}
```

### Risk 4: 新 nav item 影响中等宽度布局

`Beacon GEO` 比其他导航文案更长，在 768px 附近可能挤压。

**Mitigation:** 降低 nav gap，或把导航显示断点提高到 860px。

### Risk 4b: 旧图片缓存导致 PROMPT MAP 仍显示

如果覆盖原 PNG 路径，浏览器或 CDN 可能继续使用缓存，让用户继续看到 `PROMPT MAP`。

**Mitigation:** 默认使用新文件名 `beacon-geo-ad-01-keyword-map.png`，并更新 `index.html` 图片引用。

### Risk 5: PDF 下载行为依赖浏览器

本次确认采用新标签页预览，用户可通过浏览器 PDF viewer 下载。不同浏览器的 PDF 下载入口位置可能不同。

**Mitigation:** 验收标准定义为“新标签页可正常打开 PDF，浏览器 viewer 支持下载”，不要求强制下载。

---

## 8. Implementation Order

1. 基于原图准备 `case-folder/beacon-geo-report/beacon-geo-ad-01-keyword-map.png`。
2. 修改 `index.html` 顶部导航。
3. 修改 CTA 文案与 PDF 链接。
4. 同步 alt / carousel metadata。
5. 将 `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` 复制/重命名为 `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf`。
6. 本地打开 `index.html` 做视觉检查。
7. 发布前检查无 404、无残留旧文案、移动端无布局破损。
