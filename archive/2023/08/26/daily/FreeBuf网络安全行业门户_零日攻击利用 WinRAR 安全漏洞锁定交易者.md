---
title: 零日攻击利用 WinRAR 安全漏洞锁定交易者
url: https://www.freebuf.com/news/376183.html
source: FreeBuf网络安全行业门户
date: 2023-08-26
fetch_date: 2025-10-04T12:00:34.583384
---

# 零日攻击利用 WinRAR 安全漏洞锁定交易者

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

零日攻击利用 WinRAR 安全漏洞锁定交易者

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

零日攻击利用 WinRAR 安全漏洞锁定交易者

2023-08-25 11:19:56

所属地 上海

![](https://image.3001.net/images/20230825/1692931968_64e81780aec1ffdb44e00.png!small)

Group-IB 的最新发现显示，自 2023 年 4 月以来， WinRAR 压缩软件曝出一个关键的安全漏洞，被认为是一个已经被利用的零日漏洞。

该漏洞被标记为 CVE-2023-38831，允许威胁者仿用文件扩展名，从而在伪装成看似无害的图像或文本文件的压缩包中启动恶意脚本。2023 年 8 月 2 日发布的 6.23 版本修补了这一漏洞，同时修复的还有 CVE-2023-40477。

在新加坡公司于 2023 年 7 月发现的攻击中，通过 Forex Station 等交易相关论坛分发的特制 ZIP 或 RAR 压缩文件被用于传播 DarkMe、GuLoader 和 Remcos RAT 等多种恶意软件。

Group-IB 恶意软件分析师安德烈-波罗文金（Andrey Polovinkin）说：在感染设备后，网络犯罪分子会从经纪人账户中提取资金。目前尚不清楚受害者总人数和由此造成的经济损失。

诱杀压缩文件的创建方式是包含一个图像文件和一个同名文件夹。

![](https://image.3001.net/images/20230825/1692932000_64e817a024db925ec1864.png!small)

因此，当受害者点击图片时，文件夹中的批处理脚本就会被执行，然后用于启动下一阶段，即用于提取和启动其他文件的 SFX CAB 存档。与此同时，脚本还会加载诱饵图片，以免引起怀疑。

波罗文金告诉《黑客新闻》：CVE-2023-38831 是由于在打开 ZIP 压缩包中的文件时出现处理错误造成的。武器化的 ZIP 压缩包已在至少 8 个流行的交易论坛上传播，因此受害者的地理位置非常广泛，攻击并不针对特定的国家或行业。

目前还不知道谁是利用 WinRAR 漏洞进行攻击的幕后黑手。尽管如此，DarkMe 是一种 Visual Basic 木马，归属于 EvilNum 组织，NSFOCUS 于 2022 年 9 月首次记录到它与一个代号为 DarkCasino 的针对欧洲在线赌博和交易服务的网络钓鱼活动有关。

同样使用这种手段传播的还有一种名为 GuLoader（又名 CloudEye）的恶意软件，它随后会尝试从远程服务器获取 Remcos RAT。

Polovinkin 说：最近利用 CVE-2023-38831 的案例提醒我们，与软件漏洞相关的风险始终存在。攻击者手段资源丰富，他们总能找到新的方法来发现并利用漏洞。

> 参考链接：https://thehackernews.com/2023/08/winrar-security-flaw-exploited-in-zero.html

# 资讯 # 漏洞 # 黑客 # 安全资讯 # 网络攻击

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