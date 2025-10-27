---
title: 源鉴SCA4.7 | 国内首创全链路可达性分析，新一代SCA能力天花板！
url: https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647792084&idx=1&sn=422b19164775e700446f52986aeba7c1&chksm=87709183b0071895958c25ac47b2f7e68e9ad23c65ee5239c532d132acb052ac00adb50ea933&scene=58&subscene=0#rd
source: 悬镜安全
date: 2024-10-19
fetch_date: 2025-10-06T18:54:05.904538
---

# 源鉴SCA4.7 | 国内首创全链路可达性分析，新一代SCA能力天花板！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGhlOSzYHh0rT72yxfs09cJ5zUXBGXgnUfZFbrH8icT3ibWPPW8VTmz7ibM0iccdiaj8VLoCJKYQGnx3ABw/0?wx_fmt=jpeg)

# 源鉴SCA4.7 | 国内原创全链路可达性分析，新一代SCA能力天花板！

原创

Xmirror

悬镜安全

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGj56PMu0icIF7jYduLbYTpshJC1x89TawLCeibYDfBNPKicmHF2ibBc98oiaKiax0bTs9Vk5mQT9wYuCLhw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGhlOSzYHh0rT72yxfs09cJ5VzicWyoiaCAFia3B8Nicsuuwia7NicoLQIxy5TqnSgDpEwvuIvmNdDk8dn2w/640?wx_fmt=jpeg&from=appmsg)

**被漏洞淹没的安全团队**

part01

SCA用户苦误报久矣。

一个小型项目就会依赖数十个甚至数百个开源库，而对于大型企业应用程序而言，这个数字会指数型暴涨，达到千万级组件、上亿级依赖关系，相应的，与这些依赖项相关的漏洞数量随之激增。

当SCA检出数万个应用程序漏洞时，用户不得不面临这些问题：

所有这些漏洞都是真实存在、可被利用的吗？

如果存在，哪些漏洞实际威胁更大、应当优先修复？

如果要修复，这些漏洞具体定位在哪？

业内通常给出的解决方案是，漏洞可达性分析，即分析项目代码中某漏洞的触发函数在代码中是否被实际调用。

然而，仅仅做到这一地步还远远不够。

让我们像攻击者一样思考，完整的攻击路径是怎样的？

首先得找到系统中可以被利用的入口点（如开放的API、网络端口等），然后通过这些入口逐步深入到系统的内部漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgcD9PpGPoEXqjzuILBiaydh3oeAoTWvS5N6lKu4h7khMGJfWtPwZ1mHg/640?wx_fmt=png&from=appmsg)

反过来说，如果过程中任一环节是不可达的，那么漏洞的实际可利用性就大大降低。

场景1：在一个不对外暴露的内部系统中，可能存在多个漏洞函数被内部代码调用，但这些漏洞由于没有外部接口暴露，攻击者很难直接利用。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgzpUFsllibsUic4h6dY2oic5j3FKUD8nVw7wZDL8j2Z63aRVReVPot4IqQ/640?wx_fmt=png&from=appmsg)

场景2：攻击者可以通过外部接口与系统交互，但项目中依赖的带有漏洞的组件并没有在代码中被实际调用。即使漏洞存在于依赖的组件中，代码也并没有使用该组件中的漏洞部分。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgS48HZQaRu0qPHrCmic9pA36AV7uTych6qHbm1N67bicflvgT3A3SpbuA/640?wx_fmt=png&from=appmsg)

场景3：攻击者能够通过外部接口访问系统，并且系统确实调用了带有漏洞的组件，但是漏洞所在的具体函数并没有被调用。

**漏洞大杀器：**

***全链路可达性分析***

***+供应链情报***

悬镜源鉴SCA在国内率先提出全链路可达性分析+供应链情报的解决思路：外部可达、组件可达、函数级漏洞可达，三层可达性分析，并结合悬镜XSBOM提供的供应链情报视角，带来前所未有的可见性和精准定位。

**1、外部可达**

源鉴SCA分析应用中存在的组件漏洞是否可以通过外部访问路径（比如通过对外开放的http服务、tcp/udp服务等）被触发，如一个Java Web应用通过Spring框架暴露了特定的API，如果这些API连接到存在漏洞的函数，则该漏洞为外部可达。

**2、组件可达**

源鉴SCA可分析开源组件是否被自研代码引入并调用，通过对源码或字节码进行静态分析，列出可达组件的所有调用点，以证明该组件在运行中是可以被实际调用。

**3、**函数级漏洞可达****

源鉴SCA引擎深度联动悬镜灵脉SAST，精准识别在代码中被实际使用的漏洞函数，并给出该漏洞在被检测应用中的完整函数调用链路。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGhlOSzYHh0rT72yxfs09cJ5gQoSNpmERENQl20ndOWiaeVItxu8arg6fFRFqobdwlQOjatic9E0rB0A/640?wx_fmt=jpeg&from=appmsg)

**精细化许可合规治理**

part02

数据显示，国内企业软件项目中，含超危和高危许可协议的项目占比达16.8%。因软件产品未遵循开源许可证相关条款规定，会造成版权侵权、专利侵权、商标侵权和许可证冲突等合规风险。

截至目前，悬镜源鉴SCA4.7版本收录开源许可证数量扩充至**3000+**，针对许可证的各许可条款以及许可责任提供详细的说明：

**1**

细化许可证兼容分析，包括具有相同条款名称但有相反责任的不同许可条款冲突的条款详情。

**2**

新增许可证系列概念：为简化合规治理，源鉴SCA将每个许可证都被分组为具有相似特征和风险的许可证系列，提供一组标准系列，例如AGPL、互惠、弱互惠等共6个许可系列；同时支持自定义添加、编辑许可证系列等功能，以满足企业法律审查人员的个性化要求。

**超全应用场景**

part03

随着开发环境的多样化，开发者使用不同的语言和工具链来构建应用，源鉴SCA 4.7版本在支持开发语言、开发环境、检测对象上持续扩展，覆盖更多应用场景。

**iOS移动应用格式支持**

***iOS漏洞与合规风险检测***

源鉴SCA支持深度检测移动应用格式 IPA(IOS App Store Package) 文件，精确识别IOS中引入的C、C++、Swift/Objective-C组件及其版本，并检测组件版本相应的漏洞、许可证合规性问题，帮助开发者确保他们使用的第三方库和组件是安全合规的，减少发布到App Store时由于违规而被拒的风险。

***iOS敏感信息检测***

源鉴SCA能够检测 IPA 文件中是否包含敏感信息（如用户身份验证信息、密钥等）及其存放路径，防止用户数据外泄，帮助开发者遵守iOS应用开发的隐私要求。

**Android移动应用格式支持**

***提升Dex文件检测性能***

大幅提升Android应用的漏洞检测速度，特别是在处理大型应用时，提高工具的检测效率。

***提升二进制解析精准度***

完善文件头识别，准确解析各类不同的文件格式，防止因解析错误而导致的漏洞误报漏报。

**ArkTS 鸿蒙语言支持**

鸿蒙是华为开发的操作系统，ArkTS 是其特有的编程语言。源鉴SCA 4.7版本新增对ArkTS语言的支持，帮助开发者在鸿蒙生态下检测其代码和依赖库中的组件漏洞，保障鸿蒙平台应用的安全性和合规性。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgxIKcQLic37EQPE1ia76UAGLcd9wuVh4LLr99gC4plCst3Zhl3DH7bxFA/640?wx_fmt=png&from=appmsg)

**本地开发环境支持**

***提供本地CLI真实构建工具***

通过使用开发者的本地环境进行代码构建和分析，源鉴SCA 4.7版本能够捕获更多精准的组件信息，避免因环境差异导致的误报或漏报。

***区分开发环境和生产环境依赖***

开发环境中的依赖通常只在开发或测试过程中使用，而生产环境中的依赖直接影响产品的安全性和性能，区分两者可以帮助开发者专注于修复生产环境中可能引发风险的漏洞，减少不必要的修复工作，优化资源分配。

**扩展集成-制品库支持**

制品库是 CI/CD 流程中的重要一环，源鉴SCA 4.7版本在支持多个代码仓库、私服仓库、镜像仓库等基础上，新增支持蓝鲸CPack制品库的制品文件来源，对构建产物中的依赖进行自动化扫描和分析。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgD2YcRibnq6IicqaAZ3lkzBNQVKPEkt5AR03HOzc6zuCcMF69GReFG6ibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgoGv1W6B2Gh8TwrCR0Taxu2eSxDg9zFqIUXSibpldB1M5GxGH274B1iaQ/640?wx_fmt=gif&from=appmsg)

SCA技术已成为数字供应链开源治理的关键入口。源鉴SCA作为悬镜第三代DevSecOps数字供应链威胁管理体系中开源治理环节的新一代开源数字供应链安全审查与治理平台，同时拥有自研专利级代码成分溯源引擎、制品成分二进制分析引擎、运行时成分动态追踪引擎、容器镜像扫描引擎，能够深度挖掘开源组件中潜藏的各类安全漏洞及开源协议风险，帮助企业从引入源头、开发过程、运行监控、管理多维度闭环治理开源威胁，持续守护中国数字供应链安全。

＋

**推荐阅读**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgoGv1W6B2Gh8TwrCR0Taxu2eSxDg9zFqIUXSibpldB1M5GxGH274B1iaQ/640?wx_fmt=gif&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgTIE454VQH4GCxW6aPKqUNGyZDWOiaIvskCRbQTOk06FGXLne67mCIIQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791324&idx=1&sn=12514828b96eac27d0c73b77601bd5c1&chksm=87709e8bb007179db181e49f59db9ad2dc4732532637b9b07382d41b4ffba259e2ec07ef14af&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGhlOSzYHh0rT72yxfs09cJ55jhqAMgGT4LMOC3xfFibfyv65WenDfUXKlhvAj1p49eiapNy15g1BqaQ/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790714&idx=1&sn=837e57de9527798408f754c126f94348&chksm=87709c2db007153be3a796d2b86def212521e4bce9721d86c9f3a2c1a298b3498f3d9931a43e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgWXkfHibm4C3niaOXrfBicwJTz2aw0kUthKjicbHmia8DIey0erxsYYNNno2DWPjyiaFTQzkgLDak2zfNQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791220&idx=1&sn=367ae9a7f1a43dc39e386c234cccda1a&chksm=87709e23b00717350808147e067afc9fffa7b9866655929685aeef3577585214c45468dcbed6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgfxnwj4QN5WticwNuqqLBxgyzv4zkibMEFia7icHIfl6sJTHqYmlAouE4P52KKTM89Ks2IKxv0ibPOCPw/640?wx_fmt=png&from=appmsg)

**关于“悬镜安全”**

悬镜安全，起源于子芽创立的北京大学网络安全技术研究团队”XMIRROR”，作为数字供应链安全和DevSecOps敏捷安全开拓者，始终专注于以“代码疫苗”技术为内核，凭借原创专利级”全流程数字供应链安全赋能平台+敏捷安全工具链+供应链安全情报预警服务”的第三代DevSecOps数字供应链安全管理体系，创新赋能金融、车联网、通信、能源、政企、智能制造和泛互联网等行业用户，构筑起适应自身业务弹性发展、面向敏捷业务交付并引领未来架构演进的共生积极防御体系，持续守护中国数字供应链安全。

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