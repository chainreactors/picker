---
title: 别让“养虾”变“养险”：基础环境漏洞有多危险？
url: https://mp.weixin.qq.com/s/Z-JzjkjTYRxwI0fs_73y6A
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:02:09.781333
---

# 别让“养虾”变“养险”：基础环境漏洞有多危险？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zfoRGB81MxNCfPOVH3Nlql6hHMby1AefouLPejEWKf6ysU5fBgWbibAUf3yPUaCJzdxXMVMN6YOZYicFncxK9HaFR6ISXAc8W0MTYHJxXqjJI/0?wx_fmt=jpeg)

# 别让“养虾”变“养险”：基础环境漏洞有多危险？

360数字安全

![]()

在小说阅读器中沉浸阅读

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/pLEuriaaPnU362NhLdPIDibrhibC5gfZR980tl5kIv8p6m64VHJU1n0pa7WajQ3lticuSKic1icw7xGRNGibTiaibdI7g7Q/640?wx_fmt=gif)**

OpenClaw这只小龙虾从一月底热度一路狂飙，一跃成为打工人、技术爱好者的专属“AI搭子”——自动整理文档、灵活调用工具、高效处理日常工作，凭实力让使用者直呼“真香”！

但在大家“养龙虾”AI提效的同时，隐藏的安全危机正悄然逼近：一个未及时修复的基础环境高危漏洞，可能让电脑沦为黑客的“后花园”，工作核心数据、个人隐私被一览无余！

**1**

**插件藏风险**

**AI搭子也会“泄密”**

近期，已有不少「养虾人」因此栽了跟头。某互联网公司运营人员为了提效，在电脑部署OpenClaw后，从技术交流群下载安装了一款“Excel自动汇总+邮件推送”的第三方插件。插件安装成功后，OpenClaw出现异常：开机自动启动且无法关闭，后台有不明网络请求和文件读写，桌面业务文档、浏览器密码等敏感信息被非法读取。

经安全技术人员排查确认，此次攻击的核心诱因，正是OpenClaw基础环境存在的安全漏洞：其在安装第三方插件时，会直接使用插件包描述文件中的名称字段拼接安装目录路径，却未对该字段做任何安全过滤，通过目录遍历漏洞绕开校验，将恶意程序非法写入Windows系统开机启动项目录。攻击者借此实现程序持久化驻留，电脑开机后后门程序自动运行，悄无声息地非法获取用户电脑内的各类敏感数据。

**2**

**危！**

**OpenClaw基础环境漏洞频发**

据360漏洞研究院相关专家介绍，该漏洞攻击门槛极低，无需用户进行复杂的技术操作，仅需诱导用户安装恶意插件即可完成攻击，且攻击行为隐蔽性极强，普通用户难以察觉。目前该漏洞已影响OpenClaw 2026.1.29-beta.1至2026.2.1之间的所有版本，已有大量用户因此遭受不同程度的信息泄露和系统安全问题。

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxN2O1vQQnYuLvH81Lw0ORqdsB055RmSM9FgQQsa4EsWsKhAic815ebGibV5JJf5N0LJeFxHvibowkGPeDXPvaqZIQLdxb4O17CH0w/640?wx_fmt=png&from=appmsg)

事实上，这只是OpenClaw基础环境漏洞风险的冰山一角。截至3月13日，国家信息安全漏洞库（CNNVD）通报OpenClaw累计82个漏洞，其中高危及以上级别占比达40.02%。这些漏洞遍布网关路由、工具执行、技能加载等核心模块，攻击门槛低、利用性强，一旦被黑客利用，轻则导致个人隐私泄露、电脑被远程控制，重则造成企业核心数据丢失、业务系统瘫痪，带来不可逆的损失。针对近期OpenClaw被曝出的WebSocket共享认证越权漏洞，360已成功复现该漏洞并验证了危害。

但对于普通用户而言，应对OpenClaw基础环境漏洞更是难上加难：多数用户缺乏专业的漏洞识别能力，难以发现隐藏在智能体运行环境中的潜在安全隐患；即便侥幸发现漏洞，也因无明确、可落地的处置方案，无法及时化解风险；更值得警惕的是，OpenClaw漏洞持续更新，用户难以实时跟进漏洞动态，即便升级版本也可能遭遇新的漏洞问题，使得OpenClaw的基础环境漏洞，成为悬在每一位“养虾人”头顶的“达摩克利斯之剑”。

**3**

**360龙虾卫士**

**一键扫描，精准修复环境漏洞**

就在大家对OpenClaw又爱又怕，想享受AI便利却忌惮安全风险时，360推出专为OpenClaw等“龙虾”智能体打造的专属安全防护方案——360龙虾卫士，以精准漏洞扫描核心能力直击基础环境漏洞痛点，为OpenClaw筑牢基础安全防线，让每一位用户都能安心“养龙虾”、放心用智能。

![](https://mmbiz.qpic.cn/mmbiz_png/zfoRGB81MxMUSW8OgPYya1YFiax8qUulbPeuH6RaI30XIcZd9D2uEGJ4RBq4mQlI7tO0VziakC005zsFvu4s8x0FcPvSPUcjIGhvDDwg5nZqA/640?wx_fmt=png&from=appmsg)

不同于传统安全工具只报漏洞、不教解决的“甩手掌柜”模式，360龙虾卫士的漏洞扫描更注重“可落地、易操作”的处置方案。平台会实时同步国家信息安全漏洞库与OpenClaw官方安全公告，完成漏洞库动态更新和处置逻辑持续优化，针对扫描发现的每一个基础环境漏洞，不仅会清晰标注危害等级、影响版本、波及模块，还会配套通俗易懂的一步式处置建议，哪怕是零基础的普通用户，也能不求助技术人员，自行快速修复漏洞，彻底降低基础环境漏洞防护的操作门槛。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zfoRGB81MxOibkHthsPDbLq5m1zNyyoXQRaE5lXgQse2IPnRhtatiaRUKSxBlScGvyVibiaGYSBHib20yrj1eeT52cbLrF1rkwEIxiappC1LibHCg8/640?wx_fmt=jpeg&from=appmsg)

不仅如此，依托360专为“龙虾”智能体打造的核心技术优势，龙虾卫士的基础环境漏洞防护能力实现全面升级，让漏洞防护更高效、更贴心、更省心：一方面，依托360智脑大模型的强大能力，突破传统特征库检测的局限，既能精准识别已知的基础环境漏洞，更能对新型、未知的漏洞威胁进行异常行为检测和潜在风险预判，打造主动防御屏障，将风险扼杀在萌芽状态；另一方面，背靠360强大的云端安全运营体系，海量漏洞库、恶意样本库实时同步更新，7×24小时专业安全团队值守并持续优化检测策略，实现基础环境漏洞的秒级识别、精准告警，让风险无所遁形。

作为“龙虾”智能体全生命周期安全的专属产品，360龙虾卫士在夯实基础环境漏洞防护核心能力的同时，还将持续迭代升级，全面覆盖Skills投毒、模型提示词注入等多场景安全防护，为OpenClaw构建全流程、全方位的安全防护体系。

**360龙虾卫士**

未来，360将持续深耕智能体安全领域，让每一位用户都能放心拥抱AI，真正实现“安全养虾、放心用虾”。

点击**【阅读原文】**或访问 clawsafe.360.cn，即刻下载360龙虾卫士。

*\*本次推出的新产品可能面临技术风险和市场风险，未来市场规模和经济效益情况取决于市场推广进度、产品接受程度等因素，公司尚无法准确预测对公司经营业绩的影响情况。本宣传不构成对读者的任何实质性承诺或信息披露。敬请广大读者理性判断，注意风险。*

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