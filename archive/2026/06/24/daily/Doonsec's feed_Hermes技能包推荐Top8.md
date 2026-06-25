---
title: Hermes技能包推荐Top8
url: https://mp.weixin.qq.com/s/k7Gxjm5-smJmHNUhpoII8w
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:15.057984
---

# Hermes技能包推荐Top8

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N46S2sKsyIBhsMJFP6Xw8ay9hboiazUeAsddyVwp7KuiametXl4Kpx4jPEdOwvQicqw8mwEQ8QlX7rap10ibwOd5QrdcWPBglQjYd7Y19A4Eibnk/0?wx_fmt=jpeg)

# Hermes技能包推荐Top8

原创

ladon
ladon

306Safe

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Hermes Agent的技能包（Skill）生态正在爆发式增长。本文精选8个最实用的技能包，覆盖内容创作、编程、数据分析、安全扫描等高频场景，附带安装方法和安全注意事项。

技能包安装通用方法

```
# 从官方市场安装 hermes skill install <skill-name>  # 从GitHub仓库安装 hermes skill install https://github.com/user/skill-name  # 从本地路径安装 hermes skill install ./my-skill  # 查看已安装技能 hermes skill list  # 更新技能 hermes skill update <skill-name>  # 卸载技能 hermes skill remove <skill-name>
```

Top8 实用技能包

**1. web-scraper（网页采集）**

**用途**：给Hermes一个URL，自动抓取网页内容、提取正文、清洗格式，输出结构化数据。适合竞品监控、新闻聚合、价格追踪。

```
hermes skill install web-scraper
```

**安全提醒**：此技能需要网络访问权限，建议在白名单中限制只允许访问特定域名。

**2. doc-writer（文档撰写）**

**用途**：根据模板自动生成技术文档、周报、需求文档。支持Markdown、Word、PDF输出。你可以把公司文档模板配置进去，以后一句话生成标准格式文档。

```
hermes skill install doc-writer
```

**3. code-reviewer（代码审查）**

**用途**：对指定代码文件或仓库进行自动审查，输出安全风险、代码风格、性能问题等分类报告。

```
hermes skill install code-reviewer
```

**安全提醒**：审查过程需要读取源码，确保不要指向包含密钥的配置文件。

**4. data-analyst（数据分析）**

**用途**：上传CSV/Excel文件，自动生成统计分析、可视化图表和分析报告。适合快速探索数据集，不用手动写pandas代码。

```
hermes skill install data-analyst
```

**5. security-scanner（安全扫描）**

**用途**：对目标URL进行基础安全扫描，包括端口探测、HTTP头安全检查、常见漏洞指纹识别。适合安全人员快速初筛目标。

```
hermes skill install security-scanner
```

**安全提醒**：仅对授权目标使用，未经授权的扫描可能违法。

**6. social-poster（社媒发布）**

**用途**：一键生成适配微信公众号、微博、小红书等平台的图文内容，自动适配字数限制和格式要求。

```
hermes skill install social-poster
```

**7. lang-translator（专业翻译）**

**用途**：技术文档级别的中英互译，保留专业术语英文原名不硬翻译，确保学术严谨。适合翻译英文技术博客和论文。

```
hermes skill install lang-translator
```

**8. cron-manager（任务调度）**

**用途**：可视化管理和创建Cron定时任务，比手写cron表达式更直观。支持自然语言描述任务需求，自动生成cron表达式。

```
hermes skill install cron-manager
```

安装安全三原则

2. **来源可信**

   ：优先从官方市场安装，第三方GitHub仓库安装前先审查代码。SkillHarm研究（arXiv:2606.02540）显示26.1%的公开技能包存在安全漏洞。
4. **权限最小**

   ：安装后在 `~/.hermes/allowlist.yaml` 中只开放该技能必需的权限，不要一劳永逸全部放行。
6. **完整性校验**

   ：安装后记录技能包文件的SHA-256值，定期比对检测是否被静默篡改（尤其是防SMP自变异中毒）。

自助写技能包

如果你有反复执行的复杂任务，可以让Hermes自动生成技能包，也可以手写：

```
# ~/.hermes/skills/my-weekly-report.md ## 触发条件 用户说"生成周报"  ## 执行步骤 1. 搜索本周项目进展记录 2. 提取关键节点和指标变化 3. 按公司模板格式化 4. 输出Markdown文件  ## 边界条件 - 无项目记录时提示"本周无项目进展" - 指标缺失时标注"待补充"
```

写好后放到 `~/.hermes/skills/` 目录，Hermes会自动识别并在下次触发时调用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rvkyDDyx4sv53bdQHLc9aiaciaqqxoojmXlic5HzYKRWCHnibkX1MXkqzL652lJpPoacJ8owSC6fuxHgnIgcWDVMIg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过