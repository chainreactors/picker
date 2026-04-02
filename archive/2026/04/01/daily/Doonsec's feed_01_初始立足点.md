---
title: 01_初始立足点
url: https://mp.weixin.qq.com/s/14U109CjpRFE7wO5-4BqRA
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:07.763643
---

# 01_初始立足点

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFDGSQyy4GGEmFx7mGI5ibWiaXOW1geP9zz6NJma58LicJlkV3EWnPz9unACFxdIr0R1agswgxwwRUtflPT9u3KcedKibgwox2zMc3s/0?wx_fmt=jpeg)

# 01\_初始立足点

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器中沉浸阅读

> 极客零零七 · AD攻击系列 · 第1篇

---

AD渗透的起点往往是——你站在企业内网里，面前是一个你一无所知的AD域，手里什么凭据都没有。后续所有攻击技术（Kerberoasting、ACL滥用、横向移动、委派攻击……）都有一个共同前提：你至少有一个域用户凭据。

**第一个域凭据从哪来？** 这是AD渗透中最关键、也最常被教程跳过的一步。本文系统梳理所有获取初始域凭据的方法，从零交互的网络层攻击到需要用户配合的社工手段。

### 一、无凭据侦察：先搞清楚面对的是什么

在没有任何凭据的情况下，你仍然可以收集大量信息。

#### 网络层发现

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9

```
## ARP扫描发现存活主机arp-scan -l
## Nmap扫描AD常见端口nmap -sV -p 53,88,135,139,389,445,636,3268,5985 10.10.10.0/24
## 端口88（Kerberos）开放 = 域控制器## 端口389（LDAP）开放 = 域控制器## 端口445（SMB）开放 = Windows机器
```

#### 无认证信息泄露

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13

```
## SMB空会话枚举（很多环境仍允许）enum4linux-ng -A 10.10.10.1crackmapexec smb 10.10.10.1 -u '' -p '' --sharescrackmapexec smb 10.10.10.1 -u 'Guest' -p '' --shares
## LDAP匿名绑定ldapsearch -H ldap://10.10.10.1 -x -b "DC=domain,DC=local" "(objectClass=user)" sAMAccountName
## RPC空会话rpcclient -U "" -N 10.10.10.1rpcclient $> enumdomusersrpcclient $> enumdomgroupsrpcclient $> getdompwinfo     # 密码策略！
```

**密码策略是关键情报**——它决定了密码喷洒的安全参数（锁定阈值、锁定窗口、最小密码长度）。

#### DNS枚举

* 1
* 2
* 3
* 4
* 5
* 6
* 7

```
## 区域传送（很少成功，但值得试）dig axfr domain.local @10.10.10.1
## 反向DNS查找，发现主机名dnsrecon -d domain.local -n 10.10.10.1 -r 10.10.10.0/24
## 通过主机名猜测功能：mail、vpn、rdp、sql、backup...
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

极客零零七

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过