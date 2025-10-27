---
title: 零基础JS逆向和前端加密暴力破解 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18867823
source: 博客园 - 渗透测试中心
date: 2025-05-10
fetch_date: 2025-10-06T22:30:00.612270
---

# 零基础JS逆向和前端加密暴力破解 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [零基础JS逆向和前端加密暴力破解](https://www.cnblogs.com/backlion/p/18867823 "发布于 2025-05-09 11:06")

##

## 网站运行的时间轴

url-->加载html-->加载js-->运行js初始化-->用户触发某个事件--调用了某段js-->明文数据-->加密函数-->加密后的 数据-->send（给服务器发信息{XHR--SEND}） -->接收到服务器数据-->解密函数-->刷新函数-->刷新网页渲染

## 浏览器的调试功能

Chrome高阶调试指南:<https://zhuanlan.zhihu.com/p/62177097>

调试时使用最多的功能页面是：元素（ELements）、控制台（Console）、源代码（Sources）、网络（Network）

* 元素（Elements）：用于查看或修改HTML元素的属性、CSS属性、监听事件、断点（DOM断点：在JavaScript调试中，我们经常使用到断点调试，其实在DOM结构的调试中，我们也可以使用断点方法，这就是DOM Breakpoint（DOM 断点））
* 控制台（Console）：控制台一般用于执行一次性代码，查看JavaScript对象，查看调试日志信息或异常信息。
* 源代码（Sources）：该页面用于查看页面的HTML文件源代码、JavaScript源代码、CSS源代码，此外最重要的是可以调试JavaScript源代码，可以给JS代码添加断点等。
* 网络（Network）：网络页面主要用于查看header等与网络连接相关的信息。
* 资源（Resources）： 查看本地资源信息的（cookie,local storage,session storage等）

![image-20240417222019491](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110604156-1931502677.png)

定位到具体位置,可以右键进行编辑

![image-20240417222132801](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110605100-748478923.png)

**这个修改也仅对当前的页面渲染生效，不会修改服务器的源代码**

**右边的侧栏个功能的介绍**

![image-20240417222410939](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110606089-84457430.png)

## **控制台**

作用是

* 查看JS对象的及其属性
* 执行JS语句
* 查看控制台日志：当网页的JS代码中使用了console.log()函数时，该函数输出的日志信息会在控制台中显示。日志信息一般在开发调试时启用，而当正式上线后，一般会将该函数去掉。

![image-20240417223215480](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110606801-1569251412.png)

小知识(tab键补全这里也是支持的),**建议大家dom树学好**

![image-20240417224107063](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110607556-416757052.png)

![image-20240417224305485](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110608189-1452081217.png)

**调试快捷键**

* F10，跳过当前方法（如果执行到一个自定义方法，不进入方法内部）
* F11，进入当前方法（如果当前方法是一个自定义方法，进入方法内部）
* SHIFT+F11 跳出当前方法
* F8，跳到下一个断点

## **网络（Network）**

![image-20240417225158772](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110608824-1482545814.png)

* Header：面板列出资源的请求url、HTTP方法、响应状态码、请求头和响应头及它们各自的值、请求参数等等
* Preview：预览面板，用于资源的预览。
* Response：响应信息面板包含资源还未进行格式处理的内容
* Timing：资源请求的详细信息花费时间

查看Network基本信息,请求了哪些地址及每个URL的网络相关请求信息都可以看的到：URL，响应状态码，响应数据类型，响应数据大小，响应时间

![image-20240417225318626](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110609529-1872352188.png)

请求URL可进行筛选和分类：选择不同分类,查看请求URL,方便查找

![image-20240417225346461](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110610185-678373502.png)

也可以直接Filter搜索查询相关URL，可以输入关键字或者正则表达式进行查询

![image-20240417225505253](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110610849-985714381.png)

## 那么在js文件中我们如何快速定位到加密函数

* 搜索关键字：登陆时的uri、passwd、Encrypt、Decrypt、.....
* 使用一个神奇的脚本提高效率：<https://github.com/Cha111Ng1/Tampermonkey_cha11/blob/main/HookScript.js>

## 利用加解密函数

* 复原原加密逻辑
* 抠出原有js
* rpc主动调用

## 工具推荐

### phantomjs

<https://phantomjs.org/download.html>

PhantomJS是一个基于webkit的javaScript API。它使用QtWebKit作为它核心浏览器的功能，使用webkit来编译解释执行javaScript代码。任何你可以基于在webkit浏览器做的事情，它都能做到。它不仅是个隐性的浏览器，提供了诸如css选择器、支持wen标准、DOM操作、json、HTML5等，同时也提供了处理文件I/O的操作，从而使你可以向操作系统读写文件等。phantomJS的用处可谓非常广泛诸如网络监测、网页截屏、无需浏览器的wen测试、页面访问自动化等。

在前端渗透过程中，常会遇到需要进行爆破，但密码字段使用了自定义加密算法加密的情况。此时可以使用Burp配合jsEncrypter插件自定义加密算法进行爆破。流程图

![image-20240418103638129](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110611479-210648815.png)

项目地址：

<https://github.com/c0ny1/jsEncrypter>

这里面自带靶场,直接利用小p搭建就可以

![image-20240418105105118](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110612084-222131565.png)

选取rsa加密,进行

![image-20240418105144297](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110612738-2101035531.png)

找到公钥(ps:现在几乎没有公钥泄露了,几乎都被提交了)

![image-20240418105150843](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110613499-1735427197.png)

![image-20240418105209657](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110614228-2137719733.png)

加密js下载下来

![image-20240418105315771](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110614875-1106474963.png)

先将rsa.js文件保存到本地，重命名为rsa.js，然后修加密JSphantomjs\_server.js

开启端口

![image-20240418105323702](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110615570-1998794745.png)

![image-20240418105329707](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110616249-1806354735.png)

最后在Burp使用插件连接phantomjs\_server.js中开启的webserver

![image-20240418105341819](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110616846-2118720500.png)

然后用常用的字典爆破,

![image-20240418105349061](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110617567-1242042741.png)

成功

项目地址：<https://github.com/Cha111Ng1/Tampermonkey_cha11>

一个渗透测试油猴脚本库，整理常用脚本

### HookScript.js

一些用于hook的常用断点+禁用无限debug

// ==UserScript==
// @name 「Hook Script」fuck断点
// @namespace <http://tampermonkey.net/>
// @version 0.1
// @description 一些用于hook的常用断点，禁用无限debug
// @author Cha111Ng1
// @match http\*://\*/\*
// @icon data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAAAXNSR0IArs4c6QAAAKZlWElmTU0AKgAAAAgABgESAAMAAAABAAEAAAEaAAUAAAABAAAAVgEbAAUAAAABAAAAXgEoAAMAAAABAAIAAAExAAIAAAAVAAAAZodpAAQAAAABAAAAfAAAAAAAAABIAAAAAQAAAEgAAAABUGl4ZWxtYXRvciBQcm8gMy4zLjQAAAADoAEAAwAAAAEAAQAAoAIABAAAAAEAAABaoAMABAAAAAEAAABaAAAAAF5d/ccAAAAJcEhZcwAACxMAAAsTAQCanBgAAAOaaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjkwPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjkwPC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6Q29sb3JTcGFjZT4xPC9leGlmOkNvbG9yU3BhY2U+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6UmVzb2x1dGlvblVuaXQ+MjwvdGlmZjpSZ...