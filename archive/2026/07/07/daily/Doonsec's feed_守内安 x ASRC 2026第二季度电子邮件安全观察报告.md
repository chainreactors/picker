---
title: 守内安 x ASRC 2026第二季度电子邮件安全观察报告
url: https://mp.weixin.qq.com/s/cEd1Cf9xWGVTli99OpuzzQ
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:02:36.262294
---

# 守内安 x ASRC 2026第二季度电子邮件安全观察报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpeURJnWApIWW4ju1m0UuTg4VWgUXHzveHPMqNgEbly6ibH0dy7cpMVR9H8dDeDyRWh1ibRcKWqmDjoxUAlSNwxkxQ2qnicvV2ibzZ4/0?wx_fmt=jpeg)

# 守内安 x ASRC 2026第二季度电子邮件安全观察报告

守内安
守内安

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

2026年第二季度，电子邮件安全环境面临典型的威胁平移。攻击者正加速从依赖传统的已知病毒特征，转向以规避防毒软件静态检测为核心的高级威胁形式（对应 MITRE ATT&CK: Defense Evasion）。数据显示，本季度带有恶意内容的邮件量较上一季暴增约8倍，并于今年5月达到峰值。

值得警惕的是，5 月，恰逢多数企业开展内部演练，备战HW时期。极易被黑客利用此时间点发动真实攻击，从而衍生出严重的管理与通报风险：

**1.防范预期落差**：部分员工在预知有演练的心理状态下，面对异常邮件失去应有的警惕，认为只是模拟演练，不会产生实际损失。

**2.警报疲劳与通报拥堵**：当演练邮件与真实攻击同时涌入，it运维（Helpdesk）与安全部门（SOC）的资源会迅速被海量反馈的钓鱼邮件信息占用，真真假假的信息可能直接影响到应急预案的响应，导致实际响应滞后。

**3.“计中计”效应**：当安全团队拦截到真实攻击并发布给全公司紧急通知（如：【请注意！目前有真实钓鱼攻击，主题为 XXX】）时，员工容易将该通知信误认为是演练环节而置之不理，导致“人防”在最关键的时刻失效。

本季我们拦截并分析了数个具有代表性的高级威胁样本，其共通点在于深度结合社交工程与合法云端服务滥用：

PART.01

**假恐吓真入侵：**

**从纯社交工程到搭载恶意内容的转变**

过去的恐吓邮件（Sextortion/Extortion）多半依赖暗网泄露的账密库，单纯以话术胁迫受害者付款，邮件中通常不含恶意附件或链接。然而本季出现新型变种：黑客在恐吓邮件中附带恶意软件，并以“敏感数据被盗的证据”为诱饵，诱骗受害者点击打开。此手法结合了过去常见于网页攻击的“技术支持诈骗（Tech Support Scam）”的逻辑：**利用恐惧情绪扰乱受害者的理性判断力，让真正的入侵发生在误信邮件内容之后**。一旦点开附件，设备将被立即植入后门，使攻击从单纯的言语诈骗升级为实质的网络攻击，进而取得计算机的远程控制权限。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpdujtsygSVgK29xzHmLU4HVVJj3qYeiaibRTQbS4KWadibeOAoac1lXf5ZTQK0y70DLiakI1lqKxeBtd8rkORic7tLNwvsiaicWLiaviae8/640?wx_fmt=png&from=appmsg)

(传统恐吓邮件)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpc4iaaTrWYZdeJKJhmDCOR4oXS2W09o3HZg1vStb5mlCv7IUqz1LYuBOpBDNhB0VdwEDyIXraQVEsI5F7F1G33gQbBnqXbzTgKo/640?wx_fmt=png&from=appmsg)

(含恶意附件的恐吓邮件，试图同时骗取财物及电脑控制权限)

PART.02

**假加薪/中奖通知：**

**仿真欺骗与 AWS 基础设施滥用**

在第二季度，我们检测到许多关于“天降横财”的钓鱼邮件。这些钓鱼邮件内藏的钓鱼链接多半都会滥用公共服务或是使用短链接来避免第一时间被检测拦截。

 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpe6AXfAiaX5FpicVyibViaGLRprPVs2aeFeSWuicGG9Rl5y9ghMlrbZmNO5ibdXHIvpFjnpyS9aObdxPMtOysicLBYEBF4EHKwKOgzjXU/640?wx_fmt=png&from=appmsg)

(假加薪通知)

从以上收到的涨薪邮件来看，攻击者滥用Amazon Web Services (AWS) 合法基础设施来发送伪造的钓鱼信息。钓鱼页面主要的JavaScript攻击程序代码，以高度混淆（Obfuscation）的方式破坏可读性，并将变量名称、API 网址与字符串替换成数组索引，企图规避防毒软件或安全人员的静态分析。我们发现程序代码中直接写死了Telegram Bot的密钥。当用户输入账号密码并点击发送后，程序代码会组合包含密码的字符串，并通过AJAX将数据传送到黑客指定的Telegram聊天室。这个攻击主要想窃取的是合法的微软登录凭证，而它不仅仅偷取密码，还会收集受害人的环境信息。代码中包含请求 getVisitorIP() 函式，利用第三方服务 https://ipinfo.io/json 来抓取用户的 IP 地址、所在城市、国家与电信运营商信息。同时也会收集浏览器版本与语言配置信息。

PART.03

**滥用 Cloudflare workers.dev：**

**绕过多因素认证（MFA）的设备代码钓鱼（Device Code Phishing）**

本季最精密的攻击手法之一，是滥用 Cloudflare Serverless 服务（workers.dev）的进阶钓鱼。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfNYiaBL2yYCficufYyxeBPwTy3alA0otIKIY0ahu8SvnetQc21eOxibjZEh9PJFI9dGzibBwtInvurwHGKBnHDapdfNhAzVwDNx8g/640?wx_fmt=png&from=appmsg) (滥用 Cloudflare Serverless 服务（workers.dev）的进阶钓鱼邮件)

手法分析如下：

**·规避网址扫描**：邮件刻意将链接改写为 https:\\，诱导收件人手动复制粘贴。此举不仅避开了安全设备对恶意超链接（<a> tag）的自动解析，一旦收件人按照黑客的指引粘贴至浏览器地址栏，浏览器页面会直接跳转至真实的钓鱼网站，而如Cloudflare 这样的合法域名更能轻易绕过安全网关（SWG）与浏览器内置的恶意网址检测。

**·沙箱规避与环境隔离**： 恶意网页通过独立作用域封装 JavaScript 代码，防止与原始页面变量产生冲突；同时代码刻意延迟 2 秒执行，一方面规避部分动态沙箱检测机制，另一方面等待页面文档对象模型（DOM）加载完毕。

**·剪贴板挟持与多因素（MFA）绕过**：当受害人点击诱饵按钮（data-href），恶意代码会强制篡改受害人剪贴板内容，随后跳转至真正的微软登录页面。若受害人按页面提示粘贴设备代码并完成多因素认证，凭借有效的身份凭证（Cookie / 单点登录凭证），攻击者远端设备可直接获取该账号的完整 OAuth 访问令牌，实现账号全权限接管。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpfgvAlx8SCPakr5aA0rLo0RmXjhhgewb42xg8AEkuOCkhVfneGketUic6RVCEWQibIERrTf4X7jf0DhIdaDhs6T4oOTE2hkxN5dw/640?wx_fmt=png&from=appmsg) （微软 MFA 钓鱼页面）

**·状态监控**： 该网页会在后台携带专属会话标识（SID，Session ID），持续向恶意命令控制服务器（域名：api.duemineral.uk）轮询攻击执行状态，返回状态包含捕获成功、会话失效、请求拒绝三类，整套攻击流程自动化程度极高。

PART.04

**结语与建议**

攻击者正广泛利用开源网络情报（OSINT），从 LinkedIn 等平台自动抓取目标的姓名、岗位与组织架构信息。这使得高针对性的鱼叉式钓鱼已具备自动化与规模化投放的能力，社交工程将比以往更难分辨，企业应限制不必要的人事信息公开；为了防止假冒企业内部邮件，在邮件网关（Gateway）端针对外来邮件的主题或邮件正文强制插入“内部”或“外部”标签，也是一种直观能有效降低误点率的做法。

企业针对邮件安全的防护措施，多半已采用SPF、DKIM 与 DMARC等识别邮件来源是否遭到假冒的防护机制，但这并不能高枕无忧，当供应链或外部合作伙伴的合法网域遭黑客攻陷（BEC 攻击）时，带有合法签章的钓鱼邮件仍会畅通无阻。导入基于行为分析（UEBA）或升级智能体来进一步强化防护能力。

最后，建议采用正向鼓励的方式，建立非惩罚性政策，鼓励员工在察觉可疑上下文（Context）时，主动反馈给相关安全部门或管理员，以达到“人防+技防”的安全目的。

******END****

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247651222&idx=1&sn=0674c7e57249a57240b5ed0fcd6cdcf2&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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