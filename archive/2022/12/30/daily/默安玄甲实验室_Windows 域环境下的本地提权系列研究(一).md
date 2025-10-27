---
title: Windows 域环境下的本地提权系列研究(一)
url: https://mp.weixin.qq.com/s?__biz=MzkzNjI2MzgzOA==&mid=2247485148&idx=1&sn=fa5b955d4bd9cff1c8e5235cf2165f3b&chksm=c2a02f2df5d7a63b3de6d3ccf13481d9c70aa93b0ec2cee7c1c7c445e629c692189e7d265184&scene=58&subscene=0#rd
source: 默安玄甲实验室
date: 2022-12-30
fetch_date: 2025-10-04T02:45:07.412074
---

# Windows 域环境下的本地提权系列研究(一)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/50Hiagic8dst4pJQX0wcQR2PM4kp1jpuySGSK6icywQStGOR7ffr7nB9wW8RoNlXJW7eSibGSJqibia4IoAqbXvdKQuw/0?wx_fmt=jpeg)

# Windows 域环境下的本地提权系列研究(一)

默安玄甲实验室

## 前言

我们将针对于域环境下的本地提权进行研究并输出一系列专题文章，以域内的一些老生常谈的技术为基础，并加以组合利用，最终实现自动化的域内本地提权。接下来我们就以经典的委派为开场，拉开Windows 域环境下的本地提权研究系列的第一个大幕。

## 什么是委派

Kerberos 委派是 Windows ADDS 中的一项重要功能，旨在解决身份认证中的双跳问题（Double-hop Problem），一个经典的例子是：

Web 服务器 A 上跑着一个文件管理应用，服务器 A 仅提供 Web 服务，真正的文件将存储在共享服务器 B 上。用户登录 Web 系统并上传文件，此时服务 A 需要以用户的身份将文件发送至服务 B，但是服务 A 并没有从用户到服务 B 的 ST。此时，委派的作用就是允许服务 A 模拟用户去获取这张 ST，并访问服务 B。

一句话总结，Kerberos 委派作用于服务账户，使服务能够模拟其他计算机账户或用户账户，达到服务能够以其他用户的权限访问另一个服务的目的。

## 委派发展史

### 1.1 非约束委派

微软最早在 Windows 2000 中引入了非约束委派实现上述功能。非约束委派在传统的 Kerberos 认证基础上，新增了可转发的 TGT：

![](https://mmbiz.qpic.cn/mmbiz_png/50Hiagic8dst5gt9fQXCPNhfibh6U4ZWZk8KUvacsJ2fFydvoIycDB8H7vvuS4GykWOVhUEpdfrEbxn253qdr685w/640?wx_fmt=png)

1. 1. 用户访问服务 A，使用 Kerberos 协议发起认证。
2. 2. 用户通过 `AS Exchange` 请求并获得一张可转发的 TGT。
3. 3. 用户通过 `TGS Exchange` 携带可转发的 TGT 请求 KDC。
4. 4. KDC 根据用户请求的 SPN，检查对应的服务 A，发现其 `userAccountControl` 设置了 `TRUSTED_FOR_DELEGATION` Flag，返回一张转发的 TGT。
5. 5. 用户通过 `TGS Exchange` 携带可转发的 TGT 请求并获得一张从用户到服务 A 的 ST。
6. 6. 用户通过 `AP Exchange` 将转发的 TGT、该 TGT 的会话密钥、ST 发送给服务 A。
7. 7. 服务 A 认证该用户能够合法访问自己，至此完成用户的认证。
8. 8. 服务 A 通过 `TGS Exchange` 携带用户 TGT、代表用户请求并获得从用户到服务 B 的 ST。

事实上，**服务 A 可以利用这张用户 TGT 申请从用户到任意服务的 ST**，当然，最终能否访问这些服务取决于该用户自身的权限。

#### 配置

域管理员权限执行：打开服务账户（所有配置了 SPN 的账户都是服务账户，包括默认的机器账户和配置了 SPN 的用户账户）的属性菜单，点击委派选项卡，勾选"信任此计算机来委派任何服务(仅 Kerberos )"，即可完成该服务账户的非约束委派配置。

配置完成后，查看该服务账户的 `userAccountControl` 属性，已存在 `TRUSTED_FOR_DELEGATION` 标志位。

```
AdFind.exe -h 192.168.159.112 -u island.com\zhangsan -up ZS@123qwe -b "DC=island,DC=com" -f "(userAccountControl:1.2.840.113556.1.4.803:=524288)" -dn
```

###

### 1.2 约束委派

从上述过程中可以看出，非约束委派并不能阻止服务 A 滥用用户 TGT，因此微软在 Windows 2003 中引入了约束委派。约束委派的通信架构完全不同，新增了 S4U2self 和 S4U2proxy 两个 Kerberos 子协议：

1. 1. S4U2proxy，Service for User to Proxy，该扩展协议允许服务代表用户获取从用户到不同服务的 ST。
2. 2. S4U2self，Service for User to Self，该扩展协议允许服务代表用户获取从用户到服务自身的 ST。

这两个扩展协议的作用都是让服务代表用户从 KDC 请求 ST。不同的是，服务通过 S4U2proxy 获取的是其他服务的 ST，这是约束委派的最终目的。而服务通过 S4U2self 获取的是服务自身的 ST，用于协议转换，该 ST 可以充当 S4U2proxy 请求所需的必选参数之一。

![](https://mmbiz.qpic.cn/mmbiz_png/50Hiagic8dst5gt9fQXCPNhfibh6U4ZWZk8gicicOtcvphz6JpNntMuZCjC6RYKW3jiaOY4ekeia4vJavoB6iacRrQI5hA/640?wx_fmt=png)

#### S4U2proxy

约束委派没有可转发的 TGT，取而代之的是可转发的 ST：

1. 1. 用户访问服务 A，使用 Kerberos 协议发起认证。
2. 2. 用户通过 `AS Exchange` 请求并获得一张正常的 TGT。
3. 3. 用户通过 `TGS Exchange` 携带正常的的 TGT 请求 KDC。
4. 4. KDC 根据用户请求的 SPN，检查对应的服务 A，发现其 `userAccountControl` 设置了 `TRUSTED_TO_AUTH_FOR_DELEGATION` Flag，返回一张可转发的、从用户到服务 A 的 ST。
5. 5. 用户通过 `AP Exchange` 将 ST 发送给服务 A。
6. 6. 服务 A 认证该用户能够合法访问自己，至此完成用户的认证。
7. 7. 服务 A 通过 `TGS Exchange(S4U2proxy)` 将自身的 TGT、可转发的 ST 发送给 KDC
8. 8. KDC 检查服务 A 的 `msDS-AllowedToDelegateTo` 属性，确定服务 B 位于其中，返回一张从用户到服务 B 的 ST。

发起 S4U2proxy 请求时，服务 A 必须提供两样东西：1. 自身的 TGT；2. 可转发的、从用户到服务 A 的 ST。

该过程中，KDC 分别进行两项检查：1. 检查服务 A 的 `userAccountControl TRUSTED_TO_AUTH_FOR_DELEGATION flag`，确定是否信任服务 A 进行委派；2. 检查服务 A 的 `msDS-AllowedToDelegateTo` 属性，确定是否允许委派至服务 B。

#### S4U2self

非约束委派只能用于全程使用 Kerberos 协议的场景，这就意味着用户必须通过 Kerberos 协议登录 Web 服务器。但事实上许多情况下并非如此，约束委派同样弥补了这一缺陷：

1. 1. 用户访问服务 A，通过 HTTP 协议发起认证并通过。
2. 2. 服务 A 通过 `TGS Exchange(S4U2self)` 携带自身的 TGT 请求 KDC。
3. 3. KDC 检查服务 A，发现其 `userAccountControl` 设置了 `TRUSTED_TO_AUTH_FOR_DELEGATION` Flag，返回一张可转发的、从用户到服务 A 的 ST。
4. 4. 如果 KDC 发现服务 A 的 `userAccountControl` 属性未设置 `TRUSTED_TO_AUTH_FOR_DELEGATION` Flag，返回一张不可转发的、从用户到服务 A 的 ST。
5. 5. 后续同上 5-8。

在 S4U2self 过程中，用户的身份通过 `PA-FOR-USER`（或 `PA-S4U-X509-USER`）类型的 `PA-DATA` 表示，`PA-FOR-USER` 中包含用户名、作用域、校验码和认证协议：

```
PA-FOR-USER ::= SEQUENCE {
   -- PA TYPE 129
   userName [0] PrincipalName,
   userRealm [1] Realm,
   cksum [2] Checksum,
   auth-package [3] KerberosString
}
```

最终，服务 A 使用 S4U2self 帮助用户获得了一张从用户到服务 A 自己的、可转发的 ST，取代了原本用户通过 Kerberos 协议申请该 ST 的过程。

但问题是，服务 A 在 TGS Exchange(S4U2self) 阶段并没有发送任何有关于用户 A 的凭证，KDC 也不会对用户的身份进行认证。身份认证是 AS Exchange 阶段应该做的事，这里已经被 HTTP 协议取代。这也就意味着，**服务 A 可以通过 S4U2self 协议模拟任意用户，获取从任意用户到服务 B 的 ST。**只要服务 A 具有 SPN，就能使用 S4U2self 协议，而无需设置 `TRUSTED_TO_AUTH_FOR_DELEGATION` Flag。

#### 配置

域管理员权限执行：打开服务账户的属性菜单，点击委派选项卡，勾选"仅信任此计算机来委派指定的服务"，可以选择"仅使用 Kerberos"或"使用任何身份验证协议"子选项，区别在于能否使用 S4U2self 进行协议转换，最后在下方添加被允许委派到的服务。

配置完成后，查看该服务账户的 `msDS-AllowedToDelegateTo` 属性，该属性包含了 S4U2proxy 允许委派至的服务。若同时该服务账户的 `userAccountControl` 属性存在 `TRUSTED_TO_AUTH_FOR_DELEGATION` 标志位，说明选择了"使用任何身份验证协议" 子选项，即允许 S4U2proxy 协议转换。否则则为"仅使用 Kerberos"子选项，此时虽仍然可以通过 S4U2self 模拟任意用户到服务 A 的 ST，但该 ST 不可转发，也就无法用于后续的 S4U2proxy，即阻止了协议转换。**事实上，在仅有服务 A 配置了约束委派的情况下，此时确实无法 S4U2proxy。但若服务 B 同时配置了 RBCD，此时仍然可以 S4U2proxy。**

```
AdFind.exe -h 192.168.159.112 -u island.com\zhangsan -up ZS@123qwe -b "DC=island,DC=com" -f "(msDS-AllowedToDelegateTo=*)" msDS-AllowedToDelegateTo userAccountControl
AdFind.exe -h 192.168.159.112 -u island.com\zhangsan -up ZS@123qwe -b "DC=island,DC=com" -f "(&(msDS-AllowedToDelegateTo=*)(userAccountControl:1.2.840.113556.1.4.803:=16777216))" msDS-AllowedToDelegateTo userAccountControl
AdFind.exe -h 192.168.159.112 -u island.com\zhangsan -up ZS@123qwe -b "DC=island,DC=com" -f "(&(msDS-AllowedToDelegateTo=*)(!userAccountControl:1.2.840.113556.1.4.803:=16777216))" msDS-AllowedToDelegateTo userAccountControl
```

###

### 1.3 基于资源的约束委派

基于资源的约束委（Resource-Based Constrained Delegation，RBCD）的出现并不是为了弥补约束委派的任意用户伪造问题，而是为了解决约束委派不能跨越域或林等信任边界的问题，同时也能够更加便利的管理委派。原先配置非约束委派和约束委派，必须拥有 `SeEnableDelegation` 特权，通常只有域管理员拥有，而配置 RBCD 只需资源所有者的权限即可。因此，为了使用户、资源有更多的独立性，Windows 2012 中引入了基于资源的约束委派。

RBCD 不再是通过域管理员配置服务 A 的属性来实现服务 A 能委派至哪些服务，而是由服务 B 的管理员自己来配置服务 B 的属性来实现哪些服务能委派至服务 B。换句话说，约束委派限制了服务 A 到其他服务的传出信任，RBCD 则限制了其他服务的到服务 B 的传入信任。

RBCD 与约束委派在通信架构上大致相同，也是服务 A 通过 S4U2proxy 请求从用户到服务 B 的 ST。但在 S4U2proxy 请求时，他们携带的从用户到服务 A 的 ST 并不相同，约束委派需要可转发的 ST，RBCD 则不用：

1. 1. 用户访问服务 A，使用 Kerberos 协议发起认证。
2. 2. 用户通过 `AS Exchange` 请求并获得一张正常的 TGT。
3. 3. 用户通过 `TGS Exchange` 携带正常的的 TGT 请求 KDC。
4. 4. KDC 根据用户请求的 SPN，检查对应的服务 A，发现其 `userAccountControl` **未设置** `TRUSTED_TO_AUTH_FOR_DELEGATION` Flag，返回一张**普通的**、从用户到服务 A 的 ST。
5. 5. 用户通过 `AP Exchange` 将 ST 发送给服务 A。
6. 6. 服务 A 认证该用户能够合法访问自己，至此完成用户的认证。
7. 7. 服务 A 通过 `TGS Exchange(S4U2proxy)` 将自身的 TGT、普通的 ST 发送给 KDC
8. 8. KDC 检查服务 A 的 `msDS-AllowedToDelegateTo` 属性，发现没有该属性；或者有该属性，但服务 B 没有位于其中。则 KDC 继续检查。
9. 9. KDC 检查服务 B 的 `msDS-AllowedToActOnBehalfOfOtherIdentity` 属性，确定服务 A 位于其中，返回一张从用户到服务 B 的 ST。

需要注意的是，如果 KDC 检查服务 A 存在 `msDS-AllowedToDelegateTo` 属性，且服务 B 位于其中，则会进入约束委派流程。但此时收到的 ST 却是不可转发的，KDC 将不再检查 `msDS-AllowedToActOnBehalfOfOtherIdentity` 属性，而是直接返回失败。只有在服务 B 不位于服务 A 的 `msDS-AllowedToDelegateTo` 属性中时，才会继续检查 RBCD。

换句话说，如果没有配置服务 A 的约束委派，仅配置了服务 B 的基于资源约束委派，KDC 在检查 `ServicesAllowedToSendForwardedTicketsTo` 失败后，依然会检查 `ServicesAllowedToReceiveForwardedTicketsFrom`，只要后者检查通过，就会返回一张从用户到服务 B 的 ST。也就是说配置 RBCD 无需事先配置约束委派，这是合理的，这样才着实达到了配置更简单、操作更独立的目的。

#### 配置

服务 B 管理员权限使用 Powershell Cmdlet 进行配置：

```
import-module ./Microsoft.ActiveDirectory.Management.dll
Set-ADComputer -Identity ServerB -PrincipalsAllowedToDelegateToAccount ServerA
Get-ADComputer -Identity ServerA -Properties PrincipalsAllowedToDelegateToAccount
Set-ADComputer -Identity ServerB -PrincipalsAllowedToDelegateToAccount $null
```

配置完成后，查看该服务账户的 `msDS-AllowedToActOnBehalfOfOtherIdentity` 属性，该属性包含了哪些服务允许委派至自身。

```
AdFind.exe -h 192.168.159.112 -u island.com\zhangsan -up ZS@123qwe -b "DC=island,DC=com" -f "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)" msDS-AllowedToActOnBehalfOfOtherIdentity userAccountControl
```

###

### 1.4 委派发展小结

最初，微软通过转发用户 TGT 实现非约束委派，让服务 A 拿着这张 TGT 去申请从用户到服务 B 的 ST，但是这无法阻止服务 A 去申请其他服务的 ST。要解决这个问题，一个直观的想法是在用户 TGT 中添加一个字段来约束该 TGT 仅能被拿去申请指定服务的 ST，但是对于用户来说他并不确切的知道 Web 服务需要访问的后端服务，也就无法很好的在 TGT 中限定服务。既然无法在用户侧限定能申请的服务，那就尝试在服务侧限定，于是出现了约束委派。

约束委派不再是通过转发 TGT 实现委派，而是通过 S4U2self、S4U2proxy 两个 Kerberos 扩展协议进行委派，事先在服务账户上配置该服务能通过委派去访问哪些限定的服务。之后，服务就可以通过 S4U2self 申请从用户到服务自己的、可转发的 ST，再通过 S4U2proxy 拿着自己的 TGT 和可转发的 ST 去申请从用户到特定服务的 ST。但是这两个子协议都作用于 TGS Exchange 阶段，全程也只需要服务自己的 TGT，因此对于 KDC 来说并不能认证用户身份，这意味着服务可以模拟任何用户获得到特定服务的 ST。

基于资源的约束委派并不是为了弥补用户伪造的问题出...