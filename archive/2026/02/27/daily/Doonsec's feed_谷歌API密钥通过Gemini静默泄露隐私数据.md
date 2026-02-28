---
title: 谷歌API密钥通过Gemini静默泄露隐私数据
url: https://mp.weixin.qq.com/s/X-8KhMKbkNoyKTSiydOhwQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:28.909190
---

# 谷歌API密钥通过Gemini静默泄露隐私数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX15hY1Cu9MOqw7KibJcqibr0ibR4vB3SrFA1OImTnSoqibsuguyXCMFiaIqCnDBibGSSmVMZXiaAwuMjwBicNVSDNRYgC5Xv7EJPQvKp0k/0?wx_fmt=jpeg)

# 谷歌API密钥通过Gemini静默泄露隐私数据

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1y2KDfNiatGZ9Xr11SSxasL8cE1fQlhQdnex6FjAIlMLL44WgeTX5wQfs4ibiaEQJj4P4Lc23gKVRazgZB8m2oWa0sedCOVwEziac/640?wx_fmt=jpeg&from=appmsg)

##

谷歌云API密钥存在严重的权限提升漏洞——传统对外公开的密钥会静默授予攻击者对Gemini AI端点的未授权访问权限，导致私有文件、缓存数据和计费AI服务面临泄露风险。

十余年来，谷歌一直明确要求开发者将格式为AIza...的API密钥直接嵌入客户端HTML和JavaScript代码。Firebase官方安全清单曾声明"API密钥并非机密"，谷歌地图文档也指导开发者将密钥公开粘贴至网页。这些密钥最初仅设计为项目计费标识符，而非认证凭证。如今这些指导方针已严重过时。

当谷歌云项目中启用Gemini API（生成式语言API）时，该项目所有现有API密钥都会静默获得敏感Gemini端点的访问权限——既无警告弹窗，也无确认对话框，更不会向开发者发送邮件通知。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1liaX922s5CHjG5aib1vNENj6JdicI1FLlcazE2M3ls9wDgNCfTLiaRaKyttv2Il2eTGUmuIiazBBRLEDqiahElib69kBMSLx6f0j7QQ/640?wx_fmt=jpeg&from=appmsg)

三年前部署的地图嵌入密钥，可能在一夜之间变成能访问AI上传文件、缓存上下文和计费推理服务的有效凭证。

##

**Part01**

## ****漏洞成因分析****

Truffle Security研究人员发现，该问题本质是权限提升漏洞而非简单配置错误。关键因素在于事件顺序：开发者遵循谷歌指南将地图API密钥置于公开JavaScript代码后，其他团队成员又在同一云项目激活了Gemini API。公开密钥立即获得敏感Gemini端点访问权，而原始开发者从未收到通知。

该漏洞根源符合两项已知缺陷：CWE-1188（不安全的默认初始化）和CWE-269（错误的权限分配）。谷歌云中新API密钥默认设为"无限制"，意味着从创建伊始就能访问项目中所有已启用API（包括Gemini）。

**Part02**

## ****攻击者能做什么****

攻击者无需任何基础设施即可实施攻击：访问公开网站→从页面源码提取AIza...密钥→直接查询Gemini API：

> curl "https://generativelanguage.googleapis.com/v1beta/files?key=$API\_KEY"

成功响应，从而获取以下权限：

* 私有文件与缓存数据：通过/files/和/cachedContents/端点暴露上传数据集、文档及存储的AI上下文
* 财务损失：攻击者可耗尽Gemini API配额或产生每日数千美元的受害者账单
* 服务中断：配额耗尽可能导致合法Gemini服务完全瘫痪

Truffle Security扫描2025年11月Common Crawl数据集（约700TiB公开网络内容存档），发现2,863个活跃谷歌API密钥存在此风险。受影响机构包括大型金融机构、安全公司、全球招聘企业及谷歌自身。研究人员确认，至少有一个自2023年2月就嵌入谷歌产品网站的密钥（早于Gemini问世时间）已静默获得Gemini模型端点的完全访问权。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1Zyg5klgxFCOO76uVhpuVrZQiaLsgFLg3Of9UY9y0mw5WtSQmAPF5EDNaJoHicNhgIibA4P63lLJIYg0ByXu3DQ5wYb0uMeohgyo/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## ****修复措施与现状****

谷歌已公布修复路线图，包括：为AI Studio密钥设置限定默认值（默认仅Gemini访问）、自动拦截野外发现的泄露密钥、向开发者主动发送密钥暴露通知。但研究人员指出，截至披露日根本性修复仍在进行中，尚未确认是否完成架构级解决方案。

**Part04**

## ****开发者应急指南****

使用谷歌云服务（如地图、Firebase、YouTube数据API等）的组织应立即采取行动：

* 审计所有GCP项目：进入"API和服务">"已启用API"，检查每个项目的"生成式语言API"
* 检查API密钥配置：标记所有无限制密钥或明确允许生成式语言API的密钥
* 确认无密钥公开：检查客户端JavaScript、公开代码库和CI/CD流水线中的AIza...字符串
* 立即轮换暴露密钥：优先处理遵循旧版"密钥可安全共享"指南部署的陈旧密钥
* 使用TruffleHog扫描：执行trufflehog filesystem /path/to/your/code --only-verified检测代码库中可访问Gemini的有效密钥

这种公开标识符静默获取敏感AI权限的模式，很可能不仅存在于谷歌。随着AI能力被快速集成到现有平台，传统凭证的攻击面将持续以始料未及的方式扩大。

**参考来源：**

Google API Keys Expose Private Data Silently Through Gemini

https://cybersecuritynews.com/google-api-keys-gemini/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3tSDVhn4H8MfzIKxtt4We0D52fia93Y5a2TI7y0t4j0PpiclCRBqdQCZWYrwG4B4hpaT2593sVoic8GylJKxPrgP1gyC1304Y78I/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX16d9YFd8C2ZLm5AxSaONt9eF8xcnfW9nhy3jyhoyrY28GWAnNeXJ0ojss2bj9w5V2asdI31nwVv2SUldtdhLfWuCE2l8fCzT8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

向上滑动看下一个

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