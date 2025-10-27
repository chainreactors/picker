---
title: 高通骁龙通告22个安全漏洞，联想、微软和三星设备受影响
url: https://www.freebuf.com/news/354778.html
source: FreeBuf网络安全行业门户
date: 2023-01-11
fetch_date: 2025-10-04T03:32:15.145497
---

# 高通骁龙通告22个安全漏洞，联想、微软和三星设备受影响

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

高通骁龙通告22个安全漏洞，联想、微软和三星设备受影响

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

高通骁龙通告22个安全漏洞，联想、微软和三星设备受影响

2023-01-10 12:20:52

所属地 上海

高通公司 2023 年 1 月的安全公告解决了其骁龙套件中的 22 个软件漏洞。固件保护公司Binarly的efiXplorer团队，OPPO琥珀安全实验室的Zinuo Han，IceSword Lab的Gengjia Chen，研究人员nicolas（nicolas1993），STEALIEN的Seonung Jang和百度安全的Le Wu报告了一些漏洞。

以下是公司解决的最严重漏洞报告：

![](https://image.3001.net/images/20230110/1673321942_63bcddd633c3795c250bb.jpg!small)

最严重的缺陷是跟踪为 CVE-2022-33219 的汽车缓冲区溢出的整数溢出（CVSS 得分 9.3）。“汽车中的内存损坏是由于整数溢出到缓冲区溢出，同时向共享缓冲区注册新侦听器。

高通公司修复的另外两个严重问题是：

* CVE-2022-33218（CVSS 得分 8.2） – 该漏洞是由于输入验证不当而导致的汽车内存损坏。
* CVE-2022-33265（CVSS 得分 7.3）– 该漏洞是电力线通信固件中的信息暴露。

这些漏洞影响了使用联想，微软和三星制造的Snapdragon芯片组的笔记本电脑和其他设备。

## 联想发布安全更新

1月3日，Lenovo（联想）发布安全更新，修复了ThinkPad X13s BIOS中的多个安全漏洞，本地用户可利用这些漏洞导致内存损坏或敏感信息泄露。

本次ThinkPad X13s BIOS更新中共修复了如下漏洞：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CVE-ID | 类型 | 评分 | 受影响产品/组件 | 描述 |
| CVE-2022-40516 | 基于堆栈的缓冲区溢出导致内存损坏 | 8.4 | Qualcomm BIOS | 本地用户可利用这些漏洞导致内存损坏、拒绝服务或任意代码执行。 |
| CVE-2022-40517 |
| CVE-2022-40520 |
| CVE-2022-40518 | 缓冲区过度读取 | 6.8 | Qualcomm BIOS | 本地用户可利用这些漏洞导致信息泄露。 |
| CVE-2022-40519 |
| CVE-2022-4432、CVE-2022-4433、CVE-2022-4434、CVE-2022-4435 | 缓冲区过度读取 | None | ThinkPad X13s BIOS | 本地用户可利用这些漏洞导致信息泄露。 |

**影响范围**

ThinkPad X13s BIOS 版本<1.47 (N3HET75W)

目前这些漏洞已经修复，Lenovo ThinkPad X13s用户可将BIOS更新到1.47 (N3HET75W)版本。

> 参考来源：https://securityaffairs.com/140528/security/qualcomm-snapdragon-flaws.html

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

文章目录

联想发布安全更新

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