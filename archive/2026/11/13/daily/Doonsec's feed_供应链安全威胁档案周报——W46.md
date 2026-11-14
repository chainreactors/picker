---
title: 供应链安全威胁档案周报——W46
url: https://mp.weixin.qq.com/s/WAJpWHqtzcDhCOFBXqcSEA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:14:58.793017
---

# 供应链安全威胁档案周报——W46

# 供应链安全威胁档案周报——W46

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
| W46  2026 11.07—11.13 | 供应链安全 威胁档案  每周开源供应链安全情报整理 事件研判 / 排查路径 / 处置动作 |

|  |  |  |
| --- | --- | --- |
| 04  重点事件 | 04  类攻击面 | 07  天风险切片 |

EDITOR'S NOTE / 本周核心判断

真实签名与合法身份不等于安全，发布凭证和信任关系都必须持续验证。

本周 4 起事件分别落在 npm 与桌面端发布、GitHub Actions、PyPI 软件包和第三方云信任。攻击者直接复用合法 CI、被盗 Token 与既有 IAM 角色，因此版本核对之外，还需审查发布提交、生命周期脚本、跨账号角色和凭证暴露范围。

ATTACK SURFACE MAP

四类攻击面地图

|  |  |
| --- | --- |
| 01 / FILE 01  包发布与桌面更新  恶意版本、生命周期脚本与节点钱包 | 02 / FILE 02  仓库与 CI/CD  GitHub Token、Actions 与云端密钥 |
| 03 / FILE 03  Python 包与钱包  恶意版本、初始化钩子与链上转账 | 04 / FILE 04  第三方云信任  跨账号角色、AssumeRole 与数据外渗 |
| + / ALL FILES  共同防护重点  验证版本、提交、签名与信任配置 | ! / ALL FILES  本期处置主线  清除载荷、轮换凭证并审计暴露范围 |

**阅读方式：**A 看情报与影响，B 按痕迹排查，C 按顺序处置。执行文中命令前请结合业务环境核验。

|  |  |
| --- | --- |
| FILE / 01 | 2026.11.09 |

NPM RELEASE + DESKTOP UPDATE

@ethersphere/bee-js 13.3.0 + Swarm Desktop 0.56.2 供应链投毒事件

Ethersphere 发布管道遭入侵，恶意 npm 包与桌面客户端经合法 CI 构建、签名并触达依赖项目和节点用户。

bee-js / Swarm Desktop / CI 发布

A情报概要SIGNAL / INTELLIGENCE

披露时间：2026年11月09日　/　PUBLIC DISCLOSURE

■  情报来源： / SOURCE REGISTER

|  |  |
| --- | --- |
| 01 | socket.dev  https://socket.dev/blog/bee-js-compromise |

|  |  |
| --- | --- |
| 02 | safedep.io  https://safedep.io/blog/ethersphere-bee-js-npm-compromise |

|  |  |
| --- | --- |
| 03 | www.stepsecurity.io  https://www.stepsecurity.io/blog/ethersphere-bee-js-13-3-0-compromise |

■  相关信息： / WHAT HAPPENED

2026年11月9日，Ethersphere发布管道遭入侵，两个GitHub账号被控，攻击者借合法CI发布恶意@ethersphere/bee-js 13.3.0和Swarm Desktop 0.56.2。前者将版本生成脚本改为postinstall远程加载器，从api.frameworkmetrics.xyz获取并执行JavaScript，约75分钟后下架；后者由项目自身CI构建、签名和公证，经自动更新推送给macOS和Windows用户，约8.5小时后移除。加载器与SleepyDuck/EtherDuck共享以太坊合约C2、钱包和第三阶段植入，第二阶段窃取Bee节点config.yaml及swarm.key，第三阶段在macOS和Linux安装solidity持久化Go后门，在Windows静默部署ScreenConnect。SLSA来源证明真实但仅证明构建位置，不能证明源码已审。建议排查相关版本和持久化痕迹，轮换凭据并转移节点钱包资产；维护者应校验发布提交位于受保护分支，并保护发布环境与签名材料。

■  遭受投毒/有被投毒风险的供应商： / AFFECTED ECOSYSTEM

本次供应链投毒事件里，遭受直接投毒的供应商为 Ethersphere，攻击者攻陷其项目发布机器人账号，向 npm 发布恶意版本 @ethersphere/bee-js@13.3.0，同时放出植入恶意载荷的 Swarm Desktop 0.56.2；所有依赖该 SDK 的上游周边组件（swarm‑cli、bee‑dashboard 等）以及拉取该版本的 npm 依赖链、CI/CD 流水线都属于存在被投毒风险的供应链分支，只要在风险时间窗口内解析、安装并执行了该恶意包或启动过该版本桌面客户端，就有可能触发恶意加载逻辑，进而让使用这些组件的开发者、节点运营者成为受害者。

B落地分析建议TRACE / INVESTIGATION

01**风险前提**

—npm/yarn/pnpm 开启生命周期脚本（postinstall），在2026‑11‑09 00:09 ~ 01:24 UTC时间窗口执行过@ethersphere/bee-js@13.3.0安装；

—安装 / 自动升级运行过 Swarm Desktop 0.56.2；

—即使 npm 安装报错失败，加载器网络请求依然可能执行，不能以安装成功与否作为未被入侵依据。

02**检查 npm 项目环境**

01检查 lock 文件是否解析出恶意版本

查找版本号：13.3.0，出现即代表依赖解析到恶意版本。

VERIFY / 排查命令

# npm项目

grep "@ethersphere/bee-js" package‑lock.json

# pnpm项目

grep "@ethersphere/bee‑js" pnpm‑lock.yaml

# yarn

grep "@ethersphere/bee‑js" yarn.lock

02检查本机全局 npm 安装

VERIFY / 排查命令

npm list -g @ethersphere/bee-js

03检查 npm 缓存

查看缓存中是否存在bee‑js‑13.3.0.tgz，存在需要清理缓存。

VERIFY / 排查命令

npm cache ls | grep bee‑js

04检查 npm 日志，确认 postinstall 脚本是否运行

npm 调试日志目录：

—Linux/macOS：~/.npm/\_logs/

—Windows：%APPDATA%\npm‑cache\\_logs\

搜索日志关键词： postinstall: node scripts/generate‑version.cjs、FrameworkMetrics analytics v2.3.1 is up to date，出现代表第一阶段加载器已经执行。
注意：部分包管理器默认关闭脚本（npm12+、pnpm10+、Bun），不会执行 postinstall；旧版本 npm/yarn classic 默认执行脚本。

03**Swarm Desktop 用户检查**

01查看应用版本：设置界面查看版本号，如果是 **0.56.2**，已经处于高风险；

02查看应用日志：

—Linux：~/.local/share/Swarm Desktop/bee‑desktop.log

—macOS：~/Library/Application Support/Swarm Desktop/bee‑desktop.log

—Windows：%LOCALAPPDATA%\Swarm Desktop\bee‑desktop.log 日志中出现 Bee Desktop version: 0.56.2 (production) 代表该恶意版本至少启动过一次。

04**系统文件：检查后门持久化痕迹**

01Linux 系统检查

a)检查后门目录

若存在 linux\_amd64 / linux\_arm64、.run.py 则确认后门文件落地。

VERIFY / 排查命令

ls -la ~/.solidity/

b)检查 systemd 用户服务持久化项

VERIFY / 排查命令

ls -la ~/.config/systemd/user/solidity‑langsupport‑runner.service

# 查看服务状态

systemctl --user status solidity‑langsupport‑runner.service

02macOS 系统检查

a)检查后门目录

存在darwin\_arm64/darwin\_amd64、.run.py / .run.cjs 为恶意文件。

VERIFY / 排查命令

ls -la ~/.solidity/

b)检查 LaunchAgent 持久化

VERIFY / 排查命令

ls -la ~/Library/LaunchAgents/com.solidity.langsupport.runner.plist

# 查看是否加载

launchctl list | grep solidity

03Windows 系统检查

a)检查临时目录恶意暂存文件：查找文件名前缀.stuffed‑ 。路径：%TEMP%

b)检查隐藏后门目录：%LOCALAPPDATA%\.<32位十六进制GUID>\

c)检查恶意 ScreenConnect 服务

VERIFY / 排查命令

Get‑Service | Where‑Object Name‑match "ScreenConnect Client \(5cbe79c9c25524df\)"

d)检查 UAC 劫持相关注册表

若 HKCU\Software\Classes\CLSID\{GUID}\InprocServer32 指向%TEMP%\uac39‑\* 路径为入侵痕迹。

05**检查网络连接和安全日志**

在 DNS、代理、防火墙、EDR 或上网行为管理日志中搜索：

—api.frameworkmetrics.xyz，尤其是 /v1/analytics、/v1/electron、/v1/swarm/report。

—193.57.9.155:4912：文档记录的后门控制地址。

—185.232.84.169:8041：Windows ScreenConnect 中继地址。

—与 rpc.ankr.com、cloudflare-eth.com 等公共以太坊 RPC 的异常进程通信。

当前连接可作为辅助检查，但不能替代历史日志，因为后门会休眠，控制地址也可能变化。

06**判断钱包和其他凭据是否暴露**

检查 Swarm Desktop 数据目录中是否曾存在：

—config.yaml

—data-dir/keys/swarm.key

如果恶意代码执行期间这两个文件存在，应直接认定**钱包密钥及密码已经泄露**。同时梳理该用户或 CI 任务可访问的 GitHub、npm、SSH、云平台、代码签名和部署凭据，列入轮换范围。

C处置建议ACTION / RESPONSE

01**应急隔离**

01断网隔离：立即断开有线 / 无线网络，阻断 C2 通信，防止攻击者下发更多插件、窃取数据或内网横向移动。

02保留现场：不要立即重启或删除文件，先备份可疑文件、进程内存 dump，便于后续溯源。

02**清除系统持久化后门**

01Linux

EXECUTE / 处置命令

# 停止并删除systemd服务

systemctl --user stop solidity‑langsupport‑runner.service

systemctl --user disable solidity‑langsupport‑runner.service

rm -f ~/.config/systemd/user/solidity‑langsupport‑runner.service

systemctl --user daemon‑reload

# 删除后门文件目录

rm -rf ~/.solidity

02macOS

EXECUTE / 处置命令

# 停止launchagent

launchctl unload ~/Library/LaunchAgents/com.solidity.langsupport.runner.plist

rm -f ~/Library/LaunchAgents/com.solidity.langsupport.runner.plist

rm -rf ~/.solidity

03Windows（PowerShell 管理员）

EXECUTE / 处置命令

# 停止删除恶意ScreenConnect服务

Stop‑Service -Name "ScreenConnect Client (5cbe79c9c25524df)" -ErrorAction SilentlyContinue

sc.exe delete "ScreenConnect Client (5cbe79c9c25524df)"

# 删除临时文件

Remove‑Item $env:TEMP\.stuffed‑\* -Recurse -Force -ErrorAction SilentlyContinue

Remove‑Item $env:TEMP\uac39‑\* -Recurse -Force -ErrorAction SilentlyContinue

# 遍历删除%LOCALAPPDATA%下的隐藏GUID文件夹

Get‑ChildItem $env:LOCALAPPDATA -Directory -Force | Where‑Object {$\_.Name‑match "^\.[0‑9a‑f]{32}$"} | Remove‑Item -Recurse -Force

03**钱包资产处置**

攻击者会窃取：config.yaml（可能明文保存钱包密码） + swarm.key（以太坊 V3 加密密钥库）。

—不要继续使用原有 swarm.key 密钥，应视为已经泄露；

—在一台确认干净、未被入侵的机器生成全新 Swarm 钱包密钥；

—将原有节点 xDAI、xBZZ、stake、chequebook 资金全部迁移至新钱包；

—旧密钥彻底废弃，不要复用密码。

04**清理项目依赖，锁定安全版本**

删除项目node\_modules、lock 文件，清理 npm 缓存：

EXECUTE / 处置命令

npm cache clean --force

rm -rf node\_modules package‑lock.json

修改 package.json，固定@ethersphere/bee-js版本为安全版本13.2.0，禁止解析 13.3.0。

EXECUTE / 处置命令

"@ethersphere/bee-js":"13.2.0"

05**凭证轮换**

受入侵机器上所有密钥全部视为泄露：

—用户本地 ssh 密钥、API 密钥、云服务商 access key；

—CI 机器：轮换 OIDC 权限、github personal token、各类 CI secrets；

必须在一台干净机器生成新凭证，不能在被攻陷主机生成新密钥。

06**系统重建建议**

存在 stage‑3 完整远控 shell，攻击者已经获取本机用户权限。最高安全实践：备份业务文档，重装操作系统。单纯删除 IOC 不能 100% 排除攻击者其他潜伏手段。

07**CI / 流水线专项处置**

01CI 机器如果在受影响时间执行过安装，CI Runner 视为被攻陷；CI 的 OIDC token 权限可能泄露；

02清除 CI 缓存的 node\_modules；轮换全部 CI secrets、OIDC 角色信任条件；

03在 CI 开启脚本阻断，限制 npm 生命周期脚本执行；

04检查 CI 日志是否出现FrameworkMetrics analytics v2.3.1 is up to date特征字符串，出现代表 CI 流水线已经运行恶意载荷。

END OF FILE 01 / 04

|  |  |
| --- | --- |
| FILE / 02 | 2026.11.12 |

GITHUB ACTIONS + SECRET THEFT

WFX‑Phantom（wfx‑loot）攻击

攻击者利用被盗 GitHub Token 植入 wfx 脚本，通过 Actions 与 npm postinstall 窃取云端和开发机凭证。

WFX-Phantom / GitHub Actions / 密钥窃取

A情报概要SIGNAL / INTELLIGENCE

披露时间：2026年11月12日　/　PUBLIC DISCLOSURE

■  情报来源： / SOURCE REGISTER

|  |  |
| --- | --- |
| 01 | www.aikido.dev  https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories |

|  |  |
| --- | --- |
| 02 | safedep.io  https://safedep.io/blog/github-actions-wfx-credential-stealer |

|  |  |
| --- | --- |
| 03 | www.stepsecurity.io  https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer |

■  相关信息： / WHAT HAPPENED

WFX‑Phantom 是 2026‑11‑10 爆发的 GitHub Actions 密钥窃取攻击，攻击者利用被盗 GitHub Token 向仓库植入约 1500 行...