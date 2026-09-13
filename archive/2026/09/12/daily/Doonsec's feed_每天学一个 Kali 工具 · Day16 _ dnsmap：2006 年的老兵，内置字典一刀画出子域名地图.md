---
title: 每天学一个 Kali 工具 · Day16 | dnsmap：2006 年的老兵，内置字典一刀画出子域名地图
url: https://mp.weixin.qq.com/s/ob4QbzMXJ51ycOqToLAE0Q
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:58:59.184273
---

# 每天学一个 Kali 工具 · Day16 | dnsmap：2006 年的老兵，内置字典一刀画出子域名地图

# 每天学一个 Kali 工具 · Day16 | dnsmap：2006 年的老兵，内置字典一刀画出子域名地图

原创

0day收割机
0day收割机

0day收割机

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 摘要：「每天学一个 Kali 工具」第十六天。DNS 侦察三连发收官——dnsmap：2006 年诞生的子域名爆破鼻祖之一，259KB 身板、依赖只有一个 libc6、内置 1000 词字典开箱即用，连 root 权限都不需要。文末附 DNS 三剑客终极对比表和实战速查，建议收藏。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWC5v03icaNricxSVDXPFGpbICWl6hvvKw6OTeE1OLEJrp3Tgwlq4XqXf2w9KhFg1wLyHOy1ln8Q1UBknCFb3wOec9icmtTAtVmW40/640?wx_fmt=jpeg)

## 写在前面

DNS 侦察这条线，我们已经连开两发：

* Day14 dnsrecon：Python 手术刀，12 种模式精细控；
* Day15 dnsenum：Perl 老兵，全自动一把梭挖 IP 版图。

今天补上第三块拼图，也是资格最老的一位——dnsmap，2006 年发布，比这两位都年长。

有个细节先埋个伏笔：Day14 dnsrecon 官网示例里用的字典 /usr/share/wordlists/dnsmap.txt——就是 dnsmap 家的字典。三兄弟共用一本武功秘籍，今天终于见到秘籍的主人。

三连发之后，DNS 侦察篇正式收官。

---

## 一、dnsmap 是什么？

Kali 官网的定义：

> dnsmap 使用内置字典或外部字典（`-w` 选项指定）扫描域名的常见子域名。内置字典约有 1000 个英语和西班牙语单词，如 ns1、firewall、servicios、smtp——所以它能自动在 example.com 里搜出 smtp.example.com。结果可保存为 CSV 和人类可读格式。dnsmap 不需要 root 权限运行，且出于安全考虑不应该用 root 权限运行。

三个身份标签：

| 标签 | 说明 |
| --- | --- |
| 极简主义 | 259 KB，依赖列表只有一行：libc6。整个工具就是一个 C 程序 |
| 开箱即用 | 内置字典，不带任何参数就能扫 |
| 低权限哲学 | 官方明确说"别用 root 跑"——DNS 查询本来就不需要特权，这是老派安全工程师的洁癖 |

出身故事：dnsmap 由pagvac（gnucitizen.org）于 2006 年发布，灵感来自 Paul Craig 的小说《The Thief No One Saw》（无人看见的窃贼），收录在黑客经典读物《Stealing the Network - How to 0wn the Box》里。一个从小说里走出来的工具，干了二十年情报侦察。

---

## 二、快速上手：官网示例精讲

### 示例 1：外部字典扫描（官网示例）

```
dnsmap example.com -w /usr/share/wordlists/dnsmap.txt
```

官网输出（节选）：

```
dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org) [+] searching (sub)domains for example.com using /usr/share/wordlists/dnsmap.txt[+] using maximum random delay of 10 millisecond(s) between requests
```

解读：

1. Banner 自报家门：版本 0.30、作者 pagvac、绰号 "DNS Network Mapper"；
2. 第一行 `[+]`：确认正在用指定字典爆破 example.com 的子域名；
3. 第二行 `[+]`：每次请求之间有最大 10 毫秒的随机延迟——这是 dnsmap 的默认礼貌，避免把 DNS 服务器打急眼；
4. 后续输出会逐条列出解析成功的子域名及其 IP（官网示例到此处截断）。

### 示例 2：批量扫描（dnsmap-bulk.sh）

```
# 准备域名清单echo ”example.com” >> domains.txtecho ”example.org” >> domains.txt # 批量开扫dnsmap-bulk.sh domains.txt
```

官网输出（节选）：

```
dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org) [+] searching (sub)domains for example.com using built-in wordlist[+] using maximum random delay of 10 millisecond(s) between requests
```

注意这次的字典变成了built-in wordlist（内置字典）——这就是 dnsmap-bulk 的特点：批量模式下永远用默认配置（后面详说）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWAwTKibhF1210Ou46edfN5IFVcMv3gibH3xZ43A9hVCz1z8gP9C0bcDxwA1yzX8Miaiczic9fnbEo6CiaBGqBaE765XGratCX7lXickIw/640?wx_fmt=jpeg)

---

## 三、爆破能挖到什么宝？官网列了五件"趣事"

dnsmap 的 man page 里有一段罕见的"营销文案"——《Fun things that can happen》（可能发生的趣事），把子域名爆破的战果列得明明白白：

| # | 战果 | 例子 |
| --- | --- | --- |
| 1 | 远程访问服务器 | `https://extranet.example.com` ——外网入口，重点关注对象 |
| 2 | 配置糟糕/未打补丁的服务器 | `test.example.com` ——测试环境往往防护最松 |
| 3 | 新域名 → 新网段 | 顺藤摸瓜做 whois（注册库查询是你最好的朋友），画出目标组织的隐藏 IP 块 |
| 4 | 子域名解析到内网 IP | 爆破出的子域名居然指向 RFC 1918 私有地址（10.x/172.16.x/192.168.x）——这意味着站在互联网上就能用标准 DNS 解析枚举目标的内网服务器，比区域传送还优雅 |
| 5 | 动态 DNS 的嵌入式设备 | 比如 IP 摄像头——Google Hacking 之外的另一条设备发现路线 |

第 4 条值得多品一会儿：很多公司图省事，把内网系统（OA、监控、堡垒机）的 A 记录直接挂在公网 DNS 上。dnsmap 一条爆破，内网拓扑图免费送到你面前。

这也是蓝队自查清单：拿 dnsmap 扫自己家的域名，看看解析出多少不该公网可见的记录。

---

## 四、参数速查表

dnsmap 的参数一共就五个，全在 man page 里，一张表装下：

| 参数 | 作用 |
| --- | --- |
| `-w <字典文件>` | 使用外部字典替代内置字典；man page 推荐用 crunch 或 cupp 生成个性化字典 |
| `-r <文件/目录>` | 结果存为纯文本；不给文件名则自动生成带时间戳的文件名（如 `dnsmap_example_com_br_2019_11_15_214812.txt`）；可以只给目录名，如 `-r /tmp` |
| `-c <文件/目录>` | 结果存为 CSV 格式，命名行为同 `-r` |
| `-d <毫秒>` | 每次查询之间的最大随机延迟；默认 10ms；范围 1ms～300000ms（5 分钟）；扫描占用带宽太多时调大它 |
| `-i <IP列表>` | 忽略指定 IP 的结果（过滤泛解析假阳性神器）；逗号分隔、不能有空格，最多 5 个；例：`-i 203.0.113.10,198.51.199.65` |

官方承认的短板（BUGS 章节原文）：

> 目前 dnsmap 尚不支持并行扫描，因此耗时相当长。

单线程 + 随机延迟，注定它是个"慢工出细活"的选手。急活儿交给 Day05 的 gobuster dns 模式或多线程工具，慢工细活、低噪声摸底，dnsmap 反而最合适。

---

## 五、配套命令：dnsmap-bulk 批量扫描

dnsmap-bulk 是包里的第二个命令，专为批量目标设计：

```
用法：dnsmap-bulk  [results-path]
```

| 参数 | 作用 |
| --- | --- |
| `domains-file` | 域名清单文件，每行一个域名 |
| `results-path` | 结果保存路径（可选）；给了路径就为每个域名生成一个结果文件，不给就只输出到屏幕 |

官网示例：

```
# 批量爆破域名清单，结果统一存到 /tmp/results/dnsmap-bulk domains.txt /tmp/results/
```

重要警告（man page 原文）：使用 dnsmap-bulk 时，dnsmap永远使用默认选项——内置字典、延迟 10ms、不忽略任何 IP。想自定义参数？只能单域名逐个跑。

---

## 六、DNS 三剑客终极对比

三天连学三个 DNS 侦察工具，一张表收尾：

| 维度 | dnsmap（今天） | dnsenum（Day15） | dnsrecon（Day14） |
| --- | --- | --- | --- |
| 出身 | 2006，pagvac | darkoperator | darkoperator |
| 语言 | C | Perl 多线程 | Python |
| 体积 | 259 KB | 87 KB | 1.51 MB |
| 字典 | 内置 1000 词，开箱即用 | 自带 dns.txt | 需 `-D` 指定 |
| 线程 | ❌ 单线程（官方承认慢） | ✅ 多线程 | ✅ 多线程 |
| 核心绝活 | 极简爆破 + `-i` 过滤泛解析 | whois 网段 + PTR 反查挖 IP 版图 | 12 种模式（axfr/zonewalk/SRV/TLD…） |
| 批量能力 | dnsmap-bulk（仅默认参数） | ❌ | `-iL` 域名列表 |
| 输出 | TXT / CSV | XML + domain\_ips.txt | XML / CSV / JSON / SQLite |
| 权限要求 | 明确不需要 root | 无特殊 | 无特殊 |
| 适合场景 | 快速低噪声摸底、蓝队自查 | 全自动资产版图测绘 | 精细化按需侦察 |

选型口诀：轻量摸底 dnsmap，版图测绘 dnsenum，精细手术 dnsrecon——正式项目三把刀一起上，结果取并集。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWC6E8wC6NI3GZrEDkRf6oJlzm7sfNQooszDh2KhjYBQfh73lpHTU3C07NGtMwibzP9XicVHMDz3S4KGUiaJdsChiam69pLzgtdGgLU/640?wx_fmt=jpeg)

---

## 七、实战速查

```
# 1. 零参数开箱即用：内置字典直接扫dnsmap example.com # 2. 官网同款：外部大字典dnsmap example.com -w /usr/share/wordlists/dnsmap.txt # 3. 结果双格式存档到 /tmp（自动时间戳命名）dnsmap example.com -r /tmp -c /tmp # 4. 低噪声慢扫：每次查询最多延迟 300msdnsmap example.com -r /tmp/ -d 300 # 5. man page 全家桶：延迟 800ms + 双格式存档 + 过滤 2 个泛解析 IP + 自定义字典dnsmap example.com -d 800 -r /tmp/ -c /tmp/ -i 10.55.206.154,10.55.24.100 -w ./wordlist_TLAs.txt # 6. 批量扫描：域名清单 + 结果目录dnsmap-bulk domains.txt /tmp/results/ # 7. 用 crunch 生成个性化字典再爆破（man page 官方推荐组合）crunch 3 8 abcdefghijklmnop -o custom_dict.txtdnsmap example.com -w custom_dict.txt # 8. 过滤泛解析：先找出 wildcard IP，再用 -i 屏蔽dnsmap example.com -i 93.184.216.119 # 9. 三剑客合璧：dnsmap 摸底 + dnsenum 扩版图 + dnsrecon 精细查dnsmap example.com -r /tmp -c /tmpdnsenum --enum example.comdnsrecon -d example.com -t std -a -z # 10. 爆破结果接 nmap 做端口验证dnsmap example.com -r /tmpnmap -sV $(awk '/^[a-z0-9]/ {print $1}' /tmp/dnsmap_example_com_br_*.txt | head -20)
```

---

## 八、合规提醒

dnsmap 虽然温和（默认 10ms 延迟、单线程、无需 root），红线依然要守：

1. 书面授权：子域名爆破也是主动探测，仅限自有资产或授权目标；
2. 尊重公共 DNS：爆破请求会经过递归 DNS 服务器，`-d` 调大延迟既是对目标的礼貌，也是对公共基础设施的保护；
3. 别用 root 跑：官方原话——不需要，也不应该；
4. 战果敏感：挖到解析内网 IP 的子域名（官网"趣事"第 4 条）属于高危发现，按流程报告，严禁利用扩散。

---

## 今日小结

1. dnsmap = 2006 年的子域名爆破鼻祖：259KB、单依赖 libc6、内置 1000 词字典、不需要 root，极简主义教科书；
2. 五个参数全记住：`-w` 外部字典、`-r`/`-c` 双格式存档、`-d` 随机延迟、`-i` 过滤泛解析假阳性（最多 5 个 IP）；
3. man page 的"五件趣事"就是子域名爆破的价值清单：外网入口、测试服务器、隐藏网段、内网 IP 泄露、动态 DNS 设备；
4. 短板官方自认：不支持并行扫描，慢——低噪声场景反而是优点；
5. DNS 侦察篇三天收官：dnsmap 摸底、dnsenum 扩版图、dnsrecon 做手术，三剑客结果取并集才是完整答案。

---

---

觉得有用的话，点赞 + 在看 + 转发给一起学安全的朋友。关注「每天学一个 Kali 工具」，明天见！

---

参考资料

* Kali 官方工具页：https://www.kali.org/tools/dnsmap/
* 项目主页：
* https://github.com/resurrecting-open-source-projects/dnsmap
* 灵感来源：《Stealing the Network - How to 0wn the Box》之 "The Thief No One Saw"（Paul Craig）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

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