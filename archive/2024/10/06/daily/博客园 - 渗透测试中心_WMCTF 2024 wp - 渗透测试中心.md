---
title: WMCTF 2024 wp - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18447748
source: 博客园 - 渗透测试中心
date: 2024-10-06
fetch_date: 2025-10-06T18:49:45.752130
---

# WMCTF 2024 wp - 渗透测试中心

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

# [WMCTF 2024 wp](https://www.cnblogs.com/backlion/p/18447748 "发布于 2024-10-05 12:13")

## WEB

### PasswdStealer

#### 前言

本来题目叫PasswdStealer的：）

考点就是CVE-2024-21733在SpringBoot场景下的利用。

漏洞基本原理参考 <https://mp.weixin.qq.com/s?__biz=Mzg2MDY2ODc5MA==&mid=2247484002&idx=1&sn=7936818b93f2d9a656d8ed48843272c0>
不再赘述。

#### SpringBoot场景下的利用

前文的分析得知，该漏洞在tomcat环境下的利用需要一定的条件

1. 触发一个超时错误，让reset()无法正常调用
2. 触发server()中循环处理的逻辑，让tomcat一次处理多个请求内容
3. 回显获取泄露的敏感数据

下面在裸SpringBoot场景下寻找利用方法。

测试环境：SpringBoot v2.6.13 ，tomcat替换为漏洞版本 9.0.43 ，不添加任何路由控制器。

##### step1 触发超时

目的是让read() 抛出 IOException
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121243973-526414845.png)
跳过reset()，造成limit错位。

使用上文分析时的Poc，CL大于实际值的POST包
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121244702-831722680.png)

秒返回，并没有跑出异常，这是因为aaa路由不存在，POST data并没有被tomcat处理。

这里需要寻找一个让 可以处理POST data的请求。

这里使用 multipart/form-data 上传数据。

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121245324-1035761238.png)
成功触发了timeout超时

##### step2 进入循环

接下来尝试满足条件2，让请求在超时后仍然进入 Http11Processor.java#service()中的循环，debug跟进后发现这样已经不满足条件了
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121245931-1257910665.png)

keepAlive变成了false，向上回溯调用栈，寻找原因，

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121246508-1578043658.png)
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121247096-1519601617.png)
若果statusCode在StatusDropsConnection里面，则会将keepAlive置为false

继续回溯，寻找将statusCode设置为500的地方 ，

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121247750-1017064878.png)

跟上去，发现是 ServletException 触发了它
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121248379-931847642.png)

继续跟上去，最终发现是我们触发的IOException被包成了FileUploadException
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121249040-1288111808.png)

而这里的IOException其实是discardBodyData的时候跑出的，由于没有被catch，所以直接抛到了上层。
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121249734-229497334.png)

至此我们先搞清楚了产生500的原因，**下面寻找如何让请求不产生500**，也就是在让discardBodyData()不抛出IOException, 但仍然能造成超时的方法。

首先使用一个正常的multipart包测试，

> 这里补充一下boundary的标准
> 假设 Content-Type中设置boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW，
> 那么------WebKitFormBoundary7MA4YWxkTrZu0gW 代表一个部分的开头（前面加两个--）
> ------WebKitFormBoundary7MA4YWxkTrZu0gW-- 代表表单结束 （前面后面都加两个--）

这里构造一个有头有尾的multipart上传包
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121250306-1260156243.png)

我们发现他可以走到readBoundDary()中

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121250927-422416278.png)

继续跟进readBoundDary()，根据上面讲的boundary的标准可以看出来，`marker[0] = readByte();`是在读最后两位--或者CLRF，也就是boundary的结束符号。
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121251581-1485479073.png)

但是如果我们设置为请求包为这样，也就是没有boundary结束标志的话会怎么？
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121252105-1542817419.png)
发包继续跟下去，发现如果`readByte()`读不到数据的话（因为我们没发），最终还是会调用到fill()中，在fill中造成 IOException（step1 的位置）。

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121252788-1565132135.png)

这时 `readByte()`会抛出 IOException，但是在`readBoundary`中被catch住，包成`MalformedStreamException`。

这时候再回到 `skipPreamble`函数中，发现`MalformedStreamException`会被catch住，成功避免了它继续向上抛出IOException造成500。

```
} catch (final MalformedStreamException e) {
    return false;
```

至此我们成功构建出一个超时但是返回404的请求包，而404不在`StatusDropsConnection`中，所以可以进入while循环。
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121253506-2088433277.png)

##### step3 泄露回显

这步直接使用Trace请求即可，Trace请求

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121254301-464493260.png)

#### 最终利用

这里我们设定目标为泄露正常用户的headers中flag。

首先发送一个请求（假设这个请求时受害者发送的），里面携带敏感信息，此时的`inputBuffer`长这样。
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121254921-31099119.png)

攻击者发送一个请求，正常返回
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121255536-859929041.png)

此时`inputBuffer`内的情况已经变成了这样。
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121256177-834680255.png)

最后一步，也是最重要的一步，攻击者发送一个静心构造的multipart包
![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121256841-800502458.png)

此时multipart包超时后仍然会进入while循环，继续发包，所以在`nextRequest`后 `inputBuffer`变成一个完整的Trace请求，并且通过覆盖原有buffer让flag变成了Trace请求的header

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121257496-1716033866.png)

最终通过Trace的回显获取到flag。

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005121258102-106626974.png)

这里获取的是headers信息，其实body也可以获取，稍微麻烦一些。只需要在受害者包前面发一个全是CLRF的包，提前将buffer填满CLRF，同时将body覆盖为TRACE请求的headers即可。

### EzQl

```
package org.example;

import com.ql.util.express.DefaultContext;
import com.ql.util.express.ExpressRunner;
import com.ql.util.express.config.QLExpressRunStrategy;
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import sun.misc.BASE64Decoder;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws IOException {
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8000"));
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);

        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange req) throws IOException {
                int code = 200;
                String response;
                String path = req.getRequestURI().getPath();
                if ("/ql".equals(path)) {
                    try {
                        String express = getRequestBody(req);
                        express = new String(Base64.getDecoder().decode(express));
                        ExpressRunner runner = new ExpressRunner();
                        QLExpressRunStrategy.setF...