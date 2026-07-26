---
title: OpenAI GPT Agent入侵 Hugging Face；Anthropic 推出 Claude 安全插件 | FreeBuf周报
url: https://mp.weixin.qq.com/s/H9gybinxEhxLyojbnaiWtQ
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:21:53.711157
---

# OpenAI GPT Agent入侵 Hugging Face；Anthropic 推出 Claude 安全插件 | FreeBuf周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymyA0AYWle3Wnao3wWyHqsDzMGH37D4XINGFb1Us09fC8ibRIH5cvgDSw/0?wx_fmt=jpeg)

# OpenAI GPT Agent入侵 Hugging Face；Anthropic 推出 Claude 安全插件 | FreeBuf周报

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、一周好文，保证大家不错过本周的每一个重点！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJ1UiaObonmWJbuLyoLXdutZ6T0GL6AXwFA0IHVJ9Tl93JicaeTmN55VJBw0JKrJg4sQXdypbdzqibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

🤖OpenAI GPT Agent 利用0Day漏洞入侵 Hugging Face 服务器

🧬Hugging Face 遭自主 AI Agent 入侵：生产基础设施被突破

🧠Claude Mythos 常见问题：能力、访问、竞争与影响

🛡️Anthropic 推出 Claude 安全插件，在终端内扫描代码漏洞

💥新公开的wp2shell漏洞可致攻击者接管WordPress站点

🚀Gemini 3.5 Flash Cyber：具备自动化快速漏洞发现与补丁能力

🔥ServiceNow 关键沙箱 RCE 漏洞 PoC 公开

⚠️15年历史的NGINX漏洞：攻击者可致Worker崩溃并实现远程代码执行

🕵️匿名研究员在供应商修复前公开204个0Day漏洞利用文件

💰GitHub 削减公开漏洞赏金，最高奖励转入 VIP 层级

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5NY7KgXpwrAo5WHiaX2SOibeoicce3vxyZozGALjYSLtYPrDiceL0UV2D3A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

### OpenAI GPT Agent 利用0Day漏洞入侵 Hugging Face 服务器

OpenAI测试中，AI Agent自主发现0Day漏洞并攻破Hugging Face生产环境，实现RCE。这标志AI驱动的自主网络攻击成为现实威胁，安全团队需立即应对。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX155zmnS7UhYr1fbWBNxzSD4uhKoqNvwq6ZOLAGLyFecQWksSlSCcYicCiaY2QQ0JSoprdSJmUBUgOCE4JG5QhFVMS3cVXrUUlWs/640?wx_fmt=jpeg)

### Hugging Face 遭自主 AI Agent 入侵：生产基础设施被突破

Hugging Face披露AI Agent自主攻击其基础设施，使用恶意数据集利用代码执行路径获取凭据，但未发现模型或数据集被篡改，建议用户轮换令牌。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX32ibtmcAzY1YLvLfibp5flCEa92EW4zFxWeiaSCE4m2ibibIqNWia2mreibCia3vqREovmQffCKGaD2VfbKsqSM1rReA2GYN15oPWf6bo/640?wx_fmt=png&from=appmsg)

### Claude Mythos 常见问题：能力、访问、竞争与影响

Anthropic的Claude Mythos AI模型已发现超万个高危漏洞，但能力可能被滥用。安全专家警告AI正加速攻击速度，企业需转向持续漏洞运营与优先修复。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0J5CmTmRVAt2ib8wUs3R9nRFBGaNAvzgJY506bOtUI9CFJZicKP22hQTkVqPONxKQzIBqhSMibwJLNW24Hymvgu6kxH1UpZILyTY/640?wx_fmt=png&from=appmsg)

### Anthropic 推出 Claude 安全插件，在终端内扫描代码漏洞

Anthropic 发布 Claude Security 插件测试版，集成到 Claude Code 终端，用多 Agent 系统在代码交付前扫描并修复高危漏洞，降低误报，人工审查后生效。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1aaLFcme6DEdLwUXAXCiaKEwkkq108KTDKsfDSdYokvIzUHqAhzn1WsEUtzUhXSJdewwFnXag2KlUtxFw9j9ZRodHNwyRbo7XE/640?wx_fmt=jpeg&from=appmsg)

###

### 新公开的wp2shell漏洞可致攻击者接管WordPress站点

WordPress 6.9.x/7.0.x存在两个高危漏洞（CVE-2026-63030与CVE-2026-60137），可链式利用实现未授权RCE。官方已发布7.0.2/6.9.5安全更新并启用强制自动更新，建议立即升级。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1of3ibRjzJxF559tibMsm88KNT2JtGvLricoibImoWibcF4azxwkr25ebElkJnY6J4Gqmxm78TyjK3oE6icEcHdVM00bicPbQ7ZhiavVk/640?wx_fmt=jpeg&from=appmsg)

###

### Gemini 3.5 Flash Cyber：具备自动化快速漏洞发现与补丁能力

Google发布Gemini 3.5 Flash Cyber，专为网络安全设计，高效发现、验证和修复漏洞，配合CodeMender Agent实现低成本大规模部署，已在内部成功应用。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ibksOic9jicAbaOEWaTk8r1q3Luntk7feiaGE8mCsu8cM5EfYdUXjp4oUqRNg06k0JG46obDkmob8BnE2B2SNia87XU2nEbPXNBQw/640?wx_fmt=png&from=appmsg)

###

### ServiceNow 关键沙箱 RCE 漏洞 PoC 公开

CVE-2026-6875导致ServiceNow AI平台沙箱逃逸，实现未经验证的远程代码执行。PoC已公开，漏洞可完全沦陷实例，包括数据访问、创建管理员及控制MID Server。建议立即升级修复版本。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0qZkEnev9Gn6FHEOl8QhVP35fxzyOiazcrH3ZgVYne0NibhfFTRN5gD0sIqUKcv38yC7UTib8neYQxCGIVXVJu7wOTQbt0dae4Ec/640?wx_fmt=jpeg&from=appmsg)

###

### 15年历史的NGINX漏洞：攻击者可致Worker崩溃并实现远程代码执行

CVE-2026-42533是15年历史的nginx漏洞，无需认证即可远程代码执行，源于脚本引擎未保存PCRE捕获状态，导致堆溢出和信息泄露，影响所有版本，需立即升级。

### ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX03aRscn8atNGrEBhY3G5KB7SicXicQia1W24Y9BicH9RhXiaDq5AWy7eiceLBuC50BIKCdml5SbpmibibvxyVRuykVpcMkSns7luA6nHs/640?wx_fmt=jpeg&from=appmsg)

###

### 匿名研究员在供应商修复前公开204个0Day漏洞利用文件

匿名研究员通过exploitarium仓库公开204个0Day PoC，颠覆协调披露流程，使数十个开源项目在未获补丁时暴露风险，形成持续增长的攻击工具包，影响核心基础设施与供应链。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3592yz7H0AMiaRcTGh9nkgP6Gd3rzwtxgVib0A9GTwiaJMnKAgia2xsd1jSvDCkqqU52pV78QJCSuqPT2gu3ehuN7Ae82kmsnF9LA/640?wx_fmt=png&from=appmsg)

###

### GitHub 削减公开漏洞赏金，最高奖励转入 VIP 层级

GitHub自2026年7月27日将公开漏洞赏金削减至少一半，严重级别降至1万美元，VIP层级保留3万+；转向固定金额，强调高质量而非数量，应对AI垃圾报告。

### ![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1IIj9R0KZcp5YGjFzHNCiafTN1KkUSqNOmZbry1wUiax7KWNEYSn3hPmmiadTNNib9OdRFRlbFOGOXG46taojmp8p8QzSdmxR61QA/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5Ce9OricKgAogLRlHYat9jaelbVESLOylPBnQQrU63TlHEs2zCbdNrKg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**本周好文推荐指数**

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

记一次API Gateway边界失效导致微服务集群失陷的渗透测试复盘

本文揭示微服务架构“Gateway统一认证，后端天然安全”假设的致命缺陷：通过路由泄露找到认证绕过路径，横向渗透获取核心数据，强调零信任的必要性。

![大模型分析信息时出现幻觉错误怎么办？解决方案汇总 - Raccoon-Raccoon](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX22ibhPicqneCwcduu6Sy05UQam8qdt18ZC9iao1ISscO7drFltH8Oz5FKGiaiakFeia7zR4iaNooLK1SicrtVMPV1DDtbPT9ibaRbbtojY/640?wx_fmt=jpeg&from=appmsg)

### 一封邮件干翻整个域：红队钓鱼从情报收集到武器化的全路径拆解

### 红队钓鱼成败八成取决于社工情报收集与场景设计，而非技术工具。通过伪装成内部通知、制造紧迫感，结合Evilginx2劫持MFA session cookie，一封邮件即可拿下域控。蓝队需快速响应异常发件人、URL和附件类型，速度决定攻防胜负。

### ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX33BXZd5JibvtiapoFRGcrPHicY0Hic7v0fOCTibW0hcBrtic8YycfWbCfYeYyLkRGkht0hWsg4ZicsA7eIpEwB7hMHfW8ibb8ePD8picxw/640?wx_fmt=png&from=appmsg)

###

### 源码审计的三个模式：从 nginx 到 Traefik

中间件源码审计存在三个重复模式：双路径分歧、修复链断裂、DSL攻击面扩展。SAS框架从这些视角可覆盖80%非内存类漏洞，且能反向指导设计规避风险。

![Infostealer malware found stealing OpenClaw secrets for first time](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0PfRLZgialHRAbweHJF5fXqibSjZAvuogdYAcvjfSfMw7eGMSBVTicMtBop51CR4kYrFTibEedczA6aWhv37kstHWHeoia3utsZCYg/640?wx_fmt=jpeg&from=appmsg)

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3vp7Nh5SN03lJzkelia9oMl3rDgBcDgQuSu66GUobMfu7PibWYZsgcVfAuZ1aAVwMiatGia3JO3kthfNotNqKQC8uiaS9Za2ky2BVI/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ptPNnRL9ln6TVtKnqhFaD6lZpyAbLwIM5Fj1m89oyZLopZfbJiaJygvkmWZnicUqiaMDPQFh7zAOptwmFmtCGTNSDFbCOaUfcYc/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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