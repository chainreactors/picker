---
title: Java安全之Resin解析漏洞分析
url: https://buaq.net/go-148028.html
source: unSafe.sh - 不安全
date: 2023-02-06
fetch_date: 2025-10-04T05:47:09.475785
---

# Java安全之Resin解析漏洞分析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2e019e62e4c7eaf8a8b65762275964b2.jpg)

Java安全之Resin解析漏洞分析

前言挺久没有沉下心来好好的去研究分析一个自认为有意思的东西解析流程请求路径/webshell.jsp/123.txt调用栈buildInvocation
*2023-2-5 15:13:0
Author: [xz.aliyun.com(查看原文)](/jump-148028.htm)
阅读量:44
收藏*

---

## 前言

挺久没有沉下心来好好的去研究分析一个自认为有意思的东西

## 解析流程

请求路径

```
/webshell.jsp/123.txt
```

调用栈

```
buildInvocation:4175, WebApp (com.caucho.server.webapp)
buildInvocation:798, WebAppContainer (com.caucho.server.webapp)
buildInvocation:753, Host (com.caucho.server.host)
buildInvocation:319, HostContainer (com.caucho.server.host)
buildInvocation:1068, ServletService (com.caucho.server.cluster)
buildInvocation:250, InvocationServer (com.caucho.server.dispatch)
buildInvocation:223, InvocationServer (com.caucho.server.dispatch)
buildInvocation:1610, AbstractHttpRequest (com.caucho.server.http)
getInvocation:1583, AbstractHttpRequest (com.caucho.server.http)
handleRequest:825, HttpRequest (com.caucho.server.http)
dispatchRequest:1393, TcpSocketLink (com.caucho.network.listen)
handleRequest:1349, TcpSocketLink (com.caucho.network.listen)
handleRequestsImpl:1333, TcpSocketLink (com.caucho.network.listen)
handleRequests:1241, TcpSocketLink (com.caucho.network.listen)
```

调试解析流程来到

```
com.caucho.server.webapp.WebApp#buildInvocation(com.caucho.server.dispatch.Invocation, boolean)
```

```
//...

                    if (isCache) {
                        entry = (FilterChainEntry)this._filterChainCache.get(((Invocation)invocation).getContextURI());
                    }

                    FilterChain chain;
                    if (entry != null && !entry.isModified()) {
                       //...
                        }

                    } else {
                        chain = this._servletMapper.mapServlet((ServletInvocation)invocation);
                        this._filterMapper.buildDispatchChain((Invocation)invocation, chain);
                        chain = ((Invocation)invocation).getFilterChain();
                        chain = this.applyWelcomeFile(DispatcherType.REQUEST, (Invocation)invocation, chain);
                        if (this._requestRewriteDispatch != null) {
                            FilterChain newChain = this._requestRewriteDispatch.map(DispatcherType.REQUEST, ((Invocation)invocation).getContextURI(), ((Invocation)invocation).getQueryString(), chain);
                            chain = newChain;
                        }

                        entry = new FilterChainEntry(chain, (Invocation)invocation);
                        chain = entry.getFilterChain();
                        if (isCache) {
                            this._filterChainCache.put(((Invocation)invocation).getContextURI(), entry);
                        }
                    }

                    chain = this.buildSecurity(chain, (Invocation)invocation);
                    chain = this.createWebAppFilterChain(chain, (Invocation)invocation, isTop);
                    ((Invocation)invocation).setFilterChain(chain);
                    ((Invocation)invocation).setPathInfo(entry.getPathInfo());
                    ((Invocation)invocation).setServletPath(entry.getServletPath());
                    if (this._oldWebApp != null && CurrentTime.getCurrentTime() < this._oldWebAppExpireTime) {
                        Invocation oldInvocation = new Invocation();
                        oldInvocation.copyFrom((Invocation)invocation);
                        oldInvocation.setWebApp(this._oldWebApp);
                        this._oldWebApp.buildInvocation(oldInvocation);
                        invocation = new VersionInvocation((Invocation)invocation, this, oldInvocation, oldInvocation.getWebApp(), this._oldWebAppExpireTime);
                    }

                    var26 = invocation;
                    return (Invocation)var26;
                }
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150834-e7ab4830-a523-1.png)

从`_filterChainCache`通过请求路径获取缓存的`FilterChainEntry`实体类，缓存中获取不到的话会调用`this._servletMapper.mapServlet`来进行获取

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150842-ec309aea-a523-1.png)

`entry._regexp.matcher(uri);`通过URI去匹配规则，因为`^.*\.jsp(?=/)|^.*\.jsp\z`该正则的缘故，所以这里能将xxx.jsp/123.xxx给匹配为xxx.jsp

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150849-f0895a14-a523-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150900-f6d0ea72-a523-1.png)

请求走了`ServletMapping[url-pattern=*.jsp, name=resin-jsp]`的处理机制

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150907-fb75d7e0-a523-1.png)

`com.caucho.server.dispatch.ServletMapper#mapServlet`下面代码这里会创建chain

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150916-007d66e0-a524-1.png)

创建完成后，到`com.caucho.server.http.HttpRequest#handleRequest`调用`invocation.service`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150933-0a974ef2-a524-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150943-10b7d5a4-a524-1.png)

执行filterChain走到`com.caucho.server.dispatch.PageFilterChain#doFilter`进行jsp page的处理。

## 解析PHP

在`/conf/app-default.xml`文件中有这么一项，php后缀文件使用`com.caucho.quercus.servlet.QuercusServlet`来解析

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205150955-18126b5c-a524-1.png)

使用默认的resin配置是会将这条规则进行加载的

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205151007-1effde86-a524-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230205151018-2598e30a-a524-1.png)

`QuercusServlet`会调用`Quercus`来解析PHP

resin官方说明文档：<http://quercus.caucho.com/>

## 路径解析特性

### escape编码解析

调用栈

```
splitQueryAndUnescape:254, InvocationDecoder (com.caucho.server.dispatch)
buildInvocation:1594, AbstractHttpRequest (com.caucho.server.http)
getInvocation:1583, AbstractHttpRequest (com.caucho.server.http)
handleRequest:825, HttpRequest (com.caucho.server.http)
```

`com.caucho.server.dispatch.InvocationDecoder#splitQueryAndUnescape`调用`normalizeUriEscape`进行解码

`com.caucho.server.dispatch.InvocationDecoder#splitQueryAndUnescape`代码

```
public void splitQueryAndUnescape(Invocation invocation, byte[] rawURI, int uriLength) throws IOException {
        String decodedURI;
        for(int i = 0; i < uriLength; ++i) {
            if (rawURI[i] == 63) {
                ++i;
                decodedURI = this.byteToChar(rawURI, i, uriLength - i, "ISO-8859-1");
                invocation.setQueryString(decodedURI);
                uriLength = i - 1;
                break;
            }
        }

        String rawURIString = this.byteToChar(rawURI, 0, uriLength, "ISO-8859-1");
        invocation.setRawURI(rawURIString);
        decodedURI = normalizeUriEscape(rawURI, 0, uriLength, this._encoding);

//...
        String uri = this.normalizeUri(decodedURI);
        invocation.setURI(uri);
        invocation.setContextURI(uri);
```

`com.caucho.server.dispatch.InvocationDecoder#normalizeUriEscape`代码

```
private static String normalizeUriEscape(byte[] rawUri, int i, int len, String encoding) throws IOException {
       //...

        try {
            while(i < len) {
                int ch = rawUri[i++] & 255;
                if (ch == 37) {
                    i = scanUriEscape(converter, rawUri, i, len);
                } else {
                    converter.addByte(ch);
                }
            }

            String result = converter.getConvertedString();
            freeConverter(converter);
            return result;

    }
```

循环遍历路径每个字符匹配`%`字符，匹配到则调用`scanUriEscape`

```
private static int scanUriEscape(ByteToChar converter, byte[] rawUri, int i, int len) throws IOException {
        int ch1 = i < len ? rawUri[i++] & 25...