---
title: 奇安信发布智能网联汽车云平台漏洞报告：九成存漏洞，超七成涉高危风险
url: https://mp.weixin.qq.com/s/aExQGs2gTUkNPVldS9DJqw
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:06.568629
---

# 奇安信发布智能网联汽车云平台漏洞报告：九成存漏洞，超七成涉高危风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMR7LHrJibGAZgFQlm08RN2BQKicYxJ69RE27fHqwOtKIgw3Xrz0EF0kmjDzxxTCHXdL8xaLCDM5PQvw/0?wx_fmt=jpeg)

# 奇安信发布智能网联汽车云平台漏洞报告：九成存漏洞，超七成涉高危风险

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjar7xGewXSrRuTkBOYMsEWM9BpLnQeIiawrV4ibTp7oc5vVrrevInuk2TJFoCSKicibt5n1GQ5gpMOeycw/640?wx_fmt=png&from=appmsg#imgIndex=0)

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjar7xGewXSrRuTkBOYMsEWM9uosNmcJwaF8e4jQmBVCL0CAXM6QGSxZLBLWIrj8mIjsum3aFJJvRnA/640?wx_fmt=png&from=appmsg#imgIndex=1)

2026年1月15日，奇安信代码安全实验室奇车安全团队发布《智能网联汽车云平台漏洞分析报告》（以下简称：《报告》）。报告对2025年度国内30家主流汽车厂商的云平台进行了漏洞分析，结果触目惊心：93.3%的厂商云平台存在安全漏洞，其中76.7%的厂商云平台存在超危或高危级别漏洞，直接危害车企和用户数据安全、车辆安全，整体安全风险极高。从漏洞类型、成因、危害及影响范围来看，当前行业整体软件安全水平极低，安全防护基础极为薄弱，安全态势严峻，亟需引起行业的高度重视。

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjar7xGewXSrRuTkBOYMsEWM9DKkicHiao0oR5BzmO6h3pouTJEDf9fOxR7ibrWx1HkbejdIxGibvBQABAg/640?from=appmsg#imgIndex=2)

超七成厂商存在超危/高危漏洞，

超六成漏洞源自低级错误

## 在漏洞总体状况方面，超七成厂商云平台存在超危或高危漏洞，安全风险极高。

30家汽车厂商云平台中，有23家存在超危/高危漏洞，占比高达76.7%，这些漏洞可直接导致未授权解锁车辆、未授权驾驶车辆、敏感信息泄露等严重后果。超危/高危漏洞数量最多的厂商云平台存在9个超危/高危漏洞，前5名厂商累计存在34个超危/高危漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjar7xGewXSrRuTkBOYMsEWM9Hukg1EecNA2eym9ZgyAD4cldlZ4P93Q1icKpbbcrzRf1QdjunEYzYxg/640?wx_fmt=png&from=appmsg#imgIndex=3)

图：超危/高危漏洞数量排名前5位的云平台

## 从漏洞成因来看，超六成漏洞源于低级错误。

在总共发现的207个漏洞中，有135个漏洞由身份未检验、接口未鉴权等软件开发中的低级错误引发，占比65.2%，涉及19家厂商，其中12家因此产生超危/高危漏洞，反映出行业整体软件安全水平严重不足，安全防护基础极为薄弱。

## 在主要漏洞类型方面，超七成汽车厂商云平台存在身份认证和访问控制类漏洞。

失效的访问控制与身份认证失效两类漏洞共影响22家厂商，占比73.3%。其中，60%的厂商存在失效的访问控制漏洞，包括未授权访问、越权访问等问题；43.3%的厂商存在身份认证失效漏洞，包括身份认证绕过、验证码机制失效、账号枚举、弱口令与默认凭证等问题。此类基础性漏洞的大范围存在，并非个别开发人员疏忽所致，而是系统性安全管理缺陷的集中体现，反映出多数厂商未建立基本的软件安全开发流程，安全架构设计缺位、编码规范缺失、代码审计与渗透测试严重不足。

## 同时，有半数厂商云平台存在过度数据暴露漏洞。

15家厂商云平台存在接口响应数据冗余、调试信息与内部结构泄露等过度数据暴露漏洞，这些厂商云平台后端接口未遵循“数据最小化”原则，将数据安全责任完全交给前端，违背了基本的安全设计原则。

此外，30%的厂商存在数字钥匙管理失效漏洞，包括数字钥匙非法复制、数字钥匙权限管理失效、数字钥匙授权撤销失败等问题，此类漏洞可导致非法获得车辆钥匙、“临时钥匙”变“永久钥匙”等严重后果，直接威胁车辆财产安全。

汽车数字钥匙的管理涉及到云平台、车端、移动端等多方协同，攻击面广泛，此类高风险的专属复杂业务场景，尤其需要业务团队和安全团队的紧密合作，从设计阶段就要将安全纳入，并贯穿始终。

认证失效、授权失控、数据裸奔

安全防线全面失守

## 《报告》显示，漏洞危害已经覆盖数据安全、车辆安全、账户安全等核心领域。超七成厂商面临敏感信息泄露，数据安全风险尤其突出。

22家厂商云平台因过度数据暴露、访问控制失效等漏洞，导致用户个人信息与车辆敏感数据泄露。某厂商云平台通过3个漏洞组合，任意注册用户即可批量获取车主手机号、车辆实时位置等信息；另一厂商云平台则因账号枚举与越权访问漏洞，导致车主姓名、性别、邮箱、车辆VIN码等全面泄露。这些数据被攻击者利用后，可实施精准诈骗、安装窃听装置等违法犯罪活动，甚至结合解锁漏洞实施车辆盗窃。

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjar7xGewXSrRuTkBOYMsEWM9HhicRYIicBHmXUu2OrYNZOoOQnjrI5qMr7Jic2YzdXu6GUunKW3EsV2icQ/640?wx_fmt=png&from=appmsg#imgIndex=4)

图：漏洞危害及影响的汽车厂商数量和占比

## 在车辆安全方面，2/3厂商的汽车存在未授权解锁风险，直接危害车辆财产安全。

20家厂商的车辆可通过漏洞实现远程或近场未授权解锁，其中13家厂商的车辆在解锁后可直接启动驾驶，占比43.3%。某厂商云平台中存在越权访问漏洞，导致任意用户只需通过车辆VIN码即可远程解锁任意车辆，由于车辆VIN码位于车辆前挡风玻璃下方，极易获取，因此该漏洞的攻击门槛极低，致使车辆锁车状态形同虚设。

同时，该厂商云平台还存在敏感信息泄漏问题，攻击者可以利用漏洞批量获取到该厂商汽车的VIN码、车辆实时位置，这两者结合起来，攻击者就可以对该厂商的汽车实施批量定位、解锁和启动的攻击行为，造成大规模的车辆资产风险。

## 《报告》还显示，四成厂商云平台存在账户冒用风险。

其中12家厂商的用户账户可能被攻击者利用漏洞冒用，进而产生多种危害：盗用账户余额进行充电等消费、占用试驾服务资源、篡改车辆授权权限、删除电子围栏设置、泄露出行轨迹等，既造成用户财产损失，又威胁车辆安全与隐私保护。此外，部分厂商还面临远程影响OTA、远程控制服务器等高级别威胁，虽然占比较低，但可能导致非常严重的车辆安全事件。

应对之策：十大建议筑牢车云安全防线

针对行业严峻的安全现状，奇安信从战略定位、研发根基、车云协同三大方向提出十大建议，助力厂商构建全生命周期安全体系。

在提升战略高度、压实安全主体责任方面，建议厂商将网络信息安全上升为“一把手工程”，明确企业主要负责人为第一责任人，设立专门安全管理机构，保障年度安全专项预算不低于信息化总投入的一定比例，为安全体系建设提供持续资源支持。

在践行内生安全、筑牢研发根基方面，推行安全开发生命周期，将安全需求分析、威胁建模、代码审计等环节嵌入开发流程；强化软件供应链安全，建立SBOM管理机制，严格管控供应商软件与开源组件的安全风险；建立漏洞响应机制与公开漏洞奖励计划，借助内外部力量发现漏洞，每年至少开展一次云端与车端核心功能和新功能深度白盒渗透测试。

在深化车云协同、构建主动免疫体系方面，实施零信任架构，部署动态细粒度访问控制网关，对所有请求进行持续验证与最小权限授权；引入RASP技术强化应用层防御，实时监测阻断异常行为；建立统一身份与密钥管理中心，实现数字密钥全生命周期闭环管控；落实数据分类分级保护，通过加密存储、脱敏处理等措施保障数据安全；在车端部署轻量级IDPS系统，监控车内网络流量与进程；建设车云协同安全运营平台，利用AI实现威胁全局可见、精准研判与协同响应，做到“分钟级”全局免疫。

奇安信代码安全实验室负责人表示，智能网联汽车网络安全是复杂的系统性工程，云平台作为核心枢纽，其安全短板已成为行业最大风险点。本次报告揭示的大量基础性漏洞，反映出行业在安全责任落实、研发体系建设、车云协同防御等方面的体系化缺失。厂商需尽快补齐安全短板，将安全内生于产品全生命周期，才能切实保障用户出行安全与产业健康发展。奇安信将依托在代码安全、网络安全等领域的技术积累，为智能网联汽车行业提供全链条安全解决方案，助力构建安全可信的产业生态。

关于我们

![](https://mmbiz.qpic.cn/mmbiz_png/mflphQBJic3STjs5EXib7E8mUTyW8OOibkBv0A2RCNVdryhNX6icoDx1nzX2h4hcMVPMctYfUcqLiaquTwUnRqlJSbg/640#imgIndex=5)

奇安信代码安全实验室是奇安信集团旗下，专注于软件源代码安全分析技术、二进制漏洞挖掘技术研究与开发的团队。

奇车安全团队是奇安信代码安全实验室负责智能网联汽车安全研究的团队，对主流智能网联汽车产品进行了大量的安全研究工作，在30多个汽车品牌的产品中发现了数百个安全漏洞，并曾获得2025工信部NVDB-CAVD春季汽车信息安全挑战赛第一名、中国计算机学会（CCF）首届汽车安全攻防大赛一等奖、赛力斯问界首届汽车安全大赛冠军等多个奖项。

扫描二维码或点击“阅读原文”，马上下载报告！

![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjar7xGewXSrRuTkBOYMsEWM98f7Taugt9oHmzh9iaxibCIM4fwqKzRHOj6gaLJueUzu7YXeRaQtOTKgQ/640?from=appmsg#imgIndex=6)

**推荐阅读**

[奇安信斩获首届CCF智能汽车大赛“汽车安全攻防赛”一等奖](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523838&idx=1&sn=86f2bfc58cb6869d1fc1dbd1dfba0243&scene=21#wechat_redirect)

[奇安信荣膺NVDB-CAVD2025汽车信息安全春季赛第一名](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523360&idx=1&sn=df7f6e82910263f9b6bbf26c9e9fe887&scene=21#wechat_redirect)

[黑客可入侵调制解调器，控制汽车仪表盘](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524697&idx=1&sn=859874b28c699cba937a7edf009d7623&scene=21#wechat_redirect)

[只需几个低廉小工具，即可发动“自带汽车”攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524245&idx=2&sn=d2d44afa6cf97d714aab24bf90c6299a&scene=21#wechat_redirect)

[Pwn2Own 2026 东京汽车大赛目标和奖金公布](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524221&idx=1&sn=f00b9533df932792f0734682bf483dcf&scene=21#wechat_redirect)

**转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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