---
title: 安全漏洞曝光：AMD 和 Intel面临新型攻击威胁
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247519596&idx=1&sn=88483bcb603bb9106ca73d388a24ae3c&chksm=c144ffd1f63376c7f65520acac781b6e83d1c8748666964ba534ab28f1441519a06bc648f410&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-10-18
fetch_date: 2025-10-06T18:52:55.930797
---

# 安全漏洞曝光：AMD 和 Intel面临新型攻击威胁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrkmUSQ9zhw1T8DXiaYBN9Bm29YiamEEpIvrPhkO3jdolRQYI1XYDSZrqthb0ZfJsqSw3MgRjo49ZDA/0?wx_fmt=jpeg)

# 安全漏洞曝光：AMD 和 Intel面临新型攻击威胁

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrkmUSQ9zhw1T8DXiaYBN9Bmhun3iaWN7Ot2VibiapR2NSXmCe7NXPpVE1WvSIhghhVG9K9KAcoibxVDGw/640?wx_fmt=jpeg&from=appmsg)

安全研究人员继续寻找攻击英特尔和 AMD 处理器的方法，这两家芯片巨头在过去一周针对其产品的单独研究发布了回应。该研究项目针对英特尔和 AMD 可信执行环境 (TEE)，旨在通过将受保护的应用程序或虚拟机 (VM) 与操作系统和在同一物理系统上运行的其他软件隔离来保护代码和数据。

**01**

**CounterSEVeillance 攻击方法详解**

周一，由奥地利格拉茨技术大学、德国弗劳恩霍夫安全信息技术研究所（SIT）和弗劳恩霍夫奥地利研究中心组成的研究小组发表了一篇论文，描述了一种针对 AMD 处理器的新攻击方法。

这种名为CounterSEVeillance的攻击方法针对的是 AMD 的安全加密虚拟化 (SEV)
TEE，特别是 SEV-SNP 扩展，该扩展旨在为机密虚拟机提供保护，即使在共享托管环境中运行。

CounterSEVeillance是一种针对性能计数器的旁道攻击，性能计数器用于计算某些类型的硬件事件（例如执行的指令和缓存未命中），并有助于识别应用程序瓶颈、过度的资源消耗甚至攻击。CounterSEVeillance 还利用单步执行，这种技术可以让威胁行为者逐条观察TEE 指令的执行，从而实现旁道攻击并暴露潜在的敏感信息。

研究人员解释说：“通过CounterSEVeillance单步执行机密虚拟机并在每个步骤之后读取硬件性能计数器，恶意虚拟机管理程序可以观察机密相关条件分支的结果和机密相关划分的持续时间。”

他们通过在几分钟内从单个 Mbed TLS 签名流程中提取完整的 RSA-4096 密钥，以及通过大约 30 次猜测恢复六位基于时间的一次性密码 (TOTP)，展示了 CounterSEVeillance的影响。他们还展示了该方法可用于泄露派生 TOTP的密钥，以及用于明文检查攻击。

发起CounterSEVeillance 攻击需要对托管硬件隔离虚拟机的机器拥有高权限访问权限——这些虚拟机被称为信任域 (TD)。最明显的攻击者是云服务提供商本身，但攻击也可能由国家支持的威胁行为者（特别是在其本国）或其他资金雄厚、能够获得必要访问权限的黑客发起。

“对于我们的攻击场景，云提供商在主机上运行经过修改的虚拟机管理程序。受到攻击的机密虚拟机在经过修改的虚拟机管理程序下作为客户机运行，”参与该项目的研究人员之一 Stefan Gast 解释道。

**02**

**TDXDown攻击方法详解**

研究人员指出：“来自主机上运行的不受信任的虚拟机管理程序的攻击正是 AMD SEV 或 Intel TDX 等技术试图阻止的。”他们的威胁模型从原则上来说与最近的 TDXDown 攻击非常相似，后者针对的是英特尔的信任域扩展 (TDX) TEE 技术，TDXDown攻击方法上周被德国吕贝克大学的研究人员披露。

Intel TDX 包含一个专门的机制来缓解单步攻击。通过 TDXDown 攻击，研究人员展示了如何利用此缓解机制中的漏洞绕过保护并进行单步攻击。结合此漏洞和另一个名为 StumbleStepping 的漏洞，研究人员成功恢复了 ECDSA 密钥。

**03**

**AMD 和英特尔的回应**

AMD发布公告中表示，性能计数器不受 SEV、SEV-ES 或SEV-SNP 的保护。AMD 建议软件开发人员采用现有的最佳实践，包括在适当的情况下避免依赖秘密的数据访问或控制流，以帮助减轻这种潜在的漏洞。AMD 已在 APM Vol 2 第15.39 节中定义了对性能计数器虚拟化的支持。PMC 虚拟化计划从 Zen 5 开始在 AMD 产品上提供，旨在保护性能计数器免受研究人员描述的监控类型的影响。

英特尔已更新 TDX 以解决 TDXDown攻击，但认为这是一个“低严重性”问题，并指出它“在现实环境中的风险非常小”。该公司已为其分配了CVE-2024-27457。

至于 StumbleStepping的漏洞，英特尔表示“不认为这种技术属于纵深防御机制的范围”，并决定不为其分配 CVE 标识符。

\* 本文为闫志坤编译，原文地址：https://www.securityweek.com/new-counterseveillance-and-tdxdown-attacks-target-amd-and-intel-tees/
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

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrkmUSQ9zhw1T8DXiaYBN9BmZ8PMQCuRvOwHwXYrLgmibzRictZicSIlInAJ3jznMXibOrF4X3W16NSLSg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247515741&idx=1&sn=4844e5434f49a01d9ca7e4dfa5a3cd8a&chksm=c144cce0f63345f682b14293450572f91013bfe8aa243de0049fee6aaf521decb3b74a6bb49f&scene=21#wechat_redirect)

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