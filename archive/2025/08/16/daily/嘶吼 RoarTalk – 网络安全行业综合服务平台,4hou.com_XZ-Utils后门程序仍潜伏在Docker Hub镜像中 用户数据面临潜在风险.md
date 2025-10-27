---
title: XZ-Utils后门程序仍潜伏在Docker Hub镜像中 用户数据面临潜在风险
url: https://www.4hou.com/posts/om4K
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-16
fetch_date: 2025-10-07T00:17:48.096240
---

# XZ-Utils后门程序仍潜伏在Docker Hub镜像中 用户数据面临潜在风险

XZ-Utils后门程序仍潜伏在Docker Hub镜像中 用户数据面临潜在风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# XZ-Utils后门程序仍潜伏在Docker Hub镜像中 用户数据面临潜在风险

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)58686

收藏

导语：Binarly的研究人员发现，仍有大量Docker镜像受到XZ-Utils后门程序的影响。

2024年3月首次被发现的XZ-Utils后门程序，目前仍存在于Docker Hub上至少35个Linux系统中，这可能会将用户数据置于风险之中。

Docker Hub是由Docker运营的官方公共容器镜像仓库，开发者和企业可在此上传或下载预构建的镜像，并与社区共享。

许多CI/CD流水线、开发者及生产系统会直接从Docker Hub拉取镜像，将其作为自有容器的基础层。若这些镜像存在安全漏洞，新构建的容器也会继承其中的漏洞或恶意代码。Binarly的研究人员发现，仍有大量Docker镜像受到XZ-Utils后门程序的影响。

Binarly在报告中指出：“如果发行版软件包被植入后门，那么任何基于这些包构建的Docker镜像也会受到感染。然而，我们发现部分受感染的镜像仍在Docker Hub上公开可用，而其他镜像又以这些受感染的基础镜像为基础进行构建，导致感染范围进一步扩大。”

Binarly已将这些镜像报告给Debian（仍在提供带后门程序镜像的维护者之一），但Debian以风险较低且需保证归档连续性为由，决定不将这些镜像下线。

XZ-Utils后门程序（追踪编号为CVE-2024-3094）是隐藏在xz-utils压缩工具（5.6.0和5.6.1版本）的liblzma.so库中的恶意代码。

它通过glibc的IFUNC机制挂钩OpenSSH中的RSA\_public\_decrypt函数，因此，若拥有特殊私钥的攻击者通过SSH连接到受影响的系统，他们便能绕过身份验证，以root权限远程执行命令。

该后门程序由长期参与项目的贡献者“Jia Tan”秘密植入，并被包含在Debian、Fedora、OpenSUSE和Red Hat等官方Linux发行版软件包中，使其成为去年最严重的软件供应链安全事件之一。

由于后门程序发现及时，攻击者几乎没有机会利用它。Binarly、卡巴斯基等机构还发布了扫描工具，以帮助检测依赖的开源软件中是否存在该后门。

**Debian的回应**

令研究人员感到意外的是，Debian并未从Docker Hub撤回使用带后门版本库的64位镜像，目前至少有35个此类镜像仍可下载。

Binarly表示，这一数字仅部分反映了问题的实际规模，因为他们并未对平台上的所有镜像进行XZ-Utils后门程序扫描。

Binarly在报告中解释道：“我们发现了超过35个包含后门程序的镜像。虽然这个数字看似不大，但我们仅扫描了Docker Hub上发布的一小部分镜像，且只到二级镜像就停止了。”

Debian称，他们有意选择不从Docker Hub移除这些镜像，而是将其作为历史产物保留，并告知用户仅使用最新的镜像，而非旧版本。

维护者做出这一决定的原因是，他们认为该后门程序被利用的条件不太可能满足，例如需要容器中安装并运行sshd、攻击者能够网络访问该容器上的SSH服务，以及使用与后门触发逻辑匹配的私钥等。

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250813/1755071663774970.png "1755071663774970.png")

Debian维护者的回应

但Binarly不同意这种做法，他们强调，仅仅让这些镜像可被公众获取，就会因意外拉取或在自动构建中使用而带来重大风险。

这一情况同样适用于所有可能包含受感染版本XZ-Utils后门程序的镜像，因此用户应手动检查，确保所用库的版本为5.6.2或更高（最新稳定版为5.8.1）。

文章翻译自：https://www.bleepingcomputer.com/news/security/docker-hub-still-hosts-dozens-of-linux-images-with-the-xz-backdoor/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0EluiSfG)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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