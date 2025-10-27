---
title: 警惕！PyPI现DeepSeek恶意软件包：开源安全与供应链防护再敲警钟
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787822&idx=1&sn=11f1cb7ddc2d6d5a9478505fff19fb17&chksm=8893bdc1bfe434d70a2d7e510164f267c268548b9e3c1b0d0fa9abf70cf5264a55cf29d201f6&scene=58&subscene=0#rd
source: 安全客
date: 2025-02-08
fetch_date: 2025-10-06T20:37:54.044265
---

# 警惕！PyPI现DeepSeek恶意软件包：开源安全与供应链防护再敲警钟

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb7uaS0Tr59icFdfmDIbcfkStfO5OIRre1Zv1TSoFaawzLRicIgwialHFLuEXcyb5mt33avia0XvNL5cvQ/0?wx_fmt=jpeg)

# 警惕！PyPI现DeepSeek恶意软件包：开源安全与供应链防护再敲警钟

安全客

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb7uaS0Tr59icFdfmDIbcfkStsGcbWkibKLmSArru1ZJUIbz6FzRCTufFyc7TZJIkwGzOnrgeWSDZnVw/640?wx_fmt=jpeg&from=appmsg)

**01**

**事件背景：当开源信任沦为攻击跳板**

近日，Python官方软件包仓库PyPI（Python Package Index）上曝出一起重大供应链攻击事件。黑客通过伪装成知名AI项目DeepSeek，上传了名为deepseeek和deepseekai的恶意软件包，企图利用开发者对开源生态的信任窃取敏感数据。根据Positive Expert Security Center（PT ESC）的研究，这两个软件包被下载**超过200次**，其恶意载荷通过云平台实时回传用户**环境变量、API密钥、数据库凭证**等核心信息，直接威胁企业基础设施安全。

此次事件不仅暴露了开源软件仓库的安全隐患，更揭示了现代软件供应链的脆弱性。攻击者瞄准PyPI这一全球Python开发者高度依赖的官方平台，通过仿冒流行项目名称，成功绕过开发者对开源组件的信任机制，将恶意代码植入目标环境。这一手法标志着**供应链攻击的战术升级**——从隐秘依赖漏洞利用转向主动伪造高知名度项目。

**02**

**攻击手法拆解：从代码细节到基础设施**

**恶意载荷的“三重收割”**

研究人员分析发现，恶意软件包在执行时触发以下行为：

* **窃取环境变量****：**提取系统环境变量中的敏感数据，包括云服务API密钥、数据库访问凭证、SSH密钥等。
* **回传数据至C2服务器****：**利用Pipedream（一个云集成平台）作为命令与控制（C2）节点，实现数据外泄的隐蔽化和自动化。
* **持久化潜伏****：**代码中预留了后续加载远程恶意模块的接口，为横向渗透埋下伏笔。

**攻击者的“AI助手痕迹”**

恶意代码中出现了大量注释详细的函数说明，例如对数据加密逻辑、环境变量遍历方法的逐行解释。PT ESC团队指出，这些注释风格与AI编程助手（如GitHub Copilot或ChatGPT）生成的代码高度相似，表明攻击者可能借助AI工具快速构建恶意载荷。这一发现凸显了AI技术的双刃剑效应：一方面提升开发效率，另一方面降低了恶意软件开发的技术门槛。

**账户行为中的“红旗信号”**

上传恶意包的PyPI账户bvk自2023年6月注册后长期处于休眠状态，直至攻击前突然活跃。此类“低信誉账户发布高关注度包”的模式是典型的供应链攻击特征。然而，许多开发者因急于集成DeepSeek功能，忽视了账户历史审查这一关键步骤。

**03**

**软件供应链安全：脆弱性解剖**

**开源生态的信任危机**

PyPI、npm等开源仓库已成为现代软件开发的“水电煤”，但其开放性也使之成为攻击者的温床。据Sonatype统计，2023年PyPI恶意包数量同比激增315%，仿冒知名项目名称（Typosquatting）和依赖混淆（Dependency Confusion）是主流攻击手法。此次事件中，deepseeek与deepseekai通过名称拼写变体误导开发者，正是Typosquatting的典型应用。

**供应链攻击的“蝴蝶效应”**

恶意包的传播路径揭示了供应链攻击的链式反应：

* **开发者个体：**因未验证依赖来源，引入恶意包至本地环境。
* **企业CI/CD管道：**若恶意包通过测试进入生产环境，可导致核心数据泄露。
* **下游用户：**若受感染软件被分发，攻击面将指数级扩大。

安全专家指出：“一次PyPI恶意包上传，可能引发从个人开发机到企业云集群的全链条沦陷。”

DeepSeek恶意包事件绝非孤立案例，而是当下软件供应链安全危机的缩影。随着AI驱动的攻击技术升级，开源生态必须构建更健壮的防御体系：开发者需摒弃“拿来主义”思维，企业应建立从代码到云端的全链路防护，而开源平台则需在便利性与安全性间寻找平衡点。

最终，安全的开源生态需要社区、企业与技术提供商的共同守护——唯有将“信任但验证”的理念深植每个环节，才能抵御这场无声的供应链战争。

**推荐阅读**

|  |
| --- |
| **01**  ｜[特斯拉充电桩一天被入侵两次](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787811&idx=1&sn=4927212fd9debdf7d94032ffd45aa0a9&scene=21#wechat_redirect) |
| **02**  ｜[拜登政府的警告和美国的未来](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787757&idx=1&sn=e5eae9b6df27d7b00015e86ca2284def&scene=21#wechat_redirect) |
| **03**  ｜[2024年度网络安全政策法规一览](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787787&idx=1&sn=ee8ea4a11f904302c035eb5170b8891e&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7uaS0Tr59icFdfmDIbcfkSt6fNT7C3hsGgibJbGJ5vS29CyV5sF2V7sUWk6GFa7Hgh0yMMsaVHW8WA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7uaS0Tr59icFdfmDIbcfkStU5a3Z5IfYNklle5VRq3ibWticQL0XPXYp1cicEMOj0evyyUx7l7rpictFQ/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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