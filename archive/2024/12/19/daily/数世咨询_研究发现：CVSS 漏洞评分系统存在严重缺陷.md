---
title: 研究发现：CVSS 漏洞评分系统存在严重缺陷
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247531866&idx=1&sn=6f39682cbc5c8f1e3e0d2d15020fcf16&chksm=c1440fe7f63386f17015807f15f31bd5c35bc96b1095d5c3cd51c6be49eef9751b71da5c80b7&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-12-19
fetch_date: 2025-10-06T19:39:21.510141
---

# 研究发现：CVSS 漏洞评分系统存在严重缺陷

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrp0ukacwbvLBdSxe8IsoZuj33sj5G2cnPrJnKbMgBFShrx6qHe4a2UnnhOznBblusXuGzVNXXJJg/0?wx_fmt=jpeg)

# 研究发现：CVSS 漏洞评分系统存在严重缺陷

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrp0ukacwbvLBdSxe8IsoZuicL3rnxickQvcJoADlQ3rGs6xL4TOwiazM8MLl1zy27tLylENff6YLNLg/640?wx_fmt=jpeg&from=appmsg)

**摩根大通（JPMorganChase）的网络安全专家认为，网络安全行业可能因对CVSS评分过于依赖而误解了漏洞的严重程度，从而影响了修复工作的进展。**

在本周四的黑帽欧洲大会上，代表们接到了一个通知：当前用于评估软件与硬件漏洞严重程度的全行业标准方法需要进行调整，因为这种方法可能会带来潜在误导性的评估结果。

通用漏洞评分系统（CVSS）通过综合多种指标来评估漏洞的严重程度。然而，摩根大通的网络安全专家在黑帽会议上的演讲中提出，该系统未能准确反映与漏洞相关的实际风险，这导致组织会依据不完整的数据决定修复工作的优先级。

举例来说，CVSS评分并未考虑具体的使用环境或攻击者是否已经实现了在野漏洞利用。摩根大通指出：“CVSS的影响指标对机密性、完整性和可用性给予同等重视，这忽视了组织的特殊风险等级以及漏洞可能带来的实际影响。”

在2023年，平均每日的漏洞披露数量达到了80起，这一数字相较去年呈现出了约20%的增长。其中，约有18%的漏洞被评定为严重级别，其CVSS 3.0评分为9分或超过9分。

**01**

**漏洞的严重性被低估**

摩根大通的分析显示，约有10%的安全漏洞可能未被充分重视。例如，Citrix
NetScaler中的DDoS攻击漏洞CVE-2020-8187在疫情期间披露时，评级仅为7.5分，但这一漏洞的严重程度“足以让组织陷入停顿”。

研究人员指出，在制定CVSS评分的过程中，对隐私问题的考虑不够充分。他们认为，采用通用的安全漏洞评分机制可能无法准确反映出每一起CVE事件中涉及的隐私风险。

例如摩根大通的专家提到，Zoom的一个信息泄露漏洞CVE-2019–13450被评为中等等级，即该漏洞允许在不进行用户交互的情况下激活网络摄像头，存在侵犯隐私、安全风险以及可能引发法律和声誉问题的潜在后果。

他们认为，对依赖关系的考虑不足是CVSS分数的另一个主要缺陷，影响了至少11%的CVE（已公开漏洞）优先级的确定。

成功利用安全漏洞往往需要特定的设置或依赖于其他软件的漏洞。配置和访问控制是关键因素，它们显著影响攻击者利用漏洞的能力。研究人员指出，尽管用户权限可能影响违规行为的严重性和潜在影响，但它们在CVSS分数计算中是没有得到充分体现的因素之一。

**02**

**CVSS 4.0 也有缺点**

即将推出的CVSS 4.0框架将引入更为丰富的影响指标、更精细的时间指标以及新增的辅助指标，以提高评估的准确性。然而，正如摩根大通的安全研究员所指出的，该框架在处理隐私问题及与高级持续威胁（APT）相关的关联方面仍存在不足。

摩根大通已经制定了一套框架，旨在解决APT和可利用性的权重问题以及依赖关系的问题。这家金融服务巨头已经设计了一个概念模型，并鼓励其他安全社区成员参与审查和进一步完善这一框架。

在接受CSO采访时，摩根大通的安全架构师Syed Islam表示，只有那些在安全成熟度方面达到一定水平的企业——比如拥有对业务运营至关重要的技术和应用程序的详细清单——才能从采用漏洞评估方法中获得显著收益。

\* 本文为陈发明编译，原文地址：https://www.csoonline.com/article/3623598/security-researchers-find-deep-flaws-in-cvss-vulnerability-scoring-system.html
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrp0ukacwbvLBdSxe8IsoZuECUQaibMtaEiaNZN79PwGSxg5DM3V2qcOsZKLZXr7Ff7ibicNDKuXyQGNQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247531062&idx=1&sn=ca1b73c32eb7b7655cd51fc61c3254e7&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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