---
title: 紧急预警！UAC-0247 疯狂扩袭乌克兰：诊所、政府全中招，你的聊天记录和密码正在被偷！
url: https://mp.weixin.qq.com/s/xbWpDTtq6II1qxCdwy6Mlg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:59:13.288012
---

# 紧急预警！UAC-0247 疯狂扩袭乌克兰：诊所、政府全中招，你的聊天记录和密码正在被偷！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/E3ZvvAXyiaibktjs2vJdp9icQcVicIM5q5ShHDIicgCAOLF6OmyvafancJPsFxJpAtZAO8ETDMibcaVQVuAfJJS0tGZibWSDiaxomjZyOPWMdfrfXPg/0?wx_fmt=jpeg)

# 紧急预警！UAC-0247 疯狂扩袭乌克兰：诊所、政府全中招，你的聊天记录和密码正在被偷！

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibnBeZumvF6S5On9jTv6zxcfA97wibvRcy0TURVhgkCRjTiaJC4ibENrDxeZ9mPibdVmABPOibGibshqrUhhp3qAQUrztbx8zNNYwA9Go/640?wx_fmt=png&from=appmsg)

2026 开年最凶的 APT 攻击正在上演。

乌克兰网络安全应急响应中心 CERT-UA 刚刚曝光：神秘攻击组织 UAC-0247 发动大规模跨境网络行动，目标直接对准政府部门 + 公立医院 + 国防机构，从门诊前台到政务后台，无一幸免。

这场发生在2026 年 3–4 月的暗战，手段之隐蔽、链条之完整、危害之严重，堪称教科书级 APT 攻击。

一、伪装到离谱：一封 “人道主义援助” 邮件，打开就沦陷

攻击者的套路简单又致命：

发一封标题写着 “人道主义援助” 的钓鱼邮件

冒充乌克兰本地援助机构，语气极度逼真

诱导你点开一个 “填写资料” 的链接

为了骗到你，他们甚至用上：

AI 生成的高仿网站

利用 XSS 漏洞劫持正规网站

你以为点的是救助表单，其实是地狱之门。

二、攻击链曝光：点一下，你的电脑就成了傀儡

整个入侵流程一气呵成，全程无感知：

点开链接 → 下载压缩包

解压出快捷方式 → 触发HTA 执行链

后台下载恶意 HTA 文件 → 显示假表单

计划任务静默启动 EXE

Shellcode 注入系统进程（如 RuntimeBroker.exe）

加载双阶段木马 → 释放加密载荷

开启反向 Shell（类 RAVENSHELL） → 连接黑客服务器

9 字节 XOR 加密通信 → 完全接管你的设备

从点击到被控，不弹框、不报错、无声无息。

三、五大恶意软件齐上阵：你的隐私被扒光

UAC-0247 这次动用了一整套 “窃密全家桶”：

🦅 AGINGFLY（主力远控）

C# 编写，AES-CBC 加密通信

远程执行命令、截屏、键盘记录

不存本地代码，实时从服务器下载编译，极难查杀

🔑 CHROMELEVATOR

专门偷Chromium 内核浏览器密码、Cookie、账号凭证

💬 ZAPIXDESK

直接扒取 WhatsApp 全部聊天记录、联系人、媒体文件

🔁 SILENTLOOP

PowerShell 持久化脚本

通过 Telegram 接收 C2 指令

自动更新、备份、维持权限

重装系统都不一定能清干净

🐚 RAVENSHELL

反向 Shell，建立加密 TCP 隧道，黑客想干嘛就干嘛

四、不止窃密：还在你电脑里挖矿、横向渗透、建隧道

黑客得手后绝不收手：

用 RUSTSCAN 扫描内网，横向渗透

用 LIGOLO-NG / CHISEL 搭建隐蔽隧道，长期驻留

甚至偷偷部署 XMRIG 挖矿程序，榨干设备性能

伪造工具 “BACHU” 通过 Signal 传播，入侵国防人员

政府内网、医院系统、军方终端，全成了他们的后花园。

五、普通人 & 机构必看：3 招守住防线

CERT-UA 给出最有效的防御建议，简单但致命：

严禁随意打开 LNK、HTA、JS 等后缀文件

限制执行：mshta.exe、powershell.exe、wscript.exe

邮件里的陌生链接一律不点，尤其是涉及援助、文件、表单

结语

UAC-0247 的真实身份依然成谜，但它的目标很明确：

情报窃取 + 长期控制 + 破坏关键基础设施。

这场从诊所蔓延到政府的网络战争，再次提醒我们：

在数字时代，一次不小心的点击，就能击穿整个防线。

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblj6Qa1c5j4iaSxNtaWyMmOrsJ7WJafnTfxff3PA2nhkdQL7AyqtkzhPaoCicbu2FWhIAe1y02o5icTMZiaiaD1T4WXgf5TRsAVyEFU/640?wx_fmt=png&from=appmsg)

二、为什么加入？

职场瓶颈期找不到突破方向？安全项目落地缺成熟方案？面对APT攻击、勒索病毒不知如何构建防御体系？

三、在这里，你能获得的不只是资料包，而是直接对接行业专家的「私人顾问服务」

✅ 职业发展「精准导航」

 1v1简历优化：针对安全岗（渗透测试/安全运营/合规等）拆解JD，突出核心竞争力；

 晋升避坑指南：从工程师到安全负责人，分享晋升路径，避开「技术强但管理弱」的晋升陷阱；

 技能栈规划：根据你的基础（应届生/3年经验/资深专家）定制学习路线，比如从0到1学SOC安全建设、APT威胁狩猎。

✅ 安全方案「对症开方」

 实战方案库：含医疗/制造业/等行业的勒索防御、数据安全合规、供应链安全加固方案（附落地工具清单+成本测算）；

 架构设计咨询：小到EDR选型，大到零信任体系搭建，提供「预算效果」平衡的最优解（已帮10+企业节省40%防护成本）。

✅ 圈子资源「直接对接」

 大厂安全负责人拆解真实案例（如某支付公司攻防对抗的实战复盘）；

四、适合谁？

 想突破职业天花板的安全工程师/架构师；

 需快速落地安全项目的企业负责人；

 关注行业动态的安全爱好者或IT从业人员。

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

AI紫队安全研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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