---
title: 朝鲜黑客用AI冒充熟人，4亿美元加密货币被盗：视频会议也不可信了
url: https://mp.weixin.qq.com/s/cAsELQitttuIqlLRwQNETQ
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:37.046638
---

# 朝鲜黑客用AI冒充熟人，4亿美元加密货币被盗：视频会议也不可信了

# 朝鲜黑客用AI冒充熟人，4亿美元加密货币被盗：视频会议也不可信了

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

当你熟悉的合作伙伴出现在视频会议中，你看到的可能不是本人，而是攻击者精心制作的一场骗局。

2026年11月，美国联邦调查局（FBI）与司法部（DoJ）宣布针对朝鲜关联网络犯罪活动采取协同行动。FBI确认，朝鲜关联威胁行为者通过代号 **FaceStealer** 的社会工程攻击，在过去18个月窃取超过4亿美元加密货币。

与此同时，美国司法部宣布查封并冻结超过12亿美元加密货币资产。这些资产与朝鲜关联的TraderTraitor团伙窃取的资金有关，最终被用于资助平壤非法武器计划。

这两项行动再次揭示一个值得网络安全行业高度关注的趋势：**AI正在改变网络攻击的实施方式，攻击者不再只是伪造邮件和网站，而是开始伪造人与人之间的信任。**

## 一、FaceStealer：一场精心设计的视频会议骗局

FaceStealer背后的攻击组织被关联到长期活跃的朝鲜威胁集群BlueNoroff，也被部分安全厂商追踪为APT38、UNC1069等。

这场攻击最危险的地方，并不是恶意软件有多复杂，而是攻击者能够利用受害者的真实社交关系，构建一场看起来完全正常的视频会议。

整个攻击过程可以概括为五个步骤。

**第一步：先攻陷一个可信的人。**

攻击者通过社会工程手段获取目标人物的加密货币钱包、助记词、社交账号以及其他敏感访问权限，同时窃取其Telegram、LinkedIn等通信账号。

更重要的是，攻击者会获取受害者的联系人、聊天记录，并在视频会议中偷偷录制摄像头画面。

**第二步：利用熟人身份建立信任。**

攻击者控制受害者的Telegram账号，冒充本人向其联系人发送定制化消息，邀请对方参加Zoom或Microsoft Teams会议，讨论投资机会、业务合作等内容。

对于接收邀请的人来说，发消息的是熟悉的联系人，会议邀请也符合正常业务场景，很难第一时间产生怀疑。

**第三步：利用录制视频和深伪技术制造假会议。**

攻击者在仿冒的视频会议网站中播放此前录制的真实人物视频，并利用深伪技术生成其他参会者的虚假视频。

这些视频可以来自真实受害者，也可以利用公开的YouTube访谈、行业大会演讲等素材制作。

AI生成的人像、头像和视频进一步丰富了假会议的内容，让攻击者能够模拟多人参会的场景。

**第四步：制造技术故障，诱导受害者执行恶意代码。**

会议开始后，攻击者故意制造音频异常、视频故障等问题，声称无法听到目标说话，随后要求对方点击链接安装更新，或者复制一段命令到终端执行。

这类手法与ClickFix攻击高度相似。

所谓解决问题的方法，实际上是攻击者精心准备的恶意代码。一旦执行，便可能在受害者设备上部署信息窃取程序，获取钱包信息、浏览器凭据、SSH密钥及其他敏感数据。

**第五步：让新受害者成为下一轮攻击的入口。**

攻击成功后，攻击者继续控制受害者的设备和社交账号，利用其身份攻击新的联系人。

于是，一名受害者不仅损失资产，还可能成为攻击链中的传播节点。

## 二、AI正在让社会工程攻击发生质变

过去，社会工程攻击主要依靠邮件、短信、钓鱼网站和假冒身份。

现在，AI正在让攻击者具备三种新的能力。

**1. 让假身份越来越真实**

深伪视频、AI生成头像和语音克隆，可以帮助攻击者模拟真实人物的形象与声音。

攻击者甚至不需要提前攻陷目标本人，只需要从公开互联网收集视频、照片和音频素材，就可能制作出足以迷惑普通人的虚假会议画面。

**2. 让攻击成本越来越低**

AI可以帮助攻击者生成定制化钓鱼消息、伪造人物素材、编写恶意代码，甚至自动化整理目标人物的公开信息。

过去需要专业人员完成的部分工作，现在可以被AI辅助完成。

**3. 让攻击从技术突破转向信任突破**

FaceStealer最值得警惕的地方，是攻击者并不直接攻击陌生人，而是利用被攻陷的真实联系人建立信任。

当攻击者掌握了你的社交账号、联系人和沟通习惯，传统意义上的身份验证就可能失效。

**未来，视频会议中的人脸、声音和身份，都不能再被简单视为可信凭证。**

## 三、从FaceStealer到Axios：AI攻击正在威胁软件供应链

FaceStealer并不是孤立事件。

BlueNoroff的攻击目标高度集中于加密货币、Web3、金融投资和软件开发领域。

其攻击目的不仅是窃取加密货币，还包括获取开发者设备、代码仓库和软件供应链的访问权限。

2026年4月，热门npm包Axios维护者就曾遭遇与UNC1069相关的社会工程攻击，攻击者通过获取维护者访问权限，向软件仓库推送植入恶意代码的版本。

这意味着，一名开发者被攻陷，可能影响数以万计甚至更多的软件使用者。

攻击者的目标正在从单个终端转向开发环境、代码仓库、CI/CD流水线和软件供应链。

与此同时，朝鲜关联的Contagious Interview行动也在持续利用招聘场景攻击开发者。

攻击者冒充招聘人员，通过LinkedIn发送编程测试、代码仓库或技术测评，诱导开发者下载并运行恶意代码。

更危险的是，攻击者开始利用VS Code工作区配置、Git Hooks等开发工具机制，在项目打开或操作过程中触发恶意代码执行。

**当招聘、会议、开发和协作成为攻击入口，企业原有的安全边界正在被重新定义。**

## 四、企业应该如何应对AI驱动的社会工程攻击？

面对FaceStealer这类攻击，仅靠传统杀毒软件和邮件安全产品已经远远不够。

企业需要从身份、终端、开发环境和人员管理多个层面建立防御体系。

### 1. 视频会议不能只验证人脸和声音

涉及资金转账、钱包操作、密钥授权、代码仓库权限变更等高风险行为，应通过独立通信渠道二次确认。

例如，视频会议中提出转账要求，可以通过已验证的电话、企业内部通信渠道或既有审批流程确认。

不要因为对方能够露脸、能够说出熟悉的信息，就默认其身份真实。

### 2. 建立终端安全与行为检测能力

企业应强化终端检测与响应（EDR）、应用执行控制、脚本执行监控和异常进程行为检测。

重点关注：

* 浏览器、会议软件异常启动命令行或脚本解释器。
* PowerShell、Shell等工具执行来源不明的代码。
* 异常下载、内存加载和远程连接行为。
* 浏览器凭据、SSH密钥及加密钱包相关信息的异常访问。

尤其需要警惕ClickFix攻击：**用户自己点击、自己复制、自己执行，并不意味着行为安全。**

### 3. 开发环境必须建立隔离机制

对于招聘测评、开源项目、第三方代码和未知仓库：

* 不要直接在办公电脑上运行。
* 使用一次性虚拟机或隔离环境进行分析。
* 禁止未知项目访问真实凭据、SSH密钥和生产环境。
* 对VS Code工作区配置、tasks.json、Git Hooks等进行安全检查。
* 强化代码仓库账号的MFA、权限管理和异常登录监控。

### 4. 重新设计员工安全意识培训

传统安全意识培训经常强调不要点击陌生邮件链接。

但现在需要进一步教育员工：

不要轻易相信视频会议中的熟人，不要在会议中执行所谓的音视频修复程序，不要因为招聘人员要求就运行未知代码，也不要在AI工具中上传敏感数据。

安全意识培训必须从「识别钓鱼邮件」升级为「识别AI驱动的信任攻击」。

## 五、我的观点：AI时代，信任正在成为新的攻击面

FaceStealer这类攻击给网络安全行业带来的启示，不只是深伪技术的危险，也不只是加密货币被盗。

更重要的是，**AI正在把攻击者的社会工程能力、身份伪造能力和恶意软件投递能力整合成一条高度自动化的攻击链。**

攻击者可以利用AI伪造人物、利用真实账号建立信任、利用ClickFix诱导执行代码，再利用被攻陷的设备和身份继续传播。

从邮件钓鱼，到视频会议，再到招聘面试和软件供应链，攻击入口越来越接近正常业务活动。

未来企业安全建设需要重新审视三个问题：

第一，如何确认一个人是真实的，而不是AI生成的身份？

第二，如何确保员工即使被欺骗，也不会轻易执行恶意代码？

第三，如何阻止一台被攻陷的终端进一步危害企业核心系统和软件供应链？

这三个问题，分别对应身份安全、终端安全和企业安全运营。

**AI可以让攻击者更容易伪造信任，但企业不能因此失去验证信任的能力。**

当视频中的熟人可能是假的，招聘人员可能是假的，代码仓库可能是假的，真正可靠的安全防线，应该建立在身份验证、权限控制、终端防护和行为监测之上，而不是建立在「看起来可信」的基础之上。

这才是FaceStealer给所有网络安全从业者最值得思考的警示。

end

![](https://mmbiz.qpic.cn/mmbiz_png/zj5ibzxuvcrWv3RVy2Hd2kRCbExIoc2KiaKhy9wibOMxXx7JOSlCKbhvCiaJfO7xrtjRCIPWmH3RlO9Og5QxTOlLjg/640)

推荐阅读

[OpenAI放出安全大招：AI自己找漏洞、写补丁，但最后一步依然交给人](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494221&idx=1&sn=897f6cb684141b3e2f4249d816d62b3e&scene=21#wechat_redirect)

2026-11-15

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTPKZDaNicNGib7xb7ZBvjDMhVCByT0kOSlGPq141JmQpNjLngXibSVDX98dK17ctG9yVk5NH3dPib6yDBvEKe5wFNDEMN2dL8RgBc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494221&idx=1&sn=897f6cb684141b3e2f4249d816d62b3e&scene=21#wechat_redirect)

[重磅！某网约车平台司机信息遭泄露](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494216&idx=1&sn=36a9918068f57a9ed4a42445f30671bb&scene=21#wechat_redirect)

2026-11-14

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQXhvPEGzahYiauObLjvmMLR3UpjuiaQGO4fxHZCiaGfOLFqMMopDbEfeXaqpQJTkIibM8b6sHNwI9b9OU9m5aHxmYXddQMGOEoX64/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494216&idx=1&sn=36a9918068f57a9ed4a42445f30671bb&scene=21#wechat_redirect)

[AI Agent逆向APK分析研究：一次双模型实验与字节级复核](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494211&idx=1&sn=33c696d6b1e09ff043764cde2b096e0d&scene=21#wechat_redirect)

2026-11-12

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQrVMSFtxhibZg5VHTdDENh8FkxEKv8wIB4bjMhsIicxOXYz3V7JNFcks0icibmt2eLwhk2opnWr8jjkHibVHsUHOx2oTpZeAhQSLjk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494211&idx=1&sn=33c696d6b1e09ff043764cde2b096e0d&scene=21#wechat_redirect)

[给国外大模型当“二道贩子”，这家公司栽了：AI中转站的生意没那么好做](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494205&idx=1&sn=d1dc7e18b4468901276ddbf2eb7820da&scene=21#wechat_redirect)

2026-11-11

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSB78PX0pjILXhs4dhguic7v5p9gcO2Z8qfkTVmsibhxC6PTn1U3LzJCE2kbjCOoqqtOiahCT2jzbNBibPkGVsd4ka3w2mISPrtlCc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494205&idx=1&sn=d1dc7e18b4468901276ddbf2eb7820da&scene=21#wechat_redirect)

[新品发布｜可落地的 AISOP 安全运营数字员工](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494200&idx=1&sn=64416b5a557d434cb61807a0497cdb1b&scene=21#wechat_redirect)

2026-11-10

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibQuIj1ribQ13zdMB5fwcnJaCY71hWNArI70HVPiaTribCAA0DKbmFbK2tMbB947Wu73OX7zawS8NYbcLU5OEcJUHw6xzojPMyGhFo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247494200&idx=1&sn=64416b5a557d434cb61807a0497cdb1b&scene=21#wechat_redirect)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AiaxibnzDXa1Y7uRicSTtCequUrbj3R6CelD6j6kTdgeaBdywoCOdImg0P7WnB8zQTYveOJzTzHtSely8qFvufmiaA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过