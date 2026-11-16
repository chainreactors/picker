---
title: AD域攻防：1域控信息收集
url: https://mp.weixin.qq.com/s/7qH1C8ya4Iwdn_i2by82Qw
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:43:52.400262
---

# AD域攻防：1域控信息收集

# AD域攻防：1域控信息收集

原创

云和
云和

泷羽sec-云和

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 一、 域信息收集

Active Directory是一个可以通过域控制器来管理连接在同一逻辑网络中的一组计算机和用户系统。Windows域包含以下组件：

### 1. LDAP —— 公司的“通讯录查询台”

AD 数据库就像一个巨型通讯录，里面存着所有员工、部门、电脑的信息。LDAP 就是查这个通讯录的标准问法：你说“帮我找研发部所有经理”，它按固定格式回你。MS-DRSR 是“两台域控之间怎么同步通讯录”的规矩，MS-ADTS 是“这个通讯录整体怎么设计”的说明书。你不用背规范名，记住LDAP ≈ 查通讯录的协议就够了。

---

### 2. AS（认证服务器）—— 公司的“前台门卫”

你进公司大门，门卫要核实“你是不是你”。AS 就是干这个的，而且它支持好几种“证件类型”：Kerberos 票、NTLM 口令、Netlogon 安全通道、WDigest 凭据。不同客户端拿不同证件来，门卫都认。

---

### 3. GPO —— 公司统一下发的“规章制度模板”

管理员写一套规则（比如“所有电脑屏幕 10 分钟自动锁屏”“禁止 U 盘”），GPO 就是把这套规则批量贴到每台电脑上的机制。贴的时候走两个通道：LDAP管“这条规则贴到哪个部门（OU）”，SMB管“规则文件本身怎么传到那台电脑上”。

---

### 4. DNS —— 公司的“电话簿/导航”

你想找域控办事，但不知道它在哪台机器上。DNS 里有一条专门记录（SRV 记录）写着“域控在这”，客户端一查就知道往哪走。DNS 配错了，就像电话簿上号码写错——全公司找不到门卫，域直接瘫。

---

### 5. Kerberos —— “一次性门票系统”

进门卫那换一张门票（TGT），之后去各个部门办事，出示门票换部门小票（服务票据），不用每次重新报密码。门票有有效期，过期作废。DC 就是发票中心（KDC）。

---

### 6. Netlogon —— 电脑和域之间的“专用对讲机”

员工电脑开机时要跟域说“我上线了，我是这台机器，给我验证”。Netlogon 就是这条安全通道，管计算机账户登录、域和域之间建立信任关系、通道断了怎么修。

---

### 7. W32time —— 公司统一的“对表”

Kerberos 门票对时间极其敏感：你电脑和域控时间差超过 5 分钟，票直接作废。所以域内必须有一台“标准钟”，大家定期对表，W32time 就是干这个的。不对表，门都进不去。

---

### 8. FSMO —— 五个“必须专人负责”的特殊岗位

域控之间大部分事可以商量着来（多主复制：谁都能改，改完互相同步）。但有五件事必须一个人说了算，不然会乱套，这就是 FSMO 五个角色：

* 架构主机（林级）：管“通讯录允许有哪些字段”，比如能不能加“微信号”这个属性。
* 域命名主机（林级）：管“能不能新开分公司（加新域）”，防止重名。
* PDC 模拟器（域级）：管“密码改了第一时间告诉谁”“时间以谁为准”，像个总协调员。
* RID 主机（域级）：管“发工号”，保证每个员工/电脑的编号不重复。
* 基础结构主机（域级）：管“跨部门人员变动时，引用关系别断”，像个维护交叉索引的。

---

### 一句话串起来

> DNS 是电话簿，帮你找到门卫（AS/Kerberos）；门卫发票，Netlogon 管机器对讲，W32time 保证票不过期；进公司后查通讯录（LDAP）、按规章制度（GPO）办事；五件必须专人拍板的事由 FSMO 五个岗位负责。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0aM8oEsnxzfDp0eVPWEjET53f5uAVF4y7Y2pSIzibfEGBKvfa2pMY1l43qybUeZMXYl6WanKErE0J7WhD4iaCkunOV02lG03WsDUSIfQ2JNt8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0aM8oEsnxzec62p6RZIvjqVuzMknIeGccphZ9icicZdUdz5XMrlUCZiaozjfliavADWZI8E0PwrJGeXs4UT9EatW2UNhWiaOeiaooGl8ribibBGy9s0/640?wx_fmt=png&from=appmsg)

这些组件协同工作：DNS帮助客户端找到DC，DC通过Kerberos验证身份，并依据AD DS 数据库中的对象信息和OU上链接的GPO来授权和管理资源。理解这套逻辑与物理的映射关系，是后续进行域内信息收集和攻击路径分析的结构性基础。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0aM8oEsnxzcU0oibRwAxsk2XOAo7OFgyQW4HxEaicEDxmELmHV9aeibx4OvcCiaPqeHklCDZQZpjbibymKO8QoQ0cia3R4zzZVnTb48mujNT2iad20/640?wx_fmt=png&from=appmsg)

这样对比看应该通俗易懂一点

客户端通过DNS SRV 记录找到 DC；

DC 中的KDC完成 Kerberos 身份验证并签发票据；

DC 依据AD DS 数据库中的对象信息和 OU 结构，以及OU 上链接的 GPO，形成授权与管理策略；

客户端携带票据访问资源，资源侧依据票据和策略决定是否放行。

这样对比看应该通俗易懂一点

1.DNS SRV 查询

windows上：

把 <域名> 替换为实际域名

```
nslookup -type=srv _ldap._tcp.dc._msdcs.<域名>
```

如果 DNS 不在本机，可以在命令末尾加上 DNS 服务器地址，指定向哪台 DNS 查询

```
nslookup -type=srv _ldap._tcp.dc._msdcs.<域名>
```

一个典型的输出就是

```
_ldap._tcp.dc._msdcs.corp.local   SRV service location:          priority       = 0          weight         = 100          port           = 389                   #端口          svr hostname   = dc01.corp.local       #svr hostname 就是域控制器的主机名dc01.corp.local   internet address = 10.0.0.10   #ip
```

linux上：

```
dig -t SRV _ldap._tcp.dc._msdcs.<域名>
```

以及

| 要查什么 | SRV 记录名 | 说明 |
| --- | --- | --- |
| 普通域控制器 | `_ldap._tcp.dc._msdcs.<域名>` | 最直接的 DC 定位记录 |
| PDC 模拟器 | `_ldap._tcp.pdc._msdcs.<域名>` | 只返回担任 PDC 模拟器的那一台 DC |
| 全局编录（GC） | `gc._msdcs.<域名>` 或 `_ldap._tcp.gc._msdcs.<林名>` | 返回全局编录服务器，在多域林中尤其有用 |
| Kerberos KDC | `_kerberos._tcp.<域名>` | 返回运行 KDC 的 DC，与 LDAP 记录相互印证 |
| Kerberos 密码服务 | `_kpasswd._tcp.<域名>` | 同样指向 DC，可作为辅助确认 |

这些都要有一个前提：

这些查询要求当前机器使用的 DNS 服务器能解析目标 AD 域名。如果当前 DNS 指向公网或与目标域无关，查询会失败。此时需要显式指定目标 DNS 服务器（通常就是目标 DC 本身的 IP，因为 AD 集成 DNS 一般部署在 DC 上）。

2.利用端口服务区判断域控制器

首先域控制器肯定指的是Windows计算机可以通过135、139、445、5985端口来判断，并且在80端口运行IIS服务。域控制器一定会运行LDAP服务，我们通过端口服务服务协助我们确认该计算机是不是域控制器，并且DNS服务一般是安装在域控上

| 端口 | 协议/服务 | 对 DC 判断的意义 |
| --- | --- | --- |
| 88/tcp | Kerberos | DC 作为 KDC 监听；强信号，但 Linux KDC 也可能开 |
| 389/tcp | LDAP | DC 的目录服务；强信号，但其他 LDAP 服务也可能开 |
| 636/tcp | LDAPS | LDAP over TLS，DC 常见；辅助确认 |
| 3268/tcp | Global Catalog (LDAP) | DC 特有，全局编录端口；很强信号 |
| 3269/tcp | Global Catalog (LDAPS) | 同上，TLS 版本；辅助确认 |
| 9389/tcp | ADWS（Active Directory Web Services） | 只在 DC 上默认运行；很强信号 |
| 464/tcp/udp | Kerberos 密码更改 | DC 监听；辅助确认 |
| 53/tcp/udp | DNS | DC 常兼做 DNS，但 DNS 可分离部署；只能辅助 |
| 135/tcp | RPC Endpoint Mapper | 任何 Windows 主机都有；不能区分 DC |
| 445/tcp | SMB | 任何 Windows 主机都有；不能区分 DC |
| 5985/5986 | WinRM | 可选，不是 DC 标志 |

关键点：135 和 445 只能说明“这是一台 Windows”，不能用来判定 DC。真正有区分力的是88、389、3268、9389这四个。

使用net group "domain controllers" /domain命令在域内通过SAMR获取域控制器地址

### 3.协议交互与枚举

AD 本质上是一个 LDAP 目录，直接查询即可获取大量域信息

RootDSE 匿名探测：即使没有凭据，也可尝试匿名读取根 DSE，获取 defaultNamingContext（域名）等基础信息。

bash

```
ldapsearch -x -H ldap:// -s base -b ”” ”(objectClass=*)” defaultNamingContext
```

查询域控制器对象：拥有任意域用户凭据后，可直接查询 domainController 对象类。

bash

```
ldapsearch -x -H ldap:// -D ”<用户@域名>” -w '<密码>' \  -b ”dc=<域名>,dc=<后缀>” ”(objectClass=domainController)” dNSHostName
```

Samba 套件中的 rpcclient 工具可以通过 SAMR、NETLOGON 等接口与 DC 交互，是 Linux 上非常经典的枚举工具。

* 获取 DC 名称：`dsgetdcname` 命令基于 NETLOGON 协议，专门用于发现域控制器。

  bash

  ```
  rpcclient -U ”” -N  -c ”dsgetdcname”
  ```

  或使用 `net` 命令：

  bash

  ```
  net rpc info -S  -U ””
  ```

  这会返回 DC 的 NetBIOS 名称（如 `\\DC01`），再用 `nslookup` 解析即可得到 IP。
* 枚举域信息：连接后使用 `enumdomains`、`querydominfo` 等命令，可能间接暴露 DC 名称。

### 与 LDAP/DNS SRV 方法的核心区别

| 特性 | `net group "domain controllers" /domain` | DNS SRV 查询 | LDAP RootDSE 查询 |
| --- | --- | --- | --- |
| 核心协议 | SAMR (over SMB/RPC, 端口445) | DNS (端口53) | LDAP (端口389) |
| 本质 | 查询“Domain Controllers”组的成员 | 查询服务定位记录 | 查询目录服务的根信息 |
| 依赖条件 | 域用户权限，SMB 可达 | 正确的 DNS 配置 | LDAP 可达，且允许匿名/认证绑定 |
| 主要优势 | 不依赖 DNS/LDAP，信道不同，可作为备用或隐蔽路径 | 最标准、信噪比高、直接返回 FQDN | 可同时获取域名、林名等丰富上下文 |

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gWeq1Qf233GpH82dM46B0piaUYCho5xCtG0BoAnmtJQKEqkW5f9VSD9LtMFbuDPcgTUPpyo5gYqP1xMiaDZKbfow/0?wx_fmt=png)

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