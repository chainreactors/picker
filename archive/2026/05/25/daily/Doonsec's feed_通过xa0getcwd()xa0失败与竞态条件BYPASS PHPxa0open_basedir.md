---
title: 通过xa0getcwd()xa0失败与竞态条件BYPASS PHPxa0open_basedir
url: https://mp.weixin.qq.com/s/TT8zwTTcIhrcl52q9eZP6Q
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:51.534380
---

# 通过xa0getcwd()xa0失败与竞态条件BYPASS PHPxa0open_basedir

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hYTcBbYGXIfoiaibDdYibicCiadPSP14WT5MvIiaDUicAhAzkE642qL9SoyPRTvY0ia2MMfhBcj6L9EMiaRZDqBEPa0RpmDN1oktBiaaAdibsHm1lpNmb4/0?wx_fmt=jpeg)

# 通过 getcwd() 失败与竞态条件BYPASS PHP open\_basedir

d2550自留地

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于ap0s
，作者ap0s

![](http://wx.qlogo.cn/mmhead/X6Ucic5kYIBPrvcibYvOBIPSvniaR6CT6XcV6wPZzntpT1iaH5jPBhkJAPlibZdyFxvqEFX7jj1QECNw/0)

**ap0s**
.

安全小白

# 通过 `getcwd()` 失败与竞态条件BYPASS PHP `open_basedir`

## 摘要

PHP 的 `open_basedir` 机制被设计用来限制文件操作的目录范围，是共享主机和受限环境中一项基础的安全隔离手段。然而在 PHP 8.4 中，当 `getcwd()` 因当前工作目录被删除而返回 `NULL` 时，`ini_set()` 对 `open_basedir` 的动态修改过程存在一个路径检查缺陷。结合目录操作的竞态条件，这个缺陷可以被利用来注入 `../` 路径，突破目录限制，实现任意文件读取。

## 引言

`open_basedir` 是 PHP 提供的一项重要安全配置，旨在限制 PHP 脚本能够访问的文件系统路径。当 `open_basedir` 被激活时，PHP 将限制所有文件系统操作（如 `fopen()`、`file_get_contents()` 等）只能在指定的目录及其子目录中进行，从而有效防止恶意脚本访问服务器上的敏感文件或执行未授权操作。然而，历史上有多种技术曾被用于绕过 `open_basedir` 限制，其中不乏利用 PHP 内部函数处理逻辑缺陷和系统级竞态条件的方法。本文将聚焦于一个近期发现的、利用 `getcwd()` 失败与竞态条件相结合的 `open_basedir` 绕过漏洞，该漏洞在 CODEGATE 2025 CTF 的 Gravelbox 挑战中得到了体现，并已在 PHP 官方 Issue #21961 中得到讨论和修复。我们将详细剖析这一漏洞的技术细节，旨在提高开发者和安全研究人员对此类复杂攻击的认识和防范能力。

### 调试环境

用p神的docker-php环境启动不了,可以用下面的dockerfile

vscode调试环境可以参考：https://hackerqwq.github.io/2021/11/05/vscode%E8%BF%9C%E7%A8%8B%E8%B0%83%E8%AF%95php%E5%BA%95%E5%B1%82%E4%BB%A3%E7%A0%81/#%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE

```
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. 安装 PHP 7.4 所需的特定编译依赖、GDB 以及 SSH 服务
RUN apt-get update && apt-get install -y \
    build-essential \
    autoconf \
    bison \
    re2c \
    pkg-config \
    libxml2-dev \
    sqlite3 \
    libsqlite3-dev \
    libonig-dev \
    libssl-dev \
    gdb \
    openssh-server \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 2. 下载并编译 Debug 版 PHP 7.4（以 7.4.33 最终版为例）
WORKDIR /usr/src
RUN wget https://www.php.net/distributions/php-7.4.33.tar.gz \
    && tar -zxvf php-7.4.33.tar.gz \
    && cd php-7.4.33 \
    && ./configure --prefix=/usr/local/php-debug --enable-debug --enable-cli --with-openssl --enable-mbstring --enable-pcntl \
    && make -j$(nproc) \
    && make install

# 3. 配置 SSH 服务以便 VSCode 远程连接
RUN mkdir /var/run/sshd \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# 4. 写入本地公钥实现免密登录
RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh
COPY public_key.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

# 暴露 SSH 端口
EXPOSE22

# 启动 SSH 服务并防止容器退出
CMD ["/usr/sbin/sshd", "-D"]
#docker exec -it php74-gdb-container sh -c "echo 'root:root123' | chpasswd"
```

`.vscode/launch.json`

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "调试 open_basedir 漏洞",
            "type": "cppdbg",
            "request": "launch",
            "program": "/usr/local/php-debug/bin/php",
            "args": ["${workspaceRoot}/test.php"],
            "stopAtEntry": false,
            "cwd": "${workspaceRoot}",
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                },
                {
                    "description": "fork",
                    "text": "set follow-fork-mode child",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```

注意这里必须启用`--enable-pcntl`

## `open_basedir` 机制与 `getcwd()` 失败原理

PHP 的 `open_basedir` 配置通过限制文件操作的根目录来增强安全性。当 `open_basedir` 被设置时，所有文件系统函数（如 `fopen`, `file_get_contents`, `file_put_contents` 等）都会检查所访问的文件路径是否在允许的目录内。这一检查的核心逻辑位于 PHP 源码中的 `main/fopen_wrappers.c` 文件，特别是 `OnUpdateBaseDir()` 函数和 `expand_filepath()` 函数 [1]。

### `OnUpdateBaseDir()` 函数

`OnUpdateBaseDir()` 函数负责处理 `ini_set('open_basedir', ...)` 运行时对 `open_basedir` 配置的修改。其工作流程大致如下：

1. **路径分割**: 将新的 `open_basedir` 字符串按目录分隔符（Linux 上为 `:`）进行分割，得到多个路径。例如，`open_basedir=/var/www/html:/tmp` 会被分割为 `/var/www/html` 和 `/tmp` [1]。
2. **路径解析与检查**: 对每个分割出的路径，首先调用 `expand_filepath()` 函数将其解析为真实路径（realpath），然后调用 `php_check_open_basedir_ex()` 函数检查该真实路径是否符合当前的 `open_basedir` 策略。只有当新路径比现有设置更具限制性时，才允许修改 [1]。
3. **应用新配置**: 如果所有路径都通过了检查，则将新的 `open_basedir` 配置应用到运行时环境中。

`/usr/src/php-7.4.33/main/fopen_wrappers.c:OnUpdateBaseDir`

`OnUpdateBaseDir` 内部**调用**的是 `php_check_open_basedir_ex`，后者又会调用 `php_check_specific_open_basedir`，这些函数最终都会使用 `expand_filepath_with_mode` 来进行路径解析。

### `expand_filepath()` 与 `getcwd()` 失败

`expand_filepath()` 函数负责将给定的文件路径解析为绝对路径。它会进一步调用 `expand_filepath_ex()`，最终由 `expand_filepath_with_mode()` 完成核心工作。当处理相对路径时，`expand_filepath_with_mode()` 会尝试通过 `VCWD_GETCWD()` 获取当前工作目录（Current Working Directory, CWD），然后将相对路径与 CWD 结合以解析出绝对路径 [1]。

`VCWD_GETCWD()` 是 PHP 对标准 C 库 `getcwd()` 函数的封装。在某些特定情况下，`getcwd()` 函数可能会失败并返回 `NULL`。根据 Linux 手册页，常见的失败原因有两种 [1]：

1. **路径名过长 (ENAMETOOLONG)**: 如果当前工作目录的绝对路径长度超过了系统定义的 `MAXPATHLEN`（在 Linux 上通常为 4096 字节），`getcwd()` 将会失败。攻击者可以通过创建嵌套极深的目录结构来触发此条件。
2. **目录被取消链接 (ENOENT)**: 如果当前工作目录在 `getcwd()` 调用期间被另一个进程删除（即被 `unlink` 或 `rmdir`），`getcwd()` 也会失败。

当 `VCWD_GETCWD()` 失败时，`expand_filepath_with_mode()` 包含一个**回退机制**。它会尝试使用 `VCWD_OPEN()` 函数直接打开相对路径，并让操作系统来解析。如果 `VCWD_OPEN()` 成功，`expand_filepath_with_mode()` 会返回原始的相对路径（例如 `../`），而不是一个完全解析的绝对路径 [1]。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hYTcBbYGXIdeShjpgJNgTfreeglWI3rHrwMpQWfxWhicVAaFCELZ2ukicDXj5drIeFF1G11crhArDCjGBTch8Gy2RCPZLYxYKns97mck2lrsU/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/hYTcBbYGXIeJichmY8NvxdHcDKnPrO4KpYgjKUTdPEHoWPZdvFFfQ4rldkmqyC81zRgr0t0pPKNnWhibkicPb7icefxPAjbml7icWQG0Hjr4PYFA/640?wx_fmt=png&from=appmsg)

**漏洞点**正是出现在这个回退机制中：如果 `VCWD_GETCWD()` 失败，但 `VCWD_OPEN()` 成功，`expand_filepath()` 会返回未解析的相对路径（如 `../`）。此时，`OnUpdateBaseDir()` 会将这个未解析的 `../` 路径与当前的 `open_basedir` 路径进行比较。如果当前 `open_basedir` 允许的路径是 `/var/www/html`，而 PHP 进程的 CWD 位于 `/var/www/html/sub_dir`，那么 `../` 实际上指向 `/var/www/html`，这在逻辑上被认为是“更具限制性”或“在允许范围内”的，从而通过了 `php_check_open_basedir_ex()` 的检查。一旦 `../` 被成功添加到 `open_basedir` 中，攻击者就可以利用它向上遍历目录结构，访问到 `/var/www/html` 之外的文件，例如 `/flag.txt` [1]。

这一漏洞的利用通常需要结合**竞态条件**，以精确控制 `getcwd()` 的失败和 `VCWD_OPEN()` 的成功时机。

### 竞态条件 (Race Condition) 与 TOCTOU

竞态条件（Race Condition）是指两个或多个进程或线程并发执行时，其最终结果取决于这些进程或线程执行的精确时序。在 `open_basedir` 绕过场景中，我们关注的是一种特定的竞态条件，即 **TOCTOU (Time-of-Check-Time-of-Use)** 漏洞 [2]。

TOCTOU 漏洞发生在系统在执行安全检查（Time-of-Check）和实际使用资源（Time-of-Use）之间存在时间窗口时。攻击者可以在这个时间窗口内改变资源的状态，从而绕过安全检查。在本漏洞中，竞态条件体现在以下两个阶段：

1. **检查阶段 (Time-of-Check)**: `OnUpdateBaseDir()` 调用 `expand_filepath()` 来解析路径并进行 `open_basedir` 检查。
2. **使用阶段 (Time-of-Use)**: 如果检查通过，`open_basedir` 的配置被更新，后续的文件操作将使用新的 `open_basedir` 限制。

攻击者可以利用多进程或多线程，在一个进程尝试修改 `open_basedir` 时，另一个进程通过快速重命名或删除目录来干扰 `getcwd()` 的执行，使其失败并触发 `expand_filepath()` 的回退逻辑，从而在 `open_basedir` 中引入 `../`。一旦 `../` 被加入，后续的文件操作就可以利用它来访问父目录甚至根目录下的文件 [2]。

这一漏洞的复杂性在于需要精确的时序控制，以确保在 `getcwd()` 失败和 `VCWD_OPEN()` 成功之间，以及 `open_basedir` 检查和实际文件访问之间，能够插入恶意操作。

---

**PHP `open_basedir` 绕过漏洞核心流程**

![PHP  绕过漏洞核心流程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hYTcBbYGXIeJUCYbouaflPbgCvNjutLfL57l5Tbt04vEIr3ug3qpMx3asHQh7Hhh16L8g8ib6lnfOQaR7UqpZIgA7ZCabKbbl6a5znTcAkHs/640?wx_fmt=webp&from=appmsg)

PHP `open_basedir` 绕过漏洞核心流程

---

## CODEGATE 2025 CTF Gravelbox 挑战分析

### 漏洞利用链

为了绕过 `open_basedir`，攻击者利用了上述的 `getcwd()` 失败与竞态条件漏洞。利用链的核心在于同时运行两个进程，制造 TOCTOU 漏洞：

1. **父进程 (攻击进程)**: 不断尝试通过 `ini_set("open_basedir", $cur_basedir . ":../")` 将 `../` 添加到 `open_basedir` 中。一旦成功，它将尝试读取 `/flag.txt`。
2. **子进程 (干扰进程)**: 不断地在 `/tmp` 目录下重命名一个深层目录（例如，在 `start` 和一长串 `x` 字符之间切换）。

当子进程重命名目录时，如果父进程恰好在执行 `ini_set` 并调用 `getcwd()`，由于目录结构的突然改变（目录被取消链接或路径变得无效），`getcwd()` 会失败。此时，PHP 的回退机制被触发，`VCWD_OPEN()` 成功打开 `../`，导致 `../` 被原样返回并最终通过 `open_basedir` 的检查，成功注入到配置中 [2]。

### PoC 代码解析

```
<?php
chdir("/tmp");

$allowed_path = "/tmp";

@mkdir("start/");
chdir("start/");
$cur_dir = getcwd();
$cur_dir_len = strlen($cur_dir);

// 创建一个极深的目录结构，为触发 getcwd() 失败做准备
$magic_depth = str_repeat(str_repeat("a", 249) . "/", 16 - floor($cur_dir_len / 250));
@mkdir($magic_depth, 0755, true);

chdir($ma...