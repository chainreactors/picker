---
title: 当你的行车记录仪成为“公共直播”：一次真实的免下车入侵之旅
url: https://mp.weixin.qq.com/s/Of31ZQya0VLymxgqrfU9cg
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:15:10.465744
---

# 当你的行车记录仪成为“公共直播”：一次真实的免下车入侵之旅

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibf0ia3ic4HPmoGkypZ3MibKW1tJm8hg6fDY0S5hVXNuXrpxKv00NPLkJ89YYKqv2Z9ibLru3TChZQ5548osibcsPXThjfNkH0R37nIw/0?wx_fmt=jpeg)

# 当你的行车记录仪成为“公共直播”：一次真实的免下车入侵之旅

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 新加坡的一个安全研究团队进行了名为“Drive Thru Hacking”的实验。他们发现在快餐店得来速通道排队时，就能悄无声息地入侵附近车辆的行车记录仪。调查的20多个品牌中，绝大多数存在令人心惊的安全漏洞：默认密码、未认证接口、公共视频流随处可见。本篇文章将深度解析他们的攻击手法、惊人发现，以及这个我们习以为常的设备如何变成随身携带的隐私定时炸弹。

## “得来速”通道里的黑客

想象一下，你在快餐店的得来速通道等着取餐。前后都是车，一切如常。

但就在这几分钟里，你车里那个不起眼的行车记录仪，可能已经成了别人的“战利品”。你的行程路线、车内的私密对话，甚至你家的停车位置，正被悄无声息地打包发送到一台陌生的服务器上。

这不是科幻电影。

在新加坡，一支名为Sektor的安全研究团队，把这件事变成了现实。他们管这叫“Drive Thru Hacking”（得来速入侵）。这个项目听起来有点疯狂，但他们的演示视频和严谨的研究数据，让人脊背发凉。

团队核心成员Benjamin、George和Chi Peng，采购了20多台行车记录仪，招募了40多位真实车主作为测试参与者，在新加坡扫描了超过1000个行车记录仪的Wi-Fi信号（SSID）。

他们想搞清楚：这些为了安全和便利安装的小玩意，本身到底安不安全？

答案是：糟透了。

## 行车记录仪：安全思维里的“盲区”

为什么要研究行车记录仪？

很简单，因为它太普及了，而且恰恰位于“安全”与“不安全”的认知裂痕之中。根据团队的研究，至少80%的车主会安装行车记录仪。主要动机明确：事故证据、降低保费。

但问题就出在这里——用户和厂商的注意力几乎全被“画质是否清晰”、“夜视效果如何”占据了。安全性？抱歉，它甚至没出现在备选清单里。

“用户通常更看重画质而非安全性，”研究者在演讲中坦白，“安全性甚至不在他们的次要考虑范围内。”

这种普遍心态，催生了一个极度追求成本控制的硬件市场。大多数热销品牌，如Blackview、70mai、Thingware，都产自亚洲，并以极高的性价比占领了北美等地市场。

更隐秘的风险在于，为了压缩成本，许多不同品牌的行车记录仪，实际上共享着相同的硬件方案乃至固件。

一个漏洞，就可能横扫一大片。

## “免下车”入侵实战：十分钟，从扫描到掌控

“得来速入侵”的整个流程高度自动化，团队将其拆解为10个阶段，核心思路简单直接：发现、连接、绕过认证、窃取数据、实现持久控制。

**第一步：寻找猎物**

就像传统的“Wardriving”（驾车搜寻无线网络），只不过他们把地点固定在了排队队伍里。

“我们尝试过在移动中攻击，可能因为驾驶技术不行，没法保持车距维持连接。”研究者带着一丝幽默说，“如果我们车技好点，移动攻击完全可行。”所以，他们选择了更稳妥的静止目标——排队取餐的你。

工具自动扫描周围的Wi-Fi，筛选出属于行车记录仪的SSID。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcjwxjWtNedcEicUDQLr7vIDuwWhInnu8CSG3UpQG352HX1j7KibLoD8Kic9LPOzngZYhNqvMmAiaIndUjj7Cl8aPZG1XUibOia6sSpM/640?wx_fmt=png&from=appmsg)

**第二步：叩开大门——密码的虚弱无力**

连接Wi-Fi需要密码。这是第一道，也是最脆弱的一道防线。

在研究团队购买的20多台、涵盖16个品牌的行车记录仪中，有15个品牌为旗下所有设备设置了同一个默认密码。

是的，全系通用。

只有一个品牌（在他们匿名化报告里被称为某个字母）为每台设备生成了唯一密码。但讽刺的是，这个“高级”密码也只是由8位小写字母组成。研究团队估算，利用云端算力暴力破解，几个小时就能搞定。只是这不符合他们“快速入侵”的场景，所以没采用。

更离谱的是，有四个品牌的行车记录仪，密码不仅固定，而且用户**无法修改**。这意味着，任何进入Wi-Fi信号范围内的人，都能用公开的默认密码连上去，车主对此无能为力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdWQIhvxeJ0g1NIptXmrx4pXW4GkMxjtc728pw2H0jTqpHQE9IiaCDV2p8Iyhk10ibYX1HoCBq52c9ZHrr4zNHh4tqQ11ooLWOy0/640?wx_fmt=png&from=appmsg)

“我们的攻击时间窗口很短，”研究者解释，“所以我们只摘那些‘低垂的果实’——用默认密码、常见密码或固定密码的设备。”

这只是开始。

## 绕过重重“安全机制”：厂商的承诺像纸一样薄

一些厂商意识到密码不安全，于是增加了第二道防线：“设备配对”。用户需要在手机App上操作，并**物理按下**行车记录仪上的Wi-Fi按钮，才能完成绑定。理论上，这能防止远程攻击。

可惜，理论只是理论。

对于他们测试的“C型号”行车记录仪，攻击者连接到它的热点后，无需任何配对，就能直接访问HTTP服务器和视频流。“完全远程的攻击”成为可能。

对于那些确实依赖配对流程的品牌，研究团队发现了更致命的缺陷。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdeE3lFMBndy6JOTNOTxQCwPTicpxeXeJbYotp3UbU86iccnI6jmic7a5SxtoDm6cXLCfAict6sfaDibAOzqaRqsIZ9SIY5Wz4zOod8/640?wx_fmt=png&from=appmsg)

> 行车记录仪会把已配对设备的MAC地址（网络设备的唯一硬件标识）存下来。攻击者只需要扫描获取到车主手机的MAC地址，然后伪造（Spoof）这个地址，就能被行车记录仪当作“已信任设备”，轻松绕过物理按钮验证。

演示视频中，他们用树莓派（Kali Pi）轻松实现了这一点。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfPYCyWLLKGOeE8ZpXqC9qul2KmqQopgYJLXLdd6ic3SfhVINQ3W31Lma8ib8iab9uPqVJtxVHcZzTksosngVxTu31gFDsKgsJVYQ/640?wx_fmt=png&from=appmsg)

更有甚者，他们可以发动“MFA疲劳攻击”（多因素认证疲劳）。脚本持续向行车记录仪发送大量配对请求，导致设备不断发出语音提示：“按下Wi-Fi按钮以注册智能手机…按下Wi-Fi按钮以注册智能手机…”

试想，当你开车时，行车记录仪一直在你耳边重复这句话，你会怎么做？大多数人最终会不堪其扰，按下按钮。攻击者就此得逞。

“这是个非常恼人的因素。”研究者半开玩笑地说。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdJanetIdpBcN4HHTAMq5ap8FR4S7MYiaNKKXzAZ7eUJFjscfANfViao6tDpap8Z42adKGXYYFSbSrn6IjWPhdXEbGumJ0SCDaIY/640?wx_fmt=png&from=appmsg)

## 数据失守：你的生活成了公开直播

一旦进入网络，行车记录仪里的数据就像敞开的仓库。FTP、Telnet、HTTP API、RTSP流媒体协议……敏感接口随处可见。

有些设备的安全设计堪称“行为艺术”。比如B型和O型行车记录仪，它们使用自定义协议。首次扫描只开放7777端口（API端口）。攻击者通过分析APK文件，向这个端口发送一个特定的字节序列，就会像“敲门”一样，临时打开7778和7779端口，用于传输视频和音频文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeDcHJnNukkHSEJfORx0qicjjxhZEia09HtcQ7x3RBkuYft9GkUp0BQpic4icCAQyJBibxl8BCr6T7MUWicp7ZFbFg31JkGg5caoqGy8/640?wx_fmt=png&from=appmsg)

最令人震惊的发现来自云功能。

一个名为Dashcam D的品牌（匿名），其手机App允许用户“分享实时画面”。听起来很酷？结果是灾难性的。

研究者下载了这个App，即使没有任何设备，也能浏览一个公开视频流列表。他们随机点开几个：

* 一个视频里，一位好心车主在帮助另一辆车处理故障卡，随后开车回家，车库和家庭住址在视频和地图上清晰可见。
* 另一个视频里，一对游客搭乘网约车，兴奋地讨论着旅行计划、共同朋友的名字，甚至晚餐吃什么。他们对这场“公开直播”毫不知情。

团队将这个问题作为配置错误报告给厂商。厂商的回复让人无语：这是设计功能，目的是让用户能“身临其境感受全球驾驶的刺激与乐趣”。App角落里的小字确实提到了分享功能。

“我们认为这些措辞太过理想化，对隐私问题轻描淡写。”研究者评价道。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeDQszsBIoVUsGOquhKdfKmzDDsJUQO83rQHcgC5oKTeorU65rAAUEs22zicyPbZrTbwYnVzwv1gkNmZExk6ibyG99NwrzYbYbE8/640?wx_fmt=png&from=appmsg)

> 你的行车记录仪，可能正在某个陌生人的手机屏幕上，直播你的一举一动。而你，甚至从未打开过那个分享选项。

## 从窃听到破坏：入侵的终局不止于偷看

获取视频只是第一步。在K型号行车记录仪上，研究者发现了HTTP服务器上的一个未认证文件上传漏洞。他们上传了一个基于CGI的Webshell，成功获得了远程命令执行权限，进而拿到了系统的root密码。

之后，能做的事情就多了：

* **钓鱼与欺诈**：修改配置文件，让车主的手机App在更新时，下载的是攻击者的恶意软件。
* **物理破坏**：关闭电池保护设置，让行车记录仪在车辆熄火后依然持续耗电，一夜之间就能耗尽汽车电瓶。
* **“反客为主”**：修改Wi-Fi密码，把真正的车主锁在自己的设备外面。
* **直接“变砖”**：尝试上传更复杂的后门程序时，设备直接崩溃、无法启动。这些设备的稳定性脆弱得惊人。
* **远程瘫痪**：在Q型号设备上，他们登录Telnet后触发了一个脚本，导致设备网络协议栈崩溃，指示灯狂闪。由于设备内置电池且无法强制重启，用户只能等半小时甚至更久，让它自然耗光电量。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeprFNibHAUW0A2ibmb6YIndDiaUw5xUtIib6AXntkzTSx6cavsvwGxic45J2HIL5aGaJMHibaKg7HERKBoBib4qdJs9zEPZKOyyPNXxM/640?wx_fmt=png&from=appmsg)

## 持久化攻击：你的车被“附身”了

得来速通道的接触是短暂的。但研究团队想得更远：能不能在车辆离开后，依然保持控制？

他们瞄准了带4G/5G模块的行车记录仪。这类设备内置SIM卡，支持远程查看，是天然的“跳板”。

挑战在于让攻击脚本在设备重启后依然存活。他们尝试了两种方法：

1.  **利用开机脚本**：将恶意代码注入到系统初始化脚本中。但很多设备使用只读文件系统，修改仅存在内存里，重启就失效。

2.  **挂钩二进制文件**：直接修改系统核心组件，实现更深度的持久化。这招更狠，但也更危险。一个失误就会让设备“变砖”。分享者坦言自己就写错过一个循环，导致设备再也无法启动。

“![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibfwf1XngYvL1IpKRBHBXyhQ72lTKUicsIdiczEN8icrK9SSBPKQrvOLFrQ7mwpvjbWjr2f23NtNVLib9BqshX1UjuGUCcjibkjXW9gY/640?wx_fmt=png&from=appmsg)

一旦实现了持久化控制，攻击者就能让行车记录仪定期“回拨”到命令控制（C2）服务器，持续上传GPS数据、音频和视频，实现长期监控。

他们还利用AI技术提升数据“变现”能力：用OCR识别路牌推测位置，用Whisper转录车内对话，用大语言模型（LLM）总结核心信息，甚至生成“AI漫画”来生动呈现车主的行程和对话。

仪表盘上，一个人的生活轨迹和隐私，被清晰、结构化地展示出来。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcspB7BLTy9aZGVXPvDQEhkKMhRQjwmrzu3dCVkGhPSXf9mOPKs2dOC3nepQwbwtLJf6VKFwIlFELX3GhHcfZUkYGAPQ95Eyrc/640?wx_fmt=png&from=appmsg)

## 现实世界的攻击成功率有多高？

实验室成功不算数。他们用红队工具对40位真实参与者的车辆进行了受控测试。

结果是：**40台设备中有11台被成功入侵**。

那些失败的，多是因为具体配置与实验室样本有差异导致脚本报错。成功的，则无一例外是因为行车记录仪的配置与漏洞利用条件“完美契合”。

其中，密码策略是决定性因素。

在可以修改密码的设备中，只有一半的车主真的改了。而更根本的问题是：**65%的参与者使用的行车记录仪，来自那四个根本不允许用户修改密码的品牌**。

“如果不能更改密码，就会被黑客攻击。”结论简单而残酷。

更讽刺的是，他们购买的20台二手行车记录仪中，有5台的存储卡里还留着原主人的录像。隐私，在设备转手时被彻底遗忘。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeXGBZj5YBDySZYpsrYg6wKiaMMKTaVicHtrEKTfEXJxSxwmN0xs73ZOnuDWTiaUCDKuWq5cBNk04GVnx102du6UahYIJskqQEQFk/640?wx_fmt=png&from=appmsg)

## 悲剧能否避免？给厂商和用户的最后警告

研究团队没有止步于攻击。他们开发了对应的“蓝色模块”——一套行车记录仪加固方案。通过获取root权限，植入防护脚本，实现MAC地址白名单、简易应用层防火墙（WAF）等功能，堵住已发现的漏洞。

他们甚至构想了一个“硬件加密狗”产品，插上就能为行车记录仪提供安全加固。

但这些都是“民间偏方”。问题的根源在于厂商。

团队尝试了负责任的漏洞披露。在联系的16个品牌中：

* 仅1个品牌设有专门的安全联系邮箱。
* 10个品牌使用通用邮箱。
* 剩下5个“山寨”品牌，根本找不到任何联系方式。

在收到报告的厂商中：

* 5家承认了问题。
* 仅1家通过App更新发布了修复。
* 2家表示正在开发补丁。

最大的“成果”是，有一家原本没有任何安全响应流程的制造商，因为这次接触，正在考虑建立相关机制。

“![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc3VgQVdic9UrohgxqzfTPRUNt2AOHKdWutTqcAChAicgJWa4awc8m14L78o7Co6Y6biaCF8icFXwt6VbDzUNvYEh6wtalKECibNaWs/640?wx_fmt=png&from=appmsg)

说到底，行车记录仪的安全危机，是消费电子领域“重功能、轻安全”痼疾的缩影。厂商为了成本和易用性牺牲安全，用户则毫无防备地将一个潜在的间谍设备装在了车里。

他们的研究还在继续。下一步，他们想展示如何将行车记录仪变成“移动中的僵尸网络”。

演讲最后，研究者半是调侃半是严肃地说，他们“缅怀”了许多在测试中“牺牲”的行车记录仪。“这些硬件既复杂又敏感……但我们可能找到了一种方法复活它们，也许能把它们变成科学怪人。”

而我们，是否也要等到自己的隐私被做成“AI漫画”公开展示时，才会醒过来？

给你的行车记录仪改个密码吧。如果它允许的话。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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