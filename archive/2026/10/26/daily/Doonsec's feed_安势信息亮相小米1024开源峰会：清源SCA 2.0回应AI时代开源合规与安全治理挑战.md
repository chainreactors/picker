---
title: 安势信息亮相小米1024开源峰会：清源SCA 2.0回应AI时代开源合规与安全治理挑战
url: https://mp.weixin.qq.com/s/uyqhFT3pKTqkhonC7VoYrg
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:02:07.082149
---

# 安势信息亮相小米1024开源峰会：清源SCA 2.0回应AI时代开源合规与安全治理挑战

# 安势信息亮相小米1024开源峰会：清源SCA 2.0回应AI时代开源合规与安全治理挑战

原创

安势信息
安势信息

安势信息

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# ![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/8TbJnTzbgyVnYiaTHtrSOnICwUEicbdBO72LWOFrPGBgIbT48XDtwk8Tia7OBPE68bnfcHMstmibTtCGbYTWWGsjLqVCW1hiavoCfJEnqa1iaZCZI/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

2026年10月21日，以「创造，正在发生」为主题的1024开源峰会·2026小米技术嘉年华在北京小米科技园举行。峰会由小米集团技术委员会主办、小米开源委员会承办、中国互联网协会数字文娱工作委员会协办。

小米开源委员会主席、基础技术平台部总经理张铎作开场致辞。开放原子开源基金会安全委员会标准工作组组长周峻松、小米机器人具身大模型研究负责人李庆、Zephyr蓝牙维护者孟令澳、openvela开源负责人杜超等业界专家，围绕软件供应链安全态势、VLA大模型、AI硬件开源生态等议题展开分享。

安势信息创始人薛植元带来《AI时代下的开源合规和安全治理挑战》主题演讲，系统剖析AI Coding浪潮下软件供应链安全与开源合规的新形势，并分享清源CleanSource SCA 2.0的应对思路与实践。

![2-2645798](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8TbJnTzbgyXV2d8jSNmpQKMwaeVSCmJ41jEBrqL8Hqcn9tXXRLLibABwXLMc9j2loicK8cLAPlVAvQIziapCl5EZu6IDCFo9AiabR5AppTuBeiaM/640?wx_fmt=jpeg&from=appmsg)

**开源世界正因AI变得更多、更大、更高频**

薛植元指出，AI辅助编码让软件产出速度大幅提升，开源组件的引入频率与依赖复杂度同步攀升，SBOM元数据的处理链条面临巨大挑战。与此同时，监管持续收紧——以欧盟《网络弹性法案》（CRA）为代表，SBOM正在迎来强监管时代，企业的风险处置时间被大幅压缩。新的挑战已经产生，SBOM治理需要进入2.0时代。

**发现风险越来越容易，解决风险为什么越来越难？**

演讲通过多个真实案例剖析行业痛点：

以Next.js授权绕过漏洞CVE-2025-29927（CVSS 9.1）为例，OX Security 2025年4月的客户样本研究显示，仅17.7%被判定为实际可利用。同一高危漏洞在不同产品、不同托管与部署方式下的真实风险差异显著——仅依赖CVSS评分会大幅增加无效修复成本，版本、代码与部署证据才是实际利用判断的支撑。

在SFC诉Vizio智能电视源码交付争议案中，识别出Linux内核、BusyBox等GPLv2组件只是第一步，企业仍需判断分发义务，核验源码、脚本与文件是否对应当前交付版本。

Shai-Hulud事件的启示在于，恶意风险与具体的npm发布版本强相关，恶意脚本在安装阶段即可触发。组件被引入、安装甚至运行后再扫描告警，风险早已进入环境——安全检查滞后于组件引入，是传统模式的根本短板。

![2-2892013](https://mmbiz.qpic.cn/mmbiz_jpg/8TbJnTzbgyWhKOI1MDea5SSISnia9II9aFw2f9ZMHaIMR1F3V0EbiaR2Gb7nIyicFcia2icj2iaeXiaNKRzqib5ksR0bUWSjForPZ8g5twUufKM6POw/640?wx_fmt=jpeg&from=appmsg)

**清源SCA 2.0：让检测能力主动适应软件**

针对上述挑战，薛植元介绍了清源SCA 2.0的核心跃迁——从「用户适应检测工具」转向「检测能力主动适应软件」，让每次检测都建立在正确的项目理解之上。

AI辅助创建检测任务：自动识别项目类型与构建方式，如依据pom.xml判定Maven多模块项目、检测私有npm仓库配置、发现Dockerfile时建议同步检测容器镜像；并整合Manifest/Lockfile、构建脚本与插件、私有仓库制品、最终交付二进制等多来源证据，形成完整的依赖视图，解决人工配置易遗漏、经验难复用、扫描覆盖不足等问题。

引入前完成策略判断：当Coding Agent提出候选依赖时，即调用清源完成版本风险、恶意情报、许可证与企业策略核验；符合策略的继续开发，不符合的阻断自动引入、推荐替代或提交审批，AI辅助完成依赖替换与代码修改后重新执行安全及功能验证，全过程保留证据。

全生命周期软件信任治理：SCA 1.0以扫描与报告为中心，结果停留在告警列表；SCA 2.0以业务治理为中心，覆盖「引入前决策—智能检测与构建—可信识别与研判—执行处置—复扫验证与交付」五个环节，实现安全、研发、法务与交付的协同闭环。

薛植元将SCA 2.0的核心价值概括为三点：**可消费**——结果不止于告警列表，按产品版本关联组件与证据，被业务持续使用；**可执行**——把结论推进到修复、整改与审批等真实业务流程；**可验证**——保留检测、研判与整改证据，支持复扫、复核与交付核验。

![2-2243799](https://mmbiz.qpic.cn/mmbiz_jpg/8TbJnTzbgyXI7kPexVlwWzchekhNrkDSDpH63yxxglgeO9o1z4kaR5kEH3MycfAlBWxTPxT5T9o5SZxuhZmicqWkynQ5tGOW1I9KEft2HtQg/640?wx_fmt=jpeg&from=appmsg)

软件风险治理的终点不是发现更多漏洞，而是在AI加速软件开发的时代守住安全与合规底线，让可信交付成为企业的新竞争力。安势信息愿与开源社区及产业伙伴合作共建，让每一行代码、每一个组件都更可信。

END

**关于安势信息**

上海安势信息技术有限公司（Sectrend）是全球先进的**AI+软件供应链安全治理解决方案提供商**。

核心团队来自Synopsys、华为、阿里巴巴、腾讯、中兴通讯等国内外知名企业。

安势信息始终坚持DevSecOps的理念和实践，以AI、多维探测和底层引擎开发等技术为核心，提供包括**清源CleanSource SCA（软件成分分析）、清本CleanCode Security Agent（新一代代码安全智能体）、清正CleanBinary (二进制代码扫描)、清流PureStream（AI风险治理平台）、可信开源软件服务平台、开源治理服务等产品和解决方案**，**打造AI时代下的代码安全能力建设**。

覆盖高科技、AI、互联网、ICT、汽车、高端制造、半导体&软件、金融等多元化场景的AI+软件供应链安全治理最佳实践。

欢迎访问安势信息官网www.sectrend.com.cn或发送邮件至 info@sectrend.com.cn垂询。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/8TbJnTzbgyUYLJIS07PoT6ImZds4q5uFsjuLknkn0qZCJX0S4mCAc9P1GALlyvsYbevYScdwX3hDouSiabibliaNXHnMG1emZtkdqxgojnic2dU/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibSWU7ian1thvBluqThXBxaKVctb2mLIQLnJ7NcCwc5NHH8Fr4Qq4JTAGvsYedrr22aOVmW6IOicibPhZPRNzkvqhg/0?wx_fmt=png)

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