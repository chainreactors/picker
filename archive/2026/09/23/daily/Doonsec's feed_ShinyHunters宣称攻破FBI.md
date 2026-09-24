---
title: ShinyHunters宣称攻破FBI
url: https://mp.weixin.qq.com/s/bAXg7Pcau4vxGidqkvMzrQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:04.308787
---

# ShinyHunters宣称攻破FBI

# ShinyHunters宣称攻破FBI

安世加

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**新闻**

*News Today*

9月21日周一晚间，ShinyHunters篡改了FBI自己的招聘网站apply.fbijobs.gov，页面被替换成"本站已被ShinyHunters接管"，随后FBI把网站下线显示"维护中"。团伙声称：他们在Oracle PeopleSoft里发现了一个预认证RCE零日漏洞，用它拿下了FBI的服务器，再横向进入FBI托管在AWS GovCloud里的系统，拖走了2到3TB数据——覆盖FBI现任员工、离职员工和所有特工申请人的姓名、住址、电话、配偶信息、出生日期，号称能查到CJ（刑事司法）、HR、Medlink三个内部服务。

The Register、404 Media、CyberInsider都收到了5000条记录的样本。有媒体用OSINT工具抽查了样本里的电话号码，部分确实和署名对得上，还有一部分能关联到司法部（FBI的上级单位）人员。也就是说，样本至少部分是真的——但2到3TB的总量、GovCloud横向移动这些说法，FBI既未确认也未否认，Oracle和AWS也没回应。目前只能确定两件事：篡改真实发生了，泄露的数据至少有一部分来自真实人员。

已验证：apply.fbijobs.gov被篡改、样本含真实FBI/司法部相关人员电话待验证：2-3TB数据总量、AWS GovCloud横向移动、PeopleSoft零日的具体细节

最有意思的是动机。ShinyHunters明确告诉媒体"这不是财务驱动的"——他们不要赎金，要FBI撤回或更正今年5月15日发布的通告。那份通告说这伙人骚扰受害者及其家属、搞swatting、经常谎称掌握不存在的敏感材料。ShinyHunters说这些都是污蔑，这次行动就是逼FBI改口，限期一周，否则公开全部数据。勒索团伙第一次把"数据"当成了改写官方叙事的筹码，而不是换钱的商品。

技术路径值得防守方细看。FBIJobs的招聘系统跑的是PeopleSoft——一款在企业和高校里部署极广的老牌HR/ERP套件，管理着人事、薪酬、招聘全流程。今年6月ShinyHunters就曾用PeopleSoft漏洞扫过100多家机构，当时对FBI门户的尝试失败了，Oracle随后发过紧急安全警告，Mandiant也把那波利用活动关联到了ShinyHunters。这次如果说法成立，等于同一伙人、同一类入口，绕了一圈回来了。团伙还放话，同一个零日已经用来打了教育行业，接下来会打更广的目标。

这里有一个所有企业都该对号入座的问题：你的HR系统、招聘门户、报销系统，进过渗透测试的范围吗？这类系统在安全评审里常年被归为"内部系统"，没人认真测，但它们存的数据——员工住址、家属信息、身份证号、薪酬——恰恰是威胁情报价值最高的那类。FBI的教训是，一个"后台"招聘系统不仅能泄露全员人事档案，还可能成为跳进GovCloud的跳板。公网应用和内部基础设施之间的网络分段、 HR系统自身的补丁管理（Oracle已经就PeopleSoft发过警告，打没打？）、以及员工数据的分级保护，这三件事值得今天就排进计划。

对企业安全团队还有一个不太舒服的提醒：如果连FBI都可能被人事系统打穿，那么"我们规模小、没人盯"的假设更加不成立了。ShinyHunters这类团伙的攻击动机已经不局限于钱——你的数据可能被用来胁迫你的客户、你的监管方，甚至你的对手。当勒索数据的用途从"换赎金"扩展到"达成其他目的"时，数据泄露的代价模型就变了：以前是钱的问题，现在可能是业务连续性、声誉甚至人身安全的问题。

后续一周是关键观察窗口。FBI会不会改通告、Oracle会不会确认零日并发补丁、ShinyHunters到底放不放出2TB数据、以及GovCloud的说法最终是真是假——每一条都值得盯。对企业来说，无论结局如何，"把HR系统当关键资产管"这个结论已经成立了。

信息来源：The Register

本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！

安世加为出海企业提供SOC 2、ISO 体系、PCI DSS认证咨询服务（点击图片可详细查看）

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/757fvrbk7obeYAM2Mj3y9CdTAlmsxLfZ2mmfssFQ6kib1QIeQqqibWfHNA0stkAib5LXvnx5kvTcXE3Bhk4k4W9xR4SonZz65AyR58AOgmm15Q/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247544514&idx=1&sn=7f6ad64b4f0f871a02f7e3e07a447353&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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