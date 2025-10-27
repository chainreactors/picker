---
title: 黑客使用新的IceBreaker恶意软件攻击博彩公司
url: https://www.4hou.com/posts/ykKE
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-11
fetch_date: 2025-10-04T06:18:46.739698
---

# 黑客使用新的IceBreaker恶意软件攻击博彩公司

黑客使用新的IceBreaker恶意软件攻击博彩公司 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客使用新的IceBreaker恶意软件攻击博彩公司

布加迪
[新闻](https://www.4hou.com/category/news)
2023-02-10 11:11:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)187180

收藏

导语：黑客们近期一直在使用一种前所未见的IceBreaker（“破冰船”）后门攻击在线博彩公司。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675285959173050.png "1675285959173050.png")

黑客们近期一直在攻击在线博彩公司，他们使用了一种似乎前所未见的后门，研究人员将其命名为IceBreaker（“破冰船”）。

这种攻击方法依赖这种手段：威胁分子以面临问题的用户为幌子，欺骗客户服务工作人员打开他们发送的恶意截图。

这种攻击至少从2022年9月以来就出现了。其背后的组织依然身份不明，只有依稀模糊的线索指明其源头。

事件响应公司Security Joes的研究人员认为，IceBreaker后门是一个新的高级威胁团伙的杰作，他们使用了“一种非常特别的社会工程伎俩技术”。如果深入分析这种技术，有望更清楚地了解这伙人是谁。

Security Joes在分析了来自去年9月份发生的一起事件的数据后，抢在这伙黑客攻陷目标之前成功应对了另外三起攻击。

研究人员表示，他们能找到的关于IceBreaker威胁分子的唯一公开证据是去年10月份MalwareHunterTeam上的一条推文（https://twitter.com/malwrhunterteam/status/1576984214351724546）。

**欺骗客户服务**

为了投放后门，威胁分子冒充是用户，声称登录或注册在线服务遇到了问题，于是联系目标公司的客户支持人员。

黑客说服支持工作人员下载一个图片，声称该图片可以更清楚地描述问题。研究人员表示，该图片通常托管在一个冒充合法服务的虚假网站上，不过他们还发现该图片来自Dropbox存储平台。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675285862259528.png "1675285862259528.png")

图1. IceBreaker的作案手法（图片来源：Security Joes）

Security Joes表示，他们仔细分析了威胁分子与支持工作人员之间的对话，结果发现IceBreaker的母语不是英语，却故意要求与说西班牙语的工作人员交谈。然而研究人员发现，他们还说其他语言。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675285854994566.png "1675285854994566.png")

图2. IceBreaker使用法语与工作人员聊天（图片来源：Security Joes）

以这种方式投放的链接会导致一个含有恶意LNK文件的ZIP压缩包，该恶意文件获取IceBreaker后门，这其实是一个Visual Basic脚本，下载至少自2013年以来就一直处于活跃状态的Houdini远程访问木马（RAT）。

如下图所示，Windows快捷方式文件的图标已被更改，使其看起来没有什么害处。该快捷方式包含从攻击者的服务器下载MSI载荷的命令，在没有用户交互的情况下安装载荷，并在没有用户界面的情况下运行它。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675285845980221.png "1675285845980221.png")

图3. LNK文件（Screenshot.jpg）的属性（图片来源：Security Joes）

Security Joes的研究人员表示，下载的恶意软件是“一个高度复杂的编译过的JavaScript文件”：除了运行从攻击者的服务器获取的脚本外，该文件还可以发现运行中的进程，窃取密码、cookie和文件，并为攻击者打开代理隧道。

**IceBreaker后门**

恶意LNK是投放IceBreaker恶意软件的主要第一阶段载荷，而VBS文件被用作后备手段，以防客户支持人员无法运行快捷方式文件。

这个恶意快捷方式文件冒充是JPG图片，并相应地修改了其扩展名。它下载的MSI载荷在Virus Total在线扫描平台上的检测率非常低，在60次扫描中只有4次被检测出来。

MSI包里面有一大堆的诱饵文件，以逃避基于特征码的检测工具和分析引擎。最后一层是提取到受害者临时文件夹中的CAB压缩包，负责投放“Port.exe”载荷。

Security Joes表示，这是一个C++ 64位可执行文件，有不同寻常的覆盖层，保留了附加到文件末尾的部分数据。分析人员认为，这是一种隐藏额外资源以免被安全产品发现的方法。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675285828196704.png "1675285828196704.png")

图4. Port.exe文件的属性（图片来源：Security Joes）

Security Joes在进一步分析后发现，该样本是一个前所未见的用Node.js编写的模块后门，为威胁分子提供了以下功能：

• 通过扩展恶意软件内置功能的插件进行定制。

• 发现进程。

• 从本地存储环境窃取密码和cookie，特别是谷歌Chrome。

• 启用Socks5反向代理服务器。

• 通过在Windows启动文件夹中创建一个新的LNK文件（WINN.lnk），实现持久性。

• 通过web套接字将文件泄露到远程服务器。

• 执行自定义VBS脚本。

• 获取屏幕截图。

• 生成远程shell会话。

如果被攻击的对象没有将客户支持服务外包给外部提供商，威胁分子就可以使用该后门窃取帐户凭据、在网络中横向移动，并扩大入侵范围。

目前关于IceBreaker组织的信息还不多，但Security Joes决定发布分析报告，并披露所有已获取的攻陷指标（IoC），以帮助防御者发现和应对这个威胁。

研究人员已经发布了一份技术报告（https://www.securityjoes.com/post/operation-ice-breaker-targets-the-gam-bl-ing-industry-right-before-it-s-biggest-gathering），描述了这伙威胁分子的作案手法及其后门的工作机理。YARA规则也已发布，以帮助组织检测恶意软件。

此外，Security Joes建议怀疑遭到了IceBreaker攻击的公司寻找在启动文件夹中创建的快捷方式文件，并检查未授权执行开源工具tsocks.exe的情形。

应密切关注msiexec.exe进程的创建（这也是一种攻陷指标），该进程接收URL作为参数，还应密切关注从临时文件夹启动的VBS脚本和LNK文件的执行。

本文翻译自：https://www.bleepingcomputer.com/news/security/hackers-use-new-icebreaker-malware-to-breach-gaming-companies/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iOiFgi9S)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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