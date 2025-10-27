---
title: AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞
url: https://www.freebuf.com/news/415915.html
source: FreeBuf网络安全行业门户
date: 2024-11-23
fetch_date: 2025-10-06T19:18:20.162860
---

# AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞

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

AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞

2024-11-22 12:04:40

所属地 上海

谷歌透露，其基于人工智能的模糊工具OSS-Fuzz 已被用于帮助识别各种开源代码库中的26个漏洞，包括 OpenSSL 加密库中的一个中度漏洞。这一事件代表了自动化漏洞发现的一个里程碑：每个漏洞都是使用AI发现的，利用AI生成和增强的模糊测试目标。

提到的OpenSSL漏洞是CVE-2024-9143（CVSS评分：4.3），一个超出范围的内存写入缺陷，可能导致应用程序崩溃或远程代码执行。这个问题已经在OpenSSL的3.3.3、3.2.4、3.1.8、3.0.16、1.1.1zb和 1.0.2zl版本中得到了解决。

![](https://image.3001.net/images/20241122/1732248248_674002b80fec51b0bd2ee.png!small)

## **破题人类无法发现的漏洞**

谷歌在2023年8月增加了利用大型语言模型（LLM）来提高OSS- Fuzz中模糊覆盖率的能力，并表示该漏洞可能在代码库中存在了20年，而且在现有的由人类编写的模糊目标中是无法发现的。此外，他们还指出，使用AI生成模糊测试目标已经提高了272个C/C++项目的代码覆盖率，新增了超过370,000行新代码。

谷歌解释说，这样的漏洞之所以能够长时间未被发现，一个原因是线覆盖率并不能保证函数没有漏洞。代码覆盖率作为一项指标，无法衡量所有可能的代码路径和状态，不同的标志和配置可能会触发不同的行为，从而暴露出不同的漏洞。这些人工智能辅助的漏洞发现也是可能的，因为LLMs被证明擅长模仿开发人员的模糊工作流程，从而允许更多的自动化。正如谷歌之前就提到过，其基于LLM的框架Big Sleep帮助发现SQLite开源数据库引擎中的一个零日漏洞。

## **C++****代码安全性大幅提升**

与此同时，谷歌一直在努力将自己的代码库转换为内存安全语言，如Rust，同时还对现有的C++项目（包括Chrome）中的空间内存安全漏洞（当代码可能访问超出其预定范围的内存时）进行改造。其中包括迁移到安全缓冲区和启用强化的libc ++，后者将边界检查添加到标准的 C ++数据结构中，以消除大量的空间安全缺陷。它进一步指出，纳入这一变化所产生的间接费用很小（即平均0.30%的绩效影响）。

谷歌表示，由开源贡献者最近添加的“hardened libc++”引入了一系列安全检查，旨在捕获生产中的越界访问等漏洞。虽然C++不会完全成为内存安全的语言，但这些改进降低了风险，从而使得软件更加可靠和安全。

具体来说，hardened libc++通过为标准C++数据结构添加边界检查来消除一大类空间安全漏洞。例如，hardened libc++确保对std::vector的每个元素的访问都保持在其分配的边界内，防止尝试读取或写入超出有效内存区域的尝试。同样，hardened libc++在允许访问之前检查std::optional是否为空，防止访问未初始化的内存。这种改进对于提高C++代码的安全性和可靠性具有重要意义。

参考原文：

<https://thehackernews.com/2024/11/googles-ai-powered-oss-fuzz-tool-finds.html>

# 漏洞 # 漏洞挖掘

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

破题人类无法发现的漏洞

C++代码安全性大幅提升

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