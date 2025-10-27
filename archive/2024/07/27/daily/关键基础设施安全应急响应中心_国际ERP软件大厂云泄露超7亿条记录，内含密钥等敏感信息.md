---
title: 国际ERP软件大厂云泄露超7亿条记录，内含密钥等敏感信息
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545108&idx=2&sn=a85dbf959b9d167b0b87de214fa4f931&chksm=c1e9bd45f69e34535f268e208cf74f445fe0914d312061eecfdde61993c32a8326d29f1b08b1&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-27
fetch_date: 2025-10-06T17:43:14.338531
---

# 国际ERP软件大厂云泄露超7亿条记录，内含密钥等敏感信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvuJZ8bcC0yXiaIK8bGDnCO7k3XCEz9DXBm5mPBpeYPYhER147AyiasM6gic6eeTibia0a9cEKERfVjZRA/0?wx_fmt=jpeg)

# 国际ERP软件大厂云泄露超7亿条记录，内含密钥等敏感信息

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvuJZ8bcC0yXiaIK8bGDnCO7mubyAOgTEYIWibQrAchzDpQbtuUJ7u0o7RJPO7Kb9u6tHic7WJMSgS1g/640?wx_fmt=jpeg&from=appmsg)

ClickBalance一个云数据库暴露在公网，导致7.69亿条记录泄露，其中包括API密钥和电子邮件地址等信息。

7月25日消息，根据安全研究员Jeremiah Fowler的最新发现，ERP软件提供商ClickBalance拥有的一个包含7.69亿条记录的云数据库未设置任何密码或安全认证，恶意威胁行为者可以轻而易举地访问这些数据。

ClickBalance是墨西哥最大的企业资源规划（ERP）技术提供商之一，提供可以从任何设备访问的ERP工具。ERP工具负责管理和自动化各部门的业务流程，涵盖财务、人力资源、供应链、制造和销售等部门。

Fowler向WebsitePlanet报告了这一问题。该报告指出，该数据库包含了潜在的敏感信息，如访问令牌、API密钥、密钥、银行账号、税号和381224个电子邮件地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voquSCVLY9QCAiacW04cp3eMJqzKrhHGPnt3Iibs2fZZRz5DiaxyxzHibAMqicZ1hR3kEGFK2frQ0icDcg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voquSCVLY9QCAiacW04cp3eumpAcAobTtCwqKXQR1aX1pfTrUsDNrL086YdNUmUpTNaWogs7sKnXw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7voquSCVLY9QCAiacW04cp3eNGa2eSdUUOMUD7iaGHUicrTL1JMs7PQCibwKNygaX5ia3ZqTzMkG9oAAEg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图：泄露记录的截图（来源：Jeremiah Fowler）

API和密钥的暴露非常令人担忧，因为网络犯罪分子可能利用这些数据未经授权地访问关键系统和敏感数据，进而引发数据盗窃、账号接管、未经授权的交易和服务中断。

电子邮件地址的暴露也带来了潜在的风险。相关风险不仅限于垃圾邮件，因为91%的网络攻击始于钓鱼邮件。犯罪分子可以创建欺骗性电子邮件以窃取个人信息、财务数据和登录凭证。网络犯罪分子获取业务相关的电子邮件地址之后，可能发动有针对性的钓鱼攻击。

目前尚不清楚数据库暴露了多长时间，也不清楚是否有其他人访问过。不过，Fowler指出，对于管理着大量客户、员工和终端用户数据的科技公司来说，数据保护是一大难题。为此，他们设计了企业资源规划（ERP）、客户关系管理（CRM）和持续诊断与缓解（CDM）系统，方便跟踪和管理这些数据。然而，数据泄露可能暴露敏感信息，带来长期的运营和战略风险。

好消息是，Fowler发送了负责任的披露通知，几小时后该数据库限制了公共访问。尽管如此，为了防范这些风险，组织应更改密码并启用双因素认证（2FA）。

同样重要的是，要警惕未经请求的电子邮件和可疑的信息请求。通过访问控制和安全存储实践保护密钥、令牌和其他管理凭证也至关重要。

**参考资料：**

hackread.com

原文来源：安全内参

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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