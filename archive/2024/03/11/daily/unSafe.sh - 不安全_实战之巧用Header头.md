---
title: 实战之巧用Header头
url: https://buaq.net/go-227204.html
source: unSafe.sh - 不安全
date: 2024-03-11
fetch_date: 2025-10-04T12:08:11.837483
---

# 实战之巧用Header头

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

![](https://8aqnet.cdn.bcebos.com/d36641f52effd131a6cc5e634502a145.jpg)

实战之巧用Header头

案例：遇到过三次一次是更改accept，获取到tomcat的绝对路径，结合其他漏洞获取到shell。 一次是更改accept，越权获取到管理员的MD5加密，最后接管超管权限。一次是更改accept，
*2024-3-10 23:29:51
Author: [mp.weixin.qq.com(查看原文)](/jump-227204.htm)
阅读量:67
收藏*

---

## 案例：

遇到过三次
一次是更改accept，获取到tomcat的绝对路径，结合其他漏洞获取到shell。

一次是更改accept，越权获取到管理员的MD5加密，最后接管超管权限。

一次是更改accept，结合参数获取到key。

这里以越权的案例介绍，其他的两个没保存图

原始请求包：![](https://mmbiz.qpic.cn/mmbiz_png/BYtyQicN4iaC6LrZxALoXic3ibBvYd1p9GaVGx1iaOxRaQSwyVlz2HSoq9icjVDiau1p32PPwyIbWKWVql1iakDoeMOndg/640?wx_fmt=png)

成功获取到当前用户的password以及sql接口

![](https://mmbiz.qpic.cn/mmbiz_png/BYtyQicN4iaC6LrZxALoXic3ibBvYd1p9GaVZ03hBqnqqOelyLW2Fz6R0uxTOnL5jt44GCnYAA6O1A95cXib4xwg2gg/640?wx_fmt=png)

构造参数id=1后成功获取到管理员权限以及管理员md5密码，md5解密后成功接管管理员权限

![](https://mmbiz.qpic.cn/mmbiz_png/BYtyQicN4iaC6LrZxALoXic3ibBvYd1p9GaVGaQ2NImSLzibFg9eSnG0CRDbk5Fsa0ibpp0a90KwRUDCcQmXSmQ6lN1A/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/BYtyQicN4iaC6LrZxALoXic3ibBvYd1p9GaViav6v50ppp1ECklAlTddP3D4Rh89IDs2DLZGmQO7eRiazib20BOxEFAJw/640?wx_fmt=png)

## 漏洞分析：

核心还是根据Accept进行不同响应导致的

### 第一种代码：

RESTful API情况下，直接写在controller中
后端请求根据请求头中Accept 字段判断进行生成不同格式的响应数据。

```
@RestController
public class MyController {

@GetMapping(value = "/data", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<MyData> getJsonData() {
        // 生成 JSON 格式的响应数据
        MyData data = new MyData();
        // 设置数据...
        return ResponseEntity.ok(data);
    }

@GetMapping(value = "/data", produces = MediaType.TEXT_HTML_VALUE)
    public ResponseEntity<String> getHtmlData() {
        // 生成 HTML 格式的响应数据
        String html = "<h1>Hello, World!</h1>";
        return ResponseEntity.ok(html);
    }
}
```

### 第二种代码：

filter进行设置编码

```
public class MyFilter implements Filter {

@Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest httpRequest = (HttpServletRequest) request;
        HttpServletResponse httpResponse = (HttpServletResponse) response;

        String acceptHeader = httpRequest.getHeader("Accept");
        if (acceptHeader != null && acceptHeader.contains("text/html")) {
            httpResponse.setHeader("Accept", "text/plain");
        }

        chain.doFilter(request, response);
    }
}
```

controller进行判断情况

```
@Controller
public class MyController {

@GetMapping(value = "/data")
    public String getData(HttpServletRequest request) {
        String acceptHeader = request.getHeader("Accept");
        if (acceptHeader != null && acceptHeader.contains("application/json")) {
            // 返回 JSON 格式的视图
            return "jsonView";
        } else {
            // 返回 HTML 格式的视图
            return "htmlView";
        }
    }
}
```

## 漏洞可能出现业务：

### 从开发角度探讨出现这种业务的原因：

1. 响应内容的格式要根据客户端的需求而动态变化：如果你的业务需要根据客户端的需求动态地生成不同格式的响应数据，例如根据客户端要求返回 JSON 或者 HTML 格式的数据。这通常用于构建 RESTful API 或者多渠道支持的应用程序。
2. 客户端与后端交互方式多样化：如果你的应用程序被多个不同的客户端（如浏览器、移动设备、API 调用等）访问，并且每个客户端对响应数据的需求不同，例如某些客户端需要 JSON 格式，而其他客户端需要 HTML 格式。此时，根据客户端请求头中的 Accept 字段来返回适当格式的数据是很常见的需求。
3. 处理特定类型的请求：有些业务场景可能需要处理特定类型的请求，例如文件上传、XML 数据解析等。这些请求可能需要特殊的处理逻辑，并返回与请求内容相关联的响应数据。

### 具体业务：

1. 多客户端应用程序时：多客户应用程序需要处理多种类型的客户端请求，如一个web如果同时具有apk，小程序，ios等时可以考虑测试这个。
2. 多组件存在时：多组件程序时需要处理多种不同类型请求的请求包。（上面的案例就是这种情况，因为该系统有多个组件，所以我当时才进行测试该漏洞。）

## 拓展以及思考：

除了accept以外是否还有其他的header头也会导致不一样呢，比如cdn模式下的Accept-Language会不会也有产生不一样的效果呢？

绕waf时的Accept-Encoding会不会也产生奇效呢？

User-Agent遇到403时，会不会也碰撞出不一样的火花。

这些就留给大家自己去探究了

## 最后：

基于开发的角度去探究漏洞，或许思路会更巧更妙

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzIzMTIzNTM0MA==&mid=2247493816&idx=1&sn=cff760a54a5316fe89481113987b74fe&chksm=e8a5e2dbdfd26bcd8ef827cf590d558dc1fd5167427d0587ad9d989675c0d32694011ba590ba&scene=58&subscene=0#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)