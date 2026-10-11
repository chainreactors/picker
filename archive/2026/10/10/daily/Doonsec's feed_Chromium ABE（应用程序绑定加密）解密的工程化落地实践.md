---
title: Chromium ABE（应用程序绑定加密）解密的工程化落地实践
url: https://mp.weixin.qq.com/s/mF-3Md7ZOwxkI_trKyPr6A
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:00:25.031269
---

# Chromium ABE（应用程序绑定加密）解密的工程化落地实践

# Chromium ABE（应用程序绑定加密）解密的工程化落地实践

Ratin
Ratin

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Chromium 应用程序绑定（App-Bound Encryption，以下简称ABE）的解密已不是新鲜事，本文将侧重于讨论其在工程上的落地实践，以及分享过程中 AI & Security 的体会。

最终落地一个**无需 UAC 提权**、**无视浏览器独占锁**，读取并解密浏览器数据的可工程化方案，以及对 **Edge/ChatGPT App 的 Chrome 数据导入功能实现分析**。

https://github.com/KNSoft/KNSoft.MakeLifeEasier/tree/main/Source/Samples/AbeDecrypt

PoC: AbeDecrypt Sample: 本文 PoC 示例，演示本文例举的 4 种解密方式，获得 Chrome/Edge 里所选 User Data 的 v10/v20 Key，并显示所选 Profile 解密出来的 Cookie 及密码数据：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K13K17OKUJia07yy7kO0YAOOymQrA6hksuuITBsibuibgpwjOtFPhpczktQM1ric5q5E4ficVUTuLWR6J9nsQm1b2cx5jHGkjGianUIY/640?wx_fmt=other&from=appmsg)

https://github.com/KNSoft/KNSoft.ZPigeon

KNSoft.ZPigeon: 支持读取 Chrome/Edge 浏览器各 Profiles 下的各类数据（含 Cookie、密码）及启动可远程控制的无头浏览器实例：

![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K09JibPjhuIvKsrWicNJJ4vXGUoicMpxkPtuRQKLyWRlb5LiaDyKaLIs2NkRP8sXYh0C5E7KWjURq6I6VBMXjDibJUI70y9GNaxldYc/640?wx_fmt=other&from=appmsg)

##

**背景**

最近在做 KNSoft.ZPigeon，一个 AI 加持的 Windows 远程管理平台。之所以想做，是因为我一直相信鸽子的最终形态会是功能极其强大的企业 IT 管理系统，而今在企业 IT、终端安全、Windows 底层研发与 AI 四个领域的积淀够让我离这个目标更进一步了。

其中功能自然包含浏览器数据的获取，ABE 是最后一关。PoC 虽多，但只是证明“方案可行”，真正落地还要兼顾易用性和效率，并处理多 Profile、浏览器运行中的独占锁、权限要求等实际问题，这也是本文重点。

Chromium 如何加密与保存数据？

相关资料很多，Chromium 本身也开源，所以实现部分以 Chromium/Chrome/Edge 为基线快速梳理机制；关键机制直接说结论，不再大段摘录代码，未开源部分（浏览器私有实现）再额外说明。

### 数据存放

系统预装 Edge 数据存放于 `%LOCALAPPDATA%\Microsoft\Edge\User Data` 目录，Chrome 类似：

* Local State：JSON，存放密钥（非明文）。DPAPI、ABE 的 Key 都在这里
* Default：默认 Profile 目录，同级目录还可能有 Profile 1、Profile 2 等

+ Network\Cookies：SQLite，cookies 表（Cookie，加密）
+ Login Data：SQLite，logins 表（密码，加密）
+ Login Data For Account: SQLite, 同 `Login Data`，但这包含登录浏览器账号存储的密码
+ History：SQLite，历史记录（明文）
+ ...

加密内容如 `Cookies` 库 `cookies` 表的 `encrypted_value` 列、`Login Data` 库 `logins` 表的 `password_value` 列，以 Blob 形式存储：

```
0             3       15                  末尾-16
┌─────────────┬───────┬───────────────────┬───────┐
│ "v10"/"v20" │ nonce │ 密文 ct           │ tag   │
│  3 B        │ 12 B  │ 与明文等长         │ 16 B  │
└─────────────┴───────┴───────────────────┴───────┘
版本号         随机数   AES-256-GCM 输出    防篡改校验
```

其中：

* 版本号：目前 Windows 上只有 v10 和 v20 两种加密方式
* nonce：随机生成 12 字节，每条记录独立、只用一次
* AES-256-GCM(v10/v20 Key, nonce, 明文) 运算（AAD 为空）得到密文 + tag（用于校验）

其中密文要用对应加密版本（v10/v20）的 Key 解密，`Local State` 的 `os_crypt` 节点存放核心密钥：

```
{
"os_crypt":{
"encrypted_key":"<Base64 编码>",
"app_bound_encrypted_key":"<Base64 编码>"
}
}
```

* `encrypted_key`

  Base64(`"DPAPI"` 5 字节前缀 + DPAPI Blob)，Blob 加密保存 v10 Key
* `app_bound_encrypted_key`

  Base64(`"APPB"` 4 字节前缀 + ABE Blob)，Blob 加密保存 v20 Key

去掉开头的前缀后，**根据后面的 Blob 解出对应的 Key 是解密的关键点，下文将对不同加密版本说明这些 Blob 是如何得出的、如何从 Blob 解出 Key**。

而密文用对应加密版本的 Key 解密后，得到的内容则根据业务而定，例如：

* `cookies`

  的 `encrypted_value`：从数据库 Schema 24 起为 SHA256(host\_key) + **cookie 值**，开头的“域名指纹”防止密文被跨站拷贝复用
* `logins`

  的 `password_value`：直接是**密码本身**

v10/v20 加密密钥在 `Local State` 里跨 Profile 共享；记录加密格式与密钥 Envelope 均存在版本迁移，因此新版浏览器中仍可能保留旧版格式。

### 加密版本 v10：DPAPI

Windows CNG DPAPI 是数据保护 API。它只绑定用户，除了系统保存的用户级 Master Key（`%APPDATA%\Microsoft\Protect\<SID>\`），调用者还可以再传入一个可选熵参与加密（Chromium 没有使用可选熵，用了也不见得提升安全系数。

```
加密：CryptProtectData([in] 明文, [in, opt] 可选熵, [out] 密文)
解密：CryptUnprotectData([in] 密文, [in, opt] 可选熵, [out] 明文)
```

**同一登录用户下的任意进程都能解开 v10 Key。**

首次需要加密时生成 v10 Key：

* 生成随机 **32 字节 AES-256 密钥，这就是 v10 Key**
* 调用 `CryptProtectData(v10 Key)` 得到 DPAPI Blob
* 把 `"DPAPI"`（5 字节前缀）拼到 DPAPI Blob 前面，再进行 Base64 编码
* 写入 `Local State` 的 `os_crypt.encrypted_key` 字段

后续根据 `Local State` 的 `os_crypt.encrypted_key` 字段反向运算即可拿到 v10 Key，然后进行加解密。十分简单，几行 PowerShell 就能把 v10 Key 解密并打印出来（以系统内置 Edge 为例）：

```
# 1. 读 Local State，取 encrypted_key，Base64 解码
$blob = [Convert]::FromBase64String((Get-Content "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Local State" -Raw | ConvertFrom-Json).os_crypt.encrypted_key)

# 2. 验证前缀 "DPAPI" 并剥掉，DPAPI 解密
if ($blob.Length -le 5 -or [System.Text.Encoding]::ASCII.GetString($blob, 0, 5) -cne 'DPAPI') { throw 'Invalid encrypted_key: missing DPAPI prefix' }
Add-Type -AssemblyName System.Security
$key = [Security.Cryptography.ProtectedData]::Unprotect($blob[5..($blob.Length-1)], $null, [Security.Cryptography.DataProtectionScope]::CurrentUser)
if ($key.Length -ne 32) { throw "Invalid v10 key length: $($key.Length)" }

# 3. 打印
($key | ForEach-Object { $_.ToString("X2") }) -join ''
```

### 加密版本 v20：ABE（App-Bound Encryption，应用程序绑定加密）

引入 `elevation_service.exe`，注册为**以 SYSTEM 身份执行的系统服务**（如 `GoogleChromeElevationService` / `MicrosoftEdgeElevationService`），开放 COM 接口供浏览器调用，通过 COM 为浏览器封装、解封 v20 Key。

首次需要加密时：

* 浏览器生成随机 **32 字节 AES-256 密钥，这就是 v20 Key**
* 浏览器调用 `IElevator::EncryptData`，把 v20 Key 和“保护级别”（见后文）交给服务
* **服务私有处理，Chromium 源码中目前通过 `GOOGLE_CHROME_BRANDING` 编译器开关控制，如果启用，则调用私有 `PreProcessData`，把原始 v20 Key 转换成私有 Envelope，未来取 Key 时再对等地调用私有 `PostProcessData` 处理。Edge 也有这步，具体见后文**
* 服务模拟客户端（`IServerSecurity::ImpersonateClient`），并取得 **“调用方路径”**（`I_RpcOpenClientProcess` + `QueryFullProcessImageNameW`），把校验数据与 v20 Key （或者转换成的私有 Envelope） 一起在**调用方用户上下文**中执行 DPAPI 加密
* 服务退出模拟，再在 **SYSTEM 上下文**中执行 DPAPI 加密，得到 ABE Blob，返回给浏览器
* 浏览器拼接 `"APPB"` + ABE Blob，Base64 编码后写入 `os_crypt.app_bound_encrypted_key`

后续浏览器通过 `Local State` 的 `os_crypt.app_bound_encrypted_key` 字段拿到 ABE Blob，通过 COM 得到 v20 Key，即可进行加解密。

可见沿用了 Windows CNG DPAPI，并在 SYSTEM 上下文进行验证及加解密操作。

#### Chromium 定义的“保护级别”：

* `PROTECTION_NONE`

  不校验应用身份
* `PROTECTION_PATH_VALIDATION`

  解封时要求当前调用方的规整路径与封装时一致
* `PROTECTION_PATH_VALIDATION_WITH_ISOLATION`

  除路径一致外，还校验进程的隔离状态

默认值是 `PROTECTION_PATH_VALIDATION_WITH_ISOLATION`，即同时校验“调用方的规整路径”和“进程的隔离状态”：

* 调用方的规整路径：

+ 去掉 exe 文件名
+ 去掉末尾的 Temp / Application / 版本号目录
+ 把 `Program Files (x86)` 归一化为 `Program Files`

* 进程的隔离状态：

+ Elevation Service (SYSTEM) 以带有隔离标记（`SetTokenInformation(TokenSecurityAttributes)`，例如 Chrome 的 `GOOGLECHROME://ISOLATION`）的 Token 创建浏览器进程
+ 服务查询调用进程 Token 中是否存在此隔离标记，阻止非隔离客户端读取隔离客户端存储的 Key

虽然默认值指示校验进程的隔离状态，且校验代码确已默认启用，但隔离标记只授予经 Elevation Service 以隔离方式启动的浏览器实例，常规启动的浏览器并不携带。加密时记录的隔离状态为 False，解密时双方一致即可通过，故该校验对普通机器尚无实际约束。即使未来有约束，目测绕过的方式依然很多。当下的关键点，便是过掉路径校验。

#### 私有 Envelope

Chrome 和 Edge 基于 Chromium 预留的扩展都做了近乎相同的私有处理。服务拿到 v20 Key 明文后，先转换成私有 Envelope，再做后续的 DPAPI 加密。Envelope 目前又有 3 个版本：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K2yfoibUEILPkCa5iaI8uia4BTPrOteQs3ibXGe1hu5H14RzI74iaRiao1vjFDHery4CwbiapPzLoLsAIKfOazaMTq76RrVCydTR7rmd8/640?wx_fmt=png&from=appmsg)

v1 与 v2 只是加密算法不同，用的 Key 是固定的，通过二进制逆向可得到：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1Siaz0RLAl2aCWl6y34icQpYYFtyyK8MvwyvicRlNtCyibM0mDFplewR7X17iasINRdS8NIWZfR1CZyLOzgmGgheBMxicPTgpOfNqpk/640?wx_fmt=png&from=appmsg)

v20 Key 的明文直接用以上硬编码 Key 加密得到密文 ct（`ciphertext[32]`），再组合成 Envelope。

而 v3 加入了 CNG。v20 Key 不再被直接加密，而是先随机生成 32 字节的 **Envelope AES Key**：

* Envelope AES Key XOR 一个固定的 32 字节 Mask，再在服务的 SYSTEM 上下文中读取 Windows CNG/KSP 保存的 Key（Chrome 是 `Google Chromekey1`，Edge 是 `Microsoft Edgekey1`）加密，得到 `cng_block[32]`
* v20 Key 用 Envelope AES Key 做 AES-256-GCM 加密，得到 `nonce[12] + ciphertext[32] + tag[16]`

XOR 用的固定 Mask 通过二进制逆向可得到：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3ula5AgWnXslickoJVz4AZb9JpdO6ia7SL9x5PtcUSx0zKcIGPHT16dP5UYfELcq6SpMgezVqx69VLiaibbuResBXtUPQxvf2y8KE/640?wx_fmt=png&from=appmsg)

4 种 v20 解密方案

### 过路径校验

#### 1. Drop：把可执行程序扔进浏览器目录

十分简单直接，既然验证客户端路径，那把程序扔进浏览器目录里路径就对了。我想到要考虑的有：

* 需要管理员权限才能向启用 ABE 的浏览器安装目录丢东西（Per-User 安装的浏览器 ABE 也用不了），例如 Windows 内置的 Edge
* 缺少技术上的纵深

+ “进程的隔离状态”或者未来的防御手段可以轻易防住
+ EDR 特征明显，且文件监控极其容易实现

#### 2. Inject：注入到浏览器进程

DLL 注入对大家来说已是基操，但 DLL 也不是注入必需的，Map + `CreateRemoteThread` 就够了。将自身代码映射到浏览器进程，然后用远端线程执行它。

* 无需管理员权限
* EDR 特征明显

#### 3. Hijack：劫持浏览器进程执行代码

这条路线可以说是 Inject 方案的升级版，思路一致，无非是把代码（调用 Elevation Service 接口进行解密）放到浏览器进程空间里执行。只是用 `CreateProcess` + Map，主线程代替远端线程，归并为一个方案也不为过。

如果想做得足够优雅，还是比较考验技术的。xaitax/Chrome-App-Bound-Encryption-Decryption 是一个值得参考的例子，我在 KNSoft.ZPigeon 中落地的方案也算是 Hijack。

EDR 特征仍然明显，但劫持的方式太多了，看是道高一尺还是魔高一丈。

### 调用 Elevation Service COM 接口 `DecryptData`

过掉路径校验后，问题就是如何调用 Elevation Service 接口。接口定义可以参考 Chromium 的 `e...