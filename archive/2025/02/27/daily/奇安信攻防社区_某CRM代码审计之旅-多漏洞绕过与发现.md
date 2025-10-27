---
title: 某CRM代码审计之旅-多漏洞绕过与发现
url: https://forum.butian.net/share/4131
source: 奇安信攻防社区
date: 2025-02-27
fetch_date: 2025-10-06T20:33:19.787290
---

# 某CRM代码审计之旅-多漏洞绕过与发现

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

### 某CRM代码审计之旅-多漏洞绕过与发现

* [漏洞分析](https://forum.butian.net/topic/48)

某CRM的代码审计之旅

某CRM的代码审计之旅
===========
0x01 权限绕过
---------
该项目使用了shiro进行权限验证
![image-20241031181522968](https://oss-yg-cztt.yun.qianxin.com/butian-public/f5fbe1c1ba2ad6f57b59878efc185802b.png)
查看依赖版本，发现该版本配合spring存在认证绕过漏洞
shiro通过org.apache.shiro.web.filter.mgt.PathMatchingFilterChainResolver#getChain来匹配路由和过滤器
```java
public FilterChain getChain(ServletRequest request, ServletResponse response, FilterChain originalChain) {
FilterChainManager filterChainManager = this.getFilterChainManager();
if (!filterChainManager.hasChains()) {
return null;
} else {
String requestURI = this.getPathWithinApplication(request);
if (requestURI != null && !"/".equals(requestURI) && requestURI.endsWith("/")) {
requestURI = requestURI.substring(0, requestURI.length() - 1);
}
Iterator var6 = filterChainManager.getChainNames().iterator();
String pathPattern;
do {
if (!var6.hasNext()) {
return null;
}
pathPattern = (String)var6.next();
if (pathPattern != null && !"/".equals(pathPattern) && pathPattern.endsWith("/")) {
pathPattern = pathPattern.substring(0, pathPattern.length() - 1);
}
} while(!this.pathMatches(pathPattern, requestURI));
return filterChainManager.proxy(originalChain, pathPattern);
}
}
```
http请求的路由通过`getPathWithinApplication`方法获取，最终调用`org.apache.shiro.web.util.WebUtils#getRequestUri`方法
```java
public static String getRequestUri(HttpServletRequest request) {
String uri = (String)request.getAttribute("javax.servlet.include.request\_uri");
if (uri == null) {
uri = request.getRequestURI();
}
return normalize(decodeAndCleanUriString(request, uri));
}
```
该方法核心是`decodeAndCleanUriString`和`normalize`两个方法来处理请求url
- `decodeAndCleanUriString`: 主要是讲`;`之前的路径保留而舍弃之后的部分，即`/aa/..;/bbb`被处理为`/aa/..`
- `normalize`
- 替换反斜线
- 替换 `//` 为 `/`
- 替换 `/./` 为 `/`
- 替换 `/../` 为 `/`
单看好像都没问题但是组合起来就丸辣。比如我们配置shiro的拦截配置
```java
map.put("/home/\*\*","anon"); //anon 表示未授权访问
map.put("/admin/\*","authc"); //authc 表示需要权限认证
shiroFilterFactoryBean.setFilterChainDefinitionMap(map);
```
要是我们构造`/home/..;/admin/xxx` ，shiro通过上述操作获取到的URI为`/home/..`，会命中`"/home/\*\*","anon"`从而不进行认证。
当shiro放行请求后会交给spring处理，而在spring中对于请求路径又有自己的处理逻辑
其在`org.springframework.web.util.UrlPathHelper`中存在spring实现的`getRequestUri`方法
```java
public String getRequestUri(HttpServletRequest request) {
String uri = (String)request.getAttribute("javax.servlet.include.request\_uri");
if (uri == null) {
uri = request.getRequestURI();
}
return this.decodeAndCleanUriString(request, uri);
}
```
然后通过`decodeAndCleanUriString`来处理请求url
```java
private String decodeAndCleanUriString(HttpServletRequest request, String uri) {
uri = this.removeSemicolonContent(uri);
uri = this.decodeRequestString(request, uri);
uri = this.getSanitizedPath(uri);
return uri;
}
```
其中的三个方法主要是过滤`;`、urldecode和过滤`//`，最终的`/home/..;/admin`变成`/home/../admin`定位到admin的路由。
整体的流程就是
1. 客户端请求URL: `/home/..;/admin/index`
2. shrio 内部处理得到校验URL为 `/home/..,`校验通过
3. spring 处理 `/home/..;/admin/index` , 请求 `/admin/index`, 成功访问鉴权接口
0x02 任意文件读取
-----------
我们找一个漏洞来测试一下鉴权绕过，有关文件加载操作的类和方法主要有
```java
File
FileInputStream
BufferedInputStream
InputStream
getName
read
write
getFile
getWriter
download (危险的路由名)
...
```
根据上述思路，我们找的在`xxxLogController`，找的了`download`方法
```java
public void download(String path, HttpServletRequest request, HttpServletResponse response) {
try {
File file = new File(path);
String filename = file.getName();
InputStream fis = new BufferedInputStream(new FileInputStream(path));
byte[] buffer = new byte[fis.available()];
fis.read(buffer);
fis.close();
response.reset();
response.addHeader("Content-Disposition", "attachment;filename=" + new String(filename.replaceAll(" ", "").getBytes("utf-8"), "iso8859-1"));
response.addHeader("Content-Length", "" + file.length());
OutputStream os = new BufferedOutputStream(response.getOutputStream());
response.setContentType("application/octet-stream");
os.write(buffer);
os.flush();
os.close();
} catch (Exception var9) {
this.logger.error("下载文件失败", var9);
}
}
```
其根据传入`fileName`直接获取文件内容返回给response。
### 复现
直接访问会跳转登录页
![image-20241101114437342](https://oss-yg-cztt.yun.qianxin.com/butian-public/fd2bddff3ed504516097d8479cde53951.png)
利用`/..;/`进行绕过
![image-20241101114536839](https://oss-yg-cztt.yun.qianxin.com/butian-public/f43148c1562883b48d73d1dde92bb54e1.png)
成功读取到目标文件，证明鉴权绕过可行。
0x03 命令执行
---------
既然看到读取如此简单，那我们再扩大危害看看有没有可以RCE点。
查找`Runtime.getRuntime`方法的调用，找的了`exeCommand`方法实现
```java
private void exeCommand(String command) throws IOException {
logger.info("MySQL数据库正执行命令：" + command);
Runtime runtime = Runtime.getRuntime();
Process exec = runtime.exec(command);
try {
exec.waitFor();
} catch (InterruptedException var5) {
logger.error("MySQL数据库执行命令出错：" + var5.getMessage(), var5);
}
}
```
因为是私有方法，直接同类中向上找的了调用方法
```java
public void doRestore(String fileName) {
String sqlFile = fileName;
...
if (osName.toLowerCase().startsWith("windows")) {
mysqldump = "cmd /c \"" + this.mysqlPath + "mysql\"";
} else {
mysqldump = this.mysqlPath + "mysql";
}
StringBuffer sbCommand = new StringBuffer();
sbCommand.append(mysqldump).append(" -u").append(this.username).append(" -p").append(this.password).append(" -h").append(this.host).append(" -P").append(this.port).append(" -B ").append(this.database).append(" < ").append(this.exportPath + sqlFile);
try {
this.exeCommand(sbCommand.toString());
} catch (IOException var6) {
}
}
```
构造的执行语句为：
```shell
cmd /c mysqlPath/mysql -u UserName -p Password -h host -P xx -B xx < sqlFile
```
而其中sqlFile是通过参数传入fileName的，这里可以用`||`来绕过执行任意命令
![image-20241101143112713](https://oss-yg-cztt.yun.qianxin.com/butian-public/ff38d284a18d80d73ebffc7ad5f428e28.png)
该类属于Service层，我们要找到Controller层对其的调用，利用jar-analyzer工具的表达式搜索
```php
#method
.isStatic(false)
.hasClassAnno("Controller")
.hasAnno("RequestMapping")
.hasField("backupService")
```
该表达式是寻找一个方法，其不是静态方法，类注释为`Controller`，方法注释为`RequestMapping`（表示是一个http接口），并且存在变量名为`backupService`(遵循该系统service层定义命名规律)。
最终找到如下方法
```java
@RequestMapping({"/restore"})
@ResponseBody
public String doRestore(@RequestParam String fileName) {
try {
this.backupService.doRestore(fileName);
} catch (Exception var3) {
var3.printStackTrace();
throw new CommonException(var3.getMessage());
}
return I18n.i18nMessage("adp\_db.success ");
}
```
### 复现
构造poc测试，成功访问
![image-20241206101001954](https://oss-yg-cztt.yun.qianxin.com/butian-public/fb629420e2bfb08180e6748c083423cbb.png)
0x04 反序列化
---------
查看shiro过程中看到了几个低版本组件，比如xstream，我们用jar-analyzer查找例如`fromXML`等触发反序列化的方法
在WechatxxxService类中找的一处调用
![image-20241104193837854](https://oss-yg-cztt.yun.qianxin.com/butian-public/fd25283d0d76af84071613d33e74b2423.png)
可以看到对整个request body进行了fromXML转换，因为时Service层我们还是可以通过之前方法快速找的controller层的调用
![image-20241104194017293](https://oss-yg-cztt.yun.qianxin.com/butian-public/f00c93983851485dfd6da6bec9735a34f.png)
### 复现
利用`woodpecker`生成poc
![image-20241104194231309](https://oss-yg-cztt.yun.qianxin.com/butian-public/f72c9a239e9787f0863b6714ebf02b90d.png)
访问接口构造请求，成功接受到请求
![image-20241104194402382](https://oss-yg-cztt.yun.qianxin.com/butian-public/f9fd8f9df3b3a993060cf9691fc9f8de7.png)
这样似乎不太完美，我们尝试构造回显
### 回显
对于tomcat下构造回显链主要是找到全局存储了request和response的类，通过tomcat启动时线程中的变量一步步反射获得request和response变量
> 基于全局存储思路出现了两种获取request和response的方法：
>
> - 方法一：通过 `WebappClassLoaderBase`来获取 Tomcat 上下文的联系，进而获取AbstractProtocol$C...