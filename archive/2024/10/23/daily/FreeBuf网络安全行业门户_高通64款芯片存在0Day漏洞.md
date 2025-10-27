---
title: 高通64款芯片存在0Day漏洞
url: https://www.freebuf.com/news/413449.html
source: FreeBuf网络安全行业门户
date: 2024-10-23
fetch_date: 2025-10-06T18:50:57.574777
---

# 高通64款芯片存在0Day漏洞

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

高通64款芯片存在0Day漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

高通64款芯片存在0Day漏洞

2024-10-22 16:14:56

所属地 上海

近日，高通公司发布了一项重要的安全警告，揭示了其多达64款芯片组存在严重的“**0Day漏洞**”。这一漏洞被标识为CVE-2024-43047，影响广泛，波及多个搭载骁龙芯片的Android智能手机和平板电脑、物联网设备等多个领域。

![](https://image.3001.net/images/20241022/1729585089_67175fc15fbf0ce2cc2ac.png!small)

所谓“**0Day漏洞**”，是指那些尚未被软件厂商或操作系统供应商知晓的安全漏洞。攻击者可以利用这些漏洞，在未被检测的情况下对系统进行攻击，窃取数据或执行恶意代码。

根据高通的公告，CVE-2024-43047源于数字信号处理器(DSP)服务中的使用后释放(use-after-free)错误，可能导致内存损坏。该漏洞的CVSS评分为7.8，表明其严重性较高。

值得注意的是，这一漏洞已经被有限且有针对性地利用，攻击者可以通过运行恶意代码来控制设备。美国网络安全机构 CISA 已将高通的漏洞列入其已知或已被利用的漏洞列表。

此次漏洞的发现和披露由谷歌安全分析小组及国际特赦组织安全实验室共同完成，并且已有恶意攻击者开始利用这一漏洞。这使得受影响的用户面临潜在的隐私泄露、设备控制以及恶意软件安装等风险。

**这一漏洞的存在，可能导致以下严重后果：**数据泄露：攻击者可通过漏洞获取用户敏感信息，如通讯录、照片、银行账户等，造成隐私泄露；系统瘫痪：恶意攻击可能导致设备系统崩溃，影响用户正常使用；远程控制：攻击者甚至有可能通过漏洞实现对设备的远程控制，进而实施更为复杂的犯罪行为。

高通公司已经发布了针对该漏洞的安全补丁，建议所有用户尽快更新其设备固件以避免潜在的安全威胁。然而，由于一些用户尚未及时更新手机，因此仍需保持警惕。

据悉，该漏洞影响到高通生产的 64 款芯片组型号如下：FastConnect 6700、FastConnect 6800、FastConnect 6900、FastConnect 7800、QAM8295P、 QCA6174A、 QCA6391、 QCA6426、QCA6436、QCA6574AU、QCA6584AU、QCA6595、 QCA6595AU、QCA6688AQ、QCA6696、QCA6698AQ、QCS410、QCS610、QCS6490、高通®视频协作 VC1 平台、高通®视频协作 VC3 平台、SA4150P、SA4155P、SA6145P、SA6150P、 SA6155P、SA8145P、SA8150P、SA8155P、SA8195P、SA8295P、SD660、SD865 5G、SG4150P、Snapdragon 660 移动平台、Snapdragon 680 4G 移动平台、骁龙 685 4G 移动平台 (SM6225-AD)、骁龙 8 Gen 1 移动平台、骁龙 865 5G 移动平台、骁龙 865+ 5G 移动平台(SM8250-AB)、骁龙 870 5G 移动平台(SM8250-AC)、骁龙 888 5G 移动平台、骁龙 888+ 5G 移动平台 (SM8350-AC)、骁龙 Auto 5G 调制解调器-RF、骁龙 Auto 5G 调制解调器-RF Gen 2、骁龙 X55 5G 调制解调器-RF系统、骁龙 XR2 5G 平台、SW5100、SW5100P、SXR2130、WCD9335、WCD9341、WCD9370、WCD9375、WCD9380、WCD9385、WCN3950、WCN3980、WCN3988、WCN3990、WSA8810、WSA8815、WSA8830、WSA8835。这些芯片或将用于三星Galaxy S22 Ultra、一加OnePlus 10 Pro、Sony Xperia 1 IV、OPPO Find X5 Pro、荣耀 Magic4 Pro、Xiaomi 12等，名单中还包括用于蓝牙和 Wi-Fi 连接的 Snapdragon 调制解调器和 FastConnect 模块。

此次受影响的高通芯片型号众多，覆盖了从入门级到高端市场的多个系列。设备制造商需密切关注高通公司的最新动态，及时跟进并应用相关补丁，确保产品安全。用户应保持警惕，定期检查设备系统更新情况，并遵循厂商建议进行安全设置。

# 系统安全 # 数据安全

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