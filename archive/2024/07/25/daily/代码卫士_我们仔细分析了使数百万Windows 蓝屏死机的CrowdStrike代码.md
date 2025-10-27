---
title: 我们仔细分析了使数百万Windows 蓝屏死机的CrowdStrike代码
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520194&idx=1&sn=8b7005cae90d257d5bb3feff7e6a7434&chksm=ea94bea8dde337be4a06359bee3c3f03fbe5d237fc4b37d86075295fbe2ce7932397fb5fbae4&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-07-25
fetch_date: 2025-10-06T17:44:22.495331
---

# 我们仔细分析了使数百万Windows 蓝屏死机的CrowdStrike代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFqoaWD6xPKzv4niaIDTohhfkswLajPk9U09nwGt6VnfaF8kjxCXYsFIQ/0?wx_fmt=jpeg)

# 我们仔细分析了使数百万Windows 蓝屏死机的CrowdStrike代码

Thomas Claburn

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**上周，杀毒厂商 CrowdStrike 为使用广泛的 Falcon 平台发布更新，导致全球微软设备崩溃。**

该事件影响广泛。供应链公司 Interos 估测CrowdStrike 和微软的674620名直接企业客户关系受影响。微软表示850万台 Windows 机器无法运作。除了投入大量的IT修复时间外，大规模的 Windows 系统崩溃导致全球航空和运输交付延迟。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFicWlbzicKZ0EJLQtTWOxgibLJMxd3DibA5Mgs3PcbVQCvu96rLYiaicOPjXw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

**空字节还是逻辑错误？**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

CrowdStrike 公司目前给出的事件原因是“一个逻辑错误导致系统崩溃和受影响系统上出现蓝屏。”系统崩溃源自可能损坏的数据进入Falcon 的配置文件 Channel File中，而该文件负责控制 CrowdStrike 安全软件的运作方式。Channel File 由 CrowdStrike 负责更新并推送到运行该软件的系统中。而 Falcon 通过这些文件中的信息检测并响应威胁。而这是Falcon 基于行为的机制来识别、强调和对抗计算机上恶意软件和其它非必要活动的一部分。在本案例中，配置文件被推送到运行 Falcon 的 Windows 计算机中，达到导致系统崩溃的点。重启受影响机器时，Falcon几乎会立即启动并再次崩溃。

CrowdStrike 提到，Windows 机器上的 Channel File 存储在如下目录中：

C:\Windows\System32\drivers\CrowdStrike\

这些文件的命名方式为 “C-“ 之后添加唯一的识别号码。本案例中该文件一“C-00000291”开头，随后是多个其它号码，并以扩展 .sys 结尾。但 CrowdStrike 公司表示这些都不是内核驱动，而是Falcon 使用的数据文件，它们确实在驱动层运行。

也就是说，损坏的配置文件虽然并非驱动可执行文件，但由 CrowdStrike 高度可信的且可在操作系统上下文中运行的代码进行处理。当恶意文件导致代码不受控制后，会破坏整个周边操作系统即本案例中的 Windows。

CrowdStrike 公司在上周末发布的一份技术总结中解释称，“Channel File 291 控制 Falcon 评估 Windows 系统上 named 管道执行的方式。Named 管道用于Windows 中正常的、进程间或系统间的通信。”

CrowdStrike 公司提到，“在协调世界时 (UTC) 04:09发生的更新旨在针对网络攻击中常见C2框架所使用的新发现的恶意named管道。配置更新触发逻辑错误，导致操作系统崩溃。”换句话说，CrowdStrike 发现恶意软件滥用Windows的一个特性即 named 管道来与恶意软件的C2服务器进行通信，通常是下令恶意软件执行所有恶意类型。CrowdStrike 公司推送配置文件更新来检测和拦截管道滥用，但该配置文件导致 Falcon 崩溃。

虽然有人猜测该错误是因为 Channel File 中的空字节导致的，但CrowdStrike 坚决否认这一说法。CrowdStrike 公司提到，“这和Channel File 291或其它 Channel File 中包含的空字节毫无关联。”该公司承诺将进一步分析事件根因来判断该逻辑缺陷是如何发生的。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFicWlbzicKZ0EJLQtTWOxgibLJMxd3DibA5Mgs3PcbVQCvu96rLYiaicOPjXw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

**Falcon 访问不存在的内存信息**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

虽然关于该逻辑错误的具体详情尚未正式披露，而 CrowdStrike 公司的首席执行官 George Kurtz 被要求就此在国会接受质询，但安全专家如谷歌 Project Zero 团队的技术大拿 Tavis Ormandy 和 Objective-See 公司的创始人 Patrick Wardle 都以令人信服的说法提到，Channel File 在某种程度上导致 Falcon 能够访问内存中并不存在的信息，从而导致系统崩溃。

Falcon 似乎从一个循环中的内存的一个表格中读取了条目，并利用这些条目作为进入内存实施进一步操作的指针。当至少其中一个条目不正确或不存在时，由于该配置文件的原因，它包含一个垃圾值，内核级别的代码就会认为该垃圾值是有效的并进行使用，从而导致访问未映射的内存。该恶意访问被进程器和操作系统捕获，并触发蓝屏死机，因为在这时操作系统认为非常底层的地方发生了异常。实际上在这种情况下崩溃要比尝试继续并乱写数据并引发更多损失要更好。

Wardle 表示，崩溃转储和反编译表明系统崩溃源自试图将未初始化数据当作指针（野指针）来用，但其余详情尚不得而知。他表示，“我们仍不清楚Channel文件为何会触发崩溃的确切原因”。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFicWlbzicKZ0EJLQtTWOxgibLJMxd3DibA5Mgs3PcbVQCvu96rLYiaicOPjXw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

**内核悖论和缺少QA**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

网络安全老兵、OpenSSF的总经理 Omkhar Arasaranam 认为，确切原因仍然止步于猜测，因为他无法访问 CrowdStrike 的源代码或者 Windows 内核。

他指出，CrowdStrike 的 Falcon 软件由两个组件组成：一个是数字化签名且由微软批准的驱动 CSAgent.sys，另外一个是通过最新安全信息更新软件的 Channel Files。

他分析表示，“CrowdStrike 所做的本质上是拥有一个已签名的驱动，之后加载了一些 Channel 配置。我们不清楚该Channel 配置文件牵涉的内容，它是文件中的内容和 CSAgent.sys 解释方式的结合。”

他解释称，从一个堆栈跟踪来看，CSAgent.sys 因为执行恶意指针解引用而被终止。它尝试从地址 0x000000000000009c 访问内存，但实际上该内存并不存在。

他提到，“它本不应具有访问这个内存区域的权限。当你拥有一个像这样非常底层的程序时，就会遇到一种悖论：内核整体应当为操作系统做很多底层操作如内存分配等担责。因此，如果内核，本质上，尝试访问它不应访问的内存，那么从操作系统理论层面来看，正确的做法是假定已被分配的内存没有一个是安全的，因为如果内核不了解，那么实际上就会使系统停止。”再加上 Windows 驱动架构运作方式即驱动可设置标记boot-start，这一情况更加复杂。

他解释称，“因此正常情况下，如果驱动存在bug并导致类似后果，那么Windows可通过在下次不加载该驱动的方式自动恢复。但如果被设置为应该是为关键驱动如硬盘保留的 boot-start，那么Windows 就不会将其从启动序列中删除，并将继续一再失败，也就是我们看到的 CrowdStrike 一样的失败。”

*（我们认为微软建议人们重启Azure上受影响 Windows 虚拟机多达15次次以解决该问题的原因，就是因为每次该出错的配置文件将在 CSAgent.sys 驱动开始解析之前自动更新到未损坏的文件存在较小的概率。多次重启后，用户终究会获得这种竞争条件。）*

Arasaratnam 表示，除此以外，我们将无法知道告知 CSAgent.sys 进行恶意指针解引用的 Channel File 更新如何设法通过了质量保证 (QA)。他指出，“鉴于崩溃发生的频率，似乎很明显一些内容通过了QA。即使是一个简单的QA就会捕获到这种情况。它不同于千分之一机器的极端案例，对吧？”

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFicWlbzicKZ0EJLQtTWOxgibLJMxd3DibA5Mgs3PcbVQCvu96rLYiaicOPjXw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

**最佳实践**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRfkFlrDPxnGCXQibQBicianfFprSS8EichWnIluJ8w4UwsJRUhiaUL9ic1vhTetzoAJvBjgeU3icFX7LAXw/640?wx_fmt=png&from=appmsg)

Arasaratnam 表示，本应注意到多个最佳实践。其中一个是尽可能不要在内核模式下运行软件。第二个是确保进行进行更彻底的QA。第三，像谷歌一样，部署增量金丝雀发布。

他解释称，“我在谷歌时，所使用的其中一种技术是进行金丝雀发布——渐进或缓慢上线——并观察正在发生的情况，而不是导致如微软估测的850万台机器崩溃。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[微软：是欧盟把Windows 内核的密钥交给了 CrowdStrike，触发蓝屏死机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520167&idx=1&sn=8e80c74dda2ec337dca9a0451873c7bc&chksm=ea94becddde337dbdaf65d39b9eb60cb90bd15bc0a6dabb0defc375c80975c52f344d6b5405f&scene=21#wechat_redirect)

[关于CrowdStrike 使 Windows 蓝屏死机，你需要知道的都在这里](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520109&idx=1&sn=f70fb8a65546c2f9ad15c895357b4258&chksm=ea94be07dde33711cb8de08051d20315cae01150c1cce58af83248ce1933418d827a742b82ab&scene=21#wechat_redirect)

[Falcon Sensor 在数周前导致 Linux 内核崩溃 恢复工具已推出](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520157&idx=2&sn=a93459b30ee5e2a9c5d7fde92fbadf1f&chksm=ea94bef7dde337e10afa600f28254053392253623ae5fc070b7b622dcdff148744cc5c6cc9cf&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/07/23/crowdstrike\_failure\_shows\_need\_for/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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