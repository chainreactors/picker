---
title: 溯源专题 | 通过PE中PDB路径信息进行溯源
url: https://www.freebuf.com/articles/network/351557.html
source: FreeBuf网络安全行业门户
date: 2022-12-13
fetch_date: 2025-10-04T01:18:58.647857
---

# 溯源专题 | 通过PE中PDB路径信息进行溯源

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

溯源专题 | 通过PE中PDB路径信息进行溯源

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

溯源专题 | 通过PE中PDB路径信息进行溯源

2022-12-12 10:57:51

所属地 广东省

欢迎关注同名微信公众号！[狼蛛安全实验室](https://mp.weixin.qq.com/s/ccMQEhCoSwOaUV1RMFpFvg)！

## **引言**

PDB（Program Database），即程序数据库文件。面向Windows平台的大多数编译器可以生成PDB文件，这些编译器将有关可执行文件（Portable Executable File，PE文件）的调试信息存储在独立的PDB文件中，这样既缩小了可执行文件的体积又缩短其加载数据所需的时间。

![1670206059_638d526bceec26ce5e547.jpg!small](https://image.3001.net/images/20221205/1670206059_638d526bceec26ce5e547.jpg!small)

由源代码到生成可执行文件需要进行多次处理（源代码 -> 预处理 -> 编译 -> 汇编（生成目标文件） -> 链接 ->可执行二进制文件），可执行文件的代码部分已经都是由机器语言指令组成。

![1670206065_638d5271c0ab96dd7d7e6.jpg!small](https://image.3001.net/images/20221205/1670206065_638d5271c0ab96dd7d7e6.jpg!small)

而程序员想进行源码级别的调试，就需要调试器通过PDB获取调试所需要的基本信息，包括源文件名、变量名、函数名、类型数据、对应的行号等等；这样程序员便可以将程序的当前执行状态与源代码关联起来。

由于PDB文件和可执行文件是相互独立的，为了方便调试器加载PDB文件，编译器在生成可执行文件时会默认将PDB文件的路径信息存储在可执行文件中；而该PDB路径信息便是本文溯源的重点。

## **溯源思路**

使用PE工具（IDA也可以）查看可执行文件的调试段便可以看到存储PDB的绝对路径：

![1670206027_638d524b5fd0181b12423.jpg!small](https://image.3001.net/images/20221205/1670206027_638d524b5fd0181b12423.jpg!small)

使用十六进制编辑器直接搜索“pdb”关键字也可以得到PDB路径：

![1670206020_638d524498574402f86ca.jpg!small](https://image.3001.net/images/20221205/1670206020_638d524498574402f86ca.jpg!small)

文件路径具有强烈的独特性，每个人对于文件的存放目录可以说是迥然不同，而对于工程项目文件的存放也是如此。

假如，狼小蛛在一次应急响应中捕获到一个样本PhaseOne.exe，而它的PDB路径为E:\CodeOfKindness\Foobar\PhaseOne\Release\PhaseOne.pdb。

![1670206002_638d5232434a8f8aca06d.jpg!small](https://image.3001.net/images/20221205/1670206002_638d5232434a8f8aca06d.jpg!small)

半年后，狼小蛛又捕获到一个恶意样本PhaseTwo.exe，发现该样本PDB路径居然是E:\CodeOfKindness\Foobar\_new\PhaseTwo\Release\PhaseTwo.pdb。

![1670205995_638d522bd2d15930b158b.jpg!small](https://image.3001.net/images/20221205/1670205995_638d522bd2d15930b158b.jpg!small)

通过逆向分析发现PhaseTwo.exe和半年前的PhaseOne.exe在代码上高度相似，且两者使用了同一个Foobar框架。

![1670205989_638d5225c8749b5a94858.jpg!small](https://image.3001.net/images/20221205/1670205989_638d5225c8749b5a94858.jpg!small)

结合路径特点（X:\CodeOfKindnees\Foobar\_X\XXX\Release\XXX.pdb）和样本使用的框架以及代码特点，由此，狼小蛛高度自信地认为这两个样本出自同一组织之手，并为其命名为CodeOfKindness\_FB。

## **防溯源-隐去PDB路径**

这里以微软的VS举例：

![1670205966_638d520ed5685195f51bb.jpg!small](https://image.3001.net/images/20221205/1670205966_638d520ed5685195f51bb.jpg!small)

依次点击

项目 -> 项目具体属性 -> 配置属性 -> 链接器 -> 调试

然后把"生成调试信息"设置为"否"，这样在生成可执行文件中就没有PDB路径。注意：缺少PDB文件会导致本地调试器失效，因此在我们只需要为Release版生成的可执行文件设置。

![1670205977_638d521957e3964c19d5d.jpg!small](https://image.3001.net/images/20221205/1670205977_638d521957e3964c19d5d.jpg!small)

# 技术分享 # 攻击溯源

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

引言

溯源思路

防溯源-隐去PDB路径

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