---
title: 9.8分！OpenAM爆严重反序列化漏洞，攻击者无需认证即可RCE
url: https://mp.weixin.qq.com/s/9wp9Sj6kFtOHGLMxFGG8UQ
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:48:48.542897
---

# 9.8分！OpenAM爆严重反序列化漏洞，攻击者无需认证即可RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquO6Bn9mz1JichGiaga4FbPJ53EkyYOD6wcibDD5rQa5XdZXfV9FLaq9q42Px8z3SbQ0QXGjMgj3f5lNHBM4cX9ewY9DfAbHCtBorw/0?wx_fmt=jpeg)

# 9.8分！OpenAM爆严重反序列化漏洞，攻击者无需认证即可RCE

小金星
小金星

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 9.8分！OpenAM爆严重反序列化漏洞，攻击者无需认证即可RCE

---

想象一下：攻击者只需发送一个HTTP请求，无需任何账号密码，就能直接在你的企业身份管理服务器上执行任意命令。

这不是科幻，而是刚刚发生的真实漏洞。

2026年4月7日，OpenIdentityPlatform官方发布了**CVE-2026-33439**安全公告，这是一个影响OpenAM的严重反序列化漏洞，CVSS评分高达**9.8分（Critical）**。攻击者可以在**无需任何认证**的情况下，完全控制目标服务器。

---

## 漏洞概述

| 属性 | 内容 |
| --- | --- |
| **CVE编号** | CVE-2026-33439 |
| **CNVD编号** | QVD-2026-18805 |
| **漏洞类型** | 远程代码执行（RCE） |
| **CVSS评分** | 9.8（严重） |
| **影响组件** | OpenIdentityPlatform OpenAM |
| **影响版本** | OpenAM ≤ 16.0.5 |
| **利用条件** | 无需认证，无需用户交互 |
| **POC状态** | 已公开 |
| **EXP状态** | 已公开 |

**危害描述**：攻击者通过发送精心构造的序列化Java对象，可在目标服务器上执行任意操作系统命令，实现完全接管。

---

## 技术分析：一场"补丁绕过"的经典案例

### 1. 漏洞背景：历史漏洞CVE-2021-35464

时间拨回2021年，研究人员发现了OpenAM中的第一个反序列化RCE漏洞——**CVE-2021-35464**。

该漏洞的问题出在 `jato.pageSession` HTTP参数上。OpenAM使用JATO框架（Java Application That Objects）处理Web请求，当用户请求中包含 `jato.pageSession` 参数时，服务器会对其进行**Java反序列化**操作：

```
$ terminal

// 简化伪代码
String sessionData = request.getParameter("jato.pageSession");
Object obj = deserialize(sessionData);  // 直接反序列化用户可控数据
```

由于没有任何类过滤，攻击者可以构造恶意序列化对象，借助Java gadget链（如Apache Commons Collections、Spring框架等）实现远程代码执行。

### 2. 官方修复：WhitelistObjectInputStream

漏洞曝光后，OpenAM官方进行了修复：引入`WhitelistObjectInputStream`类，对反序列化操作实施**类白名单**机制——只有白名单中的类才允许被反序列化。

这看起来是一个"正确"的修复方案。然而，开发者忽略了一个关键问题：

> **JATO框架中，存在第二个反序列化入口点。**

### 3. 被忽视的角落：jato.clientSession

在JATO框架中，除了 `jato.pageSession`，还有另一个参数 `jato.clientSession`，由 `ClientSession.deserializeAttributes()` 方法处理：

```
$ terminal

public class ClientSession {
    public void deserializeAttributes(String sessionData) {
        // 调用 Encoder.deserialize()
        Object obj = Encoder.deserialize(sessionData);
    }
}

public class Encoder {
    public static Object deserialize(String data) {
        // 这里没有白名单过滤！！！
        return new ApplicationObjectInputStream().readObject(data);
    }
}
```

关键问题在于：

●**`jato.pageSession`** 经过 `IOUtils.deserialise()` → 有白名单保护

●**`jato.clientSession`** 经过 `Encoder.deserialize()` → **无任何过滤**

这两个方法使用不同的反序列化入口，后者完全裸奔。

### 4. 攻击链如何工作

攻击者只需要构造一个恶意的序列化Java对象，通过 `jato.clientSession` 参数发送即可：

```
$ terminal

# 攻击Payload结构（概念性）
jato.clientSession = [恶意序列化对象]
```

**利用条件**：

1.目标JSP页面必须包含 `<useClientSession>` 标签

2.密码重置页面完美符合条件：`/ui/PWResetUserValidation`、`/ui/PWResetQuestion`

3.这些页面**无需认证**即可访问

**Gadget链**：OpenAM 16.0.5的WAR包中内置了Click框架的类，攻击者可以利用`Click1` gadget链实现命令执行：

```
$ terminal

// 简化的攻击链原理
ObjectMapper → Click1 Gadget → Runtime.exec()
```

---

## 攻击利用分析

### 攻击条件

| 条件 | 说明 |
| --- | --- |
| 网络要求 | 只需能访问目标OpenAM服务 |
| 认证要求 | **无需任何认证** |
| 用户交互 | **无需用户交互** |
| 目标端点 | 任何包含`<useClientSession>`标签的JATO端点 |

### 典型攻击路径

```
$ terminal

1. 攻击者确定目标OpenAM服务器
2. 定位未授权端点（如 /ui/PWResetUserValidation）
3. 构造恶意序列化payload（使用ysoserial或自定义gadget）
4. 发送GET/POST请求，jato.clientSession参数携带payload
5. 服务器反序列化 → 触发gadget链 → 执行系统命令
6. 获得服务器root/管理员权限
```

### 实际危害

一旦漏洞被利用，攻击者可以：

●✅ 获取服务器完整控制权

●✅ 窃取存储在OpenAM中的所有用户凭据

●✅ 伪造任意用户身份登录企业内部系统

●✅ 横向渗透到其他关联系统

●✅ 部署后门长期潜伏

---

## 影响范围

### 受影响版本

| 版本 | 状态 |
| --- | --- |
| OpenAM ≤ 16.0.5 | 🔴 受影响 |
| OpenAM 16.0.6 | ✅ 已修复 |

### 影响量级

●**影响组件**：OpenIdentityPlatform OpenAM（企业级身份管理解决方案）

●**部署场景**：大型企业、政府机构、金融行业的单点登录（SSO）、身份认证系统

●**风险等级**：由于是开源自研方案，被大量企业二次定制使用，实际影响范围可能达到**万级**以上

---

## 漏洞时间线

| 时间 | 事件 |
| --- | --- |
| 2021年 | CVE-2021-35464 披露，官方修复 `jato.pageSession` |
| 2026年4月 | 研究人员发现 `jato.clientSession` 绕过 |
| 2026-04-07 | 官方发布CVE-2026-33439安全公告 |
| 2026-04-07 | 发布修复版本 OpenAM 16.0.6 |
| 2026-04-08 | NVD正式收录漏洞，POC/EXP在网上传播 |

---

## 处置建议

### ✅ 官方修复方案

**立即升级**：官方已发布修复版本，建议所有用户立即升级。

```
$ terminal

# 升级到最新版本
OpenAM >= 16.0.6

# 下载地址
https://github.com/OpenIdentityPlatform/OpenAM/releases
```

### ⚠️ 临时缓解措施

如果无法立即升级，可采取以下措施：

1.**网络层隔离**

○对OpenAM服务实施访问控制

○禁止外部网络直接访问管理后台

2.**WAF防护**

○在WAF上规则阻断包含 `jato.clientSession` 参数的请求

○规则示例：`block where param jato.clientSession exists`

3.**监控告警**

○监控针对 `/ui/PWReset*` 端点的异常请求

○关注大量来自同一IP的探测行为

---

## 总结

CVE-2026-33439是一个典型的"**修复不完整**"导致的安全漏洞。厂商在修复历史漏洞时，只关注了已知攻击面，而忽略了同一框架中的其他入口点，最终酿成又一场安全危机。

**安全启示**：

1.修复漏洞时，需要全面审视同类问题

2.企业身份管理系统一旦沦陷，影响范围极广

3.面对已公开EXP的漏洞，响应速度至关重要

---

**参考来源**：

●NVD: https://nvd.nist.gov/vuln/detail/CVE-2026-33439

●GitHub Advisory: https://github.com/OpenIdentityPlatform/OpenAM/security/advisories/GHSA-2cqq-rpvq-g5qj

---

*（全文完）*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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