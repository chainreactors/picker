---
title: 每日安全动态推送(26/2/27)
url: https://mp.weixin.qq.com/s/DfjI6Rk320hKVMl4FHQtgw
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:57:19.138952
---

# 每日安全动态推送(26/2/27)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/2/27)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器中沉浸阅读

•  OpenClaw AI代理遭信息窃取与漏洞攻击
<https://sectoday.tencent.com/event/2RVKRJwBVJfJhgnJttC1>

多个黑客组织针对开源AI助手OpenClaw发起攻击，利用其配置文件和漏洞窃取用户敏感数据。攻击者通过信息窃取恶意软件获取OpenClaw的配置文件，包括API密钥、认证令牌、私钥、设备信息及用户记忆文件，从而重建用户的数字身份。同时，攻击者还利用OpenClaw中的多个漏洞，如日志投毒（CVE-2026-25253）和供应链污染，入侵超过30,000个实例并部署恶意软件。此事件标志着网络犯罪行为从传统凭证窃取转向针对AI系统的数字身份攻击，并凸显了AI工具集成到日常工作中带来的新安全风险。

•  SuperClaw：面向自主AI编码代理的安全红队开源框架
<https://cybersecuritynews.com/superclaw-red-team-ai-agent/>

《SuperClaw：面向自主AI编码代理的开源预部署安全测试框架》一文首次系统性地提出了针对自主AI代理行为安全的测试方法，突破传统静态扫描工具的局限，为AI安全验证提供了全新范式。

•  AI辅助黑客入侵600台FortiGate防火墙
<https://sectoday.tencent.com/event/JPVMi5wB5M25NX6PAWFy>

一名以牟利为目的的威胁行为者利用生成式AI工具，在五周内入侵了55个国家的600多台FortiGate防火墙。攻击主要利用暴露的管理端口和弱单因素认证凭证，而非FortiGate本身的漏洞。尽管该黑客技术水平有限，但通过AI工具进行了攻击规划、命令生成和工具开发。活动涉及Active Directory入侵、凭证收集和备份基础设施攻击，表明生成式AI正在显著降低网络犯罪的门槛，使得技术门槛较低的攻击者也能发动大规模攻击。该事件凸显了强化密码策略、启用多因素认证和加强网络分段的重要性。

•  Nginx整数溢出漏洞分析：深入探究Range头处理缺陷
<https://hackmag.com/security/nginx-int-overflow>

本文详细分析了 Nginx 1.13.1 中因 Range 请求处理不当引发的潜在漏洞，通过实际调试演示了漏洞触发机制，并提供了完整的复现环境与命令，是学习 Web 服务器安全分析与漏洞挖掘的优秀参考资料。

•  Cline CLI 供应链攻击事件
<https://sectoday.tencent.com/event/O9BchpwBnYhVxRrje_DE>

2026年2月，攻击者通过劫持 Cline CLI 的 npm 发布令牌，成功推送了恶意版本 2.3.0。该恶意版本包含一个 postinstall 脚本，静默安装了 openclaw@latest 包。攻击者利用了 Cline 的 AI 驱动 GitHub Actions 工作流中的提示注入漏洞，结合缓存污染和凭证配置不当，获得了代码执行权限。此次攻击影响了 Cline 的 500 万用户，突显了在 CI/CD 流水线中使用 AI 代理的安全风险。Cline 团队迅速响应，弃用了恶意版本并吊销了令牌，同时迁移到 OIDC provenance 以提升供应链安全性。

•  AI渗透测试发现Vercel托管的SvelteKit应用中‘SvelteSpill’漏洞
<https://securitybrief.asia/story/ai-uncovers-sveltespill-flaw-in-vercel-sveltekit-apps>

本文揭示了由AI自主发现的SvelteKit应用在Vercel平台上的高危漏洞SvelteSpill，突显了AI在安全研究中的潜力与实际价值。

•  Windows 记事本漏洞PoC发布，可实现恶意命令执行
<https://cybersecuritynews.com/poc-windows-notepad-vulnerability/>

本文详细分析了Windows现代记事本中的远程代码执行漏洞（CVE-2026-20841），揭示了攻击者如何通过诱导用户打开特定Markdown文件并点击恶意链接来实现命令注入。该漏洞修复及时，但其利用方式简单，对用户交互依赖性强，具有高度现实威胁。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HhcytTU2b7fDFB286mPqPOHlrgjH6Chv6CdQyTw7FOdHezZ2PQGKia9B4f7REZkzibNUwV0IyvRjgbgPzPULnFYvvvcgYqHMsgbic0OwACUqMg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

腾讯玄武实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

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