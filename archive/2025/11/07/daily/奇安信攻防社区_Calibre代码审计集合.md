---
title: Calibre代码审计集合
url: https://forum.butian.net/share/4635
source: 奇安信攻防社区
date: 2025-11-07
fetch_date: 2025-11-08T03:01:09.982359
---

# Calibre代码审计集合

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Calibre代码审计集合

* [漏洞分析](https://forum.butian.net/topic/48)

Calibre 是一款跨平台的免费开源电子书软件套件。Calibre 支持将现有电子书组织到虚拟图书馆中，显示、编辑、创建和转换电子书，以及将电子书与各种电子阅读器同步。支持编辑 EPUB 和 AZW3 格式的书籍。本文介绍了Calibre近期披露的3个CVE漏洞。

前言：
---
Calibre 是一款跨平台的免费开源电子书软件套件。Calibre 支持将现有电子书组织到虚拟图书馆中，显示、编辑、创建和转换电子书，以及将电子书与各种电子阅读器同步。支持编辑 EPUB 和 AZW3 格式的书籍。本文介绍了Calibre近期披露的3个CVE漏洞。
环境搭建：
-----
漏洞影响版本：&lt;=7.14.0
项目地址：[calibre](https://github.com/kovidgoyal/calibre)
Python setup.py build\\_dep windows #构建依赖项
Python setup.py win64 --dont-sign #安装
安装后在操作页面开启服务
![image-20251030104714576](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa58293552ebb5b1ff77e84e912c3cc2e.png)
![image-20251030104733565](https://oss-yg-cztt.yun.qianxin.com/butian-public/f5f7a333908f1b12ce55da40e94b7b1ea.png)
Calibre拓展：
----------
通过对披露的漏洞细节进行分析，了解到各个模块文件主要是通过cdb.py调用，其中定义了Calibre对于电子书数据库执行操作所用到的一系列API。路由器会根据传入的HTTP请求路径动态地导入一个辅助模块，其命名格式为`cmd\_\*.py`。例如当请求`/cdb/cmd/export`路由的时候，路由器将解析出对应的模块名称`cmd\_export.py`，并调用其中的函数执行，发包请求体中的内容会作为对应的参数传入从而触发相应的操作。
首先定位到src/calibre/srv/cdb.py文件看下核心代码：
![image-20251030104751090](https://oss-yg-cztt.yun.qianxin.com/butian-public/f2a481b4935e87f246a527e43cc2c9a43.png)
代码中的 `module\_for\_cmd(which)`函数根据 which 参数动态加载模块。如果加载的模块没有设置 readonly 属性或 readonly 属性为 False，会取反结果为true，下来代码会调用`ctx.check\_for\_write\_access(rd)`检查写权限。这里模块的加载是动态的，且`module\_for\_cmd(which)`函数没有对 which 参数进行路径限制或校验，从这里攻击者可以传入相对路径或包含恶意路径的模块名，从而通过控制 which 参数去加载其他模块。如果存在某个模块其中readonly 属性被设置为 True，那么可以通过传入该模块名去绕过 `ctx.check\_for\_write\_access(rd)` 的检查。下来通过`m.implementation`方法调用对应模块的`implementation` 方法，传入用户构造的参数，实现调用不同的功能模块并执行相关模块的主要功能。
一、CVE-2024-6781（任意文件读取漏洞）：
--------------------------
### 1.1漏洞分析：
由披露的paylaod可知该漏洞的来源在于cmd\\_export.py文件，下来定位到`src/calibre/db/cli/cmd\_export.py`进行分析，可以看到这里 readonly 模块变量为True，此时`check\_for\_write\_access()`函数不会被触发，绕过了检查。当传入的action为`extra\_file`时，`db.copy\_extra\_file\_to()`方法从用户提供的HTTP参数去构建相对路径，直接用于读取文件内容，并将其存储到 BytesIO 变量中返回给用户。
![image-20251030104808056](https://oss-yg-cztt.yun.qianxin.com/butian-public/fd4239d83d7497b46d9b510c12a0d1b3f.png)
由于没有对传入的relpath 参数进行过滤和路径限制，攻击者可以构造恶意路径去包含路径遍历的字符串，导致存在任意文件读取漏洞。
### 1.2漏洞复现：
根据漏洞分析结果构造如下请求包
POST <http://ip:8080/cdb/cmd/export> HTTP/1.1
Host: ip:8080
Content-Type: application/json
​
\["extra\\_file", 1, "../../../../../Users//321.txt", ""\]
利用情况如下：
![image-20251030104820413](https://oss-yg-cztt.yun.qianxin.com/butian-public/fdb4ddf7256a07f9c97865974308a86a3.png)
二、CVE-2024-6782（远程代码执行）：
------------------------
### 2.1漏洞分析：
定位到src/calibre/db/cli/cmd\\_list.py进行分析：
此处readonly值为True，不会进行权限校验。
![image-20251030104829706](https://oss-yg-cztt.yun.qianxin.com/butian-public/f40714c0d28ff66306b70a8cceb8fa4b8.png)
该函数主要功能是根据用户输入的查询信息去查询书籍并返回查询的结果，其中template模板参数由用户控制是否传参。
![image-20251030104842491](https://oss-yg-cztt.yun.qianxin.com/butian-public/f0b2c5a2b56278670eecba19e39657032.png)
在 `implementation()` 函数中，当 `field == 'template'` 时，可以提供一个模板去处理搜索到的结果。此时代码会初始化一个字典 `vals` 存储每本书的格式化结果，下来调用 `safe\_format` 方法处理用户提供的 `template` 参数。该方法会对传入的模板内容进行格式化，确保生成的模板内容安全有效，并将格式化后的结果存储在 `data['template']` 中。
![image-20251030104855417](https://oss-yg-cztt.yun.qianxin.com/butian-public/f60b27298aaea853f0e7bb6ca29beb7f1.png)
接下来跟进分析`src/calibre/utils/formatter.py`文件：`formatter.safe\_format()`方法会将用户提供的模板字符串 template 作为输入，并进行格式化。用户提供的 template 参数没有经过严格的校验和过滤，直接传递给了 `formatter.safe\_format()` 方法，然后又调用 `evaluate` 方法进行实际的格式化操作。
![image-20251030104910726](https://oss-yg-cztt.yun.qianxin.com/butian-public/f4f3c002f7ff5f0fbdb558a78c8288c1e.png)
继续跟进代码：发现exaluate函数对于传入的参数没有做过滤，如果传入的参数以`python：`开头就会继续调用解析执行。
![image-20251030104921135](https://oss-yg-cztt.yun.qianxin.com/butian-public/fb5d9076170317063201862bd77ff6799.png)
综合分析以上代码可得出：在格式化的时候代码不会对用户输入内容进行过滤，没有过多地验证或清理。因此如果 template 模板参数中包含以`python:`开头的代码恶意代码，服务器就可执行任意python代码。
### 2.2漏洞复现：
根据漏洞分析构造请求体如下
POST <http://ip:8080/cdb/cmd/list> HTTP/1.1
Host:ip:8080
Content-Type: application/json
Content-Length: 303
​
\[
\["template"\],
"",
"",
"",
1,
"python:def evaluate(a, b):\\n import subprocess\\n try:\\n return subprocess.check\\_output(\['cmd.exe', '/c', 'whoami'\]).decode()\\n except Exception:\\n return subprocess.check\\_output(\['sh', '-c', 'whoami'\]).decode()"
\]
利用结果如下：
![image-20251030104940970](https://oss-yg-cztt.yun.qianxin.com/butian-public/f5325aeb12377352f25843b9e1d6e432f.png)
三、CVE-2024-7008（反射xss漏洞）
------------------------
### 3.1漏洞分析：
该漏洞定位于src/calibre/srv/legacy.py文件
![image-20251030105117497](https://oss-yg-cztt.yun.qianxin.com/butian-public/fb51acc814314961c9ab387e6fe6c51a1.png)
分析该代码块可得出，如果请求的路由是/browse/book/{%}的形式，服务器将直接把传入的`reset`参数内容插入变量redirect中，然后通过使用 lxml 的函数将此变量直接拼接到HTML和JavaScript代码中。JavaScript代码中提到`window.location.href = "..."`，用户可控的rest参数没有进行过滤，无清理和转义直接插入。如果参数包含双引号则会闭合字符串，后面的内容就会被当做代码执行，因此存在xss缺陷。
### 3.2漏洞复现：
根据代码逻辑构造如下payload：
\[[http://ip:8080/browse/book/TEST&amp;quot;;window.stop();alert(document.location);%2f%2f\](http://ip:8080/browse/book/TEST%22;window.stop();alert(document.location);%2f%2f](http://ip:8080/browse/book/TEST&quot;;window.stop();alert(document.location);%2F%2F%5D(http://ip:8080/browse/book/TEST%22;window.stop();alert(document.location);%2F%2F))
验证截图如下：

* 发表于 2025-11-07 10:06:46
* 阅读 ( 441 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)](https://forum.butian.net/people/77)

[中铁13层打工人](https://forum.butian.net/people/77)

83 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---