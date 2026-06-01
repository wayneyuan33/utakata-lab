# Beacon GEO Landing Page PRD

## UTAKATA LAB 首页首推内容与 Blog 更新

**Version:** 1.0  
**Date:** 2026-05-30  
**Status:** Implemented (homepage module + 3 blog posts inline)  
**Owner:** UTAKATA LAB  

---

## 1. 结论与策略判断

你的方向是对的：不要一上来卖“复杂平台”，先卖一次性的 **AI Visibility Report**。

Beacon GEO 目前看起来已经具备平台能力：项目、Prompt 生成、模型采集、Coverage / SOV / Recommendation Rate、竞品对比、趋势、CSV 导出等。但对于 UTAKATA LAB 的首页访客来说，直接卖平台会带来三个问题：

- 理解成本高：用户还没建立“为什么要监控 AI 可见性”的需求，就被带进了产品功能。
- 信任门槛高：平台意味着长期订阅、数据接入、流程改变，而初次接触更适合低风险诊断。
- 销售路径长：用户更容易先购买或咨询一份报告，再理解是否需要持续监控。

因此，首页首推模块建议聚焦为：

> **AI Visibility Report Tool: Beacon GEO**  
> See how AI answer engines describe, compare, and recommend your brand.

对外不先说“平台”，而是说：

> We run a structured AI visibility report for your brand, category, and competitors.

Beacon GEO 作为背后的工具和方法论出现。用户先买“结果”，不是买“系统”。

---

## 2. 本次更新目标

### 2.1 Business Goal

把 UTAKATA LAB 首页从“展示能力与观点”推进到“明确的可咨询产品入口”，让访客看到一个可以立刻询问、购买、试做的服务：

- 单次 AI Visibility Report
- 企业 / 品牌 / 竞品的 GEO 可见性诊断
- 可用于 CMO、SEO/GEO team、content team、agency client report

### 2.2 User Goal

让访客在 30 秒内理解：

- GEO 是什么问题
- 为什么 AI 回答里的品牌可见性值得测量
- Beacon GEO 能输出什么样的报告
- 如果需要报告，应该如何联系 UTAKATA LAB

### 2.3 Page Goal

新增一个位于 Hero 下方、Work 前方的置顶模块：

**AI Visibility Report Tool: Beacon GEO**

并新增两篇 Writing / Blog：

1. GEO 概念解释：什么是 GEO，以及企业如何看到自己的 GEO 情况
2. Beacon GEO 产品推介软广：如果需要 AI Visibility Report，可以联系 UTAKATA LAB

---

## 3. 信息架构更新

当前首页结构：

1. Hero
2. Work
3. Writing
4. Contact

建议更新为：

1. Hero
2. **Featured Offer: AI Visibility Report Tool: Beacon GEO**
3. Work
4. Writing
5. Contact

导航可暂时保持不变，不新增 Beacon GEO 导航项。因为模块位于 Hero 下方首屏之后，用户自然会看到。后续如果模块表现好，再考虑增加 nav item：

- EN: Report
- JP: レポート

---

## 4. 新增首推模块 PRD

### 4.1 Section Purpose

这个模块不是产品功能页，而是一个“轻量销售入口”。

它要完成三件事：

- 把 GEO 从抽象概念转成可测量的问题
- 展示 Beacon GEO 能生成怎样的数据与报告
- 引导用户联系 UTAKATA LAB 获取一次性 AI Visibility Report

### 4.2 Section Placement

位置：Hero section 后，Portfolio / Work section 前。

模块 ID 建议：

```html
id="beacon-geo"
```

### 4.3 Section Label

EN:

```text
Featured Report
```

JP:

```text
注目レポート
```

### 4.4 Module Title

EN:

```text
AI Visibility Report Tool: Beacon GEO
```

JP:

```text
AI可視性レポートツール：Beacon GEO
```

### 4.5 Lead Copy

EN:

```text
Find out how AI answer engines describe, compare, and recommend your brand before your buyers do.
```

JP:

```text
購入者がAIに尋ねる前に、AIがあなたのブランドをどう説明し、比較し、推薦しているかを把握します。
```

### 4.6 Supporting Copy

EN:

```text
Beacon GEO helps us run structured AI visibility reports across real buyer prompts, competitor entities, and multiple AI answer engines. Instead of guessing whether your brand appears in AI answers, we measure coverage, share of voice, recommendation signals, and content opportunities.
```

JP:

```text
Beacon GEO は、実際の購買者に近い Prompt、競合ブランド、複数の AI 回答エンジンをもとに、AI検索におけるブランド可視性を測定するためのレポートツールです。AI回答に自社ブランドが表示されているか、どれほど推薦されているか、競合と比べてどのような状態かを可視化します。
```

### 4.7 CTA

Primary CTA:

EN:

```text
Request an AI Visibility Report
```

JP:

```text
AI可視性レポートを相談する
```

Link:

```text
mailto:utakatalab.hello@gmail.com?subject=AI%20Visibility%20Report%20Inquiry
```

Secondary CTA:

EN:

```text
See what the report measures
```

JP:

```text
測定内容を見る
```

Behavior: scrolls to the metric / report deliverable area within the same section.

### 4.8 Key Proof Points

Use four compact proof points, preferably as simple text blocks rather than heavy cards.

1. **Coverage**  
   Measures whether your brand appears in AI-generated answers.

2. **Share of Voice**  
   Compares your brand presence against competitors across answer appearances.

3. **Recommendation Signals**  
   Identifies whether AI explicitly recommends your brand or favors competitors.

4. **Prompt-Level Evidence**  
   Preserves raw AI answers and structured findings for reporting and content planning.

### 4.9 Report Packaging

Position the offer as a report, not a subscription.

Recommended public-facing package:

```text
One-time AI Visibility Report
```

Suggested included items:

- Brand and competitor setup
- Prompt set design or calibration
- AI answer collection across selected models
- Coverage, Share of Voice, Recommendation Rate
- Entity comparison table
- Raw answer evidence
- Content opportunity findings
- Executive summary and next-step recommendations

Optional internal package tiers:

| Package | Scope | Best For |
| --- | --- | --- |
| Starter Report | 1 brand, 3-5 competitors, 20-30 prompts, 1 market/language | First diagnosis |
| Category Benchmark | 1 brand, 5-8 competitors, 50-80 prompts, 2-3 models | Competitive category scan |
| Agency / Client Report | Multiple tracks, exportable data, executive report support | Client deliverables |

Pricing can stay off-page for now. Use “contact us” until the offer is validated.

---

## 5. Visual Recommendation

### 5.1 Recommended Direction

For v1, use an **ad-style product visual carousel**.

This is the recommended first-launch format because:

- It is more controllable: every visual can state one clear value point.
- It avoids exposing loading states, internal test data, or accidental product details.
- It matches the UTAKATA LAB site tone better: calm, editorial, evidence-led.
- It lets the user inspect each screen at their own pace.
- It can later be reused as a sales deck, proposal insert, or social preview asset.

The page should not feel like a SaaS product tour. It should feel like a short report preview.

### 5.2 Ad-Style Product Visual Carousel

Recommended component:

```text
4-slide horizontal carousel / stepper
```

Each slide should include:

- The prepared ad-style product visual
- Short accessible alt text
- Optional title / caption outside the image only if needed

Controls:

- Previous / next arrows
- Four step dots
- Optional auto-advance every 4-5 seconds
- Pause auto-advance when hovered or focused
- Keyboard accessible buttons

Mobile:

- Swipeable horizontal carousel
- Show one slide at a time
- Do not duplicate long explanatory copy below every image
- Keep the visual large enough that it reads as a homepage ad asset, not a small embedded slide

### 5.3 Slide Storyboard

Use the prepared product visuals as the basis, but frame each screen as a report-building step:

1. **Prompt Strategy Setup**  
   Show prompt types, model selection, Excel import/export, and generated prompts.  
   Slide copy: “Turn buyer questions into structured AI visibility tests.”

2. **Capture Running**  
   Show the collection progress screen.  
   Slide copy: “Collect answers from selected AI models.”

3. **Track Dashboard**  
   Show Coverage, SOV, Recommendation Rate, competitor comparison, and entity table.  
   Slide copy: “Measure brand visibility against competitors.”

4. **Aggregate Dashboard**  
   Show cross-track aggregate view and trend / SOV widgets.  
   Slide copy: “Turn AI answers into an executive-ready report.”

### 5.4 Slide Copy Draft

Slide 1:

```text
Prompt Strategy
Start from real buyer questions, not generic keywords.
```

Slide 2:

```text
AI Answer Capture
Collect answers across selected models and markets.
```

Slide 3:

```text
Visibility Metrics
Measure Coverage, Share of Voice, and Recommendation Rate.
```

Slide 4:

```text
Report Output
Compare entities, preserve evidence, and identify content opportunities.
```

## 6. Asset Requirements

Source assets provided:

- Project Aggregate Dashboard screenshot
- AI Answer Capture Progress screenshot
- Track Dashboard and Entity Comparison screenshot
- Prompt Review and Model Selection screenshot

Recommended site asset folder:

```text
case-folder/beacon-geo-report/
```

Recommended filenames:

```text
case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png
case-folder/beacon-geo-report/beacon-geo-ad-02-ai-answer-capture.png
case-folder/beacon-geo-report/beacon-geo-ad-03-visibility-metrics.png
case-folder/beacon-geo-report/beacon-geo-ad-04-report-output.png
```

Implementation note: these four assets are already generated in the site folder. Use these exact local paths in `index.html`; do not point to external image sources.

The source product-panel crops used to regenerate the ads are stored here:

```text
case-folder/beacon-geo-report/source-panels/beacon-geo-ui-01.png
case-folder/beacon-geo-report/source-panels/beacon-geo-ui-02.png
case-folder/beacon-geo-report/source-panels/beacon-geo-ui-03.png
case-folder/beacon-geo-report/source-panels/beacon-geo-ui-04.png
```

The reproducible asset generation script is:

```text
tools/create_beacon_geo_ads.py
```

### 6.1 Prompt for Web Content and Development Agent

```text
You are responsible for updating the UTAKATA LAB homepage content and implementation for the new Beacon GEO featured module.

Please use the four prepared Beacon GEO homepage ad visuals exactly from these local paths:

1. case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png
2. case-folder/beacon-geo-report/beacon-geo-ad-02-ai-answer-capture.png
3. case-folder/beacon-geo-report/beacon-geo-ad-03-visibility-metrics.png
4. case-folder/beacon-geo-report/beacon-geo-ad-04-report-output.png

Important visual guidance:
- These are no longer PPT-style slides. Treat them as homepage advertising / product proof visuals.
- Do not recreate the old screenshot-heavy PPT look with many text labels, metric chips, or long captions.
- The images already contain the intended ad copy, product screenshot, spacing, and color treatment.
- Do not crop them in a way that cuts off text, product UI, the left accent stripe, or the right cream shape.
- Use `object-fit: contain` or a stable aspect-ratio container if needed; avoid `object-fit: cover` for these assets.
- Keep the carousel / visual area large enough that the product screen is visibly real evidence, not decoration.
- On mobile, show one visual at a time and prevent text, controls, and image edges from overlapping.
- Add useful alt text for each image, but keep visible captions short or omit them if the module copy already explains the offer.

Color and layout guidance:
- The assets use a deep sage / forest background so they intentionally differ from the homepage warm cream background while staying inside the UTAKATA LAB “Long Light” palette.
- Do not add additional bright blue, cyan, green, purple, or gradient treatments around the carousel.
- Use existing site tokens where possible: deep forest, sage dark, warm cream, Soft Ember, Pale Dusk.
- The Beacon GEO section should still sell a one-time AI Visibility Report, not a SaaS platform subscription.

Content / implementation checks before completion:
- Place the Beacon GEO module immediately below Hero and before Work.
- CTA should open: mailto:utakatalab.hello@gmail.com?subject=AI%20Visibility%20Report%20Inquiry
- Follow the updated Tech PRD language strategy: bilingual copy uses `data-en` / `data-jp`, without `hidden` on bilingual nodes.
- Verify desktop and mobile: no overlapping text, no cropped carousel controls, no image clipping, and at least one Beacon GEO visual is visible without user interaction.
- Update any old wording that calls these “PPT-style screenshot slices”; call them “ad-style product visuals” or “Beacon GEO product visuals.”
```

---

## 7. Suggested Layout

### 7.1 Desktop

Use a two-column editorial layout:

- Left: copy, proof points, CTA
- Right: ad-style Beacon GEO product visual carousel

The visual should feel like evidence, not decoration. Beacon GEO is a dashboard/report product, so the screen itself should be visible and readable.

### 7.2 Mobile

Stack order:

1. Label
2. Title
3. Lead copy
4. CTA
5. Screenshot carousel
6. Proof points
7. Report deliverables

Do not hide the report deliverables on mobile. They are key to making the offer concrete.

### 7.3 Visual Tone

The existing UTAKATA site uses a warm, restrained “Long Light” palette. Beacon GEO screenshots are dark blue/black product UI, so the module should bridge them carefully:

- Keep the page background warm cream
- Use dark product screenshot as the visual anchor
- Use thin borders and restrained labels
- Avoid making the whole section a dark tech block
- Use the existing ember accent for CTA

---

## 8. Blog Update PRD

The current Writing section uses inline expandable blog posts. New posts should follow the same accordion pattern.

Content status: the two new Blog posts below now have complete EN / JP final body copy.

Use these final copy source files for implementation:

```text
blog-02-what-is-geo-and-how-can-a-company-measure-it.md
blog-03-beacon-geo-turning-ai-answers-into-a-brand-visibility-report.md
```

Implementation should prepare the Writing accordion structure, ordering, titles, summaries, CTA slots, and full article bodies from these files. It must not ship outline-only or placeholder article bodies as final public Blog content.

Add two new posts above or below the existing “What does an AI say about your brand?” post. Recommended order:

1. What is GEO?
2. AI Visibility Report Tool: Beacon GEO
3. Existing post: What does an AI say about your brand?

Alternative order if you want softer selling:

1. Existing post
2. What is GEO?
3. Beacon GEO

I recommend the first order if Beacon GEO becomes the new homepage lead.

---

## 9. Blog Post 1 PRD

### 9.1 Purpose

Educational article. It should explain GEO without sounding like a buzzword explainer.

### 9.2 Working Title

EN:

```text
What is GEO, and how can a company measure it?
```

JP:

```text
GEOとは何か。企業はAI検索での見え方をどう測るべきか
```

### 9.3 Summary

EN:

```text
GEO is not just another SEO acronym. It is the practice of understanding how AI answer engines describe, compare, and recommend your brand.
```

JP:

```text
GEOは単なるSEO用語ではありません。AI回答エンジンがブランドをどう説明し、比較し、推薦しているかを把握するための考え方です。
```

### 9.4 Article Structure

1. Opening: buyers are asking AI instead of only searching Google
2. Definition: GEO means Generative Engine Optimization
3. Difference from SEO: ranking pages vs appearing inside answers
4. What companies should measure:
   - brand coverage
   - share of voice
   - recommendation rate
   - positioning accuracy
   - competitor mentions
   - content gaps
5. How to run a simple first diagnosis:
   - choose category
   - define competitors
   - write buyer prompts
   - test across models
   - collect and compare answers
6. Why manual checking is not enough:
   - too many prompts
   - answers vary by model
   - evidence needs to be preserved
   - teams need repeatable reporting
7. Closing: GEO turns AI visibility from a feeling into a measurable marketing signal

### 9.5 Soft CTA

EN:

```text
If you want to understand how your brand appears in AI answers, UTAKATA LAB can run a structured AI Visibility Report using Beacon GEO.
```

JP:

```text
AI回答の中で自社ブランドがどのように表示されているかを把握したい場合、UTAKATA LAB は Beacon GEO を使った AI可視性レポートを作成できます。
```

---

## 10. Blog Post 2 PRD

### 10.1 Purpose

Product-led soft advertorial. It should introduce Beacon GEO through the report use case, not through a feature checklist.

### 10.2 Working Title

EN:

```text
Beacon GEO: turning AI answers into a brand visibility report
```

JP:

```text
Beacon GEO：AI回答をブランド可視性レポートに変える
```

### 10.3 Summary

EN:

```text
Beacon GEO helps turn buyer prompts, AI answers, and competitor mentions into a structured report for marketing and content teams.
```

JP:

```text
Beacon GEO は、購買者のPrompt、AI回答、競合言及を、マーケティングチームが使える構造化レポートへ変換します。
```

### 10.4 Article Structure

1. Opening: most teams have anecdotes about AI answers, but not a reporting system
2. What the report answers:
   - Does AI mention our brand?
   - Does AI recommend us?
   - Which competitors appear more often?
   - What language does AI use to describe each player?
   - Which prompts reveal content gaps?
3. How Beacon GEO works:
   - define project, brand, competitors, market, language
   - generate or import prompts
   - review and calibrate prompt set
   - collect answers from selected models
   - analyze coverage, SOV, recommendation, entity comparison
   - export data and report findings
4. What the dashboard shows:
   - aggregate visibility
   - track dashboard
   - prompt evidence
   - entity comparison
5. Who the report is for:
   - CMO / VP Marketing
   - SEO/GEO team
   - content marketing team
   - agency / consultant
   - sales enablement
6. Closing CTA: contact UTAKATA LAB for a first report

### 10.5 CTA

EN:

```text
If you need a first AI Visibility Report for your brand, contact UTAKATA LAB. We can help define the prompt set, run the analysis, and turn the findings into practical content and positioning recommendations.
```

JP:

```text
自社ブランドの AI可視性レポートが必要な場合は、UTAKATA LAB までご相談ください。Prompt設計、分析実行、コンテンツ改善・ポジショニング改善の提案まで支援できます。
```

---

## 11. Content and Copy Rules

Follow the current UTAKATA LAB voice:

- Warm, precise, not hype-driven
- Avoid “future of search” style overclaiming
- Avoid overusing AI acronyms without explanation
- Explain GEO through buyer behavior and reporting needs
- Keep Beacon GEO as a practical tool, not a grand platform promise

Words to avoid:

- revolutionary
- cutting-edge
- unlock
- empower
- next-generation
- AI-powered everything

Preferred language:

- measure
- compare
- report
- evidence
- buyer prompts
- answer engines
- visibility
- recommendation
- content opportunity

---

## 12. Implementation Scope

### 12.1 In Scope

- Add new Beacon GEO featured module below Hero
- Add four ad-style Beacon GEO product visual assets
- Add primary CTA to email
- Add two new inline expandable blog posts using the final EN / JP body copy files
- Add bilingual EN / JP content for module and blog cards
- Keep the existing static site architecture

### 12.2 Out of Scope

- Full Beacon GEO product page
- Pricing table
- Payment flow
- Lead form backend
- CMS integration
- Platform login / product access

---

## 13. Acceptance Criteria

The update is complete when:

- Beacon GEO module appears immediately below Hero on desktop and mobile
- The module clearly sells a one-time AI Visibility Report, not only a platform
- CTA opens an email inquiry with relevant subject line
- An ad-style product visual carousel shows the four Beacon GEO report-building steps
- At least one product visual is visible without needing user interaction
- Carousel controls are usable on desktop and mobile
- Two new blog posts appear in the Writing section
- Both new Blog posts have complete EN / JP final body copy written from the outlines
- Outline-only or placeholder Blog content is not allowed in final launch acceptance
- Blog posts expand and collapse using the existing interaction pattern
- EN / JP language toggle works for all new copy
- No text overlaps on mobile
- Product screenshots are readable enough to communicate real dashboard evidence

---

## 14. Recommended Next Step

Implementation can proceed for the homepage Beacon GEO module, carousel, and final Blog insertion using the four prepared ad-style product visuals in this sequence:

1. Prompt Map: `case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png`
2. Answer Run: `case-folder/beacon-geo-report/beacon-geo-ad-02-ai-answer-capture.png`
3. Visibility Lens: `case-folder/beacon-geo-report/beacon-geo-ad-03-visibility-metrics.png`
4. Report View: `case-folder/beacon-geo-report/beacon-geo-ad-04-report-output.png`

Launch with the carousel as the final v1 visual format.
