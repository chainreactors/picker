---
title: 基于Flutter的安卓恶意软件，瞄准东亚市场
url: https://www.freebuf.com/articles/370789.html
source: FreeBuf网络安全行业门户
date: 2023-07-01
fetch_date: 2025-10-04T11:55:24.204417
---

# 基于Flutter的安卓恶意软件，瞄准东亚市场

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

基于Flutter的安卓恶意软件，瞄准东亚市场

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

基于Flutter的安卓恶意软件，瞄准东亚市场

2023-06-30 11:29:07

所属地 上海

![](https://image.3001.net/images/20230630/1688093748_649e4434e7a6d845da359.png!small)

网络安全研究人员分享了一个名为Fluhorse的Android恶意软件的内部运作情况。

Fortinet FortiGuard实验室研究员Axelle Apvrille在上周发表的一份报告中说，这种恶意软件的出现代表了一种重大转变，因为它直接将恶意组件纳入Flutter代码中。

Check Point在2023年5月初首次记录了Fluhorse，详细说明了它通过伪装成ETC和VPBank Neo的流氓应用程序对位于东亚的用户进行攻击，尤其是在越南。

该恶意软件最初是通过网络钓鱼的方式来入侵，最终目标是窃取凭证、信用卡信息和以短信形式收到的双因素认证（2FA）信息，并将其发送到威胁者控制的远程服务器。

Fortinet对2023年6月11日上传到VirusTotal的Fluhorse样本进行了逆向工程，其最新发现表明，该恶意软件已经进化，通过将加密的有效载荷隐藏在一个打包器中，融入了更多的复杂性。

Apvrille解释说：解密是使用OpenSSL的EVP加密API在原生水平上进行的（以加强逆向工程）。加密算法是AES-128-CBC，其实现使用相同的硬编码字符串作为密钥和初始化向量（IV）。

解密后的有效载荷是一个ZIP文件，其中包含一个Dalvik可执行文件（.dex），然后将其安装在设备上，以监听传入的短信并将其外流到远程服务器上。

Apvrille说：静态逆转Flutter应用程序是反病毒研究人员的一个突破，但是不幸的是，预计未来会有更多的恶意Flutter应用程序发布。

> 参考链接：https://thehackernews.com/2023/06/fluhorse-flutter-based-android-malware.html

# 资讯

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