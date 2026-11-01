---
title: 【安全圈】Gitee 725 万个公开仓库被扫出 26400 个有效凭证，9473 个是阿里云密钥
url: https://mp.weixin.qq.com/s/xeV7DbBK_tmpPc9umDqN9Q
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:19:29.995726
---

# 【安全圈】Gitee 725 万个公开仓库被扫出 26400 个有效凭证，9473 个是阿里云密钥

# 【安全圈】Gitee 725 万个公开仓库被扫出 26400 个有效凭证，9473 个是阿里云密钥

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyH6pkZwVianrsUV0gMymQYMBbicwcsX4zhNPBEEfaM7cbgzab537C1uatpZCpVyCSGmoIJkCyKAe3Jz78IarMHqNMY0HrymEjz2U/640?wx_fmt=other&from=appmsg)

2026 年 10 月 28 日，独立安全研究员 Ben Zimmermann 联合 MongoDB 旗下 Kingfisher 团队，发布了一份针对 Gitee（码云）的大规模凭证泄露审计报告。研究共扫描该平台 7,256,531 个公开仓库，经去重并逐一调用厂商 API 验证后，确认存在 26,400 个唯一且当前仍然有效的私有凭证。

与以往同类研究不同的是，这 26,400 个密钥并非"疑似泄露"，而是经实际认证测试确认此刻仍可调用的活密钥。

## 泄露分布

从厂商维度看，阿里云 AccessKey 对数量最多，达 9,473 组。研究者测算，约每 766 个 Gitee 仓库中，就有 1 个包含经确认仍有效的阿里云凭证。

其余依次为：YouTube API Key 3,805 个，DeepSeek API 密钥 3,170 个，智谱 AI（BigModel）1,489 个，OpenAI 1,348 个。此外还包括 GitHub Token 600 个、Infura 499 个、JWT 391 个、Mapbox 346 个、AWS 338 个、Google Cloud 283 个、Google Gemini 260 个、Weights & Biases 222 个、MongoDB 220 个、HuggingFace 155 个。长尾部分还涉及 LangSmith、OpenWeather、Algolia、PostHog、OpenRouter、MySQL、Stripe、Slack、Twitter 等服务的凭证。

报告中特别提到，研究者还发现了某大型企业级 AI 平台的组织管理员凭证仍处于有效状态。此类高权限密钥一旦被滥用，影响范围远超单个 API 调用配额。

## 泄露成因

报告指出，绝大多数泄露源于开发者的操作失误，而非有意公开。常见情形是在快速开发中将 API Token 硬编码进 `.env`、`config.py` 等配置文件并直接提交。

由于 Git 会永久保留历史提交记录，即使开发者事后从当前文件中删除了密钥，历史版本中仍可被完整检索到。本次扫描覆盖了完整的 commit history，因此已被"删除"的密钥同样被计入统计。

从时间维度看，仅 2025 年一年提交的凭证就达 12,242 个，接近整个数据集的一半。这说明泄露是持续新增的，而非历史遗留。

## 扫描工具的覆盖率问题

本次研究同时使用 TruffleHog 和 Kingfisher 两款扫描器。结果显示，TruffleHog 检出 12,737 个，Kingfisher 检出 14,664 个，而两者同时检出的仅有 1,001 个。

两款工具的检测能力高度互补：TruffleHog 在阿里云密钥检测上占优（9,428 对 993），而 Kingfisher 在 DeepSeek（2,940 对 230）、OpenAI（1,198 对 150）、HuggingFace（154 对 1）上占绝对优势。其中智谱 AI 的 1,489 个凭证，TruffleHog 因缺乏对应检测器而完全未能检出。

这意味着，单一扫描工具只能覆盖约一半的风险。企业即便已在 CI 环节部署密钥扫描，也需单独验证工具是否覆盖其实际使用的云服务商与 AI 平台。

## 横向对比

按每千个仓库中的有效凭证数计算，Bitbucket 为 2.39，GitLab 为 3.11，Gitee 为 3.64，Gitee 在原始数量和单位密度上均高于前两者。

报告同时给出方法论提醒：此前针对 GitLab 和 Bitbucket 的扫描仅使用 TruffleHog，而本次使用了双扫描器。若只保留 TruffleHog 的结果，Gitee 的密度为 1.76。因此在进行横向比较时需谨慎。

按提交者邮箱域名统计，多数凭证来自 qq.com、163.com、gmail.com 等个人邮箱，因此难以按企业进行完整归因。可识别的企业域名包括 google.com（66 个）、huawei.com（32 个）、microsoft.com（22 个）、bytedance.com（22 个）、alibaba-inc.com（20 个）、jd.com（18 个）、tencent.com（13 个），另有 Oracle、Apple、Meta、Anthropic 等较小规模的出现。报告说明，企业域名的统计结果仅为下限。

## 研究方法

Gitee 于 2013 年由 OSChina 推出，曾被工信部选定为国家开源代码托管平台。其公开 API 限制较为严格，既无分页的项目列表接口，站内代码搜索功能也疑似多年前已下线。2021 年曾有研究者因 API 限制放弃同类研究。

本次研究通过组合多个渠道完成仓库枚举：使用官方 REST 搜索接口以三字符前缀（aaa 至 zzz）穷举，结合平台 Explore 动态页、用户 projects 与 starred 页面，以及支撑站内搜索的内部 Elasticsearch 端点。该搜索端点对单条查询截断至 200 条结果，研究者按语言与许可证分桶递归拆分绕过限制。最终获得 1,704,759 个用户名种子，去重后得到 7,256,531 个公开仓库。

扫描运行在 Modal 无服务器平台上，使用约 350 个并发容器，语料拆分为 50 批、每批约 15 万仓库，通过 SSH bare clone 后由两款扫描器同时处理。总耗时约一个月，总成本 3,097.64 美元，由 Modal 提供的 5,000 美元算力额度赞助覆盖。研究者指出，该架构只需更换 clone URL 即可复用于绝大多数 Git 托管平台。

## 处置进展

研究团队已向暴露量最高的厂商发送协调报告，提供完整的有效凭证清单及来源仓库元数据，以便厂商定位受影响客户。但由于泄露规模过大，研究者未逐一通知个人开发者。截至报告发布时，尚未确认这些凭证已被吊销。

报告同时指出两个结构性问题：一是 Gitee 缺乏类似 GitHub 与厂商联动的平台级密钥扫描合作机制；二是多数国内厂商缺少公开的漏洞或密钥上报通道，导致安全研究员难以有效协助止损。研究者认为，相比依赖泄露者自行处理，厂商侧主动吊销是更可靠的修复路径。

## 建议措施

研究者建议开发者立即审查自己的公开 Gitee 仓库，轮换已暴露的令牌，清理历史提交日志，并在部署前引入自动化机密扫描。

需要强调的是，从代码中删除密钥或重写仓库历史并不会使该密钥失效。凡曾进入公开仓库的凭证，都应视为已泄露，必须在服务商侧进行轮换或禁用。

具体操作上：阿里云用户应新建 AccessKey 对、更新应用、停用旧密钥并审查操作日志；Google 与 YouTube API 用户应轮换受影响的 API 密钥并添加使用限制；OpenAI 用户应立即轮换密钥并配置消费上限。

***END***

阅读推荐

[【安全圈】官方插件遭投毒！Claude Code被植入SSH后门](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079634&idx=1&sn=5f118197d2668a55db0755ec56254013&scene=21#wechat_redirect)

[【安全圈】9.8分Linux内核0day曝光：AI写PoC隔空夺取root](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079634&idx=2&sn=601725818b316bd0cb060b687e599f0c&scene=21#wechat_redirect)

[【安全圈】伪装GPT-6与Claude！黑客滥用官方数字签名投毒挖矿](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079634&idx=3&sn=08008f9ffacfbca4089cfc8a82436c43&scene=21#wechat_redirect)

[【安全圈】58 亿美元出逃：币安热钱包栽在 EIP-7702](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079622&idx=1&sn=71b12ef7d179251d4e8a097e84c0c341&scene=21#wechat_redirect)

[【安全圈】群晖NAS被全盘加密，补丁停在九月](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079617&idx=1&sn=d85132aae96dbf8cdc1e7966d416c4e8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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