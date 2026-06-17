---
title: 基于Chrome MCP与AI的红队自动化加解密工作流
url: https://mp.weixin.qq.com/s/nEV1vZL7kmk7KcU5bKmpfw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:01:40.060991
---

# 基于Chrome MCP与AI的红队自动化加解密工作流

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jkSyaHNyD4ic2UbXV4S6JwAaQDlUBMeKND6RiahsicPBOBGHYY36pdiaoar4OL79XEJdFoic9rss7nIUWOR6Y2O2afkEiaSbbWMvwqtUDoZ4gicHFg/0?wx_fmt=jpeg)

# 基于Chrome MCP与AI的红队自动化加解密工作流

小猴
小猴

亿人安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文首发在：奇安信攻防社区

https://forum.butian.net/ai\_security/188

当目标登录接口被AES-CBC与SM2双重加密，传统爆破工具彻底失效。本文提出一种红队工作流：Chrome MCP自动化逆向提取密钥 + AI生成加密Payload + BurpSuite jsrpc实时加解密，将前端加密防线转化为进攻通道

# 基于Chrome MCP与AI的红队自动化加解密工作流

## 一、研究背景与攻击动机

随着前端加密技术的全面普及，红队测试正面临前所未有的挑战。目标系统的登录接口不再接收明文凭证，取而代之的是经过AES-CBC对称加密或SM2国密算法处理后的密文载荷。部分高安全等级系统甚至采用双重加密策略——先以SM2加密对称密钥，再以AES-CBC加密业务数据，形成多层防护体系。

这一趋势直接导致传统攻击工具体系的结构性失效：

| 工具/方法 | 失效原因 | 表现 |
| --- | --- | --- |
| BurpSuite Intruder | 无法生成合法密文 | 所有爆破请求返回400/403 |
| Hydra/Medusa | 不支持加密预处理 | 无法与目标协议握手 |
| 自定义字典攻击 | 明文载荷被服务端拒收 | 无有效响应 |
| 自动化扫描器 | 缺乏加密载荷生成能力 | 完全丧失探测功能 |

红队迫切需要一套能够穿透前端加密黑箱、自动化完成密钥提取与请求伪造的技术方案。本文基于Chrome DevTools MCP、AI逆向分析与BurpSuite jsrpc，构建了一条端到端的自动化加解密攻击链路，将前端加密防线转化为进攻通道。

## 二、双重加密的技术剖析

### 2.1 常见的双重加密架构

高安全等级系统通常采用混合加密方案，兼顾安全性与性能：

```
┌─────────────────────────────────────────────────────────────┐
│                      客户端加密流程                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  明文数据 ──→ AES-CBC加密 ──→ Base64编码 ──→ 请求体         │
│       ↑                                                     │
│       │                                                     │
│  AES密钥 ──→ SM2公钥加密 ──→ 密钥密文 ──→ 请求头            │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      服务端解密流程                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  密钥密文 ──→ SM2私钥解密 ──→ AES密钥                       │
│       ↓                                                     │
│  请求体 ──→ Base64解码 ──→ AES-CBC解密 ──→ 明文数据         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**第一层：非对称加密（SM2/RSA）** — 保护对称密钥的传输安全。前端使用服务端分发的公钥加密AES密钥，确保只有持有私钥的服务端能够解密。

**第二层：对称加密（AES-CBC）** — 保护业务数据的机密性与完整性。使用随机生成的AES密钥加密请求体，密钥本身被非对称加密保护。

这一架构的理论安全性在于：攻击者即使截获完整请求，在没有SM2私钥的情况下也无法解密AES密钥，进而无法还原明文数据。

### 2.2 攻击面的重新审视

然而，从红队视角看，这一架构存在一个根本性的脆弱点——**加密过程完全发生在客户端**。

这意味着：

* 加密算法实现、公钥、IV等所有密码学参数均存在于前端代码中
* 加密函数是JavaScript运行时中可被调用的公开接口
* 攻击者可以**直接调用前端加密函数**，而非自行实现算法

这一洞察构成了本文攻击方法论的核心：与其逆向算法，不如重用算法；与其提取密钥，不如调用函数。

## 三、自动化攻击架构

### 3.1 整体工作流

本文提出的自动化攻击链路由三个核心组件协同完成：

```
┌─────────────────────────────────────────────────────────────┐
│                    阶段一：密钥与逻辑提取                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Chrome MCP ──→ 自动导航登录页                              │
│       ↓                                                     │
│  AI自动分析 ──→ 定位加密函数、提取公钥/AES密钥/IV            │
│       ↓                                                     │
│  jsrpc注入 ──→ 将加密函数暴露为全局可调用接口                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    阶段二：载荷自动生成                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AI生成Payload ──→ SQL注入/XSS/越权测试载荷                 │
│       ↓                                                     │
│  调用原生加密函数 ──→ 通过jsrpc调用浏览器内加密              │
│       ↓                                                     │
│  生成合法密文 ──→ 可直接提交的有效请求                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    阶段三：BurpSuite集成                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BurpSuite插件 ──→ 拦截请求，识别待加密字段                 │
│       ↓                                                     │
│  jsrpc调用 ──→ 将明文载荷发送至浏览器加密                    │
│       ↓                                                     │
│  替换密文 ──→ 自动完成请求加密并转发                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Chrome MCP：自动化逆向的抓手

Chrome DevTools MCP作为MCP协议的浏览器控制实现，使AI能够程序化地操作Chrome浏览器。在攻击流程中，MCP承担以下任务：

**任务一：自动导航与状态准备**

```
// AI通过MCP执行的自动化操作序列
1. navigate_to("https://target.com/login")
2. wait_for_element("#username", timeout=5000)
3. fill_input("#username", "test_user")
4. fill_input("#password", "任意测试密码")
5. click_button("登录")
6. capture_network_request("/api/login")
```

**任务二：加密函数定位**

```
// AI在控制台执行的代码
// 搜索加密相关全局对象
const cryptoKeys = Object.keys(window).filter(k =>
    k.toLowerCase().includes('encrypt') ||
    k.toLowerCase().includes('sm2') ||
    k.toLowerCase().includes('aes')
);
console.log('候选加密对象:', cryptoKeys);

// 遍历Vue/React组件树查找加密服务
const app = document.querySelector('#app').__vue_app__;
const cryptoService = app.config.globalProperties.$crypto;
```

**任务三：参数提取**

```
// 断点提取密钥与IV
debugger;
// 在加密函数入口处执行
console.log('AES Key:', key);
console.log('IV:', iv);
console.log('SM2 Public Key:', publicKey);
```

### 3.3 AI驱动的加密逻辑分析

AI模型在接收到MCP捕获的请求和源码后，执行以下分析流程：

**第一步：加密类型识别**

| 特征 | 判定 | 后续动作 |
| --- | --- | --- |
| 密文以`04`开头，长度130+字符 | SM2 | 提取公钥，准备SM2加密调用 |
| 密文为Base64，解码后长度16倍数 | AES-CBC | 提取Key和IV，确认填充模式 |
| 同时存在两种密文 | 双重加密 | 定位密钥封装与数据加密的两层逻辑 |

**第二步：调用链追踪**

AI通过MCP的`evaluate_script`能力，在浏览器中执行JavaScript以追踪加密调用栈：

```
// 注入Hook，拦截所有加密相关调用
const originalEncrypt = window.encryptFunction;
window.encryptFunction = function(...args) {
console.trace('Encrypt called with:', args);
debugger; // 触发断点，供AI分析上下文
return originalEncrypt.apply(this, args);
};
```

**第三步：自动化脚本生成**

AI根据分析结果，自动生成jsrpc注入脚本，将加密函数暴露给外部BurpSuite调用。

### 3.4 jsrpc：浏览器与BurpSuite的加密桥梁

jsrpc技术的核心是在浏览器内维持一个常驻的加密服务，通过WebSocket或HTTP与BurpSuite插件通信。

**浏览器端注入脚本**：

```
// 通过Chrome MCP注入
(function() {
// 定位原始加密函数
const aesKey = "7f3a8b2c5d1e9f4a";
const iv = "3c5f7a9b1d3e5f7a";
const sm2PublicKey = "04b9364f5c8a3e2d...";

// 封装加密接口
window.encryptService = {
// AES-CBC加密
aesEncrypt: function(plaintext) {
const encrypted = CryptoJS.AES.encrypt(plaintext,
                CryptoJS.enc.Utf8.parse(aesKey), {
iv: CryptoJS.enc.Utf8.parse(iv),
mode: CryptoJS.mode.CBC,
padding: CryptoJS.pad.Pkcs7
                });
return encrypted.ciphertext.toString(CryptoJS.enc.Base64);
        },

// SM2加密
sm2Encrypt: function(plaintext) {
return SM2Utils.encrypt(sm2PublicKey, plaintext);
        },

// 双重加密：SM2封装密钥 + AES加密数据
doubleEncrypt: function(plaintext) {
const sessionKey = this.generateSessionKey();
const encryptedKey = this.sm2Encrypt(sessionKey);
const encryptedData = this.aesEncryptWithKey(plaintext, sessionKey);
return {
key: encryptedKey,
data: encryptedData
            };
        }
    };

// 启动RPC服务
const ws = new WebSocket("ws://localhost:8080/encrypt");
    ws.onmessage = function(msg) {
const request = JSON.parse(msg.data);
const result = window.encryptService[request.method](request.payload);
        ws.send(JSON.stringify({ id: request.id, result: result }));
    };
})();
```

**BurpSuite插件端**：

插件拦截请求后，识别需要加密的字段，将明文通过WebSocket发送至浏览器加密，接收密文后替换原请求内容。

## 四、实战案例：突破双重加密登录接口

### 4.1 目标分析

某企业后台系统的登录接口采用双重加密架构：

**请求格式**：

```
POST /api/auth/login HTTP/1.1
Host: admin.target.com
Content-Type: application/json

{
"key": "04a3b2c1d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c...