---
title: 悬镜安全正式成为首批开源风险评估与治理技术实验室软件物料清单（SBOM）工作组成员单位
url: https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791492&idx=2&sn=64593644b52f5e1fcfac5142b3400afa&chksm=87709fd3b00716c53d7df71ec8d1d4474f06778ca73f1b8b498014d011c178a78dba98227592&scene=58&subscene=0#rd
source: 悬镜安全
date: 2024-09-14
fetch_date: 2025-10-06T18:30:03.023176
---

# 悬镜安全正式成为首批开源风险评估与治理技术实验室软件物料清单（SBOM）工作组成员单位

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1OgialtQciaeVS7Fic7XwHxHP3NpjwCWYFQh1srvGnpImbCfh8gD65DEHqw/0?wx_fmt=jpeg)

# 悬镜安全正式成为首批开源风险评估与治理技术实验室软件物料清单（SBOM）工作组成员单位

原创

Xmirror

悬镜安全

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgALRzA4dxvk3TIxjvYl6iaZYTLlFC0WhuKC0ogplsM3dbjcqyicYMDyQWMsI3RiawC0PfeERBeMiaIzg/640?wx_fmt=gif)

近日，国家工业信息安全发展研究中心公布首批软件物料清单（SBOM）工作组成员单位，悬镜安全顺利通过国家工业信息安全发展研究中心持续数月的测评与审核，成功入选成为首批SBOM工作组成员单位。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1OibX1jIRUmE1UCaQ8zjq6ZKjBIIehApiaiaiaOlzqjUKvhkWnpmnribibIVjw/640?wx_fmt=jpeg&from=appmsg)

国家工业信息安全发展研究中心是工业和信息化部直属事业单位，是我国工业信息安全领域重要的服务保障机构，具有等保测评、商用密码安全性评估、信息安全风险评估、电子数据司法鉴定、软件测试等资质。此次成立SBOM工作组，并启动“筑链计划”，旨在健全提升产业链供应链韧性和安全水平制度，建立产业链供应链安全风险评估和应对机制，加强软件供应链风险治理能力建设，提升软件安全性和透明度，推动软件物料清单（SBOM）体系完善与推广应用。

SBOM作为数字供应链安全治理的基础性工具之一，悬镜安全是其国内较早的实践者和布道者。2023年，悬镜安全团队联合倪光南院士及北京大学、开源中国、电信研究院、中兴通讯等产业机构的专家学者发布中国的数字供应链SBOM格式DSDX，以企业级实战化应用实践，其目标是成为数字供应链安全治理与运营的核心技术抓手，以助力行业从软件供应链安全过渡到数字供应链安全时代。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1O4FG4HRwaRe12QUJVKd7rnKtz9qkYiaD0iaI8lGnh1JFaibo5LSzViaR14Q/640?wx_fmt=jpeg&from=appmsg)

**中国数字供应链SBOM格式DSDX**

现有的国际SBOM格式依赖于软件供应链，而如今数字供应链扩大了原有软件供应链的内涵，不仅囊括数字应用，还包括基础设施环境和供应链数据。数字供应链安全更是涵盖数字应用安全、基础设施服务安全以及供应链数据安全。基于此，国内自有SBOM格式-DSDX重点引入了运行环境信息和供应链流转信息，加强了清单间的互相引用，并实现最小集/扩展集的灵活应用，深度支持代码片段信息的存储及追踪，为企业用户提供整个数字供应链基础设施视角的落地治理实践。

**解读一**

**DSDX 组件信息**

适用于数字应用的微服务场景，多个微服务承载着不同的业务需求，每一个微服对应一个SBOM，共同组成为业务系统量身定制的的数字供应链SBOM。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1Ouic9iaOiaJjU6BKIOaOLib6eQFXGso4y8vCER8RKJpFGPeHovXSGOP1L4A/640?wx_fmt=png&from=appmsg)

由组件作为最小重复单元，结构更加简洁；

不同SBOM之间可以通过DSDX ID进行关联

**解读二**

**DSDX 代码片段信息**

提供了代码文件/片段相似度及来源信息的描述，从而辅助分析代码片段中是否引入开源组件、是否有已知的安全漏洞、对应的开源许可证、对源代码进行溯源分析等。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1OdQpG8B1NIWicslsh5fUjpU39phU5Q6jWmzaFraLq8d4iaUEiag30zH4BQ/640?wx_fmt=png&from=appmsg)

代码文件/片段相似度及来源信息描述；

可以作为外部链接被DSDX引用，节省清单篇幅

**适配中国企业实战化应用实践场景**

DSDX v1.0的核心特点包括全场景覆盖、强大的兼容性、供应链数据溯源和强大的自身安全性。针对性适配中国企业实战化应用实践场景。

1

全场景覆盖：涵盖源码、二进制、镜像等不同阶段的物料清单，对组件、漏洞、许可证风险全面覆盖；

2

强大兼容性：兼容SPDX、CycloneDX、SWID国际标准和国内标准，但不止于主流规范，在最小元素集基础上扩展其他元素；

3

供应链数据溯源：涵盖数字供应链流转信息、可追溯文件、组件，依赖的过程变化及其来源，保证SBOM的修改全程可追溯；

4

强自身安全性：物料清单本身满足机密性要求和完整性要求，具备真实性校验、防篡改等保护机制。

DSDX通过与悬镜源鉴SCA开源威胁管控平台深度联动，可全面提升企业数字供应链安全风险的发现能力、分析能力、处置能力、防护能力以及安全管理水平。

开源应用组件级资产测绘：DSDX可以生成全面兼容、安全可溯源的软件物料清单，精细化识别开源软件组件及其构成和依赖关系，输出透明化的数字应用组件资产及风险清单。

许可证合规性管理：基于DSDX记录的开源软件许可证信息，进一步实现许可证条款解读、兼容性分析等，帮助企业确保自身遵守许可证相关条款，规避潜在的知识产权等法律问题或处罚，避免后续公司业务自身权益受到损害。

提升软件质量：基于DSDX提供的组件信息，识别出过时或废弃的组件，鼓励开发团队使用最新且安全的库，从而提高整体的软件质量。

安全事件应急响应：DSDX中包含了详尽的软件组成成分，安全团队可以通过DSDX分析软件风险，并进行持续监控；在有供应链安全事件发生时，安全团队也能根据DSDX快速定位第三方组件中已知漏洞的影响范围，并针对性地对修复措施进行优先级排序，加速供应链攻击事件应急响应速度。

SCA技术是数字供应链开源治理的关键入口，DSDX为代表的SBOM格式将在整个供应链引入、生产、交付等关键环节的开源治理实践中发挥着重要作用。深度支持DSDX的源鉴SCA，针对性适配中国企业实战化应用实践场景，为供应链上下游企业用户提供安全新方案与整体建设新思路，保障数字供应链下开源资产的安全引入及安全管控，助力行业及产业从软件供应链安全向数字供应链安全过渡升级。

**END**

在悬镜看来，不断推进国产安全治理平台核心技术自主可控，是国家安全产业发展的关键基础，是实现我国数字强国建设的必由之路。此次悬镜安全成为首批SBOM工作组成员单位，将大力配合国家工业信息安全发展研究中心开展SBOM理论和技术研究、标准研制、趋势研判，支持软件供应链管理和治理体系建设。推动SBOM相关研发平台建设，开展SBOM关键技术攻关、典型应用场景研究；建立技术、产品、服务供需对接平台，打造产业生态闭环。通过举办会、展、培训等多种方式，加强政、产、学、研、用等多方沟通交流，推广研究成果和优秀产品案例，加快规模化落地推广。

＋

**推荐阅读**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1OgjzfHtnMDuvWScicUwQl4r6dR9KU6miaZLvrzhsXhu1dsU6YNbebYZsA/640?wx_fmt=gif&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1Onx3icsHaibE4G51EX7XM7OU72lHUKXHSXR0rchg8zKF9PCNDPiblBIj2Q/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791220&idx=1&sn=367ae9a7f1a43dc39e386c234cccda1a&chksm=87709e23b00717350808147e067afc9fffa7b9866655929685aeef3577585214c45468dcbed6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1OCmbC2D7Z14SSgkCz4apFicqxzugaeBNBSibZHbXiasvBNkP3MvIz8icUicA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790091&idx=1&sn=2ba130f27b2525909230264fe511135a&chksm=87709a5cb007134a75df2f64737e86097fdd32f7424911cb13438293512fc83412e1930ce058&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGjMEIicKTp2gvsZVbztQfl1OzFXqlZbGtz0FkN8YKK8fwRE7BUv6vicTQp2xvyWhibVPxGNKw1ghoj4w/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790805&idx=1&sn=92ad07ba4b4ae72f43c131b0c7269e28&chksm=87709c82b00715945bae210edda101a5872e5ca6908912d0dd39522f6a230dabf14b521dc507&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGhy7SukE0tiaicmlQQyf92GJXrzRL1BrqreWA4RdeicBXeZ73dQe7GsDquXUEIVxyDVxmE2IF15msh0A/640?wx_fmt=png&from=appmsg)

**关于“悬镜安全”**

悬镜安全，起源于子芽创立的北京大学网络安全技术研究团队“XMIRROR”，作为数字供应链安全和DevSecOps敏捷安全开拓者，始终专注于以“代码疫苗”技术为内核，凭借原创专利级“全流程数字供应链安全赋能平台+敏捷安全工具链+供应链安全情报预警服务”的第三代DevSecOps数字供应链安全管理体系，创新赋能金融、车联网、通信、能源、政企、智能制造和泛互联网等行业用户，构筑起适应自身业务弹性发展、面向敏捷业务交付并引领未来架构演进的共生积极防御体系，持续守护中国数字供应链安全。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgbc11SUokwoUiacpXOWwicJCC2iaPL17Bia4raDLC9kyMgGPBcaicxnw4QbhZ8nyrstrsIbPTicmo0BRwQ/640?wx_fmt=png&from=appmsg)

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