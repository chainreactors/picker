---
title: SaaS-API越权漏洞检测系统 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17084609.html
source: 博客园 - 渗透测试中心
date: 2023-02-02
fetch_date: 2025-10-04T05:29:18.460707
---

# SaaS-API越权漏洞检测系统 - 渗透测试中心

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

# [SaaS-API越权漏洞检测系统](https://www.cnblogs.com/backlion/p/17084609.html "发布于 2023-02-02 00:53")

## 概述

通过替换认证信息后重放请求，并对比数据包结果，判断接口是否存在越权漏洞

## 特点

1. 支持HTTPS
2. 自动过滤图片/js/css/html页面等静态内容
3. 多线程检测，避免阻塞
4. 支持输出报表与完整的URL、请求、响应

## 安装和使用

### 安装依赖

git clone  https://github.com/y1nglamore/IDOR\_detect\_tool.git

```
python3 -m pip install -r requirements.txt
```

### 启动

```
python3 start.py
```

即可监听socks5://127.0.0.1:8889。

### 安装证书

使用SwitchOmega等插件连接该代理，并访问[mitm.it](http://mitm.it/)即可进入证书安装页面，根据操作系统进行证书安装。

以MacOS为例：

[![175143_y7wfgR](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202005252198-128429728.png)](https://camo.githubusercontent.com/407c65ced03efb3965d1259b90eaf2895afc5ad845241d34e3ea9f498b29b40d/687474703a2f2f63646e322e7069632e79316e672e7669702f755069632f323032332f30312f32352f3137353134335f7937776667522e706e67)

下载安装后，打开钥匙串访问，找到mitmproxy证书，修改为alwaystrust

[![175302_B8WD5s](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202005253032-915025785.png)](https://camo.githubusercontent.com/99e6ce332df13ddd899a9727ddb84842539d2e292cf4f751d37f46664d615431/687474703a2f2f63646e322e7069632e79316e672e7669702f755069632f323032332f30312f32352f3137353330325f4238574435732e706e67)

### 检测漏洞

首先准备好目标系统的A、B两账号，根据系统的鉴权逻辑（Cookie、header、参数等）将A账号信息配置config/config.yml，之后登录B账号

[![175522_XdPt84](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202005253841-1050639239.png)](https://camo.githubusercontent.com/28ebe676735ae2b8cfaef4176704b5b425d694d3085bd30750845b55b89e91d4/687474703a2f2f63646e322e7069632e79316e672e7669702f755069632f323032332f30312f32352f3137353532325f5864507438342e706e67)

使用B账号访问，脚本会自动替换鉴权信息并重放，根据响应结果判断是否存在越权漏洞

[![175435_PFm3WY](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202005254594-758946979.png)](https://camo.githubusercontent.com/c45dcb6ff2a45f6601dae441f449d9435646c59d0626133a6ab6cff4024c6982/687474703a2f2f63646e322e7069632e79316e672e7669702f755069632f323032332f30312f32352f3137353433355f50466d3357592e706e67)

生成报表

每次有新漏洞都会自动添加到report/result.html中，通过浏览器打开：

[![181645_PaztjA](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202005255350-1160825839.png)](https://camo.githubusercontent.com/d1aca41a623236013ebf287efd7a4097bc3abf0e6d2f14f0e4e7664c50a7574e/687474703a2f2f63646e322e7069632e79316e672e7669702f755069632f323032332f30312f32352f3138313634355f50617a746a412e706e67)

点击具体条目可以展开/折叠对应的请求和响应：

[![181811_HJMDoo](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202005256093-1501670836.png)](https://camo.githubusercontent.com/0196d75f63c508b464d7529d94ad32ae60c8e300932e60856bcabd34666752e1/687474703a2f2f63646e322e7069632e79316e672e7669702f755069632f323032332f30312f32352f3138313831315f484a4d446f6f2e706e67)

检测逻辑

[![230504_ECb2mP](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230202005256869-909260404.png)](https://camo.githubusercontent.com/4eca57affb695383ec88008c3b47f6eebd86ce9357889c294cc3e0adc47ac6d1/687474703a2f2f63646e322e7069632e79316e672e7669702f755069632f323032332f30312f32362f3233303530345f454362326d502e6a7067)

原文连接：https://github.com/y1nglamore/IDOR\_detect\_tool

posted @
2023-02-02 00:53
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(362)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025