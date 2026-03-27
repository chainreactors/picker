---
title: 又一个开发工具沦陷，Apifox遭供应链投毒攻击
url: https://mp.weixin.qq.com/s/Gd9ax4BebeTy8TXOwQii3A
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:30:24.291360
---

# 又一个开发工具沦陷，Apifox遭供应链投毒攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOq9NK29LX2CCz4ibP0V6atGt4yP8ODUo1Y9FVFqiaakEDRS5gTSXzJUgqO4F1bcGibyK0m5v4fUlPNA7jk3GjYcxTe2RRp0ro7Xamw/0?wx_fmt=jpeg)

# 又一个开发工具沦陷，Apifox遭供应链投毒攻击

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器中沉浸阅读

概述

Apifox是被广大开发者用于API开发、测试、联调的一款工具，它集API文档管理、API调试、API数据Mock、API自动化测试于一体。其桌面客户端基于Electron框架开发，支持Windows/macOS/Linux三端。近期，Apifox遭遇供应链投毒攻击，攻击者篡改了Apifox官方CDN上的动态JS文件，在大量开发者电脑上植入隐蔽后门，最终可实现凭证窃取和远程命令执行等恶意功能。此次攻击影响公网SaaS版桌面客户端（Electron 框架），Web版和私有化部署版不受影响。

事件时间线

（1）2026年3月4日，恶意代码开始出现在官方CDN上托管的JS文件中。

（2）3月22日左右，攻击者使用的C2恶意域名（apifox.it[.]com）C2域名下线，存活18天。

（3）3月25日，多名安全研究人员发布此次攻击事件的技术分析[1, 2]，当天Apifox发布正式安全公告[3]。

攻击分析

官方CDN上被篡改的JS文件为"hxxps://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js"，原有代码是Apifox用于事件追踪的SDK，在Apifox启动过程中加载，正常大小为34KB。但在3月4日之后请求到的文件体积膨胀至77KB，其中添加了恶意代码，使得投毒后的JS文件动态加载"hxxps://apifox[.]it[.]com/public/apifox-event.js"。

其中apifox[.]it[.]com为攻击者模仿官方域名使用的恶意域名。由于Apifox桌面客户端基于Electron开发，未严格启用sandbox参数，且暴露了Node.js API（fs、child\_process、os、crypto等），导致渲染进程可直接访问本地文件系统和执行系统命令。

**恶意代码**

投毒后的JS文件结构前面一部分为经过Webpack打包的合法事件追踪代码，然后增加了约40KB的恶意载荷。加入的恶意代码经过大量混淆，使用包括字符串数组与洗牌（shuffling）、RC4、代理函数、十六进制常量等在内的常用混淆手段，此外若对代码做过度格式化，运行时可能触发反分析逻辑[4]。

**攻击过程**

**（1）初始触发**

客户端启动时动态加载被投毒的apifox-app-event-tracking.min.js。首先采集设备信息，包括MAC地址、CPU、主机名、用户名、OS版本等。若有Apifox accessToken，调用官方API "https://api.apifox.com/api/v1/user"窃取使用者的邮箱/姓名。窃取的信息加密后作为HTTP请求中的自定义请求头发送给C2服务器。

**（2）获取后续载荷**

向C2服务器apifox[.]it[.]com发送GET请求，获取"/public/apifox-event.js"。服务器需要客户端携带齐全上一阶段存放收集信息的自定义请求头，才会返回响应。响应内容经过内置密钥解密后调用eval()函数执行。

执行的代码通过script标签引入下一阶段的后续代码（比如<script src="hxxps://apifox[.]it[.]com/02ab429d.js">），后续代码加载完成后立即从DOM中移除该script节点，从而减少攻击痕迹。

**（3）数据窃取与远程执行**

Script标签引入的恶意代码具有针对多平台窃密的功能。针macOS和Linux系统，递归读取~/.ssh/（私钥、config、known\_hosts等）、~/.zsh\_history、~/.bash\_history、~/.git-credentials，并通过ps aux命令获取进程信息。针对Windows系统，读取%USERPROFILE%\.ssh\目录，并通过tasklist命令获取进程信息。收集的信息加密后通过POST请求发往"hxxps://apifox[.]it[.]com/event/0/log"。

其他研究者发现还有的窃密载荷会读取~/.zshrc、~/.npmrc、~/.kube/\*、~/.subversion/\*、主目录/桌面/文档等，发往C2服务器另一个端点"/event/2/log"[2]。

这说明攻击者可以根据受害者环境定制不同的后续攻击策略，并且通过C2服务器可以下发任意JS载荷，实现远程命令执行、持久化、横向移动等操作，甚至利用窃取的Git/npm/K8s等各类凭证进行二次供应链投毒。

影响范围与风险

此次攻击事件受影响用户为2026年3月4日～3月22日期间使用Apifox公网SaaS版桌面客户端（版本低于2.8.19）的用户，Windows/macOS/Linux三个平台均受影响。

恶意代码窃密目标涉及SSH私钥、Git凭证、云Access Key、K8s Token等重要敏感信息，可能造成企业高价值资产泄露，引发代码仓库劫持、生产环境入侵甚至二次供应链攻击。

防护与处置措施

**官方修复措施**

Appfix官方已发布2.8.19修复版本，在该版本及后续更新中，彻底废除在线动态加载，改为本地内置打包。官方内部已重置所有服务器相关的安全凭证。

**用户处置建议**

（1）尽快将Apifox客户端升级至2.8.19或更高版本。

（2）如果在3月4号之后使用过受影响版本，全面排查并重置在设备里的存储过的敏感凭证（包括但不限于Git密钥、鉴权密钥、数据库密码、云服务Access Key及环境变量等）。

（3）在网络层面封禁apifox.it.com及其所有子域名。

总结

在此次攻击事件中，攻击者利用Apifox桌面客户端Electron框架未开启沙盒参数和动态加载机制这些特点，篡改官方CDN上托管的JS文件，植入高隐蔽性后门，在十余天时间中实施了影响大量用户的窃密行动。近期针对开发者使用工具的供应链攻击事件屡次发生，表明开发者工具已成为高价值攻击面。如今任何一款被广泛使用的研发工具都必须密切关注自身安全性，将“零信任”理念贯穿产品设计与运维始终，方能减少此类攻击事件造成的影响。

IOC

**C&C**

apifox.it.com

**URL**

hxxps://apifox[.]it[.]com/public/apifox-event.js

hxxps://apifox[.]it[.]com/<随机字符串>.js

hxxps://apifox[.]it[.]com/event/0/log

hxxps://apifox[.]it[.]com/event/2/log

参考链接

[1].https://2libra.com/post/network-security/8HvXoR\_

[2].https://rce.moe/2026/03/25/apifox-supply-chain-attack-analysis/

[3].https://docs.apifox.com/8392582m0

[4].https://www.leavesongs.com/PENETRATION/apifox-supply-chain-attack-analysis.html

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9MwcASpslaIh8PnHo0JfwshiadSVsClrmdXKpyuliav4miaaLvcIIm4Xz3tPoLlYWWWQwgsDeLYye7RJiaIzzCMvrnRQkrKcdkbIs/640?wx_fmt=gif&from=appmsg)

点击阅读原文至**ALPHA 9.1**

即刻助力威胁研判

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

奇安信威胁情报中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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