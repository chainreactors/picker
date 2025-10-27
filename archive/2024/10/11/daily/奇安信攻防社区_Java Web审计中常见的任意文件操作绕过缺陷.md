---
title: Java Web审计中常见的任意文件操作绕过缺陷
url: https://forum.butian.net/share/3797
source: 奇安信攻防社区
date: 2024-10-11
fetch_date: 2025-10-06T18:45:31.184904
---

# Java Web审计中常见的任意文件操作绕过缺陷

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

### Java Web审计中常见的任意文件操作绕过缺陷

* [漏洞分析](https://forum.butian.net/topic/48)

随着研发安全开发意识的不断提高，很多情况下相关风险都有一定的止血措施。，任意文件操作是一个很常见的安全漏洞浅析代码审计中常见的一些绕过案例。

0x00 前言
=======
在 Java Web 应用程序中，任意文件操作是一个很常见的安全漏洞，它允许攻击者通过操纵应用程序来访问服务器上的文件。这种漏洞通常是由于应用程序对用户输入的文件路径参数处理不当导致的。
一般情况下，可以关注相关的文件操作类，来辅助审计。
- InputStream
- File
- OutputStreaam
- BufferedInputStream
- FileInputStream
- ......
根据参数位置，可以分为request请求参数以及请求路径path两种。
request请求参数中的任意文件操作风险比较常见：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6d2c364c2c607de39a745ba48896022f5c431c06.png)
而请求路径Path的则比较复杂，根据实现方式可以粗略分为自定义Servlet以及类似 @PathVariable 注解框架自带的特性两种。实际利用时可能会存在一些限制，具体的分析可见https://forum.butian.net/share/2265。
本质上还是因为没有对用户可控的内容进行安全检查，导致了相关的风险。
0x01 常见绕过缺陷
===========
一般情况下，针对任意文件操作风险，一般会采用\*\*白名单\*\*或者\*\*输入验证\*\*的方式进行防护\*\*：\*\*
- 对所有用户可控的文件名与路径进行安全检查进行严格的验证，确保它们不包含路径遍历序列或非法字符。例如配置了全局过滤器或者额外进行了路径处理（例如过滤“../”）
- 对用户输入的内容转换成相关的资源目录文件，对此进行限制，用户只能访问特定的文件或目录。
但是在实际应用系统中，由于涉及到的功能比较复杂，结合框架自身特点等种种特殊条件下，相关的安全措施可能会有绕过的缺陷。下面结合实际审计案例进行梳理，分享一些实际的案例。
1.1 过滤内容不严谨
-----------
首先是输入验证，一般情况下主要会对类似`../`的输入进行安全检查。但是在特定场景下这类的措施是不足以抵御相关漏洞的。下面是实际审计中遇到的一些案例。
### 1.1.1 windows目录穿越符
对于任意文件操作的风险常常会通过过滤类似../进行防护，例如下面的例子：
```Java
public static boolean check(String filePath) {
if (StringUtil.isBlank(filePath)) {
return true;
}
return StringUtil.contains(filePath, "../");
}
```
最简单的攻击者可能尝试使用 Windows 特有的目录穿越符（如 `..\` 或 `%5C` 表示反斜杠）来访问上级目录。从而绕过相应的安全措施。
### 1.1.2 java.net.URL处理特性
在Java中，可以通过使用URL类来实现获取共享文件夹文件的file协议。例如下面的例子：
```Java
URL url = new URL("FilePath");
InputStream inputStream = url.openStream();
// 使用 InputStreamReader 和 BufferedReader 包装 InputStream
BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
// 逐行读取文件内容
String line;
while ((line = reader.readLine()) != null) {
System.out.println(line);
}
// 关闭 BufferedReader 和 InputStream
reader.close();
inputStream.close();
```
某些应用程序可能只检查文件后缀。限制只能访问类似png、jpg等图片资源，在一定程度上收敛了风险。实际上可以通过#的方式绕过，URL在解析时会忽略相应的内容：
```Java
URL url = new URL("file:/var/log/../../../../etc/passwd#.png");
System.out.println(url.getPath());
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-bfe5e104709b13d8f7dccc1b55dddcf49c13dd9e.png)
对于过滤了`../`的情况，实际上也很好解决，查看java.net的源码，可以看到在解析时做了一层URL解码。结合Spring Controller在解析时自解码一层的特点，可以通过双重URL编码的方式，绕过对应的`../`检查：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-fbe7080183b11789c362c485896ef9ca38636907.png)
### 1.1.3 与其他安全措施冲突
由于业务系统的复杂性，除了任意文件下载的防护，类似xss、sql注入的防护可能都会通过相关的filter进行处理。也方便管理。在某些情况下可以存在冲突，导致了防护的绕过。下面是一个实际的例子：
在filter中对获取参数内容的方法进行了重写，首先调用cleanAnyFileRead方法将类似`../`输入替换成null，最后使用Jsoup组件进行xss处理，将相关xss内容替换成null：
```Java
@Override
public String getParameter(String parameter) {
String value = super.getParameter(parameter);
if (value == null) {
return null;
}
return JsoupUtil.clean(cleanAnyFileRead((String) value));
}
private static String cleanAnyFileRead(String value) {
value = value.replaceAll("\\.+/", "");
return value;
}
```
因为存在先后顺序，这里存在冲突。可以利用最后xss内容替换，在`../`中植入xss poc，来绕过对`../`的检查：
```php
..<script>/..<script>/..<script>/etc/passwd
```
1.2 获取实际访问文件资源方法不当
------------------
除了对文件名与路径进行安全检查以外，一般情况下还会获取用户实际访问的文件资源路径并进行限制，禁止尝试访问非白名单目录以外的内容。
在获取用户实际访问的文件资源路径时，一般会结合一些现有的工具类进行处理。例如在网上现搜的安全措施：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-4eeda15585b2df42c20848075a95df807648dccc.png)
查看`StringUtils.cleanPath`具体的方法实现，如果路径长度不为0，会对路径进行规范化处理，将`\\`替换成`/`,如果规范化后的路径不包含`.`,直接返回对应的内容:
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-4e0fd49ce057636881a7df2cfcdba3e0d8c867a5.png)
检查路径中是否有冒号（:），这通常用于区分协议和路径。如果有冒号，那么提取协议部分 prefix。这里主要是对类似file协议进行处理：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a78b27393aacde2a84058e50f5b4add17e539742.png)
然后将 pathToUse 按照`/`拆分成多个元素，存储在数组 pathArray 中：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-dd51a4fe510a467c11cf3a527b2ca221a1386007.png)
使用一个双端队列 pathElements 来构建一个清理后的路径。遍历 pathArray，对于每个元素按照如下策略进行处理：
- 如果元素是 .，则忽略它，因为它表示当前目录
- 如果元素是 ..，则表示需要回退到上一级目录，因此增加 tops 计数
- 如果 tops 大于 0，则从 pathElements 中移除最后一个元素（回退操作）
- 如果既不是 . 也不是 ..，则将元素添加到 pathElements 的前面（实际路径内容）
如果 pathArray 的长度与 pathElements 的大小相同，说明没有相对路径引用，返回原始的 normalizedPath，否则将 tops 中的每个`..`添加到 pathElements 的前面，将 pathElements 中的元素使用 / 连接起来，形成清理后的路径：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-0ed7ee78aa23395da3670e6df4c74d80b6576938.png)
可以看到，实际上cleanPath方法对类似`../`的清理是不彻底的。以实际例子说明，例如用户可用传入fileName，读取/var/log/下的日志文件，若fileName没有经过安全检查的话，这里明显会存在任意文件读取的风险：
```Java
public static String readLogFile(String fileName) {
// 构建完整的文件路径
String fullPath = "/var/log/" + fileName;
StringBuilder contentBuilder = new StringBuilder();
try (BufferedReader br = new BufferedReader(new FileReader(fullPath))) {
String line;
while ((line = br.readLine()) != null) {
// 将读取的每一行添加到 StringBuilder 中
contentBuilder.append(line).append(System.lineSeparator());
}
} catch (IOException e) {
return null; // 返回 null 表示读取过程中出现错误
}
......
// 返回整个文件的内容
return contentBuilder.toString();
}
```
可以通过获取用户实际访问文件资源，然后判断是否在/var/log目录下进行防御，这里可以对fileName和fullPath两个参数调用cleanPath进行处理。下面分别讨论：
- \*\*fileName\*\*
假设用户的输入是`/../../../../etc/passwd`:
```Java
StringUtils.cleanPath("/../../../../etc/passwd")
```
因为pathArray 的长度与 pathElements 的大小在处理后并不相同，所以`..`会原封不到的添加到 pathElements 的前面，也就是处理后的内容会原样输出，拼接`/var/log/`后依旧存在任意文件读取风险：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-1587360b40a7c80ccc32b1240131b45d24b474b8.png)
- \*\*fullPath\*\*
假设用户的输入是`/../../etc/passwd`，在跟`/var/log/`拼接后组成fullPath再调用cleanPath处理:
```Java
StringUtils.cleanPath("/var/log/../../etc/passwd")
```
此时两个`../`刚好与前面目录抵消，返回`/etc/passwd`，确实是用户最终实际访问到的文件资源。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-8daeec52c1990185a023e53e98bcc5a422a24bd7.png)
但是只需要`../`足够多，同样的会因为pathArray 的长度与 pathElements 的大小在处理后并不相同，引入额外的`../`:
```Java
StringUtils.cleanPath("/var/log/../../../../etc/passwd")
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-5cdc3278c5aacc683ce3f492706a4916805325a0.png)
这里如果是通过判断cleanPath处理后的fullPath是否在`/var/log`范围内的话，从结果上看在一定程度上是可以抵御任意文件读取访问的。
但是只需要修改相关poc，此时处理后的路径就是在`/var/log`范围了，若仍继续访问原来的fullPath的话，同样的会存在安全风险：
```Java
StringUtils.cleanPath("/var/log//..//..//..//..//../etc/passwd")
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b098f8db963c02a52c384831f48aaae4e4db45bb.png)
这里主要是pathArray 的处理策略问题，可以看到对于多个`/`的情况，影响了pathArray的组成，认为存在“空”目录：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ab2dee0ed770ddd3827c033a265164afbfaf430c.png)
综上，单一的cleanPath方法并不能很好的解决任意文件读取风险。除此以外，还有很多其他的工具类，在实际使用时，需要关注具体的实现，避免使用不当导致的绕过问题。
0x03 其他
=======
除了上述案例以外，例如Web框架的解析特性，也可是考虑的方向。尤其是对于请求Path的文件读取场景，在获取path时可能会存在差异，也可能导致安全措施的绕过。在实际审计过程中可以额外关注。
在实际漏洞修复时，也可以参考下一些主流框架的修复措施，例如CVE-2023-34062。通过Path对象调用`normalize()`方法将路径标准化，即解析任何`.`（当前目录）和`..`（上一级目录）的引用，如果规范化后的请求资源路径不是以设置的静态资源目录开头的话，返回resp.sendNotFound，表示内容不存在。通过对请求内容的规范化处理避免了目录遍历的风险：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-cdbd41307ec87ea1f22258ea9ad30136fd44ed59.png)

* 发表于 2024-10-10 09:00:02
* 阅读 ( 6146 )
* 分类：[代码审计](https://forum.butian.net/community/code%20audit)

3 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[...