---
title: 【网络安全面试必刷】20个高频Linux命令考点与真实入侵排查复盘
url: https://mp.weixin.qq.com/s/QXYYx7PH-gzOIBfLkPxZmw
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:01:55.069062
---

# 【网络安全面试必刷】20个高频Linux命令考点与真实入侵排查复盘

# 【网络安全面试必刷】20个高频Linux命令考点与真实入侵排查复盘

沧海讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

面试季快到了，不少正在备面的同学问的最多的就是：“面试里，Linux命令和日志排查到底会问到什么程度？”

面试官考察的角度肯定不是你会多少命令，而是当你面对一个真实的入侵场景时，能不能快速定位问题，并清晰地讲出你的处置逻辑。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9R6BCdeSXfBGHpKAiaJeHncjV5EZWABCgiba6sgL1YDic4ibN0VGv9Ag6mCgfFfoJsKorq0HxY8rckWn9JJkJFVSHyl76ZLDFsWGT0/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

今天为大家梳理了最近两年面试中反复出现的考点，整理成了清单，建议收藏备用！

---

### 一、命令速查：20个高频考点与参数详解

我将这20个命令按考察频率分成了四组，并附上了面试中最容易被追问的参数细节。

#### 1. 文件与目录操作（5个）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CsKJlMFPH9QI9lavZKVnbumiaRShh4Cd6ibzX0YjJtZLRe0RFEalgPVFZbyF4WmWUmOauUhvltAZbzjvYUzu1Q8aDibBoMccwiazXkz3nBNO38E/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

💡 面试**技巧**：`find` 是面试的重灾区。排查后门时，下面这条组合命令出现频率极高：

```
find / -type f -mtime -1 -not -path "/proc/*" -not -path "/sys/*"2>/dev/null
```

原理解析：加上-not -path 是为了排除伪文件系统，避免无意义的报错；2>/dev/null 则是把权限拒绝的错误信息丢进“黑洞”，让输出结果干净可读。

#### 2. 权限管理（2个）

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9TP43hQ7TDGu9RjicWKgNctrBpaPLZGAHAAWpL0sIztbeho3M03v67R0cW7dFvjrsJdqMZiaWXoRUP72yzWlMYsfibXhIHH9qq5PQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

💡 面试**技巧**：权限题最爱考 **SUID滥用场景**。攻击者上传的提权脚本常带 `4755权限，面试时你可以这样回答：用`find / -perm -4000 批量扫描，再结合 ls -la 查看时间戳是否异常。

#### 3. 进程监控（3个）

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9T7WPdVZGqwQicUFib9ubDyFGVAgN6Nib1HrpLlqzXhsEEI9BPniboEflibbZfaGe0iaagMQLLXK7DTVv3fMd7qOZCj5eq3ctTKicTiatE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

💡 面试**技巧**：使用 ps 时，推荐写成 ps -ef | grep [a]pache。这种写法能巧妙避免 `grep` 自身进程出现在结果里。面试时提到这个细节，绝对能让面试官眼前一亮！

#### 4. 日志分析（10个命令及组合）

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9RHFJSmq5nfhyRGtl7DKwIia5Byzw6iaia8Ib1qGibForWPhcyc4xEa0C40pCribkC2icQTCuSNbDDeDuaXlXh6N0peqDx20ibwmbfKG4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

💡 面试**技巧**：awk 的频次统计是面试必考题。比如统计访问日志里异常IP的出现次数：

```
awk'{print $1}' access.log |sort|uniq -c |sort -nr |head -20
```

原理解析：这条管道的逻辑是：提取IP → 排序 → 去重计数 → 按次数降序 → 取TOP20。面试官常会让你现场改需求，比如“只统计状态码为404的”，你只需改成

awk '$9==404{print $1}' 即可。

---

### 二、 真实排查案例：SSH弱口令入侵完整处置

光背命令不够，下面带你走一遍我面试时讲过的案例。从发现到结案，每个步骤对应什么命令、输出什么结论，一目了然。

#### 阶段一：异常发现——登录行为审计

安全告警提示某台服务器存在异常登录，首先看 SSH 登录记录：

```
grep"Failed password" /var/log/auth.log |tail -20
```

或者使用 journalctl 会更简洁：

```
journalctl -u sshd --since "24 hours ago"|grep"Failed password"
```

**关键发现**：大量 Failed password for root from 192.168.x.x 记录，且时间密集。

继续用 awk 统计攻击源IP：

```
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
```

**注意**：$(NF-3) 是取倒数第4个字段，也就是IP地址。不同日志格式可能会有偏移，实际使用时要先 cat 看一下样例确认。

🗣️ **面试追问点**：

- 如果攻击者用了不同用户名，Failed password for invalid user 和 Failed password for root 要分开统计吗？
**- 先不分，看整体分布，再聚焦高频IP。**

#### 阶段二：确认入侵——成功登录与行为追溯

发现存在 Accepted password 记录，且来自陌生IP：

```
grep "Accepted" /var/log/auth.log | awk '{print $1,$2,$3,$(NF-3)}'
```

确认入侵时间窗口后，查该时段内的命令历史。

注意：攻击者可能清理 .bash\_history，所以要结合 last 和进程审计：

```
last -f /var/log/wtmp | grep "192.168.x.x"ps aux | grep -E "pts/[0-9]+"  # 看当前活跃终端
```

#### 阶段三：定位后门——文件与进程双重排查

**进程侧**：用 top 或 htop 发现 CPU 占用异常的陌生进程，记下PID后：

```
ls -la /proc/<PID>/exe          # 看实际执行文件路径cat /proc/<PID>/cmdline | tr '\0' '\n'  # 还原完整启动参数
```

**文件侧**：按时间窗口查找新增或修改的文件：

```
find / -type f -newermt "2026-08-10 14:00" ! -newermt "2026-08-10 16:00" 2>/dev/null
```

重点关注 `/tmp`、`/dev/shm`、`/var/tmp` 等可写目录，以及 `.ssh`、`cron.d`等持久化位置。

🗣️ **面试追问点**：

- 如果攻击者改了文件时间戳（如 `touch -r /bin/ls /tmp/backdoor`），怎么发现？

- 用 stat 看 Change time（ctime），或者结合文件系统日志（如 auditd）。

#### 阶段四：清理与加固——应急报告输出

处置完成后，输出应急报告需要包含的关键数据：

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9ThyYEYf4sqOfduMYKeia6ALWC24GtJyByRBgWxOic96ibwHraTrSbaW5e8lSQOGojKLwP0I1ShNt2GOVwa4aqnGHx1ul6DFkybTo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

---

### 三、 面试追问深度：从初级到中级的跃迁

面试官通常会根据你的回答继续深挖，判断你处于什么水平。以下是三个层次的典型问题，你可以对照自测：

🌱 **初级（能执行、会查日志）**

* “`grep` 和 `egrep` 有什么区别？”

* “`awk` 的 `-F` 参数是做什么的？”

* “怎么实时看日志更新？”

🌿 **中级（懂原理、能设计排查方案）**

* “如果日志被删除了，还能怎么追溯？”
* “`journalctl` 和传统文本日志相比，优缺点是什么？”

* “设计一个脚本，自动分析SSH暴力破解并封禁IP”

🌳 **高级（有架构思维、能预判攻击链）**

* “面对日志投毒（log poisoning），你的分析流程怎么保证可靠性？”

* “大规模集群场景下，如何设计日志采集与分析架构？”

**跃迁建议**：
从初级到中级，核心差距不在命令数量，而在 **“为什么用这个命令”** 和 **“命令搞不定时怎么办”**。比如面试时你可以提到：

* 当 grep 太慢时，可以用 rg（ripgrep）或 ag 加速；
* 当单文件日志太大时，要考虑 split 拆分或 zcat 直接读压缩日志。

希望这份指南能帮你在面试季脱颖而出！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9RRrKWnlKhaxmeFXLLPFpS4WglXvibRM4DO9tEuvBcj2nDBXgFT44iaX2e9Te2iccb0iasEN4yt8Etv035lnSDkRFofYickBFbMP2P4/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

---

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

**沧海专属黑客/网络攻防技术资料**

@沧海讲安全：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcYaRKqWc1cxP8sBrX6KZasFTJEVibWmdyoGAuRO4AbzaVjUJ8guoWAzQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcCP8oaOCQm8Cp2qhpCxWiaOjzYrOoA1iac5eSafBicPxSQcpYtchyfVvxA/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcUumOTUmUznuo7MzKl1JiaEQIeSh4ibkO6jxY68zVZz7iayrwGRtGu2bHw/640?wx_fmt=jpeg&from=appmsg)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcvsT9h4B1hS9VEPengMcOtNL24949kb4cibKLS9HkIb1k2htW8GYqzMQ/640?wx_fmt=jpeg&from=appmsg)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6Kqcm6J0eAql29R6DIM8bJW4rweVBicM8ibGMOmLNFTpdcQ0gFvefMTOg9dA/640?wx_fmt=jpeg&from=appmsg)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

@沧海讲安全：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

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