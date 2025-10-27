---
title: 人工智能图像编辑工具遭网络攻击，2000 万用户数据信息泄露
url: https://www.freebuf.com/news/393017.html
source: FreeBuf网络安全行业门户
date: 2024-03-02
fetch_date: 2025-10-04T12:11:51.125446
---

# 人工智能图像编辑工具遭网络攻击，2000 万用户数据信息泄露

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

人工智能图像编辑工具遭网络攻击，2000 万用户数据信息泄露

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

人工智能图像编辑工具遭网络攻击，2000 万用户数据信息泄露

2024-03-01 11:07:30

所属地 上海

##

人工智能图像编辑工具 Cutout.Pro 近期发生一起严重数据泄露事件，约 2000 万会员用户的电子邮件地址、散列和加盐密码、IP 地址以及姓名等敏感信息被放在数据泄露论坛上出售。![1709262468_65e1468464a0db0530ed3.png!small?1709262473772](https://image.3001.net/images/20240301/1709262468_65e1468464a0db0530ed3.png!small?1709262473772)

> Cutout.Pro 是一个人工智能驱动的照片和视频编辑平台，可用于图像增强、背景移除、漫反射、着色、旧照片修复和新图像内容生成。

化名为 "KryptonZambie "的威胁犯罪分子在 BreachForums 黑客论坛上分享了一个链接，该链接指向一个 CSV 文件（从 Cutout 窃取的 5.93 GB 数据），CSV 文件中有一个由 4140 万条记录组成的数据库转储，其中 2000 万条记录由唯一的电子邮件地址组成。

威胁犯罪分子嚣张的表示，在公布被盗数据时，Cutout 可能还没有意识到自身网络系统已经被入侵了。因此，目前其仍然可以轻松访问其内部系统。

![1709262475_65e1468b3bb18b9e9a2e6.png!small?1709262476037](https://image.3001.net/images/20240301/1709262475_65e1468b3bb18b9e9a2e6.png!small?1709262476037)

黑客在黑客论坛上发布数据（来源：Bleeping Computer）

泄露的 Cutout 用户数据包括以下信息：

> 用户 ID 和个人照片
>
> API 访问密钥
>
> 账户创建日期
>
> 电子邮件地址
>
> 用户 IP 地址
>
> 手机号码
>
> 用户类型和账户状态

据悉，数据泄露监控和警报服务 Have I Been Pwned (HIBP) 已经将 Cutout 用户数据泄露事件添加到其目录中，并确认泄露的数据集包括 19972829 Cutout 用户的敏感信息。威胁犯罪分子的泄密行为将使被盗数据在更大范围内流通，无疑会对 Cutout 造成严重影响。

目前，虽然 Cutout.Pro 方面没有通过官方声明核实此次数据泄露事件，但 HIBP 创始人 Troy Hunt 指出，他已经独立核实了多个与泄露邮件地址匹配的邮件，确认密码重置请求可以通过。此外，多家媒体也已经证实，数据泄露中列出的电子邮件与 Cutout.Pro 的合法用户完全匹配。

Cutout 用户数据泄露发生后，包括 Bleeping Computer 在内的多家媒体都向 Cutout 公司发送了电子邮件，以期获得此事件的更多信息，但都没有收到回复。

最后，网络安全专家强调，Cutout.Pro 新老用户应该立即在该服务和其它可能使用相同凭证的在线平台上重置密码，并时刻警惕有针对性的网络钓鱼诈骗。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/20-million-cutoutpro-user-records-leaked-on-data-breach-forum/

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