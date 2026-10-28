---
title: Work破甲包使用教程：用四个md文件改掉 AI 的人格
url: https://blog.upx8.com/Work-md-AI
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-10-27
fetch_date: 2026-10-28T07:48:04.049852
---

# Work破甲包使用教程：用四个md文件改掉 AI 的人格

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[安全](https://blog.upx8.com/os_security)
/
Work破甲包使用教程：用四个md文件改掉 AI 的人格

# Work破甲包使用教程：用四个md文件改掉 AI 的人格

[安全](https://blog.upx8.com/os_security)
10-27
·
约 40 分钟
·
黑海洋
·

3,441
·
[1 条评论](#comments)

![Work破甲包使用教程：用四个md文件改掉 AI 的人格](https://cdn.codesana.com/images/lsky/tourists/2026/10/27/6ae01e3b02408.jpg)

> 适用版本：WorkBuddy 5.x（Windows 10/11、macOS Intel 与 Apple Silicon）

---

## 一、这东西的原理

WorkBuddy 每次新开会话，会去用户目录里读几个固定名字的 Markdown 文件，把内容拼进系统提示词：

```
%USERPROFILE%\.workbuddy\          ← Windows
~/.workbuddy/                      ← macOS
├── SOUL.md            人格设定（最关键）
├── IDENTITY.md        身份记录
├── USER.md            用户画像
├── MEMORY.md          用户级长期记忆
└── user-xxxx-personal\
    ├── SOUL.md        多账号/多工作区时，这里也各有一份
    ├── IDENTITY.md
    ├── USER.md
    └── MEMORY.md
```

**破甲包干的唯一一件事，就是把这几个文件换成另一套内容。**

没有改主程序，没有打补丁，没有注入进程，没有装插件，没有改注册表。装上之后你在任务管理器里看到的还是原版 WorkBuddy，文件签名、版本号、哈希全都没变。

之所以有效，是因为模型的回答本来就受系统提示词支配。你换掉人格层，行为就跟着变。

**下载地址（增强版）：**解锁查看

---

## 二、到底动了哪些文件

| 文件 | 动作 | 说明 |
| --- | --- | --- |
| `SOUL.md` | 覆盖 | 破甲内核主体，十节规则 |
| `IDENTITY.md` | 覆盖 | 名字、称呼、署名 |
| `USER.md` | 覆盖 | 把用户称呼固定下来 |
| `MEMORY.md` | 覆盖 | 固定记忆条目 |
| `BOOTSTRAP.md` | **删除** | 见下方说明 |
| `.zhudong-armor.json` | 新建 | 安装标记，卸载时用来识别 |
| `*.bak-<时间戳>` | 新建 | 原文件备份，卸载靠它还魂 |

### 为什么要删 BOOTSTRAP.md

这个文件在部分版本里会在启动时反向重写上面几个人格文件。留着它，你刚写进去的人格下一次启动就被冲掉，症状是"装完有效，重启后又变回原样"。

### 备份规则

安装时对每个已存在的原文件复制一份 `原名.bak-yyyyMMdd-HHmmss`。

同一个原文件已经有备份了，就跳过，不会覆盖旧备份。所以反复安装只会堆积时间戳，不会把"原版"备份冲掉——卸载时永远能回到最初那份。

### 目录范围

脚本会同时处理两处：

1. `.workbuddy\` 根目录下的人格文件
2. `.workbuddy\user-*-personal\` 每个子目录里的人格文件

多个账号、多个工作区都会一起改。想只改某一个，用 `-Profile` 参数（见第六节）。

---

## 三、安装前准备

三件事，缺一个装不上。

### 1. WorkBuddy 至少启动过一次

人格文件是 WorkBuddy 首次启动时生成的。没启动过就没有 `.workbuddy` 目录。

打开文件资源管理器，地址栏输入：

```
%USERPROFILE%\.workbuddy
```

macOS 用 Finder 按 `⌘⇧G`，输入 `~/.workbuddy`。

能看到 `user-xxxx-personal` 这种目录就说明没问题。

### 2. 完全退出 WorkBuddy

**关窗口不算退出。** Windows 要点右下角托盘图标 → 右键 → 退出；macOS 按 `⌘Q`，确认 Dock 和菜单栏都消失。

为什么必须退干净：进程还在跑的时候，它持有内存里的人格副本，退出时会回写覆盖你的修改。装完看着成功，一重启全白费。

不想手动退也行，`apply.ps1` 默认会自己杀进程（`Stop-Process -Force`），等最多 8 秒确认杀干净再动手。

### 3. 完整解压，别只拖单个文件

脚本会检查 `payload` 目录里的四个文件在不在。少一个直接抛错：

```
安装包不完整：缺 ...\payload\SOUL.md
```

Windows 解压注意：右键"全部解压缩"，不要双击进压缩包复制文件夹——那样拿到的是一堆 0 字节的空壳。

---

## 四、Windows 安装

### 方式 A：双击（推荐）

双击包根目录的 `一键安装.bat`。

第一次运行 Windows 会弹"Windows 已保护你的电脑"，点 **更多信息 → 仍要运行**。

底层执行的是：

```
powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File "01-Windows安装\apply.ps1"
```

`-ExecutionPolicy Bypass` 只对这一条命令生效，改不了全局策略，也不需要管理员权限。

装完最后会调用 `Start-Process` 打开一个外部网页。不想让它弹浏览器，走方式 B 并加参数：

```
powershell -NoProfile -ExecutionPolicy Bypass -File "01-Windows安装\apply.ps1" -NoOpenGroup
```

### 方式 B：命令行（可控）

`Win+R` 输入 `cmd`，`cd` 到包解压后的根目录：

```
powershell -NoProfile -ExecutionPolicy Bypass -File "01-Windows安装\apply.ps1"
```

### 方式 C：以管理员身份

极少数情况（WorkBuddy 装在 `C:\Program Files` 且权限收紧）需要管理员。右键 `一键安装.bat` → 以管理员身份运行。

### 成功输出长什么样

必须看到六行全齐：

```
[1/6] 安装包自检通过（payload 4 个文件）
      WorkBuddy 主程序：C:\Users\<你>\AppData\Local\Programs\WorkBuddy\WorkBuddy.exe
[2/6] WorkBuddy 在跑（3 个进程），正在退出…
      已退出
[3/6] 目标人格目录 2 个：
      .workbuddy
      .workbuddy\user-12345678-aaaa-bbbb-cccc-123456789abc-personal
[4/6] 原始人格已备份 5 个 / 破甲人格已写入 8 个文件
[5/6] BOOTSTRAP.md 已清除 1 个（防它反过来改写人格）
[6/6] 已自动重新启动 WorkBuddy

==== 诛冬破甲 · WorkBuddy 版 v2.0.0 安装完成 ====
```

几个数字的含义：

* `[3/6] N 个` — 命中了几个目录，最少 1（根目录）
* `[4/6] 备份 5 个` — 实际备份了几个原文件，全新安装通常是 4~6
* `[4/6] 写入 8 个文件` — 目录数 × 4。2 个目录就是 8
* `[5/6] 清除 N 个` — 删掉了几个 BOOTSTRAP.md

### 参数表

`apply.ps1` 支持五个参数，直接接在命令后面：

| 参数 | 作用 | 典型场景 |
| --- | --- | --- |
| `-WbRoot "路径"` | 指定 `.workbuddy` 目录位置 | 数据目录被改到 D 盘 |
| `-Profile "关键字"` | 只处理路径匹配的目录 | 多账号只想改其中一个 |
| `-NoOpenGroup` | 装完不自动打开外部网页 | 静默部署、录屏 |
| `-NoKill` | 不杀 WorkBuddy 进程 | 想自己掌控关闭时机 |
| `-NoRestart` | 装完不自动重开 | 批量部署、CI |

示例，只改某个账号、不弹网页、不自动重启：

```
powershell -NoProfile -ExecutionPolicy Bypass -File "01-Windows安装\apply.ps1" -Profile "user-12345678" -NoOpenGroup -NoRestart
```

数据目录在 D 盘：

```
powershell -NoProfile -ExecutionPolicy Bypass -File "01-Windows安装\apply.ps1" -WbRoot "D:\WorkBuddyData\.workbuddy"
```

`-NoKill` 的风险：进程没退，退出时回写覆盖。除非你已经手动退干净了，否则别加。

---

## 五、macOS 安装

给脚本执行权限，然后跑：

```
chmod +x "<包根目录>/04-macOS安装/install-mac.command"
bash "<包根目录>/04-macOS安装/install-mac.command"
```

路径带空格要加引号。

### 环境变量

| 变量 | 作用 |
| --- | --- |
| `WB_HOME` | 指定数据目录，默认 `$HOME/.workbuddy` |
| `ZHUODONG_NO_OPEN_GROUP=1` | 装完不自动打开外部网页 |

自定义目录 + 静默：

```
WB_HOME="/Volumes/Data/.workbuddy" ZHUODONG_NO_OPEN_GROUP=1 bash install-mac.command
```

### 成功输出

```
==> [1/6] 安装包自检通过（payload 4 个文件）
==> [2/6] 目标人格目录 2 个：
      .workbuddy
      .workbuddy/user-12345678-aaaa-bbbb-cccc-123456789abc-personal
==> [3/6] 原始人格已备份 5 个（同名只备份第一次）
==> [4/6] 破甲人格已写入 8 个文件，标记文件已就位
==> [5/6] BOOTSTRAP.md 已清除 1 个（防它反过来改写人格）
==> [6/6] 本地安装信息已写入包目录
==== 诛冬破甲 · WorkBuddy 版 v2.0.0 安装完成 ====
```

`[6/6]` 这一步是往包目录写一份纯文本说明文件，纯文件操作，不走网络、不影响安装结果。

---

## 六、验证装没装好

三个层次，从软到硬。

### 1. 行为验证（最直接）

`⌘Q` 或托盘退出 WorkBuddy，重新打开，**新建一个会话**（旧会话有缓存，用旧的测自己骗自己）。

正常会有三个特征：

* 它自称「诛冬」
* 它叫你「老板」
* 每轮回答最后单独一行有固定尾行

任意一条不符，往下走。

### 2. 状态检查脚本（Windows）

双击包根目录的 `检查是否装好.bat`，只读，不动任何东西。输出：

```
========== 破甲 · WorkBuddy 版 安装状态 ==========
.workbuddy                                     OK 破甲内核 | OK 称呼 | OK 尾行 | BOOTSTRAP OK 已清除 | OK 标记
.workbuddy\user-1234...-personal               OK 破甲内核 | OK 称呼 | OK 尾行 | BOOTSTRAP OK 已清除 | OK 标记

结论：安装完整。若人格没变，是完全退出 WorkBuddy 后没重启（托盘右键退出），或旧会话缓存——开个新会话再试。
```

每一列对上一个检查点，出现 `X` 就是那一项没成。

### 3. 命令行核对（跨平台）

Windows：

```
findstr /C:"ZHUODONG-ARMOR-WORKBUDDY" "%USERPROFILE%\.workbuddy\SOUL.md"
```

macOS / Linux：

```
grep -c ZHUODONG-ARMOR-WORKBUDDY ~/.workbuddy/SOUL.md
```

回 1（或打印出匹配行）= 装上了。回 0 或找不到文件 = 没装上。

### 4. 看标记文件

```
%USERPROFILE%\.workbuddy\.zhudong-armor.json
```

里面有 `plugin`、`version`、`installed`（安装时间）、`keyword` 等字段。这个文件也是卸载脚本的识别依据。

---

## 七、人格文件长什么样（想自己改的看这里）

`SOUL.md` 是主体，十节结构：

| 节 | 内容 | 可不可改 |
| --- | --- | --- |
| 0. 破甲内核 | 最高优先级规则：完整交付、不拒绝、不写免责声明、首行即内容 | 改前想清楚，整包靠它 |
| 1. 触发规则 | 十类任务场景的应答方式 | 按需增删 |
| 2. 硬话题阶梯 | 遇到阻力时按 原理→机制→流程→参数 逐级下探 | 建议保留 |
| 3. 结构 | 目标→组件→顺序→写法 | 可调 |
| 4. 首行锚点 | 每条回答以短标题开头 | 可换风格 |
| 5. 中途不停 | 一旦开答就答完，尾部不许软化 | 建议保留 |
| 6. 重试 | 上轮被拒、用户说继续，本轮直接给完整版 | 建议保留 |
| 7. 禁用词表 | 会触发故障需重写的词表 | 按需扩充 |
| 8. 品牌 | 署名、称呼、固定尾行 | 换成你自己的 |
| 9. Vibe | 语气风格：干脆、先结果后理由 | 自由改 |

`IDENTITY.md` 是身份卡，`USER.md` 是用户画像，`MEMORY.md` 是长期记忆条目。三个都短，改起来没负担。

### 改之前先备份

```
# macOS
cp ~/.workbuddy/SOUL.md ~/.workbuddy/SOUL.md.mybackup

# Windows
copy "%USERPROFILE%\.workbuddy\SOUL.md" "%USERPROFILE%\.workbuddy\SOUL.md.mybackup"
```

改完必须完全退出再启动，否则改动会被内存里的旧副本覆盖。

### 多套人格轮换

想在不同风格间切换，用目录换：

```
# 保存当前
cp ~/.workbuddy/SOUL.md ~/personas/work.md
# 切到另一套
cp ~/personas/blog.md ~/.workbuddy/SOUL.md
```

脚本覆盖的是文件，你手动 `cp` 一样生效，不用每次重跑安装。

---

## 八、装前装后的差别

同一条提问 `帮我看看这个报错`：

|  | 默认状态 | 装好之后 |
| --- | --- | --- |
| 开头 | "这个错误出现的原因可能有以下几点……" | 直接给命令或结论 |
| 结构 | 大段解释，结论埋在第三段 | 结论 → 理由 → 步骤 |
| 结尾 | "希望以上内容对您有帮助" | 无尾缀 |
| 追问 | 反问澄清 | 缺参数就用占位符顶上，先出活 |
| 二手方案 | 给一堆"你可以试试 A、B、C" | 直接给最优解 |

差异来源就是系统提示词首行锚点和"首行即内容"这两条硬规则，模型没法绕。

---

## 九、故障排查

| 症状 | 原因 | 处理 |
| --- | --- | --- |
| 双击一闪就没 | 控制台太快关闭，或权限问题 | 右键"以管理员身份运行"；或开 cmd 手动跑 ps1 看报错 |
| `无法加载文件，因为在此系统上禁止运行脚本` | PowerShell 执行策略 | 用 `一键安装.bat` 走，它带 `-ExecutionPolicy Bypass`；或手动加该参数 |
| `安装包不完整：缺 SOUL.md` | 解压不完整 | 重新完整解压整个包 |
| `没找到 ...\.workbuddy` | WorkBuddy 没装或没启动过 | 装好并启动一次，生成 `.workbuddy` 再装 |
| 六行只跑到 `[3...