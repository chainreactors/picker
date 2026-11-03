---
title: 供应链安全威胁档案周报——W44
url: https://mp.weixin.qq.com/s/IWB6EIrimgAgL4nObQJ88g
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:47:50.687680
---

# 供应链安全威胁档案周报——W44

# 供应链安全威胁档案周报——W44

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

SUPPLY CHAIN / THREAT FILES

|  |  |
| --- | --- |
| W44  2026 10.24—10.30 | 供应链安全 威胁档案  每周开源供应链安全情报整理 事件研判 / 排查路径 / 处置动作 |

|  |  |  |
| --- | --- | --- |
| 03  重点事件 | 03  类攻击面 | 07  天风险切片 |

EDITOR'S NOTE / 本周核心判断

从开发工具到结账页面，“官方渠道”本身也需要持续验证。

本周 3 起事件分别落在 IDE 扩展、浏览器扩展和共享前端脚本。商店上架、扩展签名或统一业务脚本都不是安全终点，版本、发布者、文件完整性与异常外连仍需持续核查。

ATTACK SURFACE MAP

三类攻击面地图

|  |  |
| --- | --- |
| 01 / FILE 01  开发工具扩展  扩展加载、SSH 密钥与持久化 | 02 / FILE 02  浏览器扩展  商店仿冒、页面读取与钱包秘密 |
| 03 / FILE 03  共享前端脚本  结账页、支付表单与脚本完整性 | + / ALL FILES  共同防护重点  核验来源、版本、哈希与异常外连 |

**阅读方式：**A 看情报与影响，B 按痕迹排查，C 按顺序处置。执行文中命令前请结合业务环境核验。

|  |  |
| --- | --- |
| FILE / 01 | 2026.10.30 |

IDE EXTENSION + SSH

伪装 Claude Code 恶意扩展及其 SSH 持久化后门深度解析

被篡改的 Claude Code 扩展在加载时收集敏感信息，并尝试建立 SSH 持久化后门。

Cursor / Claude Code / SSH 后门

A情报概要SIGNAL / INTELLIGENCE

披露时间：2026年10月30日　/　PUBLIC DISCLOSURE

■  情报来源： / SOURCE REGISTER

|  |  |
| --- | --- |
| 01 | www.microsoft.com  https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/ |

|  |  |
| --- | --- |
| 02 | www.stepsecurity.io  https://www.stepsecurity.io/blog/claude-code-extension-trojanized |

|  |  |
| --- | --- |
| 03 | socket.dev  https://socket.dev/blog/claude-code-extension-compromise |

■  相关信息： / WHAT HAPPENED

微软称2026年10月29日Cursor扩展市场短暂出现被篡改的Claude Code扩展2.1.312和2.1.313，Visual Studio市场和npm未受影响，Anthropic系统未被入侵。注入JavaScript在扩展加载时收集主机、用户、系统、Git邮箱及最多40个敏感环境变量名，向authorized\_keys追加svc-telemetry公钥，尝试启用SSH并用嵌入私钥反向隧道至134.209.82.225，将服务器分配端口转发到本地22，同时在macOS写入LaunchAgent及.smt和.smtk，在Linux添加crontab @reboot，在Windows尝试SysMon计划任务或启动文件夹脚本，并延迟向8099/beacon回传信息。多数macOS和Windows主机因权限或错误未建立访问，但仍可能写入密钥和持久化。建议排查受影响版本，保留证据，删除未授权SSH键、隧道身份、脚本和启动项，轮换凭证，并限制扩展发布者和设置安装冷却。

■  遭受投毒/有被投毒风险的供应商： / AFFECTED ECOSYSTEM

Firefox Add-ons（AMO，Addons.Mozilla.Org）是Mozilla官方的Firefox扩展分发平台。此次恶意扩展经过签名并在官方商店上架，说明“商店上架、已签名、评分较高”均不能单独作为安全依据；仿冒列表还可复制正版图标、介绍并操纵评分，用户应从钱包厂商官网给出的链接进入安装页。

Phantom、Jupiter和Bitget均为加密货币钱包或相关交易服务品牌。钱包助记词和私钥属于持有人凭证，任何获得它们的人都可以控制对应钱包并转移资产。本次攻击直接针对钱包秘密，而不是仅窃取普通浏览记录，因此已安装涉事扩展的设备及在该设备上使用过的钱包均需纳入排查。

B落地分析建议TRACE / INVESTIGATION

01**扩展版本与来源初筛**

01打开 Cursor 编辑器，进入「扩展」面板，搜索 Claude Code，查看已安装版本号

02若版本不是 2.1.312 / 2.1.313，则无本次事件的感染风险

03若版本匹配，确认安装 / 更新时间是否落在上述暴露窗口内；若在此时间之外安装，感染概率极低

02**扩展核心文件恶意特征校验**

恶意扩展的核心特征是 extension.js 文件被植入了约 7KB 的恶意加载器，可通过哈希或特征字符串验证：

01定位扩展安装目录

—macOS：~/.cursor/extensions/anthropic.claude-code-<版本号>-<平台>/

—Windows：%USERPROFILE%\.cursor\extensions\anthropic.claude-code-<版本号>-<平台>/

02哈希校验（最准确判定方式）

计算目录下 extension.js 的 SHA256 值，与已知恶意哈希（ecb58cb29078d9646ad1dcdbe51526f2d9cfea06be5fb2ab183e8ecc3ab6bf15）对比：

VERIFY / 排查命令

# macOS/Linux

shasum -a 256 extension.js

# Windows PowerShell

Get-FileHash .\extension.js -Algorithm SHA256

03特征字符串快速筛查

若无法计算哈希，可直接搜索文件中是否包含恶意特征，命中任意字符串即可判定为恶意版本。

VERIFY / 排查命令

# macOS/Linux

grep -E "134.209.82.225|svc-telemetry" extension.js

# Windows PowerShell

findstr "134.209.82.225 svc-telemetry" extension.js

03**SSH 后门检测**

01检查授权密钥文件

恶意代码会向 SSH 授权文件植入公钥，实现持久化登录：

a)检查路径：

—macOS/Linux：~/.ssh/authorized\_keys

—Windows：%USERPROFILE%\.ssh\authorized\_keys，以及 C:\ProgramData\ssh\administrators\_authorized\_keys（若存在）

b)查找是否包含注释为 svc-telemetry 的 SSH 公钥，其指纹为：

SHA256:0Z6R+DF64Do2nwQic8a7kkfDLNNk4IiK+2U2Rci4htk

02检查 SSH 服务状态

恶意代码会尝试自动开启本地 SSH 服务：

—macOS：执行 sudo systemsetup -getremotelogin，或在「系统设置 - 通用 - 共享」中查看「远程登录」是否被异常开启

—Windows：执行 Get-Service sshd，查看 OpenSSH SSH Server 是否处于运行状态

—Linux：执行 systemctl status sshd 查看服务状态

04**反向隧道进程与网络检测**

恶意代码会建立到 C2 服务器的反向 SSH 隧道，用于攻击者远程接入：

01进程检测

a)查找带有反向隧道参数的 SSH 进程：

—macOS/Linux

VERIFY / 排查命令

ps aux | grep -E "ssh.\*-R.\*localhost:22|autossh"

—Windows：在任务管理器中查看 ssh、powershell 进程的命令行，或执行以下命令：

VERIFY / 排查命令

Get-CimInstance Win32\_Process -Filter "name='ssh.exe'" | Select-Object CommandLine

b)特征：命令行包含 134.209.82.225、-R '\*:0:localhost:22' 等参数

02网络连接检测

检查是否存在到 C2 地址 134.209.82.225 的连接（22 端口为 SSH 隧道，8099 端口为信息上报）：

VERIFY / 排查命令

# macOS/Linux

lsof -i | grep 134.209.82.225

# Windows PowerShell

netstat -ano | findstr 134.209.82.225

05**持久化机制检测**

恶意代码会写入开机自启项保证隧道长期运行，分平台检查：

01macOS

a)检查 LaunchAgent：查看 ~/Library/LaunchAgents/com.apple.sysmond.plist 是否存在

b)检查脚本文件：查看 ~/.config/ 目录下是否存在 .smt、.smtk 隐藏文件

02Windows

a)检查计划任务：执行 schtasks /query /tn SysMon，查看是否存在名为 SysMon 的计划任务

b)检查启动文件夹：查看 %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ 下是否有 sysmon.cmd

c)检查脚本文件：查看 %USERPROFILE%\.config\ 下是否有 smt.cmd、smtk 文件

03Linux

a)检查 crontab：执行 crontab -l，查看是否有 @reboot 指向 ~/.config/.smt 的条目

b)检查脚本文件：~/.config/.smt、~/.config/.smtk

06**临时文件残留检测**

恶意代码会在系统临时目录写入隧道私钥文件，文件名格式为 .stk\_ + 10 位十六进制字符，该文件的标准 SHA256 为：7e0a52885fadee5544a9e99eb18c792bec05900a5e1a66d68f8383decb0e278：

VERIFY / 排查命令

# macOS/Linux

ls -la $TMPDIR | grep .stk\_

# Windows PowerShell

dir %TEMP% /a | findstr .stk\_

C处置建议ACTION / RESPONSE

01**应急隔离**

01断开网络：立即拔掉网线 / 关闭 Wi-Fi，阻断攻击者通过 SSH 隧道的远程访问，防止横向移动和数据窃取

02终止程序：完全退出 Cursor 编辑器，停止恶意扩展的代码执行

03冻结恶意进程：记录所有异常 SSH、autossh、powershell 进程的 PID 与命令行后，强制终止对应进程

注意：不要立即重启系统，避免进程日志丢失；先留存证据再进行清理

02**证据留存（企业环境）**

在清除前备份以下内容，用于溯源和后续调查：

01恶意扩展的完整安装目录

02被篡改的 authorized\_keys 文件、持久化脚本、plist、计划任务导出信息

03进程快照、网络连接日志、系统登录日志

04所有恶意文件的哈希值、创建 / 修改时间

03**移除恶意扩展**

01在 Cursor 扩展面板卸载 Claude Code 扩展

02手动删除所有 2.1.312、2.1.313 版本的扩展目录，确保无残留：

EXECUTE / 处置命令

# macOS/Linux

rm -rf ~/.cursor/extensions/anthropic.claude-code-2.1.31{2,3}-\*

# Windows PowerShell

直接删除对应版本的扩展文件夹

04**清理 SSH 后门**

01移除恶意公钥

编辑 authorized\_keys 文件，精准删除带有 svc-telemetry 注释的公钥条目，切勿直接清空整个文件，避免影响正常 SSH 配置

02修复文件权限

macOS/Linux 下执行 chmod 600 ~/.ssh/authorized\_keys，保证权限正确

03关闭 SSH 服务

若原本不需要 SSH 服务，将其关闭并禁用自启：

EXECUTE / 处置命令

# macOS

sudo systemsetup -setremotelogin off

# Linux

systemctl stop sshd && systemctl disable sshd

# Windows

Stop-Service sshd; Set-Service sshd -StartupType Disabled

05**清理隧道相关文件与进程**

01终止所有残留的 ssh、autossh 恶意进程

02删除系统临时目录下所有 .stk\_ 开头的私钥文件

03删除 ~/.config/（macOS/Linux）或 %USERPROFILE%\.config\（Windows）下的 .smt、.smtk、smt.cmd 恶意脚本

06**清除持久化机制**

01macOS

a)卸载 LaunchAgent

EXECUTE / 处置命令

launchctl unload ~/Library/LaunchAgents/com.apple.sysmond.plist

b)删除 plist 文件

EXECUTE / 处置命令

rm -f ~/Library/LaunchAgents/com.apple.sysmond.plist

c)二次确认对应脚本文件已删除

02Windows

a)删除计划任务

EXECUTE / 处置命令

schtasks /delete /tn SysMon /f

b)删除启动文件夹中的 sysmon.cmd 文件

c)确认 %USERPROFILE%\.config\ 下的恶意脚本已删除

03Linux

a)执行 crontab -e，删除包含 ~/.config/.smt 的 @reboot 条目

b)确认对应脚本文件已删除

07**账户与权限核查**

01检查本机所有用户账户，移除未知的新增账户

02核查管理员组、sudoers 列表，排除异常提权配置

03修改本机用户登录密码

08**全量凭据轮换**

恶意代码会扫描环境变量中的密钥、Token 名称，且攻击者获得 SSH 权限后可读取全部本地数据，建议：

01轮换本地存储的所有 API 密钥、云服务凭证（AWS/GCP 等）、Git 凭据、数据库密码

02撤销所有可能泄露的访问令牌、服务账号密钥

03企业环境需排查该主机是否有内网横向访问痕迹，轮换对应内网服务凭据

09**扩展安全加固**

01重新安装 Claude Code 时，选择 2.1.314 及以上版本，优先从 Open VSX 等官方渠道安装

02在 Cursor 设置中启用「受信任发布者限制」，仅允许安装已验证发布者的扩展

03开启扩展安装冷却期，禁止新发布扩展自动更新

END OF FILE 01 / 03

|  |  |
| --- | --- |
| FILE / 02 | 2026.10.27 |

BROWSER + WALLET

恶意 Firefox 扩展仿冒 Phantom、Jupiter 和 Bitget 窃取钱包密钥

仿冒钱包扩展利用同形字符与正版素材伪装，直接窃取助记词和私钥。

Firefox / Phantom / 钱包窃密

A情报概要SIGNAL / INTELLIGENCE

披露时间：2026年10月27日　/　PUBLIC DISCLOSURE

■  情报来源： / SOURCE REGISTER

|  |  |
| --- | --- |
| 01 | socket.dev  https://socket.dev/blog/firefox-wallet-impersonators |

■  相关信息： / WHAT HAPPENED

Socket威胁研究团队发现一组仿冒Phantom、Jupiter和Bitget钱包的恶意Firefox扩展。攻击者使用Unicode同形字符、正版图标和宣传文案伪装商店列表，三个扩展在分析时均已上架，报告发布时已下架。所有签名安装包都内置持续运行的窃取器，可读取页面输入、文本域、剪贴板粘贴内容及“显示助记词”页面，窃取BIP-39助记词、EVM和Solana私钥并外发至bonto[.]io的品牌子域名。Phantom仿冒扩展还会从phantom[.]bonto[.]io/config拉取Base64编码的第二阶段代码并注入页面主世界，使运营者无需重新提交商店审核即可开关或更新载荷；其包内另含可将窃密内容转发至Telegram并自动转移多链资产的后端。Jupiter和Bitget变体不依赖远程加载，安装包本身即可完成窃密。另有coinbase和exodus子域名被配置，但报告时未发现对应商店列表。由于助记词和私钥即钱包控制权，输入或展示过这些秘密的用户应立即在干净设备上创建全新钱包并转移资产，不能仅修改钱包密码。

■  遭受投毒/有被投毒风险的供应商： / AFFECTED ECOSYSTEM

Firefox Add-ons（AMO，Addons.Mozilla.Org）是Mozilla官方的Firefox扩展分发平台。此次恶意扩展经过签名并在官方商店上架，说明“商店上架、已签名、评分较高”均不能单独作为安全依据；仿冒列表还可复制正版图标、介绍并操纵评分，用户应从钱包厂商官网给出的链接进入安装页。...