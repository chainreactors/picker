---
title: 恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器
url: https://www.4hou.com/posts/LG4W
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-06
fetch_date: 2025-11-07T03:09:08.951474
---

# 恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器

恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9322

收藏

导语：建议曾下载过上述任何一款恶意包的开发者立即清理感染文件，并轮换所有访问令牌和密码，因为这些凭证极有可能已被泄露。

近期，npm注册表中出现10款模仿合法软件项目的恶意包，它们会下载一款信息窃取组件，从Windows、Linux和macOS系统中收集敏感数据。

这些恶意包于7月4日被上传至npm平台，因采用多层混淆技术躲过标准静态分析机制，长期未被发现。据网络安全公司Socket的研究人员透露，这10款恶意包的下载量已接近1万次，能够窃取系统密钥环、浏览器及身份验证服务中的凭证信息。

截至本文撰写时，尽管Socket已向npm平台报告相关情况，但以下恶意包仍可获取：

1. typescriptjs

2. deezcord.js

3. dizcordjs

4. dezcord.js

5. etherdjs

6. ethesjs

7. ethetsjs

8. nodemonjs

9. react-router-dom.js

10. zustand.js

Socket研究人员表示，这些恶意包通过虚假验证码验证伪装成合法程序，进而下载一款以PyInstaller打包的24MB信息窃取器。

攻击者为诱骗用户下载，采用了“拼写劫持”（typosquatting）手段——利用多款知名软件的名称拼写错误或变体命名恶意包。涉及的合法软件包括TypeScript（JavaScript的类型化超集）、discord.js（Discord机器人开发库）、ethers.js（以太坊JavaScript开发库）、nodemon（Node应用自动重启工具）、react-router-dom（React浏览器路由工具）及zustand（轻量React状态管理工具）。

开发者在npm平台搜索这些合法包时，可能因拼写失误或直接选择搜索结果中的恶意包而中招。恶意包安装后，会自动触发“postinstall”脚本，生成一个与主机检测到的操作系统匹配的新终端。该脚本在可见的安装日志之外执行“app.js”文件，并立即清空窗口以规避检测。

“app.js”文件是恶意软件加载器，采用四层混淆技术：自解码eval包装器、动态生成密钥的XOR解密、URL编码载荷以及深度控制流混淆。

脚本会通过ASCII码在终端显示虚假验证码，为安装过程制造合法假象。

![ascii-captcha.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251103/1762159491107426.jpg "1762159491107426.jpg")

虚假的 ASCII 验证码步骤

随后，它会将受害者的地理位置和系统指纹信息发送至攻击者的命令与控制（C2）服务器。获取这些信息后，恶意软件会从外部来源下载并自动启动特定于平台的二进制文件，该文件是一款以PyInstaller打包的24MB可执行程序。

这款信息窃取器的攻击目标包括各类系统密钥环（如Windows凭据管理器、macOS钥匙串、Linux SecretService、libsecret及KWallet），以及基于Chromium内核的浏览器和Firefox浏览器中存储的数据（包括用户配置文件、保存的密码和会话Cookie）。

此外，它还会在常见目录中搜索SSH密钥，并尝试查找和窃取OAuth令牌、JWT令牌及其他API令牌。

被盗取的信息会被打包成压缩文件，先临时存储在/var/tmp或/usr/tmp目录，随后被窃取至攻击者的服务器（IP地址：195[.]133[.]79[.]43）。

建议曾下载过上述任何一款恶意包的开发者立即清理感染文件，并轮换所有访问令牌和密码，因为这些凭证极有可能已被泄露。

从npm或其他开源索引获取包时，建议仔细核对名称是否存在拼写错误，并确保所有包均来自可靠的发布者和官方仓库。

文章翻译自：https://www.bleepingcomputer.com/news/security/malicious-npm-packages-fetch-infostealer-for-windows-linux-macos/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?MoNqWLiJ)

#### 你可能感兴趣的

* [![]()

  恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)
* [![]()

  Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
* [![]()

  8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)
* [![]()

  黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)
* [![]()

  超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)
* [![]()

  工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)
  2025-11-06 12:00:00
* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
  2025-11-05 12:00:00
* [8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)
  2025-11-05 10:37:58
* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)
  2025-10-31 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)

  胡金鱼
* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)

  胡金鱼
* [8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)

  胡金鱼
* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)

  胡金鱼
* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)

  胡金鱼
* [工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)

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