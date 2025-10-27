---
title: 恶意 PyPI 包窃取了 AWS 密钥
url: https://www.4hou.com/posts/NG5m
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-15
fetch_date: 2025-10-06T19:17:06.127789
---

# 恶意 PyPI 包窃取了 AWS 密钥

恶意 PyPI 包窃取了 AWS 密钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 恶意 PyPI 包窃取了 AWS 密钥

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-11-14 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)136350

收藏

导语：该软件包已被下载超过 37,000 次，并执行 Windows 和 Linux 平台特定的脚本。

自 2021 年以来，一个名为“fabrice”的恶意 Python 包一直出现在 Python 包索引 (PyPI) 中，从开发人员那里窃取 Amazon Web Services 凭证。

据应用安全公司 Socket 称，该软件包已被下载超过 37,000 次，并执行 Windows 和 Linux 平台特定的脚本。

大量下载是由于fabrice 对合法的SSH 远程服务器管理包“fabric”进行错字造成的，这是一个非常受欢迎的库，下载量超过2 亿次。

该 Fabrice 之所以长期未被检测到，是因为在 PyPI 上首次提交后就部署了先进的扫描工具，而且很少有解决方案进行追溯扫描。

**操作系统特定的行为**

Fabrice 包旨在根据其运行的操作系统执行操作。在 Linux 上，它在“~/.local/bin/vscode”处设置一个隐藏目录，用于存储分割成多个文件的编码 shell 脚本，这些文件是从外部服务器 (89.44.9[.]227) 检索的。

研究人员解释说，shell 脚本被解码并授予执行权限，让攻击者能够以用户权限执行命令。

在 Windows 上，fabrice 下载编码的有效负载 (base64)，该有效负载是为启动隐藏的 Python 脚本 (d.py) 而创建的 VBScript (p.vbs)。 Python 脚本负责获取恶意可执行文件（“chrome.exe”），该可执行文件被放入受害者的下载文件夹中。

其目的是安排 Windows 任务每 15 分钟执行一次，以确保重新启动后的持久性。

**AWS凭证被盗**

无论使用哪种操作系统，fabrice 的主要目标都是使用“boto3”（Amazon Web Services 的官方 Python SDK）窃取 AWS 凭证，从而允许与平台进行交互和会话管理。

Boto3 会话初始化后，它会自动从环境、实例元数据或其他配置的源中提取 AWS 凭证。然后，攻击者将窃取的密钥泄露到 VPN 服务器（由巴黎的 M247 运营），这使得追踪目的地变得更加困难。

![trigger.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241112/1731395415124112.png "1731395389221910.png")

Python函数窃取AWS凭证

当用户检查从 PyPI 下载的包时，可以降低拼写错误的风险。另一种选择是专门为检测和阻止此类威胁而创建的工具。

在保护 AWS 存储库免遭未经授权的访问方面，管理员应考虑使用 AWS Identity and Access Management (IAM) 来管理资源权限。

文章翻译自：https://www.bleepingcomputer.com/news/security/malicious-pypi-package-with-37-000-downloads-steals-aws-keys/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?obuH9qEE)

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