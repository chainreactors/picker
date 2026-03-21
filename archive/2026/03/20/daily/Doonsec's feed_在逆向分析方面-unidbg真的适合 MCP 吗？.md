---
title: 在逆向分析方面-unidbg真的适合 MCP 吗？
url: https://mp.weixin.qq.com/s/cdewcQvzitbRVtW-Dzeh2g
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:02:48.722024
---

# 在逆向分析方面-unidbg真的适合 MCP 吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1ZFDomJSIUawThEsOaXSJ9IUEBIPOXtDXqFzGFc3kfQHGGIC0Uqq0OFZz1y3pP8P08xnpSJjbvymTBC2SlSAbuHK6YNniaickpo/0?wx_fmt=jpeg)

# 在逆向分析方面-unidbg真的适合 MCP 吗？

执着的猫
执着的猫

看雪学苑

![]()

在小说阅读器中沉浸阅读

**一、引言**

# MCP（Model Context Protocol）是当下 AI 工具链的热门话题。当 unidbg 社区引入 MCP 功能后，不少人觉得这是个好方向——让 AI 直接操作调试器，下断点、读内存、单步执行，听起来很美好。

#

事实上，在 unidbg 官方加入 MCP 之前，笔者就已经尝试过给 unidbg 做 MCP 接入。结果发现问题比想象中多得多，最终放弃了这条路线，转而采用 Claude Code 的 Skill（自定义命令）机制来辅助逆向分析。

本文记录这个过程中的思考和踩坑，探讨为什么 unidbg 这类模拟器场景下，MCP 可能并不是最佳选择。

**二、我们最初想做什么**

2.1 理想中的 MCP

设想是这样的：unidbg 启动后暴露一组 MCP 工具，AI 可以：

1. 读写内存和寄存器
2. 下断点、单步执行
3. trace 指令和内存访问
4. 反汇编、搜索内存模式

逆向工程师只需要对话："帮我看看这个函数第三个参数指向什么结构体"，AI 自动下断点、读数据、推理分析。

### 2.2 unidbg 官方的实现

后来 unidbg 官方确实做了这件事——一个完全自研的 HTTP+SSE 服务器（约 2600 行代码），暴露了 50+ 个调试工具：

* **内存操作：read\_memory、write\_memory、search\_memory**
* **寄存器操作：get\_registers、set\_register**
* **代码分析：disassemble、assemble、patch**
* **断点管理：add\_breakpoint、add\_breakpoint\_by\_offset**
* **执行控制：continue\_execution、step\_over、step\_into**
* **追踪：trace\_code、trace\_read、trace\_write**
* **函数调用：call\_function、call\_symbol**

实现得很完整，本质上是一个**AI 驱动的 GDB**。

但当我们把它放到实际的逆向分析工作流中一评估，就发现了一系列结构性问题。

**三、第一道坎：补环境——MCP 完全无法介入**

### 3.1 unidbg 补环境是什么

用过 unidbg 的人都知道，让一个 SO 跑起来最痛苦的不是逆向分析本身，而是**补环境**——手动模拟 SO 依赖的所有 Java/Android 环境。

unidbg 不是真机，它只模拟 ARM CPU。当 native 代码通过 JNI 回调 Java 层时，unidbg 会抛出异常告诉你："这个 JNI 方法我不认识，你得自己写 mock。"

### 3.2 真实的补环境过程

这是一个典型的循环：

```
运行 → 崩溃: "callObjectMethodV not implemented: okhttp3/Interceptor$Chain->request()"
→ 补上这个 mock → 重新编译运行
→ 崩溃: "callObjectMethodV not implemented: okhttp3/Request->url()"
→ 补上这个 mock → 重新编译运行
→ 崩溃: "callObjectMethodV not implemented: okhttp3/HttpUrl->toString()"
→ ...（重复 20-30 次）
```

一个典型的网络请求签名 SO，最终需要 mock 的 JNI 接口清单可能是这样的：

```
// 网络库调用链
"okhttp3/Interceptor$Chain->request()"
"okhttp3/Request->url()"
"okhttp3/Request->method()"
"okhttp3/Request->headers()"
"okhttp3/Request->body()"
"okhttp3/Request->newBuilder()"
"okhttp3/Request$Builder->addHeader()"
"okhttp3/Request$Builder->build()"
"okhttp3/HttpUrl->toString()"
"okhttp3/HttpUrl->encodedPath()"
"okhttp3/HttpUrl->encodedQuery()"
"okhttp3/Headers->size()"
"okhttp3/Headers->name()"
"okhttp3/Headers->value()"

// IO 缓冲区
"okio/Buffer-><init>()"
"okio/Buffer->writeString()"
"okio/Buffer->readByteArray()"
"okio/Buffer->clone()"
"okio/Buffer->read()"

// Android 系统 API
"android/content/Context->getSharedPreferences()"
"android/content/SharedPreferences->getString()"

// 文件系统模拟
"/proc/self/status"  → 需要伪造 TracerPid: 0（反调试）
"/proc/self/cmdline" → 需要返回正确的包名

// 总计可达 200-300 行 Java mock 代码
```

每个 mock 还不是简单返回 null 就行。比如`SharedPreferences->getString()`需要根据 key 返回特定的值（密钥、配置等），`Headers->name()/value()`需要维护一个完整的请求头列表并按索引返回。有些 mock 之间还有状态依赖——`Buffer->writeString()`写入的数据，后面`Buffer->readByteArray()`要能读出来。

### 3.3 为什么 MCP 处理不了补环境

MCP 的工具集全部是**运行时调试工具**——read\_memory、set\_register、add\_breakpoint 等等。

但补环境需要的是：

**1. 修改 Java 源码**

MCP 没有任何工具能编辑`.java`文件。当 SO 崩溃在一个未实现的 JNI 方法上时，你需要在继承`AbstractJni`的测试类里加一个`case`分支。这是纯粹的代码编辑操作，不是调试操作。

**2. 触发编译**

改完代码后需要`mvn compile`或 IDE 增量编译。MCP 不接入构建系统。

**3. 读取编译/运行报错**

unidbg 的报错信息打印在 Java 的 stdout/stderr 上，不是在调试器控制台里。MCP 看不到这些输出。

**4. 理解 JNI 语义**

补环境不仅是"返回一个值"，还需要理解 SO 期望的语义。

比如：

```
// SO 调用 chain.proceed(request) 期望拿到 Response
// 如果返回 null，后续代码就 NPE 了
// 必须返回一个合法的 Response mock
case "okhttp3/Interceptor$Chain->proceed(Lokhttp3/Request;)Lokhttp3/Response;":
return responseClass.newObject(null);
```

这需要理解 OkHttp 的 API 设计，不是简单的内存读写能解决的。

**5. 反复重启**

补环境的循环是"改一个 mock → 重启整个模拟器 → 看下一个报错"。每次都是完整的进程生命周期。MCP 连接的是一个运行中的调试会话，一旦进程结束，MCP 会话也就断了。

### 3.4 这个阶段真正需要的是什么

需要的是一个能**读报错→改代码→触发编译→重新运行**的循环。这恰好是 AI 代码编辑工具（Claude Code、Cursor 等）的核心能力，而不是 MCP 调试工具的能力。

**四、第二道坎：算法还原中的试错**

### 4.1 hook 点经常选错

SO 跑通后进入逆向分析阶段。核心工作是"下断点捕获数据→验证算法假设"。

但 hook 点经常选错，这是常态：

1. 先 hook 地址 A → 发现第一次调用时寄存器指向的数据是空的
2. 改成只看第二次调用 → 发现数据格式不对
3. 换一个地址 B → 发现是解密后的数据，已经过了密钥设置阶段
4. 回头换地址 C → 终于拿到正确的数据

最终写出来的代码可能是这样的：

```
debugger.addBreakPoint(module.base + 0xABCDE, new BreakPointCallback() {
intcallCount =0;
@Override
public booleanonHit(Emulator<?> emulator, long address) {
if (callCount == 0) {  // 只在第一次调用时捕获
RegisterContextctx = emulator.getContext();
longx2 = ctx.getLongArg(2);
byte[] keyCtx = emulator.getBackend().mem_read(x2, 0xF0);
// 解析轮密钥...
        }
        callCount++;
return true;
    }
});
```

### 4.2 MCP 的致命问题：不可回溯

```
AI: add_breakpoint(地址A) → continue → 断点命中
AI: read_memory(x2, 240) → "数据是空的"
AI:"可能 hook 早了，continue 等第二次命中"
AI:continue → 程序直接跑完了，没有第二次
AI:"需要重新开始... 但我没有重启模拟器的能力"
→ 卡住，需要人工干预
```

或者更常见的：

```
AI: 断点命中 → read_memory → 拿到一堆数据
AI:"我觉得应该看地址 B 而不是这里"
AI: remove_breakpoint → add_breakpoint(地址B) → continue
→ 但执行已经过了地址 B，这次跑不到了
→ 又卡住了
```

unidbg 模拟器每次运行都是从头开始：初始化 → 加载 SO → JNI\_OnLoad → 调用目标函数 → 结束。整个生命周期可能只有几秒。**错过一个断点，就得重头再来。但 MCP 没有"重启模拟器"的能力。**

而代码是**声明式**的——`callCount == 0`写一次，改个数字重跑 3 秒搞定。

### 4.3 代码方式的迭代成本

```
改一行 callCount == 1 → 重新编译运行 → 3 秒拿到结果
改一个地址 0xABCDE → 0xABCF0 → 3 秒拿到结果
多加一行 ctx.getLongArg(3) → 3 秒拿到结果
```

每次迭代成本极低，而且之前所有的 mock 环境、初始化逻辑都在代码里，不会丢失。

**五、第三道坎：算法验证——MCP 没有计算能力**

## 5.1 逆向分析的本质是"验证假设"

逆向不是"看数据"，而是"提出假设→验证→修正"的循环。

比如你怀疑 SO 里有一段魔改 AES，验证方式是：

```
// 假设：SO 使用自定义 Rcon 做 key expansion
// 验证：本地实现 key expansion → 对比 SO 的轮密钥

static int[] keyExpansion(byte[] key) {
int[] w = new int[44];
for (int i = 0; i < 4; i++)
        w[i] = getU32(key, i * 4);
for (int i = 4; i < 44; i++) {
int temp = w[i - 1];
if (i % 4 == 0)
            temp = subWord(rotWord(temp)) ^ CUSTOM_RCON[i / 4 - 1];
        w[i] = w[i - 4] ^ temp;
    }
return w;
}
```

然后还有 InvMixColumns、AES-CBC 解密、PKCS#7 验证... 总计 200 行纯算法代码。

### 5.2 MCP 的困境

AI 通过`read_memory`拿到轮密钥的 hex dump 后，需要在"脑中"做 GF(2^8) 乘法、矩阵运算、S-box 查表... 这不现实。最终 AI 还是会说："我帮你写个 Python 脚本验证吧"——**又绕回了代码生成的路子**。

MCP 工具集里没有"执行任意计算"的工具。它能读数据，但不能处理数据。

**六、第四道坎：输出爆炸**

### 6.1 trace 的数据量

unidbg 的 trace 输出量极大。一个包含自定义虚拟机的 SO，一次函数调用可能产生**数十万条指令**。

MCP 的`trace_code`实现将每条指令都作为一个 JSON 事件推入无界队列：

```
activeTraceCode = emulator.traceCode(begin, end, (emu, address, insn) -> {
    JSONObject event = new JSONObject(true);
event.put("event", "trace_code");
event.put("address", "0x" + Long.toHexString(address));
event.put("mnemonic", insn.getMnemonic());
event.put("operands", insn.getOpStr());
event.put("regs_read", formatRegValues(insn, regsAccess.getRegsRead()));
    server.queueEvent(event);  // 每条指令一个事件，无上限
});
```

然后`poll_events`一次性全部拼成字符串返回：

```
private JSONObject pollEvents(JSONObject args) {
List<JSONObject> events = server.pollEvents(timeoutMs);
StringBuilder sb = new StringBuilder();
for (JSONObject event : events)
        sb.append(event.toJSONString()).append('\n');
return textResult(sb.toString());
}
```

10 万条指令 × 每条 ~300 字节 =**30MB JSON**。

两个问题：

**-内存爆炸：LinkedBlockingQueue无界，大范围 trace 直接 OOM**

**-上下文爆炸：AI 的上下文窗口根本装不下这么多数据**

### 6.2 代码方案天然解决这个问题

```
// Java 端：trace 写文件，不占 AI 上下文
traceHook = emulator.traceCode(module.base, module.base + module.size);
traceHook.setRedirect(new PrintStream(new File("trace_output.log")));
```

```
# Python 端：按需过滤，只看关心的指令
for line in open("trace_output.log"):
    if "str" in line and target_address in line:
print(line.strip())
```

写文件 + 离线过滤，天然支持任意大小的 trace 数据。

**七、我们最终选择的方案：Skill**

7.1 什么是 Skill

Claude Code 的 Skill 是一种自定义命令机制。在项目目录下创建`.claude/skills/<name>/SKILL.md`，定义一个 prompt 模板。使用时输入`/skill-name`触发 AI 按模板生成代码。

核心区别：**MCP 让 AI 操作调试器，Skill 让 AI 写代码。**

### 7.2 针对 unidbg 设计的 Skill

**`/hook [地址] [描述]`**— 断点捕获代码生成：

```
---
name:hook
description:生成 unidbg BreakPointCallback 代码
allowed-tools:Read, Write, Edit
argument-hint: [地址 要捕获的数据描述]
---
阅读项目中已有的 hook 脚本作为参考模板。
在用户指定的地址生成 BreakPointCallback：
-读取相关寄存器（根据 ARM64 调用约定推断参数）
-读取寄存器指向的内存（根据描述推断数据结构和大小）
-打印格式化输出（hex dump + 人类可读解释）
-支持 callCount 过滤（如"只看第 N 次调用"）

目标: $ARGUMENTS
```

**`/trace [范围] [关注点]`**— Trace 捕获 + 分析脚本

```
---
name:trace
description:生成 unidbg trace 捕获脚本和配套的 Python 分析脚本
allowed-tools:Read, Write, Edit
argument-hint: [函数地址范围 关注的数据]
---
生成两个文件：
1. Java trace 脚本：使用 traceCode...