---
title: GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次
url: https://www.4hou.com/posts/YZg9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-14
fetch_date: 2025-11-15T03:07:27.525349
---

# GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次

GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8420

收藏

导语：攻击者已重返OpenVSX平台，沿用原有基础设施，但更新了命令与控制服务器端点及Solana交易信息。

上月曾入侵OpenVSX与Visual Studio Code应用市场的GlassWorm恶意软件攻击活动再度回归，此次新增三款携带恶意载荷的VSCode扩展，累计下载量已超1万次。

GlassWorm是一套恶意软件攻击体系，通过Solana区块链交易获取恶意载荷，攻击目标包括GitHub、NPM、OpenVSX平台的账号凭证，以及49款扩展程序中的加密货币钱包数据。

该恶意软件利用不可见的Unicode字符（显示为空白但可作为JavaScript执行）实施恶意操作。

其首次现身时，通过微软VS Code与OpenVSX应用市场的12款扩展传播，下载量达3.58万次。不过有观点认为，攻击者人为刷高了下载数据，因此该攻击活动的实际影响范围尚无法确定。

针对此次安全事件，OpenVSX已为受GlassWorm入侵的部分账号（具体数量未披露）轮换访问令牌，实施安全强化措施，并将该事件标记为已解决。

**GlassWorm再度来袭**

持续追踪该攻击活动的Koi Security表示，攻击者已重返OpenVSX平台，沿用原有基础设施，但更新了命令与控制（C2）服务器端点及Solana交易信息。

![hidden.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251110/1762762065964955.jpg "1762762027140666.jpg")

隐藏的有效负载

三款携带GlassWorm恶意载荷的OpenVSX扩展如下：

- ai-driven-dev.ai-driven-dev — 3400次下载

- adhamu.history-in-sublime-merge — 4000次下载

- yasuyuky.transient-emacs — 2400次下载

Koi Security指出，这三款扩展均采用与初代恶意文件相同的不可见Unicode字符混淆技术，且该技术仍能成功绕过OpenVSX新增的防御机制。

正如Aikido此前报告所述，GlassWorm操作者并未因上月的曝光而退缩，已转向GitHub平台活动。此次通过新扩展重返OpenVSX，表明其有意在多平台恢复攻击运营。

**攻击基础设施遭曝光**

借助匿名线索，Koi Security成功接入攻击者服务器，获取了该攻击活动受害者的关键数据。检索到的数据显示，GlassWorm的影响范围遍及全球，受害者系统分布于美国、南美洲、欧洲、亚洲，其中还包括中东地区的一个政府机构。

关于攻击者身份，Koi Security透露其为俄语使用者，采用RedExt开源浏览器扩展C2框架开展攻击。

![data.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251110/1762762075203265.jpg "1762762075203265.jpg")

来自暴露端点

研究人员已将所有获取的数据（包括多个加密货币交易所及即时通讯平台的用户ID）提交给执法部门，并正协调推进受影响机构的通知工作。

Koi Security透露，目前已确认60名独立受害者，同时指出此次仅从一个暴露的端点获取了部分受害者名单。目前，这三款携带GlassWorm恶意载荷的扩展仍可在OpenVSX平台下载。

文章翻译自：https://www.bleepingcomputer.com/news/security/glassworm-malware-returns-on-openvsx-with-3-new-vscode-extensions/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?kiqTSvOk)

#### 你可能感兴趣的

* [![]()

  GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)
* [![]()

  CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)
* [![]()

  NuGet平台现恶意包 暗藏破坏有效载荷](https://www.4hou.com/posts/VW69)
* [![]()

  国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/0MQG)
* [![]()

  Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)
* [![]()

  TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)
  2025-11-14 12:00:00
* [CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)
  2025-11-14 10:10:20
* [NuGet平台现恶意包 暗藏破坏有效载荷](https://www.4hou.com/posts/VW69)
  2025-11-13 12:00:00
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/0MQG)
  2025-11-13 10:34:14

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)

  胡金鱼
* [CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)

  胡金鱼
* [NuGet平台现恶意包 暗藏破坏有效载荷](https://www.4hou.com/posts/VW69)

  胡金鱼
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/0MQG)

  胡金鱼
* [Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)

  胡金鱼
* [TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)

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