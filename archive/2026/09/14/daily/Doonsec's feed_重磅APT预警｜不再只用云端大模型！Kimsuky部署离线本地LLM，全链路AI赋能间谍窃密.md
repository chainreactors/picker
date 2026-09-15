---
title: 重磅APT预警｜不再只用云端大模型！Kimsuky部署离线本地LLM，全链路AI赋能间谍窃密
url: https://mp.weixin.qq.com/s/7xYDnAMQlckPHTXVGDoqaw
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T07:00:46.866292
---

# 重磅APT预警｜不再只用云端大模型！Kimsuky部署离线本地LLM，全链路AI赋能间谍窃密

# 重磅APT预警｜不再只用云端大模型！Kimsuky部署离线本地LLM，全链路AI赋能间谍窃密

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

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibl7vFXMbkrNPZt5uPctXlKMN359iaDr12yiciahoG2Cgd0e5598LRokwZMIB1IjLJaxVJEzsPgM5Z3tjwxsZTVmm8Pdu25bupUNgU/640?wx_fmt=png&from=appmsg)

导语

过去大家看到AI用于网络攻击，大多是黑客调用ChatGPT、Claude等在线云端大模型，生成钓鱼邮件、伪造文档。

韩国安全厂商Genians最新披露GitPower行动，朝鲜侦察总局下属APT Kimsuky（金素基 / APT43） 已经完成整套离线AI攻击环境搭建：部署Ollama、GPT4All本地大模型，配置RAG检索增强体系，搭配Cursor AI代码助手、Whisper语音转文字工具。

所有AI运算全部在黑客自己的服务器本地完成，数据不会流出到第三方云端，不会留下云端对话日志。从生成高仿真鱼叉诱饵、编写恶意代码，到入侵后自动解析窃取到的涉密文档，实现间谍工作全流程AI提效，目标瞄准外交、军工、科研、虚拟资产金融行业。

一、APT的离线AI武器栈：全套开源工具本地跑

安全人员在Kimsuky攻击基础设施中，捕获大量工具运行痕迹，整套环境全部基于公开开源AI软件组装而成，不需要自研大模型，落地门槛并不高：

1. 本地大模型运行层：Ollama / GPT4All / Msty

在黑客受控服务器本地部署开源大模型，不需要访问外网AI服务，所有输入输出留在攻击者内网。

2. RAG检索增强知识库（LocalDocs）

把入侵后偷来的合同、报告、会议纪要批量导入本地知识库。AI自动对海量窃取文档做摘要、提取关键情报，不用黑客人工逐条阅读。

重大风险：受害者的涉密资料不会上传外部AI平台，外部厂商完全拿不到任何访问日志，溯源取证难度极大。

3. AI代码开发工具 Cursor

大量日志痕迹显示黑客高频使用Cursor，用来辅助编写、迭代PowerShell、RAT远控恶意载荷，审阅生成的恶意输出，加速木马开发。

4. 语音处理Whisper（faster‑whisper）

窃取录音、会议音频之后，自动批量转写成文字，快速挖掘音频里面的机密谈话内容。

5. AI Agent开发框架：LLamaSharp、Semantic Kernel

用于把各个AI组件串联，尝试实现部分攻击任务自动化。

Genians研判：目前该团伙还处在技术验证迭代阶段，并没有从零训练专属大模型，主要复用市面上成熟开源AI工具，搭建属于自己的攻击工作流。

二、攻击链路升级：AI贯穿钓鱼投递→入侵→情报处理完整链条

1、鱼叉诱饵阶段：AI生成以假乱真业务文档

不再简单复制盗用旧文档。针对虚拟货币、金融行业目标，利用本地大模型生成高度逼真的报告、合作协议、投资分析文档。

文字行文流畅，格式完整，接近真实办公材料，降低受害者警惕。诱饵一般打包进ZIP压缩包，内部放置伪装PDF图标的LNK恶意快捷方式。用户双击看似文档的文件，后台PowerShell载荷静默执行，从GitHub仓库拉取AsyncRAT远控后门。

2、入侵驻留：GitHub充当C2指挥通道

GitPower行动标志性战术：把加密的恶意载荷伪装图片存放在公开GitHub仓库，受害主机定期拉取更新载荷，GitHub的正常业务流量可以很好掩盖攻击行为。

3、数据窃取之后：本地RAG自动消化海量涉密材料

拿到内网大量文档、录音、聊天记录之后，直接喂给本地RAG知识库：

自动筛选高价值情报，提取关键人名、项目、资金、谈判信息；

音频录音批量转文字；

对海量文件做归类整理，极大减少黑客人工分析工作量。

关键风险：所有这一切全部离线完成，没有任何云端日志可以追踪。

4、额外探测行为

攻击中还会主动探测受害者泄露信息：包括虚拟资产钱包、Gmail账号、网站注册历史，用来进一步扩大后续社会工程攻击范围。

三、为什么“本地离线AI攻击”比云端AI更棘手？

1. 无云端审计痕迹

黑客使用ChatGPT等在线大模型，会在服务商侧留下prompt对话记录，可作为威胁线索。而本地Ollama整套运算发生在黑客自己服务器，外部完全看不到交互痕迹。

2. 数据不会外泄，受害者涉密材料不会流向第三方AI服务商

传统云端AI，上传的涉密材料会进入大模型服务商系统；离线RAG只在攻击者内网流转，外部无法通过AI平台发现情报泄露。

3. 攻击迭代速度变快

借助Cursor等AI编码工具，恶意脚本、载荷修改调试效率大幅提升，快速生成多版本免杀样本。

4. 诱饵质量持续提升

本地大模型可以结合已经窃取到的受害者业务背景，定制高度贴合目标业务场景的钓鱼文档。

四、企业检测与防御实操建议

Genians安全中心特别提示：面对AI生成诱饵，只做文档关键词静态检测效果越来越差，防御重心要转移到行为检测、威胁狩猎（EDR行为视角）。

🛡️安全团队落地要点

1. 终端威胁狩猎重点监控行为

警惕外来ZIP压缩包内部的`.lnk`伪装文档快捷方式；

监控PowerShell从GitHub raw地址下载脚本、载荷的异常外联行为；

识别AsyncRAT远控家族相关IOC，关注计划任务持久化行为。

2. 邮件网关防护

针对外交、军工、科研、区块链金融等高风险部门，强化鱼叉邮件过滤；

警惕附件为zip，内含PDF/Word图标的LNK快捷文件，这类是GitPower行动高频载体。

3. 不要只靠文档内容检测钓鱼

AI生成的文档语法、格式高度仿真，传统关键词匹配容易失效；优先看附件类型、文件后缀、文件元数据、文件来源链路。

4. 敏感数据管控

高价值涉密文档增加水印、权限最小化；一旦被窃取，黑客可通过本地RAG快速解析全部信息。

👨‍💼员工安全提示

1. 收到陌生邮件压缩包，优先解压看后缀，不要双击看上去是PDF、Word实际后缀为`.lnk`的文件；

2. 来源不明的合作报告、投资分析、行业简报，务必通过电话、官方渠道二次核验发件人身份。

五、安全启示

AI赋能攻击已经进化到新阶段：不再仅仅用来写钓鱼邮件，黑客开始搭建完整离线AI作战环境。

开源大模型门槛持续下降，APT可以把整套AI能力私有化部署，摆脱对ChatGPT等外部在线服务的依赖，情报处理、恶意代码开发都在自己内网闭环完成。

这就意味着，过去依赖“抓取云端AI日志”的溯源思路会逐步失效。安全防御需要从“识别文档内容真假”，转向监控文件执行行为、异常外联、恶意持久化动作。

文末互动

你们现在的EDR有没有针对LNK+GitHub下载载荷这类行为做告警？怎么看待本地大模型被APT滥用的风险？欢迎评论区交流。

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