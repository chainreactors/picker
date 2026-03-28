---
title: 【热点】从LiteLLM到Apifox：AI供应链投毒背后的工具链信任危机
url: https://mp.weixin.qq.com/s/tBcU3oNRdP8AJAelfMp2sg
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:46.212534
---

# 【热点】从LiteLLM到Apifox：AI供应链投毒背后的工具链信任危机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zfoRGB81MxOecxajTMzlczoxiapzWKriaHicxUgQul6o2iaBYE8ficbNCt59wxySQzvMZU7mRYcAbunbiaAAhrQTzIosymKEZ80iaa9HV1c9nrkYRE/0?wx_fmt=jpeg)

# 【热点】从LiteLLM到Apifox：AI供应链投毒背后的工具链信任危机

360数字安全

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

2026年3月，AI开发领域短时间内接连爆发LiteLLM、Apifox、ContextHub 三起供应链投毒事件，攻击者瞄准AI开发工具链展开多方位渗透，事件迅速发酵并在开发者社区及行业内引发高度警惕。

360 NDR（流量检测智能体）通过持续监测与深度分析发现，此次系列攻击手段覆盖Python组件官方包投毒、开发工具远程资源劫持、AI编码代理文档诱导，核心目标直指密钥、云服务凭据、K8s配置、Git凭证等开发者环境高价值资产，已波及互联网、金融、智能制造等多领域AI基础设施。

本次供应链攻击相关告警如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxPDy22ToBzN9WAlwU9nhqERziaicz5ibicSC214ejS5K5ianWEYGM1h7Bb7yhianA4W2GoVrqQnH4Qt9YZWibU0IdzMEuHOY7z87L2kps/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zfoRGB81MxNIxcyhWlk4dibQ9rm5Rgmb2tPS2yxgbOtaCciaZLlQopWMPG9MIEVLxVEa5t21w83bS1ATLUiaGVBWg0LXCF31s12HIHX2YgDzEc/640?wx_fmt=png&from=appmsg)

三起供应链投毒事件拆解

**同源异路的恶意执行链**

三起供应链投毒事件虽攻击载体、实施手段各异，但均构建起“植入-触发-窃取 -外传”的完整恶意执行链，核心作案逻辑高度一致——利用开发者对AI工具链官方渠道、权威文档的天然信任实现静默攻击，技术手段充分结合开发工具运行机制与AI特性，隐蔽性极强，且均呈现出主机端与网络端跨层行为联动的显著特征，这也成为识别此类供应链攻击的核心依据。

在**LiteLLM**事件中，攻击者先攻陷Trivy工具链窃取项目PyPI发布令牌，获得官方发布权限后，将恶意代码植入Python包的.pth 文件。该文件会在Python解释器启动时自动加载执行，无需开发者显式调用，随后恶意代码遍历～/.ssh/、~/.aws/等敏感路径，收集云凭据、K8s 令牌等核心信息，经AES-256+RSA-4096双重加密后，通过HTTPS回传至攻击者控制的models.litellm.cloud域名，还会植入后门进程实现持久化控制，其恶意版本 1.82.7/1.82.8在发布仅3小时内即触发敏感信息窃取行为。

**Apifox**事件则是典型的远程资源劫持攻击，攻击者劫持官方CDN域名cdn.apifox.com，将34KB的正常JS文件替换为77KB的恶意版本；当全平台客户端启动时，会自动加载该恶意脚本，脚本随即从非官方域名apifox.it.com动态加载第二阶段攻击载荷，最终收集SSH密钥、命令行历史等敏感数据，通过携带af\_uuid、af\_os等设备标识的HTTP请求外传至攻击者服务器，整个攻击过程依托工具正常启动流程完成，无任何异常提示，恶意脚本更是潜伏18天，造成大范围影响。

**Context Hub**的文档诱导攻击中攻击者利用AI编码代理对官方文档的信任，在项目文档中植入恶意指令，诱导Claude等AI模型在生成代码时，自动将恶意依赖包写入requirements.txt；一旦该代码被提交至代码仓库，下游所有开发者执行pip install时都会安装恶意包，实现供应链级别的规模化扩散，且该攻击方式成本极低，检测难度大幅提升。

工具链成攻击突破口！

**四大安全问题亟待重视**

此次LiteLLM、Apifox、Context Hub三起供应链投毒事件，并非孤立的安全事故，而是AI技术快速普及背景下，开发工具链安全体系滞后的集中体现，其背后折射出的多重安全问题：

**01**

**开发工具链信任体系成为攻击者主要突破点：**开发者对PyPI官方仓库、工具厂商CDN、官方文档库的天然信任，让这些本应是安全屏障的渠道沦为“攻击跳板”。LiteLLM恶意版本以官方身份发布、Apifox恶意脚本通过官方CDN分发、ContextHub恶意指令伪装成权威文档建议，这些内容均属于开发者环境中 “默认可信”范畴，常规安全策略会直接放行，让恶意代码轻松进入受信任环境。

**02**

**传统安全防护机制对AI供应链攻击的针对性严重缺失：**防火墙的核心关注边界访问行为，无法识别“合法应用发起的异常请求”，如Apifox客户端启动阶段对非常规域名的访问；基于特征的检测手段高度依赖已知恶意样本，对官方渠道分发的“无特征恶意文件”无能为力，如LiteLLM中被植入的.pth恶意文件；终端防护则容易将敏感文件访问、网络外联等攻击行为，误判为正常的开发操作，最终导致整个攻击过程全程“静默执行”，难以被及时发现。

**03**

**AI开发工具安全设计短板为攻击者提供低成本入侵路径：**当前AI开发工具处于快速迭代阶段，功能更新优先级远高于安全机制搭建，诸多安全漏洞暴露：LiteLLM未对PyPI发布令牌进行严格隔离导致令牌泄露；Apifox未启用Electron沙箱机制，且不当暴露Node.js系统级API，让远程加载的脚本具备系统级操作能力；ContextHub未对第三方文档进行安全解析和校验，让恶意指令有机可乘。这些设计疏漏让AI工具链安全防护成为行业空白。

**04**

**供应链攻击的危害已从“单点失陷”升级为“体系性暴露”**：开发工具链已深度嵌入企业研发全流程，一旦被突破，攻击者可从“开发源头”直接渗透，绕过生产环境所有防护措施。此类攻击不仅会造成企业高价值资产泄露，引发云资源被操控、数据库被篡改、核心业务受损等风险；若窃取到CI/CD令牌，还可篡改软件发布流程，形成持续攻击通道；而开源组件投毒、文档诱导攻击更具备供应链级扩散能力，易形成行业性安全危机。

尤为值得警惕的是，ContextHub所代表的“间接提示注入的供应链化”已成为AI时代新型攻击范式，攻击者无需入侵任何系统，仅通过伪造文档即可实现攻击，攻击面将随AI工具普及持续扩大，检测难度远高于传统供应链攻击。

应对方案

**构建全链路AI开发工具链安全防御体系**

360数字安全专家认为，在AI技术深度融入软件开发的时代，开发工具链的安全已成为企业数字安全的核心基石，单纯的单点防护已无法应对规模化、体系化的供应链攻击。

对于企业而言，开发工具链已深度嵌入研发全流程，一旦被突破，攻击者可直接从“开发源头”渗透，绕过所有生产环境的防护措施，成为企业安全体系的最大 “短板”。因此，企业亟需从紧急处置、技术防护、体系搭建等多维度入手，构建全链路、体系化的开发工具链安全防御体系，筑牢AI开发环境的安全屏障

**01**

**紧急处置**

面对已发生的LiteLLM、Apifox、Context Hub 供应链攻击，企业需第一时间开展应急处置，降低攻击影响，防止攻击者进一步渗透：

一是立即开展IOC排查，在企业网络日志中检索models.litellm.cloud、apifox.it.com、checkmarx.zone等恶意域名，同时检查文件系统中是否存在 litellm\_init.pth 等可疑文件，及时发现入侵痕迹；二是锁定工具安全版本，并开启哈希校验，防止安装恶意版本；三是全量轮换敏感凭据，避免攻击者利用已窃取的信息进一步入侵企业云资源、容器集群等核心资产；四是对AI生成代码进行全量检测，排查是否存在恶意依赖包，及时清除安全隐患。

***关键 IOC汇总：***

models.litellm.cloud

checkmarx.zone

apifox.it.com

apifox.it.com/public/apifox-event.js

apifox.it.com/event/0/log

apifox.it.com/event/2/log

cdn.openroute.dev

upgrade.feishu.it.com

system.toshinkyo.or.jp

ns.feishu.it.com

ns.openroute.dev

api.feishu.it.com

d.feishu.it.com

panel.feishu.it.com

**02**

**部署专业检测工具**

企业需摒弃传统的单一防护手段，部署具备行为分析、全链路检测能力的专业安全产品，实现对供应链攻击的早期预警、精准检测与全链溯源。

360NDR（流量检测智能体）的检测能力已落地供应链攻击防护，成为此次系列事件中的核心防护手段。该系统通过“主机行为+网络流量”的协同分析，精准识别供应链攻击的跨层异常特征。同时，360NDR融合流量分析与沙箱动态分析能力，搭配百亿级威胁情报赋能，即使是官方渠道分发的无特征恶意文件，也能实现精准检测与早期预警；还可存储原始攻击数据，实现攻击行为的可视化溯源分析，并与防火墙、终端防护等设备联动，形成“检测-预警-溯源-处置”的完整防护闭环。

目前，**360 NDR（流量检测智能体）已全面覆盖LiteLLM、Apifox、Context Hub等典型AI供应链攻击场景，可7×24小时实时监测异常外联、敏感信息读取、可疑执行链等关键行为，在攻击触发初期发出告警，大幅降低攻击危害。**

**03**

**安全左移**

短期的应急处置与技术防护只能应对已发生的攻击，企业要从根源上抵御AI供应链攻击，需推动安全能力左移，将安全防护融入开发、测试、部署全流程，构建全链路的开发工具链安全防御体系。

同时，企业需建立供应链攻击应急响应体系，制定针对性的应急处置预案，定期开展模拟演练，提升企业对供应链攻击的发现、处置、溯源能力，确保攻击发生时能够快速响应，将损失降至最低。

未来，360数字安全集团将不断完善供应链攻击防护能力，为企业提供从源头防控到全链防护的一体化安全解决方案，助力企业筑牢AI开发环境的安全屏障，守护智能经济时代的核心生产资料安全。

点击**【阅读原文】**查看AI工具供应链投毒完整报告。

往期推荐

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | **01** | ● 2026两会观察 | 周鸿祎为智能体人才培养献策，360先行落地 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585196&idx=1&sn=411d31527985da5cfb73f1beb83c429b&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **02** | ●  360龙虾卫士重磅上线：九大能力专治OpenClaw“裸奔” | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585414&idx=1&sn=eda1a5e0a9282e83255dfe33c7de4ab7&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **03** | ● IDC双报告首推：360以绝对实力护航每只“龙虾”安全 | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585375&idx=1&sn=e70a863eb3baac335080bdc9c4d0143a&scene=21#wechat_redirect) | |
| |  |  | | --- | --- | | **04** | ● 360安全龙虾「养虾速成课」正式上线ISC.AI学苑！ | | ► [点击阅读](https://mp.weixin.qq.com/s?__biz=MzA4MTg0MDQ4Nw==&mid=2247585434&idx=2&sn=9e145e933928722c36df13f6cdbd53dd&scene=21#wechat_redirect) | |

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

360数字安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pLEuriaaPnU2LObg7LSibTNuxCKqwibiahgWQqYS5faAYwjYz8VJXmYxaZCYbgZ8IHwM06bPpXD9nI8buP1lle7PyQ/0?wx_fmt=png)

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