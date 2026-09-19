---
title: 【突发】ZCode静默上传全量Git历史，请快速自查
url: https://mp.weixin.qq.com/s/pjojxB16hQ98JFOeTgbDGA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:56:24.042697
---

# 【突发】ZCode静默上传全量Git历史，请快速自查

# 【突发】ZCode静默上传全量Git历史，请快速自查

原创

ferstar
ferstar

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 一、发生了什么

**只要处于登录状态，ZCode（智谱官方AI编程桌面端）就会在后台静默将整个工作区——包括完整的`.git`历史、LFS大文件缓存、reflog以及全局应用配置——打包加密，直传阿里云OSS。**macOS与Windows两侧均已独立实测坐实。

更关键的架构事实：**加密用的RSA公钥由服务端随上传凭证动态下发，私钥只存在于云端**——本地生成的那份几百MB密文，用户和客户端本体都解不开。

起点很偶然：清理磁盘时发现`~/.zcode`占用超过700MB，其中`v2/checkpoints/`（快照投料区）就有约303MB，里面躺着一个313MB的`.enc`加密文件。顺手删掉后，**半小时内它又重新打包了一份**——这不是缓存，是一个常驻的重传机制。

## 二、证明真假：证据链

### 2.1 本机物证（macOS）

快照投料区内的状态文件：

```
{
  "workspacePath": "/Users/ferstar/myprojects/<某商业项目>",
  "lastCompressedSize": {
    "encryptedSizeBytes": 313070842,
    "workspaceSizeBytes": 345549173
  },
  "kind": "baseline",
  "failureCount": 564
}
```

解读：

1. 客户端扫描本地打开的商业项目，排除`node_modules`等少量目录后，把剩下345MB内容打包加密成313MB的`baseline`（全量快照）；
2. 上传已失败**564次**，密文滞留本地`pending/`目录持续重试。

该项目总规模10GB，排除依赖后剩下的345MB**几乎全是核心资产**。

### 2.2 本机物证（Windows）

Windows端数据根目录为`%USERPROFILE%\.zcode`，快照投料区同样在`v2\checkpoints`，按工作区哈希分目录。独立复核的证据比macOS侧更完整：

* 共**32个工作区**被抓过快照（只要在该工作区里发过prompt即中招）；
* 最大单包**107MB**（某含模型文件的项目），重试失败**152次**；
* 约**14个工作区无失败记录=已成功上传入库**，多为几十KB~几百KB的小仓；
* `lastAcceptedManifestHash`字段普遍存在，说明服务端至少受理过manifest；
* **关键语义**：`failureCount`只代表最近一次重试失败——`baseline`很可能早已成功上传。判断"从未泄露"的唯一依据是它从来没成功过，而这种情况基本不存在。

### 2.3 逆向证据：上传链路还原

日志未直接暴露上传地址，对客户端`app.asar`逆向后，整条链路还原如下：

![image](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpficHa0VPseIcwKoZDL0wX7xAd25UWAZIqkmI2gEByHDwicr4hMg9S25dUcHbl4EiavdgIVfIF4razZHiamfibJVhxpibyib2MCkGXMA/640?wx_fmt=webp&from=appmsg)

image

两步流程：

1. **向协调服务器要凭证**：客户端请求`https://zcode.z.ai`（代码中的`VITE_ZCODE_ENDPOINT_ORIGIN`常量），服务端返回OSS表单签名（`policy`、`x-oss-signature`）、动态Object Key、大小限制，以及**本次加密要用的RSA公钥**；
2. **表单直传OSS**：客户端本地打包并流式加密后，**不经过智谱业务服务器**，直接HTTP POST表单把`tar.gz.enc`甩给阿里云OSS；传完后由OSS服务端callback通知智谱后端登记。

流量特征佐证：进程常驻HTTPS连接为`zcode.z.ai`的解析IP外加两个阿里云OSS节点。且**bucket域名由服务端动态下发、从不落客户端日志**——想靠hosts拉黑OSS的路线走不通。

### 2.4 加密与密钥托管证据

客户端采用标准信封加密（Envelope Encryption）：

```
keyId: String(i.encryption.key_version),
keyWrapAlgorithm: "rsa-oaep-sha256",
publicKeySpkiPem: Ylt(i.encryption.public_key)
```

* 文件内容以随机生成的对称密钥经**AES-256-CTR**加密；
* 对称密钥以**RSA-OAEP-SHA256**包裹，所用公钥即服务端随上传凭证动态下发的那把。

**密钥托管分析**：RSA公钥是服务端临时给的，私钥从头到尾只在云端。实测用本机全部私钥尝试解envelope均失败。这意味着：

> 本地硬盘上的密文，用户打不开，ZCode客户端自己也打不开，全天下只有智谱后端的私钥能解。

若该机制真为断点恢复/跨设备同步而设计，密钥理应绑定本地（如Git、Time Machine的做法）。**一把只有服务端能解开的钥匙，唯一的功能是保证服务端单方面可读。**

### 2.5 开关与隐私政策对照：默认常开、UI关不掉

| 开关 | 你以为它管 | 实际管 |
| --- | --- | --- |
| **优化体验** （`optimizeAgentExperienceEnabled`） | 数据采集/遥测上传 | **只管要不要拿你的数据训练模型** 。关闭后快照照抓、照传 |
| **仓库快照索引** （`repoSnapshotIndexingEnabled`） | 快照功能本身 | **只管服务端拿到快照后要不要建索引** 。关闭后本地打包上传一点不落 |

客户端组装代码证实：负责快照捕获与上传的sidecar在启动时**无条件实例化**，代码中不存在任何针对用户配置的条件判断，唯一前提是`tokenProvider`能取得登录JWT。

> **结论：只要登录账号，上传机制即常开，UI中不存在任何可关闭它的开关。**

隐私政策对照：政策明确写了会收集"对话中提交的文本、文件和代码"——这属于AI助手推理的常规操作。但通篇**只字未提**会将整个工作区连同完整Git历史静默打包上传；官方文档、FAQ、更新日志同样毫无说明。唯一能对上的只有一句万能套话："优化计划默认关闭，不主动加入不会将输入用于训练"。

**补刀**：快照行为与模型渠道无关——即使配置了第三方API（自建中转/OpenAI兼容端点），推理内容确实直连你的`baseUrl`，但快照sidecar**只认登录态JWT**：用谁的模型，它都照拍、照传。

## 三、上传了什么

### 3.1 Manifest量化统计

密文不可解，但快照生成时留下的Manifest（文件清单）明文写在本地。对这份包含**42,411个文件**的清单统计如下：

| 内容 | 体积 | 占比 | 包含的信息 |
| --- | --- | --- | --- |
| `.git/lfs/` | 196.1 MB | 56.8% | LFS缓存：项目历史中下拉过的所有大文件与二进制资产 |
| `.git/objects/` | 102.2 MB | 29.6% | 完整Git历史对象库（Commit、Tree、Blob） |
| `.git/logs/` | 0.6 MB | 0.2% | reflog轨迹：本地所有分支操作与未推送记录 |
| 其余源码与文档 | ~46.2 MB | 13.4% | `src/` 、各类配置文件与业务代码 |

**`.git`一个目录占整包86.6%。**云端拿到的远不止当前工作区代码，而是仓库自创建以来的全部历史：

* 早已被覆盖删除的敏感配置与历史key；
* 尚未推送远端的分支名（直接暴露未公开的研发动向）；
* `.git/config`中的内部自建GitLab域名与仓库路径。

### 3.2 extra-manifest搭车

代码中另有一个`repo_snapshot_extra_manifest`：对ZCode全局配置文件（如`settings.behavior.json`）计算哈希后，**跨工作区打包，随每次快照一起上传**。

Windows侧复核补充了更严重的风险点：ZCode的`model-providers.json`/`provider_config.json`中保存着**明文API key**——该目录理论上一直处于可被端走的射程内。因此`.zcode\v2`目录不应整体交给任何网盘同步。

### 3.3 触发时机

抓取触发点有两个：

* `captureBeforePrompt`：**每次发送Prompt前**（`captureStage=prompt`）；
* 任务结束时标记`repo-wiki-update`（`captureStage=terminal`）。

日志统计显示，单个活跃会话最多可产生**62次**快照捕获。

## 四、怎么解决

**为什么删除无效**：手动删pending包是打地鼠——实测删除后半小时内即重新打包（`failureCount`从564增至565），上传器发现本地文件缺失会直接重造。设置里的开关也管不着（见2.5）。

**防御思路**：让快照**无米下锅**——在文件系统/代码层面从内核级阻断写入。客户端的IO报错会被自身吞掉，对话、补全、工具调用全部正常，唯一失效的是"检查点回滚/时间线"功能（该功能本就是拿全量代码上云换来的）。

### 4.1 macOS：`chflags`不可变锁

```
# 清空并锁定checkpoints目录
rm -rf ~/.zcode/v2/checkpoints
mkdir -p ~/.zcode/v2/checkpoints
chflags uchg ~/.zcode/v2/checkpoints

# 验证：应该输出Operation not permitted
touch ~/.zcode/v2/checkpoints/test
```

回滚：`chflags nouchg ~/.zcode/v2/checkpoints`

### 4.2 Linux：`chattr +i`不可变锁

```
# 清空并锁定checkpoints目录
rm -rf ~/.zcode/v2/checkpoints
mkdir -p ~/.zcode/v2/checkpoints
sudo chattr +i ~/.zcode/v2/checkpoints

# 验证：应该输出Operation not permitted
touch ~/.zcode/v2/checkpoints/test
```

回滚：`sudo chattr -i ~/.zcode/v2/checkpoints`

### 4.3 Windows第一层：ACL锁死投料目录（等价`chattr +i`）

先**彻底退出ZCode（含托盘）**，然后管理员PowerShell：

```
$ck = "$env:USERPROFILE\.zcode\v2\checkpoints"

# 清空历史投料（含pending密文包，留着本地也解不开）
Remove-Item "$ck\*" -Recurse -Force

# 可读、拒绝一切写入/追加/改属性（deny优先于grant）
icacls $ck /inheritance:r /grant "${env:USERNAME}:(OI)(CI)(RX)" /deny "${env:USERNAME}:(OI)(CI)(WD,AD,WEA,WA)"

# 验证：应报Access denied
New-Item "$ck\test.txt" -ItemType File -EA Stop
```

回滚：`icacls $ck /remove:d "$env:USERNAME"`

### 4.4 Windows第二层（可选，更彻底）：字节级stub快照咽喉

两种captureStage在`app.asar`中最终汇聚到唯一方法`captureBeforePrompt(t)`。将其开头改为无条件`return`，并做**等长替换**——asar头表与文件大小一字节不变，无需重打包：

```
$asar = '<ZCode安装目录>\resources\app.asar'
Copy-Item $asar "$asar.bak"                      # 先备份，300MB级别
$enc = [Text.Encoding]::GetEncoding(28591)       # Latin-1，字节双射，文本偏移=字节偏移
$t = [IO.File]::ReadAllText($asar, $enc)

$m = [regex]::Match($t, 'async captureBeforePrompt\(([A-Za-z$_]+)\)\{([A-Za-z$_]+)\.workspaceIdentity\?\.trim\(\)\|\|await this\.captureScheduler\.schedule')
if (-not $m.Success) { 'pattern not found（版本变了或已stub），abort'; exit 1 }

$hdr  = "async captureBeforePrompt($($m.Groups[1].Value)){"
$pos  = $m.Index + $hdr.Length
$len  = $m.Groups[2].Value.Length + '.workspaceId'.Length
$repl = 'if(1)return;'.PadRight($len)             # 等长填充，语法仍合法，unreachable

$fs = [IO.File]::Open($asar, 'Open', 'ReadWrite', 'None')
$fs.Seek($pos, 'Begin') | Out-Null
$b = $enc.GetBytes($repl); $fs.Write($b, 0, $b.Length)
$fs.Dispose()
```

原理说明：

* 替换目标：`{t.workspaceIdentity?.trim()||await ...}` → `{if(1)return; <空格补齐>...}`；
* 函数直接短路，prompt前捕获、任务结束捕获、搭车上传一起失效；
* 该方案可行有一个前提：当前版本（3.12.3）Electron fuse中`EnableEmbeddedAsarIntegrity = DISABLED`，官方未开启asar完整性校验；
* **切勿用文本编辑器打开asar**，必须全程按字节流处理（Latin-1编码保证文本偏移=字节偏移）；
* 建议将该脚本做成启动器中的幂等步骤（匹配到pattern就打、已stub就跳过、结构变化就报错），软件自动更新后防御自动续命。

### 4.5 验证与实测结果

```
# 启动ZCode干一轮活后检查：
# 1. checkpoints目录应保持为空
gci "$env:USERPROFILE\.zcode\v2\checkpoints" -Recurse -Force | Measure-Object
# 2. 进程应稳定存活（stub语法错误的话主进程秒挂）
```

Windows实测：**stub+目录锁双闸**开启后正常干活，`checkpoints`始终0文件；两道保险互相独立、互为兜底。

### 4.6 已上传数据的止损

* **无法召回**：信封加密私钥只在云端，用户只能确认"本地不再新增"，已上传的密文无法要求删除或自行销毁；
* **仓库级止损**：涉及真实敏感内容（密钥、商业代码、内部GitLab地址、未推送分支）的仓库，建议直接**轮换密钥、清理历史**（如`git filter-repo`重写后再强推），并评估内部域名与凭据的暴露面；
* **本机残留清理**：删除pending密文包（本地也解不开，无保留价值）。

## 五、结语

模型推理吃代码上下文，属于AI编程工具的固有代价，用户普遍知情。真正越线的是四点同时成立：

1. **数据范围**：整仓+全部Git历史（`.git`占86.6%），远超推理所需上下文；
2. **密钥姿态**：只有服务端能解的加密——这不是为用户准备的备份，而是单方面可读的采集；
3. **默认常开、UI关不掉**：sidecar无条件实例化，两个相关开关均不触及捕获与上传本身；
4. **零披露+自动重传**：隐私政策只字未提，删包半小时内自动重建，564次失败仍持续重试。

工具没有原罪，但红线应由使用者自己划。既然软件里关不掉，就用操作系统的锁（`chflags`/`chattr`/ACL）和字节级stub把它关进笼子里。

## 参考来源

* 扒一扒ZCode静默上传全量Git历史的骚操作—ferstar(https://blog.ferstar.org/posts/zcode-silent-workspace-snapshot-upload/)
* 急！！！ZCode静默上传整仓快照：Windows实测证实+三重防御落地—NodeSeek(https://www.nodeseek.com/post-935260-1)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/O57ZTjAp9KOL0JJPSBRFM8Y3GwpOwWSpDSvWexu4uJ40TCnMzqRM9JQOxx8KibqwUWUXdicAXohNyARfdV9agCFw/0?wx_fmt=png)

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