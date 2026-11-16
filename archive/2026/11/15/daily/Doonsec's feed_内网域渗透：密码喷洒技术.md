---
title: 内网域渗透：密码喷洒技术
url: https://mp.weixin.qq.com/s/LQfCEtj4HUogmO_B68gSJg
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:43:29.828017
---

# 内网域渗透：密码喷洒技术

# 内网域渗透：密码喷洒技术

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

拿到 webshell、隧道也搭好了，面对一整段 192.168.21.0/24 的内网，下一步从哪下手？外网打得再漂亮，最终价值都要落在内网里。常规企业安全建设普遍"外网严、内网松"：外网部署了各种安全设备，内网里弱口令、中间件漏洞一大堆。进了内网，性价比最高的横向动作，往往就是密码喷洒。

根因很简单：域环境里，大量员工入域后初始密码一直没改，再加上企业习惯用"公司名+年份"这类规律密码，密码复用率极高——一套密码本喷下去，倒下的不是一台机器，是一整片 C 段。

本文复盘一次完整的实战链路：GitLab 未授权拿到账号密码 → 同网段 Shiro 反序列化注入内存马，摸到隔离网段 192.168.21.x/24 → FRP 搭 SOCKS5 隧道 → fscan 摸清家底 → 一波喷洒喷出两台主机的有效域口令，RDP/SMB 双通道落地。密码本来源、工具选择、喷洒节奏，一文讲清。

---

## 密码喷洒：反着来的爆破

**什么是密码喷洒攻击？**

通常情况下，穷举攻击是固定好用户名，用多个密码逐个尝试验证。与穷举攻击相反，密码喷洒攻击是固定好密码，拿一批用户名去逐个验证。在域系统中，员工往往因为初始入域的密码一直未修改，被攻击者用密码喷洒的方式直接拿下权限。

密码喷洒属于一种自动化攻击方式：为了避免只盯一个用户爆破而触发账户锁定，密码喷洒是对一批用户做尝试——既避开了单用户的锁定阈值，也提高了撞出有效口令的效率。说白了，它就是反着来的爆破：不换密码，换用户名。

```
一个密码试一百个用户，没有任何一个用户会触发锁定；而域内初始密码不改、口令复用又普遍，这就是喷洒能"一波喷穿一片"的根本原因。
```

**打进去之前，先回到信息收集**

在获取到 webshell、打通内网隧道之后，就回到了渗透测试的本质——信息收集。拿到 shell 的机器上，用前期收集到的账号密码，就可以对后续的机器做密码喷洒。这次实战的前置铺垫分三步：

**信息泄露：** 通过 GitLab 未授权获取到一批账号密码。

![GitLab未授权访问获取账号密码](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1goXXT9PjrD55gEzTpzCHHmLNGJFk5GFUhdHiau1IUmvp3obkjjH45NXic5YgRCQJviciaL0oDrgJWx0FceuC8N0jSaKhB9QJY2COrY/640?wx_fmt=png&from=appmsg)

**突破边界：** 同网段 Shiro 反序列化注入内存马，发现隔离网段 192.168.21.x/24。

![Shiro反序列化注入内存马突破边界](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grjITVL9I3uPGGUrTiaaReQ0Z8CxH9HStyYcdjedNCgfVNphUiaSLGBibN7ogwVUvKMOtoPhGTic8kVsHj5461F29KxdTK67pwiaicHQ/640?wx_fmt=png&from=appmsg)

**搭建隧道：** FRP 搭建 SOCKS5 代理 + Proxifier 全局代理，把攻击流量送进隔离网段。

![FRP搭建SOCKS5代理隧道](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1grkIxnIQwM39D1YTranbfuhvBKzqnHe7Lqz98JE6frumwia8KlNLaMa6UfCWUt5zyMPuMsBekITbo7KaY65XDV1uJwxroHUgKa8/640?wx_fmt=png&from=appmsg)

---

## fscan 摸清内网家底

隧道通了，先跑一轮 fscan，把内网的主机、端口、服务指纹一次性收齐：

```
192.168.21.130:80 open
192.168.21.80:8080 open
192.168.21.191:135 open
D:445 open
192.168.21.191:445 open
192.168.21.130:445 open
192.168.21.73:445 open
192.168.21.80:445 open
192.168.21.55:445 open
192.168.21.27:445 open
192.168.21.130:135 open
192.168.21.191:139 open
192.168.21.172:139 open
192.168.21.130:139 open
192.168.21.73:139 open
192.168.21.69:139 open
192.168.21.80:139 open
192.168.21.55:139 open
192.168.21.27:139 open
192.168.21.73:135 open
192.168.21.172:135 open
192.168.21.69:445 open
192.168.21.80:135 open
192.168.21.55:135 open
192.168.21.69:135 open
192.168.21.27:135 open
192.168.21.27:88 open
192.168.21.73:7680 open
[+] NetInfo:
[*]192.168.21.172
   [->]wdwork2
   [->]192.168.21.172
[+] NetInfo:
[*]192.168.21.130
   [->]zentao
   [->]192.168.21.130
[+] NetInfo:
[*]192.168.21.191
   [->]wdwork3
   [->]192.168.21.191
[+] NetInfo:
[*]192.168.21.69
   [->]wdwork5
   [->]192.168.21.69
[+] NetInfo:
[*]192.168.21.55
   [->]wdwork1
   [->]192.168.21.55
[+] NetInfo:
[*]192.168.21.27
   [->]DC
   [->]192.168.21.27
[*] 192.168.21.27  (Windows Server 2012 R2 Standard 9600)
[+] NetInfo:
[*]192.168.21.73
   [->]wdwork4
   [->]192.168.21.73
[+] 192.168.21.172        MS17-010        (Windows 7 Professional 7601 Service Pack 1)
[+] 192.168.21.55        MS17-010        (Windows 7 Professional 7601 Service Pack 1)
[+] 192.168.21.191        MS17-010        (Windows 7 Ultimate 7601 Service Pack 1)
[*] 192.168.21.191       WDMHOUT\WDWORK3           Windows 7 Ultimate 7601 Service Pack 1
[*] 192.168.21.172       __MSBROWSE__\WDWORK2           Windows 7 Professional 7601 Service Pack 1
[*] 192.168.21.130       WDMHOUT\ZENTAO            Windows Server 2012 R2 Standard 96080
[*] 192.168.21.27  [+]DC WDMHOUT\DC                Windows Server 2012 R2 Standard 9600
[+] NetInfo:
[*]192.168.21.80
   [->]ftweb
   [->]192.168.21.80
[*] 192.168.21.55        WDMHOUT\WDWORK1           Windows 7 Professional 7601 Service Pack 1
[*] 192.168.21.73  (Windows 10 Pro 16299)
[*] WebTitle:http://192.168.21.80:8080 code:200 len:154    title:login
[*] 192.168.21.80        WDMHOUT\FTPWEB            Windows Server 2008 R2 Enterprise 7601 Service Pack 1
[*] 192.168.21.80  (Windows Server 2008 R2 Enterprise 7601 Service Pack 1)
```

扫描结果里是一堆 Windows 机器，并且直接扫到了 DC（192.168.21.27，Windows Server 2012 R2），还有三台机器命中 MS17-010。有 DC、有大量域内主机，这就是标准的域环境——密码喷洒的主场。

---

## 喷洒实战：一波密码本喷穿 C 段

**密码本从哪来**

密码本靠前期信息收集整理得到，实测来源包括：信息泄露（GitLab 这类）、翻配置文件、翻回收站、桌面账号密码本、mimikatz 抓到的凭据。本次使用的密码本如下（已去重）：

```
ErpBack@2021..
Wdmh@Test123
Wdmh@Work123
Wdmh@work2021..
Wdmh@creat2021..
wdmh@123
Wangdi.com@123
Wangdi.com@123..
Wangdi.com@Zentao123
Wangdi.com@CRM123
WDMHINTRA@2021..
wdmhintra.com@2021..
wdmhintra.com@123.
wangdi@123
wangdi@123..
CRM@2021..
MH@2021..
PH1@2021..
ERP@2021..
Zhangdi@123
zhangdi@123
Wangwei@123
wangwei@123
Zhangjie@123
zhangjie@123
Zhangsan@123
zhangsan@123
Zhangsan@2021..
Lisisi@123
lisisi@123
lisisi@2021..
Zhangzq@123
Zhangzq@WdmhB123
```

**工具选择：超级弱口令**

把收集到的账号密码导入超级弱口令工具中使用：

![超级弱口令工具导入密码本](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpzKzWNESSnlf6o7mWxlp0gXoe4zFQCjEshKoyOgVTapNQW6WtfHYxaHACuaoauZMwaVw0HKUoVDXIMqicA9pbqDhB8IfzMRVgA/640?wx_fmt=png&from=appmsg)

**喷哪些协议**

一般对 SSH、RDP、SMB 进行喷洒，原因很直接：

• SSH：直接获取主机权限

• RDP：远程登录到这台机器

• SMB：横向移动

**喷洒结果**

192.168.21.55 —— 口令复用，一个账号 RDP/SMB 双通道可用：

• RDP——WDWORK3\wdwork----Wdmh@Work123

• SMB----445----WDWORK3\wdwork----Wdmh@Work123

![192.168.21.55喷洒出RDP与SMB有效口令](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqRHpSkamhzCu1odU7CJOicVvSiabH7Vb9Nqv9icMl0bjn3EOFMQZuiaoS7d8Mgwx1UlQtqUKE6nn0u1k2OzVf9FCsmjxczVtEZ3tc/640?wx_fmt=png&from=appmsg)

192.168.21.130 —— administrator 的口令同样在密码本里：

• RDP----3389----administrator----Wangdi.com@123

• SMB----445----WDWORK1\administrator----Wangdi.com@123

![192.168.21.130喷洒出administrator有效口令](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grYaBmV50ACld91hxuFNqc2ebw9icLnJA4jnLbbXPrIqMTTo3PyINtib9bG8C6TOFUhoUPo6pmOO1UweKsS4Z349jRPibvkCia5GQQ/640?wx_fmt=png&from=appmsg)

```
一波喷洒直接命中两台主机的有效域口令，且都是 RDP/SMB 双协议可用——拿到的不是"能登录的账号"，而是横向的桥头堡。
```

---

## 写在最后

密码喷洒的思路一句话就能说清：不断收集内网账号密码，不断去喷洒。几个实战要点：

1. **密码本来源**：信息泄露、翻配置文件、翻回收站、桌面账号密码本、mimikatz 抓到的，来源越杂，命中率越高；

2. **工具放内网跑**：喷洒工具尽量放到内网机器上执行，本地跑线程高、流量大，容易把隧道冲崩；

3. **针对 C 段喷**：喷洒时针对一个 C 段进行，能爆出来的机器会多很多；

4. **滚雪球**：内网渗透中，能拿到主机管理员账号密码，横向就事半功倍，尤其是在大内网环境里，密码复用率很高——一波喷洒拿到一批主机，对拿到的主机再抓密码，用新密码再喷一波，如此反复。口令获取还可以翻敏感文件，运气好的话，桌面就有账号密码.txt 这样的文件。

可喷洒的端口也不限于 445 和 3389，135、139、22、1433、3306、1521 都在射程内；工具不止超级弱口令，fscan 同样能干，顺手就行。

防御方向也顺带说一句：强制新账号首次登录改密、本地管理员密码随机化（LAPS）、按源地址维度监控 4625 爆破行为，都能把"一波喷穿一片"的收益打下来。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HezRQjNneVHy39103FjCvxFaZicO2OgEB05ZbBLwibDiaCTqDJNUHUCC9OXjVeiasG4ibOVR0dg284RCzVquVhvQ3xQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过