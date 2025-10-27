---
title: 打破物理隔离！多个政府机密系统遭APT组织攻破
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512759&idx=1&sn=f8e4e1c802e414d2df292cf24a9abc10&chksm=ebfaf597dc8d7c8107b2cb74780a5c04e648f2508cae58aa7acf93d657d3edf0b9021c9169ea&scene=58&subscene=0#rd
source: 安全内参
date: 2024-10-10
fetch_date: 2025-10-06T18:53:51.768282
---

# 打破物理隔离！多个政府机密系统遭APT组织攻破

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7v9LZFaHftwOadLB78oEYrWD4ib3vibKT8QkTclibLo3dGs73PWIhWibG9jSf3phdMz1SoBmhxmqbI8dA/0?wx_fmt=jpeg)

# 打破物理隔离！多个政府机密系统遭APT组织攻破

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tOiaW1QLOL6usmkMDCU0wCorXE2Of8aL4MtmOXyIJN3QTQfibQL7gcTL5GS4FMQr1A7MqyaUTXmRkA/640?wx_fmt=jpeg)

**APT组织GoldenJackal利用U盘等介质实施摆渡攻击，至少两次成功穿透了政府机密系统实施窃密活动，受害者包括某南亚国家驻白俄罗斯大使馆、某欧洲政府机构。**

前情回顾·**打破物理隔离神话**

* [打破物理隔离：RAMBO侧信道攻击令人防不胜防](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512604&idx=2&sn=e28691514456eaaed77ba791576fd2c3&chksm=ebfaf53cdc8d7c2a02dccd185b89c58ddd28fe1eff746588cc7c1e93ff18b3a83b034ad31818&scene=21#wechat_redirect)
* [打破隔离网络！研究员披露最新DNS窃密漏洞](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507030&idx=1&sn=6a65d5507431119d6b6459321a4e5afb&chksm=ebfa9b76dc8d1260e4517484a586925dd9bef68de3245988f7af372f24acc2e8cd72d7644215&scene=21#wechat_redirect)
* [打破物理隔离！利用电源信号灯的轻微闪烁进行窃听](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247498787&idx=1&sn=55cab117a119e7e19826952fa8768b1d&chksm=ebfabb03dc8d32156b8ad95262d37736c350d991eb71bf78699c1a6bda038d1030b3eba96722&scene=21#wechat_redirect)
* [物理隔离神话的迷信or自信？击穿气隙系统的17个恶意软件框架](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247500498&idx=4&sn=0580be99bb7bd1a1bdfcb0c35b3766e8&chksm=ebfa85f2dc8d0ce44a39f73585083b8b6c1129c38286097468af89a9d6885e55312347005f51&scene=21#wechat_redirect)

安全内参10月9日消息，一个名为GoldenJackal的APT黑客组织成功攻破了欧洲政府机构的气隙隔离系统。黑客使用了两套自定义工具集窃取了大量敏感数据，包括电子邮件、加密密钥、图像、档案以及文件。

根据欧洲安全厂商ESET的报告，至少有两波重大事件与此有关。第一波发生在2019年9月和2021年7月，目标是某南亚国家驻白俄罗斯大使馆。第二波事件针对的是一个欧洲政府机构，具体发生在2022年5月至2024年3月之间。

2023年5月，卡巴斯基发布了关于GoldenJackal活动的警告，指出该威胁行为者专注于政府和外交机构，主要目的是进行间谍活动。

虽然早已知晓GoldenJackal通过USB闪存驱动器传播自定义工具，例如“JackalWorm”，但此前并没有确认过成功攻破气隙隔离系统的案例。

气隙隔离系统常用于关键操作，专门管理机密信息。作为一种安全措施，这类系统与开放网络完全隔离。

**穿透气隙系统发起攻击**

ESET观察到的较早攻击表明，黑客的第一步是感染连接互联网的系统，可能是通过被植入木马的恶意软件或文档。该阶段，黑客使用了一种名为“GoldenDealer”的恶意软件。

GoldenDealer监控这些系统上插入的USB驱动器。一旦检测到USB插入，它会自动将自身及其他恶意组件复制到USB设备上。最终，当同一USB设备被插入气隙隔离的计算机时，GoldenDealer就能够在隔离系统上安装“GoldenHowl”后门和“GoldenRobo”文件窃取器。

在此阶段，GoldenRobo会扫描系统中的文档、图像、证书、加密密钥、档案、OpenVPN配置文件等有价值的信息，并将其存储在USB驱动器的隐藏目录中。

随后，当USB驱动器从气隙隔离的计算机中移除并重新连接到原先联网的系统时，GoldenDealer会自动将存储在驱动器上的窃取数据发送到威胁行为者的指挥与控制（C2）服务器。

“GoldenHowl”是一种多功能的Python后门，具备文件窃取、持久性维持、漏洞扫描以及直接与C2服务器通信的能力。ESET表示，这款工具似乎专为联网的机器设计。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7v9LZFaHftwOadLB78oEYrWR8PFiagozoMLLfL9YSraoghf7p0lkgzozWPGqgy9yGeLG5j1ibF5XGUw/640?wx_fmt=other&from=appmsg)

*图：GoldenJackal攻击概述*

**新的模块化工具集**

从2022年开始，GoldenJackal使用了一套基于Go语言开发的新型模块化工具集，执行与之前类似的活动，但该工具集允许攻击者为不同的机器分配不同的角色。

例如，一些机器专门用于文件外传，而另一些机器则作为文件的暂存点或配置分发节点。

感染USB设备的新恶意软件被命名为“GoldenAce”，而负责窃取文件并将其发送给攻击者的工具被分别称为“GoldenUsbCopy”和“GoldenUsbGo”，其中后者是前者的升级版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7v9LZFaHftwOadLB78oEYrWs6HxLejNnkt5WWmAhN7hwfibIqosia0s2xiaJL37HM2r1hqAKR3StHb4A/640?wx_fmt=jpeg&from=appmsg)

*图：GoldenUsbCopy和GoldenDealer的代码比较*

GoldenUsbGo不再使用AES加密配置，而是根据硬编码指令外传文件，传输的文件包括最近14天内修改过的文件，且文件大小不得超过20 MB。除此之外，GoldenUsbGo还会筛选特定内容的文件，例如包含“pass”、“login”或“key”等关键词的文件，或某些文件类型（如.pdf、.doc/.docx、.sh、.bat等）。

另一个值得关注的恶意软件组件是“GoldenBlacklist”，其基于Python实现的版本名为“GoldenPyBlacklist”，该工具负责在文件外传之前过滤和归档特定的电子邮件信息。

最后，GoldenMailer负责通过电子邮件将窃取的信息发送给攻击者，而GoldenDrive则用于将数据上传到Google Drive。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7v9LZFaHftwOadLB78oEYrWxTYNoOZxk7SIn6hsPB69DApd9lC39xVXG2RNSCGvCrmjRwZNoND4EQ/640?wx_fmt=other&from=appmsg)

*图：在欧洲攻击中使用的更新工具集*

这些工具集与卡巴斯基报告中描述的部分工具有一定重叠，表明GoldenJackal具备开发新型自定义恶意软件的能力，并能持续优化这些工具以进行隐蔽的间谍活动。

关于这些工具的完整威胁指标（IoCs）列表，可参阅GitHub页面：

https://github.com/eset/malware-ioc/tree/master/goldenjackal。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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