---
title: Copy Fail漏洞深度学习
url: https://mp.weixin.qq.com/s/4Ov6k5yoSaGyuHQ3GTE5EQ
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:21:17.408359
---

# Copy Fail漏洞深度学习

# Copy Fail漏洞深度学习

S\_i\_d
S\_i\_d

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

根据相关的资料，重新学习一下这个copy fail 漏洞，相关参考：

https://bbs.kanxue.com/thread-291167.htm

https://juejin.cn/post/7634537755251081226

https://github.com/Juguitos/copy-fail

https://zhuanlan.zhihu.com/p/2033279916859470743

**漏洞原理剖析**

这个漏洞的本质可以用一句话描述：它是 Linux内核 crypto 子系统中的一个逻辑漏洞，使普通用户能够向任意可读文件对应的 Page Cache 写入4个可控字节，最终获得 root 权限。

漏洞发生在copy\_from\_iter()函数里面。

## Page cache & AF\_ALG

Linux在读取磁盘文件时，Linux不每次都去读取磁盘，而是先去到Page chche里面寻找是否有缓存，如果找到就直接使用缓存数据，没找到再去访问磁盘。

但是page cache是多个进程共享的，如果有人能修改，那么多有进程都会看到修改后的内容。

然后我们需要去了解AF\_ALG接口，也就是User Space Crypto API，用户态程序可以直接调用内核加密算法。

比如：

```
socket(AF_ALG)
```

```
User
 ↓
AF_ALG Socket
 ↓
Crypto Subsystem
 ↓
Kernel
```

当调用Authencesn算法时，copyfail漏洞就出现了。

## AEAD &  Authencesn

AEAD即Authenticated Encryption with Associated Data，带关联数据的认证加密，是一种同时提供数据加密、完整性验证和身份认证的加密模式。

AEAD不仅对数据进行加密以保证保密性，还通过认证机制确保数据在传输或存储过程中未被篡改，同时验证密钥和数据的正确性。

简单来说就是把密文和不加密但要认证的数据同时参与认证。aad就是表示需要认证但是不需要加密的附加数据。比如tls里面的记录头信息。

AEAD算法比如aes-gcm,

```
AEAD(
   key,
   nonce,
   plaintext,
   aad
)
=
(ciphertext, tag)
```

而Authencesn全称是： Authenticated Encryption with Associated Data and Extended Sequence Numbers，具有关联数据和扩展序列号的认证加密。主要是给IPsec ESP使用的。普通的aead是aad、payload参与认证，authencesn则是aad,payload,sequence number参与认证。这样攻击者即使复制了整个包，也会因为sequence number的不同而过不了认证。

copyfail漏洞与authencesn处理有关系，研究人员发现，在authencesn 处理时，会重新组织内存布局并交给copy\_from\_iter()，用户空间可以通过AF\_ALG接口，调用authencesn 并且完全控制aad的内容。authencesn 并没有随aad进行完整校验，导致page cache的内容被authencesn 修改。

## splice & ESN scratch write

splice() 是 Linux 提供的零拷贝数据传输机制。在支持的场景下，它不会复制实际数据，而是让 pipe\_buffer 直接引用已有的内核页（例如文件的 page cache 页），从而减少内存拷贝开销。

在 file→pipe 的 splice 路径中，pipe\_buffer 通常不会保存文件内容的副本，而是持有对应 page cache 页的引用。因此后续内核组件如果错误地将这些页当作可修改的临时缓冲区，就可能直接修改底层 page cache，而不仅仅是修改 pipe 中的数据。

普通的 `read()` + `write()` 流程需要将文件数据拷贝到用户空间 buffer，再从用户空间 buffer 拷贝到目标。而 `splice()` 直接把文件的 page cache 页面引用传递给管道的另一端，全程不发生数据拷贝。

引用自参考博客

我们还需要理解 IPsec ESP 协议中 ESN（Extended Sequence Number）机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1xZZibq7hkKyd3I0KVSRLbBkMgvhhadKyUia6D1K0kJp1SRgk486sJKm3KRib3OI5GfCTC2UBHoyokbk7BpAv2GqmZbIiaA1MNTyc/640?wx_fmt=png&from=appmsg)

ESP 协议最初只有一个 32 位序列号。发送一个数据包，序列号就加一。

但 32 位最多只能表示约 42 亿个包。在高速网络环境下，这个数字并没有想象中那么大。如果序列号最终重新回到 0，就可能出现重放攻击问题，因为旧的数据包又拥有了相同的序列号。

因此 IPsec 引入了 ESN（Extended Sequence Number）。

ESN 实际上把序列号扩展成了 64 位，其中：

* 低 32 位仍然放在网络数据包中传输；
* 高 32 位由通信双方在本地维护。

这样序列号几乎不可能发生回绕。

ESP 的认证机制需要计算 HMAC。

如果 HMAC 只覆盖低 32 位序列号，那么当序列号从 0x00000000FFFFFFFF 增加到： 0x00000001FFFFFFFF 时，网络上传输的低 32 位仍然都是：0xFFFFFFFF

这样两个不同的数据包可能得到相同的认证输入。

因此 RFC 要求：认证计算必须包含完整的 64 位序列号。也就是说，高 32 位虽然没有发送出去，但仍然必须参与 HMAC 运算。

Linux 原来的 authenc 框架是在 ESN 出现之前设计的。它默认认为参与认证的数据只有：

* SPI
* 低 32 位序列号
* 数据负载

它并不知道还有一个“高 32 位”。但协议要求高 32 位必须参与认证，因此 authencesn 就必须想办法把这 4 个字节塞进认证计算的数据流中。

在 ESP 输出数据包时，数据包尾部通常会预留一块空间，用于存放最终计算出来的认证标签（auth tag）。

而在 HMAC 尚未计算完成之前，这块空间实际上还是空的。开发人员发现，既然这里反正暂时没有内容，不如先借用这块空间。于是 authencesn 会把 ESN 的高 32 位临时写到这块区域中。这样 HMAC 在遍历整个缓冲区时，就能够看到完整的 64 位序列号。

因此：

* 把高 32 位写进去；
* 执行 HMAC；
* HMAC 计算完成；
* 再把真正的 auth tag 写回去。

从最终网络数据包来看，这 4 个字节从来不会真正发送出去，它只是一个临时工作区。这就是所谓的：ESN scratch write（ESN 临时写入）。

正常情况下，整个过程是：首先，高 32 位被写入认证标签的位置。随后加密和认证过程成功执行。最后，真正计算出来的 auth tag 会覆盖掉这 4 个字节。

因此最终数据包中只会留下：

* payload
* auth tag

临时写入的数据已经消失。

所以很多年里，这种设计一直都正常工作。

直到copy fail的发现：开发者默认认为，后续步骤一定会成功。但是实际上，加密或者认证操作可能失败。

例如：

* 内存分配失败；
* 加密请求失败；
* 异步操作失败；
* 驱动返回错误。

如果错误发生在高 32 位已经写入之后，而真正的 auth tag 还没有写回之前，那么流程会提前退出。这样就出现了一个问题：那 4 个字节仍然残留在 dst buffer 中。原本只是临时工作区的数据，没有被恢复。

因此：

* 缓冲区内容变得异常；
* 某些内核数据可能泄漏；
* 后续代码可能读取到错误的数据；
* 用户空间可能观察到不应该看到的内容。

这就是 Copy Fail 的本质。

## 漏洞的出现

前面已经提到了一些漏洞的背景原理，现在具体到copy fail漏洞是怎么发生的。

漏洞的引入从2017年开始。在 2017 年之前，algif\_aead 的解密采用的是 **out-of-place 解密模式**。

所谓 out-of-place，就是：

* 输入缓冲区（src）和输出缓冲区（dst）不是同一个。
* 解密后的数据写入另外一块内存。

当时的代码逻辑是：

* TX SGL（发送缓冲区）作为输入。
* RX SGL（接收缓冲区）作为输出。

TX SGL 里面保存了用户发送进来的全部数据：

* AAD
* 密文
* Auth Tag

而 RX SGL 是用户调用 recvmsg() 时提供的接收缓冲区。

```
解密前：
TX：
[AAD][密文][TAG]

RX：
[空]

解密后：

RX：
[？？][明文]
```

这里的问题在于：AEAD 算法本身只负责处理密文。它不会主动去处理 AAD。

AEAD 的工作流程实际上是：

* AAD：参与认证，但不加密。
* 密文：参与认证，并且需要解密。
* Tag：用于验证完整性。

因此解密结束以后： 密文部分会变成明文。  AAD 理论上应该原样保留。

但是底层加密算法只会操作密文区域。

然而对于 algif\_aead 而言： AAD 在 src 中。  dst 中对应位置是空的。

于是解密完成以后：

```
dst:

[AAD区域] [明文]
```

前面的 AAD 区域没人填。

结果用户收到的数据变成：

```
0000000000000000 + plaintext
```

AAD 全是 0。  这违反了 AEAD 接口的语义。

内核开发者Stephan Mueller 提交的 commit 72548b093ee3，就是专门解决这个问题。

开发者的思路非常简单：既然算法不会复制 AAD，那么调用者自己复制： 先把 AAD 和密文复制到 RX， 然后算法直接在RX上解密。

于是新增了一步：

```
src ----copy----> dst
      AAD区域
```

这样：

* AAD 被提前写入 dst。
* 解密时算法只处理密文。
* 最终用户收到：

```
AAD + plaintext
```

这才符合 AEAD API 的要求。

因此这个补丁本身其实是完全正确的。

但是这样修复之后 ，解密后收到的是

```
RX：
[AAD][明文]
```

AEAD算法还需要去验证tag，开发者采用了直接引用的方法，

```
RX：
[AAD][密文]
         ↓
       TAG页面
```

也就是sg\_chain()。

这里没有复制tag，而是在 scatterlist后面再挂一个节点。

这样就给漏洞的出现提供机会

在 Linux 内核中，为了追求极致的性能，用户经常会使用 `splice()` 或 `sendfile()` 系统调用。这些调用的核心优化就是**零拷贝（Zero-Copy）**。

当用户通过 `splice()` 将一个文件中的数据发送到 `algif_aead` 的 Socket 时，内核为了省去将数据从内核复制到用户空间的开销，会**直接把该文件在 Page Cache（页面缓存）中的物理页面（Pages）拿过来，作为 TX SGL 的内存流**。

这意味着：

* **此时 TX SGL 里的 AAD、密文等数据，在物理上就是 Page Cache 里的页面。**
* 这些页面是由内核的管理机制（如文件系统、块设备层）锁定的，通常是只读的。

但是漏洞单靠 `splice` 还不够，攻击者还需要利用一个网络编程中常见的标志：`MSG_MORE`。

当调用 `sendmsg()` 或 `splice()` 时如果带了 `MSG_MORE`，意思是：“我后面还有数据要发，你先别急着提交给硬件/加密算法，先在内核里攒着。”

此时，`algif_aead` 会把当前的 TX SGL（来自于 Page Cache 的页面）暂存到内核的 Socket 缓冲区中（即 `ctx->tsgl`）。

漏洞的触发还需要 `copy_from_iter` 参与。

用户接下来调用 `recvmsg()` 尝试去解密并接收数据。

正如我们前面分析的，commit 72548b093ee3 引入了一个修复操作：**在解密前，必须先把 AAD 区域从 src（TX SGL）复制到 dst（RX SGL）。**

内核在执行这个复制时，使用的是底层内存拷贝函数（如 `copy_from_iter` 或 `memcpy_from_page`）。 它的意图是：从 TX SGL（源）读取 AAD，写入 RX SGL（目的）。

**但是，如果攻击者故意进行恶意构造，让 RX SGL 的接收缓冲区，“正好”也指向刚才那个 Page Cache 页面呢？**（或者由于并发、重用等原因导致了页面的重叠）。

更严重的是，即使没有完全重叠，根据前面讲的 `sg_chain()` 逻辑： 解密时，算法需要验证 Tag。为了效率，内核直接用 `sg_chain()` 把 TX 的 Tag 页面挂到了 RX SGL 的尾部。

此时的 RX SGL 变成了这样一个“缝合怪”：

```
RX SGL: [ 用户Rx缓冲区 ] -> [ 链表指针 ] -> [ 来自TX的Tag页面 (实质是Page Cache) ]
```

如果此时调用发生错误，或者在复杂的并发并发套接字操作中，内核在执行：

```
// 伪代码：本意是将数据拷入RX，但RX的某个节点（比如Tag）其实指向了Page Cache
crypto_aead_copy_aad(...);
```

**由于对输入/输出边界缺乏严格的检查，内核在复制（Copy）时如果发生失败（Fail）——也就是**`copy_fail`**名字的由来：**

* 内核尝试向 RX SGL 写入 AAD 或者是解密后的明文。
* 结果由于某些页面的共享或重用，这个写入目标**错误地指向了尾部挂载的那个属于 Page Cache 的只读页面**。
* `copy_from_iter`

  这种函数在向一个“只读”的 Page Cache 页面强制写入数据时（内核态有最高权限，可以绕过写保护），**直接污染了（Dirtied）系统全局的 Page Cache！**

`copy_fail` 的闭环：

* **Page Cache 提供舞台**

  用户用 `splice` 发送文件，导致加密算法的输入源（TX）直接引用了内核的 Page Cache（页面缓存）。
* **Commit 72548b093ee3 引入工具**

  为了修复 AAD 为 0 的问题，引入了“主动 Copy AAD 到 RX”以及“用 `sg_chain` 将 Tag 页面直接挂到 RX 尾部”的逻辑。这导致 **RX SGL 间接持有了 Page Cache 页面的写权限**。
* **Copy Fail 瞬间引爆**

  在解密、复制的异常处理路径中（Fail 路径），内核未能正确校验边界，导致原本应该写到用户缓冲区的明文或 AAD，**直接覆盖写进了 Page Cache 页面**。

由于 Page Cache 是全局共享的，一旦它被污染，当其他正常进程（甚至系统核心服务）再次读取该文件时，读到的就是被篡改后的数据。这就完成了从一个“加密 API 语义修复”到“任意文件覆盖 / 本地提权（LPE）”的漏洞演变。

## 漏洞利用过程

我们已经知道，`sg_chain()` 最终将包含 **Tag** 的页面指针挂载到了接收端 `combined dst SGL` 的尾部。现在，我们把整个利用过程从头到尾走一遍。

假设我们的目标是：**在无需任何写权限的情况下，向系统关键文件（如**`/usr/bin/su`**）的偏移 t 处，强行写入 4 字节的可控恶意数据。**

### Step 1：用户空间精心构造并发送数据

在用户空间，攻击者需要通过配置特殊的解密参数，分两步欺骗内核：

* `assoclen = 8`：通过 `sendmsg` 的控制消息设置 AAD 长度为 8 字节。
* `authsize = 4`：通过 `setsockopt(ALG_SET_AEAD_AUTHSIZE)` 设置认证标签大小为 4 字节。

随后，通过两条路径向 `AF_ALG` 套接字注入数据：

Python

```
# 1. 构造恶意 4 字节载荷（最终要写入 Page Cache 的数据）
evil_bytes = b'\xde\xad\xbe\xef'

# AAD 前 4 字节任意填充，后 4 字节为 payload
aad = b'\x00\x00\x00\x00' + evil_bytes
op.sendmsg([aad], cmsg, MSG_MORE)       # 使用 MSG_MORE 标志让内核暂存

# 2. 通过 splice() 引入目标文件的 Page Cache
pipe_r, pipe_w = os.pipe()
target_fd = os.open("/usr/bin/su", os.O_RDONLY) # 仅需只读权限！
os.splice(target_fd, pipe_w, t + 4, offset_src=0)  # 文件 → 管道 (长度 t + 4)
os.splice(pipe_r, op.fileno(), t + 4)               # 管道 → AF_ALG 套接字
```

### Step 2：TX SGL 布局分析

经过上述操作后，内核在物理内存中为 `TX SGL` 攒出来的连续视图如下：

Plaintext

```
TX SGL 内存布局:
+--------------------+----------------------------------------+
| sendmsg data (8B)  | splice data (t+4 bytes)                |
| AAD: 4 zero bytes  | file[0:t+4]                            |...