---
title: 在线PDF工具暴露了数万份用户上传的文件
url: https://www.freebuf.com/news/405809.html
source: FreeBuf网络安全行业门户
date: 2024-07-13
fetch_date: 2025-10-06T17:42:51.625277
---

# 在线PDF工具暴露了数万份用户上传的文件

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

在线PDF工具暴露了数万份用户上传的文件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

在线PDF工具暴露了数万份用户上传的文件

2024-07-12 11:13:29

所属地 上海

随着在线文档处理需求的增加，一些看似好用且免费的工具在安全性上可能并不靠谱。据Cyber News消息，两款在线PDF制工具已经暴露了数万份用户上传的文件。

![](https://image.3001.net/images/20240712/1720754057_66909f89c49f4ed9fc6b7.png!small)

这两款PDF在线工具分别为PDF Pro （pdf-pro.io） 和 Help PDF （help-pdf.com），由同一家英国公司运营，均为用户提供 PDF 转换、压缩、编辑以及签署文档功能。

研究人员发现，暴露的 Amazon S3 存储桶呈开放状态，意味着任何人都能够获取其中的数据。对其进行分析发现，这两款工具已经累计暴露了89062份文件，其中87818 份文件通过 PDF Pro 上传，1244 份文件通过 Help PDF 上传。

这些暴露的文件涉及了大量用户的敏感信息，包括、护照、驾驶执照、证书、合同以及其他一些个人文件和资料。研究人员称，通过访问这些个人文件，网络犯罪分子可以从事各种欺诈活动，例如申请贷款，出租房产或使用受害者的身份进行物品交易，甚至可以更改或伪造合同或许可证等文件，以创建虚假身份、伪造资格或操纵法律协议以谋取利益，从而可能给受害者带来法律问题。

针对暴露的存储桶，Cyber News提出了如下缓解措施：

* 立即限制对存储桶的公有访问
* 更改存储桶策略和访问控制列表 （ACL） 以仅将访问权限限制为授权用户或应用程序
* 确保存储桶中的所有对象都设置为私有或配置了适当的访问控制
* 在存储桶上启用服务器端加密，以保护静态数据。管理员可以根据自己的要求在 SSE-S3、SSE-KMS 或 SSE-C 之间进行选择

对于用户而言，虽然不少PDF在线工具都会声明会对用户文件保护，包括会加密存储并在用户处理完文件后删除，但显然，其中一些工具仍然会保留用户文件，因此建议用户不要将个人敏感文件上传至网络。

**参考来源：**

> [Online PDF maker leaks user-uploaded documents](https://cybernews.com/security/online-pdf-maker-leaks-user-documents/)

# 数据安全

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