---
title: UniCTF 两道流量分析 WP
url: https://mp.weixin.qq.com/s/7aVP1dtuK4Y7vZhv9NuEGg
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:25.210472
---

# UniCTF 两道流量分析 WP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8luVgd0LFMvOcibVTT4GZX2otdQEvrjPUQAImB3WfodbtpIRrsGNEVpw/0?wx_fmt=jpeg)

# UniCTF 两道流量分析 WP

江思澄
江思澄

云晞科技Sec

![]()

在小说阅读器中沉浸阅读

**YunSee团队招新**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/nNzOrpxNkNMDupRfkbNbIW6mXS9bM9vOzCniciaURunvfYOGlfU3Utu7j8d7yVCcYcr62xpZCJ5a1ROzmZO3EswQ/640?wx_fmt=gif&from=appmsg)

为了进一步壮大团队实力，我们现面向全网招募密码学、AI 安全、逆向方向的师傅 加入交流。只要你愿意分享、热爱探索、喜欢和同好一起“碰撞火花”，我们都热烈欢迎！

招新要求：

* 具有 CTF 比赛经验者优先，且在相关赛事中取得优异成绩者将予以重点考虑；
* 优先考虑能定制和训练 CTF 解题 Agent 的选手

当然，我们也十分欢迎愿意一起交流、组队打 CTF 的师傅加入我们的“魔丸”交流群，在这里共同探讨技术、相互学习进步。

联系方式：

* 简历发邮箱：achenc1013@gmali.com
* 魔丸交流群：1034296865

## 工厂应急响应挑战赛

### **任务 1：谁把阀门打开了？**

找到 Modbus 打开阀门指令的相关信息。

打开阀门操作应该对应功能码是0x05，而打开操作的data通常为0xFF00

```
modbus.func_code == 5 && modbus.data == ff:00
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic80v7VzGw8hUsiadnlSgwZ6xB89tDawTFlLtxGtco7ibdD9ibOWOkfMX0zQ/640?wx_fmt=png&from=appmsg)

fig:

**transaction\_id = 0x3c4d**

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8WTdHcT4J9IWTGH6iakbYWrGW5tzdfrbEwCWCKbraHcw6Bu6f9HjNvOQ/640?wx_fmt=png&from=appmsg)

fig:

**function\_code = 0x05**

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8LreqBBaCu8ICbXicEhAS8hqDjXDlCK3UZ0XEyNBayj0iayCQdHkovKlA/640?wx_fmt=png&from=appmsg)

fig:

coil\_address找Reference Number即可

**Reference Number = 0x0015**

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8K2AuOREiawYibOa5n9vmYLRH5GgRMe6uPpBKzG8B1nbC0ebTp28Nv3wg/640?wx_fmt=png&from=appmsg)

fig:

flag{0x3c4d\_0x05\_0x0015}

### **任务 2：被读取的 NodeId**

找到通过 OPC UA 协议读取的 NodeId。

读取请求我们直接针对ReadRequest进行模糊筛选

```
tcp contains "ReadRequest"
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8fBiaky05Z2M04mOy92ibRhJL4gibicwHOewicxBpTSIzegpGj2hcib62ic96w/640?wx_fmt=png&from=appmsg)

fig:

第一个包就是

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8ytc9hnxcpbQs8xe2gohdmBM2eEmB8VZEWHMIl4zdLOq2lkd90KFERg/640?wx_fmt=png&from=appmsg)

fig:

flag{ns=2;s=Valve/Status}

### **任务 3：控制站域名解析结果**

找出控制站域名 ctrlws.factory.local 的解析 IP。

```
dns.qry.name == "ctrlws.factory.local"
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8CWlwhEro5cQBX19kRAx5arh1S82tHRBBACT1jcQXdLblk3lF0L32rw/640?wx_fmt=png&from=appmsg)

fig:

可以看到A地址域名解析的IP

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8AEicAibpUYgAiatSMLF9jWelUlIPKJ8ickNJHWzGFtYJXJwUVKwZzuxj6w/640?wx_fmt=png&from=appmsg)

fig:

flag{192.168.1.10}

### **任务 4：连接建立时间**

确定SCADA（源：192.168.1.5）到控制站（目的：192.168.1.10）上首个成功发起的时间点(UTC)。

```
ip.src == 192.168.1.5 && ip.dst == 192.168.1.10 && tcp
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8KvEibJd8HHmtrsxHLh4IWiaxt5zJr1GPjU9yq5YoGwpTaKia8SWErMbuA/640?wx_fmt=png&from=appmsg)

fig:

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8VhHIuvegdgiaLf8aX61gEZL0SXjZL60DuVtBAGs4LLqFTl09kkic9rXQ/640?wx_fmt=png&from=appmsg)

fig:

flag{2025-03-15T09:30:01Z}

### **任务 5：HTTP 请求痕迹**

提取 SCADA 对控制站发起的 HTTP 请求的 Host 与 URI。

已知SCADA 系统（192.168.1.5）控制站（192.168.1.10）

```
http && ip.src == 192.168.1.5 && ip.dst == 192.168.1.10
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8MpNAJhCFvr4bzzhIwibSicd8ZHyoD74Bak4AqhRYSgkZctZibZhl3eXBA/640?wx_fmt=png&from=appmsg)

fig:

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8NaiaxA8IwejpbuAqDqF9ms0GkP62V9iaNSpZ8gMyfwY8ZGCp2ABZb7uA/640?wx_fmt=png&from=appmsg)

fig:

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8lXvWDqXIQwqAHxYouKA5gqXl5iaBMIVs6M3yfU36NzZxsP8woX9jbkA/640?wx_fmt=png&from=appmsg)

fig:

flag{ctrlws.factory.local\_/api/status}

### **任务 6：ICMP Echo Request 序列号**

攻击者（192.168.1.100）对控制站发起了 ICMP Echo Request（ping）。找出该 ICMP 请求的序列号（Sequence Number）。

直接针对icmp报文进行过滤

```
icmp && ip.src == 192.168.1.100 && ip.dst == 192.168.1.10
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8QVA8RAxh4lqgTiauIbvoBy5yHWTwXmwP9BzguiaKKkGWhvY91UEAyAVA/640?wx_fmt=png&from=appmsg)

fig:

BE表示大端序，LE表示小端序。而协议是按照大端序发的，所以BE才是正确的序列号

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8kD6AP0fUj06ckRyxkib2ibmib7opDoraCShBt9TSFRDw2WplchqfXRhEQ/640?wx_fmt=png&from=appmsg)

fig:

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8wwBbOvEhoVY2hf8qLAkxeE7u2g050F3w9q1zh3noNOlEMyUzmQCAIw/640?wx_fmt=png&from=appmsg)

fig:

flag{0x0123}

### **任务 7：SNMP Get 请求的 OID**

SCADA 对控制站发起了 SNMP Get 请求。找出该请求查询的 OID（Object Identifier）。

SNMP的默认端口是161

```
udp.port == 161 && ip.src == 192.168.1.5 && ip.dst == 192.168.1.10 && udp
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8f1nVfvibCvbxI9a1gHNDb7cOPT3hUYwufJKyJp3w6sfkQhhcicUCs1ng/640?wx_fmt=png&from=appmsg)

fig:

追踪UDP流

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8O9gXMbNttrQNtQtgTS9CVZUD05tG8uAcmlZTsILT9iagmibhCNfWtYsQ/640?wx_fmt=png&from=appmsg)

fig:

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8M1t7WrMcia2D5TRkl4djRdnfVIo69u2o8fa4zV3SH0iaRqPAbGL0Ny5A/640?wx_fmt=png&from=appmsg)

fig:

## BlueBreath

在统计会话中TCP协议频次最高的端口就是：8000

**Server：172.30.96.1:8000**

**Client：192.168.80.129**

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8ns0XpZxUJxkKDHwFNG6PgzhMvH4rMwOoibbytFfkjoY1UvdLpJvhxag/640?wx_fmt=png&from=appmsg)

fig:

NetA自动下载了一个压缩包，但是解压需要密码

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8TspOyoyicm6Zyyuxf30VgKHOF7d4OGIJ2KA4yxestf4GPEoNO8cG6Rg/640?wx_fmt=png&from=appmsg)

fig:

已知是一个png文件，尝试使用bkcrack明文破解

```
89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52
# PNG的固定开头16字节
```

写一个明文文件

```
open("png.header","wb").write(bytes.fromhex("89504E470D0A1A0A0000000D49484452"))
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8UmeMLLVsOUZ8PhOibeKgD2ys1YwrslJIoDG6jdHcLl6icicNoTkvEADVA/640?wx_fmt=png&from=appmsg)

fig:

```
bkcrack -C hint.zip -c hint.png -p png.header
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8GL0tLqnhxYhxKP0SicR31oqT9xtV5fFTAPicumHcNVmotO5vd5Obicq3Q/640?wx_fmt=png&from=appmsg)

fig:

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8tV5ZppjwsGIm65hILv9Qdaxib1vDn6fdsn2SLsKvV4hh6ib3lvg0YfIA/640?wx_fmt=png&from=appmsg)

fig:

这图片我也不清楚有啥用，没啥可用的信息

先来到wireshark 筛选http POST请求

```
http.request.method == "POST"
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8iazSzy1G7lWk7KDPzYJOVX3WokTQia6z9xHXDOfLgOJkNBdYm4BtPuQA/640?wx_fmt=png&from=appmsg)

fig:

发现上传了shell.php可疑文件

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic88cIazMQ9ZBkDvbWZSPuZ49p7eib2dwRYLGmjD8oaQVTmIoraSU0jGPw/640?wx_fmt=png&from=appmsg)

fig:

像二进制被加密数据

筛选所有包含shell.php 的流

```
http.request.method == "POST" && http.request.uri contains "shell.php"
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8ZPch0fFnUw0lYfgMZDS6p5y66icDOrxvQMdSYOhzbVIahWOJ0PvZT7w/640?wx_fmt=png&from=appmsg)

fig:

前三个流一大片乱码，怀疑是后门的加密源码

从第四个流开始，这里的传输的加密数据好似哥斯拉那种加密shell后门，请求的命令以及执行结果回显

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8TFOCHU3dJe3LgGVARiaoUeiaxxXymocdGVwSib0IZMsYz57PuwPzhRxIA/640?wx_fmt=png&from=appmsg)

fig:

数据的开头都是：7b e8 3b 65 66 35 66 66 30 ...

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8ovu4eU78BLvcTL9Y4CnzWRVmicyZEOzFpU119ic9ml0iag7ZZU5ZjqrjA/640?wx_fmt=png&from=appmsg)

fig:

webshell 常见做法是“先压缩再混淆”，于是尝试以 gzip 固定头 1f 8b 08 00 00 00 00 00 00 作为已知明文，利用 C XOR P 反推出前 9 字节密钥

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNNvb3IJcqeYhKibG4pn35Jic8jG5t5cicZD4FbxEVltsE843ugvcSHjBZGC0WV6Xl01c8pS4edgSDeUw/640?wx_fmt=png&from=appmsg)

fig:

得到的是可显示的字符串，说明...