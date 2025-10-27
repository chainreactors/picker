---
title: 远程访问木马RAT样本分析
url: https://forum.butian.net/share/3943
source: 奇安信攻防社区
date: 2024-12-27
fetch_date: 2025-10-06T19:33:06.732286
---

# 远程访问木马RAT样本分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 远程访问木马RAT样本分析

样本分析
信息熵表明该恶意程序可能在内存中存在有效负载。
查看字符串和导入表：
Software\Microsoft\Windows\CurrentVersion表明程序执行某些和注册表相关的操作，CreateProcessA或ShellE...

样本分析
====
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-99232b88c42ec0cdc358dbc50db1f9371e80ce77.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-91c9b5437fcb4aff7be4beb0ad6425f809371b76.png)
信息熵表明该恶意程序可能在内存中存在有效负载。
查看字符串和导入表：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-85344a0c197c3cc8fe339acbc8230e664a52fe23.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1a62f8ca776b64fa5262cc9ff41588ab2e8ead78.png)
`Software\Microsoft\Windows\CurrentVersion`表明程序执行某些和注册表相关的操作，`CreateProcessA`或`ShellExecuteA`可能用来执行进行下阶段的有效负载，找一找也能发现和注册表相关的API`RegSetValueExA`、`RegCreateKeyExA`。
沙箱
--
在沙箱中运行了下该恶意程序。
第一个指标，恶意程序一直在尝试联系恶意域名stonecold.ddns.net：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8eaec3c7224cccd55dcdfa67b272da886b6e4675.png)
成功链接后，发送多个 TCP 数据包，在指定端口上创建2502套接口。
第二个指标，恶意软件启动后立即在临时文件目录释放了文件：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-531f5aa7a35b1f307da2c34e959e77e1978cf660.png)
查看进程列表，可以知道，第一阶段的恶意程序在资源中提取了三个文件，分别是 cmdkuqqy, cckgcf.exe 和 ka9zcqw3l6l48a1uuba，然后执行第二阶段的恶意样本cckgcf.exe，将提取的另外俩个文件作为参数传递。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b20b124c4cc1efcccdf222367924c3648d5ae1ea.png)
cckgcf.exe
==========
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-761c6247f1fe7135f7848828efc41e5c91760093.png)
`GetCommandLineW`函数接收命令行参数，这里应该是接收刚刚俩个加密文件。如果参数获取成功，才会进行下一步，进行解密。
恶意程序的API都经过混淆，需要动态解析出来：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e5797ce2bafc880e64ed914fb79ff0879f9238de.png)
单步调试可以发现隐藏在恶意软件进程中的shellcode，该shellcode是一个可以执行的PE格式文件：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a0249d2c9aa83338e8e5d2ea98389891e833e5c0.png)
这种技术叫做进程挖空技术。其中启动一个处于挂起状态的进程，在本例中是恶意软件本身。然后在挂起的进程中分配内存，并将 shellcode 写入该内存。最后将映像基址更改为 shellcode 的起始地址，进程从挂起状态恢复。现在它将从注入的 shellcode 开始执行
可以直接将shellcode提取出来，单独分析。
再看下沙箱：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d747e3b7c06e742fca9e332de6df87aa8585991a.png)
该第二阶段恶意程序在注册表下创建了一个值为`ratotpvvsmo.exe`的值，在run位置创建的注册表项值可以实现恶意程序的持久化。
ratotpvvsmo.exe
===============
第三阶段和第二阶段在初始化执行的是相同的操作：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-689c71d710b39e36d5f5da48b38b003874e586e4.png)
从另一个加密资源中提取数据并解密，在这里应该还有一个shellcode。
同样的操作将shellcode提取出来。
第四阶段
====
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-80ce55343cdf56777186d745a26d4d7af782a59b.png)
第四阶段是一个.NET库的DLL文件，还加了Eazfuscator保护器。
dnSpy打开效果如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-aa124f68e4ed1fc4d02a4d447b0bc144a219b57c.png)
将其解混淆可以得到：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a820c01dda7fc036afcb3d81cf4400348cf8026a.png)
提取配置文件
------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f0085d6576952510c33338008c36d83897a6a0da.png)
`smethod\_16` 是一个静态方法，用于加载和提取可执行文件的资源数据。
调用 `FindResourceEx`寻找资源，使用 `LoadResource` 加载查找到的资源，返回资源句柄。`LockResource` 获取资源的内存地址。这里的目的是读取加密资源的前四个字节，从加密资源中获取四个字节的解密密钥。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-14d36d4e81f828bfceddb0019d2d1420cc793193.png)
它还用于使用指定的 `Guid` 和 `Rfc2898DeriveBytes` 类生成加密密钥，然后使用 `RijndaelManaged` 类解密输入的字节数组。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-745db7902494f802c28ae616b67bbbb161fc974c.png)
`RijndaelManaged` 是AES的实现。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2d8220eac4b18cdb53c31c8c53674984ba267208.png)
在这里实现了资源的加载，下断点可以得到该恶意程序解密配置文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-90a96c9700b80a9cfce94d6d55a0fe93e9762f61.png)
动态调试可以看到，解密后的RAT配置：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2b41a7951d4e12240b089323eed76def9001d724.png)
该恶意软件根据上述配置文件调整其设置，然后执行 RAT 配置中提供的一系列步骤。然后它继续创建互斥锁，从注册表中查询机器 GUID，并在 %appdata% 中创建一个包含机器 GUID 值的文件夹。此文件夹是恶意软件的主要工作目录。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1b0483604b1a6ce279b2ce45a2f502fc24c4b316.png)
之后会在系统中创建一个`run.dat`文件。它获取当前日期时间并将这些值作为字节保存在`Run.dat`文件中。这可能被用作特定系统中感染开始时间的指标。
解析字符串
-----
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-dc494549e0e138c7e6ebb286f5a8cfa0f706a554.png)
恶意软件在运行过程中动态解析字符串，以规避检测。其结构中包含了基于 \*\*LOL bins\*\*（Living Off the Land 二进制文件）的预定义名称和路径值。通过在运行时组合这些值，恶意软件能够伪装其恶意文件和进程，使其看起来像 Windows 的本机二进制文件，从而降低被发现的风险。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5d443414409a0f662dd82fdbb088064c522ffed0.png)
在上面的截图中，可以看到恶意软件从可用的结构中选择了`DNS Monitor`和`dnsmon.exe`。
解析C2
----
恶意软件通过动态配置所有必要设置，解析其 C2 服务器的域名和端口号以建立连接。解析出的端口号为 \*\*2502\*\*，C2 服务器的地址为 \*\*stonecold.ddns.net\*\*。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7d4b98d20f911c4d532c3be548cd184298799195.png)
在代码中，`0x9C6` 的十进制值正好对应 \*\*2502\*\*。
恶意软件会创建一个异步套接字并尝试建立连接。由于其代码结构动态化，相关参数值是从不同的方法调用中获取的。一旦建立连接，恶意程序会持续向 C2 服务器以异步方式发送心跳消息，以维持通信。
当前，因 C2 服务器已关闭，恶意软件的后续执行停止。
使用互联网模拟器，我们可以通过模拟 C2 服务器处于活动状态来欺骗恶意软件。然而，恶意软件包含某种身份验证机制，在创建套接字之前会等待服务器的特定响应。这里使用 Netcat 监听指定端口，发现恶意软件持续发送心跳数据包，如以下截图所示：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5e908ef92e16cc344c7171d640b88afea7a7a7f6.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-e571541466538f2b853e919f446c87ba81102fec.png)
通过分析，可以确认 C2 服务器使用的是一个 DuckDNS 域。DuckDNS 是一项免费动态 DNS 服务，允许域名绑定到不断变化的 IP 地址，主要用于合法用途，如远程访问设备。然而，攻击者也可以滥用此服务，将其用于恶意软件的命令与控制 (C2) 通信。攻击者选择 DuckDNS 的原因包括隐藏 C2 服务器的实际位置、保持匿名、规避检测，并能够快速应对域名或服务器被封禁的情况。

* 发表于 2024-12-26 09:00:02
* 阅读 ( 2921 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![友人Aaaaaaaaaa](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/36845)

[友人Aaaaaaaaaa](https://forum.butian.net/people/36845)

5 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![友人Aaaaaaaaaa](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---