# 提交类型 / Type of change

- [ ] 新增案例 / New case
- [ ] 补充或修订已有案例 / Update an existing case
- [ ] 修正错误 / 失效链接 / Fix error or dead link
- [ ] 翻译 / Translation
- [ ] 文档与流程改进 / Docs or process improvement

# 案例信息 / About the case

（非案例提交可不填 / Skip if this isn't a case submission）

- 分类 / Category：
- 文件 / File：`cases/xx-xxxx/xxxx.md`

**1. 这个 Case 解决了什么问题？/ What problem does it solve?**

**2. 别人能复现吗？/ Can others reproduce it?**

能 / Yes · 部分能 / Partly · 不能 / No —— 原因 / why：

**3. 有没有可量化的结果？/ Any measurable results?**

<!-- 有就填真实数据，没有就不填。不要编。Real numbers only, or leave blank. -->

# 自查 / Checklist

- [ ] 文件放在了正确的分类目录 / File is in the correct category folder
- [ ] 文件名是英文 kebab-case / Filename is English kebab-case
- [ ] 填了 front matter（`title` / `category` / `author` / `date` / `lang`）
- [ ] 写清了 Problem、GPT-6 Workflow、Result 三部分
- [ ] 引用他人内容已注明出处和链接 / Third-party content is credited
- [ ] 没有密钥、内网地址、客户信息、个人隐私 / No secrets, internal URLs or personal data
- [ ] 如果新增案例，已运行 `python3 scripts/generate_index.py` 更新索引（可选，CI 会检查）
      If adding a case, ran the index script (optional; CI checks it anyway)

# 授权 / License

提交本 PR 即表示同意内容以 [CC BY 4.0](../LICENSE) 发布，并授权本仓库收录与展示。
By submitting this PR you agree to publish your content under [CC BY 4.0](../LICENSE).
