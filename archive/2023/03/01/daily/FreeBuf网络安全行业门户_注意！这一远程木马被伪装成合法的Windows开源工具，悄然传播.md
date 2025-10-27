---
title: 注意！这一远程木马被伪装成合法的Windows开源工具，悄然传播
url: https://www.freebuf.com/news/358876.html
source: FreeBuf网络安全行业门户
date: 2023-03-01
fetch_date: 2025-10-04T08:20:24.331632
---

# 注意！这一远程木马被伪装成合法的Windows开源工具，悄然传播

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

注意！这一远程木马被伪装成合法的Windows开源工具，悄然传播

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

注意！这一远程木马被伪装成合法的Windows开源工具，悄然传播

2023-02-28 13:40:59

所属地 上海

近日，趋势科技发现了一波新的攻击，目的是将PlugX远程访问木马伪装成一个名为x32dbg的开源Windows调试器工具进行传播。该合法工具允许检查内核模式和用户模式代码、故障转储及CPU寄存器。

经研究人员分析x32dbg.exe有一个有效的数字签名，因此它被错认为是安全的。这让攻击者能够逃避检测，保持持久性，提升权限，并绕过文件执行限制。

![](https://image.3001.net/images/20230228/1677554311_63fd7287e958bd1f1486a.png!small)

该RAT使用DLL侧面加载，如x32dbg调试工具（x32dbg.exe）时，恶意加载自身有效载荷DLL。

攻击者通过修改注册表和创建计划任务来实现持久性，即使在系统重新启动时也能保持访问。

专家报告说，x32dbg.exe被用来投放一个后门，一个UDP shell客户端，收集系统信息，收集主机信息，并创建一个线程来持续等待C2命令，并使用硬编码的密钥来解密C&C通信。

最后，报告总结说，尽管安全技术有所进步，但攻击者继续使用这种技术，因为它利用了对合法应用程序的基本信任。只要系统和应用程序继续信任和加载动态库，这种技术对于攻击者提供恶意软件和获取敏感信息仍然是可行的。

> 参考链接：securityaffairs.com/142770/malware/plugx-trojan-disguised-windows-tool.html

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