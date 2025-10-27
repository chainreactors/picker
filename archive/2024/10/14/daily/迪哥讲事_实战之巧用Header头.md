---
title: 实战之巧用Header头
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496107&idx=1&sn=153907948ada6dce89dfe8688d1dc423&chksm=e8a5fbc8dfd272de4366b9b4623c536b4debdc2b883e24f22039f52803063681438fe92c586f&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-14
fetch_date: 2025-10-06T18:47:54.202119
---

# 实战之巧用Header头

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj77N8Eodcm5QDD9duH8gDd1xicREB8UgZ5Njia82jo7YOJHHRDsrEZ2yYrdXUgRMY6bQKSp9YKqLAKg/0?wx_fmt=jpeg)

# 实战之巧用Header头

迪哥讲事

以下文章来源于goddemon的小屋
，作者goddemon

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5Vo5QO3Lf212OHF0qDvuSib45H89dA4fnEj6wC5xSgSMw/0)

**goddemon的小屋**
.

自信从容，虚心进步，慢慢成长

## 案例：

遇到过三次
一次是更改accept，获取到tomcat的绝对路径，结合其他漏洞获取到shell。

一次是更改accept，越权获取到管理员的MD5加密，最后接管超管权限。

一次是更改accept，结合参数获取到key。

这里以越权的案例介绍，其他的两个没保存图

原始请求包：![](https://mmbiz.qpic.cn/mmbiz_png/BYtyQicN4iaC6LrZxALoXic3ibBvYd1p9GaVGx1iaOxRaQSwyVlz2HSoq9icjVDiau1p32PPwyIbWKWVql1iakDoeMOndg/640?wx_fmt=png)将Accept改为
Accept: application/json, text/javascript, */*; q=0.01

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

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

##

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

##

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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