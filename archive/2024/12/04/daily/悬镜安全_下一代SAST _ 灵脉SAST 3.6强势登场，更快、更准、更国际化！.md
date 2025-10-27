---
title: 下一代SAST | 灵脉SAST 3.6强势登场，更快、更准、更国际化！
url: https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647794869&idx=1&sn=39db0ddeb21d8003b1f51bdd9c3016e0&chksm=8770ace2b00725f43e4a6935fba88e1b7d17e2c5a3323b5cd2c188d95a2d1d6c9c0bdbad4e5f&scene=58&subscene=0#rd
source: 悬镜安全
date: 2024-12-04
fetch_date: 2025-10-06T19:39:37.297363
---

# 下一代SAST | 灵脉SAST 3.6强势登场，更快、更准、更国际化！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeU6KgY6hZ5JbVias3ZDlv1iacuncgibhBaOzMibNp0xcLPgfeRWt7pcRib2w/0?wx_fmt=jpeg)

# 下一代SAST | 灵脉SAST 3.6强势登场，更快、更准、更国际化！

原创

Xmirror

悬镜安全

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGj56PMu0icIF7jYduLbYTpshJC1x89TawLCeibYDfBNPKicmHF2ibBc98oiaKiax0bTs9Vk5mQT9wYuCLhw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeXFNOvDXD3loYEydiaDdDWeah66kVKtJjolIkVuxOGbhfTWzNBZLYy4g/640?wx_fmt=jpeg&from=appmsg)

**1**

**引擎发力
多重保障又准又快**

**01.AI强化检测精准度**

悬镜灵脉SAST 3.6版本AI模型强化了针对命令注入、文件操作漏洞、SQL注入、XPath注入、XSS跨站脚本、不安全随机值、弱加密算法、弱哈希算法、Cookie安全性问题以及信任边界破坏等缺陷类型的分析能力；同时在评估缺陷等级时，会进行跨文件、跨函数的方式综合上下文信息，提供更加精准的等级判定。

**02.两大扫描模式随心选**

灵脉SAST Java、C/C++等引擎支持快速扫描和深度扫描两大模式：

* **快速扫描****：**针对时间敏感的开发者，提供高效率、覆盖常见缺陷的轻量级检测，适合日常代码检查。

* **深度扫描****：**在更高安全性要求的场景下，使用高精度的全程序分析，追踪复杂调用链，能够检测隐蔽性强、依赖全局上下文的漏洞。

**03.source-sink一致缺陷合并**

复杂项目中一个源点（source）可能关联多个路径，这些路径最终指向相同的风险点（sink），导致检测报告中出现大量重复的结果，影响用户理解和分析的效率。

悬镜SAST通过全局分析，追踪数据来源（source）与数据终点（sink）之间的关系，对不同分支条件下数据流中多个路径进行去重和归一化处理，且支持用户友好的多路径切换展示，避免因路径重复造成的误报感知和疲劳分析。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeRPXM0z6wbtLZZ4KACZg2Y5Ja99z1qFKC4lf8NfSyhNHhtYbh7OaJiaQ/640?wx_fmt=png&from=appmsg)

**04.提升数据流分析精度**

悬镜灵脉SAST 3.6版本采用静态单赋值（SSA）技术将变量的所有定义和使用转化为唯一的静态分析路径，简化程序的控制流和数据流图（CFG和DFG），避免因变量混淆而导致误报的同时显著提升分析效率。

**05.灵活的任务配置**

Go语言支持跨平台编译和构建，代码中可能包含多个操作系统（OS）、架构（Architecture）和构建标签（Build Tags）的条件编译逻辑，使静态分析面临额外的解析复杂度。

悬镜灵脉SAST支持明确配置这些选项，可选定目标操作系统、架构、构建标签和配置代理，使引擎能够聚焦于目标环境代码，避免因条件编译引发的误报，提高检测的完整性和准确性。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIejyGNtE5D2DAHtMPgYE49IQP2oKmXbMJpAbtSkDiavj7ZFI7NgYiaR2ow/640?wx_fmt=png&from=appmsg)

**2**

**精准锁定
后门查杀护航安全**

悬镜灵脉SAST 3.6版本通过分析代码的内部结构、语法和逻辑特征深度检测隐藏的后门问题，并定位至具体代码文件及对应的代码行号，展示从入口函数（如completed()）到具体问题代码（如statement.executeQuery(query)）的调用流，使用户能够快速理解问题的来源和传播途径，并提供详细的修复建议，在代码提交阶段即时发现并修复后门问题。

***智能分析***

相比传统模式匹配或单文件静态分析，灵脉SAST通过跨文件数据流分析、全局调用关系图构建和AI智能辅助，显著增强检测后门的深度和广度。

***检测全面***

支持主流编程语言（Java、Python、C++、Go等）和常用框架的后门检测，覆盖常见业务场景，包括命令执行后门、代码注入后门、SQL注入后门、表达式注入后门、反序列化后门、反射调用后门、硬编码后门凭证等。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeU0ak9LcX7waia7avjXzYfNbRfYM5HtL3eFI78eUhO3Cc5bCsefrpUHA/640?wx_fmt=png&from=appmsg)

**3**

**再创新高**

**知识库规则9000+**

灵脉SAST持续扩展检测规则，目前知识库已支持9000+检测规则，其中：

1）Java：新增40+规则，包括Android、CWE等标准集；

2）C/C++：新增10+规则，包括通用规则集、AUTOSAR C++14等标准集；

3）Go：新增10+规则，包括通用规则集、CWE、OWASP 2021 TOP10、OWASP 2017 TOP10等标准集。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjpZZWBB57qXicXw2hrbrslEveznmNUFQGlGibUz8g5Wcm9FIwaoKEcovSPH2E2SE9NuPV2Gf9nBO9g/640?wx_fmt=jpeg&from=appmsg)

**4**

**面向全球
国际化接轨**

随着企业软件安全需求的全球化，特别是海外研发中心或外包开发团队的增加，静态应用安全测试（SAST）工具需要支持多语言环境，以适应全球化团队的沟通与协作。

悬镜灵脉SAST 3.6版本支持知识库规则英文查阅、平台中英文页面、英文生成报告内容等，可满足国内外资企业、跨国公司以及海外企业需求。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeNjRo4vrpp64YFghtdzUz5aUia9ckTMyBxsdxgicbUCQGYibcLQDNccSOw/640?wx_fmt=png&from=appmsg)

**5**

**持续优化**

**提升用户体验**

**01.快速检测/项目管理**

(1)优化任务/应用列表、分析结果页面交互，跳转查看任务更方便。

(2)优化任务word、pdf详细报告，生成速度进一步提高。

(3)缺陷审计：支持批量审计操作，审计操作更便捷。

**02.规则管理**

（1）自定义白名单：优化C/C++、Objective-C语言的方法白名单配置，支持 C++/Objective-C的命名空间配置。

（2）文件路径过滤：优化文件路径过滤规则配置方式。只需输入关键字即可进行过滤，操作更便捷。

（3）自定义规则：支持用户自定义规则以检测代码中的潜在问题由此检测出更多缺陷。新建自定义规则时，需要按照语法要求进行配置。

**03.系统管理**

优化数据备份和数据清理机制，避免长时间后影响磁盘占用情况的发生。

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeol20OZVuFVAyTLGKoAkvNhiaVPbpwn4bdcSSf8fUR3u5iczXDkDrvWuA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeol20OZVuFVAyTLGKoAkvNhiaVPbpwn4bdcSSf8fUR3u5iczXDkDrvWuA/640?wx_fmt=gif&from=appmsg)

**申请免费试用**

**灵脉SAST 3.6版本**

**↓**

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIe2iaT7e63NKaAS0R5d5y11Rn4K3Dlkr41fd9Poa4x0icMd6iaCQMKic7Afg/640?wx_fmt=png&from=appmsg)

悬镜灵脉SAST是落地实践应用安全左移的基石之一，是敏捷安全工具链中前置到安全编码阶段的重要赋能环节。悬镜敏捷安全工具链作为第三代DevSecOps数字供应链安全体系中的重要能力支撑，将不断提供更智能、更可信的创新供应链安全产品服务，持续守护中国数字供应链安全。

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeol20OZVuFVAyTLGKoAkvNhiaVPbpwn4bdcSSf8fUR3u5iczXDkDrvWuA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeol20OZVuFVAyTLGKoAkvNhiaVPbpwn4bdcSSf8fUR3u5iczXDkDrvWuA/640?wx_fmt=gif&from=appmsg)

＋

**推荐阅读**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIegaWedrOaEibYOx7AajhXntwDaDjxKRa5j7h4Vy5gKG5U1efHrrlBP1Q/640?wx_fmt=gif&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjCDMNSmfOyI6VAcOMYxkg89H6RphcoZCZGpySfTHia4qtp0j9eoSRgKpgrlsrqvAYEsVOtQPLjfng/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791074&idx=2&sn=9d81dcfdfb016ad6e6f64e3b0c8c2afc&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIesO0szQUGMFGKBVicsUMFOyicLUD47pEwU7IFzjKXF1pXHaBPvRbMsDag/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791525&idx=1&sn=53fda8c621f38d6a60214e808f654212&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGhUERhKfSDYZ3wEfkTraLst97njICLJvgLnkU8lVG4dsibSjicXbtc9uRFSapNfDjcarV26qE9g5xvg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790982&idx=1&sn=36ece411a3b20638b30a5a661ba401d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiautibEZoLYaVDIlf4VibgUIeM3Mk9NWDg9uxhGSV9v0eRzSqWHPkO4kq0gGXuiaUrUbmqjQ1j80OrKQ/640?wx_fmt=png&from=appmsg)

**关于“悬镜安全”**

悬镜安全，起源于子芽创立的北京大学网络安全技术研究团队”XMIRROR”，作为数字供应链安全和DevSecOps敏捷安全开拓者，始终专注于以“AI智能代码疫苗”技术为内核，凭借原创专利级”全流程数字供应链安全赋能平台+敏捷安全工具链+供应链安全情报预警服务”的第三代DevSecOps数字供应链安全管理体系，创新赋能金融、车联网、通信、能源、政企、智能制造和泛互联网等行业用户，构筑起适应自身业务弹性发展、面向敏捷业务交付并引领未来架构演进的共生积极防御体系，持续守护中国数字供应链安全。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjpZZWBB57qXicXw2hrbrslEFIGODrFPJUfSSicXlHtlaR2UsOGmZTsiaov0ZGlJ43TQaqhcN1Aj78cQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiaEbrH3Qvf3yLRbjBVL227eDf2sYupEV9Yfz1GSa972dXGfL4Gc5sbjaTWXnia3OnDNTgCBRIeNTEQ/0?wx_fmt=png)

悬镜安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiaEbrH3Qvf3yLRbjBVL227eDf2sYupEV9Yfz1GSa972dXGfL4Gc5sbjaTWXnia3OnDNTgCBRIeNTEQ/0?wx_fmt=png)

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