---
title: 恶意安卓应用程序假冒谷歌、Instagram、WhatsApp 窃取用户凭证
url: https://www.freebuf.com/news/400593.html
source: FreeBuf网络安全行业门户
date: 2024-05-12
fetch_date: 2025-10-06T17:16:30.442281
---

# 恶意安卓应用程序假冒谷歌、Instagram、WhatsApp 窃取用户凭证

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

恶意安卓应用程序假冒谷歌、Instagram、WhatsApp 窃取用户凭证

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

恶意安卓应用程序假冒谷歌、Instagram、WhatsApp 窃取用户凭证

2024-05-11 11:44:12

所属地 上海

![1715399532_663eeb6c758776f3a53fd.png!small](https://image.3001.net/images/20240511/1715399532_663eeb6c758776f3a53fd.png!small)

近日，研究人员发现有恶意安卓软件伪装成谷歌、Instagram、Snapchat、WhatsApp 和 X（前 Twitter）从受攻击的设备上窃取用户的凭据。

SonicWall Capture Labs威胁研究团队在最近的一份报告中提到：这种恶意软件利用著名的安卓应用程序图标误导用户，诱使受害者在其设备上安装恶意应用程序。

该活动的传播媒介目前尚不清楚。但一旦被安装到用户手机上，就会要求用户授予它访问辅助服务和设备管理员 API 的权限。

一旦获得到这些权限，恶意应用程序就能迅速地控制设备，从而在受害者不知情的情况下执行从数据窃取到恶意软件部署等任意操作。

该恶意软件旨在与命令与控制（C2）服务器建立连接，以接收执行命令，使其能够访问联系人列表、短信、通话记录、已安装应用程序列表；发送短信；在网页浏览器上打开钓鱼网页，以及切换摄像头闪光灯。

这些钓鱼网址模仿了 Facebook、GitHub、Instagram、LinkedIn、微软、Netflix、PayPal、Proton Mail、Snapchat、Tumblr、X、WordPress 和雅虎等知名服务的登录页面。

博通公司旗下的赛门铁克公司（Symantec）就社交工程活动发出警告，该活动利用 WhatsApp 作为传播媒介，冒充与防御相关的应用程序，传播一种新的安卓恶意软件。

赛门铁克公司表示：成功发送后，该应用程序将以通讯录应用程序的名义安装自己。执行后，该应用程序会请求短信、通讯录、存储和电话的权限，随后将自己从视图中删除。

这也是继发现传播 Coper 等安卓银行木马的恶意软件活动之后的又一次发现，Coper 能够收集敏感信息并显示虚假的窗口覆盖，欺骗用户在不知情的情况下交出他们的凭据。

上周，芬兰国家网络安全中心（NCSC-FI）披露，有人利用钓鱼短信将用户引向窃取银行数据的安卓恶意软件。

该攻击链利用了一种名为 "面向电话的攻击发送（TOAD）"的技术，短信会敦促收件人拨打一个与讨债有关的号码。一旦拨通电话，另一端的骗子会先告知受害者该短信是诈骗短信，随后受害者将会在手机上安装杀毒软件进行保护。

此外，他们还会让接听电话的人点击第二条短信中发送的链接来安装所谓的安全软件，但实际上该软件是恶意软件，其目的是窃取网上银行账户凭证，并最终进行未经授权的资金转移。

虽然 NCSC-FI 没有确定这次攻击中使用的安卓恶意软件是哪一个，但很可能是 Vultr 。上月初，NCC 集团详细说明了 Vultr 利用几乎相同的程序渗透设备的情况。

最近几个月，Tambir 和 Dwphon 等基于安卓的恶意软件也在野外被检测到，它们具有各种设备收集功能，后者针对的是中国手机制造商生产的手机，主要面向俄罗斯市场。

卡巴斯基说：Dwphon作为系统更新应用程序的一个组件，表现出预装安卓恶意软件的许多特征。虽然确切的感染路径尚不清楚，但可以推测，受感染的应用程序被纳入固件可能是供应链攻击的结果。

俄罗斯网络安全公司分析的遥测数据显示，受到银行恶意软件攻击的安卓用户数量比上一年增加了32%，从57219人跃升至75521人。据报告，大部分感染发生在土耳其、沙特阿拉伯、西班牙、瑞士和印度。

卡巴斯基指出：虽然受个人电脑银行恶意软件影响的用户数量持续下降，但2023 年，遭遇移动银行木马的用户数量大幅增加。

> 参考来源：[Malicious Android Apps Pose as Google, Instagram, WhatsApp to Steal Credentials](https://thehackernews.com/2024/05/malicious-android-apps-pose-as-google.html)

# 安卓恶意程序 # 安卓恶意软件

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)