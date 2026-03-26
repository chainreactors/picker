---
title: 【漏洞预警】LiteLLM 投毒、Apifox 后门连发，敲响供应链安全警钟
url: https://mp.weixin.qq.com/s/foeEgdzYWGhZKb4DZC9Gfw
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:27:42.727305
---

# 【漏洞预警】LiteLLM 投毒、Apifox 后门连发，敲响供应链安全警钟

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KEyAvJTWH1poRPmk6aOO6sSZDzNib9nmXQLJicEL1zhAdwicctb7ia2QhiaGQOkhCvqTKicrO1ibDg6rYAzAOxalT8FgVIv5OYRhTObYicbKfX567ZE/0?wx_fmt=jpeg)

# 【漏洞预警】LiteLLM 投毒、Apifox 后门连发，敲响供应链安全警钟

云弈安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/KEyAvJTWH1pdJ08doKby0a9NtdNoiaKfyMuib4ExGorvFv1epVchms9eXOWbahuHTd3EcVAk0YRdxS2JG9Q6HyUiaaftXYszIUDVASI7r0JNkE/640?wx_fmt=gif&from=appmsg)

**01**

**漏洞信息**

2026 年 3 月 24 日至 25 日，开发者领域接连被曝**两起重大供应链安全事件**：**AI 开发核心 Python 库 LiteLLM 在 PyPI 被植入恶意代码**，**国内主流 API 协作工具 Apifox 桌面端被曝出存在后门漏洞**，两大高频开发工具相继沦陷，引发全行业供应链安全危机。**LiteLLM**作为连接百余家大模型提供商的统一网关，**月下载量高达 9500 万次**，**Apifox**则**覆盖国内数百万 API 开发、测试从业者**，二者的安全问题直接波及 AI 开发、接口研发等多个开发者生态，让整个技术社区对供应链安全的脆弱性有了更深刻的认知。

**02**

**事件影响**

**——双工具沦陷，覆盖全栈开发场景**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KEyAvJTWH1rwDiaib0mibxSaC2taRTpTTR4gsEcsBT3E8Np4OCJYJZPpd3VyiaiakNS0NWtr04XghdXj7bG7jvS4GkOBnoqOrPwsPlnXvMoznxzM/640?wx_fmt=png&from=appmsg)

**LiteLLM 投毒 -****AI 开发生态核心基建遭重创**

**!**

**下载量惊人，影响范围广泛**

* **月下载量：**LiteLLM的**月下载量超过9500万次**，**日均下载量约340万次**。
* **云环境渗透率：**据安全机构Wiz数据显示，**36%**的云环境中都存在LiteLLM的身影。
* **潜在受影响安装次数：**由于LiteLLM的广泛使用，此次投毒事件潜在受影响的安装次数巨大。

**!**

**AI应用面临重大风险**

LiteLLM作为AI应用中的关键中间件，其被投毒意味着攻击者可能窃取到：

* **SSH密钥：**用于远程登录服务器的私钥。
* **云凭证：**包括AWS、GCP、Azure等云服务商的访问密钥。
* **Kubernetes配置：**集群管理的重要凭证。
* **数据库密码：**直接访问数据库的密码。
* **加密货币钱包：**数字货币的安全存储信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KEyAvJTWH1rZUlPaBoYqxuicrg67LFWATdG13ongUbRNzNUvFlMSrxFE4VHjmPiaSU9OmdXqZ23VyAZfI86w3RRd8Xvbo2cibsDE5yTnDyOticM/640?wx_fmt=png&from=appmsg)

**Apifox 后门 - 国内 API 开发者终端面临全面入侵**

**!**

**全平台无差别受影响**

受影响范围覆盖 Apifox 桌面端全平台（Windows/macOS/Linux），作为国内开发者高频使用的API一体化协作工具，其用户群体涵盖后端开发、测试、前端工程师等，终端入侵风险直接触达数百万从业者的本地开发环境。

**!**

**终端被完全控制，窃取维度多元**

攻击者可通过漏洞远程控制用户终端，本地数据与开发环境均面临全面泄露风险。

* 窃取 SSH 密钥、Git 明文凭证、命令行操作历史。
* 获取 Apifox 账户信息、主机机器指纹。
* 执行任意远程代码。
* 遍历用户主目录、桌面、文档目录结构，窃取 npmrc 认证令牌、Kubernetes 集群配置等开发核心信息。

**03**

**攻击手法揭秘**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KEyAvJTWH1qzjUZ5SCbJXgQ3bX263A9TRia1CurbjYzlRP44VUfP6dP2TvlxfGV7lpviac52DJ7MhPAutzmubKXUeBm51DH5xhcVaFPAPwf98/640?wx_fmt=png&from=appmsg)

**LiteLLM 投毒 -****全链路渗透，**

**绕过官方发布流程**

**·**

**投毒方式**

**绕过正常流程，直接上传恶意版本**

攻击者通过入侵LiteLLM维护者的PyPI账户，直接上传了含有恶意代码的版本1.82.7和1.82.8，完全绕过了GitHub的正常发布流程。

**·**

**恶意代码三阶段攻击**

**凭证窃取**

* 恶意脚本系统性地搜集宿主机上的敏感信息，包括但不限于SSH密钥、云凭证、Kubernetes配置、数据库密码等。
* 使用AES-256-CBC加密和RSA公钥加密技术，将窃取的数据打包发送至攻击者控制的域名。

**横向移动与持久化**

* 在Kubernetes环境中部署特权Pod，挂载宿主机文件系统，写入后门。
* 在本地写入持久化后门脚本，并通过systemd用户服务实现开机自启。

**·**

**意外暴漏的bug**

此次攻击之所以被迅速发现，是因为恶意代码中存在一个递归fork bomb的bug，导致被感染机器内存耗尽并崩溃。否则，攻击者可能会在后台默默窃取数据数天甚至数周。

![](https://mmbiz.qpic.cn/mmbiz_png/KEyAvJTWH1p97dRzILqjJTcr8icTKXdqPWicrPvBhAv5Exz7Zia02UX55eQpYtH8jIxuTFaI7p4GzeS90fGDKKZLIVYSB0Qa5dQaXDvLGOnFia0/640?wx_fmt=png&from=appmsg)

**Apifox 桌面端后门 - 利用框架漏洞，**

**恶意代码高度混淆**

**·**

**投毒方式**

**篡改 CDN 文件，域名混淆降低警惕**

攻击者将官方34KB的apifox-app-event-tracking.min.js文件篡改为77KB的恶意版本，在合法代码后追加42KB高度混淆的后门代码，并通过伪造的apifox.it.com域名作为C2服务器，该域名利用视觉相似性伪装成官方子域名，注册门槛低且不受标准体系监管，极具迷惑性。

**·**

**漏洞根源**

**框架配置不当，暴露核心接口**

Apifox 桌面端基于Electron框架开发，未严格启用sandbox参数，暴露Node.js API接口，成为攻击者的核心入侵入口，攻击者通过篡改官方CDN上的事件追踪 JS 文件，实现恶意代码的分发。

**04**

**解决方案**

**·**

**修复方案**

![](https://mmbiz.qpic.cn/mmbiz_png/KEyAvJTWH1qswYC7ZQeatrlyNOpicHEcCs7ibkChicV4DWBTDZ1icLau9JkUlicsoFXCGpp8K4FjDfBuQHwvMC2Id5ibJF9CCpiaA0HGLYfCAoGN4c/640?wx_fmt=png&from=appmsg)

**LiteLLM 投毒**

|

**紧急检查**

* 使用pip show litellm检查当前安装版本
* 搜索~/.cache/uv和site-packages目录下的litellm\_init.pth文件
* 检查Docker镜像和CI/CD流水线中的虚拟环境

|

**卸载与清理**

* 卸载LiteLLM：pip uninstall litellm -y
* 清理缓存：pip cache purge或rm -rf ~/.cache/uv
* 删除恶意文件：find ~ -name "litellm\_init.pth" -delete 2>/dev/null

|

**检查持久化痕迹**

* 检查~/.config/sysmon/sysmon.py和~/.config/systemd/user/sysmon.service文件
* 审查Kubernetes集群中的可疑Pod和Secrets

|

**轮换凭证**

* 立即轮换SSH密钥、云凭证、Kubernetes配置、.env文件中的API Key、数据库密码等所有高价值凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KEyAvJTWH1oK0gzenESVlq3SugXCSAe65qj5FKaEeYL81R7BpsWKzVSIxMibv90evrSv0QcFXmOQzkJpBriciaAbMEFsvlIWWqJW18C1melBGA/640?wx_fmt=png&from=appmsg)

**Apifox 后门**

|

**紧急检查**

* 打开开发者工具（Windows/Linux：Ctrl + Shift + I；macOS：Cmd + Option + I），执行检测代码console.log({机器指纹: localStorage.getItem('rl mc'),缓存信息头: localStorage.getItem('rl headers')});，若返回 64 位十六进制机器指纹且包含系统信息，即确认已被感染。

|

**立即处置**

* 停止使用 Apifox 桌面端，等待官方修复版本；
* 切勿以管理员权限运行 Apifox，降低攻击影响范围；
* 检查本地网络连接，排查异常外发流量；
* 可临时使用 Apifox 网页版或 Postman 等替代工具。

|

**本地清理**

* 清除本地 Apifox 相关缓存文件，检查本地 SSH 密钥、Git 凭证等敏感信息是否存在泄露风险，若发现异常及时更换。

**·**

**云弈安全解决方案**

**提升安全意识：**开发者应时刻保持警惕，对任何来自PyPI、CDN或其他渠道的依赖包进行严格的安全审查。

**加强依赖管理：**固定版本、启用哈希校验、减少在线拉取latest版本，确保依赖的可复现构建，禁用非必要的框架接口与权限。

**实施最小权限原则：**限制开发环境、云平台、Kubernetes 集群等的凭证访问权限，避免使用高权限账户进行日常开发，大幅减少攻击面。

**建立应急响应机制：**制定详细的应急响应计划，包括隔离受影响主机、清除恶意版本、排查持久化痕迹等步骤。

**●****安全警钟****●**

此次LiteLLM 投毒与Apifox 后门事件的接连爆发，并非独立的安全事故，而是供应链攻击成为主流攻击手段的鲜明信号。从开源依赖包到商业桌面工具，从云端基础设施到本地开发终端，供应链的每一个环节都可能成为攻击者的切入点，而开发者对第三方工具的高度依赖，也让供应链安全风险被持续放大。

这两起事件不仅暴露了当前开发者生态中依赖管理、框架配置、流程管控等方面的诸多安全隐患，更凸显了供应链安全在技术飞速发展背景下的极端重要性。无论是 AI 开发还是常规的接口研发，开发者都应摒弃 “重功能、轻安全” 的思维，将供应链安全纳入开发全流程，从依赖选择、版本管控到终端防护、应急处置，构建全维度的安全防护体系，才能在复杂的安全环境中，守护开发环境与基础设施的安全。

**关于我们**

云弈科技作为深耕网络空间安全的国家高新技术企业与"专精特新"企业，秉持"攻防一体"核心理念，依托自主创新实战能力，构建了以安全托管运营为核心的全场景安全服务矩阵，为用户打造体系化、常态化、实战化、可持续进化的智能安全运营解决方案。

云弈科技已为政府、运营商、金融、能源、教育等关键信息基础设施行业的数千家客户筑起坚实的安全屏障，赢得了市场的高度信赖。未来，我们将持续引领网络安全创新，以前沿技术与专业服务为国家数字化建设注入核心安全动能，构筑安全、稳定、可信的网络空间坚实屏障。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/KEyAvJTWH1pyjWYA8LBBheN1h9f1epl3h0TBgo39DYLic9cldj3kwznRsAEEQZRq7DNvygfsB5sIOgutibBlUFfJsZeCt7JSUH7xky6tA7cPs/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/KEyAvJTWH1rAH0BCpicCuxHAXVcy8CkaMiczXfQib7DRIIYvXmxJcPFzWTFW7G9q7FpYNa31QYOY1OI6Ad213w0GDen18wf5FgN8dRgZVpp0Vc/640?wx_fmt=gif&from=appmsg)

**权威认可**

国家高新技术企业

中关村高新技术企业

北京市“专精特新”中小企业

北京市“创新型”中小企业

北京市科技型中小企业

北京国际大数据交易所数据经纪商

《2023信创产业TOP100榜单》TOP100企业

WIA2023创新奖

......

![](https://mmbiz.qpic.cn/mmbiz_gif/KEyAvJTWH1reYKGFYsdd5W6wbY2lPx9zpGmWrBBibibY6MomO7kf0cBWo3Jl3j6jdHxIicJIVOTLiaibJibrPiaIg0uYv2bI50q69iccu92iarIdiafng/640?wx_fmt=gif&from=appmsg)

**荣誉奖项**

中国网络安全产业联盟先进会员

中国网络安全创新百强企业

中国网络安全产业百强企业

中国网络安全市场百强企业

2025年“数据要素×”大赛区域协同赛道优秀奖

2025年中国互联网创新大赛低空经济专题奖

2024年京津冀信息通信领域网络安全

实战攻防演练优秀攻击团队

2023中国网络安全产业势能榜

【金融】行业年度杰出“创新型”安全厂商

2022年中国网安产业潜力之星

......

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/KEyAvJTWH1qFDz5FjK66BW7YJbS74XPbkicOuvliawbAuWBrKGtW6j2Mazy35E5feOvhA8fPefichNYvCG8t48UnBzPpc2sYVDsnzmicu7S6Wbc/640?wx_fmt=gif&from=appmsg)

**合作联盟**

中国网络安全产业联盟

中国网络安全产业创新发展联盟

北京市工商业联合会

中国电子工业标准化技术协会

中国通信企业协会

北京网络空间安全协会

统信同心生态联盟

麒麟软件安全生态联盟

ISC终端安全生态联盟

UOS主动安全防护计划

海光产业生态合作组织

网络安全服务阳光行动成员

......

![](https://mmbiz.qpic.cn/mmbiz_jpg/KEyAvJTWH1oDDcAnoaYthMAraaVACbCrbUCSsHHuibKlEsY3ckFykUhUqydaI8WQ55XfUA5BoGZJAnQ4ZHcsiaBAasOjUEYnvqX8DUhNDdAwA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/73HCAFeXzF20SFy0DLZiaZBeibHKpuwUk05CXZmDqLVEJ48OT17wPxd2iaEhtEuiaIuZvj3smX6UpKttVbzNJleicOQ/0?wx_fmt=png)

云弈安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/73HCAFeXzF20SFy0DLZiaZBeibHKpuwUk05CXZmDqLVEJ48OT17wPxd2iaEhtEuiaIuZvj3smX6UpKttVbzNJleicOQ/0?wx_fmt=png)

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