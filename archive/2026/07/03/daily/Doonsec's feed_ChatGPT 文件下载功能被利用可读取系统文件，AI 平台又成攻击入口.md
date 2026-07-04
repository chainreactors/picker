---
title: ChatGPT 文件下载功能被利用可读取系统文件，AI 平台又成攻击入口
url: https://mp.weixin.qq.com/s/l-s-ini63NdySEs5D2IG_Q
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:48:08.480588
---

# ChatGPT 文件下载功能被利用可读取系统文件，AI 平台又成攻击入口

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AyvgaRYHWDYBWkia1HVkMeP6ySDcO5BxXr5WHVCFfesYvHYoQLA13OOQjwwmgCmsdKplgkeUywFvJFVFPJsj6pBQ3ib4LibYbZ1CBBF2zibWtng/0?wx_fmt=jpeg)

# ChatGPT 文件下载功能被利用可读取系统文件，AI 平台又成攻击入口

汇能云安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AyvgaRYHWDaIpaaOAPZKYcckOqZ7edCiaQjSBXlnqaVIZqicOsTBrEuf4MsUZPnxGtKo44dV5ibKPjYV3kKqAL0cPyOYepXUPyVgPu6Ycxa2o8/640?wx_fmt=jpeg&from=appmsg)

**7****月****3****日，星期五****，您好！中科汇能与您分享信息安全快讯：**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AyvgaRYHWDbOnQS5ram3Yp5Wm9yxvicBsxjrb4FsrVCcs3DBp8NXVDIJhDjH3fNgE0dXwMRIQXCOIAAnqpHH0IgaPpWHqykMjo5WQNysCibPA/640?wx_fmt=gif&from=appmsg)

**01**

**Anthropic Claude Cowork 沙箱被攻破，AI 编程工具的安全神话碎了一地**

Anthropic 的 Claude Cowork 是很多开发者用的 AI 编程助手，主打一个 "沙箱隔离、安全无忧"。**但安全研究人员发现了一条漏洞链，攻击者只要在本地有代码执行权限，就能直接提权到 root，把 Anthropic 精心搭建的安全防护层全部绕过**，说白了，这个沙箱就是个筛子。这事儿给所有用 AI 编程工具的企业敲了警钟 —— 你以为代码跑在隔离环境里就安全了？攻击者可能已经在沙箱里开派对了。建议企业重新评估 AI 工具的安全边界，不要盲目信任厂商宣传的 "隔离安全"，该有的权限管控和审计一个都不能少。

**02**

**美国国土安全部信息共享网络被黑客攻破，政府关键基础设施安全再亮红灯**

美国国土安全部（DHS）正式确认其国土安全信息网络（HSIN）遭到黑客入侵。HSIN 是联邦、州、地方、国际及私营部门之间协调应急响应和共享威胁情报的核心平台，相当于美国国土安全体系的 "神经中枢"，这个平台被攻破意味着攻击者可能已经获取了大量敏感的威胁情报和应急响应信息。联想到近年来美国政府系统频繁被入侵（OPM、SolarWinds、Colonial Pipeline），这次事件再次说明，政府关键信息基础设施的安全防护远没有想象中那么牢固。对国内政企单位来说，这也是个提醒：信息共享平台的安全等级必须与其承载的数据敏感度相匹配。

**03**

**CitrixBleed 漏洞公开不到 24 小时就被利用，打补丁的速度永远追不上攻击者的速度**

Citrix NetScaler 设备刚披露了一个 CitrixBleed 级别的漏洞，结果不到 24 小时攻击者就开始在野利用了，这个漏洞可以导致会话劫持和凭据泄露，对于使用 NetScaler 作为入口网关的企业来说影响巨大。还记得 2023 年的 CitrixBleed 吗？那个漏洞被勒索团伙利用搞了无数企业，这次又来了。**现在攻击者的漏洞利用速度越来越快，从漏洞公开到武器化的时间窗口已经压缩到小时级别。企业不能再按 "月" 为单位打补丁了，关键设备的漏洞响应必须以 "天" 甚至 "小时" 为单位。**建议所有使用 Citrix NetScaler 的企业立即检查版本并应用安全更新。

**04**

**ChatGPT 文件下载功能被利用可读取系统文件，AI 平台又成攻击入口**

安全研究人员发现了一个 ChatGPT 的漏洞链，通过绕过安全防护加上路径遍历漏洞，攻击者可能通过平台的文件下载机制访问系统文件（比如 /etc/passwd）。虽然这需要一定的技术门槛，但说明 AI 平台正在成为新的攻击面。越来越多的企业把敏感数据喂给 AI 平台处理，如果平台自身存在安全漏洞，这些数据就面临泄露风险。建议企业在使用 AI 平台处理文件时，不要上传包含敏感信息的文件，同时关注平台的安全更新公告。

**05**

**900 多个 Oracle E-Business 实例暴露在互联网上，攻击者已在积极利用漏洞**

超过 900 个 Oracle E-Business Suite 实例直接暴露在互联网上，而且攻击者已经在积极利用其中的漏洞。**Oracle EBS 是很多大型企业的核心 ERP 系统，里面存着财务、供应链、HR 等关键业务数据，**这些暴露在公网的实例就像把保险柜的钥匙挂在门口一样。企业应该立即检查自己的 Oracle EBS 是否暴露在互联网上，如果是，立即限制访问并应用安全补丁。核心业务系统绝不应该直接暴露在公网，必须通过 VPN 或零信任架构访问。

**06**

**假冒 VLC 播放器投递 ValleyRAT 远控木马，HR 主题钓鱼邮件成重灾区**

攻击者通过伪装成 VLC 播放器的恶意可执行文件和恶意 libvlc.dll 来部署 ValleyRAT 远控木马。**攻击链伪装成 HR 主题的钓鱼邮件，一旦受害者运行假 VLC，恶意代码就会在内存中运行后门程序，让攻击者完全控制受害电脑，这种 "假软件 + 内存马" 的攻击方式很隐蔽，传统杀毒软件很难检测。**建议企业加强对员工的安全意识培训，特别是 HR 部门，不要随意下载和运行来路不明的软件。同时部署 EDR 等终端检测工具，对内存中的异常行为进行监控。

**07**

**AsyncRAT 利用 DLL 劫持和合法远程工具潜伏，90 多个仿冒软件网站成传播渠道**

AsyncRAT 恶意软件的新攻击活动被曝光，攻击者在 90 多个仿冒软件网站上放置伪装成正常安装包的恶意程序，利用 DLL 劫持技术和合法的 ScreenConnect 远程控制工具实现隐蔽访问。受害者以为自己在下载正版软件，实际上安装的是远程控制木马，这种攻击方式的高明之处在于它利用了合法的远程控制工具，可以绕过很多安全检测。建议用户只从官方网站或可信的应用商店下载软件，企业应限制未经授权的远程控制工具的使用。

**08**

**微软 365 钓鱼新招：OAuth 设备代码流窃取会话令牌，MFA 形同虚设**

一种名为 ARToken 的新型钓鱼工具被发现，它利用微软的 OAuth 设备代码登录流程来窃取 Microsoft 365 的会话令牌。攻击者不需要破解密码或多因素认证，直接偷走已经认证过的会话令牌就能访问受害者的邮件、SharePoint 和 OneDrive 文件。这种攻击方式直接绕过了 MFA（多因素认证），因为攻击者拿到的是已经通过认证的令牌。建议企业启用条件访问策略，限制设备代码流的使用场景，并部署异常登录检测机制。

**09**

**Ousaban 银行木马瞄准伊比利亚半岛用户，伪造税务 PDF 成诱饵**

针对西班牙和葡萄牙银行用户的 Ousaban 恶意软件攻击活动被曝光，攻击者通过伪造的损坏 PDF 文件和税务门户网站来诱骗 Windows 用户。一旦受害者打开恶意 PDF 并运行下载器，银行会话就会被劫持。虽然这次攻击主要针对欧洲用户，但这种 "伪造税务文件" 的攻击手法在国内也很常见。每年报税季都是钓鱼攻击的高峰期，企业和个人都要警惕来路不明的税务相关邮件和文件。

**10**

**2026 年网络安全趋势：AI 发现漏洞的速度越来越快，但安全并没有变得更简单**

Verizon《2026 年数据泄露调查报告》揭示了一个令人不安的趋势：AI 驱动的攻击系统能在数分钟内发现过度授权的负载、映射身份关联，并计算出通往关键资产的最短路径。AI 确实让漏洞发现变得更高效了，但讽刺的是，攻击者也在用同样的技术。安全攻防的天平并没有因为 AI 而向防御方倾斜，反而可能更加失衡。对企业来说，不能指望 AI 自动解决所有安全问题，基础安全建设（最小权限、零信任、及时打补丁、安全意识培训）仍然是最重要的。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/AyvgaRYHWDbMpMujRwtkeua6eFl2Qt6HrzGQbcnhF9rkHnNvWO7EQicANYa0EnnEtGsPM8VxEbeS0rob6zyG0aeibsVwdG8VyZp9AI1V6R8UA/640?wx_fmt=gif&from=appmsg)

信息来源：人民网 国家计算机网络应急技术处理协调中心 国家信息安全漏洞库 今日头条 360威胁情报中心 中科汇能GT攻防实验室 安全牛 E安全 安全客 NOSEC安全讯息平台 火绒安全 亚信安全 奇安信威胁情报中心 MACFEESy mantec白帽汇安全研究院 安全帮  卡巴斯基 安全内参 安全学习那些事 安全圈 黑客新闻 蚁景网安实验室 IT之家IT资讯 黑客新闻国外 天际友盟

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AyvgaRYHWDYCMY3F4yRwHfENRyOBogFCiaC1Ltuib2VdYkibAXk5duSy0OxYQ9mPvQ9hv7aLpaDUaLH3l2NUhjYsQN8TheUFEEMJbpSJGCc8DA/640?wx_fmt=png&from=appmsg)

本文版权归原作者所有，如有侵权请联系我们及时删除

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NSXvotEG4JxfVX9phMzJeKxa6TJkRkiad551HzMtpQVE1WJGiaB2n35mb3ponQiblLvDVPs7yb9iaq1ulcBl8ibpveg/0?wx_fmt=png)

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