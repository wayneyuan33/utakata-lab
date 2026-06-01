# Beacon GEO Site Update PRD

## 顶部导航、示意图命名、示例报告下载入口

**Version:** 1.0  
**Date:** 2026-05-30  
**Status:** Implemented - verified against index.html (2026-06-01)  
**Owner:** UTAKATA LAB  
**Related Page:** `index.html`  
**Related Existing PRD:** `beacon-geo-landing-prd.md`

---

## 1. 背景

UTAKATA LAB 首页已经新增 Beacon GEO 作为首推产品模块，定位为：

> AI Visibility Report Tool: Beacon GEO

当前页面仍有三个需要补齐或调整的地方：

1. 顶部导航没有 Beacon GEO 入口，用户需要向下滚动才会看到首推产品。
2. 第一张产品示意图左侧大标题仍为 `PROMPT MAP`，需要改为 `KEYWORD MAP`。
3. Beacon GEO 模块中的次级按钮目前是 `What we measure`，需要改成 `Download Example Report`，并在本次开发中链接到已提供的示例报告 PDF。

这三个改动的共同目标是：让 Beacon GEO 在首页上更像一个明确可进入、可理解、可下载样本的主推产品，而不是仅作为页面中部的一段介绍。

---

## 2. 产品目标

### 2.1 Business Goal

- 提高 Beacon GEO 首推产品在首页的可见性。
- 让访客从顶部导航即可直接跳转到 Beacon GEO 模块。
- 将产品表达从内部工作流语言 `Prompt Map` 调整为更容易被市场、SEO、内容团队理解的 `Keyword Map`。
- 为 PDF 示例报告建立明确下载入口，降低咨询前的信息门槛。

### 2.2 User Goal

访客应能在进入首页后快速完成以下动作：

- 从顶部菜单看到 `Beacon GEO`。
- 点击后直接跳转到首页的 Beacon GEO 首推模块。
- 从视觉素材中理解第一步是围绕关键词 / buyer questions 规划 AI visibility 测量范围。
- 点击 `Download Example Report` 下载或查看示例报告 PDF。

### 2.3 Page Goal

首页导航从当前：

1. Work
2. Writing
3. Contact

更新为：

1. Beacon GEO
2. Work
3. Writing
4. Contact

Beacon GEO 按钮目标为当前首页模块：

```text
#beacon-geo
```

---

## 3. Scope

### 3.1 In Scope

- 顶部导航新增 `Beacon GEO` 链接。
- `Beacon GEO` 链接锚点跳转到首页首推产品模块。
- 桌面端导航可正常显示新增菜单项。
- 移动端保持当前导航策略；如当前移动端隐藏导航，则不额外新增移动菜单。
- 将第一张 Beacon GEO 产品示意图中的 `PROMPT MAP` 改为 `KEYWORD MAP`。
- 新增第一张示意图的 Keyword Map 版本文件并在首页引用新文件，避免浏览器或 CDN 继续缓存旧图。
- 将按钮文案从 `What we measure` 改为：
  - EN: `Download Example Report`
  - JP: `サンプルレポートをダウンロード`
- 使用已提供的 PDF 样本作为示例报告来源文件。
- 本次开发中将 PDF 样本放入正确的静态发布路径，并写入页面真实链接。
- 按钮应可直接打开或下载该 PDF。

### 3.2 Out of Scope

- 新增独立 Beacon GEO 产品页。
- 新增报告申请表单后端。
- 新增登录、支付、订阅或 SaaS dashboard 入口。
- 制作完整示例 PDF 报告正文；本次直接使用已提供的匿名样本 PDF。
- 重新设计整个 Beacon GEO 模块。
- 重写已有 Blog 内容。

---

## 4. Functional Requirements

### FR-1: 顶部导航新增 Beacon GEO

顶部导航增加一个 `Beacon GEO` 链接，并放在第一位，位于 `Work` 之前。

**Rationale:** Beacon GEO 是当前首页主推产品，应该优先于作品集和文章入口。

**Expected behavior:**

- 点击 `Beacon GEO` 后滚动到 `section#beacon-geo`。
- URL hash 更新为 `#beacon-geo`。
- 语言切换时该菜单项保持 `Beacon GEO`，不需要翻译。

### FR-2: Prompt Map 改为 Keyword Map

将以下图片中的大标题：

```text
PROMPT MAP
```

改为：

```text
KEYWORD MAP
```

原始图片：

```text
case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png
```

开发目标图片：

```text
case-folder/beacon-geo-report/beacon-geo-ad-01-keyword-map.png
```

**Expected behavior:**

- 首页 carousel 第一张图中不再出现 `PROMPT MAP`。
- 新图视觉风格应与原图一致，包括字体、字号、位置、颜色、背景和整体比例。
- 默认新建 `beacon-geo-ad-01-keyword-map.png` 并同步更新 `index.html` 第一张 carousel 图片引用。
- 与第一张图相关的 carousel title、alt text、dot aria-label、JS metadata/caption 也需同步改为 Keyword Map 口径。

### FR-3: CTA 改为 Download Example Report

当前按钮：

```text
What we measure
```

改为：

```text
Download Example Report
```

日文：

```text
サンプルレポートをダウンロード
```

**Expected behavior:**

- 点击按钮在新标签页打开 PDF 示例报告，用户可在浏览器 PDF viewer 中下载。
- 示例报告 PDF 已提供，开发输入源文件为：

```text
outputs/GEO_Monitoring_Report_Sample_Anonymized.pdf
```

- 开发需要将该 PDF 复制/重命名到项目静态发布路径：

```text
case-folder/beacon-geo-report/beacon-geo-example-report.pdf
```

- 按钮必须使用明确的 `href` 指向上述静态发布路径。
- 发布前必须验证该路径可访问，不允许上线会 404 的 CTA。

---

## 5. Copy Requirements

### 5.1 Navigation

EN:

```text
Beacon GEO
```

JP:

```text
Beacon GEO
```

### 5.2 CTA

EN:

```text
Download Example Report
```

JP:

```text
サンプルレポートをダウンロード
```

### 5.3 Carousel Metadata for First Visual

EN title:

```text
Keyword Map
```

JP title:

```text
キーワードマップ
```

EN caption:

```text
Map the buyer questions AI will answer.
```

JP caption:

```text
AIが回答する購買者の質問をマッピングします。
```

## 6. Acceptance Criteria

- 顶部导航桌面端显示 `Beacon GEO / Work / Writing / Contact`。
- `Beacon GEO` 点击后跳转到 Beacon GEO 首推模块。
- 页面中第一张 Beacon GEO 示意图显示 `KEYWORD MAP`，不再显示 `PROMPT MAP`。
- 第一张 carousel 的 title / caption / alt / aria-label / JS metadata 使用 Keyword Map 口径，并包含 EN/JP 对应文案。
- Beacon GEO 模块次级按钮显示 `Download Example Report` / `サンプルレポートをダウンロード`。
- 示例报告 PDF 源文件 `outputs/GEO_Monitoring_Report_Sample_Anonymized.pdf` 已被放入静态发布路径 `case-folder/beacon-geo-report/beacon-geo-example-report.pdf`。
- 按钮 href 指向 `case-folder/beacon-geo-report/beacon-geo-example-report.pdf`。
- 点击按钮在新标签页正常打开 PDF，浏览器 PDF viewer 支持下载，不出现 404。
- 英日双语切换后，导航与按钮文案显示正常。
- 桌面端和移动端没有导航换行遮挡、按钮溢出、图片裁切异常。

---

## 7. 已确认的审阅结论

以下为已确认决策：

1. **导航位置**
   - 已确认 `Beacon GEO` 放在顶部导航第一位，位于 `Work` 之前。
   - `Beacon GEO` 保留英文品牌名，不做日文翻译。

2. **Keyword Map 的命名**
   - 已确认视觉大标题改成 `KEYWORD MAP`。
   - 已确认 carousel title / alt / caption / aria-label / metadata 同步修改为 Keyword Map 口径。
   - 已确认默认使用新图片文件 `beacon-geo-ad-01-keyword-map.png`，降低旧图缓存风险。

3. **PDF 路径与交付方式**
   - 已确认 PDF 样本已提供，源文件为 `outputs/GEO_Monitoring_Report_Sample_Anonymized.pdf`。
   - 开发需将该样本放入项目静态资源目录：`case-folder/beacon-geo-report/beacon-geo-example-report.pdf`。
   - 页面 CTA href 必须指向该静态发布路径。

4. **PDF 打开方式**
   - 已确认使用新标签页打开 PDF 预览。
   - 用户可在浏览器 PDF viewer 中下载。
   - 技术实现使用 `target="_blank"` + `rel="noopener"`，不强制加 `download`。

5. **示例报告文件名**
   - 默认使用：`beacon-geo-example-report.pdf`
   - 文件名应保持英文、无空格，便于静态站部署和链接维护。

---

## 8. 风险提示

### Risk 1: PDF 发布路径与页面链接不同步

PDF 样本已经提供，主要风险从“文件未完成”变为“源文件没有复制到页面引用的静态发布路径”，从而导致 404。

**Mitigation:** 开发必须将 `outputs/GEO_Monitoring_Report_Sample_Anonymized.pdf` 放入 `case-folder/beacon-geo-report/beacon-geo-example-report.pdf`，并在发布前验证 CTA 可打开该 PDF。

### Risk 2: `Keyword Map` 与产品真实方法论不完全一致

Beacon GEO 实际测量的是 prompts / buyer questions / AI answer scenarios，不只是传统 SEO keyword。如果只写 `Keyword Map`，可能更易懂，但也可能让专业用户误以为这是传统关键词工具。

**Mitigation:** 在 caption 或旁边文案中保留 buyer questions / AI prompts 的解释。

### Risk 3: 顶部导航新增项造成窄屏拥挤

桌面宽度较小时，新增导航项可能与 logo、语言切换按钮拥挤。

**Mitigation:** 检查 768px、1024px、1440px 视口；必要时缩小 nav gap 或调整断点。

### Risk 4: 图片文字修改后视觉不一致

如果直接在 PNG 上覆盖文字，字体、抗锯齿、位置、颜色可能与原图不一致。

**Mitigation:** 优先使用原素材生成脚本或源文件重新生成；如只能编辑 PNG，应进行视觉 QA。

### Risk 4b: 图片缓存导致用户仍看到旧的 PROMPT MAP

如果覆盖原文件 `beacon-geo-ad-01-prompt-strategy.png`，浏览器或静态托管/CDN 可能继续返回旧图。

**Mitigation:** 默认生成新文件 `beacon-geo-ad-01-keyword-map.png`，并更新 `index.html` 图片引用。

### Risk 5: 直接下载 PDF 可能被部分浏览器改为预览

本次确认采用新标签页预览，用户可通过浏览器 PDF viewer 下载。不同浏览器的下载按钮位置和体验可能略有不同。

**Mitigation:** 将验收标准写为“新标签页可正常打开 PDF，并支持用户在浏览器 PDF viewer 中下载”，不要求强制下载。

---

## Implementation record (2026-06-01)

- Navigation: `index.html` includes a Beacon GEO nav link targeting `#beacon-geo`.
- Keyword Map asset: the first carousel visual uses `case-folder/beacon-geo-report/beacon-geo-ad-01-keyword-map.png`.
- PDF CTA: `index.html` links `Download Example Report` to `case-folder/beacon-geo-report/beacon-geo-example-report.pdf` with `target="_blank"` and `rel="noopener"`.