---
title: K8s曝9.8分漏洞，黑客可获得Root访问权限
url: https://www.freebuf.com/news/413438.html
source: FreeBuf网络安全行业门户
date: 2024-10-23
fetch_date: 2025-10-06T18:51:00.228049
---

# K8s曝9.8分漏洞，黑客可获得Root访问权限

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

K8s曝9.8分漏洞，黑客可获得Root访问权限

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

K8s曝9.8分漏洞，黑客可获得Root访问权限

2024-10-22 15:41:05

所属地 上海

近日，安全研究人员Nicolai Rybnikar 发现Kubernetes镜像构建器中存在严重安全漏洞（CVE-2024-9486 ，CVSS ：9.8），攻击者可在特定情况下获得Root级访问权限，从而导致系统出现问题。

![](https://image.3001.net/images/20241022/1729584623_67175def728a8e7c0cb86.jpg!small)Nicolai Rybnikar进一步表示，该漏洞可允许在镜像构建过程中默认凭据保持启用状态，使用Proxmox提供商构建的虚拟机镜像没有禁用这些默认凭据，这意味着使用这些镜像的节点可能可以通过这些凭据访问。

## 漏洞详情

**描述**：该漏洞存在于Kubernetes镜像构建器处理某些操作的方式中，可能允许攻击者利用它获得对底层节点的根级访问权限。

**影响**：成功利用可能导致攻击者完全控制受影响的节点，从而执行任意命令、修改系统文件和访问敏感数据。

### 潜在攻击向量

**镜像构建过程**：攻击者可能针对镜像构建过程，注入恶意代码或配置。
**供应链攻击**：通过受损的镜像或构建工具，攻击者可以利用该漏洞。

### 影响范围

Kubernetes镜像漏洞对应0.1.37及更早版本。使用Proxmox提供商的这些版本的集群尤其容易受到影响。不仅影响集群的即时安全性，还影响其操作完整性。 相比之下，使用其他提供商构建的镜像不共享此漏洞，因此其影响范围更可控。企业更新到Image Builder的最新版本，实施推荐的缓解策略，并持续监测。

### 缓解策略

**更新Kubernetes**：确保所有Kubernetes组件（包括镜像构建器）都更新到包含CVE-2024-9486补丁的最新版本。版本0.1.38纠正了漏洞并引入了重大更改：它在镜像构建期间设置了一个随机生成的密码，并在完成后禁用构建器帐户。在此期间，组织可以通过在受影响的虚拟机上禁用构建器帐户来降低风险。

**镜像扫描**：实施严格的镜像扫描和验证过程，以检测并防止使用受损的镜像。

**访问控制**：加强访问控制和权限，限制谁可以与镜像构建器及相关组件进行交互。

**监控和日志记录**：增强监控和日志记录，以便快速检测可疑活动并对潜在的入侵做出响应。

### 安全建议

**立即行动**：评估当前Kubernetes环境的状态，并尽快应用必要的补丁。
**安全审计**：进行全面的安全审计，以识别可能被利用的任何潜在弱点或配置错误。
**员工培训**：教育团队了解与该漏洞相关的风险以及保护容器化环境的最佳实践。

Kubernetes镜像构建器中的CVE-2024-9486漏洞凸显了在容器化环境中维护更好安全实践的关键重要性，此漏洞尤其对使用受影响版本和Proxmox提供商的组织构成风险。升级到版本0.1.38是保护系统免受未经授权访问和潜在混乱的必要步骤。此外，实施推荐的缓解策略并进行定期的安全审计将有助于保护防御措施免受此漏洞及未来漏洞的侵害。

参考来源：<https://thecyberexpress.com/openssh-vulnerability/>

# 系统安全

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

漏洞详情

* 潜在攻击向量
* 影响范围
* 缓解策略
* 安全建议

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