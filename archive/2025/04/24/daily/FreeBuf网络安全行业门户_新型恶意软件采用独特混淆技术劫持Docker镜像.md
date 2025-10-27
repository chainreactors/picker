---
title: 新型恶意软件采用独特混淆技术劫持Docker镜像
url: https://www.freebuf.com/articles/428513.html
source: FreeBuf网络安全行业门户
date: 2025-04-24
fetch_date: 2025-10-06T22:05:56.242472
---

# 新型恶意软件采用独特混淆技术劫持Docker镜像

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

新型恶意软件采用独特混淆技术劫持Docker镜像

* ![]()
* 关注

* [技术](https://www.freebuf.com/articles)

新型恶意软件采用独特混淆技术劫持Docker镜像

2025-04-23 11:36:35

所属地 上海

![image](https://image.3001.net/images/20250423/1745420545869132_c4c8f9c81fe248318654f82e1b8d8adf.webp!small)

安全研究人员发现新型恶意软件正在攻击Docker环境，该软件采用复杂的多层混淆技术逃避检测，通过劫持计算资源进行加密货币挖矿（cryptojacking）。

Darktrace与Cado Security Labs的安全专家分析指出，该攻击活动既展现了攻击者的技术独创性，也暴露出容器化基础设施面临的日益增长的安全风险。

## **Docker成为恶意软件主要攻击目标**

作为主流容器化平台，Docker因其广泛普及和从公共仓库便捷部署的特性，正成为网络犯罪分子的重点攻击目标。

攻击者通常利用配置错误或暴露的Docker服务来启动恶意容器，这些容器多使用托管在Docker Hub上的镜像。本次攻击活动始于从Docker Hub拉取`kazutod/tene:ten`镜像的请求。

该容器设计用于执行嵌入在镜像层中的Python脚本`ten.py`。安全分析师使用Docker内置工具提取并分析镜像后，发现其采用了复杂的混淆方案：

* `ten.py`脚本定义了一个lambda函数，该函数会反转经过base64编码的字符串，解码后使用zlib解压缩，最终执行生成的代码
* 该过程循环重复：解码后的有效载荷会再次调用相同的解码函数，每次传递新的混淆字符串
* 分析师发现需要经过63次解码循环才能最终暴露实际恶意代码

这种深度分层混淆技术实属罕见。虽然单层混淆通常足以绕过基于特征的检测，但攻击者使用数十层混淆的目的显然是为了干扰人工分析和自动化工具。尽管如此，研究人员仍能在数分钟内自动化完成反混淆过程并提取最终有效载荷。

## **加密货币挖矿的新手段**

与传统直接部署XMRig等工具进行加密货币挖矿的恶意软件不同，该攻击活动采用了创新手法。反混淆后的代码会连接至`teneo.pro`——这是一家运营去中心化社交媒体数据网络的合法Web3初创企业。

通过运行节点并持续发送"保活"心跳包，恶意软件可获取"Teneo Points"（该网络根据节点在线时长和活跃度发放的私有加密代币）。值得注意的是，该恶意软件并未像合法节点软件那样执行实际数据抓取，而是单纯模拟活动以最大化代币奖励。

这种攻击方式使攻击者能够获利，同时避免了传统挖矿操作常见的高资源占用和网络异常。报告指出，这反映出攻击者正从易被检测的知名挖矿工具，转向滥用合法的去中心化平台和奖励系统的趋势。由于这类私有代币的封闭性，攻击者的实际收益难以追踪和量化。

## **安全防护建议**

安全专家强调Docker环境仍是极具吸引力的攻击目标，并建议企业采取以下防护措施：

* 非必要情况下避免将Docker服务暴露在互联网
* 采用强认证机制和防火墙限制访问权限
* 定期审计和监控容器活动是否存在异常
* 仅从可信来源拉取镜像并进行恶意软件扫描

随着攻击手段不断翻新，防御者必须保持警惕，及时调整安全策略以保护容器化基础设施免受日益复杂的威胁。

**参考来源：**

> [New Malware Hijacking Docker Images with Unique Obfuscation Technique](https://cybersecuritynews.com/new-malware-hijacking-docker-images/)

# 网络安全 # 容器安全

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