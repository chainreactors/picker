---
title: 【银行逆向百例】17Android逆向之libDexHelper梆梆加固frida检测绕过
url: https://mp.weixin.qq.com/s/LxbfK28ZoSZg5hbJ5qGfHA
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:48:05.696433
---

# 【银行逆向百例】17Android逆向之libDexHelper梆梆加固frida检测绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vRTpz13XcLibN0DPOv0BsPJ5R5fEd3AJ5ln5uomwEjyF1ocI5bypWPsHcMsicLicavkVWw5rFWZibw5WyNHR69Rmz9eaqRlHQgKNssQtD0AKMuA/0?wx_fmt=jpeg)

# 【银行逆向百例】17Android逆向之libDexHelper梆梆加固frida检测绕过

原创

挖个洞先
挖个洞先

挖个洞先

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**“** 你拥有的一切都过期了，你热爱的一切都旧了，所有你曾经嘲笑过的，你变成他们了。——《Forever Young》 **”**

01

—

环境版本

环境：

电脑，Windows 11 专业版 23H2

```
https://github.com/JiaoSuInfoSec/JiaoSuInfoSec_T00ls_Win11
```

软件：

Florida，16.1.8

```
https://github.com/Ylarod/Florida/releases/tag/16.1.8
```

02

—

操作步骤

1、梆梆加固企业版

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL976had4JiaibibKTTib37ibJx6C5JXjEslRxfiaaIXG0QpricA1vxA5Cic74Ug9ra7FVxDicIf4pZtCeIVYHBjrCCMJJ2hOGhMOyLUMgl4/640?wx_fmt=png&from=appmsg)

2、使用florida 16.1.8

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLibXeLgk2xThqQB8hCcja6vTnDuz4N4TzpyYdOWDUKu5h9sKzAa0JxIHrTnaoXVNgH4BE97DU0F5ANALw3XomDm9Uzh6uTIq70g/640?wx_fmt=png&from=appmsg)

3、进入APP首页一段时间后frida崩溃

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9iad51praLTE0mJ5jWYAu0xTRibKoW4sOnh3QnFkbvuDEBzuDqwjYZTc4KHdBnOEclShQ3yo0OIVe197m5judbIBVH4JibYjxo7g/640?wx_fmt=png&from=appmsg)

4、定位崩溃点在libDexHelper.so

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9tiaZZPTaPVghmIibconRm3N6kD8RVia8Aq35gU17lZvysj2KOZr9Fe6f9Vwrvib1v58U7j0W81QQwuDeH7ib9RocDrSk06s563DCQ/640?wx_fmt=png&from=appmsg)

```
/** * trace-exit.js * * 通用 Android native 崩溃诊断脚本 * * 只做三类记录： * 1. 加载链记录 * 2. JNI 注册链记录 * 3. 崩溃现场记录 * * 不做： * - 返回值修改 * - 内存 patch * - 目标样本定制 * - “疑似模块/关键帧”推断 * * 用法： *   frida -U -f <package> -l trace-exit.js * * RUNBOOK： * 1. 第一次跑，先用 PRESET = "startup" *    看最后加载了哪些 so，以及 JNI 初始化是否开始 * * 2. 如果怀疑崩在 JNI 注册链，切 PRESET = "jni" *    看 FindClass / RegisterNatives / GetMethodID * * 3. 如果只想看最终崩溃点，切 PRESET = "crash" *    重点看 fault 类型、native 栈、Java 栈 * * 4. 如果想长时间采集并离线分析，切 PRESET = "json" *    然后把输出重定向到文件 * * 常用配置： * - PRESET = "default" *   默认通用模式，保留完整功能 * * - PRESET = "startup" *   快速看启动链，只看 LOAD / JNI / CRASH 摘要 * * - PRESET = "jni" *   重点看 JNI 注册链和相关调用栈 * * - PRESET = "crash" *   只看崩溃相关 native / Java 栈 * * - PRESET = "json" *   用 JSON 行输出，适合落盘和后处理 * * 手动细调： * - CONFIG.mode = "summary" *   只输出 LOAD / JNI / CRASH 摘要，适合先粗看启动过程 * * - CONFIG.mode = "verbose" *   输出完整 native / Java 调用栈，适合深入定位崩溃现场 * * - CONFIG.logAllDlopen = true *   打印所有 so 加载路径；默认只重点打印 /data/ 下的 so * * - CONFIG.logAllFindClass = true *   打印所有 FindClass 的 native 栈；默认只对 com/ 类名展开 * * - CONFIG.logAllMethodLookups = true *   打印 GetMethodID / GetStaticMethodID 的 native 栈 * * - CONFIG.printJavaStack = false *   关闭 Java 栈输出，减少日志量 * * - CONFIG.printRecentContextOnEveryEvent = true *   每次事件都输出最近上下文；默认只在 CRASH 场景展开 * * - CONFIG.outputFormat = "json" *   每行输出一个 JSON 对象，方便落盘和后处理 * * - CONFIG.eventAllowlist = ["LOAD", "CRASH"] *   只输出指定类型的日志；留空表示不过滤 * * - CONFIG.eventBlocklist = ["HOOK"] *   屏蔽指定类型的日志；在 allowlist 之后生效 * * - CONFIG.showHookRegistrationLogs = false *   关闭启动时的 HOOK 注册日志，减少初始化噪音 * */"use strict";const DEFAULT_PRESET = "default"; // default | startup | jni | crash | jsonconst PRESET = (typeof globalThis !== "undefined" && globalThis.TRACE_EXIT_PRESET)    ? String(globalThis.TRACE_EXIT_PRESET)    : DEFAULT_PRESET;const BASE_CONFIG = {    mode: "verbose", // "summary" | "verbose"    outputFormat: "text", // "text" | "json"    eventAllowlist: [],    eventBlocklist: [],    showHookRegistrationLogs: true,    maxFrames: 24,    maxJavaFrames: 24,    maxRecentEvents: 80,    maxRecentLoads: 30,    recentContextCount: 8,    maxStringLength: 160,    dedupWindowMs: 800,    logAllDlopen: false,    logAllFindClass: false,    logAllMethodLookups: false,    printJavaStack: true,    printRecentContextOnEveryEvent: false,    dumpNativeStackOnLoad: true,    dumpNativeStackOnJniRegister: true,    dumpJavaStackOnLoad: true,    classPrefixesForStack: ["com/"],    libraryPrefixesForStack: ["/data/"]};const PRESET_OVERRIDES = {    default: {},    startup: {        mode: "summary",        eventAllowlist: ["LOAD", "JNI", "CRASH"],        eventBlocklist: ["HOOK"],        showHookRegistrationLogs: false,        printJavaStack: false,        dumpJavaStackOnLoad: false    },    jni: {        mode: "verbose",        eventAllowlist: ["JNI", "CRASH", "JAVA_STACK"],        eventBlocklist: ["HOOK", "LOAD", "INFO"]    },    crash: {        mode: "verbose",        eventAllowlist: ["CRASH", "JAVA_STACK"],        eventBlocklist: ["HOOK", "LOAD", "JNI", "INFO"],        showHookRegistrationLogs: false    },    json: {        mode: "summary",        outputFormat: "json",        eventBlocklist: ["HOOK"],        showHookRegistrationLogs: false,        printJavaStack: false,        dumpJavaStackOnLoad: false    }};function buildConfig(preset) {    const override = PRESET_OVERRIDES[preset] || PRESET_OVERRIDES.default;    return Object.assign({}, BASE_CONFIG, override);}const CONFIG = buildConfig(PRESET);const SCRIPT_VERSION = "1.0.0";const JSON_SCHEMA_VERSION = "1.0";const SESSION_ID = Date.now().toString(16) + "-" + Math.random().toString(16).slice(2, 8);const SESSION_START_MS = Date.now();let gRecentEvents = [];let gRecentLoads = [];let gJavaReady = false;let gLastEventTimes = Object.create(null);let gEventSeq = 0;let gPackageName = "";let gEventCounts = Object.create(null);function now() {    return new Date().toISOString();}function uptimeMs() {    return Date.now() - SESSION_START_MS;}function formatUptime(ms) {    return "+" + String(ms) + "ms";}function emitJsonEvent(type, payload) {    const event = Object.assign({        schema: "trace-exit",        schemaVersion: JSON_SCHEMA_VERSION,        scriptVersion: SCRIPT_VERSION,        preset: PRESET,        sessionId: SESSION_ID,        packageName: gPackageName,        processId: Process.id,        processName: Process.name,        processArch: Process.arch,        processPlatform: Process.platform,        threadId: Process.getCurrentThreadId(),        seq: ++gEventSeq,        ts: now(),        uptimeMs: uptimeMs(),        type: String(type)    }, payload || {});    console.log(JSON.stringify(event));}function log(msg) {    if (CONFIG.outputFormat === "json") {        emitJsonEvent("LOG", {            message: String(msg)        });        return;    }    console.log("[" + now() + "][" + formatUptime(uptimeMs()) + "] " + msg);}function shouldEmitType(type) {    const t = String(type || "LOG");    if (t === "HOOK" && !CONFIG.showHookRegistrationLogs) {        return false;    }    if (CONFIG.eventAllowlist.length > 0 && CONFIG.eventAllowlist.indexOf(t) === -1) {        return false;    }    if (CONFIG.eventBlocklist.indexOf(t) !== -1) {        return false;    }    return true;}function logType(type, msg) {    if (!shouldEmitType(type)) {        return;    }    if (CONFIG.outputFormat === "json") {        emitJsonEvent(type, {            message: String(msg)        });        return;    }    log("[" + type + "] " + msg);}function isVerbose() {    return CONFIG.mode === "verbose";}function summarizeConfig() {    return {        version: SCRIPT_VERSION,        preset: PRESET,        sessionId: SESSION_ID,        packageName: gPackageName,        processArch: Process.arch,        processPlatform: Process.platform,        pageSize: Process.pageSize,        mode: CONFIG.mode,        outputFormat: CONFIG.outputFormat,        printJavaStack: CONFIG.printJavaStack,        showHookRegistrationLogs: CONFIG.showHookRegistrationLogs,        dumpNativeStackOnLoad: CONFIG.dumpNativeStackOnLoad,        dumpNativeStackOnJniRegister: CONFIG.dumpNativeStackOnJniRegister,        dumpJavaStackOnLoad: CONFIG.dumpJavaStackOnLoad,        eventAllowlist: CONFIG.eventAllowlist,        eventBlocklist: CONFIG.eventBlocklist,        classPrefixesForStack: CONFIG.classPrefixesForStack,        libraryPrefixesForStack: CONFIG.libraryPrefixesForStack    };}function truncateString(value) {    if (value === null || value === undefined) {        return "";    }    const s = String(value);    if (s.length <= CONFIG.maxStringLength) {        return s;    }    return s.substring(0, CONF...