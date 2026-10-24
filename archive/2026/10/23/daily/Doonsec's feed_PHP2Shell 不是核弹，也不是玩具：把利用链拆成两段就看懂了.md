---
title: PHP2Shell 不是核弹，也不是玩具：把利用链拆成两段就看懂了
url: https://mp.weixin.qq.com/s/SBRI0ZXU8Ag5uiBb-sM99w
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:43:09.237039
---

# PHP2Shell 不是核弹，也不是玩具：把利用链拆成两段就看懂了

# PHP2Shell 不是核弹，也不是玩具：把利用链拆成两段就看懂了

网安之家-CyberHomestead

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# PHP2Shell 复盘 与 fscan 工具链审计报告

**CVE-2026-109618 / CVE-2026-109619 / CVE-2026-115560 + fscan / pscan 命令生成器与报告生成器源码审计**

---

## 0. 结论速览

1. 1. **PHP2Shell 的"核弹"叙事和"跳蛋"叙事都不完全对**。漏洞触发面确实通用，RCE 面确实不通用——这两件事被混成了一件，所以两边都能自圆其说。技术事实和公关叙事可以同时为真。
2. 2. **难度不在漏洞，在利用链的物理约束**。PHP2Shell 的稳定原语是悬空指针和堆块尺寸，不是字符串或对象图。这意味着每次成功利用都要重新标定：目标二进制的符号偏移、Zend MM 的堆布局常数、ASLR 泄漏结果、PHP 与 Apache 的初始化顺序。这是"漏洞通用、PoC 不通用"的根本原因。
3. 3. **官方补丁提交本身就是最好的漏洞说明书**。`3584a98` 一个提交改了 **389 个文件、+10759 / −988** 行，其中新增的 `tests/basic/oom_rfc1867_*` 系列测试把每一条内存放大路径都写成了可执行用例。这批用例比任何二次分析都精确。
4. 4. **最硬的量化证据**：同为 PHP 8.4.26，Debian 13 Trixie 的 `zif_system` 偏移是 `0x465370`，Debian 12 Bookworm 是 `0x45a3b0`。堆喷参数 `841`、`406`、`+0x690d8` 是按 Bookworm 标定的，搬到 Trixie 上 5 次尝试全部 `stage1 HEAP_LEAK_FAILED`。
5. 5. **CVSS 9.2 与 NVD 9.8 的分歧，恰好落在争议点上**。PHP 官方 v4.0 给 `AC:H`（攻击复杂度高），NVD v3.1 给 `AC:L`。两个分数描述同一组漏洞，**区别就是"打过去能不能直接拿到 shell"这个问题本身**。内部工单建议：主用 PHP 官方向量，风险说明里保留 9.8。
6. 6. **"七成互联网"是传播语言，不是攻防指标**。W3Techs 2026-10 的口径是"可识别服务器端语言的网站中 PHP 占 69.3%"——分母是"能识别出服务器端语言"的网站，不是"全部网站"，也不是"全部暴露面"。
7. 7. **国内安全公众号讨论失焦的地方在框架层**。ThinkPHP、Discuz! 这类 PHP 应用，漏洞不在框架代码里，框架跑在 PHP 上。升级框架 ≠ 升级 PHP。公开传播里大量厂商公告更爱转 CPython、GPT-5.5 和"防御者之窗"，国内应用侧几乎没人提。节奏是别人带的，风险是自己扛的。
8. 8. **"先升级，再谈规则"是对的**。WAF/IPS 规则是补偿控制——真实利用可能只用结构合法、外观像普通表单的 HTTP 请求；单靠一个 multipart 特征签名证明不了安全。
9. 9. **fscan 工具链的核心设计是一张参数数据库**。整个套件只有两个纯静态 HTML，零依赖、零安装、离线可用，逻辑全部落在 `PARAMS` 这一张表上，用 `fs`/`ps` 双字段解决 fscan ↔ pscan 的参数名差异。
10. 10. **审计发现 7 处实现层缺陷 + 4 处设计规范未实现项**，其中 3 处会实际影响使用（文件选择器丢路径、默认值被静默省略、HTML 转义未处理引号）。详见 §3.5。

---

# 第一部分 · PHP2Shell

## 1.1 为什么"打过去就直接拿 shell"很难

把利用链拆成两层，两层的通用性完全不同：

```
┌─ 触发层（通用）───────────────────────────────────────────────┐
│  版本未修复 + upload_progress 开启 + memory_limit 有限          │
│  + post_max_size 够大 + 能对任意 .php 发 POST                   │
│  + 两次请求命中同一 worker                                      │
│  → 现象：Fatal error: Allowed memory size of 8388608 bytes     │
│           exhausted in Unknown on line 0                        │
└────────────────────────────────────────────────────────────────┘
┌─ RCE 层（不通用）──────────────────────────────────────────────┐
│  精确堆布局 + 精确 libphp.so 偏移 + 成功地址泄漏 + 特定 INI/ELF  │
│  → 现象：system("id>/out/p1")                                   │
└────────────────────────────────────────────────────────────────┘
```

**触发层的通用性来自"输入可以控制内存"**，RCE 层的门槛来自"要在一个具体的内存布局上精确落刀"。

PHP2Shell 不是"把 payload 交给某个业务函数执行"那种 RCE。普通应用层 RCE 的稳定原语是字符串、对象图、业务逻辑，跨版本换个 payload 常常还能用；PHP2Shell 的稳定原语是**悬空指针和堆块尺寸**——被释放对象的尺寸、下一次分配会不会重用同一个 bin、伪造对象字段的偏移、Zend MM 的堆布局、`libphp.so` 的符号偏移、ASLR 泄漏的结果、PHP 与 Apache 的初始化顺序，全都要提前知道。

### 实测条件表（实验室取值 → 不满足会怎样）

| 条件 | 实验室取值 | 不满足会怎样 |
| --- | --- | --- |
| 精确镜像 | `php:8.4.26-apache-bookworm` | 堆喷尺寸全部失效 |
| SAPI | mod\_php + `mpm_prefork` | FPM 得另写一条利用链 |
| Worker 数 | 1 | 无法稳定完成 A→B 同进程利用 |
| `display_errors` | On | Cookie 泄漏链失效 |
| `max_input_vars` | 默认 1000 | 超限 warning 的触发时机变了 |
| `memory_limit` | 8M | OOM 分配点漂移，对象落点改变 |
| `session.use_strict_mode` | Off | 带 `\x00` 的 PHPSESSID 逼不出换 ID |
| `libphp.so` 符号偏移 | `zif_system = 0x45a3b0` | 阶段 3 可能调错函数 |
| 堆布局常数 | `HTDATA = +0x690d8` 、`filler = 841` | 重占失败，通常只是崩溃 |
| 用户态地址范围 | 本机映射约 `0x79...` | 泄漏解析器会判定未泄漏 |
| 命令长度 | 有效命令不超过 14 字节 | 得换别的长度控制方式 |

> **注意"Worker 数 = 1"这一条**。它直接对应官方 advisory 里那句"更多 worker 与无关流量会提高所需尝试次数，但不消除条件"。多 worker 部署下，请求 A（producer）和请求 B（consumer）落到同一进程需要调度配合——这就是"多 worker 摊薄单请求成功率"的技术含义。

### RCE 需要两类地址泄漏

| 泄漏类型 | 目标 | 取得方式 |
| --- | --- | --- |
| Zend MM chunk 基址 | 约 2 MiB 对齐 | 构造超长 `zend_string`，让 `php_url_encode(PS(id))` 越界读，从 `Set-Cookie: PHPSESSID=` 里捞 |
| `libphp.so` 基址 | ELF 装载基址 | 读 `zval_ptr_dtor` 的地址，减去目标构建的文件偏移 |

任一没拿到，伪造出来的 `HashTable` 就只是指向随机内存，表现出来是 worker 崩溃，不是命令执行。

### 三段式利用链与析构路径

```
请求 A：带 PHP_SESSION_UPLOAD_PROGRESS 字段的 multipart POST
        + 约 12 MiB 字段把内存撑爆   →  OOM → longjmp → 状态脏
请求 B：841 个 48 字节字段 + 79 字节伪造块做堆重占
        把伪造的 ZSTR_LEN 设成 0x1000
        靠越界读从响应 Set-Cookie 泄漏 chunk 基址
阶段 3：15 字节 carrier 改写悬空 reference 的 val.value
        再塞进携带伪造 HashTable 的字段
```

析构链（这条链就是 RCE 的落地方式）：

```
php_session_track_init()
 → zval_ptr_dtor(PS(http_session_vars))
   → zend_reference_destroy(R0)
     → zend_array_destroy(fake HT)
       → zend_hash_destroy(fake HT)
         → pDestructor(&bucket->val) = zif_system
           → system("id>/out/p1")
```

伪造的 `HashTable` 是依赖地址和堆布局的二进制结构，不是能抽象成"固定 Raw HTTP 包"的东西。**直接把 stage3 的 body 复制到别的机器上，多数情况下只会得到一次纯崩溃。**

### 你那句"搭配堆栈泄露可能稳定在野利用"

这个判断在技术上成立，而且它指向了真正的门槛所在。

门槛不是 ASLR 本身，而是**缺少一个通用的、跨构建的内存泄露原语**。当前状态下，攻击者要为每个目标构建做一次标定（符号偏移 + 堆常数），这是**每目标成本**，所以无法规模化。

但一旦出现通用泄露原语，标定就退化成**一次性成本**——标定一个代表性构建，把偏移表和堆常数固化进工具，之后换目标只需重新计算基址。VulnCheck 已经做到 x86-64 + ASLR 开启下的成功（10-22 01:30 ET 起商业提供），ARM64 上泄漏可用但 RCE 尚未功能化，且 ARM64 的 ASLR 可被相对容易地暴力枚举。

所以真正该盯的指标不是"有没有 PoC"，而是这三个：

| 指标 | 意义 |
| --- | --- |
| 是否出现**跨构建通用**的内存泄露原语 | 决定标定成本是否从每目标变成一次性 |
| 是否有**非白盒**的偏移获取途径 | 决定标定是否还需要本地调试权限 |
| 泄漏原语是否出现在**多个 PHP 版本**上 | 决定可武器化的目标池大小 |

这三个指标里任意一个突破，"打过去直接拿 shell"的门槛就会塌。**在那之前，补丁先打，规则同步上，这是唯一确定有效的动作。**

---

## 1.2 漏洞原理（追到操作系统调用层）

### CVE-2026-109618：OOM corruption

PHP 用 `longjmp()` 处理内存耗尽：

```
zend_mm_safe_error()            # Zend 内存管理器分配失败入口
  → zend_error_noreturn()       # 提升为不可恢复错误
    → zend_bailout()            # = longjmp()，直接跳回请求顶层
```

**`longjmp()` 的语义决定了它会跳过所有中间栈帧**。正常异常退栈会逐层执行清理逻辑（析构函数、资源释放、全局指针复位），`longjmp()` 一个都不做。

请求启动阶段极其敏感：PHP 正在解析 `multipart/form-data`，`$_POST`、`$_FILES`、数组键、文件元数据、`session upload progress` 等结构正在逐步建立。此时某块 request memory 可能**已经挂到内部结构中，但还没有完成初始化**。

如果这时发生一次 OOM，即使失败的那次分配和这块半初始化内存没有直接关系，执行流也会被提前拽走：

```
multipart 解析
  → request-owned 结构已发布但未完全初始化
    → 任意一次分配触发 memory_limit
      → longjmp / bailout
        → 匹配的初始化或清理被跳过
          → request shutdown 继续运行
            → shutdown 把无效状态当有效数据读取或分支
              → 内存破坏 → 函数指针被劫持 → RCE
```

**"失败的那次分配不需要与那块非法内存相关"** 是 GHSA 原文的关键句。它意味着攻击者可以用一台独立的"内存放大器"在远处制造分配失败。

### 官方补丁把漏洞点拆成了三层

```
① Zend 内存管理层   → OOM 出口从 longjmp 改为 UnwindExit
② 请求解析层        → 关键分配改为 fallible 路径，允许上层停止解析并正常清理
③ 请求关闭层        → 清理 PG(http_globals)、last error、module activation
④ 早期初始化        → 新增 php_basic_early_rinit()，复位序列化/反序列化/URL scanner 状态
```

### CVE-2026-109619：stale global state

worker 全局位置缓存了 request-owned memory 的地址。请求结束后这块内存被释放，**worker 进程还活着，地址也留在原处**。下一个请求只要在正常初始化覆盖它之前碰到这段状态，就出现 use-after-free。

官方把利用抽象成 producer / consumer 两段、五个必要条件：

```
请求 A（producer）
  → 把 request-owned session / error / extension state 发布到 worker 全局
    → fatal error、OOM、超时或 shutdown 后诊断打断匹配的 reset
      → request memory 被释放，worker 继续存活
        → 请求 B（consumer，同一 worker）
          → 在正常 request 初始化覆盖全局状态之前
            → 某段早期逻辑读取、释放、分支或调用悬空指针
```

五个条件缺一不可：①攻击者可达的 producer；②reset 被跳过或被回填；③worker 不退出且 request heap 被释放；④后续请求命中同一 worker；⑤正常初始化前存在 consumer。

### 为什么 mod\_php 最危险

| SAPI | 启动失败后的行为 | 应用代码前可利用？ |
| --- | --- | --- |
| **Apache mod\_php** | **无条件调用 request shutdown** ，即使 startup 已失败 | ✅ 是，已在默认配置下验证完整 RCE |
| FrankenPHP | 类似 mod\_php，无条件调用 shutdown | 源码判定为很可能可被与应用无关的攻击利用 |
| **PHP-FPM** | 启动失败即**退出子进程**，从池中移除 | ❌ 该精确序列不成立（应用期变体路径另算） |
| LSAPI | 建模同 FPM | ❌ 应用相关利用可能，未验证 |

**FPM 上"完整利用未演示"不是 FPM 安全**，而是 FPM 的失败语义恰好切断了 mod\_php 那条链。

### producer / consumer 的两类已确认 consumer

**消费者 A：INI 诊断**。warning、notice、deprecation 在初始化期间就能消费陈旧的 error state，**不需要致命、不需要被显示、不需要被记录**。因为全局状态在 PHP 决定"是否报告"之前就已被访问：

| 无效手段 | 原因 |
| --- | --- |
| 改 `error_reporting` | 全局状态在决策**之前**已被访问 |
| 使用 `@` | 同上 |
| `display_errors=Off` / `log_errors=Off` | 同上 |

可达性：mod\_php 的 `.htaccess` 与 Apache `php_value`/`php_flag`/`php_admin_*`**目录级配置在 `php_request_startup()` 之前应用**；FPM 只有在前端下发 `PHP_VALUE`/`PHP_ADMIN_VALUE` 且产生早期诊断时才有条件可达（FPM pool 值在 worker 启动时应用，`.user.ini` 在正常初始化之后应用，都不构成同样的早期 consumer）；LSAPI 可早期应用环境 INI 值，属有条件候选；FrankenPHP 默认配置下未确认等价消费者，但**不等于免疫**。

**消费者 B：session upload progress**。默认开启，无需应用调用 `session_start()`，可在普通 session 初始化之前进入 session 和 decoder 状态。与 INI 诊断路径**相互独立**。

### 已确认的两个具体场景

1. 1. **PHP 8.5 `fatal_error_backtraces`**：致命错误上报会把回溯状态（请求所有）存进全局；**关闭阶段的复位逻辑总是被漏掉**（always missed）。后续请求的任意一条...