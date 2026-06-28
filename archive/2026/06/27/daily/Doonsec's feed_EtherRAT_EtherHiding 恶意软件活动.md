---
title: EtherRAT/EtherHiding 恶意软件活动
url: https://mp.weixin.qq.com/s/M5PoEYbc5XZ5pFt8X1iWfw
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:12:25.157539
---

# EtherRAT/EtherHiding 恶意软件活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8n4TaM4iabR48QhqicfibmENkQaBlSprXp6Xf234VkEvCzNcRA1WFtGvWrgrqV9veEp0Piape3Uh9YBfKiaOowVqMDic0p9ZLumHwiaSU/0?wx_fmt=jpeg)

# EtherRAT/EtherHiding 恶意软件活动

原创

忍者
忍者

Khan安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8ngEBlos4QoQnNLVtDYxDxMpbXf3ecokz32f7go7fIjjiatzD3alo8WMuwndoIUh0ZXS5Rhc4SaWdrSYjfbcngHAw6YBpQC5MLE/640?wx_fmt=png&from=appmsg)

## **1. 威胁概述**

**威胁名称**：EtherRAT / EtherHiding 变种
**威胁类型**：远程访问木马 (RAT) + 动态C2配置管理
**首次发现**：2024年（根据“The DFIR Report”水印）
**攻击目标**：广泛目标，通过社工诱导用户执行恶意文件
**技术特点**：**利用以太坊区块链作为C2配置存储和分发渠道**，使用Cloudflare隧道作为C2代理，实现高度隐蔽和动态的基础设施管理。

---

## **2. 攻击链详细分析**

### **阶段1：初始感染**

* **向量**

  用户运行恶意文件（可能是通过钓鱼邮件、恶意广告或盗版软件分发）。
* **技术**

  典型的社工攻击，依赖用户执行。

### **阶段2：安装持久化**

* **植入物**

  EtherRAT（EtherHiding变种）安装到主机。
* **持久化机制**

  未在图中明确，但RAT通常会通过注册表、启动文件夹或计划任务实现持久化。

### **阶段3：区块链配置检索（创新点）**

* **核心创新**

  **不直接连接C2服务器，而是从以太坊区块链读取配置**。
* **机制**

+ **不可阻挡**

  区块链去中心化、不可篡改，无法通过传统手段删除配置。
+ **隐蔽性**

  网络流量看起来是合法的以太坊节点通信。
+ **高可用性**

  区块链始终在线，保证了配置的可用性。

+ 恶意软件连接到以太坊网络（可能通过公共节点或内置节点）。
+ 读取特定智能合约或交易数据中的**加密/混淆的C2配置**。
+ **重要澄清**

  区块链本身不是C2服务器，而是**配置分发渠道**。这带来了几个优势：

### **阶段4：C2配置解析**

* **配置内容**

  从区块链获取的配置包含：

+ **真实C2域名列表**

  使用Cloudflare隧道（`*.trycloudflare.com`）。
+ **诱饵域名列表**

  用于混淆和逃避检测。
+ **连接参数**

  端口`443`，协议`HTTPS`，模式`rotate`（轮换）。

* **动态性**

  配置会**定期轮换**，攻击者可通过发布新的区块链交易来更新C2地址。

### **阶段5：C2连接**

* **连接方式**

  通过HTTPS连接到活跃的C2服务器。
* **基础设施**

  使用Cloudflare隧道作为代理，隐藏真实C2 IP，同时提供DDoS保护和SSL加密。

---

## **3. 威胁指标（IOCs）**

### **3.1 网络指标**

| 类型 | 值 | 备注 |
| --- | --- | --- |
| **域名** | `seasonal-estimation-heating-necessarily.trycloudflare.com` | [ACTIVE C2] |
| **域名** | `entered-medications-motherboard-advanced.trycloudflare.com` | [ACTIVE C2] |
| **域名** | `walt-messaging-affairs-occurring.trycloudflare.com` | [ACTIVE C2] |
| **域名** | `estimation.com` | [decoy] |
| **域名** | `entered.com` | [decoy] |
| **域名** | `ag.com` | [decoy] |
| **端口** | `443` | HTTPS |
| **协议** | `HTTPS` | 加密通信 |

### **3.2 区块链相关指标**

* **区块链**

  以太坊（Ethereum）
* **可能的地址/合约**

  需要进一步追踪具体存储配置的以太坊地址（图片未提供具体地址）
* **数据格式**

  加密/混淆的配置数据（可能为JSON或自定义格式）

### **3.3 文件指标**

* **文件类型**

  可执行文件（.exe）、脚本、文档（含宏）
* **哈希值**

  未提供，但需要收集样本进行哈希计算

---

## **4. MITRE ATT&CK 战术技术映射**

| 战术 | 技术ID | 技术名称 | 具体表现 |
| --- | --- | --- | --- |
| **初始访问** | T1566.001 | 钓鱼附件 | 恶意文件分发 |
| **执行** | T1204.002 | 用户执行：恶意文件 | 依赖用户点击 |
| **持久化** | T1547.001 | 注册表运行键/启动文件夹 | 可能的持久化机制 |
| **防御规避** | T1027 | 混淆文件或信息 | 加密的区块链配置数据 |
|  | T1573.002 | 加密信道：非对称加密 | HTTPS通信 |
| **命令与控制** | T1071.001 | Web协议：HTTPS | C2通信 |
|  | T1090.003 | 代理：多层代理 | 使用Cloudflare隧道 |
|  | T1584.004 | 劫持基础设施：服务器 | 利用Cloudflare基础设施 |
| **资源开发** | T1583.006 | 获取基础设施：购买基础设施 | Cloudflare账户、域名 |

---

## **5. 检测与缓解建议**

### **5.1 检测规则（示例）**

```
Yaml

# Snort/Suricata规则示例

alert dns $HOME_NET any -> any any (msg:"MALWARE EtherRAT C2 Domain Query"; dns.query; content:"trycloudflare.com"; nocase; sid:1000001; rev:1;)

alert tls $HOME_NET any -> $EXTERNAL_NET any (msg:"MALWARE EtherRAT C2 SSL Certificate"; tls.sni; content:"trycloudflare.com"; nocase; sid:1000002; rev:1;)
```

### **5.2 行为检测指标**

1. **异常进程**

   ：非浏览器进程（如`svchost.exe`、`powershell.exe`）频繁访问`*.trycloudflare.com`。
2. **以太坊节点流量**

   ：主机与以太坊节点（端口30303 TCP/UDP）通信，尤其是非区块链相关业务主机。
3. **配置文件创建**

   ：在临时目录创建包含加密数据的配置文件。
4. **域名模式**

   ：查询长度超过30字符的随机子域名（如`seasonal-estimation-heating-necessarily.trycloudflare.com`）。

### **5.3 防御措施**

1. **网络层面**：

* 阻止`*.trycloudflare.com`的非业务流量（需评估业务影响）。
* 监控异常HTTPS流量（特别是JA3/JA3S指纹异常）。
* 阻止非授权的以太坊节点通信（端口30303）。

2. **终端层面**：

* 实施应用程序白名单，防止未授权可执行文件运行。
* 使用EDR监控进程链和网络连接。
* 定期审计计划任务、注册表Run键等持久化位置。

3. **威胁狩猎**：

* 搜索日志中与Cloudflare隧道域名相关的DNS查询和SSL握手。
* 分析以太坊区块链交易，寻找可疑的配置存储地址。
* 检查主机上是否有与以太坊相关的异常进程或文件。

---

## **6. 影响评估与威胁等级**

**威胁等级**：**高危（High）**
**理由**：

1. **技术先进性**

   利用区块链作为C2基础设施，传统封锁手段失效。
2. **隐蔽性**

   结合合法云服务（Cloudflare）和加密通信，难以检测。
3. **动态性**

   C2配置可实时更新，攻击基础设施快速变换。
4. **潜在影响**

   一旦感染，攻击者可完全控制受害主机，可能导致数据泄露、勒索软件部署或进一步横向移动。

**归因线索**：图片来自“The DFIR Report”，可能是一个活跃的威胁行为者或恶意软件即服务（MaaS）平台。Cloudflare隧道域名的使用表明攻击者熟悉云基础设施并试图规避传统安全控制。

---

## **7. 总结与建议**

EtherRAT/EtherHiding代表了一种**新型的C2基础设施管理范式**，将区块链的不可阻挡性与云服务的隐蔽性相结合。安全团队应：

1. **更新检测逻辑**

   将区块链节点通信和云隧道域名纳入监控范围。
2. **加强用户教育**

   强调社工攻击风险，不执行来源不明的文件。
3. **威胁情报共享**

   积极共享相关的IOCs和TTPs，特别是以太坊地址和新的C2模式。
4. **评估防御体系**

   检查现有安全控制是否能够检测此类规避技术。

**未来趋势**：预计更多恶意软件将采用类似的去中心化配置分发机制，包括使用其他区块链（如Solana、Polygon）或分布式存储（如IPFS）。安全防御需要向行为分析和异常检测进一步演进。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aPmkR80bcV3JwGBDpU6XB9v8QmVNuqicT4vSSnibBesxWSwrwSORopnXEPcjahRUcLrTDK5MszhYG4ho8icFMuXMg/0?wx_fmt=png)

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