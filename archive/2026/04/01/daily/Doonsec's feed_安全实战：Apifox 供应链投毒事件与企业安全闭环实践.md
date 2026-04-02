---
title: 安全实战：Apifox 供应链投毒事件与企业安全闭环实践
url: https://mp.weixin.qq.com/s/4Yx2Mk2kCk6am3S4vmFHKw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:15.761141
---

# 安全实战：Apifox 供应链投毒事件与企业安全闭环实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Zjic54DsBHbGGJKoEV76rfZbVRs85roHfB44djeia9D7NIg6ibMWiaAAYAqGRadzjSx4v6BLCniaVibzDp0s68xzYibsiccnibFWS0IZgynpricMibpdU4/0?wx_fmt=jpeg)

# 安全实战：Apifox 供应链投毒事件与企业安全闭环实践

原创

山石网科
山石网科

山石网科新视界

![]()

在小说阅读器中沉浸阅读

# ![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/NGIAw2Z6vnLzibrp7C4HmazCNIQXMJIRxvbibNMMmxDGrTN0Z9ibYzXnSNKobTzADCPgdo1b7ukKNARFEicHqQiajWw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=m8vage54&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8Jb8ZACqDjPdMzgicp2SzdZ19mFnVcBO53s1uA2cSfarQkwibVUeCeH9w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=kzx4ched&tp=webp#imgIndex=1)

Apifox 供应链投毒事件与企业安全闭环实践

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NGIAw2Z6vnLKuKAwMiaYedpTAYugKibaTBsHzf5pDuztECgfIgOfpG5DRF31jzhosMEj23dlx186q0zgLaIZj9lA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=2c2qx2ig&tp=webp#imgIndex=2)

#

2026年3月25日，Apifox官方发布紧急漏洞预警，确认其公网SaaS版桌面客户端遭受供应链攻击，恶意代码通过CDN广泛分发，潜伏时间长达18天（3月4日-3月22日）。攻击者篡改外部JS文件，窃取开发者SSH密钥、Git令牌、K8s凭证等敏感信息，发送至仿冒域名apifox.it.com，对企业代码安全与数据资产构成严重威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zjic54DsBHbEaRxJNWVJVHSRpouVpAunPLaibiaB1fzhw6wDicRh08dskPtrWMWoSRibZ79529tQmc99RryrkvzRZhW8SGIL7Lavs9RmiaPUoNMBk/640?wx_fmt=png&from=appmsg)

在此次席卷全网的Apifox供应链投毒事件中，山石网科依托山石智铠（EDR）等安全产品与服务，帮助某企业完成威胁定位、快速处置、全面通知的全流程安全闭环，牢牢守护企业安全。

在接到Apifox官方紧急漏洞预警后，山石网科安全服务团队第一时间启动应急响应机制，迅速提取核心IOC：仿冒官方域名的恶意地址apifox.it.com。依托山石智铠EDR强大的终端日志回溯能力，对该企业近期全量终端日志进行精准检索，筛选出针对该恶意域名的DNS查询行为，发现大量访问记录，涉及多台运行Apifox客户端的终端设备，为后续精准处置提供了坚实的数据支撑。

![](https://mmbiz.qpic.cn/mmbiz_png/Zjic54DsBHbHnOfIMMdmWaHfG553zP6UvKsWYiaRtv2WXRMq1gDjKcLkTibL4PkVt038U05ic3ibXFjExNAJsX7ib045BGVEoRCQJiaDHPkJgsDzX8/640?wx_fmt=png&from=appmsg)

在确认受影响终端后，山石网科安全服务团队依托山石智铠EDR与应急响应流程，快速启动多层级阻断措施：一方面联动边界防火墙创建黑名单，精准拦截恶意域名apifox.it.com；另一方面在山石智铠主机防火墙模块中，新增"apifox投毒事件恶意IP出站阻断策略”，对关联恶意IP地址实施流量封禁，从终端层面切断数据外发路径，实现网络边界与终端本地的双重防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zjic54DsBHbGBn7E7ghEpa3B7ExEbvyxbEYsXlia4HlRMA6xpD0a5bCZ8P30CRVPpqjDIicw71aaPol5xQmicgh2ZymJafFZUZ4hKPcQBJfeZuU/640?wx_fmt=png&from=appmsg)

与此同时，山石网科安全服务团队第一时间为企业搭建“apifox投毒事件处置”专项工作群，向企业安全负责人及相关终端负责人同步智铠EDR排查出的终端访问记录，同步推送包含客户端升级、敏感凭证轮换等步骤的标准化处置指南，明确要求风险时段内使用过Apifox客户端的员工全面排查，确保每一位相关员工都能快速响应、规范处置，将风险遏制在萌芽状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zjic54DsBHbHHDMNJ16I4uAe3jh3JffhIH4WkcmL2jcN0J1jWricMIVw29OpNBJiauMo7Yx4rREWoiar4rwnqNPvEzuxQBd4oFHJZicmy9hX21X8/640?wx_fmt=png&from=appmsg)

在完成终端定位、多层阻断与专项群协同处置后，山石网科安全服务团队结合完整投毒事件技术分析与山石智铠EDR的终端排查数据，协助企业安全负责人面向全公司发布安全预警全员邮件，要求所有风险时段内使用过Apifox的员工全面排查整改，将安全要求覆盖至每一位员工，完成从技术处置到全员意识提升的完整安全闭环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Zjic54DsBHbHcVW0GqTunyCJEerBKT0cGHtxsnqVV4DwLbJuOeTJf2t9bgVX4wuR7W34rXggTIZy3eB0mWOnvMCMD9f0GRibY70jnymRdJS44/640?wx_fmt=png&from=appmsg)

此次Apifox供应链投毒事件，正是当下企业数字化转型中供应链安全风险的典型缩影—随着Agent（Skills）等工具在业务场景中的广泛应用，供应链攻击面正被进一步放大，无形中为攻击者打开了更多隐秘入口，让“信任链”的脆弱性暴露无遗。

山石网科的实战处置，恰恰印证了“人-技术-流程”三位一体的安全运营防护体系，正是应对这类新型复杂威胁的核心答案：

1. 专业安全运营团队是抵御突发威胁的“指挥中枢”

2. 山石智铠EDR/防火墙等产品是安全防护的技术底座

3. 完善的制度流程是安全动作执行落地的保障

山石网科将以“可持续安全运营”为理念锚点，深度融合自身多年企业安全服务实战经验，通过山石智铠EDR、下一代防火墙、OpenXDR平台等核心产品与安全服务的深度协同，为企业打造“预防-防御-检测-响应”的全链路安全闭环。让每一次供应链交互都可管、可控、可信任，为企业数字化转型筑牢最坚实的安全屏障。

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnIYnBoVjHn0mWO3pro1TfcNW1g9SygLH6FI0c8mzWjXzibo9E0zM28pwRHFqwdHGwa2KbdicjgWdTtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=852hkcz1&tp=webp#imgIndex=6)

* [实力加冕！山石网科入围数说安全 “防火墙销量明星”，硬核防护筑牢数字安全防线](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661305973&idx=1&sn=50bbbb6a591504ba7d4eefbe5262d610&scene=21#wechat_redirect)
* [不做被动响应！山石网科以边界防线直击 OpenClaw 小龙虾核心风险](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661305945&idx=1&sn=c00ab1d97cec9c7d9a6f0e7b4f4da87f&scene=21#wechat_redirect)
* [山石安全能力中心｜警惕OpenClaw Skill注入风险](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661305922&idx=1&sn=b1a17183e623ff6b6b62d2ff52109f09&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8KrXv9sZf93yt4huq2kARyZSgmdnic40GayohIYiaD2FAkkAqJehJSMtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=7oqdpqlb&tp=webp#imgIndex=7)

山石网科是中国网络安全行业的技术创新领导厂商，由一批知名网络安全技术骨干于2007年创立，并以首批网络安全企业的身份，于2019年9月登陆科创板（股票简称：山石网科，股票代码：688030）。

现阶段，山石网科掌握30项自主研发核心技术，申请560多项国内外专利。山石网科于2019年起，积极布局信创领域，致力于推动国内信息技术创新，并于2021年正式启动安全芯片战略。2023年进行自研ASIC安全芯片的技术研发，旨在通过自主创新，为用户提供更高效、更安全的网络安全保障。目前，山石网科已形成了具备“全息、量化、智能、协同”四大技术特点的涉及基础设施安全、云安全、数据安全、应用安全、安全运营、工业互联网安全、信息技术应用创新、AI安全、安全服务、安全教育等10大类产品及服务，50余个行业和场景的完整解决方案。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/NGIAw2Z6vnLzibrp7C4HmazCNIQXMJIRxPibycdiaNQCI4PNojUk3eYCQDZs6c5zNMUkq7yFNeYQIxicAV33eHNdFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=2m7uy0lj&tp=webp#imgIndex=8)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/NGIAw2Z6vnLeYk6PLMhT83A1E2qOZnzFHtZIZ3HOIvib2kbe7Itgt7OO2PT1E97ZXn9X3ic7A1RwVriacwT1hUFGA/0?wx_fmt=png)

山石网科新视界

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/NGIAw2Z6vnLeYk6PLMhT83A1E2qOZnzFHtZIZ3HOIvib2kbe7Itgt7OO2PT1E97ZXn9X3ic7A1RwVriacwT1hUFGA/0?wx_fmt=png)

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