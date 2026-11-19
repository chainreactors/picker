---
title: 【安全圈】50个品牌被冒名：开发者自己粘了木马命令
url: https://mp.weixin.qq.com/s/EobscwNErPdKRCO3IROGDw
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:10.972632
---

# 【安全圈】50个品牌被冒名：开发者自己粘了木马命令

# 【安全圈】50个品牌被冒名：开发者自己粘了木马命令

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

木马

**核心事实**：法国 Stormshield 的威胁情报团队公开了一条代号 **Trigram** 的流水线。它冒充约 **50 个**区块链与 AI 品牌，用招聘、会议邀请、包裹通知三种剧本钓鱼，最终一步是让受害者**自己把恶意命令粘进终端执行**。目标集中在欧洲与美国的 AI、区块链、物流三个行业。

这套东西不是「钓鱼邮件 + 附件」的老剧本。它把社工、假招聘站、终端命令、软件供应链、投毒仓库拧成一条链，而且背后有一套完整的后台在跑：管理平台、受害者追踪控制台、邮件投递基础设施。Stormshield 说，这是他们所见首个被公开描述的此类行动运营工具链。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGcicnawVW8a3MiaPd5PbxoDibcgpp0WxzfokBdA33ZJZtKeDhlzCYgibgz0vMhZjlVC2dL43FWhZ8jmefM2wJEZkL7WxPqYugiaDFc/640?wx_fmt=other&from=appmsg)

## 📧 从一封 offer 到一条命令

第一步是邮件，署名招聘方，职位是全远程软件开发，年薪写得足够诱人。邮件里带一个链接，指向「招聘平台」；同时还给一个推荐码，注册时要填。

那个站点做得很正：公司介绍、岗位职责、薪资，一样不缺。表单要你填姓名、邮箱、求职方向、作品集链接、个人陈述。提交后进「人机验证」。问题就出在这一步——页面让你复制一段命令，粘到终端里跑一下，说是完成校验。

这里有个细节值得记一下：第一轮那命令是干净的，跑完只是把页面上的 nonce 用 HTTP POST 回传，然后页面报「操作超时，请重试」。等你重试第二次，**复制按钮的行为已经被换掉了**——粘到剪贴板里的是攻击者构造的命令。用 Ctrl+C 手动复制，结果一样。这一步设计的目的很清楚：先让你相信「这东西没问题」，第二次才动手。

## 💻 三行一组的落地命令

实际执行的命令按系统分三支：Windows 拉起 PowerShell 下载运行 `v.cmd`；Linux 用 bash 下载运行 `u`；macOS 用 bash 下载运行 `verify_m`。这三个都是加载器，接下来统一去远端拉 `install_guard.js`。

这个阶段做的事有点意思：解出 Base64 脚本，设置工作目录，加一把锁防止并发安装，然后检查本机 Node.js 版本。低于 18 或者根本没有，就按系统与架构下载装一个 **Node.js 20.18.1**。装完再下 `install_guard.js`，落地窃密模块。

为了跑一个窃密脚本先给你装个 Node，逻辑上很怪，工程上很实用——它绕开了「这台机器有没有运行时」的不确定性，也顺便让后续载荷都能用 JS 写。窃取目标列得很齐：系统信息、浏览器凭据、加密货币钱包、本地敏感文件。macOS 与 Linux 上还会弹一个假对话框，让你输入系统密码「应用系统更新并验证驱动与安全设置」。

## 🎯 后台在给受害者打分

Stormshield 挖到一套叫 `rms-platform` 的后台，挂在 `170.205.30[.]27:8000`。它记录访客每一步动作，同时盯着爬虫和已被下架的仿冒域名。每个「真实访客」会被打上 important / moderate / useless 三档标签，等于在筛人。

API 路由暴露的能力更直接：抓 GitHub 资料找目标、发钓鱼邮件、管诱饵、发访问码、查看并导出已收集数据、监控钱包。追踪控制台和诱饵页面共用同一份 JavaScript，靠 hostname 或 URL 路径决定给你看哪个界面——所以它跑在你打开的每一个仿冒站上。

访问码那一段也露了底：码被拒时页面回的消息是「已被使用」「已锁定到其他 IP」「无效码」三种。这不是面向大众的钓鱼，是**预先筛过名单的点杀**。页面还会读 `cn_ip_restricted` 这个 cookie，按 IP 地理位置把特定区域挡在外面。

## 🔍 三条线汇到同一个基础设施

除了假招聘站，还有两条独立路径指向同一套东西。

一条是供应链。2026 年 10 月 31 日，`antd-img-crop` 仓库被推入伪造提交，通过 `prebuild.js` 钩子生效——开发者只要跑一次 `npm run build` 就中招。npm 包本身没被污染，中招的是仓库。载荷装完假 Node 安装器后拉一段加密 JS，全程在内存里跑，C2 地址靠 GitLab dead drop 取。

另一条是 IDE 扩展。一个名叫 `google-dev-tools.google-update-support` 的 VS Code / Cursor 扩展被侧载进来，多半是在「编码测试」环节诱导安装，跑完即删。

归属判断靠的是硬指标，不是猜：后台超级管理员账号 `eros1030109@gmail[.]com` 与 Genians 记录的 Kimsuky「Operation GitPower」重合；MongoDB 用户名 `silviattech1129_db_user` 同时出现在 antd-img-crop 劫持案用的 GitLab dead drop 历史里；`asteara[.]org` 曾被 Proofpoint 标为 UNK\_DeadDrop 的关联基础设施。Stormshield 给的结论是「高置信度」，指向朝鲜相关集群。

## 🛡️ 对开发者真正有用的是那条规矩

这条链最狠的地方在于它不需要 0day，也不需要你的系统有洞。它要的是你在求职焦虑里把一段看不懂的命令粘进终端。**任何招聘流程都不该要求你执行 shell 命令**，人机验证也不需要。真要做线上编码测试，给个沙箱链接就够了。

* **别信复制按钮**

  ：粘进终端前先粘到文本编辑器看一眼原文。第二次「重试」尤其危险，按钮行为可以被页面改写。
* **查仓库钩子**

  ：`package.json` 里的 preinstall / prebuild / postinstall 脚本要么删要么审，别让 build 顺手拉起网络下载。
* **扩展来源**

  ：VS Code 与 Cursor 只装商店里的、有真实发布者的扩展。测试环节让你侧载 vsix，先问一句为什么。
* **钱包与密钥隔离**

  ：开发机不放开钱包助记词、SSH 私钥、`.env`。这条链的目标清单里，这三样都在。

## 📌 处置进展

Stormshield 在分析过程中观测到一次 C2 轮换，说明这套基础设施仍在运营。SafeDep 与 Genians 分别就 antd-img-crop 与 GitPower 发过独立分析，UNK\_DeadDrop 一条线由 Proofpoint 自 2026 年 4 月起跟踪。截至发稿，假冒域名仍在被陆续下架，后台未见关停公告。

***END***

阅读推荐

[【安全圈】178个站点被投毒：官方CDN送出了盗卡脚本](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=1&sn=30b6dbda996787a2462c7afcd183f474&scene=21#wechat_redirect)

[【安全圈】运维工具长出蠕虫：SCKit跳到技术员电脑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=2&sn=a83acfe4ccc4a76cfdbf3a930ca47aca&scene=21#wechat_redirect)

[【安全圈】一次补掉17个洞：遗留API开关被彻底删除](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=3&sn=cbb961e616211be500f55d885d1a8cac&scene=21#wechat_redirect)

[【安全圈】无印良品明文存卡号：109万张信用卡多留了五年](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079900&idx=1&sn=07e67415a5bb07511d553704768da1d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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