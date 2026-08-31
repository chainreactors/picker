---
title: 柏林遭黑客窃取5.79TB数据，曼彻斯特机场确认客户数据泄露
url: https://mp.weixin.qq.com/s/WrqlJwQH6DxxZgsgq0h22Q
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:50:38.777695
---

# 柏林遭黑客窃取5.79TB数据，曼彻斯特机场确认客户数据泄露

# 柏林遭黑客窃取5.79TB数据，曼彻斯特机场确认客户数据泄露

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX2nQ4Itf1eRRCEfolQ0zEfxuwReCrBmhibEWmFdjYNNZzZcriceMniaXvJEebCLgpXUK5ib2XUib4rNicHCkdibakEXArWSYF4MPict1O8/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0ogsqcEOybshnVU0ZIFr3htvPoP32aUGCteyuIZ7ETmSwApteLr7nIiamnhfc9uanFzyicJbF7ZsMWZMHoDHrTgmK9od5Lo8yJM/640?wx_fmt=jpeg&from=appmsg)

Part01

柏林拒绝向黑客支付赎金

柏林州政府已证实，在8月该市国家行政网络遭到入侵后，其成为了一起勒索企图的目标，并表示不会满足勒索者的要求。

同一份声明披露，取证工作发现参议院移动、交通、气候保护与环境事务部所辖范围内存在进一步的数据外泄，外泄时间介于2026年8月7日至8月12日之间。

外泄数据的范围和内容仍在核查中，参议院总理府表示，不排除被窃取的数据中包含个人数据或其他非公开数据。

参议院总理府在回答提问时表示，该部门于8月7日首次报告了数据外泄，这比8月14日该部门被切断网络连接早了7天。

柏林方面尚未公布网络中外泄数据的具体数量。目前流传的唯一明细来自攻击者一方——8月28日被索引的一条泄露网站帖子声称窃取了5.79TB的数据，涉及12,076人的个人信息。

截至8月29日，参议院就该事件发布的两份通报均未向数据可能遭到泄露的人员提供任何指引。

“柏林州正在遭受勒索。”柏林市长凯·韦格纳在红色市政厅举行的参议院特别会议后表示，此语引自柏林官方城市门户网站的机器翻译英文版本。

参议院总理府的声明称，州刑事警察局、检察机关及联邦安全机构正在调查涉嫌实施攻击的人员，目前尚未确定攻击背后的任何组织。

德国《明镜周刊》已将Rhysida列为率先报告此次攻击归因的组织，报道援引了该组织暗网泄露网站上的条目及参与响应的安全消息来源。《黑客新闻》于8月29日通过泄露网站监测服务确认，一条标题为“Berlin, Germany”的条目已于8月28日被添加至Rhysida的泄露网站。

该帖子声称扫描了5.79TB数据、约144万个文件，且仅将受害者标识为“德国柏林”，而非参议院或任何具体部门。条目中未出现赎金数额，其列出的11个文件类别（其中最大的一类为124,823个地图和地理数据文件）合计约占所声称文件总数的四分之一。

Part02

攻击手法与事件处置

美国网络安全和基础设施安全局（CISA）、联邦调查局（FBI）以及多州信息共享与分析中心（MS-ISAC）在一份关于Rhysida的联合公告中披露了该组织的攻击手法，记录了以下初始访问途径：

* 面向外部的远程服务上的有效账户：攻击者使用遭泄露的有效凭证，通过内部虚拟专用网络（VPN）接入点进行身份验证，尤其是在默认未启用多因素认证（MFA）的组织中。

* Zerologon（CVE-2020-1472）：Microsoft Netlogon远程协议中的权限提升漏洞，微软已于2020年8月11日修复。
* 网络钓鱼：相关机构记录显示，这也是成功入侵受害者网络的途径之一。

该公告发布于2023年11月，当时上述机构首次对Rhysida的双重勒索攻击发出警告。公告指出，“FBI和CISA不鼓励支付赎金”，因为支付赎金并不能保证数据恢复，反而可能助长攻击者对更多组织实施攻击。

上述机构建议优先修复已知被利用的漏洞、在所有服务中启用多因素认证，并对网络进行分段以阻止勒索软件传播。

同一份文件提到，开源报告显示Vice Society（微软将其追踪为Storm-0832）与部署Rhysida的攻击者之间存在相似之处，而Check Point在2023年也指出了与Vice Society的关联。

截至8月29日，监测服务共列出了280个Rhysida受害者，其中9个位于德国，包括2026年5月遭袭的斯图加特市政府和2025年6月遭袭的援助组织Welthungerhilfe。其列表中还包括运营西雅图-塔科马国际机场的西雅图港务局，该条目于2024年9月被索引。

参议院总理府表示，柏林州数据保护专员和联邦信息安全办公室（BSI）正在持续获知事件进展。截至8月29日，《黑客新闻》未发现柏林数据保护与信息自由专员就此事发布任何声明。

内政事务参议员伊里斯·施普兰格表示，就目前情况而言，与9月20日柏林众议院选举相关的领域没有数据外泄，其安全官员认为选举环境是安全的。

柏林于8月17日首次披露了该事件，称取证工作已确认州网络遭到入侵，且两个受影响的部门自前一个周五起已被隔离。

在8月19日的新闻发布会上，韦格纳表示该事件在当时是而且至今仍然是严重事件，并强调根据目前掌握的信息，没有敏感数据离开州网络。

在两个部门断网期间，住房补贴申请和支付业务无法办理。所有参议院部门已于8月23日重新联网，取证工作和州网络扫描仍在进行中。

Part03

曼彻斯特机场确认客户数据遭窃取

运营曼彻斯特机场、伦敦斯坦斯特德机场和东米德兰兹机场的曼彻斯特机场集团（MAG）于8月27日表示，一个未经授权的第三方获取了与上述三个机场的停车场、贵宾休息室和快速通道预订以及机场内WiFi注册相关的客户数据。

“乘客安全或航空安保在任何时候都没有受到损害。”MAG发言人在公司发布的声明中表示，并补充说机场运营和客户停车服务仍在正常运行。

被获取的数据包括电子邮件地址、电话号码、车辆登记信息和邮政编码。MAG表示，无论是MAG自身还是被访问的系统，均不存储客户的银行或支付信息。MAG的声明仅将其描述为一个独立于MAG自身的系统。

MAG的客户信息页面指出，该事件“不涉及机场运营系统”，并建议乘客照常前往机场。

截至8月29日，“管理我的预订”在线服务已作为预防措施被暂停。72小时内需要变更的预订，可于工作日9:00至17:00致电客户服务部门0208 163 8001处理。

受影响客户约为870万这一数字已广泛流传，来源为一位公司发言人对媒体透露的信息，而MAG自身的材料并未公布具体数字。

MAG表示已直接联系受影响的客户，并引导他们查阅英国国家网络安全中心（NCSC）的数据泄露指南，建议他们对可疑的电子邮件、短信和电话保持警惕。

参考来源：

Berlin Refuses to Pay Hackers Who Stole Data From the City's State Network

https://thehackernews.com/2026/08/berlin-refuses-to-pay-hackers-who-stole.html

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0libf8LzftSm6VZDiarpFqH2q1run3yK9BZ325tAcvOYazjXWkPDD9uCnx7x1I0sEB7icfGib6jiak9n48AE8yjRoToge845nXiaTWU/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1yyL5Vl0nh0phHN7f9WxW0KrycyDR2x2yfZgF5eSsJ4u8Zsv5ENWkicv0NYBtK4xBB7BPdP6QswQBCSBncIbH99T386xkuVz04/640?wx_fmt=png)

预览时标签不可点

阅读原文

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
听过