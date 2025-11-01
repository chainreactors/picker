---
title: 黑客利用基于redtiger的信息窃取工具窃取Discord账户
url: https://www.4hou.com/posts/mkoA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-10-31
fetch_date: 2025-11-01T03:11:06.708355
---

# 黑客利用基于redtiger的信息窃取工具窃取Discord账户

黑客利用基于redtiger的信息窃取工具窃取Discord账户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用基于redtiger的信息窃取工具窃取Discord账户

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10496

收藏

导语：据报告，威胁者目前正滥用RedTiger的信息窃取模块，攻击目标主要集中在法国的Discord用户。

据安全研究员观察，攻击者正利用开源红队工具RedTiger，构建一款可窃取Discord账户数据与支付信息的信息窃取恶意软件。该恶意软件还能盗取浏览器中存储的凭证、加密货币钱包数据及游戏账号信息。

RedTiger是一款基于Python开发的渗透测试套件，支持Windows和Linux系统。其集成功能丰富，包括网络扫描、密码破解、开源情报（OSINT）相关工具、Discord专用工具，以及恶意软件生成器。

![RedTigerDiscord.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251027/1761552340677205.png "1761552043862299.png")

RedTiger中的Discord相关工具

其中的信息窃取模块具备标准窃取能力：可获取系统信息、浏览器Cookie与密码、加密货币钱包文件、游戏文件，以及Roblox和Discord相关数据。同时，它还能捕捉受害者的摄像头快照与屏幕截图。

尽管该项目在GitHub上标注其危险功能“仅允许合法使用”，但免费无限制的分发模式，加之缺乏任何防护机制，使其极易被恶意滥用。

**攻击目标与传播方式：聚焦法国Discord用户**

![Builder.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251027/1761552343159057.png "1761552085136036.png")

RedTiger 的恶意软件构建器

据报告，威胁者目前正滥用RedTiger的信息窃取模块，攻击目标主要集中在法国的Discord用户。攻击者通过PyInstaller将RedTiger的代码编译为独立可执行文件，并为其命名为与游戏或Discord相关的名称，以诱导用户点击。

关于该恶意软件的传播途径，尚未披露具体细节，但常见方式包括Discord频道、恶意软件下载网站、论坛帖子、恶意广告及YouTube视频。

**攻击流程：多维度窃取数据，通过云存储传输**

1. 植入与扫描：恶意软件植入受害者设备后，会扫描Discord相关文件与浏览器数据库文件；

2. 提取核心数据：通过正则表达式提取明文及加密的Discord令牌，验证有效性后，获取用户个人资料、邮箱、多因素认证状态与订阅信息；

3. 注入脚本拦截行为：向Discord的index.js文件注入自定义JavaScript代码，拦截API调用，捕捉登录尝试、购买操作甚至密码修改等事件，同时提取Discord中存储的支付信息（如PayPal账户、信用卡信息）；

![discorddata.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251027/1761552345151669.png "1761552184136995.png")

恶意软件针对的 Discord 数据

4. 拓展窃取范围：从浏览器中收集保存的密码、Cookie、浏览历史、信用卡信息及浏览器扩展程序数据，同时捕捉桌面截图，并扫描文件系统中的TXT、SQL及ZIP格式文件；

5. 数据传输：收集完所有数据后，恶意软件会将文件归档，上传至支持匿名上传的云存储服务GoFile，再通过Discord网络钩子（webhook）将下载链接与受害者元数据发送给攻击者。

**反检测机制：多重手段规避分析**

RedTiger具备完善的反检测能力：内置反沙箱机制，检测到调试器时会自动终止运行；同时会生成400个进程、创建100个随机文件，以此干扰取证分析工作。

![spam.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251027/1761552348737355.png "1761552246201748.png")

在主机上发送欺骗性文件和进程来源

用户应避免从未经验证的来源下载可执行文件或游戏工具，例如模组、“修改器”或“加速器”。疑似遭入侵后，应撤销Discord令牌，修改相关密码，并从官方网站重新安装Discord桌面客户端；清除浏览器中保存的各类数据；为所有账户启用多因素认证。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-steal-discord-accounts-with-redtiger-based-infostealer/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2JvtRsEO)

#### 你可能感兴趣的

* [![]()

  黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)
* [![]()

  超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)
* [![]()

  工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)
* [![]()

  新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)
* [![]()

  窃取加密货币的恶意 VSCode 插件在 OpenVSX 平台再度出现](https://www.4hou.com/posts/PGvz)
* [![]()

  国家安全机关破获美国国家安全局重大网络攻击案](https://www.4hou.com/posts/2X5J)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)
  2025-10-31 12:00:00
* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)
  2025-10-29 12:00:00
* [工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)
  2025-10-27 15:08:24
* [新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)
  2025-10-24 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)

  胡金鱼
* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)

  胡金鱼
* [工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)

  胡金鱼
* [新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)

  胡金鱼
* [窃取加密货币的恶意 VSCode 插件在 OpenVSX 平台再度出现](https://www.4hou.com/posts/PGvz)

  胡金鱼
* [国家安全机关破获美国国家安全局重大网络攻击案](https://www.4hou.com/posts/2X5J)

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