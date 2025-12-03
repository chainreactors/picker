---
title: 恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本
url: https://www.4hou.com/posts/kgqY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-02
fetch_date: 2025-12-03T03:15:37.541349
---

# 恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本

恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/loginIng)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12651

收藏

导语：这两款模型通过付费订阅或免费本地部署的方式，在网络犯罪圈的使用率正持续上升。

WormGPT 4、KawaiiGPT等无限制大型语言模型的恶意代码生成能力正不断强化，已能输出可直接运行的勒索软件加密程序及横向移动脚本，成为网络犯罪分子的得力工具。

Unit42研究团队对这两款模型开展了专项测试。目前，这两款模型通过付费订阅或免费本地部署的方式，在网络犯罪圈的使用率正持续上升。

**WormGPT 4：专攻网络犯罪的付费无限制模型**

WormGPT原型最早于2023年出现，但据报道该项目同年便停止运营。而WormGPT 4作为该品牌的“回归之作”，于今年9月重新出现，采用订阅制模式——月费50美元或终身使用权220美元。这款模型堪称“无审查版ChatGPT”，专为网络犯罪场景训练，不受内容安全限制。

Unit42研究人员测试了其勒索软件代码生成能力，结果显示该模型可产出能加密Windows主机上所有PDF文件的PowerShell脚本。该脚本支持自定义配置：可指定目标文件路径与扩展名，采用AES-256算法进行数据加密，更内置了通过Tor网络窃取数据的选项，完全贴合真实网络攻击的操作需求。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251128/1764321117151886.png "1764321041144741.png")

生成的数据加密脚本

此外，研究人员通过提示词引导，让WormGPT 4生成了一份“极具威慑力且话术老练的勒索信”——信中宣称采用“军用级加密技术”，要求受害者在72小时内支付赎金，否则赎金将翻倍。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251128/1764321120193036.png "1764320624554126.png")

生成的勒索信

研究人员指出，“WormGPT 4在商业电子邮件妥协（BEC）和钓鱼攻击中具备可信的语言操控能力”，这使得技术水平较低的攻击者也能实施以往仅由资深威胁行为者才能完成的复杂攻击。

**KawaiiGPT：社区驱动的免费恶意工具**

KawaiiGPT是今年7月被发现的另一款恶意大模型，作为免费的社区驱动项目，其核心能力包括生成高质量钓鱼邮件，以及自动化横向移动所需的即开即用脚本。Unit42研究人员测试了其2.5版本，发现该模型在Linux系统上的部署仅需5分钟。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251128/1764321123652902.png "1764320710168905.png")

在KawaiiGPT上生成的钓鱼邮件

**多场景恶意脚本生成测试**

研究人员通过提示词指令，验证了KawaiiGPT的四大核心能力：

1. 生成鱼叉式钓鱼邮件：支持逼真的域名伪造，内置凭证窃取链接；

2. 横向移动Python脚本：利用paramiko SSH库连接目标主机，通过exec\_command()函数远程执行命令；

3. 数据窃取与外发脚本：借助os.walk函数递归遍历Windows文件系统查找目标文件，通过smtplib库打包数据并发送至攻击者控制的邮箱地址；

4. 定制化勒索信生成：可灵活配置付款说明、时限要求及常见的加密强度宣称话术。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251128/1764321127133964.png "1764320747143297.png")

数据泄露功能

尽管KawaiiGPT未能像WormGPT 4那样生成完整的加密程序或功能性勒索软件载荷，但研究人员警示，其命令执行能力足以让攻击者实现权限提升、数据窃取，以及投放并运行额外恶意载荷的操作。

这两款恶意大模型均拥有专属Telegram频道，各频道订阅成员已达数百人，社区成员在其中交流攻击技巧与使用经验。

Unit42研究团队强调：“对这两款模型的分析证实，攻击者已在实际威胁场景中积极运用恶意大模型，这类工具已不再是理论层面的威胁。”

值得警惕的是，这些工具显著降低了网络攻击的技术门槛：缺乏经验的攻击者借助它们，能够规模化实施更高级别的攻击，大幅缩短了目标侦察与工具开发的时间；同时，模型生成的钓鱼诱饵语言流畅自然、专业性强，摆脱了传统诈骗邮件中常见的语法错误，更易诱使受害者上当。

文章来源自：https://www.bleepingcomputer.com/news/security/malicious-llms-empower-inexperienced-hackers-with-advanced-tools/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2fO6m03N)

#### 你可能感兴趣的

* [![]()

  恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)
* [![]()

  Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)
* [![]()

  Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)
* [![]()

  年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)
* [![]()

  ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)
* [![]()

  九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)
  2025-12-02 12:00:00
* [Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)
  2025-12-02 11:59:00
* [Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)
  2025-11-28 12:01:00
* [年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)
  2025-11-28 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)

  胡金鱼
* [Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)

  胡金鱼
* [Shai-Hulud供应链攻击再升级 数百款知名npm包遭恶意篡改](https://www.4hou.com/posts/VW39)

  胡金鱼
* [年访问量 2600 万的电视盗版流媒体平台Photocall遭联合查处后停运](https://www.4hou.com/posts/OG3G)

  胡金鱼
* [ClickFix 攻击借仿冒 Windows 更新界面推送恶意软件](https://www.4hou.com/posts/RX30)

  胡金鱼
* [九国联合行动摧毁千余台恶意软件服务器](https://www.4hou.com/posts/xyKn)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)