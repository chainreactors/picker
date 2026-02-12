---
title: 从 SQL 注入到文件上传：Upload-Labs 前必须掌握的核心理论基础
url: https://mp.weixin.qq.com/s/kZp_S235993-wZ6g3kifyg
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:17:00.139383
---

# 从 SQL 注入到文件上传：Upload-Labs 前必须掌握的核心理论基础

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5vTt22mqAAxT0slv6rbtVgrq7ibBImIeHNICFtPaA60xVWJZV3Bv1ZZZoVIiaF4Tzbjzvh2HqMkr4O7KZLj7LeAvnpd9kGamUFiax5MQH5eMSw/0?wx_fmt=jpeg)

# 从 SQL 注入到文件上传：Upload-Labs 前必须掌握的核心理论基础

原创

武文学网安
武文学网安

武文学网安

![]()

在小说阅读器中沉浸阅读

大家好，我是武文。

上一篇文章中，我完成了 sqli-labs，并决定进入下一阶段：

👉 文件上传漏洞学习。

这篇文章我决定先整理：

**文件上传的核心理论基础——**服务器到底是如何处理上传文件的**。**

这不是枯燥理论，而是后面所有实战的底层逻辑。

---

# 一、什么是文件上传

文件上传，本质上是一种数据传输行为。

简单来说：

👉 将客户端数据以文件形式封装，通过网络协议发送到服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5vTt22mqAAzffcicUehicRsUm2gLvg3egZ933myxR03IyMy4Adeib0UrMmadwupQ05XszFhciaWmo8X3wfibyybEfCQ9dqdt4PrXtowKee16pWQA/640?wx_fmt=png&from=appmsg)

完整流程：

1️⃣ 用户选择本地文件
2️⃣ 浏览器通过 HTTP 协议发送请求
3️⃣ 通常以 POST 请求提交（multipart/form-data）
4️⃣ Web服务器接收请求并解析
5️⃣ 将文件保存到服务器硬盘

也就是说：

最终目标，是让服务器磁盘上产生一个真实文件。

---

# 二、什么是文件上传漏洞

很多人会误以为：

文件上传漏洞 = 上传文件。

其实不是。

真正的定义是：

👉 用户上传了一个可执行脚本，并通过它获得服务器执行能力。

重点在：

不是上传行为本身，而是：

👉 **服务器如何处理上传后的文件。**

如果：

* 服务器未严格验证
* 过滤机制不完善
* 文件解析存在问题

攻击者就可能上传：

```
php / asp / jsp 等脚本
```

然后获得 WebShell。

---

## 为什么现实中经常出现？

因为绝大多数网站都有上传功能：

* 头像上传
* 附件上传
* 图片分享
* 富文本编辑器

而这些地方：

往往验证不足。

---

# 三、文件上传漏洞产生的原因

这是 upload-labs 后面所有关卡的核心。

---

## 1️⃣ 服务器配置不当

例如：

* upload目录允许执行脚本
* 解析规则配置错误

---

## 2️⃣ 上传限制被绕过

开发者通常只检查：

```
是否为 .jpg
```

但攻击者可以：

* 双扩展名
* 特殊后缀
* 编码绕过

---

## 3️⃣ 开源编辑器上传漏洞

很多网站直接使用：

* 富文本编辑器
* 文件管理插件

配置错误极易产生漏洞。

---

## 4️⃣ 文件解析漏洞

经典案例：

```
shell.php.jpg
```

服务器解析错误导致执行。

---

## 5️⃣ 过滤不严

例如：

* 只检测文件名
* 不检测文件内容

---

# 四、文件上传漏洞的危害

一旦上传成功并执行。

攻击者可能：

* 执行服务器命令
* 管理数据库
* 浏览服务器文件
* 获取系统权限

这种恶意脚本，通常叫：

👉 WebShell。

---

# 五、文件上传的检测方式（重点）

upload-labs 本质就是：

逐步突破这些检测。

---

## 1️⃣ 客户端 JavaScript 检测

例如：

```
只能上传 jpg
```

特点：

* 仅浏览器检查
* 非常容易绕过

方法：

👉 BurpSuite 改包。

---

## 2️⃣ 服务端 MIME 类型检测

检测：

```
Content-Type
```

问题：

这是客户端可控字段。

---

## 3️⃣ 服务端目录路径检测

限制：

* upload目录
* path参数

目标：

防止目录穿越。

---

## 4️⃣ 文件扩展名检测

最常见。

例如：

```
禁止 .php
```

绕过方式：

* 双扩展
* 大小写
* 特殊字符

---

## 5️⃣ 文件内容检测

例如：

* 图片头校验
* 代码扫描

难度较高。

---

# 六、上传成功 ≠ 攻击成功

真正攻击成功必须：

```
可上传
+ 可访问
+ 可执行
```

很多情况下：

* 文件能上传
* 但服务器不会执行。

---

# 七、为什么文件上传是 SQL 注入后的最佳下一步

SQL 注入：

👉 控制数据库。

文件上传：

👉 控制服务器行为。

意味着：

从：

```
数据层 → 系统层
```

开始升级。

---

# 结语

完成 sqli-labs 后，我才真正意识到：

网络安全不是单一漏洞，而是一条完整攻击链。

信息收集 → SQL 注入 → 文件上传 → WebShell。

这篇文章，是进入 upload-labs 前的理论准备。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

武文学网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

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