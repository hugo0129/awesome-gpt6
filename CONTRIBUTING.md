# 贡献指南 / Contributing

[简体中文](CONTRIBUTING.md) | [English](CONTRIBUTING.en.md)

感谢你愿意把案例写下来。**一个能复用的真实案例，比一百条 Prompt 更有价值。**

---

## 三种贡献方式

| 你想做什么 | 怎么做 | 大概耗时 |
| --- | --- | --- |
| 推荐一个别人做的案例 | [Issue → Recommend a Case](https://github.com/hugo0129/awesome-gpt6/issues/new/choose) | 2 分钟 |
| 提交一个自己做的案例 | 复制[模板](templates/case-template.md) → 放进 `cases/` 对应分类 → 提 PR | 20 分钟 |
| 纠错 / 补链接 / 翻译 | 直接提 Issue 或 PR | 随时 |

---

## 提交一个 Case（完整流程）

### 1. 确认它值得收录

对照这六条，命中三条以上就值得写：

| 维度 | 说明 |
| --- | --- |
| Real | 来自真实任务，不是为了演示 AI 而设计 |
| Useful | 真的解决了问题 |
| Reusable | 别人看完能复用 |
| Complete | 有相对完整的过程，不是一句"我让 GPT-6 帮我做了 XX" |
| Insightful | 能带来新方法或新认知 |
| Measurable | 有时间、成本、质量的前后对比 |

一句话标准：**不是"看起来很厉害"，而是"看完之后我也能用"。**

### 2. 选分类

| 分类 | 目录 |
| --- | --- |
| Thinking & Research | `cases/01-thinking-research/` |
| Coding | `cases/02-coding/` |
| Design | `cases/03-design/` |
| Writing & Content | `cases/04-writing-content/` |
| Data & Office | `cases/05-data-office/` |
| Agent & Automation | `cases/06-agent-automation/` |
| Business | `cases/07-business/` |
| Startup & OPC | `cases/08-startup-opc/` |
| Education | `cases/09-education/` |
| Industry | `cases/10-industry/` |

拿不准选哪个，就选"这个案例最核心的价值发生在哪个环节"，在 PR 里说明即可，我们会帮忙调。

### 3. 建文件

```bash
git clone https://github.com/<你的 ID>/awesome-gpt6.git
cd awesome-gpt6
git checkout -b case/<简短英文名>
cp templates/case-template.md cases/02-coding/from-idea-to-webapp.md
```

命名规则：

- 英文 kebab-case，小写，用连字符：`from-idea-to-webapp.md`
- 别用中文文件名、空格、日期前缀
- 一个 Case 一个文件，不要合并

### 4. 写正文

模板在 [`templates/case-template.md`](templates/case-template.md)（[English](templates/case-template.en.md)），照着填即可。

**文件开头请加 front matter**，方便日后建立索引和网站：

```yaml
---
title: 从想法到上线：一个人用 GPT-6 做完一个 Web App
category: coding
tags: [GPT-6, Codex, Vibe Coding, Web App]
author: your-github-id
date: 2026-09-05
lang: zh
source_url: https://example.com/original-post   # 可选，原文链接
metrics:                                        # 可选，有数据就填，没有就删掉
  time_before: 8h
  time_after: 45min
---
```

`lang` 填 `zh` 或 `en`。中文案例请在标题下加一行英文摘要，反之亦然：

```markdown
> English summary: How one person shipped a full web app with GPT-6 in 45 minutes instead of 8 hours.
```

### 5. 提交 PR

```bash
git add cases/02-coding/from-idea-to-webapp.md
git commit -m "case(coding): add from-idea-to-webapp"
git push origin case/from-idea-to-webapp
```

然后开 PR，标题建议用 `case(<分类>): <案例名>`。

PR 里回答三个问题就行（模板会自动带出来）：

1. 这个 Case 解决了什么问题？
2. 别人能复现吗？（能 / 部分能 / 不能，为什么）
3. 有没有可量化的结果？

---

## 提交前自查

- [ ] 文件放在了正确的分类目录
- [ ] 文件名是英文 kebab-case
- [ ] 填了 front matter（`title` / `category` / `author` / `date` / `lang`）
- [ ] 至少写清了 Problem、GPT-6 Workflow、Result 三部分
- [ ] 有可量化结果就填了 `metrics`，没有就不编
- [ ] 引用他人内容时标注了出处和链接
- [ ] 没有贴密钥、内网地址、客户信息、个人隐私

最后一条是硬性的：**案例要真实，但不能泄露不该公开的东西。** 敏感信息请脱敏后再写。

---

## 会被拒的几种情况

- 只有结果没有过程（"我用 GPT-6 做了个网站，很好用"）
- 纯 Prompt 分享，没有场景和结果
- 明显是模型自己编的、没有真实发生的演示
- 直接搬运他人内容且不注明出处
- 软文或产品广告

被拒不等于案例没价值，通常只是信息不完整。补全过程后欢迎再提一次。

---

## 只推荐，不写

完全没问题。点 [New Issue](https://github.com/hugo0129/awesome-gpt6/issues/new/choose) → **Recommend a Case**，填这几项：

```text
Case Name:

Case URL:

Category:

What problem does it solve?

Why is it awesome?

Can others reproduce it?
```

我们会去核实并整理成正式案例，你依然会被记在 Contributors 里。

---

## 其他能帮上忙的地方

- 给已有案例补充 Prompt / Workflow / 结果
- 把中文案例翻译成英文摘要（或反之）
- 修正失效链接、错别字、错误分类
- 提出新的分类建议
- 帮我们 Review PR

---

## 行为准则

就三条：**说实话、对事不对人、别打广告。**

案例里请如实描述 AI 做到什么程度、哪些部分仍然靠人。夸大效果的案例会伤害整个仓库的可信度，这是唯一会被直接关闭的情况。

---

## License

提交 PR 即表示你同意：

1. 你的内容以 [CC BY 4.0](LICENSE) 发布；
2. 授权本仓库收录、展示和传播；
3. 你拥有所提交内容的权利，或已获得原作者授权。
