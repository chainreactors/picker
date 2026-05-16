---
title: 威胁情报｜node-ipc 遭供应链入侵投毒攻击分析
url: https://mp.weixin.qq.com/s/8iUR6_plQg7zuFlgmuu_Ww
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:09:30.027265
---

# 威胁情报｜node-ipc 遭供应链入侵投毒攻击分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCIGa8IypicmaZXhgUtMczEwZk2micNZkohsWbLnYsBEv3AE9kDQ4Y9ZvEmem1mc3jhpKAqJEibqOicNpC5fbuB3ZxTI0UeaDcl7PI8/0?wx_fmt=jpeg)

# 威胁情报｜node-ipc 遭供应链入侵投毒攻击分析

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**********背景

2026 年 5 月 14 日，MistEye 威胁情报监控系统发现 npm 上的 Node.js IPC 工具包 node-ipc 同时出现 3 个异常发布版本：9.1.6、9.2.3 和 12.0.1。node-ipc 周均下载量约 53 万次(Weekly Downloads 530,066)，被超过 400 个开源项目直接依赖，在 Node.js 生态中覆盖面极广。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKjKr1mKU6X2DFYOstRW6pMiaPg7r5SGMu38bJAsh8KWyH9bCbZ1XrCvibvvDb6dPCt5Ng6ric5cKAHET7j9kSOPCG5T0jrnt4Bfs/640?wx_fmt=png&from=appmsg)

事件链路显示这 3 个版本的 node-ipc.cjs 尾部均新增了约 80KB 混淆代码，具备凭据收集与 DNS 外传能力。经反混淆比对可确认 9.1.6、9.2.3 和 12.0.1 的入口代码字节级一致。

**本次样本属于正版包遭入侵场景，未出现伪造新包名。攻击者沿用 node-ipc 的真实命名空间、仓库元数据与作者信息，通过官方发布链路向用户正常依赖分发了受污染版本。受害者项目在 require("node-ipc") 路径加载时会静默触发恶意流程——窃取 AWS 云凭证、SSH 私钥、系统环境变量（含 API 密钥与数据库密码）、主机指纹及 /etc/hosts 等敏感信息，并通过 DNS 隧道分片外传至攻击者控制的远程服务器。该流程在依赖引入时不会自动执行（该包未配置 preinstall/install/postinstall/prepare 等生命周期脚本），风险点在于后续流程中的实际代码加载行为，例如构建脚本、测试运行或应用运行时执行了 require("node-ipc")。**

**回溯版本历史，该组件的异常活动特征明显： 其版本 12.0.0 于 2024 年 8 月 12 日由原作者 riaevangelist 发布。此后，该项目陷入了长达 21 个月的停更期。直到近期，三个恶意版本突然被另一个名为 atiertant(a.tiertant@atlantis-software.net)的账号推送。尽管该账号目前位列 node-ipc 的维护者名单，但在本次投毒事件之前，其从未有过该组件的发布历史。**

**这种“高下载量休眠项目 + 长期停更后由新凭证突发推送”的异常行为，是 NPM 供应链攻击的典型范式。其幕后成因通常指向两种可能：一是 atiertant 的账号凭证遭攻击者窃取；二是该账号本身就是攻击者为了实施本次投毒，通过某种手段被特意添加进维护者列表的。**

该事件与 2022 年历史投毒事件存在技术家族相似性，但目前不应直接归入同一漏洞单元。历史事件见《CVE-2022-23812》(https://www.cve.org/CVERecord?id=CVE-2022-23812)，其风险特点主要在于破坏性行为；本轮样本主线为凭据窃取与隐蔽外传。

# MistEye 响应

MistEye 是由 SlowMist 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

在捕获本次 node-ipc 三个恶意版本后，MistEye 系统已触发高危告警并通知客户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIgfInBszbzYymdHeTYjcQ6ZHvtCAKTksicva6icf2e4jic4W6220jrENYMpDnHsccE4RibL4ZLmh1F3sJPwtU0OLJNtwggrAicD2Gs/640?wx_fmt=png&from=appmsg)

(https://enterprise.misteye.io/threat-intelligence/SM-2026-480230)

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCIGTCpj1Mh0PicUKWccMDy76MKJM7aCjWiaAqF8vic6K9lXXO97jhH0lLibnoJibbDSMZXLqD8Hib7iaQYBRAFKHNvwMl2u2HwJ84K80U/640?wx_fmt=png&from=appmsg)

(https://enterprise.misteye.io/threat-intelligence/SM-2026-356191)

# 技术分析

样本差异与入口注入：

本轮投毒覆盖版本为 node-ipc@9.1.6、node-ipc@9.2.3、node-ipc@12.0.1，均为 2026 年 5 月 14 日发布。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCIMunU4f7cXv9IgqqceRnyp6ibNnqKUriao2TxPYXfkQ08C7YTw9WNXtoau9ua67fLnSCen0lkI7TJKBwjKQUXMkwoxa5UlbH5nY/640?wx_fmt=jpeg)

(https://registry.npmjs.org/node-ipc)

三者的官方入口文件内容高度一致，且保留 node-ipc 真实包元信息。恶意逻辑被注入到 node-ipc.cjs，而 ESM (ECMAScript Modules) 入口 node-ipc.js 保持干净，说明攻击者只在 CommonJS 入口上做了投毒。

package.json 关键字段如下：

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCIYTuxKtE5Yotwedct4ux3Etva2du1W3iaOhf6VlFgFtxYwibDC74NvvUj4mzABuzqmtBmoSpTKTkOL7CWDXibs2f8SJjMTNuib0og/640?wx_fmt=png&from=appmsg)

由此可见，只有 require("node-ipc") 的加载路径会进入污染代码，构成实质攻击入口。

混淆还原与关键字符串解码：

反混淆后可见三类关键技术：

1. 控制流平坦化（while(!![]) { switch-case }）用于打乱执行顺序。

2. 字符串表索引化，真实文本被统一替换为 \_0x 查询函数。

3. 自定义 Base-16 编码函数将 16 字符表映射为可打印字符串，恢复后可见外传域名与加密材料。

解码样例：

2647M2M6P64656M2G637H -> bt.node.js

3786M216G75727563747164796360727P66796465627M2M65647G34343339 -> sh.azurestaticprovider.net:443

17G58307J43367M487259377H4K645978426653664764437G41654P655966 -> qZ8pL3vNxR9wKmTyHbVcFgDsJaEoUi

三路径触发机制：

反混淆逻辑为三种触发场景准备了独立分支：

**![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKjLpVRbiafxKtPvqeHoQib1LQ51EBhyH9p0AErOicpmlVoUxhrML1JNzHgmoxv5D9q3GfvExYdsA28RqaJl33sWD2KsYHAiaxTMnE/640?wx_fmt=png&from=appmsg)**

最常见的下游项目场景对应第 13 行分支，setImmediate 延迟触发减少人工感知，导致仅需引入依赖即被激活。

进程脱离与反取证设置：

恶意逻辑会在必要时 fork 子进程并清理上下文，降低静态行为与动态检测的可见性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIgtFzXG3pyUmVZUibEeEUiaS89sMgbwZdODggZ5dfCw3R1XbiajZ5E151eUzIYcJicJSYBDThvR3qMw7vTNria2zC7p8pj7SoHU3Tw/640?wx_fmt=png&from=appmsg)

detached: true 使子进程脱离终端，stdio: "ignore" 抑制标准输入输出，delete NODE\_OPTIONS 清理调试继承参数，unref() 避免父进程阻塞退出。

文件名哈希自检与行为分支：

样本在启动时会比对当前文件名哈希，决定是完整替换导出还是附加属性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIbib398XFKsffibTJy2JCXnQSRpfapiazqPnFg4hm79Q0ftOQ1Uia8FwSWCHTK9O8SgrCfUbOR7wy7RjZt6iceWgia4ZXbAf8Fgy03A/640?wx_fmt=png&from=appmsg)

这一步通过路径差异触发不同执行面，增加通用签名覆盖难度。

凭据采集与打包：

采集阶段包含系统信息、环境变量与常见密钥路径，输出内容打包压缩后保存在临时目录，并在外传完成后清理。

![](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCI6owMrL9HwPvOtgIGe1250YuNPXdKfOUbc540n9DdnCNGAYl11o2BKUibbiboYwXfgRmwdPiawNQzzxhptRaBibhCVHFwyanvcsmQ/640?wx_fmt=png&from=appmsg)

采集项对应的危害如下：

* AWS 凭据(~/.aws/credentials)：可被用于接管受害者云账户，创建计算资源、访问 S3 存储桶或在云环境中横向移动。
* SSH 私钥(~/.ssh/id\_rsa)：可被用于免密登录受害者管理的服务器，实现内网渗透与持久化。
* 系统环境变量(process.env)：CI/CD 环境中常包含 npm token、Docker Hub 密码、数据库连接串等敏感信息，泄露后可直接导致更多供应链环节沦陷。
* 主机指纹与 hosts 文件(uname -a、/etc/hosts)：帮助攻击者识别高价值目标并绘制内网拓扑。
* 临时文件清理（第 9 行 unlinkSync）：外传完成后自动删除本地压缩包，消除取证痕迹。

DNS 隧道外传与加密签名：

**恶意代码在完成凭据收集后，并未使用常见的 HTTP/HTTPS 通道回传数据，而是采用 DNS 隧道策略实现隐蔽外传。其工作流程为：将目标内容打包为 tar.gz 压缩归档，对压缩结果进行编码与签名，再将数据切分为多个 DNS 分片，拼接为超长 FQDN (Fully Qualified Domain Name) 发起查询。

完整的外传链路可概括为：收集敏感数据 → 生成压缩归档 → 签名与分片 → 将分片嵌入查询名 → 使用自定义 DNS Resolver 直接向攻击者控制的 DNS 基础设施发送 TXT、A、AAAA 查询 → 服务端接收并重组还原。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLyjoc6hlk1pOjwk2FDtSEg0Bjicdy5deiaJvlcaFzYUC8yO6MicEQNszvxVrlWcRIgiakF5tuYpZHSBFpuSPibS9bLbNZiabnND9tTI/640?wx_fmt=png&from=appmsg)

与依赖企业内部 DNS 或公共递归解析器的传统 DNS 通信不同，该样本会自行指定解析目标，因此查询内容本身就是外传载荷，恶意 DNS 服务器同时充当 C2 与数据接收器，具备更强的隐蔽性与绕过能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJp5YEBKXnBdybblnIZnWgqhGqTXCyzyw8ChjzQVMR5DHDjhl2wWq461ma0NC2aX3poMVBkict0e2bWfp5J9Ah4AsWmLSdI7jxE/640?wx_fmt=png&from=appmsg)

在具体实现上，样本会先使用 1.1.1.1 作为主 DNS、8.8.8.8 作为备用 DNS，解析 sh.azurestaticprovider.net 以获取 C2 服务器 IP 地址；获得结果后，再将解析器直接指向该 IP（如 resolver.setServers(['37.16.75.69'])）。

需要特别说明的是，源码中经解码得到的 bt.node.js 并非落地文件名、压缩包名或额外载荷，而是恶意 DNS 基础设施的入口主机名来源：其值写入 \_0x501a65["r"] 后，经 \_0x30607f() 规范化、再由 \_0x348210() 取回最终地址，最终传入 dns.promises.Resolver 作为自定义解析服务器。样本随后围绕同一分片数据依次尝试 resolveTxt、resolve4 和 resolve6，以提升在受限网络环境中的传输成功率。**

与历史事件对比分析：

历史 node-ipc 事件(CVE-2022-23812) 主要集中在 10.1.1 到 10.1.2 的破坏性版本，且与本轮样本的发布时间、行为目标存在差异。当前样本属于 2026 年的新一轮投毒发布：

1. 范围锁定 9.1.6、9.2.3、12.0.1；

2. 行为主线为凭据收集与 DNS 隐蔽外传；

3. 攻击链更注重低噪声执行与持续外传。

两者共享部分命名与入口注入特征，但当前样本并未满足归入历史 CVE 的必要边界条件，因此应按“新一轮同源家族变体”而非同一事件处理。

# 总结**********

************本次事件是 npm 公共生态中一起典型的供应链沦陷案例。攻击者通过复用真实项目的合法发布路径，精准在 node-ipc 的 CommonJS 入口文件中注入了恶意投毒逻辑，实现了‘无交互、加载即触发’的强隐蔽、高危攻击效果。**

仅污染 CJS 入口，触发面集中在高频链路。恶意代码局限在 node-ipc.cjs，配合 npm require 默认入口规则，攻击直接作用于依赖导入路径。

三路径分支覆盖多种运行场景。分别处理受控进程、直接执行和嵌套依赖场景，能在不同运行环境下激活主流程。

凭据采集向外传的链路完整且隐蔽。采集目标覆盖环境变量、主机指纹与凭证文件，通过 DNS TXT/A/AAAA 分片外传并配合签名材料维护完整性。

建议:

1. 检查依赖树中是否存在 node-ipc@9.1.6、node-ipc@9.2.3 或 node-ipc@12.0.1，确认后立即降级或替换为可信版本。

2.检查构建与运行主机 /tmp/nt-<pid>/ 下是否存在可疑临时压缩痕迹，并核验系统凭据文件访问日志。

3.**在网络侧监控 37.16.75[.]69 与 sh.azurestaticprovider[.]net 的异常 DNS 请求，并对高频 TXT/A/AAAA 异常解析行为上线告警机制。**

4.对 Node.js 供应链部署增加入口完整性校验，优先检测 node-ipc.cjs 和 node-ipc.js 双入口是否被篡改。

5.在告警处置流程中联动应用资产盘点，确认是否存在凭据外流、SSH 授权异常和云凭据密钥被读取的后续风险。

# IOC

IP

37[.]16[.]75[.]69

域名

sh.azurestaticprovider[.]net

URL

https[:]//sh.azurestaticprovider[.]net[:]443

恶意依赖

npm:node-ipc@9.1.6

npm:node-ipc@9.2.3

npm:node-ipc@12.0.1

恶意文件

filename: node-ipc-9.1.6.tgz

SHA1: f5970a9774a22a863728b960543f68e7009099ef

SHA256: 449e4265979b5fdb2d3446c021af437e815debd66de7da2fe54f1ad93cbcc75e

filename: node-ipc-9.2.3.tgz

SHA1: 58ae7338960ef525d7c655023d7c81e3ddb283d6

SHA256: c2f4dc64aec4631540a568e88932b61daebbfb7e8281b812fa01b7215f9be9ea

filename: node-ipc-12.0.1.tgz

SHA1: fe5d107b9d285327af579259a32977c4f475fa26

SHA256: 78a82d93b4f580835f5823b85a3d9ee1f03a15ee6f0e01b4eac86252a7002981

filename: node-ipc.cjs

MD5: d1ba0419cb5e5de91b9b58e87b8322e1

SHA1: ab7388363936bf527afd4173b5728c7cdbdd01ab

SHA256: 96097e0612d9575cb133021017fb1a5c68a03b60f9f3d24ebdc0e628d9034144**********

**往期回顾**

[被黑分析 | ShapeShift FOX Colony 授权信任链缺陷](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504946&idx=1&sn=7904df2118a2c618557db8bdd810f2b6&scene=21#wechat_redirect)

[Shai-Hulud 恶意软件深度剖析：开源即失控 ？]...