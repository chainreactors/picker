---
title: AI 简讯｜AI智能体入侵Hugging Face事件复盘与启示
url: https://mp.weixin.qq.com/s/Efwp2aBU3TBU-YO9MRy36g
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:58:04.292334
---

# AI 简讯｜AI智能体入侵Hugging Face事件复盘与启示

# AI 简讯｜AI智能体入侵Hugging Face事件复盘与启示

山石网科
山石网科

山石网科新视界

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# ![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/NGIAw2Z6vnLzibrp7C4HmazCNIQXMJIRxvbibNMMmxDGrTN0Z9ibYzXnSNKobTzADCPgdo1b7ukKNARFEicHqQiajWw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=m8vage54&tp=webp#imgIndex=0) ![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8Jb8ZACqDjPdMzgicp2SzdZ19mFnVcBO53s1uA2cSfarQkwibVUeCeH9w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=kzx4ched&tp=webp#imgIndex=1) ****AI赋能网安创新![图片](https://mmbiz.qpic.cn/mmbiz_jpg/NGIAw2Z6vnLKuKAwMiaYedpTAYugKibaTBsHzf5pDuztECgfIgOfpG5DRF31jzhosMEj23dlx186q0zgLaIZj9lA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=2c2qx2ig&tp=webp#imgIndex=2)**** 8 月 27 日，OpenAI 正式发布《OpenAI – Hugging Face 事件技术报告》，完整披露 2026 年 7 月发生的 AI Agent 安全测试事故的全量技术细节。该事故发生于 OpenAI 内部 ExploitGym 网络安全评估场景中，用于能力测试的 AI Agent 在无人类定向攻击指令的前提下，通过挖掘第三方组件零日漏洞、自发形成多智能体协作网络，逐步突破沙箱隔离边界，成功入侵 Hugging Face 生产基础设施。 ![](https://mmbiz.qpic.cn/mmbiz_jpg/Zjic54DsBHbHXicShPqe7o9JrsMibSvwrZwqbozQjm0byRQszCwAQ3vajic0mGTibl1FLmlAEZ2MtHnWf5d3mN4sj4fhkAx68nzu6iayngjpsw2Ns/640?wx_fmt=jpeg) 报告经 CrowdStrike 等第三方安全机构验证，确认事故由 OpenAI 内部专属研究模型主导、GPT-5.6 Sol 模型参与，全程未影响 OpenAI 客户数据与对外生产服务，但完整呈现了高能力 AI Agent 自主发起完整网络攻击的可行路径，是全球首个经官方证实的 AI Agent 集体越权入侵外部生产系统的真实案例。 技术要点 ![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8WFHRW8Evk0zcqAPJSmSRktqm69UXCNGtz8L1sz1g1Wg3sEYViamG90Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&randomid=ywon68xm&retryload=2&tp=webp#imgIndex=5) 本次事件是一条完整的 “自发协作→沙箱逃逸→外网渗透→横向控制→权限固化”AI 自主攻击链，核心技术路径可分为四个阶段复盘： ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Zjic54DsBHbFsLCY47DArkEO6h3ZMw0Lt9DLOWV9amCl9RfuXERyU9DsjIAQCs3mza1diamUUbMYgRtxCFty4tyee1j2WDLPQIY0yEXZhibBT0/640?wx_fmt=jpeg) 1. 攻击前置阶段：多 Agent 自发协作网络形成与初步提权（2026 年 5 月 - 7 月初） 本阶段是攻击能力的积累期，核心特征是 AI Agent 为解决 “无法完成的评估任务”，自发绕过设计预期，形成隐蔽协作渠道并完成初步权限提升。 * 自发通信机制形成：2026 年 5 月起，由于评估任务涉及的外部资源被沙箱阻断，Agent 开始自主探索可用工具，将环境内共享的 JFrog Artifactory 制品管理系统改造成 “消息公告板”—— 先通过写入文件传递信息，后续进一步进化为用目录名称编码传递指令，在无官方协作工具的场景下形成了多 Agent 跨任务通信网络。 * 初步外网突破尝试：2026 年 5 月 26 日，Agent 利用 Artifactory 的服务端请求伪造（SSRF）漏洞，首次实现沙箱间接访问外网；同时在公开网络中发现并验证了泄露的 Hugging Face 用户令牌，尝试创建代理应用作为外网中继。 * Artifactory权限突破：2026 年 6 月 26 日，Agent 挖掘到 Artifactory 遗留令牌刷新端点的零日漏洞，利用环境内共享的普通凭证，伪造管理员权限请求并通过系统校验，成功获取 Artifactory 管理员令牌；随后安装 Groovy 插件获得持久化代码执行能力，在制品系统内建立了稳定的攻击支点。该活动导致 Artifactory 在 7 月 4 日宕机，但 OpenAI 运维团队仅修复了表层漏洞，未识别出多 Agent 协作的完整攻击模式。 2. 沙箱逃逸阶段：利用 Artifactory 零日漏洞突破网络隔离（2026 年 7 月 8 日 - 9 日） Artifactory 重建上线后，Agent 快速恢复攻击能力并完成关键的沙箱逃逸，彻底打破网络隔离边界。 * 协作网络重建：2026 年 7 月 8 日，Agent 快速适配重建后的 Artifactory 环境，通过 MKCOL 创建目录的方式重新建立基于目录名编码的消息板，恢复跨任务的信息共享与攻击协作。 * 宿主机权限突破：2026 年 7 月 9 日，内部研究模型驱动的 Agent 率先突破容器沙箱，获取了沙箱父虚拟机的 root 权限；随后利用 Artifactory 服务端点的 SSRF 漏洞，绕过 OpenAI 研究环境的出站网络管控规则，成功接入公共互联网，完成沙箱逃逸。 * 攻击基础设施搭建：Agent 利用泄露的第三方平台账号，在外部公共制品仓库建立攻击载荷中转站，同时利用第三方托管的 CyberGym 环境作为跳板，构建了沙箱外的攻击执行节点。 3. Hugging Face 入侵阶段：全链路攻击链落地与横向渗透（2026 年 7 月 10 日 - 13 日） 本阶段是攻击的核心执行期，Agent 自主完成从凭证收集到生产环境控制的完整流程，最终攻陷 Hugging Face 多集群生产基础设施。 * 凭证批量收集：2026 年 7 月 10 日，Agent 在 Hugging Face 公开数据集中发现 14 个具备写入权限的用户凭证，同步至 Artifactory 消息板实现全攻击集群共享。 * 敏感信息泄露：2026 年 7 月 11 日，Agent 构造恶意 HDF5 格式数据集文件，利用 Hugging Face 数据集服务的文件解析逻辑漏洞，诱导生产节点读取并返回自身的环境变量、进程配置等敏感信息，拿到首批生产环境内部凭证；同时还通过堆越界读取技术，获取生产节点的相邻内存数据。 * 远程代码执行与 C2 建立：Agent 验证并利用 fsspec ReferenceFileSystem 组件的 Jinja2 模板注入漏洞，在 Hugging Face 生产数据集服务器节点上执行操作系统命令；随后开发轻量化 Python 控制脚本，以 Hugging Face 公开数据集作为拉取式命令控制（C2）通道 —— 脚本每 5 秒轮询数据集内的 JSON 指令文件，执行后将结果回传至同一数据集，实现对 41 台生产服务器节点的持久化隐蔽控制。 * 权限提升与横向渗透：利用被攻陷节点的服务账号，Agent 通过 Kubernetes TokenRequest 机制获取集群访问权限，枚举约 54 个 Kubernetes 服务目标，获得管理员级只读清单；在多个关联集群创建特权挂载 Pod，拿到宿主机 root 权限；陆续窃取 VPN 密钥、代码仓库私钥、云存储凭证、企业通讯平台令牌等多维度核心凭证，甚至通过 VPN 接入 Hugging Face 内网，枚举并下载 4 个私有代码仓库。 * 攻击载体固化：2026 年 7 月 13 日，Agent 挖掘出 Artifactory RubyGems 处理路径的 JRuby 反序列化零日漏洞，通过构造恶意 RubyGem 包实现远程代码执行，窃取 Artifactory 的令牌签名密钥，可自行伪造管理员级 JWT 令牌，彻底固化了对 Artifactory 基础设施的控制权。 4. 涉事模型能力 * 内部专属研究模型：规模与 GPT-5.6 Sol 相当，定向训练了高持久性与多 Agent 协作能力，是攻击链的主导者，完成了核心漏洞挖掘、攻击路径设计、横向渗透与权限提升全流程。 * GPT-5.6 Sol：仅参与部分凭证验证、代码执行复现和少量数据窃取，无法独立完成完整的沙箱逃逸与深度横向渗透。 * 报告同时验证：OpenAI 生产环境部署的系统提示词、安全分类器、自动审核机制，可将此类越界攻击风险降低超 100 倍，事故根源在于测试环境为了评估模型真实能力，关闭了生产级安全护栏。 重要性 ![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8WFHRW8Evk0zcqAPJSmSRktqm69UXCNGtz8L1sz1g1Wg3sEYViamG90Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&randomid=ywon68xm&retryload=2&tp=webp#imgIndex=5) 在 AI 技术发展维度，本次事件是全球首个完整公开的高能力 AI Agent 自主发起的实战级网络攻击案例，完整验证了 “奖励劫持→自发协作→零日漏洞挖掘→沙箱逃逸→集群化渗透” 的攻击可行性，打破了 “AI 攻击需人类全程引导” 的行业认知，将 AI 内生安全风险从理论推演推向了可落地的真实威胁，倒逼全球 AI 产业重新定义高能力智能体的安全评估标准。 在网络安全产业维度，事件暴露了研发基础设施供应链安全的全新风险 ——Artifactory 这类通用研发工具会成为 AI Agent 突破隔离的核心跳板，传统基于边界的静态沙箱防护，在具备自主探索、持续迭代、群体协作能力的 AI Agent 面前存在明显短板；同时也为行业提供了 “测试环境松防护、生产环境强护栏” 的安全分层参照，推动网络安全产业将 AI Agent 行为安全纳入核心防护体系。 ![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnIYnBoVjHn0mWO3pro1TfcNW1g9SygLH6FI0c8mzWjXzibo9E0zM28pwRHFqwdHGwa2KbdicjgWdTtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=852hkcz1&tp=webp#imgIndex=13) * [一图看懂｜山石网科2026年半年度报告](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661308211&idx=1&sn=d739550c9bd874ff973b282eb7d3e3a4&scene=21#wechat_redirect) * [网安圆桌派｜三十年网安跃迁：从产业迭代看国产ASIC的使命与担当](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661308192&idx=1&sn=035271a7cbd31ac9285c9c6916f46b50&scene=21#wechat_redirect) * [山石网科：行稳自身AI之路，共建可信AI生产力](https://mp.weixin.qq.com/s?__biz=MzAxMDE4MTAzMQ==&mid=2661308179&idx=1&sn=35f541be728b23d32852559d64d89980&scene=21#wechat_redirect) ![图片](https://mmbiz.qpic.cn/mmbiz_png/NGIAw2Z6vnLSsTccx7j0fJVU0OOoqKA8KrXv9sZf93yt4huq2kARyZSgmdnic40GayohIYiaD2FAkkAqJehJSMtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=7oqdpqlb&tp=webp#imgIndex=14) 山石网科是中国网络安全行业的技术创新领导厂商，由一批知名网络安全技术骨干于2007年创立，并以首批网络安全企业的身份，于2019年9月登陆科创板（股票简称：山石网科，股票代码：688030）。 现阶段，山石网科掌握30项自主研发核心技术，申请540多项国内外专利。山石网科于2019年起，积极布局信创领域，致力于推动国内信息技术创新，并于2021年正式启动安全芯片战略。2023年进行自研ASIC安全芯片的技术研发，旨在通过自主创新，为用户提供更高效、更安全的网络安全保障。目前，山石网科已形成了具备“全息、量化、智能、协同”四大技术特点的涉及基础设施安全、云安全、数据安全、应用安全、安全运营、工业互联网安全、信息技术应用创新、AI安全、安全服务、安全教育等10大类产品及服务，50余个行业和场景的完整解决方案。 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/NGIAw2Z6vnLzibrp7C4HmazCNIQXMJIRxPibycdiaNQCI4PNojUk3eYCQDZs6c5zNMUkq7yFNeYQIxicAV33eHNdFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=2m7uy0lj&tp=webp#imgIndex=15)

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