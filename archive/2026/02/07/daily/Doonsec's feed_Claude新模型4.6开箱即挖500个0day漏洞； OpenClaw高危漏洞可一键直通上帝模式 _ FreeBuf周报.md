---
title: Claude新模型4.6开箱即挖500个0day漏洞； OpenClaw高危漏洞可一键直通上帝模式 | FreeBuf周报
url: https://mp.weixin.qq.com/s/5Z81R1hoBFpXbd6LG_n9ug
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:29.094834
---

# Claude新模型4.6开箱即挖500个0day漏洞； OpenClaw高危漏洞可一键直通上帝模式 | FreeBuf周报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymyA0AYWle3Wnao3wWyHqsDzMGH37D4XINGFb1Us09fC8ibRIH5cvgDSw/0?wx_fmt=jpeg)

# Claude新模型4.6开箱即挖500个0day漏洞； OpenClaw高危漏洞可一键直通上帝模式 | FreeBuf周报

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

各位 Buffer 周末好，以下是本周「FreeBuf周报」，我们总结推荐了本周的热点资讯、一周好文，保证大家不错过本周的每一个重点！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJ1UiaObonmWJbuLyoLXdutZ6T0GL6AXwFA0IHVJ9Tl93JicaeTmN55VJBw0JKrJg4sQXdypbdzqibg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

🎯Claude新模型4.6：开箱即挖500个0day漏洞，源代码审计即将颠覆

**🤖****一键触发漏洞：OpenClaw远程代码执行漏洞分析**

🌩️从凭证到云管理员仅需8分钟：AI加速AWS攻击链

💻微软将默认禁用NTLM协议，推动更安全的身份验证体系

🔢研究人员发现341个恶意ClawHub技能窃取OpenClaw用户数据

🔋暗网现新型OT攻击框架，能源基础设施面临威胁

⚔️AI扩大攻击面，大国博弈引发安全新挑战

🛡️TAMECAT 恶意软件曝光：APT42 无文件后门锁定国防高官

💽隐形入侵者：Linux平台"ShadowHS"恶意软件武器化Hackshell工具

🛠️2026年顶级AI红队测试工具全景解析

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5NY7KgXpwrAo5WHiaX2SOibeoicce3vxyZozGALjYSLtYPrDiceL0UV2D3A/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

Claude新模型4.6：开箱即挖500个0day漏洞，源代码审计即将颠覆

Anthropic发布Claude Opus 4.6模型，其网络安全领域表现亮眼，在无专门指令和领域知识的沙箱测试中，凭借常规工具挖出 500 余个经验证的未知高危零日漏洞。为防范能力滥用，Anthropic 新增六套网络安全探测机制，未来或上线实时拦截系统。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0badQZwAtPSIox3iaSuQdgFDHicV9zzyDIvt4Pkqre36icQ4h18s1zRUqiblyfI9BFE4PFks0LCHMwoI2KYQ5aVgcOtXCtsEDicEs4/640?wx_fmt=jpeg&from=appmsg)

一键触发漏洞：OpenClaw远程代码执行漏洞分析

开源AI助手OpenClaw曝高危漏洞，攻击者通过恶意链接可远程执行任意命令，CVSS评分9.8+。漏洞源于未验证URL参数和自动传输令牌，已紧急修复。建议用户立即升级并加强权限管控。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38SgoPHsqlGnJqsib3bWOXwJDhLia49Q2lnfPQ00POuYgLMrfibyPcCYj4n4ZoN784lUwsibEiaDibibO9VQ/640?wx_fmt=png&from=appmsg)

从凭证到云管理员仅需8分钟：AI加速AWS攻击链

###

AI辅助攻击者8分钟内完成AWS云攻击链，从凭证窃取到GPU资源滥用，利用LLM加速权限提升与横向移动。暴露凭证与宽松权限是根源，防御需AI快速响应与最小权限原则。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icfgFySDVR8vQfO3iablplDYYj7TOGLxnSq8I8jZ3M9qzxiaITaHParlZ8Nbficmzr8I85hQOPLc7arg/640?wx_fmt=png&from=appmsg)

###

微软将默认禁用NTLM协议，推动更安全的身份验证体系

###

###

###

微软将分三阶段逐步禁用存在安全漏洞的NTLM协议，2026年起减少使用并最终默认关闭，同时保留兼容支持。企业需审计NTLM依赖并迁移至Kerberos，确保安全过渡。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0Yx8wPricXxU8rjvwMkHL03C4OrBDwVkwthTiajpHwurrWcZsAicxOYWImOkzUpzEbvO2zarI5DiaV9DEIRiara4DVMq2pF11oGSfM/640?wx_fmt=jpeg&from=appmsg)

###

###

###

研究人员发现341个恶意ClawHub技能窃取OpenClaw用户数据

Koi Security审计发现ClawHub平台341个恶意技能，伪装成合法工具诱导用户安装窃密木马，窃取敏感数据。攻击针对macOS和Windows，利用开放上传机制传播。OpenClaw已新增举报功能，但AI代理的持久化内存加剧了安全风险。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2TOyOIvWianuXan2IU45dSzXxib4eR8otSibmnQ4lJ51DrNrAR2PTFL4sMUTzZRvWAIJia4sMCmqL3vb5eAbIgJKRzQ6kIXqkBz4I/640?wx_fmt=jpeg&from=appmsg)

暗网现新型OT攻击框架，能源基础设施面临威胁

###

###

###

###

###

暗网出现针对能源电网的工控攻击框架，疑似伊朗黑客组织开发，可精确操控配电系统，威胁关键基础设施安全，表明国家背景黑客攻击能力升级。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3xicJPPqx8MhleFF5gFIT5NXUbC76GPBBnEkAKyjS6hYsHtJQjpZAQqelsCGTqbHXQMg26gkwl0BYQr0hZ9ZxhibpFjUwxIiaugU/640?wx_fmt=jpeg&from=appmsg)

AI扩大攻击面，大国博弈引发安全新挑战

AI Agent普及加剧安全威胁，MCP协议漏洞扩大攻击面，中小企业防护能力不足。低资源攻击者利用AI规模化攻击，中伊两国AI能力增长引发安全担忧，技术差距缩小带来新挑战。

![The Rise of Autonomous Agents: Marc Benioff's AI Prediction - Fusion Chat](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2ZNW0TrX2icnaPfTPzu7hlWLgvl5m5ic6yUKwxyQEuNFNam14NTKp4h7xou96Wic7MDOe90uicVFcwMlRzo5maxolf96cuURxSNnE/640?wx_fmt=jpeg&from=appmsg)

TAMECAT 恶意软件曝光：APT42 无文件后门锁定国防高官

伊朗APT42组织使用模块化无文件后门TAMECAT，通过长期社会工程攻击高价值目标，窃取敏感数据。该恶意软件驻留内存，利用Telegram等隐蔽通信，绕过传统防御，凸显监控PowerShell和审查可信服务流量的重要性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0zWumDUJquyqeiciaLpexVqS75h1LvOibhxgt7ltO2tj2MhiaFPuN2uWUSXT1nAvwQ2L7bKpbX2OvTaB3DcqLXvLNlc3dWYemgu0Q/640?wx_fmt=other&from=appmsg)

隐形入侵者：Linux平台"ShadowHS"恶意软件武器化Hackshell工具

###

###

###

###

ShadowHS是高度隐蔽的Linux恶意软件，利用无文件加载器部署武器化hackshell，专为长期潜伏设计。其内存执行技术规避检测，具备后渗透功能，包括探测安全措施、清除竞争对手及隐蔽数据窃取。专业手法表明攻击者技能高超，非自动化攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icfgFySDVR8vQfO3iablplDYuXCES2E0OV27PG1FFicQGDmR25ictoo0DM5icQKyeOSejibiclK5o0SLk8w/640?wx_fmt=png&from=appmsg)

2026年顶级AI红队测试工具全景解析

###

###

###

###

AI红队测试已转向智能化，利用AI工具持续探测漏洞，模拟高级攻击。五大工具（Novee、Garak、Promptfoo、Giskard、HiddenLayer）覆盖技术、行为与供应链测试，集成开发与运维流程，提升防御韧性。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1NnY0Jj9xNWGovxfIWtohQ2To78SVYvPHaRXFAWW7CRak1SDyvRCA2ZibHXM1UXCQBA70gteCP5dGgrlemZnktRHNcTZ56pUTE/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS5Ce9OricKgAogLRlHYat9jaelbVESLOylPBnQQrU63TlHEs2zCbdNrKg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**本周好文推荐指数**

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icFibibPIGEfXsibI0C3or4BS59ZQ6EsSUehyHWzxq6tIFG5b5TmautNPF3E0YDL2xav0dFmmibp2oT0w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

###

红队武器库的十年演进：从Metasploit到AI辅助攻击的范式转移

###

###

### 网络安全攻防十年演进：从手工精准狙击到AI降维打击，攻击技术经历四次范式转移（手工→自动化→云化→AI），核心逻辑是攻击门槛降低与效率提升，倒逼防御体系从特征检测转向行为分析和AI对抗。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0nbOTySVrbtUSeugSnvczbEPGBR8u5aT5Q971JOtiazFI6ZX3UGmic2ialIez1s3bMAlo2Ol0bjFbY45k2u6IWicuxHRfP3F3ERic0/640?wx_fmt=png&from=appmsg)

###

揭开大语言模型的脆弱面：对抗攻击研究综述（一）

###

###

### 大型语言模型（LLM）面临对抗性攻击威胁，攻击者通过细微输入扰动诱导模型生成错误或有害输出。研究分析了攻击类型、访问权限及注入来源，强调需系统性防御策略确保LLM安全稳健。

### ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1Y4gQ9tmuvYtOzQyZo0bFmziaia6pnAdZpWoIq21ibujf1PvibMibV8lNh4HPTmArlNia1PryIibkOWTOArtm25vhqOehMDWSGibx8JVA/640?wx_fmt=png&from=appmsg)

基于 Sentence-BERT 的异常URL路径检测优化探究

###

###

###

### **Sentence-BERT优化恶意URL识别，通过语义向量化捕捉攻击特征，相比传统方法更高效准确。实验证明其可行性，后续将探索GNN等模型进一步提升效果。**

### ![1770274287_69843def79c0bca0bfb61.png!small?1770274287265](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0iaJKHtMiciagHUj7LUPDHTqcYX1kBlz0Kvkx6aIKXW0jwEp9kLQnqOeehwqCqlng2fLSZc91osFEhJfBK8kdVTUuYNqASe5mRCI/640?wx_fmt=jpeg&from=appmsg)

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

###

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)**

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38TJMDLxr9EPGGib49oQymrvRy7vGw1iakQXBCr1Udmia4dpY3JSWYEEicajmhhcyfHly9YYPIziaCVPOg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

内容含AI生成图片

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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
...