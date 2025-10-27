---
title: 浏览器加密钱包高危漏洞可致资金遭窃
url: https://www.freebuf.com/articles/web/428512.html
source: FreeBuf网络安全行业门户
date: 2025-04-24
fetch_date: 2025-10-06T22:05:55.798953
---

# 浏览器加密钱包高危漏洞可致资金遭窃

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

浏览器加密钱包高危漏洞可致资金遭窃

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

浏览器加密钱包高危漏洞可致资金遭窃

2025-04-23 14:17:24

所属地 上海

![image](https://image.3001.net/images/20250423/1745420534289336_1f8582b6af584a1b8b65f969235dc6e2.webp!small)

研究人员发现主流浏览器加密货币钱包存在重大安全漏洞，攻击者无需用户任何交互或授权即可窃取资金。

在Stellar Freighter、Frontier Wallet和Coin98等钱包中发现的这些关键漏洞，标志着针对加密货币用户的攻击手段出现重大转变。与传统网络钓鱼攻击需要用户批准恶意交易不同，这些漏洞仅需用户访问恶意网站即可清空钱包资金。

"用户只需访问恶意网站，其助记词就会在后台被窃取，攻击者可随时转移资金。"发现漏洞的Coinspect研究人员解释称，"攻击者可能等到钱包余额充足时再行动，增加溯源难度。"

## 浏览器扩展钱包漏洞暴露私钥

这些漏洞源于浏览器钱包扩展组件间消息传递机制的架构缺陷。标准钱包架构中，去中心化应用(dApp)通过内容脚本(Content Script)注入的Provider API与钱包交互，内容脚本再与可访问私钥的后台脚本(Background Script)通信。

![](https://image.3001.net/images/20250423/1745420537086733_5554b5fd8de2452abf77c0e8612ae1c0!small)

在Stellar官方钱包Freighter(CVE-2023-40580)中，研究人员发现其使用单一处理器处理UI和Provider API的通信。这种设计导致消息来源混淆，攻击者可通过篡改内容脚本的request.type参数，触发本应仅供钱包UI使用的内部功能，从而获取用户助记词。

![](https://image.3001.net/images/20250423/1745420537920740_45c05165482b485f8cb8332b883118c9!small)

Frontier Wallet存在类似漏洞，其Provider API暴露了可返回钱包状态（含加密助记词）的内部方法。尽管使用独立端口连接，攻击者仍能在钱包锁定时获取这些信息。

![](https://image.3001.net/images/20250423/1745420538162928_e7f910a73306406ab9ae39b1dfc1ed41!small)

Coin98 Wallet的漏洞则允许攻击者向内容脚本发送带有isDev:true参数的伪造消息，使后台脚本误认为指令来自合法钱包UI而非恶意网站。

## 严重安全影响

这些漏洞从多个维度突破了传统安全模型：

* **预连接风险**：恶意网站在用户接受连接前即可与钱包交互
* **静默攻击**：整个攻击过程不会触发用户警报
* **直接密钥访问**：即使钱包锁定仍可获取助记词
* **延迟利用**：攻击者可待钱包资金充足后再行动

过去一年，网络犯罪分子已利用类似"钱包清空"技术从63,000余名受害者处窃取约5,898万美元。

## 修复建议

受影响钱包已发布修复版本，用户应立即：

* 将Stellar Freighter升级至5.3.1或更高版本
* 确保Frontier Wallet更新至2024年11月22日后发布的版本
* 仅使用已更新的Coin98 Wallet版本

若怀疑钱包已遭入侵，安全专家建议立即将剩余代币转移至新创建的钱包，并停用可能泄露的钱包。随着加密货币普及，安全研究人员警告其他浏览器钱包（特别是基于未经验证代码库开发的产品）可能存在类似漏洞。鉴于此类隐蔽攻击手段日益盛行，用户应保持警惕，优先选择具备成熟安全实践的钱包产品。

**参考来源：**

> [Critical Vulnerabilities in Browser Wallets Let Attackers Drain your Funds](https://cybersecuritynews.com/critical-browser-wallet-vulnerabilities/)

# web安全 # 区块链安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

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

浏览器扩展钱包漏洞暴露私钥

严重安全影响

修复建议

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