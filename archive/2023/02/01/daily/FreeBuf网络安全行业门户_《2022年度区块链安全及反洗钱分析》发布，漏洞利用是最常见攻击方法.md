---
title: 《2022年度区块链安全及反洗钱分析》发布，漏洞利用是最常见攻击方法
url: https://www.freebuf.com/articles/paper/356136.html
source: FreeBuf网络安全行业门户
date: 2023-02-01
fetch_date: 2025-10-04T05:20:55.404641
---

# 《2022年度区块链安全及反洗钱分析》发布，漏洞利用是最常见攻击方法

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

《2022年度区块链安全及反洗钱分析》发布，漏洞利用是最常见攻击方法

* ![]()
* 关注

* [咨询](https://www.freebuf.com/consult)

《2022年度区块链安全及反洗钱分析》发布，漏洞利用是最常见攻击方法

2023-01-31 17:20:48

所属地 上海

2022年是勒索组织异常猖獗的一年。这一年，全球网络空间处于严峻的勒索攻击威胁之中，不仅仅是企业，政府部门、公益组织、关键信息基础设施、甚至是整个国家和地区，都成为了勒索组织攻击的目标。

通过对高价值数据进行加密、窃取，勒索组织有了向用户勒索的筹码。区块链技术不可逆、匿名性特征在有效保护隐私的同时，也为网络犯罪提供了“保护伞”。很多不法分子打着区块链旗号发行所谓的虚拟资产，实施诈骗，黑灰产的先进与专业度已经远超想象。

近日，慢雾科技发布了《2022年度区块链安全及反洗钱分析》，聚焦于 2022 年区块链行业所发生的重大事件，主要介绍区块链行业各赛道的安全状况，延伸并提炼出常见攻击手法，并披露其中几种钓鱼手法。接着对部分安全事件的被盗资金流向进行分析，并通过归纳总结，公布一种针对混币器资金追踪的高级分析方法。

## ****一、区块链安全现状****

根据慢雾区块链被黑事件档案库统计，2022 年安全事件共 303件，损失高达37.77 亿美元。相比 2021 年的 97.95 亿美元下降约 61%。其中 DeFi、跨链桥、NFT 等安全事件 255 起，交易所安全事件 10 起，公链安全事件 11 起钱包安全事件 6 起，其他类型安全事件 21 起。

303 起安全事件中，攻击手法主要分为三类：由项目自身设计缺陷和各种合约漏洞引起的攻击；包含 Rug Pull、钓鱼、Scam 类型的手法；由私钥泄露引起的资产损失。

2022 年最常见的攻击手法是由项目自身设计缺陷和各种合约漏洞引起，约 92 起，造成损失近 11亿美元。其中较为主要的是利用闪电贷引起的攻击，约 33 起，造成损失 3.48 亿美元，其他包括重入问题、价格操纵、验证问题等等。

因私钥被盗引起的资产损失发生率约为 6.6%，损失金额却达到 7.62 亿美元。因私钥被盗的事件中，损失最大的来自 Ronin 事件，其次是 Harmony，都是来自跨链桥。

总的来说，2022 年其他较为新型的手法为前端恶意攻击、DNS 攻击以及 BGP 劫持；最为奇葩的则是人为配置操作失误导致的资产损失。

在网络钓鱼攻击方面，慢雾科技公布了常见的钓鱼攻击手法，包括浏览器恶意书签盗取 Discord Token、“零元购” NFT 钓鱼、Redline Stealer 木马盗币、空白支票 eth\_sign 钓鱼等，并对钓鱼事件进行分析和总结。

## ****二、区块链反洗钱****

众所周知，造成区块链安全事件的黑客、黑色产业链、欺诈者和 Rug Pull 项目方一直是洗钱的主力，其中最臭名昭著的莫过于朝鲜 LAZARUS GROUP 黑客组织，给区块链生态安全带来巨大的威胁。

在黑客、黑色产业链、欺诈者和 Rug Pull 项目方洗钱过程中，自然少不了一些洗钱工具的帮忙，常见的洗钱工具有 ETH/BSC 链上的 Tornado.Cash，BTC 链上的 Coinjoin 工具（ChipMixer 等）、混币器（Blender、CryptoMixer 等）、隐私钱包（Wasabi、Samourai 等）、换币平台（ChangeNOW、SimpleSwap、FixedFloat 等）和一些交易平台。

通过对部分安全事件被盗资金的 ETH 和 BTC 流向进行分析，得到 ETH/BTC 资金流向图，能够初步评估出洗钱资金的态势。

根据部分安全事件 ETH 资金流向图，74.6% 洗钱资金流向 Tornado.Cash，资金量高达 300160ETH；23.7% 洗钱资金保留在黑客地址，暂未进一步转移，资金量为 95570 ETH；1.5% 洗钱资金流向交易平台，资金量为 6250 ETH。

根据部分安全事件 BTC 资金流向图，48.9% 洗钱资金流向 ChipMixer，资金量高达 3460 BTC；36.5% 洗钱资金保留在黑客地址，暂未进一步转移，资金量为 2,586 BTC；6.2% 洗钱资金流向Blender，3.8% 洗钱资金流向 CryptoMixer，2.1% 洗钱资金流向未知主体，1.3% 洗钱资金流向renBTC，0.7% 洗钱资金流向 Wasabi Coinjoin，0.1% 洗钱资金流向 Binance 交易平台。

## ****三、遵守下列原则，规避大部分区块链风险****

在 Web3 世界，用户的安全意识往往是参差不齐，这也导致了针对用户的钓鱼攻击花样多多且频繁发生。对于个人用户来说，遵守以下安全法则及原则，可以避免大部分风险：

### 1、两大安全法则

> 零信任：简单来说就是保持怀疑，而且是始终保持怀疑。
>
> 持续验证：你要相信，你就必须有能力去验证你怀疑的点，并把这种能力养成习惯。

### 2、安全原则

> 网络上的知识，凡事都参考至少两个来源的信息，彼此佐证，始终保持怀疑。
>
> 做好隔离，也就是鸡蛋不要放在一个篮子里。
>
> 对于存有重要资产的钱包，不做轻易更新，够用就好。
>
> 所见即所签。即你看到的内容就是你预期要签名的内容，当你签名发出去后，结果就应该是你预期的，绝不是事后拍断大腿的。
>
> 重视系统安全更新，有安全更新就立即行动。
>
> 不乱下程序。

![](https://image.3001.net/images/20230131/1675156763_63d8dd1b32229d81b8c7c.jpg!small)**扫码下载《2022年度区块链安全及反洗钱分析》**

![](https://image.3001.net/images/20230131/1675156825_63d8dd594a8f645f1b0d8.png!small)**扫描二维码 即刻下载知识大陆APP**

# 区块链安全 # 反洗钱

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

一、区块链安全现状

二、区块链反洗钱

三、遵守下列原则，规避大部分区块链风险

* 1、两大安全法则
* 2、安全原则

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