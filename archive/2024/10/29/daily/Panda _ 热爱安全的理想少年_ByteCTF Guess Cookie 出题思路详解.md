---
title: ByteCTF Guess Cookie 出题思路详解
url: https://www.cnpanda.net/ctf/1301.html
source: Panda | 热爱安全的理想少年
date: 2024-10-29
fetch_date: 2025-10-06T18:50:18.880521
---

# ByteCTF Guess Cookie 出题思路详解

[![Panda | 热爱安全的理想少年](https://www.cnpanda.net/logo.png)](https://www.cnpanda.net/)

搜一搜

# ByteCTF Guess Cookie 出题思路详解

本文最后更新于 2024.10.28，总计 28099 字，阅读本文大概需要6 ~ 22 分钟。

本文已超过 343天没有更新。如果文章内容或图片资源失效，请留言反馈，我会及时处理，谢谢！

## 0x01 写在前面

前段时间在字节 CTF 的大师赛上出了一个杂项，算是前段时间研究某个中间件的衍生产物，觉得很有兴趣，最近有时间便拿出来分享一下出题思路

## 0x02 小玩笑

当今时代，消息中间件已成为实现分布式系统和微服务架构的关键组件之一，市面上的常见的消息中间件主要有ActiveMQ、Kafka、RabbitMQ、RocketMQ，其中 RabbitMQ 主要用于金融业、Kafka 主要用于大数据行业，并且随着时间的推移，RabbitMQ 成为了最受欢迎和使用最多的消息队列之一。但是针对于 RabbitMQ 的利用和安全问题，在业内却少有研究。本题主要以 RabbitMQ 的erlang Node节点通信安全为核心，考察参赛选手对整个通信过程的安全理解。

当打开题目所给的 pcap 数据包后，可以看到172.20.10.24 和 172.20.10.4 之间通信的主要的协议有http、tcp、amqp、 ErlDP 等，如下图所示：

![1.png](https://www.cnpanda.net/usr/uploads/2024/11/1.png "1.png")

题目里设置了假的 flag，如果直接搜索 flag，会搜到 fakerflag{ByteDance@2024} 和 this is a faker flag that is ByteCTF{1e1111dce-cdf7-423f-8a8b-a62dec323d17}（开个小玩笑）

![2.png](https://www.cnpanda.net/usr/uploads/2024/11/2.png "2.png")

![3.png](https://www.cnpanda.net/usr/uploads/2024/11/3.png "3.png")

## 0x03 通信过程分析

进入正题。
根据题目描述：

> 请你尝试分析这段数据，解出 172.20.10.24 和 172.20.10.4 之间通信的 cookie

根据已有协议，http 协议的 cookie 为：

![4.png](https://www.cnpanda.net/usr/uploads/2024/11/4.png "4.png")

将其 转换为 32 位小写的 md5 后，提交发现 flag 错误，因此看看其他协议：AMQP、EPMD、ErlDP

实际上这三个协议主要是为 RabbitMQ 提供服务的，AMQP（Advanced Message Queuing Protocol，高级消息队列协议）是一个开放标准的应用层网络协议，用于在分布式系统中进行异步消息传递。它是RabbitMQ等消息中间件广泛支持的主要协议之一。AMQP协议支持多种认证机制，其中PLAIN-SASL（简单认证和安全层）是常用的一种。在PLAIN-SASL认证中，客户端通过提供用户名（username）和密码（password）进行身份验证。

除此之外，AMQP还支持其他SASL机制，如 EXTERNAL、ANONYMOUS 等，具体使用哪种机制取决于服务器的配置和安全需求。认证成功后，客户端需要经过一系列步骤才能开始消息传输，包括建立连接、创建通道、声明交换机和队列等。AMQP协议本身不使用cookie进行会话管理，而是依赖于长连接和通道的概念来维护通信状态。因此这个协议也可以排除筛选。那么就剩下两个协议了：EPMD 和 ErlDP。

这两个协议也是本题所考察的内容。即 Erlang 节点协议认证过程。

EPMD 全称为 Erlang Port Mapper Daemon，在 RabbitMQ 中主要充当"名称服务器"的作用。它的主要功能包括：

1. 将符号节点名称映射到具体的 IP 地址和端口号。
2. 维护一个活跃 Erlang 节点的注册表。
3. 协助 Erlang 节点之间建立初始连接。

EPMD 通常在端口 4369 上运行，为 Erlang 集群中的节点提供服务。

Erlang Distribution Protocol（有时简称为 Erlang Distribution 或 Erldp）是 Erlang 编程语言中用于实现分布式系统通信的核心协议。它的主要特点包括：

1. 用于 Erlang 节点之间的通信。
2. 支持远程过程调用（RPC）和消息传递。
3. 提供内置的容错和错误处理机制。

对于节点间的认证，Erlang 使用了一种称为 "Magic Cookie" 的机制：

1. 每个 Erlang 节点都有一个 cookie，这是一个字符串值。
2. 当两个节点尝试建立连接时，它们会交换并比较各自的 cookie。
3. 只有当两个节点的 cookie 相同时，连接才会建立。
4. cookie 通常存储在一个名为 .erlang.cookie 的文件中。

当然，虽然这种机制被称为 "cookie"，但它与 Web 浏览器中使用的 HTTP cookie 完全不同。Erlang 的 cookie 是一种简单的共享密钥机制，用于节点认证。本题最终的 flag 也就是这个 cookie 32 位 MD5 的小写值。
筛选与 Erlang 通信相关的协议（epmd || erldp）可以发现：

![5.png](https://www.cnpanda.net/usr/uploads/2024/11/5.png "5.png")

想要分析这段通信的含义就要首先了解 RabbitMQ 中 Erlang节点通信验证的逻辑，过程如下：

Client Node Server Node

```
|                                                |
|        1. SEND (name, flags, creation)         |
|----------------------------------------------->|
|                                                |
|        2. CHALLENGE (challenge, flags)         |
|<-----------------------------------------------|
|                                                |
|        3. CHALLENGE_REPLY (digest)             |
|----------------------------------------------->|
|                                                |
|        4. CHALLENGE_ACK (digest)               |
|<-----------------------------------------------|
|                                                |
```

现在详细分析每个步骤：
第一步：SEND 客户端节点发送一个SEND消息。包含以下信息：

* 节点名称：标识客户端节点
* 标志(flags)：包含版本信息和其他元数据
* 创建信息(creation)：用于区分同名但不同时间创建的节点

{SEND,
 NodeName, % 例如 'rabbit@node01'
 Flags, % 例如 [DFLAG\_EXTENDED\_REFERENCES, DFLAG\_DIST\_MONITOR, ...]
 Creation % 例如 1
}

对应pcap 包中的 471、517、851以及 970 行

![6.png](https://www.cnpanda.net/usr/uploads/2024/11/6.png "6.png")

第二步，CHALLENGE 服务端节点收到SEND后，回复一个CHALLENGE消息。包含：

* 挑战值(challenge)：一个随机生成的大整数
* 标志(flags)：服务端支持的功能标志

{CHALLENGE,
 Challenge, % 例如 1234567890
 Flags % 例如 [DFLAG\_EXTENDED\_REFERENCES, DFLAG\_DIST\_MONITOR, ...]
}

对应pcap 包中的 475、521、855 以及 974 行

![7.png](https://www.cnpanda.net/usr/uploads/2024/11/7.png "7.png")

第三步，CHALLENGE\_REPLY 客户端接收到CHALLENGE后，计算并发送响应：

* 摘要(digest)：使用共享的"magic cookie"和挑战值计算的MD5哈希

{CHALLENGE\_REPLY,

```
  Digest          % 服务端计算的MD5
```

}

对应pcap 包中的 976 行

![8.png](https://www.cnpanda.net/usr/uploads/2024/11/8.png "8.png")

第四步，也即最后一步，CHALLENGE\_ACK 服务端验证客户端的响应，如果正确，发送ACK：

* 摘要(digest)：服务端使用相同方法计算的摘要，用于双向认证

{CHALLENGE\_ACK,

```
  Digest         % 服务端计算的MD5
```

}

对应 pcap 包中的 977 行：

![9.png](https://www.cnpanda.net/usr/uploads/2024/11/9.png "9.png")

这就是整个验证过程，结合协议过程、pcap 包或许还不能够理解整个过程的话，还可以看看erlang节点的 cookie 认证过程代码，在官方仓库中 erlang/otp/lib/jinterface/java\_src/com/ericsson/otp/erlang/AbstractConnection.java 文件里有相关定义，其主要代码如下：

```
    protected void recvChallengeAck(final int our_challenge)
            throws IOException, OtpAuthException {

        final byte[] her_digest = new byte[16];
        try {
            final byte[] buf = read2BytePackage();
            @SuppressWarnings("resource")
            final OtpInputStream ibuf = new OtpInputStream(buf, 0);
            final int tag = ibuf.read1();
            if (tag != ChallengeAck) {
                throw new IOException("Handshake protocol error");
            }
            ibuf.readN(her_digest);
            final byte[] our_digest = genDigest(our_challenge,
                    localNode.cookie());
            if (!digests_equals(her_digest, our_digest)) {
                throw new OtpAuthException("Peer authentication error.");
            }
        } catch (final OtpErlangDecodeException e) {
            throw new IOException("Handshake failed - not enough data");
        } catch (final Exception e) {
            throw new OtpAuthException("Peer authentication error.");
        }

        if (traceLevel >= handshakeThreshold) {
            System.out.println("<- " + "HANDSHAKE recvChallengeAck" + " from="
                    + peer.node + " digest=" + hex(her_digest) + " local="
                    + localNode);
        }
    }
...

    protected void sendChallengeReply(final int challenge, final byte[] digest)
            throws IOException {

        @SuppressWarnings("resource")
        final OtpOutputStream obuf = new OtpOutputStream();
        obuf.write2BE(21);
        obuf.write1(ChallengeReply);
        obuf.write4BE(challenge);
        obuf.write(digest);
        obuf.writeToAndFlush(socket.getOutputStream());

        if (traceLevel >= handshakeThreshold) {
            System.out.println("-> " + "HANDSHAKE sendChallengeReply"
                    + " challenge=" + challenge + " digest=" + hex(digest)
                    + " local=" + localNode);
        }
    }

...
    protected byte[] genDigest(final int challenge, final String cookie) {
        int i;
        long ch2;

        if (challenge < 0) {
            ch2 = 1L << 31;
            ch2 |= challenge & 0x7FFFFFFF;
        } else {
            ch2 = challenge;
        }
        final OtpMD5 context = new OtpMD5();
        context.update(cookie);
        context.update("" + ch2);

        final int[] tmp = context.final_bytes();
        final byte[] res = new byte[tmp.length];
        for (i = 0; i < tmp.length; ++i) {
            res[i] = (byte) (tmp[i] & 0xFF);
        }
        return res;
    }
```

大致流程如下：
生成摘要： 使用 genDigest() 方法生成摘要。这个方法使用三个参数：challenge、Cookie 和一个固定字符串。

```
protected byte[] genDigest(final int challenge, final String cookie) {
    // ...
    context.update(cookie);
    context.update("" + ch2);
    // ...
}
```

交换challenge： 双方交换挑战值，但不直接交换 Cookie。

验证digest： 每一方使用接收到的challenge和自己的 Cookie 生成digest，然后与对方发送的digest进行比较。

```
final byte[] our_digest = genDigest(our_challenge, localNode.cookie());
if (!digests_equals(her_digest, our_digest)) {
    throw new OtpAuthException("Peer authentication error.");
}
```

判定 Cookie 正确： 如果双方生成的digest相同，就认为 Cookie 是正确的。因为只有双方使用相同的 Cookie 才能生成相同的摘要。

设置 cookieOk 标志： 当认证成功时，设置 cookieOk = true。

```
java
Copy
cookieOk = true;
sendCookie = false;
```

后续通信： 在后续的通信中，如果 cookieOk 为 true，就不再重复完整的认证过程。

## 0x04 一个例子来说明

举例来说，具体如下。
远程的 IP为：101.x.x.145
其流程主要如下：

| 步骤 | 消息类型 | 通信方向 | 内容 | 说明 |
| --- | --- | ...