---
title: 【2026春节】解题领红包【10.Windows 高级题 11.MCP 中级题】WP 通杀
url: https://mp.weixin.qq.com/s/Cs-RJ99lPvUW45hQmtkNpQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:22.434307
---

# 【2026春节】解题领红包【10.Windows 高级题 11.MCP 中级题】WP 通杀

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aV8UF5rUbwdv5XiciavlNQrAk3dUL5Iicicgnq9Nm4cbo3ORXNu7L8cxnQJT06vmhDDeuO2PpTVU3D9mPKgK4lJZHZStsBFpSMTBsAaUEaJvC7M/0?wx_fmt=jpeg)

# 【2026春节】解题领红包【10.Windows 高级题 11.MCP 中级题】WP 通杀

原创

吾爱pojie
吾爱pojie

吾爱破解论坛

![]()

在小说阅读器中沉浸阅读

作者**论****坛账号：jingtai123**

## 题外话

不得不说，现在的AI能力真的吓人，大部分题目解题都是分析出思路，慢慢调教AI，最终解出flag，前两道题直接粘汇编代码AI秒出答案。最后这两道题就很离谱，用的gpt5.3-codex掉进了很多坑，都是一步一步慢慢调教爬出来，海量token尝试后的结果。以下内容是AI总结，大家看个热闹。

## 【2-9】https://www.52pojie.cn/thread-2094529-1-1.html

## 【春节】解题领红包之十 {Windows 高级题} 出题老师：Poner

### 0x00 前言

本题的关键不是“改比较常量”或“硬改全局变量”，而是还原**真实校验链**。
最终结论：`UID` 对应的正确输入 `flag` 是一段 `128` 位 hex 字符串（64 字节），不是 `0x373f37f2`。

---

### 0x01 结论先行

`UID=551842` 的正确 flag：

```
 复制代码 隐藏代码
1da343dd7ce595876e7af7a5bbd885ed8003ad427e8cfcaa615bb85b00143b52369df87be613639a293536bc6340e798a8e503fe9e6d7eeaa6c799f5561bdc5b
```

---

### 0x02 误区澄清

很多分析会盯住这个点：

* `0x14001f746: cmp r8d, 0x373f37f2`

这只是最终逻辑中的一个常量比较点，**不是用户直接输入值**。
把 `0x373f37f2` 直接当 flag（十进制/十六进制字符串）会失败。

---

### 0x03 Verify 按钮事件与分支条件（静态）

核心状态机在：

* `0x140004df0`

  （`seg_4df0_5f00_annot.txt`）

关键调用点：

* `0x599a: call [0x14014c6d8]`

  -> 实际指向 `0x1400cd490`
* `0x5a05: call [0x14014c6f8]`

  -> 实际指向 `0x1400cd490`

与校验结果直接相关的全局变量：

* `g420 = [0x142632420]`
* `g424 = [0x142632424]`

关键写点：

* 失败路径：`0x5bf0/0x5bfa`、`0x5c3d/0x5c47` 写成 `g420=4, g424=0`
* 成功路径：`0x5c63/0x5c72`、`0x5cc0/0x5ccf` 写成 `g420=3, g424=al`

也就是：`cd490` 链返回为真时，`al=1` 会被写入 `g424`，之后走成功消息路径。

---

### 0x04 真正的校验链（静态）

从 `0x1400cd490` 开始，主链路为：

1. `cd490 -> cf090`
2. `cf090 -> cf270`
3. `cf270`

   通过后 `cd490 -> cf910`
4. `cf910 -> fd790`
5. `cf910 -> d3b20`
6. `cf910 -> cfb10`

对应关键地址：

* `cd490`

  ：`0x1400cd490`
* `cf090`

  ：`0x1400cf090`
* `cf270`

  ：`0x1400cf270`
* `cf910`

  ：`0x1400cf910`
* `fd790`

  ：`0x1400fd790`
* `d3b20`

  ：`0x1400d3b20`
* `cfb10`

  ：`0x1400cfb10`

#### 4.1 `cf090`：输入 flag 的 hex 解码

在 `cf090` 内可见对字符范围判断与 nibble 拼接：

* 支持 `0-9`, `a-f`, `A-F`
* 两个 hex 字符解一个字节

结论：用户输入应是 hex 字符串。

#### 4.2 `cf270`：长度约束

在 `cf270` 中可见：

* `cmp rsi, 0x40`
* `sete byte ptr [rsp + 0x23]`

结论：解码后长度必须是 `0x40`（64 字节）。

#### 4.3 `cf910`：调用 `fd790` 生成期望数据，再调用 `d3b20`

关键调用点：

* `0x1400cfa6e: call 0x1400fd790`
* `0x1400cfa85: call 0x1400d3b20`
* 调用参数：`rcx = user_bytes_ptr`, `rdx = expect_buf_ptr`, `r8d = 0x40`

#### 4.4 `d3b20`：比较核心与返回值

在 `d3b20` 中可见逐字节处理块（如 `0x44a0` / `0x5253`）以及尾部返回判定：

* `0x1400d5a33: cmp byte ptr [rsp+7], 0`
* `0x1400d5a38: sete byte ptr [rsp+0xf]`
* `0x1400d5b23: movzx eax, byte ptr [rsp+0xf]`

结论：`[rsp+7] == 0` 时返回 `1`，即比较通过。

---

### 0x05 动态取证（最小 hook）

为避免重侵入，仅 hook：

* `d3b20`

  入口/返回
* `0x1f746`

  比较点
* `0x55f00`

  验证结果点

#### Stage 1：输入 `00*64`

在 `d3b20` 入口抓到：

* `user_bytes`

  = 我们输入解码后的 64 字节（全 0）
* `expect_bytes`

  = 程序运行时生成的 64 字节（关键）
* `d3_ret = 0`
* `verify_result = 0`

#### Stage 2：把 `expect_bytes` 原样作为输入 flag

再次调用后：

* `d3_ret = 1`
* `verify_result = 1`
* `g420=3, g424=1`

  （见 `callprep_probe.log`）

即证实该 `expect_bytes` 正是 UID 对应正确 flag 的还原结果。

---

### 0x06 脚本实现

#### 6.1 solve\_uid551842.py（核心取证脚本）

```
 复制代码 隐藏代码
import ctypes
import json
import os
import subprocess
import time
from ctypes import wintypes
from pathlib import Path

import frida

TARGET = str(Path("Q10_upxdec.exe").resolve())
LOG = Path("solve_uid551842.log")

user32 = ctypes.WinDLL("user32", use_last_error=True)
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

deflog(obj):
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

defenum_windows(pid: int):
    out = []

    @EnumWindowsProc
    defcb(hwnd, _):
        p = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(p))
        if p.value == pid and user32.IsWindowVisible(hwnd):
            cls = ctypes.create_unicode_buffer(256)
            user32.GetClassNameW(hwnd, cls, 256)
            title_len = user32.GetWindowTextLengthW(hwnd)
            title = ctypes.create_unicode_buffer(title_len + 1)
            user32.GetWindowTextW(hwnd, title, title_len + 1)
            out.append((hwnd, cls.value, title.value))
        returnTrue

    user32.EnumWindows(cb, 0)
    return out

deffind_main_window(pid: int):
    for hwnd, cls, _ in enum_windows(pid):
        if cls == "52PoJie_CrackMe_2026":
            return hwnd
    ws = enum_windows(pid)
    return ws[0][0] if ws elseNone

JS = r"""
const base = Process.enumerateModules()[0].base;
const prep = new NativeFunction(base.add(0x60770), "uint8", ["pointer", "pointer", "pointer"]);

let seq = 0;
let captured = false;

function emit(o, data) {
  o.seq = ++seq;
  send(o, data);
}

function readHex(ptr, n) {
  let s = "";
  for (let i = 0; i < n; i++) {
    const v = ptr.add(i).readU8();
    s += ("0" + v.toString(16)).slice(-2);
  }
  return s;
}

Interceptor.attach(base.add(0x00d3b20), {
  onEnter() {
    const n = this.context.r8.toUInt32();
    if (n === 0x40 && !captured) {
      captured = true;
      try {
        emit({ type: "user_bytes", n: n, hex: readHex(this.context.rcx, n) });
      } catch (e) {
        emit({ type: "user_bytes_err", err: String(e) });
      }
      try {
        emit({ type: "expect_bytes", n: n, hex: readHex(this.context.rdx, n) });
      } catch (e) {
        emit({ type: "expect_bytes_err", err: String(e) });
      }
    }
  },
  onLeave(ret) {
    emit({ type: "d3_ret", al: ret.toUInt32() & 0xff });
  }
});

Interceptor.attach(base.add(0x001f746), {
  onEnter() {
    emit({ type: "cmp", r8d: this.context.r8.toUInt32() });
  }
});

Interceptor.attach(base.add(0x0055f00), {
  onEnter() {
    emit({ type: "verify_result", edx: this.context.rdx.toUInt32() });
  }
});

rpc.exports = {
  run(hwnd, uid, flag) {
    const pu = Memory.allocUtf16String(uid);
    const pf = Memory.allocUtf16String(flag);
    return prep(ptr(hwnd), pu, pf);
  }
};
"""

defprobe_once(uid: str, flag_hex: str, wait_s: float = 2.0):
    proc = subprocess.Popen([TARGET])
    pid = proc.pid
    log({"type": "probe_start", "pid": pid, "uid": uid, "flag_len": len(flag_hex)})
    sess = None
    events = []
    out = {
        "uid": uid,
        "flag_hex": flag_hex,
        "expect_hex": None,
        "user_hex": None,
        "cmp_values": [],
        "verify_values": [],
        "d3_ret": [],
    }
    try:
        hwnd = None
        for _ inrange(100):
            hwnd = find_main_window(pid)
            if hwnd:
                break
            time.sleep(0.05)
        ifnot hwnd:
            raise RuntimeError("main window not found")
        log({"type": "probe_hwnd", "pid": pid, "hwnd": int(hwnd)})

        sess = frida.attach(pid)
        script = sess.create_script(JS)

        defon_message(msg, data):
            if msg.get("type") != "send":
                events.append({"raw": msg})
                return
            payload = msg.get("payload", {})
            events.append(payload)
            t = payload.get("type")
            if t in ("expect_bytes", "user_bytes"):
                hx = payload.get("hex")
                ifisinstance(hx, str) and hx:
                    if t == "expect_bytes":
                        out["expect_hex"] = hx
                    else:
                        out["user_hex"] = hx
            elif t == "cmp":
                out["cmp_values"].append(int(payload.get("r8d", 0)))
            elif t == "verify_result":
                out["verify_values"].append(int(payload.get("edx", 0)))
            elif t == "d3_ret":
                out["d3_ret"].append(int(payload.get("al", 0)))

        script.on("message", on_message)
        script.load()
        log({"type": "probe_frida_loaded", "pid": pid})
        log({"type": "probe_run_enter", "pid": pid})
        ret = int(script.exports_sync.run(int(hwnd), uid, flag_hex))
        log({"type": "probe_run_leave", "pid": pid, "ret": ret})
        out["prep_ret"] = ret

        deadline = time.time() + wait_s
        while time.time() < deadline:
            if out["verify_values...