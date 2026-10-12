---
title: Telegram桌面版惊现IPC注入漏洞，点击链接即可被完全劫持账户
url: https://mp.weixin.qq.com/s/tmJOJYPh4E2Tr8TdDJn8pA
source: Doonsec's feed
date: 2026-10-11
fetch_date: 2026-10-12T08:13:16.911683
---

# Telegram桌面版惊现IPC注入漏洞，点击链接即可被完全劫持账户

# Telegram桌面版惊现IPC注入漏洞，点击链接即可被完全劫持账户

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

## 引言

想象这样一个场景：有人把你拉入了一个Telegram群聊。群里突然出现一个链接，你出于好奇点击了它。就在这一刻，你的Telegram账户已经不再完全属于你一个人了。

这究竟是如何发生的？

Telegram桌面版的设计存在一个致命缺陷：当用户点击链接时，程序会通过本地套接字将链接内容以文本形式传递给自己已在运行的另一个实例进程。问题的关键在于，传递过程中程序从未对作为命令分隔符的关键字符进行转义处理。这意味着，一个精心构造的恶意链接在接收端不会被解析为单个指令，而会被拆解成多个独立指令执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZia6FsfagYVpzFJiawWicUYIqibjokH8IUA2lcTAdScto114zSicz4EGTC5Ylibm3Ir6IJUk7BHghA6EA15w9LiatwibksauOVQiaZTEGwY/640?wx_fmt=png&from=appmsg)

我发现这个攻击链条包含两大核心缺陷。第一个是**命令注入漏洞本身**。第二个则是**注入命令所触发的内部机制**——一个名为`interpret:`的内部URI方案。这个方案的功能极为危险：它能根据指令文件的内容，直接读取磁盘上的指定文件并将其发送到聊天频道中，整个过程既不对请求方进行身份验证，也不向用户请求任何确认。这两种缺陷结合，就能将一次简单的链接点击转变为任意文件读取操作。在本文中，我将详细拆解整个攻击链条，并演示如何利用它窃取受害者的登录凭据文件。

| **受影响版本** | 确认受影响的Telegram桌面版至7.2.8，在Windows平台(6.9.3)已验证该漏洞 |
| --- | --- |
| **漏洞影响** | **远程任意本地文件读取** ，文件可被外泄至攻击者控制的聊天环境；**账户完全接管** |
| **CVE编号** | CVE-2026-107181 |
| **修复版本** | 7.2.9版本，修复提交为`db3405699f` |
| **严重等级** | **8.1(高危)** ，CVSS评分：`CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N` |

## 一个链接的背后：双重进程机制

现代操作系统允许应用程序注册特定的URI协议方案。当操作系统遇到这类链接时，就知道应该启动哪个程序来处理。Telegram桌面版注册了`tg://`这一协议。从此以后，系统就将所有`tg://...`开头的链接识别为Telegram专属，并以该链接URL作为命令行参数启动对应的应用程序。

**场景一：Telegram未运行**如果Telegram尚未启动，操作系统会创建一个新进程，将链接字符串作为参数传入。新进程内部将其解析为URL对象并处理——单个进程，无需任何进程间通信。

**场景二：Telegram已在运行**这时操作系统根本不知道也不检查程序是否已在运行：它仍然会启动一个与当前实例完全相同的全新进程。Telegram必须自己判断是不是"多余"的实例，而它判断的方法就是尝试连接**本地套接字**。

已在运行的实例充当服务器角色：从启动起就一直监听该套接字。新启动的进程则作为客户端。如果新进程能够成功连接套接字，说明已有实例存活，于是新进程会将接收到的链接转交给服务端进程，然后自行退出。这正是单实例应用程序的典型设计。

但这里埋下了一个隐患：套接字传输的是原始字节流，而非内存对象。新进程持有的URL对象无法直接跨越进程边界传输，必须**序列化**为一串文本。

**序列化**是将内存中的数据结构转换为字节流的过程；**反序列化**则是其逆过程。每当结构化数据需要跨越进程边界时，这两种操作都不可避免。但正是在这个转换的关键点上，数据内部的结构边界不再由程序员定义的逻辑结构决定，而是变成了文本中的**普通字符**——这就是危险的开始。

Telegram设计了一套极其简单的序列化格式：每条指令由"关键字+参数+分号"组成。例如，要打开一个链接会转换为：

```
OPEN:tg://x?a=1;
```

示例中的`tg://x?a=1`在Telegram内部没有任何处理程序，因此这个链接自身不执行任何操作——它只是一个载体。

这行文本在如下代码中生成，每个需要打开的URL都会生成一条：

```
// sandbox.cpp:295-297
for (const auto &url : cRefStartUrls()) {
    commands += u"OPEN:"_q + url.toString(QUrl::FullyEncoded) + ';';
}
```

在接收端，服务端实例进行反序列化：读取接收到的字节，在**每一个分号处**进行切割，然后将每个片段作为独立指令处理。对于每个以`OPEN:`开头的片段，提取后续内容并重建为URL对象——就好像这个URL刚从命令行传入一样：

```
// sandbox.cpp:453-463 (简化版)
for (int32 to = cmds.indexOf(QChar(';'), from); to >= from; ...) {
    auto cmd = base::StringViewMid(cmds, from, to - from);
    ...
    } else if (cmd.startsWith(u"OPEN:"_q)) {
        startUrls.append(cmds.mid(from + 5, to - from - 5).mid(0, 8192));
```

## 未转义的分隔符：致命的设计缺陷

那么问题来了：如果传输的数据本身包含了格式所使用的分隔符——分号——会发生什么情况？

让我们修改之前的示例链接，在其中添加一些内容：

```
tg://x?a=1;CMD:quit
```

对于新启动的客户端进程来说，这个链接是一个完整的URL，其中的分号只是查询参数中的普通字符。客户端将其序列化后写入套接字：

```
OPEN:tg://x?a=1;CMD:quit;
```

但服务端进程的处理逻辑完全不同：它在**每个分号处**进行切割，结果得到了两个独立的指令：

```
OPEN:tg://x?a=1
CMD:quit
```

这就是**命令注入**攻击，也是整个攻击链的第一个核心缺陷。

## interpret:协议方案——危险的内部机制

上面的例子中，我们注入了`CMD:`指令，但不要被这个名字迷惑：它只接受`show`和`quit`两个参数，所以最坏的情况也仅仅是关闭应用程序而已。

实际上Telegram总共接受四种命令，其中三种相对无害。真正关键的是第四个命令：`OPEN:`。这里有个重要细节：**它接受任何URL，而且不对协议方案进行过滤**。

深入分析源代码后，我发现了Telegram内部还存在一个名为`interpret:`的私有URI方案。

操作系统当然不知道如何处理`interpret:`开头的链接，因为它根本没有作为协议处理器注册过。这个方案只存在于Telegram自己的代码逻辑中，程序会像对待其他URL一样从启动URL列表中提取并处理它：

```
// application.cpp:1162-1164
if (url.scheme() == u"interpret"_q) {
    interprets.append(url.path());
    return false;
```

这意味着通过`OPEN:`指令，攻击者可以访问到这个内部机制：

```
tg://x?a=1;OPEN:interpret:instructions.txt
```

那么`interpret:`协议究竟是用来做什么的？

原来这是Telegram官方用于发布自身新版本的工具。每当新版本构建完成后，构建脚本需要将发布包发送到官方频道，并在消息中附上更新日志。为了避免手动操作，Telegram开发团队编写了一个自动化脚本：生成一个包含发布指令的小型文本文件，然后通过命令行参数启动Telegram并传入该文件的路径。

```
# Telegram/build/updates.py:206
subprocess.call(... 'Telegram -sendpath interpret://' + scriptPath
    + '/.../command.txt', shell=True)
```

典型的指令文件格式如下：

```
from: 1234567890
channel: 1987654321
file: out/Release/deploy/6.9.3/tsetup.6.9.3.exe
caption: TDesktop at 12.06.26:

- Fixed a crash in the media viewer.
- Added a new sticker pack.
```

其中`from:`一行会将当前登录账户ID与指定值对比，防止操作人员用错误的账号发布版本。但关键是：**只有当这一行存在时才会进行验证**，如果省略这一行就能完全绕过账户检查。`channel:`指定目标频道（必须是频道或超级群组），`file:`指定要发送的文件路径。

这一切功能都由`InterpretSendPath`函数实现。

那么真正的bug在哪里？`interpret:`协议执行的是**特权操作**：从磁盘读取任意文件并直接发送到聊天频道，整个过程既不需要用户确认，也不验证请求者的身份。

该函数根本**没有进行任何授权检查**：

```
// support_helper.cpp:673-680
QString InterpretSendPath(
        not_null<Window::SessionController*> window,
        const QString &path) {
    QFile f(path);
    if (!f.open(QIODevice::ReadOnly)) {
        return "App Error: Could not open interpret file: " + path;
    }
    const auto content = QString::fromUtf8(f.readAll());
```

从开发团队内部使用的角度来看（通过命令行调用），这似乎不是大问题：攻击者需要先在目标机器上获得立足点才能利用。但**一旦这个功能可以通过套接字访问**——也就是可以通过之前描述的注入漏洞触发——危险程度就完全不同了：一个高度敏感的功能现在可以通过受害者点击的任意链接来调用。

这就是**授权机制的缺失**，也是整个攻击链的第二个核心缺陷。

## 让指令文件落地：攻击者的布局策略

如果攻击者能够在受害者磁盘上放置一个指令文件，将`file:`指向想要窃取的文件路径，将`channel:`指向自己控制的群组，那么只需受害者点击一个链接，攻击者就能从目标机器外泄任意文件。

那么攻击者如何才能在他人的磁盘上以**可预测的路径**放置一个文本文件呢？最直接的方法就是将其作为聊天附件发送。

Telegram桌面版有一项默认设置：在群聊中接收的**不超过8MB的文件会自动下载**（广播频道中则是关闭的）。文件会被保存到标准下载文件夹，保持发送者设定的原始文件名。而且这个过程是**可预测的**（如果文件名冲突，Telegram会自动保存为类似`instructions1 (2).txt`的文件名）。请注意：像贴纸、GIF和语音消息等格式会进入内部缓存，无法直接通过文件路径访问。

Telegram自动生成的下载路径（参考`file_utilities.cpp:172-181`代码），在Windows系统上的格式为：

```
C:\Users\<用户名>\Downloads\Telegram Desktop\<文件名>
```

通过将文件发送到群聊，攻击者就能精确知道文件会被保存在哪里。路径中看似有一个未知因素：Windows用户名。但`interpret:`协议**也支持相对路径**，而相对路径是相对于Telegram的**工作目录**（即其数据文件夹，参考`logs.cpp:381`代码）解析的。

在Windows上，Telegram数据文件夹路径为`%APPDATA%\Telegram Desktop`，位于用户主目录下三层。而`Downloads`文件夹直接位于用户主目录中。因此，攻击者可以使用如下相对路径：

```
interpret:../../../Downloads/Telegram%20Desktop/instructions.txt
```

这样攻击者就获得了**完全确定性的路径**，根本不需要知道用户名。

## 从文件读取到账户完全接管

`InterpretSendPath`函数每次调用只发送一个文件：如果指令文件中包含多个`file:`行，只有最后一行生效。但有两个因素可以突破这个限制：

* 攻击者可以随意发布任意数量的指令文件
* 注入攻击不会在第一个命令后停止：每个分号都会开启一个新指令

因此，要窃取三个目标文件，只需要三个指令文件和单个链接中的三个堆叠命令：

```
tg://x?a=1
  ;OPEN:interpret:../../../Downloads/Telegram%20Desktop/instructions1.txt
  ;OPEN:interpret:../../../Downloads/Telegram%20Desktop/instructions2.txt
  ;OPEN:interpret:../../../Downloads/Telegram%20Desktop/instructions3.txt
```

整个过程中的核心技术原理保持不变：**任意文件读取**。真正变化的是读取的内容：可以是SSH私钥、浏览器密码库、云端凭据文件，或者包含API令牌的配置文件。

Telegram不会以明文存储本地数据，用户存储在磁盘上的所有内容都是加密的，包括**会话授权信息**。这个授权信息类似于网站的会话cookie，是客户端向Telegram服务器证明身份的关键凭证。拥有了它，就等于完全拥有了这个账户。

### Telegram的密钥包装机制

Telegram采用密钥包装技术保护用户数据。涉及两个层次的密钥：

1. **DEK(数据加密密钥)**：长、随机、高熵值，用于直接加密用户数据
2. **KEK(密钥加密密钥)**：只用于加密DEK，**不是用户密码**；它通过密钥派生函数(KDF)从用户密码（加上存储在加密DEK旁边的盐值）派生而来

用伪代码描述数据解密过程如下：

```
salt, encrypted_DEK = read("tdata/key_datas")
passcode            = user_passcode()          # 如果未设置本地密码则为空

KEK     = KDF(passcode, salt)
DEK     = decrypt(encrypted_DEK, KEK)
session = decrypt(authorization_file, DEK)
```

关键点来了：Telegram桌面版**默认不设置本地密码**，用户需要主动在设置中启用。如果未设置，用于派生KEK的密码就是空字符串，而盐值以明文形式与加密的DEK一起存储在`tdata/key_datas`文件中。

因此，在没有设置本地密码的情况下，**只要获取`key_datas`文件，就能重新计算出KEK并解锁DEK**，从而解密所有其他数据，包括会话授权。

### 必须窃取的关键文件

完整的账户接管需要涉及三个关键文件，其中只有两个包含真正的秘密：

```
tdata/
├── key_datas                 # 盐值和加密的DEK（核心密钥材料）
├── D877F783D5D3EF8Cs         # 使用DEK加密的MTProto授权（会话凭证）
└── D877F783D5D3EF8C/
    └── maps                  # 账户存储数据的索引（不包含秘密，但为完整性需要）
```

注意：文件夹名称`D877F783D5D3EF8C`不是随机的，也不是安装特定的。它由默认数据名称"data"派生而来（参考`storage_file_utilities.cpp:241-250`代码），在**所有安装中都是相同的**。

第三个文件（maps）只是一个索引，并不包含秘密信息。不过，没有它会话就无法加载：Telegram只在读取该索引时才读取授权信息。但攻击者也可以选择自己构建这个索引文件。在本文的概念验证中，为了简便，直接窃取所有三个文件。

最终结论是：持有这三个文件的攻击者就完全控制了该账户——将它们放入一个新的`tdata`文件夹，启动Telegram，受害者的会话就会顺利打开。

## 链接传递策略：巧妙的攻击入口

这个攻击需要受害者的一次点击，关键是**点击必须来自Telegram外部**。因为在Telegram聊天内部点击的`tg://`链接是在**进程内处理**的（参考`click_handler_types.cpp:278`代码），永远不会经过套接字传输，也就没有注入的机会。

而普通的`https://`链接会在**系统默认浏览器**中打开（参考`ui_integration.cpp:437`代码），因为Telegram桌面版没有内置浏览器。这就给了攻击者可乘之机：发送一个看似普通的HTTPS链接，然后用自己的服务器将其**重定向**到精心构造的...