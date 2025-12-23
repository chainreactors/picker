---
title: 新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据
url: https://www.4hou.com/posts/RXEz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-22
fetch_date: 2025-12-23T03:23:57.418076
---

# 新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据

新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10312

收藏

导语：安全人员建议安卓用户：若非来源绝对可信，切勿从谷歌应用商店外的渠道侧载安装APK文件。

一款名为DroidLock的新型安卓恶意软件被安全人员发现，该软件不仅能锁屏勒索受害者赎金，还可获取短信、通话记录、联系人、音频录音等信息，甚至能直接删除设备数据。

DroidLock支持攻击者通过虚拟网络计算共享系统获得设备的完全控制权，同时还能在屏幕上生成悬浮层，以此窃取用户的锁屏图案。

研究人员指出，这款恶意软件的攻击目标为西班牙语用户，其传播渠道为恶意网站——这些网站通过推广仿冒合法应用的虚假安装包，诱导用户下载安装。

据了解，该恶意软件的感染流程始于一个投放程序，它会诱骗用户安装包含核心恶意载荷的次级程序。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251212/1765532783212578.png "1765532713132197.png")

Loader 应用（顶部）和 DroidLock 应用（底部）

恶意应用会以“应用更新”为借口植入主恶意载荷，随后申请设备管理员权限与辅助功能权限，凭借这些权限实施各类恶意操作。

借助已获取的权限，DroidLock可执行多种恶意行为，包括清空设备数据、锁定设备、修改个人识别码（PIN）、密码或生物识别信息，以此阻止用户访问自己的设备。

分析显示，DroidLock内置15条可执行命令，涵盖发送通知、在屏幕生成悬浮层、静音设备、恢复出厂设置、启动摄像头、卸载应用等操作。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251212/1765532789348995.png "1765532748178197.png")

DroidLock 支持的命令

一旦接收到对应的勒索指令，该恶意软件会通过网页视图立即弹出勒索悬浮窗口，要求受害者通过一个Proton邮箱地址联系攻击者。若受害者未能在24小时内支付赎金，攻击者便威胁会永久销毁设备内的文件。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251212/1765532792169007.png "1765532792169007.png")

DroidLock的勒索覆盖

DroidLock并不会对文件进行加密，而是以销毁文件为要挟索要赎金，最终达成与传统勒索软件相同的目的。除此之外，攻击者还可通过修改设备锁屏密码，完全剥夺用户对设备的访问权限。

该恶意软件窃取锁屏图案的功能，是通过加载恶意安装包资源目录中的另一悬浮层实现的。当用户在这个仿冒的锁屏界面绘制解锁图案时，图案信息会被直接发送给攻击者。攻击者设计这一功能，是为了能在设备闲置时段通过VNC实现远程访问。

安全人员建议安卓用户：若非来源绝对可信，切勿从谷歌应用商店外的渠道下载安装APK文件；安装应用时，务必核查其申请的权限是否与功能匹配；同时应定期使用谷歌应用防护服务对设备进行安全扫描。

文章来源自：https://www.bleepingcomputer.com/news/security/new-droidlock-malware-locks-android-devices-and-demands-a-ransom/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UvT0PSos)

#### 你可能感兴趣的

* [![]()

  快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)
* [![]()

  新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)
* [![]()

  VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)
* [![]()

  MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)
* [![]()

  勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)
* [![]()

  新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)
  2025-12-23 10:36:49
* [新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)
  2025-12-22 12:00:00
* [VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)
  2025-12-18 11:59:00
* [MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)
  2025-12-17 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [快手平台深夜遭黑灰产攻击，平台紧急修复并报警](https://www.4hou.com/posts/mkDE)

  山卡拉
* [新型恶意软件DroidLock锁定安卓设备窃取多类敏感数据](https://www.4hou.com/posts/RXEz)

  胡金鱼
* [VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)

  胡金鱼
* [MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)

  胡金鱼
* [勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)

  胡金鱼
* [新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)

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