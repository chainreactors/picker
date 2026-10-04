---
title: TraderTraitor扩大狩猎范围！不再只盯加密行业，API反向呼叫后门瞄准普通IT服务商
url: https://mp.weixin.qq.com/s/oE5or4z_is6xty6Bl2vfvw
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:34:53.860131
---

# TraderTraitor扩大狩猎范围！不再只盯加密行业，API反向呼叫后门瞄准普通IT服务商

# TraderTraitor扩大狩猎范围！不再只盯加密行业，API反向呼叫后门瞄准普通IT服务商

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

![Interview task from a GitHub repository containing a weaponized .terraform.lock.hcl file](https://mmbiz.qpic.cn/mmbiz/E3ZvvAXyiaibkW8Ql5aN4YaqiakjKWQHFhvC91MkLAB0SvuRQE40ubmBqNiaYcMoqoEmXGD3lsAcK0zDaic35OfibILawYvMGlMTficw4NPpMNDe1A/640?wx_fmt=other&from=appmsg)

导语

SentinelOne实验室最新威胁情报爆出重大变化：Lazarus旗下著名子团伙TraderTraitor（UNC4899），过去因Bybit、KelpDAO等数十亿加密盗窃案闻名于世。现在该团伙把武器链投向和加密货币完全无关的IT技术服务商。

团伙沿用经典假招聘社工套路，投放FLATROOF、ROOFDECK两套macOS专用后门。最特殊的C2设计：受害主机主动向外调用第三方公开API接收指令，黑客不主动连接受害者，防火墙很难识别外来攻击会话。传统基于“黑客IP主动连入”的检测逻辑大面积失效，DevOps、云运维、外包技术团队都已经进入目标靶区。

一、团伙背景：从Web3大盗转向更广攻击面

TraderTraitor隶属于朝鲜Lazarus集团，之前所有公众大案全部聚焦加密赛道：

Bybit 15亿美元多签钱包入侵事件

KelpDAO / LayerZero 2.92亿美元DeFi攻击

作案套路广为人知：LinkedIn伪装HR，投递带毒笔试题，攻陷开发人员终端，窃取云凭证入侵基础设施。

而本次新事件出现关键变化：

受害者是一家普通IT服务企业，业务完全不涉及加密货币。这意味着：TraderTraitor不再只为盗币，同时瞄准普通科技服务商，把中小型IT公司当跳板，横向渗透服务商的众多甲方客户，实现“攻破一家，收割一批企业”的供应链式攻击。

很多人以为：不做Web3就不用担心TraderTraitor。这个认知现在已经彻底过时。

二、核心技术亮点：反向API呼叫式C2（Don’t call us，we’ll call your APIs）

传统后门：黑客C2服务器主动连接受害主机，或者受害者主动连黑客自建服务器。防火墙、威胁情报可以拉黑黑客IP、域名阻断通信。

而 ROOFDECK / FLATROOF 这套macOS后门做了彻底改造：

1. 没有硬编码黑客私有C2服务器地址；

2. 被攻陷的Mac终端周期性主动访问公开第三方API、Nostr社交中继服务；

3. 黑客把控制指令、Payload存放在Nostr匿名事件、公开API返回内容中；

4. 受害者拉取公开接口数据，解析提取指令执行，窃取结果同样回写至公开社交中继。

流量全部是访问互联网公开服务，没有任何和黑客私有服务器的直接会话。防火墙很难标记为恶意流量。就算封禁一批中继节点，攻击者随时可以切换其他公开API作为新的指令中转站。

额外配套反取证能力：

支持进程杀死、文件下载上传、命令执行、环境探测；

内置沙箱检测，识别虚拟机、分析环境直接终止运行；

尽可能减少本地磁盘落文件，大量操作内存完成，降低静态查杀检出率。

三、完整攻击全链路：假面试 → macOS沦陷 → API后门驻留

Step1 假招聘社工投递恶意测试项目

攻击者LinkedIn伪装技术HR，瞄准DevOps、云运维、后端开发岗位。向求职人员发送Terraform项目、Python笔试题源码压缩包。

诱饵是看起来完整正规的IaC基础设施代码包，里面藏恶意脚本，专门针对macOS开发机。很多开发人员习惯在自己Mac电脑解压、调试笔试题。

Step2 开发者本地运行代码，终端被植入后门

运行测试代码之后，FLATROOF加载器落地，进一步释放ROOFDECK主后门，在macOS建立持久驻留。

重点：受害者可以是求职的外部人员。黑客攻陷求职者个人Mac之后，如果该员工入职受害企业，就直接带着后门进入企业内网；或者直接利用求职者机器当做跳板攻击求职者曾经任职过的公司。

Step3 受害主机轮询公开API/Nostr中继拿指令

中毒Mac定时访问Nostr等公开API，读取黑客预埋的指令，执行本地命令：收集环境变量、AWS/Azure/GCP云会话令牌、~/.ssh密钥、源码、内部配置文件。

Step4 窃取数据回传公开中继，伺机横向扩散

采集到的云凭证、密钥回写至公开中继。攻击者拿到云凭证之后访问企业云资源。如果攻陷的是IT外包服务商，就以此跳板去入侵服务商对接的数十家甲方客户。

四、中招之后可观测痕迹（macOS重点排查）

1. Mac终端进程频繁对外访问 Nostr社交中继API接口，业务完全没有使用Nostr相关业务；

2. 系统出现无业务来源的周期性出站HTTPS请求，访问大量陌生公开第三方API；

3. 从可疑Terraform、Python笔试题压缩包执行过后的Mac主机，出现未知守护进程；

4. 发现无来源LaunchDaemon / LaunchAgent持久化项，名称伪装成系统程序；

5. 大量读取`~/.ssh`、云SDK凭证文件、Terraform配置文件的异常行为。

提示：该系列是macOS定向后门，主要针对苹果开发工作站，服务器Linux、Windows不是主要目标，但开发者Mac是入侵整个云基础设施的突破口。

五、企业&个人开发者防御建议

📌研发、DevOps个人开发者（macOS用户必看）

1. 所有面试笔试题、外部提供的Terraform/Python源码，必须在隔离虚拟机运行，禁止在日常工作Mac直接解压执行；

2. 不要在个人求职设备存放企业云密钥、SSH私钥；公私开发环境做物理隔离；

3. 留意Mac后台进程，如果出现频繁访问Nostr中继，非业务场景立刻排查。

📌企业安全运维加固要点

1. 重点防护：外包、IT服务商、云运维团队，他们是TraderTraitor新的重点目标，不只是Web3公司才需要警惕；

2. EDR/XDR开启macOS行为检测：监控异常LaunchAgent/LaunchDaemon驻留，监控非业务访问Nostr中继API；

3. 云侧：开启云凭证异常使用告警，陌生IP、陌生设备调用IAM、S3存储桶立刻告警；

4. 招聘流程：对外来求职者，禁止接收需要本地运行脚本的笔试题，尽量提供在线沙箱环境做笔试考核；

5. 威胁狩猎思路：不要只拉黑黑客私有C2IP，重点检测「业务无关程序大量轮询陌生公开第三方API」这种异常行为。

📌疑似入侵应急处置

1. 立刻断开被感染Mac的网络，防止云凭证继续泄露；

2. 清除可疑LaunchAgent/LaunchDaemon持久项，全盘检索未知守护进程；

3. 全部云平台轮换所有云会话令牌、AccessKey，SSH密钥全部重新生成；

4. 核查云平台操作日志，确认攻击者是否已经访问、修改云资源；

5. 全团队安全宣导，警惕LinkedIn假HR投递笔试题的社工套路。

文末总结

TraderTraitor的演变给行业敲响警钟：

第一，攻击目标不再局限加密货币行业，IT外包、云服务公司成为跳板猎物；

第二，C2战术进化，使用公开第三方API、社交中继做指令通道，传统黑名单封禁手段效力大幅下降；

第三，入侵入口不是服务器漏洞，而是开发者的个人Mac工作站，一道面试笔试题就可以打开整个云环境的大门。

很多企业安全防护把重心放在服务器，却忽略研发人员本地macOS终端风险。攻击者不需要攻破你的公网服务器，只需要攻破一个开发人员的电脑。

转发给DevOps、后端、云运维、HR招聘同事，警惕TraderTraitor假面试+API反向呼叫新型后门！

**加入知识星球，可获取权益**

一、"全球高级持续威胁：网络世界的隐形战争"，总共26章，为你带来体系化认识APT，欢迎感兴趣的朋友入圈交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblj6Qa1c5j4iaSxNtaWyMmOrsJ7WJafnTfxff3PA2nhkdQL7AyqtkzhPaoCicbu2FWhIAe1y02o5icTMZiaiaD1T4WXgf5TRsAVyEFU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibm0l6wIBoUfic1Rxr77k9bUlBJeO2gkADWstEJ1u2JGkNGd6Td2RFTWbUh4PWaibl2jEpIAZnNsBUjCX8D6Xrlmuw44kpnsx1H34/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibnOts86xJKqAicF3fEIc4dnBIEm1bCBvX9PhLYRgIIpzQRnfnkanibo4N4ogOicxz4HEc3rFqIBscWYQdYZpL8Ucu7kbX0aRicnZjk/640?wx_fmt=png&from=appmsg)

二、为什么加入？

职场瓶颈期找不到突破方向？安全项目落地缺成熟方案？面对APT攻击、勒索病毒不知如何构建防御体系？

三、在这里，你能获得的不只是资料包，而是直接对接行业专家的「私人顾问服务」

✅ 职业发展「精准导航」

 1v1简历优化：针对安全岗（渗透测试/安全运营/合规等）拆解JD，突出核心竞争力；

 晋升避坑指南：从工程师到安全负责人，分享晋升路径，避开「技术强但管理弱」的晋升陷阱；

 技能栈规划：根据你的基础（应届生/3年经验/资深专家）定制学习路线，比如从0到1学SOC安全建设、APT威胁狩猎。

✅ 安全方案「对症开方」

 实战方案库：含医疗/制造业/等行业的勒索防御、数据安全合规、供应链安全加固方案（附落地工具清单+成本测算）；

 架构设计咨询：小到EDR选型，大到零信任体系搭建，提供「预算效果」平衡的最优解（已帮10+企业节省40%防护成本）。

✅ 圈子资源「直接对接」

 大厂安全负责人拆解真实案例（如某支付公司攻防对抗的实战复盘）；

四、适合谁？

 想突破职业天花板的安全工程师/架构师；

 需快速落地安全项目的企业负责人；

 关注行业动态的安全爱好者或IT从业人员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkJsTBMez9zJVBx2GkJZX37f7O4FrIibRh5t4A452yETKicDN4YVqlC8IFp7j3rb1FtERwaHNkNFWq93j1mMPnGemzXIv4NGaUSU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaibkfA9XDdSgS2UFvFl6eje0BXEeKlZScMVtCNVBSqD7DzicMw2yPB4iahzUA3H97RvicGicibqricFoEQQey8l2qRVdeUHoYRcRDMbl8Q/640?wx_fmt=png&from=appmsg)

**喜欢文章的朋友动动发财手点赞、转发、赞赏，你的每一次认可，都是我继续前进的动力。**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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