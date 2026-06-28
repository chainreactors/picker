---
title: 无线渗透测试：PMKID攻击详解
url: https://mp.weixin.qq.com/s/nPCX01M-bw2HyoIaorJYcA
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:12:47.964737
---

# 无线渗透测试：PMKID攻击详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OHEQvlQxUkpLjg73LH0NoOfbIyYicTm2bkrXa699GNiaJnS1Ur2mMSfOysCW8tjqdHnt9qUibkmib0czJqkib7nWUhRYhMicYZ38Cqs/0?wx_fmt=jpeg)

# 无线渗透测试：PMKID攻击详解

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MKR5uVA8JarEwEqp3DUoqlmnXajicJjGicUVicHt7kibGzapRt0L27WUFVNkGoEKLiaC6NQkjVw9NHpp4qib2OpVbufTOokXcPTS0h4/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618185&idx=1&sn=e7a4ddec94c9af10451bca515c67e228&scene=21#wechat_redirect)

> **导语**：传统WPA2握手捕获方法必须等待客户端断开再重新认证才能获取握手包，而PMKID攻击绕过了这一步骤，直接向AP请求PMKID帧，让攻击者可以独立完成破解，无需借助任何合法客户端。配合hashcat的暴力破解，整个过程效率大幅提升。

---

## 一、开放系统认证

开放系统认证（Open System Authentication，简称OSA）是WEP（有线等效加密）协议中的一种认证流程，允许计算机通过无线调制解调器访问任何WEP网络并接收未加密文件。

**认证流程：**

* 客户端发现SSID，发送连接请求（请求帧）
* 接入点（AP）返回响应（响应帧）
* 客户端向AP发送关联或认证请求
* AP生成一个仅本次会话有效的认证码并发送给客户端

这种情况就像你把网线插到台式机，就能直接连接网络一样，这就是WEP被称为"有线等效协议"的原因。但这个机制存在明显缺陷：认证码可被解密、静态IV（初始向量）加密方式脆弱、加密强度不足等。因此WEP协议后来被共享密钥认证所增强。

![开放系统认证](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NIwLhRLaovrmCq08VG0Zs5ia1mMH8ooV5oG58eicsRgwsZMEBsP1w6Z0UyrFVbQbQFVLriboIiaTXPibbQ9KoB6SYPYIiacg7b9CDKM/640?wx_fmt=png "开放系统认证")

## 二、共享密钥认证

共享密钥认证是WEP中的一种认证方法，要求客户端和服务端事先共享同一个密钥——也就是Wi-Fi密码。

**认证流程：**

* 客户端发现SSID，发送连接请求
* AP向客户端发送一个只能用密钥（Wi-Fi密码）解密的加密文件
* 客户端输入密码后向AP发送认证请求帧
* AP验证解密后的文件，确认客户端拥有正确密钥后授予访问权限

加州大学伯克利分校的研究证明，由于WEP使用静态密钥进行加密，该协议十分脆弱，这推动了WPA和WPA2的出现。

![共享密钥认证](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MzFwK2tn5oZx60Ia8CiazcFZ7ymTIosp6ibicicHewLa9kIhHTkQZmENjvrRToZL1yU7YuxdyTumJRgbGoDuYfroYrM5Mc3ic7CbL8/640?wx_fmt=png "共享密钥认证")

## 三、WPA 与 WPA2（PSK）

**前置说明**：本文仅讨论WPA2中的PSK（预共享密钥）认证，以及单播模式（AP到客户端的一对一通信）。

Wi-Fi保护访问（WPA）于2004年推出，可在WEP的相同硬件上运行。与WEP不同，WPA使用TKIP（临时密钥完整性协议）为每个数据包动态生成新密钥。WPA2则增加了对基于AES的CCMP协议的强制支持。我们重点讨论WPA/WPA2中的认证机制。

每个使用WPA/WPA2 PSK方式登录无线网络的用户都已经知道预共享密钥（PSK）。PSK大小为256位，生成方式如下：

**PSK = PBKDF2\_SHA1（Wi-Fi密码 + Wi-Fi SSID，SSID长度，SHA1迭代4096次）**

也就是说，如果你把Wi-Fi密码告诉朋友，他也就获得了你的PSK。请注意，PSK本身并不加密流量，流量的加密密钥实际上是从这个PSK派生出来的。

**在WPA2 PSK中，预共享密钥等同于成对主密钥（PMK）。**

PSK不直接加密每个数据包中的数据，而是从PSK派生加密密钥，并加入其他变量。加密客户端与接入点之间所有传输数据的密钥称为成对传输密钥（PTK）。

**PTK = PSK或PMK + Anonce + Snonce + MAC（认证器）+ MAC（请求者）**

* 认证器（Authenticator）= AP
* 请求者（Supplicant）= 客户端
* Anonce = AP为每个数据包生成的一次性随机数
* Snonce = 客户端为每个数据包生成的一次性随机数

对于广播和多播模式，原理基本相同，但生成的密钥略有不同，此时成对密钥变为GTK（组临时密钥）和GMK（组主密钥），PSK从主会话密钥（MSK）生成。

## 四、四次握手

简单来说，四次握手的核心是把某些源密钥材料转换成数据加密材料，然后用这些材料加密数据帧。这个从源密钥材料生成数据加密材料的过程，就叫做四次握手。

如前所述，客户端和认证器（AP）都知道PSK（也称PMK）。但PMK并不直接用于加密数据，必须从PMK派生出PTK。

**握手过程详解：**

**第一步——客户端PTK生成：** AP发送包含Anonce的消息，Anonce是每个数据包的一次性值。客户端收到Anonce后，使用所有输入（两个MAC地址、PMK、自己生成的Snonce以及收到的Anonce）创建自己的PTK。

**第二步——AP PTK生成：** 客户端向AP回发包含Snonce的消息，AP据此生成与客户端相同的PTK。这条消息的MIC字段设为1，用于验证消息是否损坏，或密钥是否因中间人攻击等原因被篡改。客户端同时发送RSN IE（或PMKID）。

**第三步——组密钥生成与分发：** PTK验证通过后，AP从GMK派生GTK（用于广播和多播通信）。GTK通过PTK加密后传递给客户端，消息通知客户端安装临时密钥，并在帧中附带一个RSN IE数据包。

**第四步——密钥安装确认：** 客户端向认证器确认密钥已安装。

**简化版四次握手：**

* AP向客户端发送Anonce，客户端生成PTK
* 客户端向AP发送Snonce，AP生成相同的PTK
* AP生成组密钥并加密发送给客户端
* 客户端安装密钥并回发确认

![四次握手](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M3FwS0icVlTib3wtlPAWicIjfqnZQNfXb35icrEoZBPmmf7TF3SooFleKa4iaDibNhJ2SRDZLrkD2CIX6P4hfNmXTwRMblNBTKaia3OA/640?wx_fmt=png "四次握手")

## 五、PMK缓存与PMKID

当客户端和AP成功完成四次握手后，双方会维护一种称为PMKSA（PMK安全关联）的状态。

AP漫游是指客户端（请求者）离开当前AP的覆盖范围，并连接到另一个AP的场景。与蜂窝网络的切换类似，每次客户端离开AP范围再重新连接，设备都需要重新执行完整的四次握手。

设想这样一个企业环境场景：办公区多个楼层都有AP，你拿着笔记本电脑跑到会议室做演示，突然发现连接断了——一秒钟的延迟就可能导致整个PPT演示失败。

为了解决这个切换延迟问题，我们引入了PMK缓存功能。

当AP完成四次握手后，会将PMKID缓存到称为PMKSA的信息集合中。当客户端断开再重新认证时，路由器不再执行完整的四次握手，而是直接向客户端请求PMKSA，验证通过后快速重新关联。

**PMKSA = PMKID + PMK生命周期 + MAC地址 + 其他变量**

PMKID是另一个哈希值的哈希，计算公式如下：

**PMKID = HMAC-SHA1-128（PMK，"PMK Name" + MAC（AP）+ MAC（请求者））**

HMAC-SHA1只是伪随机函数的一个示例。PMKID作为字段出现在RSN IE帧中，路由器会附带这个可选帧。"PMK Name"是与SSID关联的固定字符串标签。

路由器缓存PMKID后，下次客户端连接AP时，双方只需验证这个PMKID，从而完全跳过四次握手过程。PMKID缓存适用于支持漫游的各种IEEE 802.11网络，随着PMKID攻击日益猖獗，许多厂商也开始提供额外的RSN安全功能。

## 六、PMKID攻击原理

所有路由器都容易受到PMKID攻击吗？不是。**只有启用了漫游功能的路由器才存在这个漏洞。**

现在我们已经了解了足够多的背景知识，来看看攻击原理：如果能从AP获取PMKID，我们就能获得一个包含Wi-Fi密码的哈希值。PMKID攻击直接针对单个RSN IE帧。由于PMKID是从PMK、固定字符串和两个MAC地址派生而来，被Hashcat官方称为"理想攻击向量"。

暴力破解PMKID需要以下参数：

* Wi-Fi密码（口令）——猜测
* Wi-Fi SSID ——已知
* SSID长度 ——已知
* 认证器和请求者的MAC地址 ——已知
* PMK Name ——已知

实际上我们只需要： **获取PMKID → 用字典猜测Wi-Fi密码 → 生成PMK哈希 → 生成PMKID哈希并与捕获的PMKID比对**

根据Hashcat官方原文，PMKID攻击的主要优势包括：

* 不再需要合法用户参与——攻击者直接与AP通信（即"无客户端"攻击）
* 不再等待合法用户与AP之间的完整四次握手
* 不再遭遇EAPOL帧的重传（可能导致无法破解的结果）
* 不再因合法用户输入错误密码而失败
* 不再因客户端或AP离攻击者太远而丢失EAPOL帧
* 不再需要固定nonce和重放计数器值（破解速度略快）
* 不再需要特殊输出格式（pcap、hccapx等）——最终数据以普通十六进制字符串形式出现

## 七、使用hcxdumptool捕获PMKID

了解了PMKID的原理后，我们尝试获取PMKID并发起攻击。使用hcxdumptool向AP请求PMKID帧，并以pcapng格式保存。

**安装工具：**

```
apt install hcxtools
```

将Wi-Fi网卡设置为监听模式：

```
aircrack-ng start wlan0
```

使用hcxdumptool捕获周围所有路由器的PMKID：

```
hcxdumptool -o demo -i wlan0mon --enable_status 5
```

其中`demo`为输出文件名，`wlan0mon`为网卡接口，`--enable_status 5`表示仅显示认证和EAP/EAPOL帧。PMKID也可以通过状态值1捕获。

**EAP帧说明：** EAP（可扩展认证协议）用于WPA2-PSK路由器的认证。在四次握手中，加密密钥正在生成，而EAP负责客户端到AP的认证过程。

EAP流程如下：

* 客户端向AP请求新的无线网络连接
* AP向用户索取身份信息，并将收到的数据转发给认证服务器
* 认证服务器向AP请求并接收身份信息的合法性证明
* AP完成用户验证，向认证服务器回发验证消息
* 服务器授予访问权限，用户连接网络，随后进入四次握手流程

EAP共有40多种认证机制，但核心流程如上所述。

![使用hcxdumptool捕获PMKID](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M2d4BJIm4XtzeTGOBCCNAPqkTHkiboS8KfESOyhQasqcZHOBtRTG7TjcjYfOOOwASKKAKTxZumpiazQET47pXyIQSsbxTa9KJt4/640?wx_fmt=png "使用hcxdumptool捕获PMKID")

## 八、转换pcapng并使用hashcat破解

使用hcxpcaptool将pcapng文件转换为hashcat可破解的哈希格式：

```
hcxpcaptool -z hash demo
```

可以看到PMKID已被写入哈希文件。将该文件重命名为`pmkidhash`，接下来进行暴力破解：

```
hashcat -m 16800 --force hash /usr/share/wordlists/rockyou.txt --show
```

其中`-m 16800`表示WPA PMKID类型的哈希模式。就这样，Wi-Fi密码就找到了。

![hashcat破解PMKID](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OVxC9yddnoia2hCGea3JcrnYVnhBJv1nlC8gR9RtPPvOkNZSwrOt3ia6rmqZdIrkbrB5RZn2A790KQgRqx7SIXdK6PmiaRRUqKek/640?wx_fmt=png "hashcat破解PMKID")

![hashcat破解结果](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MCr4eyIZUkNG6Rr7veIzicHkrmnibKEah5SZQn8FD8rdcfzJHB4jcI1ckibtWKZZlicSeaMtcVnicqRicoLojNHNngKKa6jE8MOicjjU/640?wx_fmt=png "hashcat破解结果")

![破解成功](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6P1d0yD9VIvicM6LZNia8qxu4eBAjJndyVmKOMz5vCRzRfsy3XOl5rQbYcxOl5uILgzW08XScX2Pyu5PxdxXKS3wqxhX2EUHWMzI/640?wx_fmt=png "破解成功")

## 九、仅捕获单个AP的PMKID

之前我们捕获了周围所有路由器的PMKID，如果只想捕获某一个AP的PMKID呢？需要先记录该AP的MAC地址，在之前的hcxdumptool步骤中我已经将MAC地址保存到一个名为"target"的文本文件中。

接下来，只捕获这个AP的PMKID，将输出保存为`raj`文件：

```
hcxdumptool -o raj -i wlan0mon --enable_status=1 --filterlist_ap=target --filtermode=2
```

重复上述步骤，用hashcat破解：

```
hcxpcaptool -z pmkidhash raj
hashcat -m 16800 --force pmkidhash /usr/share/wordlists/rockyou.txt --show
```

![使用filterlist_ap参数](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PERoiauVNWSZI02y7lmdg1RZHrsGalUV5Nq1CkVPz4s9627dGDLuIzK48iaP3aBGBWSq4RwpBlJuWekaOVPuFjaicib61LHoV3OWQ/640?wx_fmt=png "使用filterlist_ap参数")

![设置filterlist_ap文件路径](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NVFbdfsrgibjXZjia0Q1AKQljISTAXTdoO0pBqZnFq5MuFdhBuB6y0EDvxMb4v03ULQ7a1NyhOaRmmILO5KPbzqUB5yuCafeI4g/640?wx_fmt=png "设置filterlist_ap文件路径")

![捕获PMKID成功](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Nibg6zic4s4Wj4mqbEjcGf4rIia5BiaPiayGVJia37DlKheQibPd9MehTqn60R9JSYq1HAiceejSgcwboibRXAic2MIeAalZub3kv5pgyk0/640?wx_fmt=png "捕获PMKID成功")

![用hashcat破解](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M1zHDQjoezyVtzxpCzR8PaXGUpUo8RxrHGfE0Nx7LEQpITNrghNo2yq2aD2xp8uO4iapZz8HCnC57YQKpCoEN8J7CoVFva1SIk/640?wx_fmt=png "用hashcat破解")

## 十、转换pcapng为pcap并用Aircrack-ng破解

前面的演示中用hcxdumptool捕获了一个名为"demo"的pcapng文件，现在将其转换为pcap格式并直接用aircrack-ng破解：

```
file demo
tcpdump -r demo -w demo.pcap
```

破解命令：

```
aircrack-ng demo.pcap -w /usr/share/wordlists/rockyou.txt
```

然后输入目标编号（这里是11）即可。

![转换pcapng为pcap](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OuianiaBy14rX8UoVicTjo5kUwLicHsKuE6lAc9PkUj4MlnwbI3ibR2u4a4xfHdXFyPVVox6Ikort8VcNzXS5icgzYvlbuicMSvrhqbY/640?wx_fmt=png "转换pcapng为pcap")

![aircrack-ng破解成功](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NBQBS6QTWGicRANLLpoqVYR00LwnCiaw6sW7IHa9UAeO2ob2V57FhAdQcvMKUHcSpIdrNV4HsQc5juiaNGvwicRHmFQevr0fibUEiak/640?wx_fmt=png "airc...