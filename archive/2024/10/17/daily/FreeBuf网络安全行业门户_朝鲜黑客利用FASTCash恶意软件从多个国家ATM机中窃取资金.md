---
title: 朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金
url: https://www.freebuf.com/news/412963.html
source: FreeBuf网络安全行业门户
date: 2024-10-17
fetch_date: 2025-10-06T18:52:08.622995
---

# 朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金

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

朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

朝鲜黑客利用FASTCash恶意软件从多个国家ATM机中窃取资金

2024-10-16 17:07:57

所属地 上海

据The Hacker News消息，与朝鲜相关的恶意软件 FASTCash正利用针对Linux的新变体实施攻击，目的是窃取资金。

![](https://image.3001.net/images/20241016/1729070182_670f846665956c6418751.png!small)

研究人员表示，这种恶意软件安装在被入侵网络中处理银行卡交易的支付交换机上，以实施未授权的自动取款机提现交易。

美国相关机构于2018 年 10 月首次记录了 FASTCash，称至少自 2016 年底以来，有朝鲜背景的黑客组织Hidden Cobra就利用该恶意软件将非洲和亚洲地区的银行ATM作为攻击目标。在2017年的一起攻击事件中，该组织成功对位于 30 多个不同国家/地区的 ATM 机成功实施了攻击；2018年，同样的攻击又在 23 个不同国家的 ATM 机中上演。

虽然之前的 FASTCash仅适用于微软Windows系统和和 IBM AIX，但最新调查结果显示，新版本的恶意软件已经能够适用于Linux 系统，相关样本于 2023 年 6 月中旬首次提交到了 VirusTotal 平台。

该恶意软件为Ubuntu Linux 20.04 编译的共享对象（“libMyFc.so”）形式，攻击手法为篡改预定义的持卡人账号因资金不足而被拒绝的交易信息，并允许他们提取随机金额的土耳其里拉，每笔金额从 12000 到 30000 里拉（350 美元到 875 美元）不等 。

![](https://image.3001.net/images/20241016/1729069706_670f828a646f4c0310e92.png!small)攻击示意图

Linux 变体的发现进一步强调了对足够强大的检测能力的需求，而 Linux 服务器环境中通常缺乏这些功能，建议对借记卡实施芯片和 PIN 要求、要求并验证发卡机构金融请求响应信息中的信息验证码，并对芯片和 PIN 交易执行授权响应加密验证。

**参考来源：**

> [New Linux Variant of FASTCash Malware Targets Payment Switches in ATM Heists](https://thehackernews.com/2024/10/new-linux-variant-of-fastcash-malware.html)

# 恶意软件

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