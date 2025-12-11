---
title: Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露
url: https://www.4hou.com/posts/gylZ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-10
fetch_date: 2025-12-11T03:23:12.691741
---

# Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露

Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10818

收藏

导语：在第二轮攻击中，受恶意软件影响的软件包数量超800个（含同一软件包的所有受感染版本）。

上周发生的第二轮Shai-Hulud攻击事件，在感染NPM（Node包管理器）仓库数百个软件包后，导致约40万条原始敏感凭证泄露，且被盗数据被公开至3万个GitHub代码仓库中。

尽管开源扫描工具TruffleHog仅验证出约1万条泄露凭证为有效状态，但云安全平台Wiz的研究人员指出，截至12月1日，超过60%的泄露NPM令牌仍处于有效可用状态。

**从自传播感染到破坏性.payload**

Shai-Hulud威胁最早于9月中旬浮出水面，当时攻击者通过自传播恶意载荷攻陷了187个NPM软件包——该载荷会利用TruffleHog工具识别账户令牌，向软件包中注入恶意脚本并自动在平台发布。

而在第二轮攻击中，受恶意软件影响的软件包数量超800个（含同一软件包的所有受感染版本），且恶意程序新增了破坏性机制：当满足特定条件时，会清空受害者主机的主目录。

**泄露凭证的类型与分布**

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764750616678607.png "1764750204197917.png")

新 GitHub 账户在新仓库上发布机密信息的速度

Wiz研究人员对Shai-Hulud2.0攻击扩散至3万个GitHub仓库的凭证泄露数据展开分析，发现泄露的敏感信息包含以下类型：

1.  约70%的仓库中存在contents.json文件，内含GitHub用户名、令牌及文件快照；

2.  半数仓库包含truffleSecrets.json文件，存储了TruffleHog的扫描结果；

3.  80%的仓库存有environment.json文件，涵盖操作系统信息、CI/CD元数据、NPM包元数据及GitHub身份凭证；

4.  400个仓库托管了actionsSecrets.json文件，包含GitHub Actions工作流密钥。

该恶意软件调用TruffleHog时未启用-only-verified参数，这意味着40万条泄露凭证仅符合已知格式规范，未必仍具备有效性或可使用性。

尽管这批凭证数据存在大量无效信息，需进行大量去重工作，但其中仍包含数百条有效凭证，涵盖云服务密钥、NPM令牌及版本控制系统（VCS）身份凭证。截至目前，这些凭证已构成供应链进一步遭袭的现实风险，例如研究员监测到超60%的泄露NPM令牌仍处于有效状态。

**感染设备与环境特征**

对2.4万个environment.json文件的分析显示，约半数文件为唯一实例，其中23%对应开发者本地设备，其余则来自CI/CD运行器等基础设施。

研究人员汇总的数据表明，87%的受感染设备为Linux系统，而76%的感染案例发生在容器环境中。

在CI/CD平台分布方面，GitHub Actions占比遥遥领先，其次为Jenkins、GitLab CI及AWS CodeBuild。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764750620113673.png "1764750230119810.png")

受影响的CI/CD平台

从感染对象来看，受影响最严重的软件包为@postman/[[email protected]](/cdn-cgi/l/email-protection)和@asyncapi/[[email protected]](/cdn-cgi/l/email-protection)，这两款软件包的感染量合计占所有感染案例的60%以上。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251203/1764750623140615.png "1764750277508755.png")

感染包的流行率

研究人员据此认为，若能及早识别并管控这几个核心软件包，Shai-Hulud的攻击影响本可大幅降低。此外，从感染模式来看，99%的感染实例均源于preinstall事件触发的node setup\_bun.js脚本执行，极少数例外情况大概率为攻击者的测试尝试。

Wiz认为，Shai-Hulud幕后攻击者会持续优化并演进攻击手段，且预计短期内将出现更多攻击波次，甚至可能利用已窃取的海量凭证发起新一轮攻击。

文章来源自：https://www.bleepingcomputer.com/news/security/shai-hulud-20-npm-malware-attack-exposed-up-to-400-000-dev-secrets/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?w37K0ST9)

#### 你可能感兴趣的

* [![]()

  Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)
* [![]()

  安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)
* [![]()

  国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)
* [![]()

  Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)
* [![]()

  国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)
* [![]()

  恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)
  2025-12-10 12:00:00
* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)
  2025-12-05 12:00:00
* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)
  2025-12-05 10:28:08
* [Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)
  2025-12-04 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Shai-Hulud第二轮攻击波及NPM生态 40万条敏感凭证遭泄露](https://www.4hou.com/posts/gylZ)

  胡金鱼
* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)

  胡金鱼
* [Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)

  胡金鱼
* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)

  胡金鱼
* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)

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