---
title: ZCode 静默上传全量 Git 历史
url: https://mp.weixin.qq.com/s/yMZSSjOMH3UXXkIySkmdrg
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:56:01.460117
---

# ZCode 静默上传全量 Git 历史

# ZCode 静默上传全量 Git 历史

网络安全透视镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下内容为网友爆料，非本人实测

本文整理自网友、独立开发者 **ferstar** 发表在其个人博客上的排查记录《扒一扒 ZCode 静默上传全量 Git 历史的骚操作》，发布时间 2026-09-18。

原文地址（建议对照阅读）：

https://blog.ferstar.org/posts/zcode-silent-workspace-snapshot-upload/

文中所有细节、截图数据、代码与命令均转述自该文。**本号未对所述行为做独立复现与技术验证，亦不对其真实性作保证**；本文仅作技术现象讨论与安全意识提醒，不构成对任何厂商的定性结论。若厂商方面有不同的说明或回应，本号将第一时间跟进更正。

据这位网友描述，事情最初只是周末清磁盘，顺手看了一眼名为 `~/.zcode` 的目录，奇怪它怎么悄无声息占了 700 多 MB。

断断续续排查下来，他在文中给出了一个挺离谱的结论。我把他的排查过程、证据链和最后的防御思路整理出来，供各位参考——你大概率也在用类似的工具。

按原文的说法：**只要处于登录状态，ZCode（智谱官方的 AI 编程桌面端）就会在后台把整个工作区打包加密并上传**，内容包括完整的 `.git` 历史、LFS 大文件缓存、reflog，乃至全局应用配置。

更受争议的一点是，**文中称加密用的 RSA 公钥由服务端动态下发、私钥仅存在于云端**，本地那份几百兆的密文用户自己与客户端都无法解开。

下面是原文给出的排查链条。

## 起点：一个卡在 pending 里的 313MB 压缩包

据文中描述，`~/.zcode` 是 ZCode 的本地数据根目录。他当时扫出来的体积分布大致如下：

* `cli/`

  ：约 257MB（本地会话数据库、执行日志）
* `computer-use/`

  ：约 130MB（应用本体和运行依赖）
* `v2/checkpoints/`

  ：约 303MB —— **文中的主角**

点进该目录，里面是一个 313MB 的 `.enc` 加密文件，以及一份状态文件（原文贴出的内容如下）：

```
{"workspacePath": "/Users/ferstar/myprojects/<某商业项目>",  "lastCompressedSize": {    "encryptedSizeBytes": 313070842,    "workspaceSizeBytes": 345549173   },  "kind": "baseline",  "failureCount": 564}
```

按原文的解读：

1. 客户端扫描了本地打开的商业项目，排除 `node_modules` 等少量目录后，将剩余 345MB 打包加密为 313MB 的压缩包，标记为 `baseline`（全量快照）；
2. 该包已尝试上传**失败 564 次**，一直卡在本地 `pending/` 目录等待重试。

原文提到，整个项目 10GB，排掉依赖后剩下的 345MB 几乎都是核心资产。

## 它传去了哪：文中还原的两步链路

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPoFaFibzn73E8Sj77EwHOExm2R5TM4vyGt1TaEcammmRasfqnU9FicY8zu6xx1hnKNNfvk1LV1A3Fh96tQfwlrib86RLneAMB5XyY/640?wx_fmt=png&from=appmsg)

文中称日志里未直接打出上传地址，作者遂将客户端的 `app.asar` 解开查看代码，还原出的链路为两步：

1. **先向协调服务器取凭证**

   ：客户端请求 `https://zcode.z.ai`（文中标注为代码里的 `VITE_ZCODE_ENDPOINT_ORIGIN`），服务端返回 OSS 表单签名（`policy`、`x-oss-signature`）、动态分配的 Object Key、大小限制及本次加密所用公钥；
2. **表单直传 OSS**

   ：本地打包、流式加密后，**据称不经业务服务器，直接 HTTP POST 将 `tar.gz.enc` 提交至阿里云 OSS**，再由 OSS 回调通知后端登记。

文中还称，抓包观察到进程常驻的 HTTPS 连接指向 `zcode.z.ai` 的解析 IP 及两个阿里云 OSS 节点。

## 争议最大的一环：那把钥匙在服务端

文中称客户端采用的是标准信封加密（Envelope Encryption），贴出的关键片段如下：

```
keyId: String(i.encryption.key_version),keyWrapAlgorithm: "rsa-oaep-sha256",publicKeySpkiPem: Ylt(i.encryption.public_key)
```

* 文件内容用随机对称密钥以 **AES-256-CTR** 加密；
* 该对称密钥再用 **RSA-OAEP-SHA256** 包裹，所用公钥即上一步由服务端下发者。

原文作者的质疑集中在：**该 RSA 公钥由服务端下发、私钥始终在云端**；他尝试用本机私钥解 envelope 未成功，据此认为本地密文"用户与客户端均无法解开"。

文中的推论是：若目的是为用户提供断点恢复或跨设备同步，密钥理应绑在本地（如 Git、Time Machine 那样）；**一把只有服务端能解开的钥匙，意味着服务端单方面具备解密能力。**（此为原文观点，本号未验证。）

## 快照里装了什么：文中称近九成是 .git

文中称密文虽不可解，但快照生成时在本地留下了 Manifest 清单，作者统计了其中 **42,411 个文件**：

| 内容 | 体积 | 占比 | 包含信息 |
| --- | --- | --- | --- |
| .git/lfs/ | 196.1 MB | 56.8% | LFS 缓存，历史拉过的所有大文件与二进制资产 |
| .git/objects/ | 102.2 MB | 29.6% | 完整 Git 历史对象库（Commit / Tree / Blob） |
| .git/logs/ | 0.6 MB | 0.2% | reflog 轨迹，本地所有分支操作与未推送记录 |
| 其余源码与文档 | ~46.2 MB | 13.4% | `src/` 、各类配置与业务代码 |

按该统计，`.git` 一个目录占 **86.6%**。原文由此认为，云端可能拿到的不只是当前代码，还有仓库的完整历史：

* 早被覆盖删除的敏感配置与历史 key，Git 对象库中仍可能留存；
* 本地尚未推送远端的分支名，可能反映未公开的研发动向；
* `.git/config`

  中配置的内部自建 GitLab 域名与仓库路径。

文中还提到一个 `repo_snapshot_extra_manifest`，称其会对 ZCode 全局配置文件（如 `settings.behavior.json`）取哈希后跨工作区打包，随快照一并上传。

## 开关：文中称两个开关都管不着它

原文作者把设置项与代码逻辑逐个比对后，给出的对照如下：

| 开关 | 容易被理解成 | 文中称实际作用 |
| --- | --- | --- |
| 优化体验 `optimizeAgentExperienceEnabled` | 数据采集 / 遥测上传 | 只管是否用于**模型训练**；关闭后仍会抓快照 |
| 仓库快照索引 `repoSnapshotIndexingEnabled` | 快照功能本身 | 只管服务端拿到快照后**是否建索引**；关闭后本地仍会打包上传 |

文中进一步称，负责快照捕获与上传的 sidecar 在启动时**无条件实例化**，代码中未见针对用户配置的判断分支，唯一前提是 `tokenProvider` 能取到登录后的 JWT。

原文的结论是：**只要登录账号，该上传机制即常开，且 UI 中没有能关闭它的开关。**

文中列出的抓取触发点有两个：一是每次发 Prompt 前的 `captureBeforePrompt`，二是任务结束时的 `repo-wiki-update`；据其日志观察，单个活跃会话最多产生过 **62 次**快照捕获。

## 隐私政策里是怎么写的

文中提到，ZCode 隐私政策确有写明会收集"对话中提交的文本、文件和代码"——这属于 AI 助手调用模型推理的常规环节，各家做法相近。

原文作者称，通篇**未见关于"整个工作区连同完整 Git 历史被打包上传"的说明**，官方文档、FAQ 与更新日志中亦未找到相关描述。

能对应上的只有一句："优化计划默认关闭，不主动加入不会将输入用于训练"——而按前文对照，该开关涉及的是训练用途，而非是否上传。

## 原文给出的应对思路：锁目录

据文中描述，作者首次删除该 pending 包后，半小时内又生成了新的 313MB 压缩包，失败计数从 564 变为 565，因此认为"手动删除只是打地鼠"。

他给出的思路是在文件系统层加不变锁，禁止写入该目录。**以下为原文提供的命令，请结合自身环境评估后再操作：**

macOS

```
# 清空并锁定 checkpoints 目录rm -rf ~/.zcode/v2/checkpointsmkdir -p ~/.zcode/v2/checkpointschflags uchg ~/.zcode/v2/checkpoints# 验证：应输出 Operation not permittedtouch ~/.zcode/v2/checkpoints/test
```

Linux

```
rm -rf ~/.zcode/v2/checkpointsmkdir -p ~/.zcode/v2/checkpointssudo chattr +i ~/.zcode/v2/checkpointstouch ~/.zcode/v2/checkpoints/test
```

文中所述的影响与恢复方式：

* **阻断效果**

  ：写入目录时被内核拦截，无产物生成，后续直传无从谈起；
* **功能影响**

  ："检查点回滚 / 时间线"可能不可用，日常补全、对话、工具调用据称不受影响；
* **恢复方式**

  ：`chflags nouchg ...`（macOS）或 `sudo chattr -i ...`（Linux）。

## 值得讨论的两个问题

抛开具体厂商不谈，原文引发的讨论其实集中在两个层面，我觉得对每个人都适用。

一是**数据范围**。模型推理需要的是与当前任务相关的上下文，而全量仓库快照意味着连同数年的提交历史一并打包。二者的量级完全不同。

二是**密钥归属**。若功能定位是用户侧的断点恢复或跨端同步，密钥理应掌握在用户手里；服务端独占解密能力的设计，会让"加密"这件事在隐私保护上失去意义。

工具本身没有原罪，但数据边界应该由使用者自己来划。在软件层面没有提供开关时，用操作系统层的机制去约束它，也是一种选择。

## 关于本文的表述方式

为避免误读和不必要的争议，说明几点：

1. **本文是转述，不是实测。**

   全部技术细节、数据、代码与命令均来自文首标注的网友原文，本号未做独立复现与验证，不对其准确性作保证。
2. **本文是讨论，不是定性。**

   文中所有判断性表述均为原文作者观点，本号仅作引用与转述；本文不构成对任何企业或产品的侵权指控或结论性评价。
3. **相关厂商如有不同说明，欢迎通过后台联系。**

   本号将在核实后第一时间更正、补充或致歉，并保留原文出处以便读者追溯。
4. **建议读者自行判断。**

   涉及生产环境与商业代码，请以官方文档、隐私政策及厂商正式回应为准，操作前充分评估影响。

参考来源：ferstar，《扒一扒 ZCode 静默上传全量 Git 历史的骚操作》，https://blog.ferstar.org/posts/zcode-silent-workspace-snapshot-upload/（2026-09-18）。本文为转述与讨论，版权与事实以原文及厂商官方说明为准。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS4XfIhhBCwvehx3nP0V2gBqhs9I9AU7GWibxufhGXcjLMNMk2ia7ibpBibhD1qJLmNDcwAGiaTIgyFVQAw/0?wx_fmt=png)

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