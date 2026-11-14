---
title: 一款全自动渗透实战利器！
url: https://mp.weixin.qq.com/s/-E6GS2LRv5H8stvTVcVfSw
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:16:45.934957
---

# 一款全自动渗透实战利器！

# 一款全自动渗透实战利器！

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

介绍

GitHub C2 是面向红队攻防的指挥平台，支持 MCP 接入 AI，适配全自动渗透流程。采用 Flask 网页控制台 + Rust Agent 架构，主通道使用 Cloudflare Worker，GitHub Issue 作为备用链路，故障可自动切换。载荷基于 AES-256-GCM 加密，具备自动提权、进程级伪装、多路持久化自愈、时间窗管控、冷热自适应轮询等能力，支持 memfd 无文件上线，内置中英文界面，相比传统 GitHub 信道 C2，稳定性与隐蔽性更强。

亮点

和其他「只把 GitHub 当信道」的工具比，这几条是真正不一样的：2

* **自己的中继，GitHub 只当备胎。**

  一键在 Cloudflare 上部署 Worker + D1；主路断了**自动切 GitHub**，好了**自动切回**，终端有 `[Channel]` 通知。双通道在侧栏仍是**一台**，不是两台 Agent。
* **启动自动提权。**

  还不是 root 时按顺序试免密 sudo、已有 SUID 解释器、未打补丁的 pkexec、特权容器逃逸；成功则 **exec 替换自身**，不留双进程。无文件模式整条跳过，避免落盘。
* **进程级隐藏，不装内核模块。**

  按发行版伪装成系统守护进程，藏路径、藏 `/proc`、对齐 SELinux/AppArmor，写文件还复原时间戳。
* **持久化多路 + 自愈。**

  systemd / cron / rc.local / profile / 用户服务一起上；有人清掉一条，大约每 6 小时自己补回来。
* **时间窗。**

  只在你规定的时段说话；窗外面板显示**安静**，不是掉线。边界每天抖动，整群不会同一秒苏醒。紧急停机在窗外**照样生效**。
* **轮询全自动识别冷热。**

  编包只填一个基数。有人在操作就加快，闲着就自己放慢，省额度、也少指纹。
* **Token 失效不用重新编包。**

  填 Backup URL，Agent 自己去拉一份新 JSON 配置并热重启。
* **目标机少落文件。**

  反弹 Shell、隧道节点都编在 Agent 里，纯内存；还可以 memfd **无文件**上线。
* **载荷全程加密**

  控制台自带 **中 / 英语言包**（右上角 **EN / 中文**）。

### 隐蔽、提权、性能与稳定性

#### 自动提权

Linux 上线后若当前不是 root，会在守护化**之前**自动试（能提才提，提不了照常以当前权限跑）：

成功则 **exec 替换当前进程**，不会并排出两个 Agent。环境变量闸门防止提权成功后死循环。**memfd 无文件模式整条跳过**（再 exec 自己会破无文件约定，还会在日志里留下失败痕迹）。

#### 隐蔽

全部是**进程级**，不加载内核模块，不跟发行版内核版本绑死：

* **进程名 / 线程名**

  ：`comm` 按发行版自动扮 `polkitd` / `accounts-daemon` / `systemd-udevd` 等；工作线程扮 `kworker`。编包也可手填伪装名。
* **落地路径**

  ：root 优先藏进 `/usr/lib/systemd/…` 这类看起来像系统守护进程的位置；普通用户走 `~/.local/bin/`。写之前用 `access(2)` 探权限，不先建再删、少触发文件监控。
* **藏 `/proc`**

  ：把 `/proc/<pid>` bind-mount 成 PID 1 的视图，常规 `ps` / 看 cwd、fd 不容易对上。
* **SELinux / AppArmor**

  ：`chcon` 对齐 `bin_t` / 单元文件上下文，减少「来历不明文件」刷审计。
* **时间戳**

  ：二进制和状态文件的 mtime 对齐系统文件；每次写入后把目录 mtime 复原（`stealth_write`）。
* **流量外形**

  ：启动抖动、轮询 ±20% 抖动、时间窗边界按 Agent/按天错开；访问 GitHub 时轮换常见客户端 User-Agent。
* **崩溃不吐密**

  ：关掉 coredump，避免 Token / Secret 落到磁盘。
* **Guards**

  ：主机名、用户、标记文件、最低内存对不上就**静默退出**，少在沙箱 / 蜜罐里暴露行为。

性能

* Agent 是 **Rust**，推荐 `x86_64-unknown-linux-musl`**静态链接**，目标机不用装运行库。
* **主通道走自己的 Worker HTTPS**

  不跟 GitHub 评论抢限额、也不等 Issue 刷新；GitHub 只在主路挂了才上场。
* **反弹 Shell 是真 PTY + WebSocket**

  不走 30 秒命令轮询。
* **轮询全自动冷热**

  操作时最快 15 秒，闲置最长 5 分钟，省 API、也少固定节拍指纹。
* 大文件走 **sendit 中转**，上传按块切，不把评论通道撑爆。
* 控制台本机已带隧道服务端、反弹 Shell 服务端，**不必再下一堆配套马**。

#### 稳定性

* 双通道：**切备用失败会回滚**，避免控制台和 Agent 各听一边。
* 中继 D1 被重建、自增 id 归零时，**水位自动复位**，不会整群变聋。
* 同一条命令写到兄弟通道，Agent **去重**，切通道不丢令。
* 持久化多策略；大约 **每 6 小时自检修补**，被清一条还能长回来。
* 守护化用 **spawn + exec**，不用 `fork()`：老 CentOS 上 Tokio 多线程 fork 会锁死。
* 错误按类型退避（鉴权 / 限流 / 网络），再加抖动，不会固定间隔砸接口。
* 热升级**保留 agent id 和通道身份**；失败则旧进程继续跑。
* 设置页空字段**不覆盖**已有密钥；GET 不回明文 Secret。

### 界面

侧栏列出已上线的 Agent，顶部切换业务页。终端、反弹 Shell、文件、隧道、扫描、系统信息、资料库、报告、升级在同一工作区。

控制台内置语言包（`static/js/lang/zh.js`、`en.js`）。右上角 **EN / 中文** 一键切换，选择会记在浏览器里；未选过则按系统语言默认。下面截图是中文界面，切到 EN 后同一套页面为英文。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5yYXmGfnscSE9V84BYhic3qzHXCcQ42kSDvbV0vxqJBBdY7IUkC7kfkr2QfPNr1oRoib21JGFjv8GN3x9pz0UWytXnQR8tgiaQwvRaJEB1Kicvo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

生成器在网页里选通道、填凭据、编译，完成后直接下载二进制。双通道为 **Worker 主 + GitHub 备**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5yYXmGfnscSIHtZc5F7ywiajfKbjePcdrDHAMAPJrvU87GaUWYRFbKBCB1YSU073K6NyuK6MLV6brYllfNlflhTRC7GaVYU3wljbYsPl5BicE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

## 安装

### 环境

| 项目 | 要求 |
| --- | --- |
| 控制台主机 | Linux（Debian / Ubuntu 最省事），Python 3，公网或实验室可达 |
| 生成 Agent | 同机需 Rust（`deploy.sh` 可代装 rustup + `x86_64-unknown-linux-musl`） |
| 可选 | `gcc` / `binutils`（链接与 strip）、`upx`（压缩）、Cloudflare 账号（Worker 中继） |
| 目标机 | 按编包架构：Linux musl / gnu，x86\_64 或 aarch64 |

随包已带隧道服务端 `stowaway_admin` 和反弹 Shell 服务端 `cliws`，一般不必再下。

### 标准安装

```
git clone https://github.com/Kxiandaoyan/github-C2.gitcd github-C2bash deploy.sh
```

脚本会：

1. 识别源码目录 `c2/`（或旁路的压缩包）。
2. 创建 Python 虚拟环境并安装依赖。
3. 询问（或用参数传入）网页账号、通信 Secret、端口、绑定地址。
4. 把凭据写入 `c2/.runtime.env`（权限 0600）和数据库。
5. 检查隧道 / Shell 二进制；按需安装 Rust 与 musl 目标。
6. 用 systemd 单元 `c2-controller` 拉起控制台（无 systemd 则 5 秒自动拉起）。
7. 做登录 + 接口健康检查；升级失败会回滚上一份快照。

完成后终端会打印访问地址，形如：

```
http://<服务器IP>:<端口>/?login=<用户名>&pass=<密码>
```

用地址参数登录，页面本身不放登录表单。首次打开后把地址栏里的密码清掉即可。

### 命令行参数

```
bash deploy.sh --user admin --pass '你的密码' --c2-secret '通信密钥' --port 8080 --bind 0.0.0.0
```

| 参数 | 含义 |
| --- | --- |
| `--user` / `--pass` | 控制台登录。重装时回车沿用旧值。 |
| `--c2-secret` | 通信加密 Secret，编包与解密共用。 |
| `--port` / `--bind` | 监听端口与网卡。默认 `8080`、`0.0.0.0`。 |
| `--noninteractive` | 无人值守。密码可用环境变量 `C2_WEB_PASS`。 |
| `--skip-toolchain` | 不装 Rust。生成器将无法编译。 |
| `--skip-always-poll` | 浏览器闲置约 90 秒后停止后台扫描（默认一直扫）。 |
| `--no-systemd` | 不用 systemd，改用脚本循环拉起。 |

无人值守若要顺便装编译链：`C2_INSTALL_TOOLCHAIN=1 bash deploy.sh --noninteractive ...`

项目地址

https://github.com/Kxiandaoyan/github-C2

文章内容转自乌雲安全，侵删

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/StcNgRRgTbdLTK4dOmB1NNZ0ULO4Kj9syHzjRmmHE41OicHaZl4hTLOYzfUScc4dfr6SdicdMTFegEDoTO0jS192YxekCwt3qIDe3x9iaK0C5I/640?from=appmsg)

大模型应用课程上新

![](https://mmbiz.qpic.cn/mmbiz_gif/oibEHgiaFk5KJoJsDvLaWxgicdqE7hicokALpHwy4vp3NP409IITiboMFPak4RkRxrlgQb82WrtfL0YoJQHFpB8PgX1iaIB0q22rXKyaTcODpPSPg/640?from=appmsg)

想做大模型工程，不只是学基础 LLMOps？

🔥大模型应用与工程实践新班｜11 月 28 日开课✨

A3 全新升级，主打企业落地实战

深耕 AI Infra 落地，聚焦企业真实工程需求

想切入大模型赛道的同学，抓紧了解！

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj55AdUNSDkmXgRsU8ETjqV03OBkobNxJhv1icJYYI7ZvQibyLyTuw0xF2ibw7d8c13rhsicUWIHyOsn1NvGf3kLt0OtGjjzHtApNUG0/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2I159AwKj56FBVSE6el93uojlMVKMvibRXnYMXKicc5QknKzck7EDcKPsmNetYKDP2ibHcm7QfYmLcKhzgecQv8bLX7pNdvoC6Zva8qUwibsQD4/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=62)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj56QtrFRJPHXEyibibhtickealeZ1vrcALia2hOnDlAV5CQibXxwcSGgHIichVEicXKibUaOSzCf6PAlNJBEkheV5MhTWL8ZJuM7Kmq21lc/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=63)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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