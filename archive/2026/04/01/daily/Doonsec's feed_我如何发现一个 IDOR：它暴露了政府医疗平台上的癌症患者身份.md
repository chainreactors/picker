---
title: 我如何发现一个 IDOR：它暴露了政府医疗平台上的癌症患者身份
url: https://mp.weixin.qq.com/s/UlgNlVLEx4N-ZAYpm1NcWw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:25:57.909661
---

# 我如何发现一个 IDOR：它暴露了政府医疗平台上的癌症患者身份

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnt0zI1G4QQnaiczZz2OkpbXlASk0jqtSicFPz4lukR2U8Ag2bawlicmibrDJ6BMicrOTCU32nbicAWzAjULDdNh37UmmgBvjvBObK0TY/0?wx_fmt=jpeg)

# 我如何发现一个 IDOR：它暴露了政府医疗平台上的癌症患者身份

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

##

## ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBntiaMHpJutgk0n9G5z9QLQOib1PgDiaabYa48nraYBf9I0LhDwn0YpMLKxHxDH9g51C0jva2Wkk8CkBtgoMlLpV3WjJicahVDQbKXk/640?wx_fmt=jpeg&from=appmsg)

## 引言

在一次经过授权的漏洞赏金（bug bounty）测试中，我与合作伙伴 **itsnotthathard** 一起，在一个患者门户中发现了一个 **不安全直接对象引用（IDOR）漏洞**。

该应用是一个基于 **Odoo 17.0** 的定制肿瘤中心模块，用于管理癌症患者的预约、医疗记录以及治疗流程。

一个**自注册用户**（与任何患者记录都没有关系）通过滥用一个开发者忘记限制权限的 JSON-RPC 方法，成功枚举出了系统中**所有癌症患者的全名**。

最终影响非常严重：

* 约 **2800+ 医疗记录**
* 约 **3000+ 预约记录**
* 约 **48900+ 内部医疗消息**

这些数据全部泄露给任何可以注册账号的人。

---

## 目标系统

该门户允许患者通过基础信息和社会安全号码进行注册。

系统只校验身份证号的**格式校验位（checksum）**，但没有与后端数据库核验。

因此，任何人都可以生成一个“看似合法”的号码并注册成功。

登录后界面看似安全：

* 只能看到自己的数据
* 无法看到其他患者信息
* 无法访问其他记录

表面上完全正常。

但漏洞从来不会在“表面”。

---

## 侦察：理解 Odoo 的 RPC 层

如果你做过 Odoo 安全测试，会知道它的 Web 前端只是一个薄客户端，所有操作都通过 **JSON-RPC API**：

`/web/dataset/call_kw`

所有按钮、页面加载、数据请求最终都会调用：

* 模型（model）
* 方法（method）
* 参数（args）

---

### Odoo 常见数据访问方法

| 方法 | 作用 |
| --- | --- |
| `read` | 按 ID 读取完整记录 |
| `search_read` | 搜索 + 读取 |
| `web_read` | 前端优化读取 |
| `export_data` | 批量导出 |
| `name_get` | 返回 `(id, display_name)` |

---

前四个是“重型方法”，通常会被 ACL（访问控制）严格限制。

但 `name_get` 呢？

它只是返回一个名字，看起来完全无害。

但在医疗系统里——**非常危险。**

---

## 发现过程

我首先测试最直接的方式：

```
Model: vcc.medical.finding
Method: read
IDs: [3809]
```

返回：

> ❌ AccessError（访问被拒绝）

很好，权限正常。

同样测试：

* `search_read`

  ❌
* `web_read`

  ❌
* `export_data`

  ❌

都被阻止。

---

### 关键一步：测试 name\_get

我尝试：

```
{
  "model": "vcc.medical.finding",
  "method": "name_get",
  "args": [[3809, 3808, 3807, 3800, 3700]]
}
```

结果：

✅ 返回成功
✅ 返回真实患者姓名
❗ 没有任何权限限制

---

### 结果

系统返回的 `display_name` 类似：

```
“Medizinische Befunde: [患者姓名]”
```

直接把患者身份嵌入返回值中。

---

## 进一步测试：影响范围

我继续测试其他模型：

### 📌 vcc.appointment

约 3000+ 预约记录

### 📌 res.users

所有注册患者用户

### 📌 mail.message（最大问题）

约 48900+ 条内部消息

这些消息包含：

* 治疗流程
* 医疗更新
* 内部沟通
* 医护交接信息

全部都嵌入患者姓名。

---

## 根本原因：`.sudo()` 反模式

在错误堆栈中发现关键代码：

```
record.display_name =_("Tumor Board: %s") %record.sudo().case_id.patient_id.name
```

### 问题点：

`.sudo()` 在 Odoo 中代表：

> 以超级管理员权限执行，绕过所有 ACL

开发者这样写的初衷是：

* 为了让 display\_name 在 UI 中正确显示
* 访问关联字段 case → patient → name

---

### 但实际发生了什么？

* `name_get`

  会触发 `display_name`
* `display_name`

  使用 `.sudo()`
* `.sudo()`

  绕过权限控制
* 所有人都能获取患者姓名

---

## 核心问题总结

这不是简单的访问控制失败，而是：

> **“安全方法调用了不安全的超级权限路径”**

---

## 关键经验总结（渗透测试角度）

### 1. 不要只测 read

Odoo 中必须单独测试：

* `read`
* `name_get`
* `name_search`
* `fields_get`

---

### 2. display\_name 是攻击面

如果 `display_name` 包含敏感信息：

* 姓名
* 邮箱
* ID

并且使用 `.sudo()`
👉 就可能导致 IDOR

---

### 3. 医疗系统影响极大

同样漏洞：

* 普通系统：低危
* 医疗系统：GDPR 高危违规 + 隐私泄露

---

### 4. 不一致就是证据

如果：

* A 模型禁止 `name_get`
* B 模型允许

👉 说明是设计错误，而不是正常行为

---

### 5. 初始拒绝不代表漏洞无效

很多漏洞需要：

* 重新表达
* 简化影响
* 再提交

---

## 最终结论

这个漏洞技术上非常简单：

* 一个 RPC 方法
* 一个缺失权限检查
* 一个 `.sudo()` 调用

但影响极其严重：

> 数千名癌症患者的身份信息被暴露

---

## 最后的思考

最危险的漏洞往往不是复杂逻辑，而是：

> “大家都以为它是安全的地方”

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx
* ![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnticREf3VyfYesm0aoCmIDZGZcN3NJ3tibHmF2ia5DTyWy6n8iajuYU4TYVTKf9CsT4mXgmbVGdCqZdXz85lkTQXJnks3MOEUcVF0w/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

##

![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvoTp0padsQkToVONTUUxXwCVmyup0CzMsABrvfE2wOv8I1dVWQon4pkTp3ocnHpomr3M3YtrWeXb5TyBZpEnibI9GOTatXMPg0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

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