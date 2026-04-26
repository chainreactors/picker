---
title: 从网线到域控：一次完整AD渗透的全流程复盘
url: https://mp.weixin.qq.com/s/izlnlQtflW-WoY2RqRTe_g
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:00:45.919680
---

# 从网线到域控：一次完整AD渗透的全流程复盘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L7VicJKsiaibFDozxrHrBzkJt70sBTvYzAvbG9ibET6f97TzGpTiahRA0ZrrUZfhZ3AUaiaJYXACQSj7hrichyK1PXibBibdgicDicv4ZIkHm30pgdTpc4/0?wx_fmt=jpeg)

# 从网线到域控：一次完整AD渗透的全流程复盘

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 极客零零七 · AD攻击系列 · 第11篇（完结篇）

---

前10篇文章，每篇聚焦一个技术点。本篇把所有技术串成一条完整的攻击链——**模拟一次从零开始到拿下整个AD域的完整渗透测试过程**。

这不是某一次真实渗透的复述，而是基于大量实战经验构建的**典型攻击路径**。每一步都注明对应本系列的哪篇文章，方便回溯细节。

---

### 零、任务背景

**目标**：某中型企业（约1500员工），已签署渗透测试授权书。范围：内网AD域全覆盖，目标是获取Domain Admin权限并证明对核心资产的访问能力。

**起点**：攻击者已接入企业内网（模拟恶意内部人员或物理突破），拥有一台Kali Linux攻击机，IP地址通过DHCP获取。

**手里什么都没有——没有用户名，没有密码，没有域名。**

---

### 阶段一：网络侦察与信息收集（第1篇）

#### 目标：搞清楚面前的网络是什么样的

```
## 1. ARP扫描发现存活主机sudo arp-scan -l
## 结果：发现 10.10.10.0/24 网段有约80台主机存活## 10.10.10.1 看起来是网关## 10.10.10.10, 10.10.10.11 有多个端口响应
```

```
## 2. 针对性端口扫描——寻找域控nmap -sV -p 53,88,135,139,389,445,636,3268,5985 10.10.10.0/24 -oA scan_results
## 关键发现：## 10.10.10.10 - 端口88(Kerberos), 389(LDAP), 636(LDAPS), 3268(GC) 全开 → 域控DC01## 10.10.10.11 - 同样 → 域控DC02## 10.10.10.20 - 端口80,443,445 → Web服务器## 10.10.10.30 - 端口445,1433 → SQL服务器## 10.10.10.40-60 - 端口445 → 工作站群
```

```
## 3. 确认域名crackmapexec smb 10.10.10.10## SMB10.10.10.10445DC01[*]WindowsServer2019Build17763 x64## SMB    10.10.10.10  445  DC01  [*] domain:MEGACORP signing:True SMBv1:False## 域名：MEGACORP.LOCAL
```

```
## 4. 无认证信息收集## LDAP匿名绑定ldapsearch -H ldap://10.10.10.10 -x -s base namingContexts## 成功！返回 DC=megacorp,DC=local
## SMB空会话crackmapexec smb 10.10.10.10 -u '' -p '' --shares## 空会话可用！发现几个共享：NETLOGON, SYSVOL, IT-Share（可读）
## RID爆破枚举用户crackmapexec smb 10.10.10.10 -u '' -p '' --rid-brute 2000## 成功！枚举出约200个域用户
```

```
## 5. 密码策略crackmapexec smb 10.10.10.10 -u '' -p '' --pass-pol## [*] Minimum password length: 8## [*] Account lockout threshold: 5## [*] Account lockout duration: 30 minutes## [*] Reset account lockout counter after: 30 minutes
```

**信息收集阶段收获**：

* 域名：MEGACORP.LOCAL
* 2台域控：DC01(10.10.10.10)、DC02(10.10.10.11)
* 约200个用户名
* 密码策略：5次锁定，30分钟窗口
* 1台Web服务器、1台SQL服务器
* IT-Share共享可匿名读取

**用时：约30分钟**

---

### 阶段二：获取初始凭据（第1篇）

#### 多管齐下：Responder + 密码喷洒 + 共享搜索

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