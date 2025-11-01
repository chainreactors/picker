---
title: 开源！可信MCP，AICC机密计算新升级！
url: https://www.4hou.com/posts/J15l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-10-31
fetch_date: 2025-11-01T03:11:05.516034
---

# 开源！可信MCP，AICC机密计算新升级！

开源！可信MCP，AICC机密计算新升级！ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
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

# 开源！可信MCP，AICC机密计算新升级！

企业资讯
[行业](https://www.4hou.com/category/industry)
17小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)5723

收藏

导语：火山引擎 AICC 机密计算迎来新升级，发布支持 MCP 的可信方案——Trusted MCP，并正式开源该组件。

大模型技术变革下，通常需借助云端算力和存储资源，为端侧提供更丰富的大模型应用场景体验。与此同时，行业对端云协作下的全链路安全和透明可信提出了更高要求。火山引擎AICC 机密计算应运而生，通过为企业搭建“云端大模型安全屋”，实现公有云环境下敏感数据流转和计算的全链路安全。

近日，火山引擎 AICC 机密计算迎来新升级，发布支持 MCP 的可信方案——Trusted MCP，并正式开源该组件。开发者和企业可通过该功能实现 MCP 核心组件及组件间的通信数据安全，有效解决 MCP 应用过程中的数据泄露和身份验证等风险。新版本已在火山引擎官网上线，

GitHub地址：<https://github.com/volcengine/AICC-Trusted-MCP>

**构建可信 MCP，发布即开源**

随着MCP作为模型上下文协议被广泛采纳，AI调用大模型和工具变得更加便捷和频繁，这也引发了安全隐患：模型通过MCP协议与外部系统实时交互，安全边界从 “单一模型服务器” 拓展至 “全链路交互场景”。传统安全防护聚焦于“模型本身”，而MCP生态的攻击面将贯穿大模型应用的全周期，安全风险指数级增加。

对此，AICC 机密计算上线Trusted MCP （可信MCP），通过实现MCP本身及MCP组件间的安全通信，进一步支持智能体安全落地。

Trusted MCP是在AICC机密计算基础上实现的可信MCP解决方案，它充分利用AICC机密计算的端云互信等能力，为MCP的核心组件提供身份证明和证明验证能力，并在此基础上提供了全流程的通信加密，确保MCP核心组件及组件间的通信数据安全，解决MCP应用中服务身份不可信、数据被篡改、流量劫持、数据隐私泄露等安全风险。

![天气MCP-1030.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251031/1761902443214190.png "1761902182199389.png")

以天气查询的 Trusted MCP 交互场景举例

当前，AICC机密计算“Trusted MCP”核心代码在 GitHub 上全面开源。开源内容涵盖 Trusted MCP 整体框架、常用工具桥接示例以及权限控制插件，开发者可基于此快速集成内部工具，或参与共建更丰富的 MCP 工具仓库。

值得一提的是，针对安全增强版本的Trusted MCP，业务改造零成本，用户可通过轻量级SDK接入。

GitHub地址：<https://github.com/volcengine/AICC-Trusted-MCP>

**深化平台集成：AICC 助力火山方舟实现机密推理**

近日，火山方舟作为一站式大模型服务平台，将AICC机密计算技术原生内置于平台，在行业内率先推出MaaS原生的机密推理服务。用户在火山方舟选择“机密部署”方式，即可一键开启豆包大模型的机密推理服务。

该功能让用户在火山方舟可使用芯片级的机密推理服务，让企业隐私数据在云端获得与本地同等安全的计算保障，确保企业在火山方舟的数据“唯用户可见、唯用户所用、唯用户所有”。

同时，在火山方舟后台，当用户完成机密模型部署后，可生成实时可信验证报告，让用户了解到推理服务是否部署在硬件可信环境内，确保推理服务安全可信。

![火山方舟推理接入点安全审计页面.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251031/1761902447201456.png "1761902354145735.png")

火山方舟推理接入点安全审计页面

目前，AICC 机密计算已在PC、 手机、汽车等多个行业具备了丰富的落地实践。例如：

**·**联想个人可信云方案中，通过AICC 构建可信知识库，实现内容创建、密态存储到加密检索与输出的全流程隐私闭环。用户无需改变操作习惯，即可获得高效的智能反馈，实现“安全无感”的体验。

**·**OPPO AI 私密云项目中，为了给用户提供更好的AI服务，一些复杂请求需要通过云端大模型来进行AI推理，OPPO与火山引擎AICC携手打造私密计算云，用户数据通过密文方式端云传输，实现了用户复杂需求在云上推理计算，同时满足用户数据在云上计算不留痕的高标准要求。

**·**上汽大众基于豆包大模型打造智能知识助手“SVW Copilot•出众”，用于响应员工对于企业内部各业务领域知识库的提问，帮助员工提升办公事务效率。火山方舟机密推理服务帮助上汽大众盘活内部知识，在保障内部数据隐私与安全的前提下，实现了企业知识资源的智能化、分级化利用。

秉承“芯片级全链路加密”理念，火山引擎 AICC 机密计算将持续聚焦智能计算底座的高可用、高性能与开放性，为企业接入和应用大模型，做好端到端的可信智能链路护航。

AICC官网体验地址：https://www.volcengine.com/product/AICC

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2LBKnG7Q)

#### 你可能感兴趣的

* [![]()

  开源！可信MCP，AICC机密计算新升级！](https://www.4hou.com/posts/J15l)
* [![]()

  360助力石家庄市教育行业网络安全运营中心启航，共筑教育安全新防线](https://www.4hou.com/posts/Ey4K)
* [![]()

  Q4最后一波福利！CACTER恶意样本活动水果/周边/现金奖励等你来拿](https://www.4hou.com/posts/Dx4Y)
* [![]()

  行业实践｜构建一体化数据防泄漏体系，某省医保局与梆梆安全携手护航移动业务安全发展](https://www.4hou.com/posts/wxWm)
* [![]()

  2025Q3企业邮箱安全报告：境外威胁新格局！这几点风险速查](https://www.4hou.com/posts/xyXn)
* [![]()

  行业实践｜梆梆安全助力某股份制银行构筑零售金融3.0移动安全防线](https://www.4hou.com/posts/vwVg)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [开源！可信MCP，AICC机密计算新升级！](https://www.4hou.com/posts/J15l)
  2025-10-31 17:28:17
* [360助力石家庄市教育行业网络安全运营中心启航，共筑教育安全新防线](https://www.4hou.com/posts/Ey4K)
  2025-10-31 10:29:31
* [Q4最后一波福利！CACTER恶意样本活动水果/周边/现金奖励等你来拿](https://www.4hou.com/posts/Dx4Y)
  2025-10-31 10:22:16
* [行业实践｜构建一体化数据防泄漏体系，某省医保局与梆梆安全携手护航移动业务安全发展](https://www.4hou.com/posts/wxWm)
  2025-10-29 16:56:09

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [开源！可信MCP，AICC机密计算新升级！](https://www.4hou.com/posts/J15l)

  企业资讯
* [360助力石家庄市教育行业网络安全运营中心启航，共筑教育安全新防线](https://www.4hou.com/posts/Ey4K)

  企业资讯
* [Q4最后一波福利！CACTER恶意样本活动水果/周边/现金奖励等你来拿](https://www.4hou.com/posts/Dx4Y)

  CACTER
* [行业实践｜构建一体化数据防泄漏体系，某省医保局与梆梆安全携手护航移动业务安全发展](https://www.4hou.com/posts/wxWm)

  梆梆安全
* [2025Q3企业邮箱安全报告：境外威胁新格局！这几点风险速查](https://www.4hou.com/posts/xyXn)

  CACTER
* [行业实践｜梆梆安全助力某股份制银行构筑零售金融3.0移动安全防线](https://www.4hou.com/posts/vwVg)

  梆梆安全

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