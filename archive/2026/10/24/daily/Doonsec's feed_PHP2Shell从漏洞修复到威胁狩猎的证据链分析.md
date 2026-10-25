---
title: PHP2Shell从漏洞修复到威胁狩猎的证据链分析
url: https://mp.weixin.qq.com/s/kTNInh05PiLoA7jtwrWX4A
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:09:31.064698
---

# PHP2Shell从漏洞修复到威胁狩猎的证据链分析

# PHP2Shell从漏洞修复到威胁狩猎的证据链分析

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAjAhWibDrrjRyUszX3VEZVTgcibzdRT6mRpFl02Or2WBfYqlgzZOzofoywZwZD1aHZFD2qyCZosegFFQlohjxB5CjTfA2n40G5fo/640?wx_fmt=webp&from=appmsg)

截至材料记录的 2026 年 10 月 24 日，PHP 官方已为两个原始漏洞发布修复版本；与此同时，地下社区仍有漏洞请求、PoC 链接转发、代码片段、脚本下载以及一则本地 RCE 演示声称。外部安全研究也报告了蜜罐上的利用活动。

| 观察层次 | 材料支持的结论 |
| --- | --- |
| 补丁状态 | 两个原始漏洞已有修复版本；补丁发布后仍出现相关分享 |
| 传播状态 | 多语言论坛及 Telegram 样本中出现持续讨论与重复分发 |
| 利用状态 | 外部研究报告过蜜罐利用；一则帖子展示了自称本地实验的 RCE 输出 |

## 一、补丁可用，风险不会自动消失

所提供材料将 PHP2Shell 与两个严重漏洞联系起来：CVE-2026-109618 涉及内存耗尽（OOM）中断后的无效状态处理；CVE-2026-109619 涉及跨请求残留的过期全局状态。材料记载二者 CVSS v4.0 评分均为 9.2，PHP 项目于 2026 年 10 月 21 日发布修复版本。

| PHP 分支 | 材料列出的首个修复版本 |
| --- | --- |
| 8.2 | 8.2.35 |
| 8.3 | 8.3.36 |
| 8.4 | 8.4.27 |
| 8.5 | 8.5.12 |

版本表只是核验起点。生产环境里，Web 流量可能由容器镜像、面板安装包、发行版回移植包或独立 PHP-FPM 池承载；命令行 `php -v` 的结果未必代表线上 Web 运行时。应逐台确认二进制版本、包来源、实际工作进程与重启状态，并核查 PHP 8.1 及更早分支是否有供应商回移植修复。若仅更新文件但未重启长驻进程，仍需确认旧 worker 是否已退出。

另外， 10 月 23 日的一项独立公告：CVE-2026-115560 与会话上传进度配置有关，不能与前述两个 CVE 合并看待。若环境符合公告所述条件，应按官方建议评估 `session.upload_progress.enabled`，同时跟进后续修复。由于本文未独立验证公告细节，变更生产配置前应核对 PHP 官方原文及应用依赖。

## 二、补丁后仍有人找、转、发

截图呈现的不是单一攻击链，而是一个从“求工具”到“宣称有工具”的传播过程：早期帖子讨论漏洞与 PoC，后来出现代码片段、工具界面和下载邀约；在补丁发布之后，仍有帖子提供所谓脚本或源码压缩包。部分链接在多个平台重复出现，因此传播次数不能简单当作独立利用数量。

### 从讨论到所谓分发：证据时间线

| 时间（材料所示） | 观察 | 证据解释 |
| --- | --- | --- |
| 10 月 21 日 | 论坛出现漏洞请求、PoC 讨论、Telegram 预警及早期猜测 | 表明关注与信息流转；不证明工具可用 |
| 10 月 21 日 | 一张终端截图显示工具处于发现/内存信息阶段 | 画面中的进度状态不是命令执行成功证据 |
| 10 月 22 日 | 出现仓库链接、代码片段、新闻转帖及本地演示声称 | 演示与分享均需独立验证；本地实验不等同真实受害 |
| 10 月 22 日 | 有帖子将所谓源码压缩包与已修复版本的讨论并置 | 补丁发布后仍有分发意图；压缩包未被获取或测试 |
| 10 月 23 日 | 明确标注日期的脚本帖子提供下载与多条“利用链”说法 | 直接支持“补丁后仍在传播”，但文件与功能未验证 |

### 证据图组：早期求取与技术资料转发

**B01｜索取现成工具。** 帖子表达了获取 exploit 的需求；截图没有展示成功利用输出。

![B01：论坛中索取 PHP2Shell 利用工具](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAjUcDC8616IKmxlvESkFrLwco5KZX2ibF424CIvEV3g4EC6GRuqufpVKQfKkoDPADvlDqFVBMyqKLk6Op4hIFiaXcIG8OBn1fWXI/640?wx_fmt=png&from=appmsg)

B01：论坛中索取 PHP2Shell 利用工具

**B02｜俄语讨论及转发资料。** 两张截图分别呈现漏洞利用请求/兼容性说法，以及研究文章、公告和视频链接。转发资料不等于发帖者亲自执行过利用。

![B02a：漏洞利用请求与兼容性说法](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAj8pMiazLkOwJZAr9JicIupWialibicXOTMnvdxT2mpfK17sdI7cQm3JRuzkfn6kUZOlwXrdxB1U7txK83aL4IefWfZVgFtv5tgbcvo/640?wx_fmt=png&from=appmsg)

B02a：漏洞利用请求与兼容性说法

![B02b：被转发的技术参考与视频](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiaKgSFOLXsia3icjIe0wYiarbOFzkibq7l8iaicW69Stt3RWLUhWdtJJJXfjtP33icAGMI3Ujpb3vCUPcv9Ux8YQfA59v4MxibGCWGT0Ik/640?wx_fmt=png&from=appmsg)

B02b：被转发的技术参考与视频

**B03—B04｜代码需求与仓库链接。** 土耳其语帖子求取测试代码，另一帖子分享相同仓库链接。由于内容存在重合，应按重复传播看待，而不是计为两次独立成功利用。

![B03：论坛中索取漏洞利用代码](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiagP47bPqvdAdTXjangLjYEtBv8Fr7s5V7O4RwibebzKI1wJiaCgXe2IH6vmvohRa0CUPoD8Efe8CdvVdeJfqib9kur6L4JMuP5Bc/640?wx_fmt=png&from=appmsg)

B03：论坛中索取漏洞利用代码

![B04：论坛分享 PoC 链接](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgLmHibibfJ0OPpyG4fWjmWMGSakO0vDjN5TyZ3FOrsx8BMFFzTFOyLVX3ic5OnfG5rm3rSyg7FIQtJE2nWsuwp6gP0t6uuuj7m6c/640?wx_fmt=png&from=appmsg)

B04：论坛分享 PoC 链接

### 证据图组：代码、工具界面与跨平台再传播

**B05｜代码片段。** 可见内容提及会话上传进度与内存操作；单凭片段无法判断代码完整性、适用前提或实际效果。

![B05：讨论帖中的 Python 代码片段](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAgibJHCltiaIaOWh94wlAvh3ibynPRaOO0bicoyWyyAOVAYzFUMLgCuKOtQejmjCOJXVRBGqEMrFzhACxKiaiaC1IEdJYwiaicwPKgibh9M/640?wx_fmt=png&from=appmsg)

B05：讨论帖中的 Python 代码片段

**B06｜工具终端画面。** 截图展示目标识别及内存信息阶段，画面进度约为 24%；没有显示可独立核验的命令执行结果。

![B06：PHP2SHELL 工具演示画面](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAgK1jqHD3m4oyrZibT3bSwIpkTLuDLjibStLZwIT0H7ERibQxq22MnzpiczoFbIOickLDB8hPfC3jfNZDbOWicADpOEVc3DPFX4hyiaa0/640?wx_fmt=png&from=appmsg)

B06：PHP2SHELL 工具演示画面

**B07—B08｜Telegram 传播。** 一则波斯语预警附带仓库和目标发现线索，另一则以 CVE 标签分享先前出现过的仓库。后者与 B03、B04 指向相同来源，不应重复计数。

![B07：Telegram 中的漏洞预警与链接](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgMQVrB1jpQpvNXs95AhpOjWrp51HNUicFh4D0xWbebrpF49Nfquf7fodcicNQQcPxftFFkK1euXtROYibicO84jxM7JnibB7YicLLB8/640?wx_fmt=png&from=appmsg)

B07：Telegram 中的漏洞预警与链接

![B08：Telegram 中带 CVE 标签的 PoC 分享](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAiaj0LAiaQEaYmrJFMmvHCjRnc2QU99ycud7wxs8tQEibAPduNTBDMuKYGNLTk3WudXibBuYa9PYUaPelWPwEPGtb1ZyvWE3ibJLpJk/640?wx_fmt=png&from=appmsg)

B08：Telegram 中带 CVE 标签的 PoC 分享

### 证据图组：补丁前后与“成功”声称

**B09｜早期预警。** 帖子中对评分、缓解措施和未来扫描的说法属于当时讨论；当前补丁状态应以官方公告为准。

![B09：早期预警与利用猜测](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAjq3GQ5oYdQWV8ge9wju174EcWJ2WmalW2SeKhb3sWo6tpGvQSB7GJtpLodj1UkDRSduY0PqxoicTO224EeJXOdBMichXAibWTLWU/640?wx_fmt=png&from=appmsg)

B09：早期预警与利用猜测

**B10｜补丁后脚本分发。** 截图标注 10 月 23 日并提供脚本下载，能够支持“补丁发布后仍有人分发”的判断。脚本本身未被获取、执行或验证。

![B10：补丁后所谓脚本下载帖](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAhNW1yqoibON6ZpebmUWLHIdyWWG58vfC1rvo50XyECuH5ic3ibT5wCMLsZicXlbN3V6bGakfAq0xrPRU9CcpvibmrliaodwCArrROQc/640?wx_fmt=png&from=appmsg)

B10：补丁后所谓脚本下载帖

**B11｜自称本地 RCE 的演示。** 帖子中有失败反馈，也有另一版本“可用”的声称；嵌入画面呈现本地演示输出。即使画面真实，也只能说明该演示者声称在其环境复现，不能据此确认公网目标或客户资产遭入侵。

![B11：论坛中声称成功的本地演示](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAiahsdEuFVCPyZEHWYd1npVBiavTsYK6iaXe6blhUjLcvficiaib7vv6JNlibFGU2iaQzBU89XUQxnagr9hgSQdS7iceWc8YCqD54DesVBQ/640?wx_fmt=png&from=appmsg)

B11：论坛中声称成功的本地演示

**B12—B13｜历史新闻与所谓源码包。** B12 是对补丁消息的转帖；B13 则在补丁发布后分享所谓完整源码压缩包。链接和文件均未在材料中下载或测试。

![B12：关于紧急修复的历史转帖](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAiaXu8AeNtTX1iaHAWdgP0q3Igkd9ic4XvMSGU7ciax1yicIntibn9rpPbZTlUkBuFdia4MBeRzU6trOPxlyub7rMfgYjVUDRGYsELMAc/640?wx_fmt=png&from=appmsg)

B12：关于紧急修复的历史转帖

![B13：所谓完整漏洞利用源码的分享帖](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAgGcmt7r3wNedujxrt6YmZ6aUpOIuhviaGawnaTVAjYk42H9fhAiaCiby84csf0tSwtyIrOicmo1X4d7WnJiatPgicEt0ScRQtrntibfk/640?wx_fmt=png&from=appmsg)

B13：所谓完整漏洞利用源码的分享帖

## 三、这些证据的强度、重复与盲区

把截图转成可操作判断，至少要分清三类信号：

1. **传播信号**：求取工具、转发链接、粘贴代码或提供下载，说明有人关注或分享；不能说明代码有效。
2. **实验信号**：本地终端输出、进度条或实验室 RCE 声称，说明存在测试叙述；没有独立复现、完整环境信息和目标证据时，仍不能外推到公网受害。
3. **运营信号**：蜜罐观察、网络扫描、载荷拉取尝试或本地日志命中，可以提高调查优先级；是否执行成功，要用主机与应用遥测进一步确认。

样本也有结构性限制：只覆盖有限数量的论坛与 Telegram 截图；内容存在同源链接、转贴和重复叙述；截图无法核实论坛托管位置或暗网可达性；样本的语言分布不能代表全球利用规模。因此，**补丁发布后仍存在跨平台关注和声称分发，外部也有利用活动报告；但所给帖子本身不足以证明特定组织失陷。**

材料还引用了外部研究：watchTowr 报告其蜜罐在 10 月 21 日观测到利用行为；Unit 42 提及超过 2,260 万个可能暴露实例的估计。前者是特定蜜罐观测，后者是潜在暴露面估计，二者都不是“已确认受害服务器数”，也不能归因到截图中的发帖者。

## 四、防守侧狩猎：从异常行为拼出利用链

不要只依赖某一个字符串签名。建议将以下信号放入同一条时间线上，优先回看最近 7 天，并在高风险资产上扩展窗口：

* **进程关系：** PHP-FPM、PHP-CGI、Apache 或其他 Web 服务进程启动 Shell、脚本解释器、下载器或系统侦察命令；核对父子 PID、用户、完整命令行和 Web 请求时间。
* **文件变更：** Web 根目录、上传目录或临时目录出现由 PHP/Web 进程创建、修改或重命名的脚本文件；检查文件内容、哈希、部署记录与写入者。
* **异常请求与错误：** POST 请求中出现 `PHP_SESSION_UPLOAD_PROGRESS` 等标记、异常大请求体、重复 5xx、PHP OOM 错误或工作进程崩溃；单独命中不是漏洞利用证据。
* **出站连接：** PHP/Web 进程连接不常见的公网地址、下载载荷或连接非业务端口；先排除合法外部 API、队列、数据库及运维集成。
* **清理迹象：** PHP/Web 进程关联日志删除、会话文件清理或临时文件清除行为；需区分正常轮转与异常清理。

### 处置优先级

| 优先级 | 建议动作 | 完成标准 |
| --- | --- | --- |
| P0：止住暴露 | 盘点互联网可达 PHP 服务、容器与托管环境；升级至所在分支的修复版本或经核实的回移植包 | 记录资产、实际 Web 运行时、补丁来源和版本证据 |
| P1：确保生效 | 重启 PHP-FPM、Apache/mod\_php、容器或其他长驻工作进程；验证旧 worker 已退出 | 运行进程与服务端实际版本一致，不只看 CLI 版本 |
| P2：追溯排查 | 关联 Web/WAF、PHP 错误、EDR 进程树、文件事件、DNS 与代理日志 | 对每个高置信命中形成主机、时间、进程、请求和处置结论 |
| P3：控制 IOC | 对可疑 IP/域名先进行本地验证，结合业务影响、观测时间和置信度设置阻断或短期监控 | 有负责人、有效期和复评计划；不把短期 IOC 当永久规则 |
| P4：验证检测 | 在代表性 PHP 主机上试运行查询，确认数据源、字段映射、时间范围、误报与漏报 | 查询经过本地测试后再调度，并具备去重与告警分派规则 |

### 常见误区

* **只看 PHP CLI 版本：** Web 请求可能落在另一套 PHP-FPM、容器或面板运行时上。
* **把补丁发布日当作全面修复日：** 未升级、未重启或使用旧镜像的服务仍可能暴露。
* **把上传标记当作成功利用：** 该标记可能来自合法上传功能，也可能是被 WAF 拦截的请求。
* **把崩溃当作利用：** OOM 与段错误也可能由软件缺陷、配置或资源压力造成。
* **把 IOC 命中当作失陷：** 入站扫描命中只说明有连接尝试；还需查出站活动、进程执行和文件变化。
* **把重复链接当多个独立样本：** B03、B04、B08 等存在同源内容，应做去重与关系归并。

## 五、IOC 附录：用于核验，不是自动封禁清单

下列指标为原材料所列的防误触（defanged）值。置信度与建议动作沿用所给数据集标签；不代表本文独立验证其当前归属或恶意状态。封禁前应核查资产上下文、时间窗、代理/运营商属性以及是否存在误伤风险。缺少观测时间的条目维持“未注明”。

### IPv4

| 指标 | 置信度 | 材料建议 | 观测时间（UTC） |
| --- | --- | --- | --- |
| 45[.]198[.]224[.]169 | 高 | 封锁 | 10 月 21 日 14:15–15:52 |
| 85[.]11[.]167[.]243 | 高 | 封锁 | 10 月 21 日 08:37–10:46 |
| 158[.]69[.]113[.]75 | 中 | 封锁 | 未注明 |
| 94[.]154[.]43[.]149 | 中 | 封锁 | 未注明 |
| 143[.]246[.]223[.]124 | 中 | 封锁 | 未注明 |
| 5[.]191[.]140[.]240 | 中 | 仅监控 | 未注明 |
| 206[.]188[.]197[.]105 | 高 | 封锁 | 10 月 21 日 19:11–21:05 |
| 92[.]118[.]112[.]100 | 高 | 封锁 | 10 月 21 ...