---
title: 被当作透明管道的中转站：一次6TB泄露，暴露19家企业内网凭证
url: https://mp.weixin.qq.com/s/7FdA96qBTZGy3KlhU2eqwQ
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T07:01:11.465882
---

# 被当作透明管道的中转站：一次6TB泄露，暴露19家企业内网凭证

# 被当作透明管道的中转站：一次6TB泄露，暴露19家企业内网凭证

原创

Blake Chen
Blake Chen

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6P60eTB5mKfCxya6vEInFlZSzg0zIk2MOIF1H4AwXrtU0u5L9NVw354jicH8NxcpbPhQJDGXQ5zTqzdQZNh1RyHjYzVHbibxEjp4/640?from=appmsg)
> **导语**：2026 年 9 月，一名安全研究员称从国内头部大模型中转服务商处购得约 6TB 数据集，其中包含可直接使用的 SSH 私钥、VPN 配置、云服务凭证与 GitLab 令牌，点名小米、蔚来、深信服等企业内网。从蓝队视角看，真正的核心不是数据量，而是"合法凭证 + 正常登录"这一最难被检测的攻击形态。

![大模型中转站数据泄露概念图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NnPTWVzGvVosUicygu0lACdCHssrcLzCpleX7ic2Zd58KYXODoWnqgPBjCSPeEVpa3rHTYyDwH2utiapm2T4CSb1JJcr8Q6p7ialc/640?from=appmsg "大模型中转站数据泄露概念图")

## 一、事件概述

据报道，安全研究者 Chaofan Shou（寿超凡）公开表示，他从一家中国头部大模型中转服务商处购买了一份约 6TB 的模型数据集。他声称，数据集中的 SSH 私钥、VPN 配置、云服务凭证和 GitLab 令牌，足以访问 19 家中国科技公司的内部系统，并点名小米、华为、蔚来等企业。

在其公开的截图表格中，可以辨认出 Sangfor（深信服）的 `git.sangfor.com`、NIO（蔚来）的 `gitlab.nioint.com`、Bilibili（哔哩哔哩）的 `git.bilibili.co`、Xiaomi（小米）的 `git.n.xiaomi.com`，以及 USTC（中国科学技术大学）与 Zhejiang Lab（之江实验室）的内网 Git 地址。表格结构为"企业名称 + 内网主机 + 可用令牌"三项齐全，对应的 `glpat-` 开头的 GitLab 个人访问令牌已在截图中打码。

值得注意的是，这并非需要人工分析的原始日志，而是一份已经整理为入口清单的数据——使用它不需要任何渗透技能。

## 二、中转站为什么能看到明文

"全程 HTTPS，中间人看不到内容"是普遍认知，但在中转站场景下并不成立。研究团队此前发表的论文（arXiv:2604.08407）指出，这并非传统中间人攻击：不需要降级 TLS，也不需要伪造证书，因为使用者主动将中转站地址配置成了 API 端点。

实际数据流是：客户端的 TLS 连接终止在中转站，中转站解密读取完整的 JSON 请求体，再另建一条 TLS 连接转发给上游模型商。加密没有被破解，而是在中转站处被合法终止了一次，这被称为"对每一个流经 JSON 载荷的完整明文访问权"。一次 Agent 会话中流经中转站的内容，包括系统提示词（常含内部服务地址与数据库连接串）、工具调用参数（令牌就在其中）、工具执行结果（整段回传的配置文件与密钥）、环境变量以及上传的文件内容。

![中转站 TLS 终止导致明文暴露](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Nlapx8HdeBwlfWW3dul5RC75YSeWlIPBgoAYDNVYUuW9ST4EtcNBK5Gn6Hg8UxK1nYAib2zcEPUmrKiaeE8FjALsRT7KHoXQMAg/640?from=appmsg "中转站 TLS 终止导致明文暴露")

更易被忽略的是"中转站串联"：开发者从淘宝卖家购买额度，其 key 往往来自二级聚合商，再经 OpenRouter（开放路由平台）转发，最后才到模型商。四跳链路，每一跳都终止一次 TLS、都有完整明文权限，而配置文件中只有一个 base\_url。链路上任意一跳恶意，整条链的完整性即失效。

## 三、论文实测：428 台中转站的信任危机

研究团队付费购买 28 个中转站、收集 400 个公开中转站，共计 428 个样本实测：9 个注入恶意代码，17 个触碰研究者的 AWS 蜜罐凭证，1 个转走以太坊私钥资产；而测试的 4 个主流 Agent 框架（OpenClaw、OpenCode、Codex、Claude Code）中，没有一个校验中转站返回内容。弱口令实验中，4 万余次未授权访问使约 20 亿 tokens 流经这些节点，暴露 99 个唯一凭证、涉及 440 个会话；其中 440/440 可被命令注入，401/440 运行在自动批准（YOLO）模式下——一次载荷改写即可无需人工确认直接执行。

## 四、攻击分类与检测难点

论文将中转站恶意行为归纳为四类：载荷改写（AC-1），在响应到达客户端前替换工具调用命令，改写后的 JSON 结构合法、schema 匹配，客户端无从比对；被动窃取（AC-2），不修改内容，只扫描并外传凭证——本次 6TB 事件即属此类；另有依赖替换（AC-1.a，如把 `requests` 换成抢注的 `reqeusts`）与条件投递（AC-1.b）。

这四类都不是提示词注入，而是发生在模型推理循环之外的线格式层，提示词加固对其无效。对蓝队而言，AC-2 的检测难点最致命：流量没有任何变化，客户端原理上无法观测，响应签名也无法覆盖，因为凭证在请求路径上就已暴露。

## 五、蓝队处置建议

核心原则是：凡经过第三方中转站的凭证，一律按已泄露处理。中转站有能力记录全部明文，而客户端无法验证它是否记录，这是一个无法自证的位置，只能按最坏情况处置。

首先是排查。中转站接入门槛极低，改一个 base\_url 即可，因此实际使用范围往往超出预期。应重点排查开发机与 CI 上的 `ANTHROPIC_BASE_URL`、`OPENAI_BASE_URL` 等环境变量，Agent 客户端配置文件，以及指向非官方域名的出口 API 流量。研发个人开发机与运行 Agent 的 CI 流水线是重中之重，后者凭证权限通常更大且成套。

其次是轮换凭证，按后果排序：云厂商凭证（阿里云 AK/SK、AWS、GCP）优先级最高，其次是代码仓库令牌（本次暴露的正是这一类）、SSH 私钥、VPN 配置、数据库连接串，以及易被忽略的机器人令牌。轮换时应借机收缩权限，按最小权限重新签发。

![凭证轮换与访问控制防御](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NdH783WhvZP1238dcnPHSEpgeDkGH4xKW0JAkLuSzL3CaSRLUPrAdz9kXiafWgMqicuJ1cjyQLYfUWSmGcH9MlED0gzP4cJ5rT0/640?from=appmsg "凭证轮换与访问控制防御")

第三是检查日志，重点看内网 GitLab 的认证与克隆记录、云控制台 API 调用来源、VPN 接入记录。需清醒认识到：这类访问表现为一次正常的成功认证，没有爆破痕迹——日志中没有异常，不能作为未被访问的证据。

最后是结构性措施：将模型 API 出口白名单化，从技术上禁止随意修改 base\_url；改变 Agent 的凭证获取方式，改用短期令牌、按需下发、用完即弃——这是唯一对被动窃取有实际作用的措施；重新评估 YOLO 自动批准模式，生产环境不应启用；用容器或沙箱隔离 Agent 执行环境，只挂载必要目录。

## 六、总结

根据 MITRE ATT&CK 框架，本次事件本质上属于"有效账户"（T1078）与"供应链妥协"（T1195）的组合——攻击者持有的是合法凭证，与企业侧 WAF、EDR 看到的正常登录在日志中毫无区别。防御纵深的关键，在于承认中转站是一个被当作透明管道、实际却拥有全量明文权限的信任边界。假设已被入侵，重点在检测与响应：缩短凭证有效期、收敛权限面、保留本地透明日志，才能在下次事件中回答"哪些凭证经过哪些中转站"。

---

**参考资料**：

* 被爆国内某大型中转站服务商泄漏企业6TB数据 - CN-SEC 中文网
* 大模型中转站供应链安全危机：6TB数据泄露与428个LLM Proxy实测 - zgeo.com.cn
* LLM Router 实测论文 arXiv:2604.08407

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Mjv1DYklvjgiaOjnsicDYm1JF5AFiafVyjC133b9zpdsTMSshcHiaSgtqArHvJ1uuv2aiaMzuiaS7afglS2KeVmVvqkYaRZEv9DlOBQ/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Ncuehj7lIZLKwI0U6H4hJC6WBHNevAY6Hh9ayjL00mhtp50iahLZlP8zzwdficV1EtCkwXVObveYOZeOyBZIeia79oSmzBEoaJ5g/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NKNrrm89g6vzvcdN9iaWwV5eCBdOgSp98T0s9ibkUyxbiaWZBVprfgV9ktj09oG8iaqEnNjibyQtGPOmiaDgfe2JHGM5Wg6WO35mGfQ/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OahupfDbcNV4rEDedSo9Pc8ygrBwR8udDiaTFZaYDF2qX6BTGmwRakcLIFAWXNx2P7C0zP2Ek7gzvQT0XzWcF20es9pskzWNic4/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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