---
title: 当多租户隔离彻底崩溃时（When Multi-Tenant Isolation Completely Falls Apart）
url: https://mp.weixin.qq.com/s/OMcpVFac3vDBkH0Gmuva0Q
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:33:12.597273
---

# 当多租户隔离彻底崩溃时（When Multi-Tenant Isolation Completely Falls Apart）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntrgqVOfkjbHvB4kt4HNh08Il92PfSJGAfqGS5t2xXEAV1wFUOictDcFyw3icsIffjibzaE3nTicFFHIwD4Daz0BZwwibXDBKjOnnpE/0?wx_fmt=jpeg)

# 当多租户隔离彻底崩溃时（When Multi-Tenant Isolation Completely Falls Apart）

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsko6tqqojMnV2NOagEmIr9IeImDzSUYKfnIxDzP2ia4MGN1rPcPE96aYHXChe8UXkFyiaaya7QCW3JMFUbGND5R2ZH8rYBAOZhA/640?wx_fmt=png&from=appmsg)

*2026 年 2 月 — Sahar Shlichove*

---

我在做一次常规安全研究时，随便浏览了一个合作伙伴门户（partner portal），结果发现了一件非常糟糕的事情。

我只是改了一个 HTTP 头，把：

```
X-PRM-TenantId: 986
```

改成：

```
X-PRM-TenantId: 200
```

然后突然之间，我就看到了**另一家公司完整的合作伙伴数据**。

没有登录。
没有绕过技巧。
只是……换了一个数字。

于是我发现，一个被广泛使用的 **PRM（Partner Relationship Management，合作伙伴关系管理）平台**，基本上**没有任何租户隔离机制**。

这篇文章我想讲讲：

* 我是怎么发现的
* 为什么会发生
* 厂商的回应
* 以及大家能从这件事学到什么

---

# 我是怎么发现的

我在分析这个合作伙伴门户的 API 调用方式时，注意到每个请求都有一个 HTTP 头：

```
X-PRM-TenantId
```

里面是一个**纯数字**。

如果你做过 Web 安全测试，这种设计应该会立刻让你不舒服：

**客户端告诉服务器自己属于哪个租户？**

这类设计通常会出问题。

于是我测试了一下，把租户 ID 改成另一个数字。

```
GET /prm/api/objects/v1/Account?take=5 HTTP/1.1
Host: target-portal.platform.example
X-PRM-TenantId: 200
Accept: application/json
```

返回结果：

**187 个合作伙伴账户。**

但它们**不是我的**。

它们属于**平台上的另一家公司**。

---

# 我能看到什么

我花了大约 **1 小时**确认影响范围，然后停止测试并提交漏洞报告。

以下数据完全裸露：

---

## Account API 暴露的数据

返回内容包括：

* 合作伙伴公司名称
* 公司网站
* 收入数据（$1.1M 到 $558M）
* 公司地址与国家
* 合作伙伴等级
* 合作状态
* 销售 pipeline 数据

---

## Forms API 暴露的数据

包括：

* **619+ 邮箱地址**
* **278+ 完整姓名**
* 表单提交时间
* 元数据

---

## Schema API 暴露的数据

包括：

* **完整数据库结构（49 个对象类型）**
* 每个字段定义
* 数据类型
* 枚举值

其中有一个字段特别有意思：

```
Competitor_Products__c
```

里面列出了合作伙伴销售的竞争产品：

```
{
  "fieldName": "Competitor_Products__c",
  "picklistValues": [
"Security Platform A",
"Endpoint Protection Product B",
"Network Security Solution C",
"Cloud Security Platform D"
  ]
}
```

这基本就是：

**竞争情报数据库。**

通常公司要花很多钱才能得到这种信息。

---

最糟糕的是：

**完全不需要认证。**

不需要：

* API Key
* Session Cookie
* 登录

只需要：

```
curl + URL
```

---

# 问题核心：哪里出错了

## 1 租户 ID 由客户端控制

系统完全依赖 HTTP 头：

```
X-PRM-TenantId: 986
```

问题有三个：

1️⃣ 这个值来自客户端
2️⃣ 没有任何认证
3️⃣ 服务器没有验证权限

服务器逻辑基本就是：

> “你说你是 tenant 200？
> 那好，这就是 tenant 200 的数据。”

作者用一个比喻：

就像你走进银行说：

> “我是账户 12345。”

银行柜员回答：

> “好的，这是你的账户记录。”

**完全不检查身份。**

---

## 2 API 完全开放

即使不考虑跨租户问题，这些 API 也不应该公开。

在咖啡店里都能这样：

```
curl"https://any-company.platform.example/prm/api/objects/v1/Account?take=100" \
-H"X-PRM-TenantId: 986"
```

返回：

* 合作伙伴公司
* 收入数据
* 联系人

攻击者可以：

* 爬取合作伙伴名单
* 构建钓鱼攻击
* 收集竞争情报

---

# Forms API 还泄露了个人数据

返回示例：

```
{
  "email": "real.person@real-company.com",
  "firstName": "Real",
  "lastName": "Person",
  "company": "Real Company Name"
}
```

这些是真实用户数据。

作者已做匿名化处理。

---

## GDPR 问题

部分用户来自欧盟。

这违反：

* GDPR Article 5(1)(f)
* GDPR Article 25
* GDPR Article 32

最高罚款：

**2000 万欧元 或 全球营收 4%**

---

# 整个数据库 Schema 都公开

API：

```
/api/_describe
```

返回：

* 49 个对象类型
* 所有字段
* 数据类型

攻击者可以：

* 完整理解数据库结构
* 找出敏感数据位置

虽然 schema 泄露不如数据泄露严重，

但它给攻击者提供了：

**完整攻击地图。**

---

# 为什么会发生

作者报告漏洞后，

厂商第一反应是：

> “这是正常行为。”

是的。

**他们认为这是正常设计。**

---

原因：

客户启用了一个配置：

```
Anonymously Accessible
```

意思是：

**匿名访问。**

厂商说：

系统只是按照配置运行。

客户说：

这显然是安全问题。

---

问题核心：

**安全默认值（secure default）设计失败。**

厂商应该：

* 默认安全
* 用户主动开放

而不是：

* 默认开放
* 用户自己锁。

---

# 正确的实现方式

错误代码示例：

```
@app.route('/api/v1/accounts')
defget_accounts():
tenant_id=request.headers.get('X-PRM-TenantId')
```

这是在：

**信任客户端。**

---

正确做法：

```
@require_authentication
@require_authorization(['read:accounts'])
```

然后：

```
tenant_id = user.get_tenant_id()
```

租户 ID 应来自：

**认证会话**

而不是客户端。

---

还应该在数据库层加保护：

```
ALTERTABLE accounts ENABLE ROWLEVEL SECURITY;
```

策略：

```
CREATE POLICY tenant_isolation
USING (tenant_id = current_setting('app.current_tenant'));
```

即使应用代码出 bug，

数据库仍然会阻止跨租户访问。

---

# 漏洞披露时间线

**2 月 2 日**

作者报告漏洞。

**同一天**

客户联系 PRM 厂商。

**2 月 6 日**

客户修改权限：

* Forms API
* Revenue 数据

变为私有。

**2 月 9 日**

问题修复完成。

总耗时：

**8 天**

这是一个比较理想的披露流程。

---

# 如果被攻击者发现

攻击者可以：

### 1 获取竞争情报

完整合作伙伴网络：

* 谁是合作伙伴
* 贡献多少收入
* 产品销售情况

---

### 2 精准钓鱼攻击

攻击邮件可以写：

> “我看到你的合作伙伴等级需要更新。”

因为攻击者真的知道：

**合作伙伴等级。**

---

### 3 批量抓取数据

* B2B 联系人
* 公司网络
* 商业关系

---

### 4 跨所有租户

攻击者可以循环：

```
X-PRM-TenantId: 1..1000
```

抓取平台上所有公司。

---

# 勒索风险

攻击者可以威胁：

> 我们拥有你所有合作伙伴数据
> 收入数据
> 619 个邮箱

> 不付钱就发给你的竞争对手。

现代勒索组织（如 Cl0p、LockBit）很多时候：

**只偷数据，不加密系统。**

---

# 法律风险

受影响的合作伙伴公司可以起诉：

### 起诉厂商

原因：

**安全设计失职**

---

### 起诉客户公司

原因：

**未保护第三方数据**

---

### 同时起诉两方

通常律师会：

**谁有钱告谁。**

---

# GDPR 风险

潜在后果：

* 72 小时数据泄露报告
* 监管调查
* 巨额罚款
* 民事诉讼

例子：

British Airways 因数据泄露被罚：

**£20M**

---

# 如何测试这种漏洞

安全研究者可以关注：

### 客户端租户 ID

例如：

```
X-Tenant-ID
X-Organization-ID
?tenant=123
```

---

### 子域访问

```
companyB.platform.example
```

尝试访问：

```
tenant=companyA
```

---

### IDOR

```
/api/accounts/123
/api/accounts/124
```

---

### 枚举租户

```
for id in {1..1000}
```

---

### Schema API

```
/api/schema
/api/metadata
```

---

### 无认证访问

删除：

* Cookie
* Token
* Header

看 API 是否返回数据。

---

# 作者的经验

作者总结：

1️⃣ 即使资产不在 bounty scope，也应该报告
2️⃣ 测试要最小化
3️⃣ 不保存数据
4️⃣ 协调所有相关方

---

# 大局观

多租户架构到处都是：

* Salesforce
* Slack
* Zoom
* HubSpot

它非常高效。

但一旦隔离失败：

**整个 SaaS 平台都会受影响。**

---

历史案例：

* Salesforce cross-tenant 漏洞（2007）
* Azure CosmosDB ChaosDB（2021）
* Google Cloud 提权（2020）

---

# 作者给厂商的建议

不要：

**信任客户端租户信息**

必须：

* 从认证会话获取
* 所有 API 需要认证
* 默认安全配置

---

# 给 SaaS 客户的建议

在部署 SaaS 时：

必须检查：

* 默认权限
* API 认证
* 租户隔离机制

---

# 给安全研究者的建议

* 报告漏洞
* 减少测试
* 不保存数据
* 负责任披露

---

这次漏洞 **8 天修复**，说明：

当研究人员和公司合作时，

**安全问题是可以快速解决的。**

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx
* ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnsxpWiaUdXAuUNjxE5YFHqF7QiadAicn7G9hlMa50NU0dHIRBibxic1jS5aHYnu7fFBnEEwPcqLJlUgJ6kqJSvT8LR2TJ2my1xqBxZ8/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntJsvLfG7ObQLAkW7tP4Om4CYC3hoLLyafHAX3h81KfRD80dSsJKOCxkZ87tt58DzEV4wQPx9bRgA2vx3rHCz5zcibiczQeicqWjY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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