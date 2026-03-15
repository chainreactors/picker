---
title: 工作组和域
url: https://mp.weixin.qq.com/s/aUn-26IBZ-UhtGI-B93vfA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:26:38.660433
---

# 工作组和域

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mS3YhqKWBR3Tql23uTMcDAfvSxUic4FI0txRgBchzFoGK7hK0mdJNlkghIwSjyWZMoQp8mQavia2R8hWp0LAwsFicVEnR8pp6vWA8duBWia8kLc/0?wx_fmt=jpeg)

# 工作组和域

原创

Heihu577
Heihu577

Heihu Share

![]()

在小说阅读器中沉浸阅读

# 工作组和域

* 工作组

+ 简介
+ 工作组实操案例
+ 工作组优缺点

* 域

+ 概念
+ 实操案例
+ AD

* 权限相关

+ 本地工作组
+ 域
+ 机器用户和SYSTEM区别

* Ending...

在介绍工作组和域之前, 我们需要了解内网的概念: 内网也指局域网，是指在某一区域内由多台计算机互连而成的计算机组，组网范围通常在数千米以内。在局域网中，可以实现文件管理、应用软件共享、打印机共享、工作组内的日程安排、电子邮件和传真通信服务等。内网是封闭的，可以由办公室内的两台计算机组成，也可以由一个公司内的大量计算机组成。

## 工作组

### 简介

在一个大型单位里,可能有成百上千台计算机互相连接组成局域网,它们都会列在"网络"(网上邻居)内。如果不对这些计算机进行分组,网络的混乱程度是可想而知的 为了解决这一问题,产生了工作组( Work Group)这个概念。将不同的计算机按功能(或部门)分别列入不同的工作组,例如技术部的计算机都列入"技术部"工作组、行政部的计算机都 列入"行政部"工作组。要想访问某个部门的资源,只要在"网络"里双击该部门的工作组名 就可以看到该部门的所有计算机了。相比不分组的情况,这样的情况有序得多(尤其对大型局域 网来说)。一个典型的工作组如图:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR2RzUbBzjibCJzD6V5BHoARB6V7eyS8Lzdu69c8EwujrhYTibsYYqZCvhHUhpGW9Nkic4hpIz5OAlSXHYNdY10g5l3SbDByavgbKU/640?wx_fmt=png&from=appmsg)

说白了工作组组就是将计算机进行分组的操作, 例如: 销售组, 金融组. 这些组中存在不同的计算机.

### 工作组实操案例

#### Server 2016

一台电脑默认的工作组为: WORKGROUP, 如图:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR16WNLaYkZp1Qkf6HScO4fHKIHJ1p8iciazBnHESma9xxMQCWwic5KdR3nSppHe2M8IkHf2d9cSz8RSQbrZhsQ0ArfhYr22Meicjia8/640?wx_fmt=png&from=appmsg)

想要更改也比较容易, 直接更改即可:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR1BkNxAYhXYC5xmr4Onq5QurGEAFw6ogAYfKkhuEAONeXiaT3YuNVS5zHWRUJo2ebTVLvtrsgt9jbbB5tMUoKLYlXk0aR2UAZPI/640?wx_fmt=png&from=appmsg)

创建工作组: 如果输入的工作组的名称在网络中不存在,就相当于新建了一个工作组(当然,暂时只有当前这台计算机在该工作组内)。单击"确定"按钮,Windows会提示需要重新启动。在重新启动之后进入"网络",就可以看到所加入的工作组的成员了。当然,也可以退出工作组(只要修改工作组的名称即可)

#### Server 2003

同时, 我们也将另外一台 Server 2003 加入到工作组:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR10CVQqPuthvGltOucMDRuTKlbfib4IgNibdb9FqgnFoRia98uMEYDUC6DriaG0ySA3niaA4CQhq3X5cXmwECbwRaqWo3yibQeF0Jevw/640?wx_fmt=png&from=appmsg)

而现在 IT 组内应该存在两台机器, 分别为: ZS-PC 以及 LS-PC.

#### Win7

随后我们在一台`WORKGROUP`组内成员使用`net view /domain`命令来查看计算机中的所有组:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR28cYLaleAqvrNKxAaBf7HvWUmfFuewTke0VviaGzdicoIR4HItpXSNnExORicOJMztx0vv5hXrGfL5dVP1XdnCst3BrPB0VIItMU/640?wx_fmt=png&from=appmsg)

当然, 如果想要退出 IT 组也特别容易, 直接修改组名为 WORKGROUP 即可. 不过在网上别人照样可以访问你的共享资源。你也可以随便加入同一网络上的任何其它工作组。“工作组”就像一个可以自由进入和退出的“社团”，方便同一组的计算机互相访问。

### 工作组优缺点

优点：

1、方便管理和维护

2、资源分配方便和灵活

缺点：

1、缺乏集中管理与控制的机制

2、没有集中的统一帐户管理

3、只适合小规模用户的使用

在工作组中, 每台计算机的地位是平等的.

## 域

域(Domain) 是一个有安全边界的计算机集合 (安全边界的意思是,在两个域中,一个域中的用户无法访问另一个域中的资源) 可以简单地把域理解成升级版的工作组。与工作组相比,域的安全管理控制机制更加严格。用户要想访问域内的资源,必须以合法的身份登录域,而用户对域内的资源拥有什么样的权限,还取决于用户在域内的身份。

### 概念

#### 单域和多域

一个单域场景:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR3d7mDqqCJWT4Rb985BmfibQ6ibibkHs9H2MmetmVtmZiaY2Zu3IuFN0jGJt4CNgSkHJfIUxAPblA0CKGMwyw0jfB5dxCIMFkJG9rU/640?wx_fmt=png&from=appmsg)

在这张图中, DC 可以管理其他计算机, 并且能够给其他计算机分配策略. 不像工作组那样人人平等, 域中的 DC 相当于一个计算机管理员.

> 在真实的渗透测试环境中, 通常我们会盯着 DC 做一些事情, 俗话说擒贼先擒王. 当我们拿下 DC 之后, DC 下的其他主机也统统被拿下.

通常企业还存在备份 DC, 当 DC 出现问题时企业可以启用备份 DC 进行管理.

---

而多域则是: 由于计算机数量过多, 企业无法通过一个域来进行完整管理, 例如北京区域使用了一个域, 而上海区域使用了另一个域, 这就是多域场景. 可以使用下图进行表示:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR0mpDejPbbEj6YfvHfTt5zrlgOh5oepfFicbvGXBnszDvnbNtrtZRe1fZYaIsrMLvg9XbO6iayUugauWf11yeXyic6Fu3ZlichR48A/640?wx_fmt=png&from=appmsg)

这就是一个多域的场景, 当然也可以通过部门来划分域, 比如: 销售部, 财务部 等, 这些都需要根据企业的现状来进行划分.

而这些域之间能够进行跨域访问吗？例如 A01.com 想要访问 A03.com, 这就涉及到域的信任关系了. 后续会进行介绍.

#### 父域和子域

类似于这张图:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR1LMTgibTs9e8PtC38CJcD5rOJ6libmghtT1xw0FYzjBlQT9WOql6rmbk4J5UMR8KsQpKM6KmyPpgOBOVYPrEvdxvaibWZJbjWXe0/640?wx_fmt=png&from=appmsg)

其中 A01.com 为父域, a.A01.com & b.A01.com 为子域.

#### 域树和域森林

域树(Tree)是多个域通过建立信任关系组成的集合。一个域管理员只能管理本域,不能访问或者管理其他域。如果两个域之间需要互相访问,则需要建立信任关系,信任关系是连接不同域的桥梁。

域树内的父域与子域,不但可以按照需要互相管理、还可以跨网络分配文件和打印机等设备及资源,从而在不同的域之间实现网络资源的共享与管理、通信及数据传输。一个域树可以使用下方示例进行表示:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR3KTxfYKbPE5gp7z4dw1dOOCriczLBYzuBYR32qktbWqoLcXocuww0tXd94DjzQRLiclhmGtz1VH7VOTicE592Na6LibJ0IV3q2mfU/640?wx_fmt=png&from=appmsg)

---

域森林(Forest)是指多个域树通过建立信任关系组成的集合。而域森林可以使用下示例进行表示:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR3bUOQ06Xic9u1lOtQntoiaGicCvBFUbczauLEgPCAxbA4OibtBY2YUqXxrLic1Wg6Nia8OYtARt1Nvvtwqk2I4iaEt5JchSqibsMw62Zw/640?wx_fmt=png&from=appmsg)

其中 A01.com 需要建立信任关系访问 A01.net。

### 实操案例

在这里需要准备 Windows Server 20xx 版本的机器, 对于版本号可任意.

#### 域环境搭建

##### DC & DNS 搭建

当前这台机器的测试密码为: Qazwsxedc123!, 并且执行如下命令:

```
net user Administrator /passwordreq:yes
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR0A7YKOd6YibvBy0tmoT2v0xFdLvFjlQ8hskiaukhpDWTlnxr4sHYeagQaVxR0E0HAXr8Hjib9JTiaDY5ZqNh0YKGrdkvpdeH6qwnc/640?wx_fmt=png&from=appmsg)
> 上方图中需要记录下`网关 IP`, 在后续的配置中会使用到.

看到 VMWare 的虚拟网络编辑中, C 段为: 192.168.174.xxx, 因此我们的 DC 需要设置一个固定的 IP 地址中该网段下:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR3IVO9xlwnhpz6kk6HQw2wDlVoQjAAtrso6OflFsTrJxuicRGTIV4GiagpkgmicgEqddicCdO2lYzCV8xBuZcP11bBnH1hicuB3Ulhg/640?wx_fmt=png&from=appmsg)

当 IP 地址配置成功后, 修改计算机名称为 DC:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR3JfCe7JPibWO9cJXdaKCicuibYb2l6sWnVkxYY9OTgN10eQhwjsF3dmJiceKYc8C1bjHAYxcBK7gkBBEEE2XYicDAQ7tdM2kMdcr24/640?wx_fmt=png&from=appmsg)

随后重启计算机之后, 在 Windows Server 中可以进行添加角色或功能:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR0BVIw9qaBz2vLwBd5bPoY2kPMP2JrPZxrTe24t740HejWAu540DFUtvxqzZkRuxDYI4rq9qLdTQDxtCvMjfAXneTWRian1IXwY/640?wx_fmt=png&from=appmsg)

随后稍作等待即可安装成功, 随后将该服务器升级成域控制器:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR0fb7FxRRnZN7EaEyuOSibzOPYeTUEWVh42eQI5d108Mo8ibNI2OicZWDp7eOBuSL5Ga0XwKw6aj0dGxjBhroiaryia6coth2VXGXNc/640?wx_fmt=png&from=appmsg)

##### 域内主机搭建【加入域】

接下来我们将一台 Windows Server 2008 R2 的机器加入到域内, 首先是 DNS 配置:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR0B6zNHhD5txruiaXnqwiaHEHeVBjAUtAicZHS0hQHhiaoRREGr7hMtNDmiaNvSic72slPeVT8iawicdmg2CovZfrCsrAiccPvExt3fJPD4/640?wx_fmt=png&from=appmsg)

后续注意改一下计算机名称, 随后 ping 一下域控, 看一下是否能够 ping 通:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR1cAhQWwnKf9v3BRO8UH4mCMsic3tLmVNtAw3ZvshfcdGzMdMcHgUQOxWLYHK1WeLHrbxQMBmKia9abUGEpgWfBr5kbEYPwDLibdY/640?wx_fmt=png&from=appmsg)

随后我们在 DC 中新增一个域用户:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR07TibXVn0ojYsnynwvnCEhOpibJaCqo8icxTAtiaTibQBiaLvVBe8tKAfRAn1kEvwH7XRwo2VDNoOACd5rb7pdLCRFLSbC0g6HJy5Y0/640?wx_fmt=png&from=appmsg)

随后在 Server 2008 中进行配置域即可:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR1EqUQsibu3g7gZBou1eMGDPjr1jhpGuYXUVQVQwSesDcBGibJFTVV2Zh81zaiaGCSibmgBjtWzNbrickmGzBIJvOKgu80Qdh1n2dmk/640?wx_fmt=png&from=appmsg)

随后登录时可以选择登录本地用户还是域用户:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR1XLGfuRKVcOonsLIFgndiaWnmZrtXwFt7eq2SpwfMwokibakvM9hTf68OCIad7Pjp3Z4r2Ih6ibRrNlyhMCl3vBZI21OZdup7zA4/640?wx_fmt=png&from=appmsg)

对于其他主机也是这个设置, 修改 `DNS+计算机名【非必须】+隶属于`即可.

### AD

#### 概念

活动目录(Active Directory,AD)是指域环境中提供目录服务的组件，目录用于存储有关网络对象(例如用户、组、计算机、共享资源、打印机和联系人等)的信息。目录服务是指帮助用户快速、准确地从目录中找到其所需要的信息的服务。活动目录实现了 目录服务,为企业提供了网络环境的集中式管理机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mS3YhqKWBR1FiceHSNvoLfPObT895umW80ZqGGCibOtrzdH8G9ITzLGF0598WUzb29Pw4JfzMZ6b7icjgRNciboVsI9BLsyNmmODvBicgl4NLeNQ/640?wx_fmt=png&from=appmsg)

在上述, 我们可以看到 heihu577.com 下有很多文件夹, 这些文件夹可以被称之为“组织单元”, 其含义如下:

```
1. Builtin（内置）
    - AD 的内置容器，保存系统预定义的本地组（如 Administrators、Users 等域内置安全组）。
    - 主要用于权限分配和向后兼容，通常不建议随意修改其默认结构。
2. Computers（计算机）
    - 默认容器，用来存放新加入域的计算机账户对象（如果没有通过策略/脚本重定向）。
    - 常见对象是工作站、成员服务器的计算机账号。
3. Domain Controllers（域控制器）
    - 默认 OU（不是普通容器），用于存放域控制器计算机对象。
    - 会关联专门的 GPO（如 Default Domain Controllers Policy），用于域控安全基线与策略管理。
4. ForeignSecurityPrincipals（外部安全主体）
    - 保存来自其他域/林的安全主体占位对象（如外部用户、组的 SID 映射对象）。
    - 当跨域赋权时会自动创建，便于在当前域 ACL 中引用外部对象。
5. Managed Service Accounts（托管服务账户）
    - 存放 MSA/gMSA（托管服务账户）对象。
    - 用于让服务使用自动管理密码的账号运行，减少人工维护和密码泄露风险。
6. Users（用户）
    - 默认容器，存放新建用户（默认路径下）和一些内置用户/组对象（如 Administrator、Guest、Domain Users 等）。
    - 生产环境里常建议按部门/用途使用自定义 OU，而不是长期直接用默认 Users 容器。
```

其中, 我们搭建的域内主机可以在 DC 上进行管理:

![](https://mmbiz.qpic.cn/mmbiz_png/mS3YhqKWBR0TyKeRficCzukChY4TtcfTcz6fIJ6HCcf2VibXF2pf2H94h9xwrztArhTN7ULmrrjwny3G2dibjV4NTicAjuxk0fePXNPlTpyalgw/640?wx_fmt=png&from=appmsg)

#### 组织单元

组织单元（OU）是域中包含的一类目录对象如用户、计算机和组、文件与打印机等资源，是一个容器，可...