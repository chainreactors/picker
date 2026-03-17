---
title: GoLinHound：用 Go 把 Linux 和 SSH 的攻击路径画出来
url: https://mp.weixin.qq.com/s/uTAFatbQjyOWVNg5Z3r4gQ
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:13:23.728477
---

# GoLinHound：用 Go 把 Linux 和 SSH 的攻击路径画出来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdc7ibKVibV1MCjrHFTItcVH2u2VB6lAqDibTxssmSOdQpB5vFD9Ko7pPEsnQicickd6Y0FpQgicbZWndVHjVa9RgR1cj7nb94bI8Xibw/0?wx_fmt=jpeg)

# GoLinHound：用 Go 把 Linux 和 SSH 的攻击路径画出来

原创

工具党
工具党

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 文章介绍了一个基于 Go 语言开发的 Linux/SSH 环境数据采集工具 GoLinHound，它能像血猎犬（BloodHound）分析 Windows AD 环境一样，发现 Linux 系统的攻击路径，并将结果整合进 BloodHound 的 OpenGraph 模型中。

## 01 工具概述

搞红队攻防或者内部安全审计的，肯定熟悉 BloodHound。这东西查 Windows 域的攻击路径简直神器。

但 Linux 环境呢？服务器、跳板机、开发机，满地的 SSH 密钥、sudo 权限、缓存票据，凭感觉摸太费劲。现在，有个工具把 BloodHound 的思路搬到了 Linux 世界，它就是 GoLinHound。

简单说，GoLinHound 就是一个用 Go 写的采集器。它扫描 Linux 和 SSH 环境，把找到的关系——比如谁有谁的私钥、谁能在哪台机器上 sudo 成 root——都变成一种叫 OpenGraph 的 JSON 数据。这样一来，你就能直接把结果扔进 BloodHound CE 或者 Enterprise 里，用熟悉的界面和强大的 Cypher 查询，把 Linux 内网的横向移动、权限提升路径看得清清楚楚。

更妙的是，它能和你用 SharpHound（采集 AD 的）或者 AzureHound（采集 Azure 的）得到的数据合并。这意味着一张大图里，既有 Windows 域的路径，也有 Linux 主机的路径，甚至还能看到它们之间是怎么连起来的。

项目地址：RantaSec/golinhound (https://github.com/RantaSec/golinhound)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcCuKZngSYtI5B2hicNljicww3fsB5ILEib19LY3PzFgjRLD8dT2x1kdyic7AGz8gLSsZMpAx84xUTRVSuDT2DGqMicxJEP67ujzdiaI/640?wx_fmt=png&from=appmsg)

## 02 核心功能与数据模型

GoLinHound 到底采集些什么？它建立了一套针对 Linux 和 SSH 的数据模型，定义了各种类型的“节点”（Node）和“关系”（Edge）。理解这些，你才知道它到底在查什么漏洞。

### SSH 相关的关系

核心就围绕 SSH 密钥和授权。

* **HasPrivateKey：**

  用户拥有某个 SSH 密钥对。它会扫所有用户的 `$HOME/.ssh/` 目录找私钥。
* **CanSSH：**

  某个 SSH 密钥对能用来以特定用户身份登录某台 SSH 计算机。这通过解析 `authorized_keys` 文件获得。
* **ForwardsKey：**

  密钥对被通过 SSH 代理转发到了另一台计算机。利用这个特性可以进行横向移动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcyZvZNsjTcdK7Axla9V4oPm1Y8UpJaLqj4VRFV0hLJbiau3aZJeOrXdF40iaHKy0MPxGmAhEJ7B2icNWZSfcvdXdRX06h5nYXTts/640?wx_fmt=png&from=appmsg)

### Linux 本地权限关系

重点关注谁在机器上有什么权限。

* **IsRoot：**

  用户就是这台机器的 root。不用解释了，最高权限。
* **CanSudo：**

  用户能通过 sudo 执行 root 命令。来自对 `sudoers` 配置文件的解析。
* **CanImpersonate：**

  (root) 用户可以“扮演”系统上的任何其他用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdUZ523B5AJukQBdMC0oZRB1HwZMicLgAryORG2quS9RP61LQ13fialtEPSNbrYiamDjw1oia74vCZVLzyRUfiakXPxHMVvNjPibCDXQ/640?wx_fmt=png&from=appmsg)

### 与云（Azure）的关联

这是让跨环境攻击路径可视化的关键。

* **SameMachine：**

  一个 SSHComputer 节点同时也是一个 AZVM（Azure 虚拟机）节点。建立了本地主机和云上虚拟机身份的关联。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibetRmKMJP7cibiagbXDhu1BNdDeNx2J4IMqpwLoAHFXgAkhWv5q7bY9BJy9t7wcYo7gztahOApAHO8xpJWSibqGRI4mgCebXqZCico/640?wx_fmt=png&from=appmsg)

### 与活动目录（AD）的关联

打通 Linux 和 Windows 域的最后一块拼图。

* **HasKeytab：**

  主机上存有某个 AD 用户的 keytab 文件（包含 Kerberos 密钥）。
* **HasTGT：**

  主机上缓存了某个 AD 用户的票证授予票证（TGT），通常在 `/tmp/krb5cc_*` 这类文件里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeANWwYhUzxuWbKUXm0EyMWDInJIJULElXw5uzO7mdsftVciaReygPE27FAgFFPhrkFIUTvd7xRdpjhaBIcWylic25HsxoFyWbVc/640?wx_fmt=png&from=appmsg)

## 03 安装与快速上手

工具提供了多种部署方式，从单机测试到大规模自动化采集都可以。

```
# （可选）添加自定义节点图标到 BloodHoundBASEURL="http://localhost:8080"  # 你的BloodHound地址TOKEN=""  # 你的API Tokencurl -X "POST" \  "${BASEURL}/api/v2/custom-nodes" \  -H "accept: application/json" \  -H "Prefer: wait=30" \  -H "Content-Type: application/json" \  -H "Authorization: Bearer ${TOKEN}" \  -d @res/custom-nodes.json# 自己编译make build# 或者，直接下载最新发布版本wget -P "bin/" "https://github.com/RantaSec/golinhound/releases/latest/download/golinhound-linux-amd64"wget -P "bin/" "https://github.com/RantaSec/golinhound/releases/latest/download/golinhound-linux-arm64"# 执行采集 (需要root权限读所有文件)sudo ./bin/golinhound-linux-amd64 collect > output.json# 可选：合并多个输出文件cat *.json | ./bin/golinhound-linux-amd64 merge > merged.json
```

采集完成后得到的 `output.json` 文件，就可以在BloodHound的界面里通过“上传数据”功能导入了。

## 04 实战演示：看几个关键查询

数据导进去，光看节点连线没用，关键是要会提问。GoLinHound 文档里给出了不少现成的 Cypher 查询例子，我们就看几个最有代表性的。

**查找本地提权路径**

这个查询找的是：一个普通用户，如何利用一台机器上的关系，最终变成能在这台或另一台机器上 sudo 或本身就是 root 的用户。

```
MATCH pEnd=(admin:SSHUser)-[:CanSudo|IsRoot]->(c:SSHComputer)MATCH (c)-[:CanImpersonate]->(user:SSHUser)WHERE NOT (user)-[:CanSudo|IsRoot]->(c)MATCH pStart=allShortestPaths((user)-[*1..]->(admin))WHERE none(n in nodes(pStart) WHERE n.objectid=c.objectid)RETURN pStart, pEnd
```

**从开发环境穿透到生产环境**

假设主机名里带“TEST”、“DEV”的是测试机，带“PROD”的是生产机，这个查询能找出从测试机通往生产机用户的攻击链。

```
MATCH (testc:SSHComputer)WHERE (    testc.name CONTAINS "TEST" OR    testc.name CONTAINS "TST" OR    testc.name CONTAINS "DEV")MATCH (prodc:SSHComputer)-[:CanImpersonate]->(produ:SSHUser)WHERE (    prodc.name CONTAINS "PROD" OR prodc.name contains "PRD")MATCH p=allShortestPaths((testc)-[*..]->(produ))WHERE none(n in nodes(p) WHERE n.objectid=prodc.objectid)OPTIONAL MATCH p2=(produ)-[:CanSudo|IsRoot]->(prodc)RETURN p,p2
```

**找出存在多处的高危私钥**

一把私钥出现在多台主机上是非常危险的。这个查询能帮你识别这种“万能钥匙”。

```
MATCH (c:SSHComputer)-[:CanImpersonate]->(u:SSHUser)-[:HasPrivateKey]->(k:SSHKeyPair)WITH k, collect(DISTINCT c) AS computersWHERE size(computers) > 1UNWIND computers AS cMATCH p=(c)-[:CanImpersonate]->()-[:HasPrivateKey]->(k)RETURN p
```

## 05 优缺点分析与适用场景

说实话，看到这个工具的第一感觉是“终于有人系统地干这件事了”。但它也不是万能的。

**优点很明显：**

* **思路很好：**

  把BloodHound的成熟模式套用到Linux，解决了Linux内网路径可视化的痛点。
* **整合性强：**

  输出标准OpenGraph格式，能和现有的AD、Azure数据无缝融合，实现跨平台攻击面分析。
* **开箱即用：**

  提供了预编译二进制、源码、部署脚本（如Velociraptor Artifact），方便集成到现有自动化流程。
* **查询实用：**

  自带的Cypher查询例子直接瞄准常见的特权提升、横向移动场景，很有启发性。

**局限和需要注意的地方：**

* **需要高权限：**

  采集（`collect`）时必须具有root权限，才能读取所有用户的文件（如`.ssh`目录、`/tmp`下的票据）。这在某些审计场景下可能受限。
* **覆盖度依赖解析器：**

  它的发现能力依赖于对特定文件（`authorized_keys`， `sudoers`， Kerberos缓存文件等）的解析。如果配置以其他非标准形式存在，可能会遗漏。
* **静态快照：**

  和所有此类工具一样，它采集的是某一时刻的快照，无法实时反映变化。

> GoLinHound 更适合在一个你已获得一定访问权限（比如一个初始立足点）的环境中进行深度侦查，或者在内部安全评估中作为资产梳理和攻击面暴露检查的工具。它帮你把散落在各处的配置隐患，变成一张可查询、可推理的攻击地图。

## 写在最后

GoLinHound 项目还很新，2026年刚发布。但它的方向和首批实现的功能已经足够有吸引力。对于专注于内网安全、云安全或者红队评估的安全人员来说，这绝对是一个值得放进工具链的新玩具。

它的出现也反映出一种趋势：攻击面的管理正越来越强调“关联性”。单一系统、单一域的安全分析不够了，得把Windows、Linux、云环境串起来看。GoLinHound 正好补上了Linux这块重要的拼图。接下来，就是看社区怎么用它，以及作者会如何迭代了。试试看，说不定能在你的环境里发现意想不到的攻击路径。

**获取方式：私信回复"golinhound"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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