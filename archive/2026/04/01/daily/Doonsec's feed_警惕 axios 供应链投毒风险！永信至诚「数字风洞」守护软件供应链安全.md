---
title: 警惕 axios 供应链投毒风险！永信至诚「数字风洞」守护软件供应链安全
url: https://mp.weixin.qq.com/s/pFpmj1QkT0AMX41jBgDsew
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:27:53.581974
---

# 警惕 axios 供应链投毒风险！永信至诚「数字风洞」守护软件供应链安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WDfGU4XyhS2lXs7z2yCrQfKKEtUwOzJVgapdr3YyOibbibicyIicp4upls6ZUJuCPb9UZzsp2NahH74z7lZwPgqkTAS3xV3VCkepP2xtfxqiaAwI/0?wx_fmt=jpeg)

# 警惕 axios 供应链投毒风险！永信至诚「数字风洞」守护软件供应链安全

永信至诚

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WDfGU4XyhS0cDPy2aYCIwuibNTUn7K6pjYgvwDRgBH8sFHdRSrPbcq2Mqn3GVtTXQtGibejJUhxDU1piarbNoKGv74cUu3jZuCbTtT9zqcFHeM/640?wx_fmt=png)

永信至诚「数字风洞」安全团队监测到一起Node.js供应链投毒事件。**攻击者向npm仓库上传了axios的两个恶意版本（1.14.1和0.30.4），这些版本在安装时会自动拉取恶意依赖包plain-crypto-js@4.2.1**。无论是开发者手动安装还是通过 AI 编程工具，均会触发该恶意依赖。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WDfGU4XyhS1Ncy0ib4FYuMmGugIAdhuJXbwkheImCYqj8KF7JxLIv4y0eHXRYXfj0GZoLN9b18tiaON9eoR9L8q1aSrOLCesvYS6exXhKLReQ/640?wx_fmt=png)

本次攻击覆盖 Windows、macOS、Linux 多平台，执行后会自动销毁痕迹。**一旦开发者通过npx命令或latest标签安装时，恶意代码即在 Windows、macOS 和 Linux 平台中自动运行并建立长期控制。**目前npm官方已下架相关恶意包，但已安装系统仍受影响。

安全团队分析发现，攻击者利用npm包管理机制中的postinstall钩子触发恶意行为。安装受污染版本时，npm自动下载嵌套依赖plain-crypto-js，并根据操作系统下载对应的远程控制载荷（C2 payload）执行。**恶意脚本执行后自毁，并覆盖原始配置文件，抹除审计线索，使得企业难以察觉入侵痕迹。**

基于本次供应链投毒具备的自动触发、深层嵌套、隐蔽自毁等特性，永信至诚建议企业立即采取以下排查与阻断措施：

**01**

**核查高危版本，划定影响范围**

立即排查开发环境、CI/CD 流水线及生产服务器。**重点检索项目依赖树中是否存在 axios@1.14.1 或 0.30.4 版本，并检查 node\_modules 目录下是否包含 plain-crypto-js 文件夹**。若发现相关目录，即判定环境已感染。

**02**

**清理 npx 缓存，阻断重复感染**

**使用 Codex、Claude Code 等 AI CLI 工具的企业，需立即清理 npx 缓存。**Windows 系统删除 %LOCALAPPDATA%\npm-cache\_npx目录；macOS 及 Linux 系统删除~/.npm/\_npx目录。

**03**

**收严控依赖引入，禁用自动脚本**

在全局环境执行 npm config set ignore-scripts true，禁止安装脚本自动运行。同时，在代码库的 package.json 文件中严格指定组件安全版本（如明确锁定 axios@1.14.0），**禁止使用 latest 等模糊版本号，防止 AI 工具自动拉取未验证版本**。

**开源供应链脆弱性**

**从单点突破到全链条扩散**

axios 投毒事件表明：现代软件高度依赖开源，供应链安全风险已成为政企单位的现实挑战。此次攻击暴露出软件研发链条的结构性脆弱：**单一组件漏洞可迅速演变为全链风险。**

**开源组件泛滥，准入审核缺位**

中国信通院调查数据显示，目前超过 90% 的企业在研发中使用了开源技术。开源组件极大提升了生产力，但也导致大量外部代码在未经严格安全审查的情况下，直接进入企业核心业务线。**开发者常使用 latest 标签、AI 工具默认拉取最新版本的操作，导致带有恶意代码的组件能够轻易穿透企业网络**。

**依赖关系错综复杂，风险沿嵌套链传递**

现代软件项目依赖树庞大。研究表明，开源软件中80%的安全漏洞潜伏在传递性依赖（嵌套依赖）中。本次攻击中，**攻击者未将恶意代码直接写入axios，而是将其植入名为plain-crypto-js的深层依赖。开发者通常仅关注直接引入的顶层组件，深层嵌套的依赖长期处于安全盲区，成为恶意代码的藏身之处。**

**软件资产底数不清，缺乏有效排查手段**

本次攻击具备反取证特性：恶意脚本执行后抹除痕迹，常规审计工具无法还原攻击过程。**企业若缺乏准确的软件物料清单（SBOM），便无法回答"系统运行了哪些代码"这一基础问题。**资产清单模糊导致安全团队接收威胁情报后，无法快速定位受影响的开发终端、CI/CD节点及生产服务器，错失应急响应时机。

**传统安全防线滞后，难防研发阶段风险**

**供应链攻击发生在代码编写、依赖拉取及持续集成阶段**，AI工具的自动化操作使攻击触发更隐蔽、扩散更迅速。传统安全体系聚焦网络层与运行时边界防护，难以感知开发环境内部的投毒行为。**企业需改变被动防御模式，将安全能力前移至软件构建环节。**

**永信至诚「数字风洞」软件成分分析系统**

**构建供应链主动防御体系**

应对 axios 这类供应链投毒事件，安全机制需前置，将风险识别与管控嵌入 AI 工具参与的软件全生命周期（SDLC）。**永信至诚「数字风洞」软件成分分析系统（SCA），通过自动化解析软件构成、绘制依赖图谱、识别漏洞与合规风险状况，帮助企业建立资产可知、风险可控的开源供应链治理体系**，实现对人工操作和 AI 工具自动化行为的全流程安全管控。

**精准识别漏洞与恶意代码**

系统基于 6000 万+组件库、30 万+漏洞库、180+许可证库，同步追踪 CVE、NVD、CNNVD 等漏洞库及威胁情报。**在代码准入阶段，系统能够精准识别组件中的已知漏洞与恶意特征（如本次的 plain-crypto-js 伪装包）**。通过对风险进行多维度评级与优先级排序，系统可以在开发早期自动阻断高危组件上线，避免业务带病上线。

**穿透依赖层级，定位深层风险**

针对投毒代码往往隐藏在深层依赖中的痛点，平台具备强大的代码结构穿透能力。**系统能够精确绘制多级嵌套的开源组件依赖链条，洞察深层架构体系。当出现类似 plain-crypto-js 这类底层的恶意伪装包时，平台可快速追溯其引入源头（如定位到 axios@1.14.1），梳理从 axios 到 plain-crypto-js 的完整传播路径**。这种深层挖掘能力大幅降低了排查难度，有效切断风险随依赖链条逐层扩散的可能。

![](https://mmbiz.qpic.cn/mmbiz_png/WDfGU4XyhS2j3lfrOMqlIAhhuXBANhbJcjyTUUvtI7f68cO1VT3ia9t8lv8DWONZ8otV2dbdic4Jl0gib4r08crqXmTZVX1Lryfb5GmiaYU9Wns/640?wx_fmt=png)

**自动生成 SBOM，实现资产透明化管理**

平台支持自动扫描人工开发、AI 工具生成的源代码与二进制文件，准确识别项目中使用的所有开源成分，自动生成格式规范、可追踪的软件物料清单（SBOM）。**通过建立全局多维风险数据看板，帮助企业自动化管理软件资产。在面临0-day 投毒等突发威胁情报时，安全团队可依托 SBOM 清单，在分钟级内精确定位受影响的资产范围**，彻底改变人工排查耗时费力的现状，提升应急响应效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WDfGU4XyhS0YTNk9fXoXbUCI7oEyXggBnaDTZsYZrsShImfawPXNEW56Bfic60yfElfaqhPrVDyEpdXWq0VnsncdUw889WBqyAXsHSic72rck/640?wx_fmt=png)

**灵活集成，顺利嵌入 DevSecOps 流程**

系统支持 Git、GitLab、文件上传等多种接入方式，对接 Jenkins、GitLab CI/CD 等主流构建流水线。**在代码提交、构建及测试环节自动触发安全扫描，对研发流程零干扰，确保开源风险治理贯穿 AI 参与的软件研发全生命周期**，从源头预警并修复问题，降低后期安全运营成本。

应对 AI 工具参与研发带来的新型供应链安全风险，资产可视与安全前置缺一不可。**作为数字安全测试评估赛道领跑者、网络靶场与人才建设领军者、AI「原生安全」倡导者**，永信至诚将持续基于「数字风洞」产品体系，为企业构建可见、可控、可防御的软件供应链安全能力，确保每一次构建、依赖更新及交付链路都可验证、可信任。**保障数字健康，带给世界安全感。**

axios 投毒事件只是冰山一角，供应链攻击防不胜防。数字风洞软件成分分析系统（SCA），帮你一眼看穿依赖风险，精准定位恶意组件，让供应链威胁无处藏身。**现在扫描二维码，即刻预约「数字风洞」**软件成分分析系统**产品演示，给代码资产上个"安全锁"**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WDfGU4XyhS08zLf6oGTTlJBp8de7H7O1mBGcTGrbvFh0L4RnGEM6G7YxppibAFQ3ibrx40b4HJnG6IKywOEe3bFPXho2whAXv7xibEdSLuVU18/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/WDfGU4XyhS0xkZJLiaatUqSSic5xPYwCftu1hz7CqyhC1uatu87qJNXsV8GJnroqMeZTz75vvmJ0yAaibDSWqHYCiapoGfmWQ8rOkIZoKvKs3OI/640?wx_fmt=png)

**往期精选**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/WDfGU4XyhS1Qr38eJcFTQnib3yqnWvLSjeqoqDic4Qfu8OTib7dO6COBmASckdCzEf78NjWc8B1VpGHhWGCibk2RgvXgC0afwh3ozx9fTojOdNo/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454834133&idx=1&sn=3113aa69ea5784a5188e1cadb20dde67&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/WDfGU4XyhS12xSsJkhKcFGbl6LP2RuicYKZLOocF0Ga1wmAT4ewr6lTgNcDwcNAsvwCJRLhwicRyk8nRacgg6AibftJepjT50lzlswPAvh64Is/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454832547&idx=1&sn=8c7b57d8417cdf591e260dd4311f64c8&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454832547&idx=1&sn=8c7b57d8417cdf591e260dd4311f64c8&scene=21#wechat_redirect")

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/WDfGU4XyhS0PSVibfKrWvfeXtUVRTOCAHA2whOkPE3WMZqQqRLdAaicbKR7jDgeokfU08jHscuPic9APXOakHXlLTWgmHO1mjGtcWWmfTYNAnA/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454832493&idx=1&sn=2a2e529846541f62723b6f5f6eda508d&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454832493&idx=1&sn=2a2e529846541f62723b6f5f6eda508d&scene=21#wechat_redirect")

[![](https://mmbiz.qpic.cn/mmbiz_png/WDfGU4XyhS2gRmdKic5EMCHbkGsLIdQonkEg0eOpAhSFPRXvDwYfKhB9j8Yy4YicTuTkzM5EnEsafTjrWadS7MvXyh2ep1p3Bndd8gxV09Wxg/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454831684&idx=1&sn=3e4445cbd5089cdc2ffe9845553eaf88&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454831684&idx=1&sn=3e4445cbd5089cdc2ffe9845553eaf88&scene=21#wechat_redirect")

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/WDfGU4XyhS1Ria3jNpxyhW67YNncWC4ZMwmoWPm0iaZceOicAXT4FicbrZdicS7CLBYJRHSfeMzMbcQZ7XLLgUJOV0CdP4NibyruibX4SoIvNibtbsU/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454831924&idx=1&sn=2963b78ac99ff5a3b9e049abcfb2d4f6&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454831924&idx=1&sn=2963b78ac99ff5a3b9e049abcfb2d4f6&scene=21#wechat_redirect")

[![](https://mmbiz.qpic.cn/mmbiz_jpg/WDfGU4XyhS1U8CPAZpo6DialicVmVgXWKCgdYBNd1ahoicw3HiaPMNWzKGzOwyyyKJYq4GJgc2NEksbsBia2XjKQ2GdPGzHAVBhyiapLkfU7ALibeo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454830697&idx=1&sn=5bc73edb139ca5f292b13dcec22b65ec&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454830697&idx=1&sn=5bc73edb139ca5f292b13dcec22b65ec&scene=21#wechat_redirect")

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WDfGU4XyhS30DAUJ0MHLMa3vxe9oic56ia8DMCu6L1icVMAYXibzwNgyibwYdBTgLuSlF9icxbhGMpE2rDFX3XEANVqZe5GlbKQY06A8Hkcvcln4Y/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454830592&idx=1&sn=e94b3d45cc910fff130c5af6cd5c591c&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454830592&idx=1&sn=e94b3d45cc910fff130c5af6cd5c591c&scene=21#wechat_redirect")

[![](https://mmbiz.qpic.cn/mmbiz_png/WDfGU4XyhS0IFEKzAMexH5qVqWE0bddXn1ybhpmM3fwD837iaUpYEibgUnCttIicia0mvQUic7A5YFTMIyiaL0h1sed4T6f0yic0pXHmyh9BjJe5IM/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454830141&idx=1&sn=64bce7e4378991693e84a4837604fe5e&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454830141&idx=1&sn=64bce7e4378991693e84a4837604fe5e&scene=21#wechat_redirect")

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/WDfGU4XyhS2saia1Ht0uOKt5Eb8MkfxPnbIy3rbqe54c3LseUh4V4rcaYfVc8RGM8XfqJpHuJeLAkcJHKyzRasNas8vIQVQMHCdgWGjHpdp8/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAwNDUyMjk4MQ==&mid=2454829347&idx=1&sn=6b63a35bd8ac5046e0216e782705ea...