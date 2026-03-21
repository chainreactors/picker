---
title: 仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包
url: https://www.4hou.com/posts/rpJL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-03-20
fetch_date: 2026-03-21T04:06:25.890837
---

# 仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包

仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-03-20 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9220

收藏

导语：由于PWA仅在打开时才能窃取剪贴板内容与验证码，攻击者可通过通知推送伪造安全警报，诱骗用户重新打开应用。

一场网络钓鱼活动正通过伪造谷歌账号安全页面，分发一款网页应用，该应用可窃取一次性验证码、采集加密货币钱包地址，并通过受害者浏览器转发攻击者流量。

此次攻击利用渐进式Web应用（PWA）特性与社会工程学手段，诱骗用户以为自己正在与合法的谷歌安全页面交互，从而在不知情中安装恶意程序。

PWA可在浏览器中运行，并能像独立桌面应用一样从网页直接安装，运行时独立成窗，不显示常规浏览器控件。

**受害者浏览器沦为攻击者代理**

该攻击以安全检测、加强设备防护为幌子，骗取用户授予所需权限。攻击者使用域名google-prism[.]com，伪装成谷歌官方安全服务，展示包含四步的设置流程，诱导用户授予高危权限并安装恶意PWA应用。部分场景下，该网站还会推送配套安卓应用，声称可“保护通讯录”。

安全研究人员表示，该PWA应用可窃取通讯录、实时GPS定位与剪贴板内容。其额外功能还包括充当网络代理与内网端口扫描器，使攻击者能够通过受害者浏览器转发请求，并探测内网存活主机。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260303/1772521099164712.png "1772521048937180.png")

仿冒谷歌安全网站索要剪贴板访问权限

该伪造网站还会申请读取剪贴板文本与图片的权限（仅应用打开时生效），同时请求通知权限，以便攻击者推送提醒、下发新任务或触发数据窃取。

此外，恶意程序会在支持的浏览器上利用WebOTP API尝试拦截短信验证码，并每30秒访问/api/heartbeat接口获取新指令。

由于PWA仅在打开时才能窃取剪贴板内容与验证码，攻击者可通过通知推送伪造安全警报，诱骗用户重新打开应用。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260303/1772521104711792.png "1772521077182746.png")

假冒谷歌安全网站要求通知权限

该恶意程序的核心目标是窃取一次性密码（OTP）与加密货币钱包地址，同时生成详细的设备指纹信息。

恶意PWA中还包含一个Service Worker组件，负责处理推送通知、执行载荷下发的任务，并在本地缓存窃取的数据以备外传。

研究人员表示，最危险的模块是WebSocket中继功能——它允许攻击者将网页请求透过受害者浏览器转发，如同直接身处受害者内网一般。

由于该Worker支持周期性后台同步，在基于Chromium内核的浏览器中，只要恶意PWA未卸载，攻击者便可长期控制受感染设备。

**安卓配套恶意软件**

选择开启全套账号安全功能的用户，还会收到一个安卓APK安装包，声称可扩展对通讯录的保护。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260303/1772521115724941.png "1772521115724941.png")

假意的安全检查

该载荷被包装为“关键安全更新”，并宣称经过谷歌认证，却要求申请33项权限，包括读取短信、通话记录、麦克风、通讯录以及无障碍服务。

仅这些权限就属于高危权限，可被用于数据窃取、设备完全沦陷与金融欺诈。

恶意APK包含多个模块：

**·**自定义键盘，用于记录按键

**·**通知监听器，获取所有 incoming 通知

**·**拦截自动填充凭据的服务

研究人员表示：

“为提升持久化能力，该APK会注册为设备管理员（增加卸载难度），设置开机自启，并通过闹钟机制在组件被杀死后重新拉起。”

研究人员还观察到可用于界面覆盖攻击的组件，表明攻击者计划在特定应用中实施凭证钓鱼。

**攻击特点与清理建议**

此次攻击完全依靠合法浏览器功能+社会工程学实现，无需利用任何漏洞，仅通过诱骗用户授权即可完成恶意行为。

研究人员提醒：即便不安装安卓APK，仅网页应用本身就足以窃取通讯录、拦截验证码、定位追踪、扫描内网并通过受害者设备代理流量。

用户需注意：谷歌不会通过网页弹窗执行安全检测，也不会要求安装任何软件以增强防护。所有安全工具均只在谷歌官方账号中心提供。

建议卸载安卓恶意程序：在应用列表中查找名为“Security Check”的应用并优先卸载；若存在包名为com.device.sync、名为“System Service”且拥有设备管理员权限的应用，先在「设置 > 安全 > 设备管理员」中撤销权限，再卸载。

文章来源自：https://www.bleepingcomputer.com/news/security/fake-google-security-site-uses-pwa-app-to-steal-credentials-mfa-codes/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?kVo8BjeC)

#### 你可能感兴趣的

* [![]()

  仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包](https://www.4hou.com/posts/rpJL)
* [![]()

  嘶吼安全动态｜马自达系统遭入侵，员工信息或泄露 Perseus安卓银行木马出现升级版](https://www.4hou.com/posts/XPjV)
* [![]()

  2026职场AI观察：禁而不止的影子代理，正在埋下企业数据安全隐患](https://www.4hou.com/posts/PG26)
* [![]()

  嘶吼安全动态｜官方辟谣“七部门AI安全治理三年行动计划” 新型iPhone攻击工具“DarkSword”曝光](https://www.4hou.com/posts/RX4w)
* [![]()

  假招聘真投毒！ Next.js 面试题暗藏后门实施入侵](https://www.4hou.com/posts/rpJW)
* [![]()

  AI时代中国网络安全产业的五年变局|| 网络安全投融资的残酷分流](https://www.4hou.com/posts/MXY1)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包](https://www.4hou.com/posts/rpJL)
  2026-03-20 12:01:00
* [嘶吼安全动态｜马自达系统遭入侵，员工信息或泄露 Perseus安卓银行木马出现升级版](https://www.4hou.com/posts/XPjV)
  2026-03-20 12:00:00
* [2026职场AI观察：禁而不止的影子代理，正在埋下企业数据安全隐患](https://www.4hou.com/posts/PG26)
  2026-03-19 12:01:00
* [嘶吼安全动态｜官方辟谣“七部门AI安全治理三年行动计划” 新型iPhone攻击工具“DarkSword”曝光](https://www.4hou.com/posts/RX4w)
  2026-03-19 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [仿冒谷歌账号钓鱼攻击：利用恶意PWA应用窃取验证码、加密货币钱包](https://www.4hou.com/posts/rpJL)

  胡金鱼
* [嘶吼安全动态｜马自达系统遭入侵，员工信息或泄露 Perseus安卓银行木马出现升级版](https://www.4hou.com/posts/XPjV)

  山卡拉
* [2026职场AI观察：禁而不止的影子代理，正在埋下企业数据安全隐患](https://www.4hou.com/posts/PG26)

  灵魂舞者
* [嘶吼安全动态｜官方辟谣“七部门AI安全治理三年行动计划” 新型iPhone攻击工具“DarkSword”曝光](https://www.4hou.com/posts/RX4w)

  山卡拉
* [假招聘真投毒！ Next.js 面试题暗藏后门实施入侵](https://www.4hou.com/posts/rpJW)

  胡金鱼
* [AI时代中国网络安全产业的五年变局|| 网络安全投融资的残酷分流](https://www.4hou.com/posts/MXY1)

  山卡拉

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