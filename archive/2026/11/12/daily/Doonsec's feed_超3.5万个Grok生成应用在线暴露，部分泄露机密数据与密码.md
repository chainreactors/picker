---
title: 超3.5万个Grok生成应用在线暴露，部分泄露机密数据与密码
url: https://mp.weixin.qq.com/s/iVASTaPjYzS1oIWCKvzJ4g
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:58:24.171970
---

# 超3.5万个Grok生成应用在线暴露，部分泄露机密数据与密码

# 超3.5万个Grok生成应用在线暴露，部分泄露机密数据与密码

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX12Frbak0dRbtic1FZic5fCicu7Nqpw1KbChicOztkOiavJVMHBZN3JhnPDibQcesw0a72ibhPp3UTj1utY3ULnSc7EansIe3yzuT8rkE/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2d6mhqJlEjPZ8jvBwxl5tNuX76wHD2ZNHf93iayCz23Wus7yMLSlicHSrKZVT1Q7UWyHStibIAqdrCjeakxWTfLq7y1KibVmlpfEU/640?wx_fmt=png&from=appmsg)

Part01

超3.5万个Grok应用公开暴露

安全公司Claroc的研究人员昨日表示，他们在全网共发现37571个由Grok生成的应用，其中35578个无需登录即可向所有人开放访问。

这些公开应用中，有24个由社交平台X、以及Grok AI助手的开发公司SpaceXSI的员工搭建。大部分公开应用是游戏、落地页和计算器类工具，但约十分之一包含内部业务数据或个人信息。

员工搭建的应用涉及多类机密内容，包括新销售岗位员工的入职方案、标注594个客户的销售区域图，以及X递交给美国联邦机构、标注为机密的广告提案。SpaceXSI原名xAI，目前已下架全部24个员工搭建的应用，但未处理其他用户的公开应用。

除上述员工应用外，公开应用中还识别出另外30家机构的内部数据，覆盖建筑、能源、医疗、国防等多个领域。其中26家机构员工规模超过1000人，6家为财富500强企业。

报告估算显示，约2%的公开应用包含高危或严重级别的敏感内容。

泄露的内容包括某医疗集团可搜索的3500多名员工名单、单个患者的重症监护简报、某消防部门的实时值班看板。还有一家承包商的工时表应用，代码中以明文形式存储了所有员工的密码。

用户在Grok的聊天窗口输入需求描述，即可生成可运行的应用。8月19日，Grok面向所有订阅套餐用户开放了这一功能。这个聊天搭建工具与另一款独立终端编码工具同名，均称为Grok Build，后者的代码仓库上传问题曾在7月14日被公开报道。

根据Grok官方发布公告，每个发布的应用都会分配到grok.me下的独立子域名，应用创作者可以设置访问权限范围。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3wmZI1pg39bVI2EBH5z9W1Qvyp2VTMiamksvMr24icwjKcEHPNMkVmJl7KnrjoU0myFgVwaAs9tbNwqpjD9lvhpvGvCibbly6P1Y/640?wx_fmt=png&from=appmsg)

Part02

默认权限配置存在缺陷

只有创作者Click Publish按钮后，应用才会公开。研究人员使用付费账号测试时发现，发布流程的下一步提供三个访问权限选项："知道链接的任何人""受邀用户""仅自己"，其中"知道链接的任何人"为默认选中状态。

这一默认设置存在极大风险，因为应用地址无法做到完全保密。用户访问应用时，设备会通过DNS查询对应的子域名，被动DNS服务会记录这类查询请求，任何人只要拥有相关服务账号，就可以按特征模式搜索这些记录。

![Grok应用权限设置](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX295M3nwe5ibia8G5CcMP1WYVEHra3icERCQbsia6t8w9yhscRaPbcDPibiaTndicjPLicHwZMNS5dEViaDZr532Rw7aonzWovGxwKJtCZs/640?wx_fmt=png)

Grok会为每个应用随机生成4个单词作为名称，发现的应用中约半数遵循这一命名规则。这类名称虽然难以暴力猜测，但如果应用名称已经被收录到可搜索的列表中，这种保护机制就会完全失效。

ChatGPT的应用搭建功能同样会为每个应用分配独立子域名，但用户发布应用时，默认访问权限为"仅自己"，用户手动修改后才会变更。因此即使通过DNS数据发现ChatGPT应用的地址，访问者也会因为权限不足无法打开，只有应用所有者可以访问。

研究人员通过通用子域名发现方法获取Grok应用名称，在未登录的状态下访问了每个应用的首页。

为验证Grok自身的权限防护机制，团队搭建了两个包含虚构数据的测试应用，使用默认选中的"知道链接的任何人"权限完成发布。

第一个测试应用是联系人列表，自带数据库但未配置登录校验。在隐私窗口未登录状态下即可新增一条联系人记录，后续访问的所有用户都能看到这条新增内容。

![未授权访问测试](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2KXo2BM9ibV19RI10JvlFBHWwZxfoeT6jGR7icLXiaibNorcCLPCjAJUibAJuFvAU0gLMXqJlr4KdLzca7DHEpXqQdgdcWGqicnutW0/640?wx_fmt=png)

第二个测试应用是4人销售团队的客户列表，Grok自动为其添加了"通过Google登录""通过X登录"的按钮。但Grok生成的代码存在逻辑缺陷：用户登录后，系统会先将其加入团队成员列表，再校验其身份是否属于授权范围，导致校验流程永远可以通过。

测试中，一个不属于应用所有者的未授权Google账号成功进入应用，查看了所有客户信息，还修改了一条记录、删除了另一条记录。

上述测试仅在团队自行搭建的应用上开展，研究人员未测试已发现的公开应用是否存在同类未授权修改风险。

Part03

漏洞已同步开发方

研究人员在周日通过security.txt文件中公布的联系渠道，向SpaceXSI上报了相关发现，其中包含2个员工搭建的应用，剩余22个员工应用的相关信息在周一完成上报。

截至报告发布时，SpaceXSI尚未对漏洞上报做出正式回复，但已就相关研究问题回应了记者提问。

SpaceXSI回应称，Grok应用在创作者主动分享前始终保持私有状态。发布流程包含多个步骤，用户需要在"仅自己""知道链接的任何人"之间选择权限，同时还要确认法律免责声明，员工账号的默认权限设置为"仅自己"。

但实际检测结果显示，仍有24个由SpaceXSI和X员工搭建的应用处于公开可访问状态。

研究人员在报告中建议SpaceXSI将"仅自己"设为默认权限，同时新增限制应用仅允许企业自有邮箱域名用户访问的选项。

SpaceXSI的回应中未提及将联系其他公开应用的所有者。目前研究团队已开始主动向受影响机构发送邮件告知风险，截至报告发布时已完成3家机构的通知。为避免风险扩大，报告中隐去了所有应用的地址和名称。

10月18日，同一研究团队曾发布关于Muse的研究，指出Meta的Muse AI Agent共享的页面可通过被动DNS被发现。随后Meta暂时关闭了共享功能，并于10月22日公布了共享机制修复方案，为所有共享内容分配新的地址。

Claroc主营AI生成应用的发现与安全防护工具，该公司给出以下排查建议：

* 梳理员工使用的AI应用搭建工具。Grok、Lovable、Replit、v0、Bolt、Base44、Google AI Studio等工具无需IT部门部署或企业账号即可使用，需重点排查。
* 如果企业拥有被动DNS数据访问权限，可查询上述搭建工具的相关域名，通过隐私浏览器窗口访问查询到的结果验证权限。
* 确认所有存储内部数据的Grok应用权限设置为"受邀用户"或"仅自己"，外部用户访问时应返回错误页面。
* 使用企业外部的账号尝试登录应用，如果可以成功进入，说明应用缺少授权访问名单校验。
* 检查每个应用加载的脚本中是否包含姓名、邮箱地址、密码等敏感信息，下架无明确负责人的应用。

测试验证显示，将应用权限设置为"仅自己"后，外部用户访问页面和请求数据时都会收到401错误；执行下架操作后，应用可在数秒内停止对外服务。

参考来源：

Over 35,000 Grok-Built Apps Exposed Online, Some Leaking Confidential Data and Passwords

https://thehackernews.com/2026/11/over-35000-grok-built-apps-exposed.html

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Wh05Z0rN9nVQTjUXnyXs6uYnM9oo6THt2FhXmXzcuMkHbceiatCbhz8mR2zDd0yicfXLAnN2mwPzVRz1C0ibPQ0ocMnNt16QAkg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349303&idx=1&sn=86458815b0d0b880c32e19864a449a98&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

预览时标签不可点

阅读原文

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