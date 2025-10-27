---
title: 苹果iOS16曝出新漏洞：飞行模式下依旧可连接网络
url: https://www.freebuf.com/news/375357.html
source: FreeBuf网络安全行业门户
date: 2023-08-19
fetch_date: 2025-10-04T12:00:25.483547
---

# 苹果iOS16曝出新漏洞：飞行模式下依旧可连接网络

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

苹果iOS16曝出新漏洞：飞行模式下依旧可连接网络

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

苹果iOS16曝出新漏洞：飞行模式下依旧可连接网络

2023-08-18 10:54:11

所属地 上海

![1692329895_64dee7a79695912c7a8a8.png!small](https://image.3001.net/images/20230818/1692329895_64dee7a79695912c7a8a8.png!small)

近日，网络安全研究人员发现iOS 16存在一种新的漏洞利用后持久化技术，即使受害者的苹果设备处于离线状态，也可以利用该技术悄无声息地访问该设备。

Jamf Threat Labs 的研究人员 Hu Ke 和 Nir Avraham 在与 The Hacker News 分享的一份报告中提到：这种方法诱使受害者认为他们设备的飞行模式正常工作，而实际上攻击者在成功利用设备后已经植入了一个虚假的人工飞行模式，该模式会编辑用户界面以显示飞行模式图标，并切断除攻击者应用程序外所有应用程序的互联网连接。

飞行模式允许用户关闭设备中的无线功能，从而有效阻止设备连接到 Wi-Fi 网络、蜂窝数据和蓝牙，以及收发电话和短信。

简而言之，Jamf 设计的这种方法会给用户造成一种 "飞行模式 "已开启的假象，但同时又允许恶意行为者悄悄地为恶意应用程序链接蜂窝网络。

研究人员解释说：当用户打开飞行模式时，网络接口 pdp\_ip0（蜂窝数据）将不再显示 ipv4/ipv6 ip 地址。蜂窝网络断开就无法使用，至少在用户看起来是这样。

虽然底层更改由 CommCenter 执行，但用户界面（UI）的修改，如图标转换，则由 SpringBoard 负责。

![1692329929_64dee7c96458b4c200af1.png!small](https://image.3001.net/images/20230818/1692329929_64dee7c96458b4c200af1.png!small)

因此，攻击的目的是设计一种人为的飞行模式，使用户界面的变化保持不变，但为通过其他方式安装在设备上的恶意有效载荷保留蜂窝连接。

研究人员说：在没有 Wi-Fi 连接的情况下启用飞行模式后，用户会认为打开 Safari 会显示无法连接互联网。然后会弹出一个通知窗口，提示用户关闭飞行模式。

为了实现这个情境，CommCenter 守护进程被用来阻止特定应用程序的蜂窝数据访问，并通过一个挂钩函数将其伪装成飞行模式，该函数会改变警报窗口，使其看起来就像飞行模式的设置已经被打开了。

值得注意的是，操作系统内核通过回调例程通知 CommCenter，CommCenter 再通知 SpringBoard 显示弹出窗口。

研究人员对 CommCenter 守护进程的进行仔细检查后还发现了一个SQL数据库的存在，该数据库用于记录每个应用程序的蜂窝数据访问状态（又称捆绑 ID），如果某个应用程序被阻止访问蜂窝数据，该数据库就会将标志值设置为 "8"。

利用这个已安装应用程序捆绑 ID 数据库，就可以使用以下代码有选择地阻止或允许应用程序访问 Wi-Fi 或蜂窝数据。

当与上述其他技术相结合时，这个虚假的'飞行模式'就会看起来与真实的'飞行模式'一样，只是互联网禁令不适用于非应用程序进程，例如后门木马。

> 参考来源：[New Apple iOS 16 Exploit Enables Stealthy Cellular Access Under Fake Airplane Mode (thehackernews.com)](https://thehackernews.com/2023/08/new-apple-ios-16-exploit-enables.html)

# 漏洞 # 漏洞利用 # 苹果漏洞

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