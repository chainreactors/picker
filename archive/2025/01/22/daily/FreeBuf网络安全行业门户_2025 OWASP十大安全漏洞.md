---
title: 2025 OWASP十大安全漏洞
url: https://www.freebuf.com/news/420401.html
source: FreeBuf网络安全行业门户
date: 2025-01-22
fetch_date: 2025-10-06T20:09:27.675964
---

# 2025 OWASP十大安全漏洞

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

2025 OWASP 十大安全漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

2025 OWASP 十大安全漏洞

2025-01-21 11:30:01

所属地 上海

![](https://image.3001.net/images/20250121/1737440528_678f3d1025ec7982598b6.jpg!small)随着去中心化金融（DeFi）和区块链技术的不断发展，智能合约安全的重要性愈发凸显。在此背景下，开放网络应用安全项目（OWASP）发布了备受期待的《2025年智能合约十大漏洞》报告。

这份最新报告反映了不断演变的攻击向量，深入剖析了近年来的常见漏洞及缓解策略。旨在提升Web3开发者和安全团队的安全意识，为开发者、审计人员和安全专业人士提供宝贵的资源，以应对智能合约中最关键的安全漏洞。它还与其他OWASP项目，如《智能合约安全验证标准》（SCSVS）、《智能合约安全测试指南》（SCSTG）相互补充，为区块链生态系统的安全提供了全面的方法。

![](https://image.3001.net/images/20250121/1737440607_678f3d5fbc12ac47b29fe.jpg!small)

## 2023年至2025年的主要变化

2025年版榜单根据真实事件和新兴趋势更新了排名，并提供了新的见解。显著的变化包括新增了“价格预言机操纵”和“闪电贷攻击”两个独立类别，反映了这些漏洞在DeFi攻击中的日益普遍。

与此同时，早期版本中较为突出的“时间戳依赖”、“Gas 限制问题”等漏洞已被替换或整合到更广泛的类别中，如“逻辑错误”。

## 2025年OWASP十大漏洞详解

### SC01：访问控制漏洞

访问控制漏洞仍然是智能合约中导致财务损失的主要原因，仅2024年就造成了9.532亿美元的损失。这些漏洞通常是由于权限检查未正确实施而产生的，以致未经授权的用户可以访问或修改关键功能或数据。一个典型案例是88mph的“函数初始化漏洞”，攻击者利用该漏洞重新初始化合约并获得管理员权限。

### SC02：价格预言机操纵

操纵价格预言机（智能合约使用的外部数据源）可能会破坏协议的稳定性，导致财务损失或系统性故障。攻击者通常利用设计不良的预言机机制暂时抬高或压低资产价格。

### SC03：逻辑错误

业务逻辑漏洞通常发生在合约未能正确执行其预期功能时。这些错误可能导致代币铸造错误、借贷协议缺陷或奖励分配错误。

### SC04：输入验证缺失

未能验证用户输入可能使攻击者能够向智能合约注入恶意数据，导致意外行为或破坏合约逻辑。

### SC05：重入攻击

重入攻击利用合约在完成自身状态更新之前调用外部函数的能力。这一经典漏洞在 2016 年的 DAO 攻击中被利用，导致价值 7000 万美元的以太坊被盗。

### SC06：未检查的外部调用

当智能合约未能验证外部调用的成功时，可能会基于错误的交易结果假设继续执行，从而导致不一致或被恶意行为者利用。

### SC07：闪电贷攻击

闪电贷允许用户在一个交易中无抵押借款，但可能被利用来操纵市场或耗尽流动性池。

### SC08：整数溢出和下溢

当计算超出数据类型限制时，可能会发生算术错误，使攻击者能够操纵余额或绕过限制。

### SC09：不安全的随机性

区块链的确定性特性使得生成安全的随机性具有挑战性。可预测的随机性可能会破坏依赖随机结果的功能，如抽奖或代币分配。

### SC10：拒绝服务（DoS）攻击

DoS攻击针对智能合约中资源密集型功能，通过耗尽Gas限制或计算资源使其无法响应。

## 对现实世界的影响

OWASP 智能合约Top 10的编制基于《加密货币损失报告》等资源中记录的真实事件。仅2024年，就有149起事件被记录在案，造成了超过14.2亿美元的损失，其中访问控制漏洞（9.53亿美元）、逻辑错误（6300万美元）和重入攻击（3500万美元）是主要原因。这些数据凸显了在区块链开发中加强安全实践的紧迫性。

随着区块链技术的成熟，攻击者利用其漏洞的方法也在不断演变，这也强调了Web3项目增强自身抵御潜在漏洞能力的重要性。

参考链接：

> <https://cybersecuritynews.com/owasp-top-10-2025-smart-contract/>

# 资讯 # web安全

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

2023年至2025年的主要变化

2025年OWASP十大漏洞详解

* SC01：访问控制漏洞
* SC02：价格预言机操纵
* SC03：逻辑错误
* SC04：输入验证缺失
* SC05：重入攻击
* SC06：未检查的外部调用
* SC07：闪电贷攻击
* SC08：整数溢出和下溢
* SC09：不安全的随机性
* SC10：拒绝服务（DoS）攻击

对现实世界的影响

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