---
title: Frida 恶意软件分析实战教程
url: https://mp.weixin.qq.com/s/ZriA9hCWHtsFx9Uw-imm3g
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:17:04.315840
---

# Frida 恶意软件分析实战教程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/I4ibOKsL0MdC4xlOGJjtC9AZPCQcmbxwqmxWy4kic53XUTXJXqDzEo4DlzviaiacNToG5nCqVkoSh66ic4L9OiaYV1dZCCxdZXB6Z6ROHRhs04wm0/0?wx_fmt=jpeg)

# Frida 恶意软件分析实战教程

埃里克之旅
埃里克之旅

SOC安全分析之旅

![]()

在小说阅读器中沉浸阅读

## 一、为什么用 Frida 分析恶意软件？

传统静态分析面对加壳、混淆、动态加载等对抗手段时往往力不从心。**Frida** 作为动态插桩工具，可以在恶意软件运行时实时拦截 API 调用、解密数据、绕过反分析机制，是恶意软件分析师的核心武器之一。

**Frida 在恶意软件分析中的典型用途：**

* 🔍 **行为监控**：Hook 关键 API，观察文件操作、网络通信、注册表修改等行为
* 🔓 **动态脱壳**：在运行时 dump 解密后的 payload
* 🔑 **密钥提取**：拦截加密函数，提取密钥和明文数据
* 🛡️ **绕过反分析**：绕过反调试、反虚拟机、反 Frida 检测
* 📡 **C2 通信分析**：Hook 网络函数，还原 C2 通信协议

---

## 二、分析环境搭建

### 2.1 隔离沙箱环境

**安全警告**：恶意软件分析必须在隔离环境中进行！切勿在生产机器或联网主机上直接运行恶意样本。

</aside>

**推荐环境：**

| **平台** | **推荐方案** | **说明** |
| --- | --- | --- |
| Windows 恶意软件 | VirtualBox / VMware + Windows 10 虚拟机 | 快照功能方便还原 |
| Android 恶意软件 | Android 模拟器（Genymotion / AVD） | Root 权限 + Frida Server |
| Linux 恶意软件 | Docker / Linux VM | 网络隔离 + 快照 |

**环境搭建要点：**

* [ ] 虚拟机设置为**仅主机网络**（Host-Only）或完全断网
* [ ] 创建干净快照，方便分析后还原
* [ ] 安装 Python 3、pip、adb（如分析 Android）
* [ ] 禁用 Windows Defender 等安全软件（避免干扰分析）

### 2.2 安装 Frida

```
# PC 端安装
pip install frida frida-tools

# 验证版本
frida --version
```

**Windows 目标机额外步骤：** 无需安装 frida-server，Frida 可直接注入本地进程。

**Android 目标机额外步骤：**

```
# 查看架构
adb shell getprop ro.product.cpu.abi

# 下载对应版本 frida-server
# <https://github.com/frida/frida/releases>

adb push frida-server /data/local/tmp/
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"

# 验证
frida-ps -U
```

---

## 三、Windows 恶意软件分析实战

### 3.1 使用 frida-trace 快速行为分析

`frida-trace` 是最快的入门方式，可自动追踪 API 调用：

```
# 追踪文件操作
frida-trace -f malware.exe -i "CreateFile*" -i "WriteFile" -i "ReadFile"

# 追踪网络通信
frida-trace -f malware.exe -i "connect" -i "send" -i "recv" -i "WSA*"

# 追踪注册表操作
frida-trace -f malware.exe -i "RegOpenKey*" -i "RegSetValue*" -i "RegCreateKey*"

# 追踪进程/线程操作
frida-trace -f malware.exe -i "CreateProcess*" -i "CreateRemoteThread" -i "VirtualAllocEx"

# 追踪动态加载（DLL 注入检测）
frida-trace -f malware.exe -i "LoadLibrary*" -i "GetProcAddress"
```

<aside> 💡

`frida-trace` 会自动在 `__handlers__` 目录下生成 JS 处理脚本，你可以编辑这些脚本来自定义输出格式和过滤逻辑。

</aside>

### 3.2 Hook 网络通信 — 还原 C2 协议

```
// hook_c2_network.js
// Hook Winsock send/recv，捕获 C2 通信内容

var sendPtr = Module.findExportByName("ws2_32.dll", "send");
var recvPtr = Module.findExportByName("ws2_32.dll", "recv");
var connectPtr = Module.findExportByName("ws2_32.dll", "connect");

// Hook connect — 获取 C2 地址
Interceptor.attach(connectPtr, {
    onEnter: function (args) {
        var sockAddr = args[1];
        var port = (sockAddr.add(2).readU8() << 8) | sockAddr.add(3).readU8();
        var ip = sockAddr.add(4).readU8() + "." +
                 sockAddr.add(5).readU8() + "." +
                 sockAddr.add(6).readU8() + "." +
                 sockAddr.add(7).readU8();
        console.log("[C2] connect -> " + ip + ":" + port);
    }
});

// Hook send — 捕获外发数据
Interceptor.attach(sendPtr, {
    onEnter: function (args) {
        var buf = args[1];
        var len = args[2].toInt32();
        console.log("[C2] SEND (" + len + " bytes):");
        console.log(hexdump(buf, { length: Math.min(len, 256) }));
    }
});

// Hook recv — 捕获接收数据
Interceptor.attach(recvPtr, {
    onLeave: function (retval) {
        var len = retval.toInt32();
        if (len > 0) {
            console.log("[C2] RECV (" + len + " bytes):");
            console.log(hexdump(this.buf, { length: Math.min(len, 256) }));
        }
    },
    onEnter: function (args) {
        this.buf = args[1];
    }
});
```

**运行：**

```
frida -f malware.exe -l hook_c2_network.js --no-pause
```

### 3.3 Hook 加密函数 — 提取密钥和明文

```
// hook_crypto.js
// Hook Windows CryptoAPI，提取加密密钥和数据

// Hook CryptEncrypt
var cryptEncrypt = Module.findExportByName("advapi32.dll", "CryptEncrypt");
if (cryptEncrypt) {
    Interceptor.attach(cryptEncrypt, {
        onEnter: function (args) {
            this.pbData = args[4];
            this.pdwDataLen = args[5];
            var dataLen = this.pdwDataLen.readU32();
            console.log("\\n[CRYPTO] CryptEncrypt called");
            console.log("[CRYPTO] 明文 (" + dataLen + " bytes):");
            console.log(hexdump(this.pbData, { length: Math.min(dataLen, 256) }));
        },
        onLeave: function (retval) {
            var dataLen = this.pdwDataLen.readU32();
            console.log("[CRYPTO] 密文 (" + dataLen + " bytes):");
            console.log(hexdump(this.pbData, { length: Math.min(dataLen, 256) }));
        }
    });
}

// Hook CryptDecrypt
var cryptDecrypt = Module.findExportByName("advapi32.dll", "CryptDecrypt");
if (cryptDecrypt) {
    Interceptor.attach(cryptDecrypt, {
        onEnter: function (args) {
            this.pbData = args[3];
            this.pdwDataLen = args[4];
        },
        onLeave: function (retval) {
            var dataLen = this.pdwDataLen.readU32();
            console.log("\\n[CRYPTO] CryptDecrypt -> 解密后明文:");
            console.log(hexdump(this.pbData, { length: Math.min(dataLen, 256) }));
        }
    });
}
```

### 3.4 监控文件与持久化行为

```
// hook_persistence.js
// 监控恶意软件的文件创建和注册表持久化行为

// Hook CreateFileW — 文件操作监控
var createFileW = Module.findExportByName("kernel32.dll", "CreateFileW");
Interceptor.attach(createFileW, {
    onEnter: function (args) {
        var fileName = args[0].readUtf16String();
        var accessMode = args[1].toInt32();
        var accessStr = (accessMode & 0x40000000) ? "WRITE" : "READ";
        console.log("[FILE] " + accessStr + ": " + fileName);
    }
});

// Hook RegSetValueExW — 注册表写入监控
var regSetValueExW = Module.findExportByName("advapi32.dll", "RegSetValueExW");
if (regSetValueExW) {
    Interceptor.attach(regSetValueExW, {
        onEnter: function (args) {
            var valueName = args[1].readUtf16String();
            var dataType = args[3].toInt32();
            console.log("[REG] SetValue: " + valueName + " (Type: " + dataType + ")");
            if (dataType === 1 || dataType === 2) { // REG_SZ / REG_EXPAND_SZ
                console.log("[REG] Data: " + args[4].readUtf16String());
            }
        }
    });
}

// Hook CreateProcessW — 子进程创建监控
var createProcessW = Module.findExportByName("kernel32.dll", "CreateProcessW");
if (createProcessW) {
    Interceptor.attach(createProcessW, {
        onEnter: function (args) {
            var appName = args[0].isNull() ? "null" : args[0].readUtf16String();
            var cmdLine = args[1].isNull() ? "null" : args[1].readUtf16String();
            console.log("[PROCESS] CreateProcess:");
            console.log("  App: " + appName);
            console.log("  Cmd: " + cmdLine);
        }
    });
}
```

---

## 四、Android 恶意软件分析实战

### 4.1 动态脱壳 — Dump DEX

许多 Android 恶意软件使用加壳保护，运行时才解密真正的 DEX 文件：

```
// dump_dex.js
// 在运行时 dump 解密后的 DEX 文件

Java.perform(function () {
    var DexClassLoader = Java.use("dalvik.system.DexClassLoader");
    DexClassLoader.$init.implementation = function (dexPath, optDir, libPath, parent) {
        console.log("[UNPACK] DexClassLoader 加载: " + dexPath);
        this.$init(dexPath, optDir, libPath, parent);
    };

    var InMemoryDexClassLoader = Java.use("dalvik.system.InMemoryDexClassLoader");
    InMemoryDexClassLoader.$init.overload("java.nio.ByteBuffer", "java.lang.ClassLoader")
        .implementation = function (buf, parent) {
        console.log("[UNPACK] InMemoryDexClassLoader detected!");
        var remaining = buf.remaining();
        console.log("[UNPACK] DEX size: " + remaining + " bytes");

        // Dump DEX 到文件
        var bytes = Java.array('byte', new Array(remaining).fill(0));
        buf.get(bytes);
        buf.position(0); // 重置 position

        var file = Java.use("java.io.FileOutputStream").$new("/data/local/tmp/dumped_" + Date.now() + ".dex");
        file.write(bytes);
        file.close();
        console.log("[UNPACK] DEX dumped to /data/local/tmp/");

        this.$init(buf, parent);
    };
});
```

### 4.2 Hook SMS / 电话 — 检测间谍软件行为

```
// hook_sms_spy.js
// 检测...