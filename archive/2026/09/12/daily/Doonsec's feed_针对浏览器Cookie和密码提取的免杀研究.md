---
title: 针对浏览器Cookie和密码提取的免杀研究
url: https://mp.weixin.qq.com/s/aakytY07y_hxVuL3-v8P1Q
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:15.987307
---

# 针对浏览器Cookie和密码提取的免杀研究

# 针对浏览器Cookie和密码提取的免杀研究

原创

渊龙Sec安全团队
渊龙Sec安全团队

渊龙Sec安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 微信公众号：**渊龙Sec安全团队**
> 为国之安全而奋斗，为信息安全而发声！
> 如有问题或建议，请在公众号后台留言
> **如果你觉得本文对你有帮助，欢迎在文章底部赞赏我们**

### 1# 概述

**本文首发于国家网络空间安全云社区，作者AabyssZG**

在实战攻防对抗的过程中，面对的不仅仅只有服务器，还有内网海量的个人主机。而浏览器又作为个人主机重要的日常工作、运维以及娱乐的软件，保存了许多重要网站凭据（如堡垒机、云管理平台、企业面板、OA后台等）。

在实际内网渗透过程中，拿到个人主机的权限（如钓鱼、域控下发）后，个人主机大部分还无法操控鼠标（无RDP服务且会引发目标警觉）以及安装终端防护软件，如何无痕实现针对浏览器中保存的Cookie和账户密码的提取和还原，便成为内网渗透必不可少的一环。

最近就有一个黑暗大门的群友找到我，表示最近在内网渗透过程中，有个重要的凭据存在运维的浏览器中，而目标账号密码又有2FA验证，只能提取Cookie尝试，而该机器上面又安装了EDR，尝试寻找并魔改了一些开源项目都被EDR拦截，想要找我来实现这一个目的。

接到这一个需求后，我自己也在逐步摸索，最终我通过Golang搞定了：**BrowserDataOut** 是一套面向 Chromium 系浏览器（Chrome、Edge、Brave、Opera、360、QQ 等）数据取证/恢复的 Windows 工具链，由三个独立可编译的 Go 项目组成。

| 项目 | 角色 | 一句话说明 |
| --- | --- | --- |
| `BrowserKeysDump` | 采集密钥 | 在目标机器上导出浏览器主密钥（v10/v20）为 `keys.json` |
| `BrowserDataCopy` | 采集数据 | 浏览器运行期间复制被独占锁定的 `Cookies`、`Login Data` 等关键文件 |
| `BrowserDataRestore` | 离线解密 | 用 `keys.json` 在任意机器上解密复制的数据，输出分类 JSON |

**本项目已经提供给不少群友用作测试，目前已经能够稳定在多个杀软和EDR环境下开展作业，如360、火绒、深信服EDR等等。**

三个项目**解耦、可独立运行**，通过统一的数据格式（`keys.json` + archive 目录布局）无缝衔接，形成一条完整链路：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eOCmtcHlOA5NLYddpmZbVibuKEKlFSOYicXkiaDDbcKiaMt7MT9A6NXzQhFeBzmfV8JME1sOFYLYtVeMiaE2SbduCLeBmicI0zx2T5bDSDuiaM0zPc/640?wx_fmt=jpeg&from=appmsg)

核心思想是 **"密钥与数据分离采集，解密在任意机器完成"**：

1. 密钥（v10 DPAPI / v20 ABE）都绑定在原机器上，必须在原机器导出；
2. 数据文件（SQLite / JSON）可能被运行中的浏览器独占锁定，需要用特殊手段复制出来；
3. 解密只依赖"密钥 + 数据"，两者同源即可在分析机离线完成。

本项目工具涉及的技术栈如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eOCmtcHlOA7yxGYoTuXWwngNOrjzwicEADXVaIKOfqFlQAH5sr35tv03BFuhDBhvet2nFaaFlrQvtc8WedCyfmVygFBOolmmkTh3P0mescicQ/640?wx_fmt=png&from=appmsg)

**注：本文为笔者在实战过程中写出的随笔，部分思维导图和技术结论出自Kimi大模型，如有错误或者疏漏，欢迎各位师傅指正！**

### 2# BrowserKeysDump：如何拿到密钥

以Chromium为内核的浏览器会把 Cookie、密码、支付信息等敏感数据写入本地SQLite文件（如 `Cookies`、`Login Data` ），在这些SQLite文件的 `encrypted_value` 字段前，会加 3 字节前缀 `v10` 或 `v20`，表示后面这段密文是用哪套 os\_crypt 方案加密的。真正的密钥则放在用户数据目录下的 `Local State`（JSON 文件）的 `os_crypt` 字段里：

* v10 → `os_crypt.encrypted_key`
* v20 → `os_crypt.app_bound_encrypted_key`（以 `APPB` 开头）

Chrome 80 之后全面转向 v10，Chrome 127（2024 年 7 月）起在 Windows 上引入 v20，即 **App-Bound Encryption（应用绑定加密）**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eOCmtcHlOA6Oic45lwpqhZgfRcL2F8sgcIpLgIgkxPyx8jiavAlIgGoLzahrBGRGbSHA6DYhh2sg0ibW6Z4oOuyvWpvOk4xwEIGWic8M7hoia8gY/640?wx_fmt=png&from=appmsg)

v10/v11/v20密钥的区别如下：

| 版本 | 载体 | 加密算法 | 绑定范围 | 用途 |
| --- | --- | --- | --- | --- |
| `v10` | `Local State` 中 `os_crypt.encrypted_key`，前缀 `DPAPI` | DPAPI（Windows 用户密钥） | Windows 用户/机器 | 密码、Chrome <127 的 Cookie |
| `v11` | Linux 下 keyring 派生 | AES-128-CBC | Linux 用户会话 | Linux 密码（本工具为 Windows 专用，不处理） |
| `v20` | `Local State` 中 `os_crypt.app_bound_encrypted_key`，前缀 `APPB` | App-Bound Encryption（浏览器进程内 `IElevator` COM 解密） | 浏览器安装（Chrome 127+） | Chrome/Edge 127+ 的 Cookie |

浏览器把加密字段以统一格式存储：

## 2.1 v10密钥：DPAPI 解密

**数据层**：统一是 AES-256-GCM（AEAD），密文布局为 `v10 ‖ 12字节nonce ‖ 密文+16字节GCM校验tag`，base64 后入库。

**密钥层**（各平台不同）：

* **Windows**

  ：`encrypted_key` 是 base64("DPAPI" + DPAPI加密后的32字节随机key)，用当前用户的 `CryptUnprotectData` 解出主密钥。
* **macOS**

  ：主密钥存在 Keychain 的 "Chrome Safe Storage" 条目里。
* **Linux**

  ：优先走 GNOME Keyring / KWallet，取不到时回退到固定参数：口令 `"peanuts"` + 盐 `"saltysalt"`，PBKDF2-HMAC-SHA1 迭代 1 次派生 16 字节 key，用 **AES-128-CBC** 加密（这是 v10 在 Linux 上的特殊之处）。

**漏洞本质**：DPAPI 只把数据绑定到"机器 + 用户"，**不区分同用户下的进程**——任何以你身份运行的程序都能调 `CryptUnprotectData` 把 key 解出来，这也是各种 cookie 窃取工具的惯用路径。

Chromium 把主密钥放在 `Local State` 的 `os_crypt.encrypted_key` 中，外层由 Windows DPAPI 保护：

```
// 去掉 "DPAPI" 前缀后交给 Windows CryptUnprotectData 解密
func decryptDPAPI(ciphertext []byte) ([]byte, error) {
    var out dataBlob
    r, _, err := procCryptUnprotectData.Call(
        uintptr(unsafe.Pointer(newBlob(ciphertext))),
        0, 0, 0, 0, 0,
        uintptr(unsafe.Pointer(&out)),
    )
    if r == 0 {
        return nil, fmt.Errorf("CryptUnprotectData: %w", err)
    }
    defer procLocalFree.Call(uintptr(unsafe.Pointer(out.pbData)))
    return out.bytes(), nil
}
```

* 结果是一个 **32 字节 AES-256 主密钥**；
* DPAPI 由当前 Windows 用户主密钥解密，**换机器/换用户即失效**——这正是密钥必须在目标机器导出的原因。

## 2.2 v20密钥：App-Bound Encryption 与反射式注入

v20 的数据体仍然是 AES-256-GCM，**变化在密钥的获取链条**：

1. 从 `Local State` 取出 `app_bound_encrypted_key`，去掉 `APPB` 头；
2. 先用 **SYSTEM 权限的 DPAPI** 解一层（这一层由 SYSTEM 身份运行的 Google Update 提升服务完成，并用 chrome.exe 路径哈希作为 entropy，把密钥"焊死"在官方安装路径上），再用**当前用户DPAPI**解第二层；
3. 解出的尾部结构为 `[Chrome安装路径][1字节flag][12B IV][32B 密文][16B tag]`，按 flag 选算法再解一刀，得到最终 32 字节主密钥：

* flag=1：AES-256-GCM，key 硬编码在 `elevation_service.exe`；
* flag=2：ChaCha20-Poly1305，同样硬编码；
* flag=3（v137+）：用 CNG 里的 `"Google Chromekey1"` 解出后 XOR 硬编码常量；

1. 拿到主密钥后，解密 cookie 本体与 v10 完全相同。

Chrome 127+ 的 Cookie 使用 ABE：`app_bound_encrypted_key` ，只能由**浏览器进程内**的 `IElevator` COM 服务解密。工具的做法是把自己的 payload 注入浏览器进程代劳：

```
func injectPayload(exePath string, payload []byte, env map[string]string) ([]byte, error) {
    // 1. 解析 payload 的 PE 导出表，定位 Bootstrap 函数偏移
    loaderRVA, _ := findExportFileOffset(payload, "Bootstrap")

    // 2. 预填 payload 的导入地址槽（LoadLibraryA/GetProcAddress/VirtualAlloc/...）
    writeAddr(impLoadLibraryAOffset, addrLoadLibraryA())
    writeAddr(impGetProcAddressOffset, addrGetProcAddress())
    // ...

    // 3. 以挂起方式启动浏览器（临时 --user-data-dir 隔离）
    pi, _, _ := spawnSuspended(exePath)

    // 4. 把 payload 写入浏览器进程内存（RWX）
    remoteBase, _ := writeRemotePayload(pi.Process, patched)

    // 5. 恢复主线程，等待初始化后远程执行 Bootstrap
    windows.ResumeThread(pi.Thread)
    time.Sleep(500 * time.Millisecond)
    runAndWait(pi.Process, remoteBase, loaderRVA, defaultWait)

    // 6. 从 scratch 区读回 32 字节主密钥
    result, _ := readScratch(pi.Process, remoteBase)
    return result.Key, nil
}
```

Payload 与注入器的"通信协议"是 payload 镜像开头的 scratch 区：

```
偏移     字段
0x28     marker
0x29     status (0x1 = keyStatusReady)
0x2a     errCode
0x2c     hResult (COM)
0x30     comErr
0x40     32 字节主密钥
```

`readScratch` 一次 `ReadProcessMemory` 读 56 字节（`0x28`→`0x60`）即可拿到状态与密钥。

## 2.3 ABE 注入深度细节

**payload 导入地址槽（编译期约定，注入前预填）**：

| 偏移 | 槽位 |
| --- | --- |
| `0x40` | `LoadLibraryA` |
| `0x48` | `GetProcAddress` |
| `0x50` | `VirtualAlloc` |
| `0x58` | `VirtualProtect` |
| `0x60` | `NtFlushInstructionCache` |

注入器在本进程用 `kernel32`/`ntdll` 的 `LazyProc.Addr()` 解析这些 API 的真实地址，写入 payload 镜像后再 `WriteProcessMemory`，这样 payload 进入远程进程后无需系统加载器即可调用。

**Payload 错误码与 HRESULT 对照**：

```
errCode: 0x1 basename 提取失败    0x2 浏览器不在 com_iid 表
         0x3 环境变量缺失/超长     0x4 base64 解码失败
         0x5 SysAllocString 失败  0x6 CoCreateInstance 失败
         0x7 IElevator.DecryptData 失败  0x8 密钥长度 != 32

hResult: 0x80004002 E_NOINTERFACE        0x80010108 RPC_E_DISCONNECTED
         0x80040154 REGDB_E_CLASSNOTREG  0x80070005 E_ACCESSDENIED
         0x800706BA RPC_S_SERVER_UNAVAILABLE
```

**进程生命周期管理**：

* `spawnSuspended`

  ：命令行 `"" --user-data-dir="<临时目录>"`，`CREATE_SUSPENDED` 启动，用临时 `User Data` 避免污染真实配置；
* 注入 `RWX` 内存（`MEM_COMMIT|MEM_RESERVE` + `PAGE_EXECUTE_READWRITE`）**这是 EDR 最敏感的信号之一**；
* 恢复主线程后等 500 ms（让浏览器完成基础初始化），再 `CreateRemoteThread` 执行 `Bootstrap`，`WaitForSingleObject` 默认 30 s；
* 等待超时且进程仍存活（`STILL_ACTIVE=259`）时，日志提示"目标存活，疑似 EDR/AV 拦截"；
* 结束后 `TerminateProcess` + 2 s 等待，`defer` 兜底清理远程进程与临时目录。

**PE 解析要点**：

* `detectPEArch`

  ：读 `0x3c` 处 PE 签名偏移，校验 `PE\0\0`，按 `machine` 字段区分 `0x8664`(amd64) / `0x014c`(386)，只接受 amd64；
* `findExportFileOffset`

  ：PE32+ 可选头从 `peOff+24` 开始，`DataDirectory[0]`（导出表）在可选头偏移 112；遍历节表做 RVA→文件偏移；
* 一个隐蔽细节：`rva - sectVA + sectRaw` 必须**保持 uint32 运算**——当 `rva &lt; sectVA` 时靠 uint32 回绕得到正确结果，拆成 `int` 运算会得到天文数字。

### 3# BrowserDataCopy：如何复制被锁定的文件

以Chromium为内核的浏览器运行的时候，无法直接通过外部脚本或程序复制 `Cookies` 等浏览器数据文件，最核心的原因是对其本地数据库施加了**独占式文件锁（Exclusive File Lock）**。

> 独占式进程锁（File Locking）：Chrome 的 Cookie 和历史记录等数据本质上是SQLite数据库。当浏览器启动时，它会作为主进程打开这些文件，并对文件施加**独占锁**。此时，Windows、macOS 或 Linux 的操作系统底层会保护该文件，禁止其他进程进行读取、修改或复制（报错通常为 `PermissionError`、文件被占用或无法复制）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eOCmtcHlOA6REfzvDXM1M5SkvRicumzSYpShyjIexyyJpGbU2R5G18BemQ5f3fXQd8dDg6CYzrU4EAk3quVHw5X5cFdHPAMsxX1RxPk7JqMo/640?wx_fmt=png&from=a...