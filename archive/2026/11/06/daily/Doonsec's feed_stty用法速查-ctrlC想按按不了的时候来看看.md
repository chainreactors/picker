---
title: stty用法速查-ctrlC想按按不了的时候来看看
url: https://mp.weixin.qq.com/s/Q06n51EUuin0oBEjpuDX6A
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:55:41.286012
---

# stty用法速查-ctrlC想按按不了的时候来看看

# stty用法速查-ctrlC想按按不了的时候来看看

原创

泷羽Sec静安
泷羽Sec静安

泷羽Sec-静安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 1. 基础用法

```
# 查看当前所有 tty 设置（-a = all）
stty -a
# 输出：
# speed 38400 baud; rows 50; columns 200; line = 0;
# intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>;
# eol2 = <undef>; swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R;
# werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
# -parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
# -ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr -icrnl ixon -ixoff
# -iuclc -ixany -imaxbel -iutf8
# opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
# isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl
# echoke -flusho -extproc

# 恢复"理智默认"（出问题时救命命令）
stty sane
```

![11](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpOUsAWJHPo9ewHpr4LWyYCkV6JgqZ3CHSxO7C00rgvG5eJoEEQScqNe187CQXHHW4Xj68iaUChTITXeTZfPR4raf8O3JiaahtptU/640?wx_fmt=png&from=appmsg)

11

---

## 2. 渗透测试核心用法

### 2.1 升级 nc 反弹 shell（**最核心**）

```
# === 攻击机上：监听 + 升级（可选）===
rlwrap nc -lvnp 80
# 拿到 shell 后（远端）：
# ===升级 shell 到完整 TTY ===
python3 -c 'import pty; pty.spawn("/bin/bash")'

# 攻击机上：
# Ctrl-Z（挂起到 nc 里）
stty -echo
fg
# 回车 → 回到 shell
export TERM=xterm-256color
stty rows 50 cols 200
source /etc/skel/.bashrc    # 让 .bashrc 加载（PATH / alias / PS1）
```

![111](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpM4iaJWvE26kgTynGHC6Wn9vUZYv1jQmncXKGUFSniaBFtFV6uSK8W9D82RdA8Cj3w6FrzQqLR18vjcXJRWTibDsjUibyXF0krhwDE/640?wx_fmt=png&from=appmsg)

111

**每一步干了啥**：

| 步骤 | 作用 |
| --- | --- |
| `python3 -c 'import pty; pty.spawn("/bin/bash")'` | 启动一个伪终端（PTY），bash 跑在里头 |
| Ctrl-Z | 把当前前台任务挂起（bash → 进程组） |
| `stty -echo` | 关掉本地回显，否则 nc 收到的回车会被本地 tty 再回显一遍 |
| `fg` | 把挂起的 nc 恢复到前台 |

**为什么这套管用**：

* • `python pty` 给远端 bash 一个真 PTY，bash 以为自己在跑在真终端上
* • `stty -echo` 防止回车被本地二次回显
* • `rlwrap` 给本地 nc 加 readline，方向键能翻历史

升级后可用：`↑↓` 翻历史、`Ctrl-L` 清屏、`Ctrl-R` 反向搜索、`clear` / `top` / `htop` / `vim` 正常工作、`sudo` 能用（部分 sudo 需要 tty 才能输密码）。

> ⚠️ **不要用 `stty raw -echo`**。`raw` 会关掉 `isig`，本地 tty 不再把 `Ctrl-C` 转成 SIGINT，而是把 `0x03` 原样透传给远端；但远端 bash 同样在 raw PTY 上，也不认这个字节，结果 **Ctrl-C 完全失效**。`raw` 还会关掉 `icanon`，readline 的行编辑无法正常工作，**Tab 补全也没了**。实测确认：用 `raw` 能拿到历史和 Ctrl-L，但 Ctrl-C 和补全都不可用。只用 `stty -echo` 就够了。

### 2.2 改窗口大小

```
# 设置终端宽高
stty rows 50 cols 200
# 不然 top / vim / htop / less / man 都按 24x80 显示，看着别扭

# 装一个自动调整的小脚本（很多 OSCP 教程有）
# 或者用 python pty 时直接带尺寸
python3 -c 'import pty,os; os.environ["TERM"]="xterm-256color"; pty.spawn("/bin/bash")'
# 然后在攻击机上：
stty rows 50 cols 200
```

**怎么知道当前真实窗口大小**：

```
# 在攻击机本地执行
stty size        # 输出 "50 200"
# 用这个值在反弹 shell 里设置
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpN8SvabsB1eSicVVqWBWuzAaic3DQKOACKSB8BvibBlzHkObibB5ebpkZjaj4GZN9Clp3ZMzFRTYj4zplpmALTHCyBRBmEquzxMyW8/640?wx_fmt=png&from=appmsg)

### 2.3 恢复 echo（输入不显示时用）

有时候反弹 shell 拿到的 tty 处于 `-echo` 状态，你输入什么屏幕都不回显——盲打：

```
# 恢复回显
stty echo

# 关掉回显
stty -echo
```

### 2.4 改流控

```
# 启用 XON/XOFF 软件流控（默认）
stty ixon

# 禁用（用于串口 / 工业设备 / 某些 CTF 模拟）
stty -ixon

# 启用硬件流控（RTS/CTS，串口用）
stty crtscts
stty -crtscts    # 关
```

> **实战坑**：某些反弹 shell `Ctrl-S` 按下去会"卡住"——其实是触发了 XOFF 暂停输出。`Ctrl-Q` 恢复。`stty -ixon` 永久禁用。

### 2.5 改特殊字符映射

```
# 改"中断"字符为别的（默认 ^C）
stty intr ^X    # ^X 才是中断，^C 不再中断（避免在某些 shell 卡住）
stty intr ^C    # 恢复默认

# 改"删除"字符（默认 ^? 或 ^H）
stty erase ^H    # 某些终端用 ^H 才是删除

# 改"行尾"字符
stty eof ^D       # ^D 是 EOF（默认）
stty kill ^U      # ^U 是删整行（默认）

# 改"挂起"字符
stty susp ^Z      # ^Z 是挂起（默认）

# 一次性看所有特殊字符
stty -a | grep -E 'intr|erase|kill|eof|susp'
```

---

## 3. 完整 TTY 升级的"豪华版"（实战拷贝即用）

```
# === 攻击机本地 ===
# 1. 开监听
stty rows 50 cols 200   # 先把本地终端设大
rlwrap nc -lvnp 80

# === 拿到 shell 后，靶机上 ===
# 2. 升级到 TTY
python3 -c 'import pty; pty.spawn("/bin/bash")'
# 3. Ctrl-Z
# === 攻击机上 ===
# 4. 关掉本地回显（不要用 raw，会毁掉 Ctrl-C 和补全）
stty -echo
fg

# === 现在回车进入完整 bash ===
export TERM=xterm-256color
stty rows 50 cols 200
source /etc/skel/.bashrc    # 让 .bashrc 加载（PATH / alias / PS1）
```

升级后能用的：

* • ✅ `↑↓` 翻历史
* • ✅ `Ctrl-L` 清屏
* • ✅ `Ctrl-R` 反向搜索历史
* • ✅ `clear` / `top` / `htop` / `vim` 正常工作
* • ✅ `sudo` 能用（部分 sudo 需要 tty 才能输密码）
* • ❌ `Ctrl-C` 中断当前命令 —— 这套组合下做不到，见 2.1 节的说明
* • ❌ `Tab` 补全 —— 用 `raw` 会被破坏；`stty -echo` 也不提供补全（补全靠远端 bash 的 readline，裸 `sh` 没有）

> 想要 Ctrl-C 中断：改用 `nc -e /bin/bash` 或让远端 bash 自己 `stty sane`。但注意本地 tty 仍会吃掉 `Ctrl-C` 并杀掉 nc，所以**中断远端命令这件事在 nc 反弹 shell 里本来就不可兼得**。

---

## 4. 调试场景

### 4.1 "我按 Ctrl-C 怎么 nc 直接挂了"

```
# 原因：本地 tty 的 isig 生效，Ctrl-C 被转成 SIGINT 发给 nc 进程组
```

这是 nc 反弹 shell 的**结构性矛盾**：

| 需求 | 后果 |
| --- | --- |
| 让 Ctrl-C 传给远端（不杀 nc） | 本地必须 `isig` 关闭 → 但 `raw` 模式远端也不认 → Ctrl-C 彻底失效 |
| 让 Ctrl-C 能中断远端命令 | 本地 `isig` 必须开启 → Ctrl-C 会被本地吃掉 → nc 挂掉 |

**nc 反弹 shell 里这两件事不可兼得。** 实际可行的做法：

```
# 1. 升级 shell 之前别按 Ctrl-C，用 Ctrl-D EOF
# 2. 远端已经跑起来的命令，用 kill %1 或另开一条 nc 通道处理
# 3. 用 nc -e /bin/bash 直接给一个带 TTY 的 shell（少一层 nc 转发）
```

### 4.2 "我的输入看不见"

```
# 原因：tty 处于 -echo 状态
# 解决：stty echo
```

### 4.3 "我按 Ctrl-S 卡住了"

```
# 原因：触发 XOFF，停止输出（^S = XOFF）
# 解决：按 Ctrl-Q 恢复（XON）
# 或者：stty -ixon 永久关掉
```

### 4.4 "我按 ↑ 出`[A` 字符"

```
# 原因：当前 shell 不接 readline
# 解决 1：升级 TTY（2.1 三步）
# 解决 2：用 rlwrap 包一下（`rlwrap sh` / `rlwrap bash` / `rlwrap nc`）
```

### 4.5 "我按 Tab 出 tab 字符，不补全"

```
# 原因：sh 不带补全 + 当前 tty 不接 readline
# 解决：升级到 bash + 完整 TTY
# 或者临时：rlwrap 包一下当前 shell
```

### 4.6 "top / vim 看着很丑"

```
# 原因：终端类型或尺寸不对
# 解决：
export TERM=xterm-256color
stty rows 50 cols 200
```

---

## 5. 关键选项速查

| 选项 | 干啥 | 实战场景 |
| --- | --- | --- |
| `raw` | 不解释任何字符，全透传 | **别用** ，会毁掉 Ctrl-C 和补全 |
| `-raw` | 恢复 cooked 模式（默认） | 出问题用 `stty sane` 恢复 |
| `echo` / `-echo` | 是否回显输入 | 输入不显示 / 反复回显时用 |
| `rows N cols M` | 设终端宽高 | 升级 TTY 后必备 |
| `sane` | 恢复理智默认 | 出问题就 stty sane |
| `intr X` | 中断字符（默认 ^C） | 改键位 |
| `erase X` | 删除字符（默认 ^?） | 改键位 |
| `kill X` | 删整行（默认 ^U） | 改键位 |
| `eof X` | EOF（默认 ^D） | 改键位 |
| `ixon` / `-ixon` | 软件流控 | `Ctrl-S` 卡住时关 |
| `crtscts` | 硬件流控 | 串口 / 工业设备 |
| `-echoctl` / `echoctl` | 是否回显控制字符（如 ^C 显成 `^C`） | 看着乱时关 |
| `isig` / `-isig` | 是否识别特殊字符（^C / ^Z / ^\） | `raw` 模式默认 -isig |
| `icanon` / `-icanon` | 是否 canonical 模式（行缓冲） | `raw` 模式默认 -icanon |

---

## 6. 为什么 OSCP / 实战离不开它

* • 拿 `sh` 反弹没有历史/清屏 → `python pty` 升级 + `stty -echo` 组合拳
* • 按 Ctrl-C 直接杀整个 nc → nc 反弹 shell 的固有问题，见 4.1
* • 窗口尺寸不对，top/vim 都畸形 → `stty rows 50 cols 200`
* • 串口调试 CTF 题 → `stty` 是必杀器（设波特率、奇偶校验、停止位）
* • 输密码看不见 / 输入双重回显 → `stty echo` / `stty -echo`

> **一句话总结**：nc 反弹 shell 拿到的不是真终端，是个"假货"。`stty` + `python pty` + `rlwrap` 三个一起上，把它伪装成真终端。

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