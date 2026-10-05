---
title: GHAPPIER新型加载器曝光！带合法签名的投毒NPM包，关联PolinRider供应链APT
url: https://mp.weixin.qq.com/s/jcgnv21qqv9WxtOgv6KxTA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:54:52.362574
---

# GHAPPIER新型加载器曝光！带合法签名的投毒NPM包，关联PolinRider供应链APT

# GHAPPIER新型加载器曝光！带合法签名的投毒NPM包，关联PolinRider供应链APT

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/E3ZvvAXyiaiblE20mM8YRicBibj5iakpFuMsBl9rcTialAMKALH2qWtcHvO139xC9Kgj8QjMw0X1mYibtkzKNRahKp3mxiaicNMVdfEp9I7Ry9CfQRCU/640?wx_fmt=png&from=appmsg)

导语

CloudSEK安全团队披露全新未公开供应链攻击行动GHAPPIER。攻击者窃取开发者仓库权限，滥用NPM「可信发布」OIDC机制，给恶意包带上完整有效的官方来源证明签名，骗过常规供应链校验。

恶意代码仅藏在大文件末尾一行，不会在安装阶段触发，启动业务服务才激活四阶段载荷链，最终后门运行后立刻自删除磁盘文件，本地杀毒全盘扫描找不到任何恶意样本。该攻击横跨65个GitHub仓库、22个账号，部分样本技术特征与朝鲜APT PolinRider行动高度重合，甚至直接把以太坊区块链当做C2指挥信道。

前端、全栈研发团队务必警惕：有可信签名，不等于代码安全。

一、事件回顾：105分钟的仓库劫持

本次攻击的突破口为开源NPM包`@dforge‑core/dforge‑mcp`。

攻击者拿到该项目仓库推送权限，整个入侵操作窗口仅仅105分钟：

1. 修改3行CI配置，配置main分支每一次代码推送自动触发发布流水线；

2. 14分钟后改写GitHub Actions工作流，实现无人值守自动发包；

3. 发布恶意版本`0.2.21`，该版本作为最新包在NPM registry存活35分38秒，随后维护者紧急回滚，发布干净版本`0.2.22`止损。

最颠覆认知的一点：这个恶意版本拥有完整合法provenance来源签名，Sigstore公开日志完整记录构建信息。

签名只能证明「这个包是从哪个CI流水线构建出来」，无法保证流水线内的源代码本身没有被篡改，大量依赖签名做安全校验的防护手段直接失效。

二、GHAPPIER加载器完整攻击链路

Step1：恶意代码隐身埋入

攻击者没有大面积篡改源码，仅仅在一份99KB大型配置文件的第3320行插入一行恶意代码，肉眼翻阅代码极难发现。

重点陷阱：npm install安装包时不会执行恶意代码！

只有业务程序启动MCP服务的时候，这一行代码才会触发整套四阶段载荷链，很多企业只在安装阶段做沙箱扫描，完全漏掉风险点。

Step2：四阶段载荷链式执行

1. 第一阶段：埋入的单行代码被触发，启动第一阶加载器；

2. 第二、三阶段：逐层解密、拉取后续载荷，内存完成解析执行；

3. 第四阶段（最终RAT远控）：程序运行瞬间立刻自我从磁盘删除。

中招主机磁盘不会留存任何恶意exe/js，运维全盘检索恶意文件什么都找不到，极易误判系统没有被入侵。研究人员测试，即便恶意包已经下架，攻击链路的后端服务在事发5天后依旧保持活跃状态。

Step3：区块链充当C2指挥（PolinRider标志性手段）

安全团队在另一个受害仓库发现同源样本，确认和PolinRider行动技术特征匹配：

恶意载荷不硬编码任何域名、IP地址！

黑客把C2服务器地址写进以太坊一笔空交易的20字节地址字段，只需要花费约0.2美元转账。

恶意程序运行后主动读取链上公开交易数据，解析出控制服务器地址。

没有域名、没有固定服务器IP，安全厂商无法简单封禁域名/服务器来切断通信，溯源和阻断难度极大。

攻击链路：以太坊空交易 → 读取链上数据拿到C2地址 → 建立远控会话，接收黑客下发指令。

攻击集群规模

GHAPPIER行动已经波及65个公开GitHub仓库，22个开发者账号，73份被感染文件，攻击者主要通过窃取开发者本地缓存Git凭证，向大量无关仓库批量注入恶意代码，完成大范围扩散。

三、3个极易踩坑的认知误区

❌误区1：NPM Provenance可信签名=包安全

✅真相：签名只记录构建流水线，不能校验流水线输入的源代码是否被篡改。攻击者拿到仓库推送权限，产出的恶意包一样可以拿到合法签名。

❌误区2：安装时扫描依赖，就可以拦截供应链投毒

✅真相：GHAPPIER不在install阶段触发，业务服务启动才激活载荷，仅做安装期沙箱完全不够。

❌误区3：卸载恶意包，全盘查杀文件就能确认安全

✅真相：最终远控载荷执行后自删除磁盘本体，磁盘找不到恶意文件，入侵痕迹留在内存与系统日志中。

四、研发团队自查，出现这些现象高度警惕GHAPPIER家族

1. 项目引入`@dforge‑core/dforge‑mcp`版本`0.2.21`，建议立刻锁定版本至安全的`0.2.22`；

2. 项目大体积配置文件末尾，出现陌生单行混淆JS代码；

3. GitHub Actions工作流被不明人员修改，main分支推送自动开启无人值守npm发布；

4. 业务MCP服务启动后，主机内存出现未知远程shell会话，磁盘找不到对应恶意脚本；

5. 终端出现访问以太坊节点API，读取链上交易数据的异常网络行为；

6. 开发者本机Git缓存凭证泄露，出现非本人的代码提交记录。

五、企业研发安全加固方案

📌依赖管理

1. 排查项目依赖，立即移除/锁定`@dforge‑core/dforge‑mcp@0.2.21`，升级至0.2.22；

2. 不要单纯依靠provenance签名作为唯一安全判断依据，签名只能作为辅助参考；

3. CI流水线不要仅在install阶段扫描，业务代码启动运行阶段也要开启动态沙箱检测；

4. 重要项目锁定依赖版本号，禁止自动拉取latest最新版本。

📌GitHub仓库权限防护

1. 严格管控仓库push推送权限，最小化授权人员；

2. 保护开发者本地开发主机，防范窃取Git缓存凭证的恶意扩展、恶意包；

3. 审计Actions工作流，禁止随意开启「代码推送自动无人工审核发包」；

4. 开启提交审核，main分支代码必须经过PR评审，禁止直接push到主分支。

📌终端&运行时检测

1. EDR重点监控：服务启动瞬间内存生成未知远程Shell，进程无对应磁盘文件；

2. 告警业务进程异常访问以太坊链上API接口；

3. 监控GitHub Actions配置文件的非正常修改行为。

📌疑似中招应急处置

1. 立刻停止受影响业务服务，隔离服务器，导出内存镜像取证；

2. 排查Git提交记录，定位恶意代码注入的提交；

3. 重置所有开发者Git、仓库、NPM账号令牌；

4. 全盘审计内网横向访问痕迹，即便磁盘找不到恶意文件，也必须排查内存会话、网络日志。

文末总结

GHAPPIER这起供应链攻击敲响警钟：攻击者已经学会利用开源生态本身的安全机制来作恶。

合法来源签名、正规开源仓库、NPM官方分发渠道，三者叠加依旧可以产出恶意包；再搭配业务启动才触发+载荷自删+以太坊区块链C2三重反检测手段，传统静态防御几乎全部失效。

供应链安全不能把希望完全寄托于上游工具的签名机制，代码评审、运行时动态检测、开发机安全三者缺一不可。

转发给前端、全栈、DevOps研发同事，警惕新一代NPM供应链APT攻击！

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