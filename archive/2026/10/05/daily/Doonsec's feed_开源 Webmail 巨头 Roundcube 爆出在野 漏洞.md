---
title: 开源 Webmail 巨头 Roundcube 爆出在野 漏洞
url: https://mp.weixin.qq.com/s/XBmWhSoo0HRH9LAAXwglOg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:22:45.823387
---

# 开源 Webmail 巨头 Roundcube 爆出在野 漏洞

# 开源 Webmail 巨头 Roundcube 爆出在野 漏洞

原创

播风者
播风者

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MSx2fqEGslnmU6zK8IQbZxqdPDsBNP21xF455gnEMHJQE0U7a6pz6k5smicMvbDvBCQv5WNSY8oswdNQSw5uQgLwLzaW5jvAUA/640?from=appmsg)
> **导语**：Roundcube 官方于2026年5月24日悄然发布安全补丁，修复了 CVE-2026-48842（CVSS 8.1）。然而直到9月下旬，加拿大网络安全中心（CCCS）与 SOCRadar 才联合拉响警报——黑客已针对全球仍未打补丁的**50多万台** Roundcube 服务器展开大规模自动化扫荡与实战利用。从补丁发布到在野爆发，中间相隔**整整四个月**，大量企业和政府邮件系统在此期间已沦为黑客的"数据提款机"。

---

## 一、漏洞速览

| 项目 | 详情 |
| --- | --- |
| **漏洞编号** | CVE-2026-48842 |
| **CVSS 3.1 评分** | 8.1（高危） |
| **向量** | AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N |
| **漏洞类型** | SQL 注入（SQL Injection） |
| **受影响组件** | virtuser\_query 插件 |
| **攻击前提** | 无需账号，**预认证攻击（Pre-Auth）** |
| **危害结果** | 越权读取/篡改数据库用户信息、通讯录等敏感资产 |

**风险定级：🔴 高危**——攻击无需凭证，可直接入数据库，影响面广，在野已有利用。

---

## 二、技术根因分析

### 2.1 缺陷位置

漏洞根植于 Roundcube 的 **virtuser\_query** 插件。该插件负责在用户登录验证**之前**，将邮箱地址映射至对应的数据库账号，是 Roundcube 用户认证流程的关键桥梁。

### 2.2 缺陷机理

问题出在 PHP 代码对用户输入的处理环节——使用了存在缺陷的 `preg_replace()` 正则反斜杠转义逻辑。正常流程中，系统应对用户传入的字符进行转义以防止 SQL 语义被篡改；然而攻击者发现，当输入中包含特定构造的**反斜杠转义序列**时，preg\_replace 的转义行为会产生"逃逸"效果：

* 反斜杠在正则替换过程中被二次解析
* 单引号被意外闭合并脱离原 SQL 语句结构
* 攻击者由此注入自定义的 SQL 语句片段

这种绕过方式在 SQL 注入中属于**字符串逃逸**类攻击，经典而高效，且极难被传统规则类 WAF 捕获。

### 2.3 攻击路径

攻击者只需在登录界面或用户查询接口，构造包含特殊反斜杠序列的 Payload，无需任何有效账号，直接发送请求即可触发 virtuser\_query 插件的 SQL 查询。Payload 示例结构（以单引号闭包为核心）：

```
...' OR '1'='1 [构造的反斜杠逃逸序列] --
```

一旦触发成功，攻击者即可：

* 枚举数据库中所有用户账号信息
* 读取/导出通讯录数据
* 在某些配置下可进一步写入或提升权限

![Roundcube CVE-2026-48842 攻击路径示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6M2SzenKsGqZDkXnEfl0QcabOffx9OJ3z4A0RoN2nu432UkyyFvqKvUtVqV6D24klrduRKINuzQIYj7SkHOlaePo4skV5RdF9c/640?from=appmsg "Roundcube CVE-2026-48842 攻击路径示意图")

---

## 三、影响范围

**受影响版本**：

* Roundcube 1.6.x（**1.6.16 之前**的所有版本）
* Roundcube 1.7.x（**1.7.1 之前**的所有版本）

**不受影响版本**：

* Roundcube 1.6.16 及以上
* Roundcube 1.7.1 及以上

---

## 四、修复与应急处置

### 4.1 首选方案：升级

立即升级至以下安全版本：

| 当前分支 | 目标版本 | 下载地址 |
| --- | --- | --- |
| 1.6.x | **1.6.16** | Roundcube 官方仓库 |
| 1.7.x | **1.7.1** | Roundcube 官方仓库 |

> ⚠️ **补丁风险提示**：本次为安全补丁，升级过程通常无需额外停机时间，但建议在非业务高峰时段执行，并在升级前**完整备份数据库及配置文件**。若生产环境使用virtuser\_query插件，升级后需验证用户映射逻辑是否正常。

### 4.2 临时规避措施

若短期内无法完成升级，可通过以下任一方式降低风险：

**方式一：禁用 virtuser\_query 插件**

编辑 `config/config.inc.php`，定位到插件配置段落，将 virtuser\_query 从加载列表中移除：

```
$config['plugins'] = array(
    // 'virtuser_query',  // 注释或删除此行
    '其他插件...',
);
```

> ⚠️ 注意：禁用该插件可能导致依赖邮箱地址→数据库账号映射的认证流程失效，请先在测试环境验证对登录功能的影响。

**方式二：WAF / IPS 规则拦截**

在 Web 应用防火墙或入侵防御系统中添加规则，拦截包含以下特征的请求（仅供参考，攻击者可变换绕过）：

* 包含连续反斜杠序列（如 `\\\\`）的请求参数
* 与 virtuser\_query 插件端点相关的异常 SQL 片段

> ⚠️ 正则绕过方式多变，WAF 规则仅作辅助手段，**不能替代升级**。

---

## 五、在野利用现状

**一个被沉默了四个月的定时炸弹。**

* **2026年5月24日**：Roundcube 官方发布 1.6.16 与 1.7.1，悄然修复该漏洞，未对外公开披露漏洞细节（属于典型的"静默补丁"策略）。
* **2026年9月下旬**：加拿大网络安全中心（CCCS）联合 SOCRadar 发布紧急警报，确认黑客组织正对全球 **50多万台**仍未打补丁的 Roundcube 服务器发起大规模自动化扫荡与定向攻击。
* **低门槛，高收益**：由于该漏洞为预认证（Pre-Auth）型 SQL 注入，攻击者无需任何账号密码，只要服务器暴露在公网即可直接注入，这让黑客的自动化武器化成本极低——一个 Python 脚本 + IP 段列表，即可批量收割。
* **受害者覆盖**：企业邮件系统、政府机构、教育机构均在攻击范围内，通讯录和往来邮件数据已成为主要窃取目标。

---

## 六、总结与行动建议

CVE-2026-48842 是 Roundcube 近年来风险最高的漏洞之一：预认证、SQL注入、在野利用三重高危属性叠加，无需任何凭证即可直捣数据库。建议所有 Roundcube 管理员：

1. **立即**检查当前运行版本，确认是否在受影响范围内。
2. **优先升级**至 1.6.16 / 1.7.1；若暂无法升级，先禁用 virtuser\_query 插件。
3. 检查数据库访问日志，排查是否存在异常的 virtuser\_query SQL 查询。
4. 如生产环境配置不允许直接升级，需制定分阶段修复计划并缩短观察周期。

**漏洞修复窗口已开启，请勿继续等待。**

---

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OhjxQzQweFNUKUpiaj3ZgQVia6mHk0tJt558k2gs2lbg2GYJc40oxejjhZvrDofMuBy0tib4GG9m3VtxXmaSujh6BcCm6hGPCMu8/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OklPPJfDQE2cO0LlDzMOCIeNb5g01ia49sSgKJchHVgiaUo4N3bWahibOeic0WNyIRNJf80icWIeFh7Wegex8mAKzOgSPVleL6XtG0/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MBetynTpiaL535UHyWGUXQvUlvT7WMapaKGvdP8V2srX9hazxneia0alFDWaUuGmBxlEHxyPUEIib3fVcc2xtnyWyIKaic4QQliacI/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MPYWaCGODIIlaw6z3rEGxDibAyz0zIUnlOfz5t85OhTxuo3q19cfFQNgHwrB08ByGB2hvnsEvWicPdibhoL1yXZMW8kYeQ4IDVf8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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