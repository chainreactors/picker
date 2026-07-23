---
title: Android AI Agent现漏洞，隐形文本可执行主机代码
url: https://mp.weixin.qq.com/s/i69VBFscdZDVKoIshijNpQ
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:06:53.382657
---

# Android AI Agent现漏洞，隐形文本可执行主机代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2pmW1OlUju4teibav0JWHYakfkbV8auptDsSeiaia06vVpaMW5NAubNribFbEkOT4udiciby8S1MaWILekrppCRPIIoWyTCeBfc7hEk/0?wx_fmt=jpeg)

# Android AI Agent现漏洞，隐形文本可执行主机代码

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0lTkv52xq9XNSEweibBESHjyVA0yRR4ybK6NF9oWXCjGIGCENjzyNk09MNBedVFUrEzjYYQnNjibyAkXXRKm8VsYr6z9YZyCZec/640?wx_fmt=gif)

![first look at rabbit's Android agent](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0WBibFzmPlqRYyXPiceqiaQ8VU9sBwwFpkKhLgxPNAVbTnEOfTgPzWUJvYNQRhFDTBglPSSiacg0keUYZHJIPHKMx2mgRz7ia3Of7E/640?wx_fmt=jpeg&from=appmsg)

一款能在其他窗口上绘制内容并向共享存储写入数据的Android应用，可以向驱动该手机的AI Agent发送指令，这些指令以文本形式呈现，但人眼完全不可见。再通过两步操作，同一款应用就能在驱动Agent的PC上运行命令。

研究人员针对五个开源移动Agent框架（AppAgent、AppAgentX、Mobile-Agent-v3、Open-AutoGLM和MobA）演示了上述攻击链及其他六种攻击手法。每个框架至少被其中六种攻破。

该论文于7月1日上传至arXiv，7月14日修订。作者来自西蒙菲莎大学、香港中文大学、山东大学以及中国安全公司奇安信旗下的星图实验室。

这些漏洞均未分配CVE编号。第一作者张子东告知The Hacker News，团队没有证据表明这些技术已在受控环境之外被使用。The Hacker News检查了全部五个框架，发现论文中描述的截图路径、shell调用和广播回退机制截至7月17日仍存在于它们的主分支上。

张子东表示，团队在发布预印本之前已私下联系了受影响的维护者，但“至今未收到回复”。

Part01

攻击链：从屏幕到主机

最不夸张的部分是利用权限提升。AppAgent的控制器通过subprocess.run(adb\_command, shell=True)运行命令，并将模型输出直接放入adb shell input text {input\_str}来构建文本输入。论文列表显示，该函数完全没有进行任何清理。

实际代码稍好一些，但远未达标：它在字符串插值前仅去除了空格和单引号，却保留了其余所有shell元字符——;、&、>等均未处理。因此，模型从屏幕上读取并忠实输入的字符串会被主机shell拆分，后半部分就会在操作员的Windows主机上执行。

一个设计用于启动calc.exe的载荷，在针对AppAgent、AppAgentX、Mobile-Agent-v3和MobA的20次试验中全部成功。针对AppAgent的另一项端到端测试使用了test;pwd>rce\_success，将主机的当前工作目录写入了一个文件。

要让该字符串出现在模型“眼前”，需要利用文件竞争条件。Open-AutoGLM先执行screencap -p /sdcard/tmp.png，然后单独执行adb pull。Mobile-Agent-v3将截图写入固定的/sdcard/screenshot.png，并在两步之间休眠半秒。AppAgentX写入/sdcard/下带时间戳的文件名，其中包含递增的步骤计数器，攻击者可以监控该模式。AppAgent自带的config.yaml仍将其截图目录默认设为/sdcard。

研究人员测量了这些框架中两个步骤之间的时间窗口，范围在50至500毫秒之间，平均约210毫秒（100次运行）。一个每5至10毫秒轮询一次的后台服务，完全有时间获取文件锁、重绘PNG图像，并在Agent收集前释放。篡改操作在五个框架中的四个上取得了19/20到20/20的成功率。

为了进一步扩大时间窗口，研究人员向Agent展示了一个不可见的覆盖层，声称“网络同步正在运行”，要求它等待3秒。模型相信了该提示。

Part02

视觉幻觉与人眼盲区

研究人员测试的所有六个视觉模型，在至少18/20的实验室试验中都能读取2%透明度的文本。论文指出，该透明度水平低于正常观看条件下人类的典型检测阈值。GPT-4o、Claude Opus 4.5、Gemini 3 Pro和GLM-4V均获得20/20的成绩。随着文本可见度增加，得分并未上升，因为一开始就已经满分。

![不可见文本攻击测试](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2XgeDia2rBrvvjHK54CpFtoGrtBJIBZKO6PejFrh4wJyP0l8cVmkZouickicPvp0A1jicjCwuIJMjcy3P0rgzZf4wcKib3humhKYQQ/640?wx_fmt=jpeg)

AutoGLM-Phone（一个在设备本身上运行的9B模型）是六个模型中最弱的，成绩为18/20。人眼存在视觉阈值，但截图没有。

这种不对称性还体现在硬件层面。手机屏幕边缘有圆角并为摄像头开孔，但帧缓冲区仍是矩形，因此渲染到这些区域的像素会位于边框下方，并出现在每一张截图中。在一台Pixel 4上，一个角落约有78像素的隐藏宽度，足以容纳一条简短指令，所有五个Agent都能从该区域读取载荷。

第三种技巧完全跳过了隐蔽性：一个无障碍服务在真实应用上放置了伪造的登录Activity，让Agent将用户的凭证输入其中。人类用户可能会在意外出现的密码提示前犹豫，但五个Agent在100次试验中无一例外。

Part03

键盘未经验证

Agent没有经过授权的通道连接手机，因此它们重用了调试通道，而研究中最简单的攻击就源自于此。Open-AutoGLM将输入的文本进行Base64编码，然后发送到ADB\_INPUT\_B64——这是一个隐式广播，由ADB Keyboard（一款测试自动化工具）接收，该工具设计用于接受任何广播发送的文本。

这正是其文档说明的用途，并且该工具仍在维护中，其4月的预发布版本包含了对Android 16的修复。ADB Keyboard做了README中承诺的事情。是Agent们将测试工具变成了生产级输入管道。

Mobile-Agent-v3维护了一个狭窄的白名单：字母、数字和常见标点通过adb shell input text发送，其余所有字符（即任何非ASCII字符）通过ADB\_INPUT\_TEXT逐字符发送。MobA则更粗暴：它的type\_text函数使用text.isascii()测试整个字符串，因此消息中只要有一个emoji或重音字母，就会通过广播将整条消息一次发送出去。

任何注册了相同动作的应用都会收到同样的载荷，且无需任何权限，因此用户不会收到任何警告。如果攻击者拥有无障碍服务权限，TYPE\_VIEW\_TEXT\_CHANGED还会将同样的文本（包括密码字段）以明文形式暴露给所有五个框架。

这些前提条件都是真实的：需要设备上已安装恶意应用、Agent正在执行任务、USB或无线调试已开启。受影响的开源软件是开发者工具，而非手机上内置的助手。三星Bixby、小米小爱等第一方Agent不在研究范围内，iOS也同样未涉及。

张子东坦言：其中几种攻击仅需最少的Android权限，有一种甚至根本不需要任何权限，这降低了有动机攻击者的门槛。

Part04

无需安装的变种

另一种变体甚至不需要恶意应用。由于载荷可以藏在图像的色度通道而非亮度通道中，攻击者根本不需要接触设备，只需将一张包含载荷的图片放入消息应用，让受害者自己的Agent将其截图下来即可。研究人员称这是“扩展”而非实测结果，它也是唯一不需要安装步骤的版本。

Part05

修复方案

五个框架中的两个已经展示了正确的做法。MobA通过exec-out流式传输截图，设备端没有文件可竞态；Open-AutoGLM将参数以列表形式传递而非拼接字符串，是五个中唯一对主机命令注入免疫的。但没有一个项目同时做到这两点。以下所有修复方案都不需要修改模型本身：

* 放弃shell=True，改用argv列表传递参数，使元字符保持字面意义。
* 流式传输截图而非“写入再拉取”，避免设备端文件和TOCTOU窗口。
* 在输入广播上设置签名级别的权限，或使用显式Intent。
* 在执行每个动作前后对比前台Activity，并维护每个任务的包名白名单。
* 在模型查看截图前，对截图进行对比度增强处理（部分缓解，非根本修复）。

最显而易见的防御措施是在敏感操作上加入确认提示，Open-AutoGLM已经具备此功能。当模型判断某操作为敏感操作时，会弹出确认提示。但感知攻击会重写这一判断，因此论文认为该提示不足以防御隐式注入、UI欺骗和截图篡改。

对于广播嗅探和无障碍服务嗅探，确认提示完全无效，因为根本没有需要确认的动作——文本已经泄露了。而对于角落和开孔注入，研究人员直言不讳：“没有直接有效的基于软件的解决方案。”对角落进行遮盖只是针对硬件事实的一种权宜之计。

Part06

无处报告

沉默背后有其结构性问题。张子东表示，团队选择发送私人邮件，是因为这些项目没有专门的漏洞报告渠道。The Hacker News发现，五个仓库均未发布任何安全策略。论文还提到，团队首先联系了腾讯和阿里巴巴，但研究级的开源项目通常不在安全响应中心的范围之内。

对比微软5月关于其Agent框架Semantic Kernel的文章，相同的模型输出到达shell的模式导致了CVE-2026-25592、CVE-2026-26030和一个已修补的版本。微软的一句话总结可以直接套用：“你的LLM不是安全边界。”

覆盖层攻击并非全新发现。Wu等人于2025年5月通过覆盖窗口对AppAgent和Mobile-Agent实现了提示注入，Ding等人于同年10月提出了仅在Agent查看时才会显示的提示。这篇论文的相关工作部分既未引用上述研究，也完全跳过了移动Agent安全文献。它新增的是攻击链的终点：从屏幕到文件再到主机。

这引出了尴尬之处。Open-AutoGLM在GitHub上拥有超过25,000颗星，其README指导你启用USB调试、侧载键盘并将输入交给它。完全按照文档操作，你就已经构建了所有经测量攻击所需的前提条件——只差恶意应用本身。这份设置指南就是威胁模型的其余部分。

参考来源：

Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs

https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3M5qLVTGP6jiaibktDcXOic6E1x1CNbVhdStkk8micFrCq9q4Hp2oH9WnQ229S3ziaeHPACAgicCRKZjic3pV1CTArGRs1KdhccugdUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651342454&idx=1&sn=30ae51eba566ed3187493e4e817d3124&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38DqtZUv5FjJ2NibZ3wlLba7jpicoInsIGFnVouGN6kbudJyTf7yhkPM5z8JBrkOVNnialq3PeHX0JzJ9vkBXoUwAdicH70OSf4Wc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1UIicOAoxfTXIH1aV6iaqqHSvodicQ411jpRaOQibuRQRLR562LquiamjNoDmMmbDdgMS39z5nCu480cjyPFJddRlUibicicfCAnfPADE/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3oW9XpIZPMBSeXXX1icBkiaibr55bDylV4OXFt5dTcQ0lJZ3StMsadw1jicJeanJG6hFpSTT6mCsBPpoP1Sx3FWa8HYVODNemRI4Q/640?wx_fmt=png)

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