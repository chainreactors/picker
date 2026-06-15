---
title: Wazuh CVSS 10 分漏洞细节与PoC公开
url: https://www.freebuf.com/articles/system/486038.html
source: FreeBuf网络安全行业门户
date: 2026-06-14
fetch_date: 2026-06-15T07:09:30.650120
---

# Wazuh CVSS 10 分漏洞细节与PoC公开

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
* [培训站](https://live.freebuf.com)
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

![](https://image.3001.net/images/20260209/1770606290323007_4a7b566114624e94b90bd2fe14b98aab.png) ![](https://image.3001.net/images/20260401/1775023076_69ccb3e4192f3c60ed43b.png)

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Wazuh CVSS 10 分漏洞细节与PoC公开

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

Wazuh CVSS 10 分漏洞细节与PoC公开

2026-06-15 01:48:13

所属地 上海

![image](https://image.3001.net/images/20260615/1781489033895127_89690c5f1c5d46a0ac75665992f11942.jpeg!small)

开源防御安全社区近日曝出一个重大安全漏洞。完整技术细节及可实际利用的概念验证代码已在网上公开。这个Wazuh CVSS 10分高危漏洞允许经过认证的端点直接操控中央日志存储系统。因此，任何正在测试该下一代平台的企业都必须立即采取修复措施，否则将面临基础设施遭篡改的严重后果。

## 注入漏洞的技术原理

该高危威胁的根源在于平台的资产遥测管道深处。技术披露文件明确指出："Wazuh 5.0库存管道将Agent提供的flatbuffer字段（DataValue.index）直接转发至OpenSearch\_bulk NDJSON请求体，未进行转义处理"。由于缺乏转义机制，攻击者可轻易在该参数中嵌入恶意分隔符，使得恶意端点能够将未经授权的OpenSearch批量操作混入后端数据库查询——这些操作将以管理端的高权限凭证执行。

## 严重危害与利用风险

利用此Wazuh CVSS 10分漏洞将对企业环境造成严重影响。通过执行注入命令，恶意Agent可获得破坏性数据库权限。例如：攻击者可跨索引执行任意文档删除，导致告警系统遭人为破坏及入侵痕迹清除；还能在仪表板对象中植入持久化载荷，使取证证据被轻易销毁，导致安全分析师在应急响应过程中完全失明。

### 密钥库凭证暴露

平台默认使用本地密钥库存储的凭证转发请求，这些角色在标准安装中映射为具备完全访问权限的管理员账户，使得注入操作能以最高数据库权限执行。

## 可用补丁与修复方案

该漏洞影响自5.0.0-beta1版本起的wazuh-manager安装实例，旧版4.x分支因不存在库存同步路径而完全不受影响。开发团队已在5.0.0-beta3版本中强制实施字符转义机制。网络管理员应立即查阅GitHub官方安全公告中披露的技术细节与复现代码，升级存在漏洞的管理端是阻断未授权OpenSearch批量操作的关键措施。

**参考来源：**

> [Critical Wazuh CVSS 10 Vulnerability Details and Proof-of-Concept Released](https://securityonline.info/wazuh-cvss-10-vulnerability/)

# 终端安全 # 企业安全

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

![](https://image.3001.net/images/20250224/1740390949_67bc4225d82f40f9874cd.png)

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
* [![](https://image.3001.net/images/20260114/1768369539_69672d830bc432e202279.png)](https://www.trustasia.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2026 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)