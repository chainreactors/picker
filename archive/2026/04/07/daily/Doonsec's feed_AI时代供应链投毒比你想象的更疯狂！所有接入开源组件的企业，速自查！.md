---
title: AI时代供应链投毒比你想象的更疯狂！所有接入开源组件的企业，速自查！
url: https://mp.weixin.qq.com/s/pKZYmt0vJ3C1lHCnAU7ElA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:32:26.227454
---

# AI时代供应链投毒比你想象的更疯狂！所有接入开源组件的企业，速自查！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dAHic6zw8sw9HA1rnkAfjLvVejSOyYkK53p7a6OuprtMOGWl0YhWP0kyDdHFgiaXibtHoib0Iia165FhUxwRgeY6vXLeKxibEkVeZmjZmAm10fmZI/0?wx_fmt=jpeg)

# AI时代供应链投毒比你想象的更疯狂！所有接入开源组件的企业，速自查！

原创

智安全
智安全

深信服科技

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/EJiaEo3Lq9koGLKLb2iaWgKP2F0ftwVWJA81gM12TmKNUKESbTUmMOlHbmARBVWeoxkRAMwBLMwX5w4ianpTibj6KQ/640?wx_fmt=gif&from=appmsg)

近两周，深信服千里目安全技术中心先后监测到三起影响广泛的供应链投毒事件——

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

开源AI API网关LiteLLM在PyPI发布的1.82.7和1.82.8版本被植入恶意代码，在常规安装时即可静默触发信息窃取并横向移动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

API协作平台Apifox公网SaaS版桌面客户端遭遇供应链投毒，恶意代码可窃取凭证并远程执行命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

主流JavaScript库axios的两个npm版本axios@1.14.1、axios@0.30.4被恶意植入远程控制代码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dAHic6zw8swicE6dLKMZZcNZP1gl6XibNqULX7Pt6FaCBCvdic8wQdmTF9B1WMG5q5Gb4X2gIUlhJj8pEMwCEDRQVOmKdhHcW5icDCtPjW8pK02s/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/dAHic6zw8swicmwiavbBc3aibsricmcISeoZh76wjZ3c0bxko4HJNEmB4I9ibLKoew55WgAe1raGkzvQVrJXrlzhCD3ZCKunyypmic37ceCRRdUIick/640?wx_fmt=png)

三起影响广泛的供应链投毒事件分析

AI时代，开发迭代速度大幅提升，企业对开源组件、AI工具链的依赖程度持续加深。攻击者正是利用开发者生态的信任链条发起攻击，潜伏在开源组件、开发工具、部署流程等环节中。

从LiteLLM、Apifox到axios接连爆发的供应链投毒事件中，我们可以看出：**供应链攻击已进入常态化、精准化的新阶段，安全风险全面升级。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

**开发工具软件成为供应链攻击的首选入口。**一旦工具被攻陷，攻击者可直接获取系统权限，快速渗透内网，破坏力远超常规攻击，成为AI时代企业安全的核心短板之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

**攻击工具化与精准化是重要趋势。**以Apifox投毒事件为例，恶意软件本质上是一个远程代码执行平台。攻击者基于回传的信息筛选高价值目标并实施定制化攻击，整个攻击模式逐步向APT化演进，而常规安全防护手段难以有效抵御。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8sw8GsyCkQR7mEkiaAly1niav3rhNPiczUm1fNUfZuPNmO1cENUfCk5HgkdNASB8mwSwCvyVjLjby4gk3CPGDsTQQlugicVmoFNucSkM/640?wx_fmt=png)

**应急响应建议**

面对这类攻击，需要警惕的是，**目前公开的IoC仅涵盖侦察和凭据采集阶段，绝非攻击的终点。受影响的企业和开发者需要按照“已完全失陷”的最高级别启动应急响应，以免遗漏可能已发生的深度入侵。**

**快速排查（IoC）**

在网络侧检查是否出现对apifox.it.com、models.litellm.cloud等异常访问；

在终端侧排查litellm\_init.pth、/tmp/ld.py，6202033.vbs等恶意留存痕迹。

**全域清除感染**

Apifox客户端升级至2.8.19或以上版本（官网下载并覆盖安装）；LiteLLM降级至安全版本1.82.6并锁定依赖；axios退回至安全版本1.14.0-1.x分支或0.30.3-0.x分支。

在防火墙、企业DNS或本机hosts中封锁已知恶意域名；同步清空Apifox本地缓存数据；删除axios相关的木马文件。

**凭证轮换（按优先级执行）**

立即重置SSH私钥、Git凭证、云服务凭证AccessKey、K8s集群配置等所有可能泄露的凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8sw86hntJYSZujr8dyDqlZAc6BpcZov7wdBlDfxyibWOWTOtdibLeB6D5I786Fy5e4GaicGRNpHNuFFlibBf2ZunpG4pWoxHia70z5Q04/640?wx_fmt=png)

**从「被动修复」转向「主动治理」**

**重构AI时代的供应链安全防线**

实际上，供应链安全风险具有‌系统性、长期性和复杂性‌等特点，仅靠一次临时性、事件驱动的应急响应难以构建持久的韧性。

**企业和开发者必须将供应链安全纳入与功能开发同等优先级的体系化建设中，从制度和技术两个维度重构开发工具链信任体系，实现从「被动修复」到「主动治理」的根本转变，从而筑牢AI时代的供应链安全防线。**

**从制度层面明确规范**

企业和开发者应将安全管理融入研发流程中，通过开发工具沙箱化运行、凭据动态轮换机制、供应链SBOM管理等举措，形成常态化的安全治理体系，以制度约束推动规范化管理，从源头降低供应链安全风险，实现长效治理。

**从技术层面强化保障**

此外，为更好地应对复杂多变的供应链攻击，深信服提供一整套解决方案，帮助企业主动守护研发安全——

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

**主动运营，提前发现风险并闭环处置**

深信服MSS安全托管服务，7\*24小时主动监测风险，主动预警供应链攻击情报并协助用户应急响应，确保用户第一时间获取最新威胁情报并完成内部排查；联动aES终端安全，及时发现隐蔽威胁并实现安全事件闭环处置，有效防范攻击者深度渗透。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

**主动防御，以快制快，实时拦截新型威胁**

深信服AI+SASE赋能的下一代防火墙，通过云威胁情报网关，实时拦截C2外联等新型威胁；通过云端AI智能体，实时挖掘供应链攻击事件并全网共享威胁情报，帮助用户快速发现异常远控等新型威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibn9B3uuApiaPVvFBjCAspG8yicJnyyBPsgwECicUmbErtIyEdRSglrzW9Lw2AQbCIsibOGgFl3QPXafGxzxbSACdbKDgqBwFiaEM8s/640?wx_fmt=png)

**主动隔离，构建可信可控的研发环境**

深信服零信任上网沙箱方案，帮助用户实现业务访问与互联网访问的双重隔离，最大限度收缩攻击暴露面，保障办公与开发环境的可信可控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAHic6zw8swibpavmvcb5RYbicn3UljCics4zEybqVW6Nf115jmXHWStZwveSRvicYbdUWEPOM27gXF3QyRib70JVXhH3Qb3sCxWYU3eCp9h9bGiak/640?wx_fmt=png)

**欢迎咨询供应链攻击**

**全场景主动防护方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/dAHic6zw8swic1pdZiaF3WpcWXwTULt1p2v7eH4HwnyH2Es9zcs95ibHuPnjUPia1pamUL6fxjDIicOsib04EoltEOqrXuP82CzcykOvt3ibF1iaZxvI/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9koicYib2cMiap0JlgdQm0RlLPBOh7AhGHYVfE5bm0BPp62ySojm1TzVCjqZZw1iawBrq3Sz6jDCHibRFCg/0?wx_fmt=png)

深信服科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9koicYib2cMiap0JlgdQm0RlLPBOh7AhGHYVfE5bm0BPp62ySojm1TzVCjqZZw1iawBrq3Sz6jDCHibRFCg/0?wx_fmt=png)

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