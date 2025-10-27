---
title: 【安全头条】不法黑客滥用Google Ads分发恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649781797&idx=2&sn=887d2822682339fd5b4ad9a47f84d1c2&chksm=8893464abfe4cf5ca21883c2b99c4cdcde1baadad422d802496c695db86ecddcf9b116e60e2b&scene=58&subscene=0#rd
source: 安全客
date: 2023-01-04
fetch_date: 2025-10-04T02:59:58.125007
---

# 【安全头条】不法黑客滥用Google Ads分发恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb5NVk0OjlXAkU4SmN0d8ib7Lia7FJhltibL1k36Kd17bUEkERIydVibKv8omHYAanLH2pe9pECfYmBjQg/0?wx_fmt=jpeg)

# 【安全头条】不法黑客滥用Google Ads分发恶意软件

安全客

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb484SnTLnoXJ62gPG7yjtA3l5Lia57HmsbMcUrPLCCf2fgE9c0NcLfPPT7icG57k4mzibKmDrqEnlx6g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**第432期**

**你好呀~欢迎来到“安全头条”！如果你是第一次光顾，可以先阅读站内公告了解我们哦。****欢迎各位新老顾客前来拜访，在文章底部时常交流、疯狂讨论，都是小安欢迎哒~如果对本小站的内容还有更多建议，也欢迎底部提出建议哦！**

## **1. 不法黑客滥用**

## **Google Ads分发恶意软件**

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb5NVk0OjlXAkU4SmN0d8ib7L7FFIwQiaPtickIILdZq25AgAf7IllWuAMb09BiacsoXkDiclTiaHwD4C0GQ/640?wx_fmt=jpeg)

恶意程序的运营者日益滥用 Google Ads 将恶意程序传播给搜索合法软件的用户。

受害者包括了 Grammarly、MSI Afterburner、Slack、Dashlane、Malwarebytes、Audacity、μTorrent、OBS、Ring、AnyDesk、Libre Office、Teamviewer、Thunderbird 和 Brave。黑客会创建上述项目官方网站的克隆，但将用户点击下载的软件替换为恶意程序。通过这种方法传播的恶意程序包括 Raccoon Stealer 的变种， Vidar Stealer 的定制版本， IcedID 恶意程序加载器。当广告商利用 Google Ads 发布广告时，如果 Google 检测到目标网站是恶意的，广告会删除。恶意程序的运营者利用了一种简单的方法绕过了这种检测——方法是首先将点击广告的用户带到没有恶意程序的网站，然后再重定向到克隆网站。[点击“阅读原文”查看详情]

## **2. 谷歌智能音箱曝后门**

## **可允许黑客窥探对话**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb5NVk0OjlXAkU4SmN0d8ib7LDXue5vvJltpVGSujyD5ahBB67WDnaiaOUm5klUB4KZd2ib1CbVccHcrA/640?wx_fmt=png)

日前，Google Home智能音箱中的一个漏洞允许安装一个后门帐户，该帐户可用于远程控制它，并通过访问麦克风馈送将其变成一个窥探设备。

据悉，一位安全研究员在试验Google Home 迷你扬声器时，发现使用Google Home应用程序添加的新帐户可以通过云API向其远程发送命令，随后通过Nmap扫描，找到Google Home本地HTTP API端口，并设置了一个代理来捕获加密的HTTPS流量，进而抢夺用户授权令牌。

研究人员还发现，向目标设备添加新用户是一个两步过程，需要设备名称、证书和来自其本地API的“云 ID”。有了这些信息，他们就可以向谷歌服务器发送链接请求。

为了将流氓用户添加到目标 Google Home 设备，分析师在Python脚本中实现了链接过程，该脚本自动泄露了本地设备数据并再现了链接请求。[点击“阅读原文”查看详情]

## **3. Citrix数千台服务器**

## **存在严重安全风险**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb5NVk0OjlXAkU4SmN0d8ib7LpmHJbEIMkxLgFiaYKnpleZqDUicgDNympAS094QrBjliblB66PxH9dmhA/640?wx_fmt=png)

网络安全分析师警告称，数以千计的Citrix ADC 和网关部署仍然存在安全风险，即便该品牌服务器在此之前已经修复了两个严重的安全漏洞。

第一个漏洞是CVE-2022-27510，已于11月8日修复。可影响两种 Citrix 产品的身份验证绕过。第二个漏洞是CVE-2022-27510，已于12月13日披露并修补，其允许未经身份验证的攻击者，在易受攻击的设备上执行远程命令并控制它们。

然而，就在Citrix公司发布安全更新对漏洞进行修复时，攻击者已经在大规模利用CVE-2022-27518漏洞了。

NCC Group公司旗下的Fox IT团队的研究人员报告说，虽然大多数面向公众的 Citrix 端点已更新为安全版本，但仍有数千个端点容易受到攻击。[点击“阅读原文”查看详情]

## **4. Chrome浏览器将阻止用户**

## **通过不安全HTTP链接下载文件**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb5NVk0OjlXAkU4SmN0d8ib7LbRVwpPzBA4xjASucwcfNIasUNUiaTjMQPkHFPhJqK7RDV5fDV8FwBnQ/640?wx_fmt=png)

29日消息，谷歌Chrome浏览器即将引入一项新的安全措施：阻止下载 HTTP 链接的文件。

据报道，在“Block insecure downloads”实验Flag生效之后，如果用户尝试通过不安全的传输方式（例如 HTTP），或通过不安全的重定向下载一个文件，页面将显示一个”被阻止”的消息。预计该项功能会在明年3月推出的Chrome 111版本中正式推出。[点击“阅读原文”查看详情]

## **5. 工信部等十二部门公布**

## **2022年网络安全技术应用试点示范项目名单**

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb5NVk0OjlXAkU4SmN0d8ib7LXh8J1VRCe67GmbNsyRwKKUTzqQOwgtOp6gKkEUR38H71MHC7Arwv6g/640?wx_fmt=jpeg)

工业和信息化部、国家互联网信息办公室等十二部门近日联合公布2022年网络安全技术应用试点示范项目名单，共有99个项目上榜。

各入选项目申报单位要坚持需求导向和技术推动，加大投入力度，持续优化项目质量和服务水平，积极创造经济价值和社会效益。各示范区运营单位要聚焦发展方向，汇聚产业资源，打造高质量网络安全“高精尖”技术创新平台。各有关部门要加大支持力度，推动试点示范项目在各地区、各行业应用推广。[点击“阅读原文”查看详情]

## **6. 反间谍法修订草案**

## **二审稿增加有关网络间谍的规定**

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb5NVk0OjlXAkU4SmN0d8ib7L3Zxz1Wiaw0eN0dbfXF4lDKr3yibqlnXsyK3SYZkjXKr5MPzVAyYKKoOw/640?wx_fmt=png)

反间谍法修订草案今天再次提请十三届全国人大常委会第三十八次会议审议。修订草案二审稿进一步加强反间谍宣传教育，提高全民反间谍意识，在立法指导思想和基本原则中增加规定“筑牢国家安全人民防线”，同时增加规定新闻媒体等单位应当面向社会开展反间谍宣传教育，增强全民国家安全素养，明确重点单位应当加强对涉密人员的反间谍安全防范教育。

修订草案规定了间谍行为的定义。有意见提出，帮助实施间谍行为具有一定的社会危害性，需要依法惩处，但性质应区别于直接实施间谍行为。修订草案二审稿将帮助实施间谍行为在法律责任中明确予以处罚。还有意见提出，网络窃密、攻击、破坏是间谍行为新形态，建议增加有关网络间谍的规定。修订草案二审稿将为间谍组织及其代理人提供针对关键信息基础设施的网络安全漏洞等信息的行为规定为间谍行为。

修订草案二审稿还进一步加大了对反间谍工作的支持力度，增加规定：对在反间谍工作中作出重大贡献的个人和组织按照国家有关规定给予表彰和奖励；重点单位应当加强对涉密事项、场所、载体等反间谍物理防范措施；鼓励反间谍领域科技创新，发挥科技在反间谍工作中的作用；明确国家安全机关应当加强反间谍工作的人才队伍建设和专业训练。

针对有意见提出应处理好开展反间谍工作与保护个人、组织合法权益之间的关系，加强对国家安全机关反间谍工作的监督，修订草案二审稿将第四章章名修改为“保障与监督”，明确国家安全机关查阅调取、查封扣押冻结不能超出执行任务的范围和限度，明确国家安全机关对人身、物品、场所进行检查以及决定不准出境等的批准层级。

此外，为做好与出境入境管理法、刑事诉讼法等相关法律的衔接，增强法律的可操作性，修订草案二审稿增加国家安全机关对相关人员决定不准出入境和撤销决定应及时通知移民管理机构的规定以及行刑衔接的规定。[点击“阅读原文”查看详情]

![](https://mmbiz.qpic.cn/mmbiz_gif/Ok4fxxCpBb7QxxODhJSnPyIZe6ZNAgPibByWLDwGu5SWicFr0g9FbXs5Ffdsx3EibAuPaf8njVefjA9B54oHsRqwg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb7QxxODhJSnPyIZe6ZNAgPibsxfq5yL6kPEIaGDzibzV1W1QWNXic8dnx3Ky93Ay7PEpb7lgYGREddkA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

上期回顾

[【安全头条】APT攻击转向恶意Excel加载项作为初始入侵向量](http://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649781739&idx=3&sn=d985ab86459a9d9fb341a57192f0f776&chksm=88934584bfe4cc92e8b9faf6c33e83e1c44ecc73304219bb825e7441e219a266027665b53d9d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/Ok4fxxCpBb5ZMeq0JBK8AOH3CVMApDrPvnibHjxDDT1mY2ic8ABv6zWUDq0VxcQ128rL7lxiaQrE1oTmjqInO89xA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**戳“阅读原文”查看更多内容**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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