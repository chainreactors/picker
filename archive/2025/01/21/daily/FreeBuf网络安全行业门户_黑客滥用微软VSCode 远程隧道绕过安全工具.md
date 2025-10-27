---
title: 黑客滥用微软VSCode 远程隧道绕过安全工具
url: https://www.freebuf.com/news/420277.html
source: FreeBuf网络安全行业门户
date: 2025-01-21
fetch_date: 2025-10-06T20:10:16.462293
---

# 黑客滥用微软VSCode 远程隧道绕过安全工具

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

黑客滥用微软VSCode 远程隧道绕过安全工具

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客滥用微软VSCode 远程隧道绕过安全工具

2025-01-20 11:54:14

所属地 上海

据Cyber Security News消息，微软VSCode 远程隧道功能正被攻击者利用，以绕过安全措施部署恶意脚本。

![](https://image.3001.net/images/20250120/1737345720_678dcab8e42523784e9ee.jpg!small)

VSCode 远程隧道是流行开发环境中的一项功能，让开发者通过安全隧道连接到远程计算机的本地编码环境，从而提高开发参与度和灵活性。

根据 On the Hunt 的博客文章，攻击者可在用户不知情的情况下安装安装 VSCode CLI 并创建远程隧道的文件或脚本，进而非法访问开发人员设备，窃取机密数据、部署恶意软件并通过网络横向移动。

最初发送的恶意 LNK 文件包含一个 PowerShell 命令，允许用户从远程 IP 地址下载并执行 Python 脚本。 VSCode CLI 二进制文件 code-insiders.exe 由 Python 脚本下载并执行。 Python 脚本使用 Github 上的 CLI 二进制文件生成并验证 VSCode 隧道。

![](https://image.3001.net/images/20250120/1737345305_678dc91990e54817aed7c.jpg!small)攻击链

为 VSCode 创建一个远程隧道，攻击者利用通过网络浏览器创建的隧道在 Python 有效载荷上执行命令。

![](https://image.3001.net/images/20250120/1737345376_678dc9608ba997445023b.jpg!small)
Python 脚本设置隧道

在不使用攻击者GitHub 帐户的情况下向 VSCode 进行身份验证，需按下 connect to tunnel 按钮。

![](https://image.3001.net/images/20250120/1737345543_678dca07907fc03984131.jpg!small)连接到隧道

一旦验证了账户，就可以看到有活动隧道的远程主机列表。 选择在线受害者主机将连接到该主机上运行的 VSCode 远程隧道。这使得遍历受害者远程计算机上的目录成为可能。此外，还可以创建新文件或脚本并远程运行。

因此，企业最好限制自己的员工或客户访问远程隧道，否则应禁止使用隧道，或采取措施防止隧道被滥用。

**参考来源：**

> [Hackers Abusing Microsoft VSCode Remote Tunnels To Bypass Security Tools](https://cybersecuritynews.com/hackers-abusing-microsoft-vscode-remote-tunnels/#google_vignette)

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