---
title: 代码审计之XXE与SSRF与Struts2审计案例
url: https://mp.weixin.qq.com/s/BUcNCx9qHVwroobniFFB3A
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:32:42.177859
---

# 代码审计之XXE与SSRF与Struts2审计案例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKYphmw4EMGbbnpic0VLV8fDO587u5fPib14ZjeicjL8XqKibDiarjupKib1Bw/0?wx_fmt=jpeg)

# 代码审计之XXE与SSRF与Struts2审计案例

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

本公众号所发文章仅用于技术交流学习，不得用于任何违法犯罪目的，一切后果自行承担，与本公众号以及作者无关。

XXE与SSRF与Struts2审计案例XXE注入XMLReader 解析文件SAXBuilder 解析文件SAXReader解析XML内容SAXParserFactory解析XML⽂件DocumentBuilderFactory解析xml内容实际案例SSRF漏洞审计HttpURLConnection.getInputStream案例代码URLConnection.getInputStream代码示例HttpClient.execute代码示例Request.Get.execute代码示例URL.openStream代码示例SSRF漏洞真实案例Struts2漏洞审计

# XXE与SSRF与Struts2审计案例

## XXE注入

漏洞触发点，一般有如下五点：

```
 XMLReader 解析文件
 SAXBuilder 解析文件
 SAXReader 解析文件
 SAXParserFactory 解析文件
 DocumentBuilderFactory 解析文件
```

上述为java中常见的一些关于XXE的类或者方法

### XMLReader 解析文件

这里面去找 XMLReader    xmlReader.parse    inputSource.setCharacterStream

```
 packagemain.java.XMLInjection;

 importorg.xml.sax.InputSource;
 importorg.xml.sax.XMLReader;
 importorg.xml.sax.helpers.XMLReaderFactory;

 importjavax.xml.stream.XMLReporter;

 publicclassURLStreamExample {
     publicstaticvoidmain(String[] args) {
         try {
             //创建XMLReader实例
             XMLReaderxmlReader=XMLReaderFactory.createXMLReader();

             //禁用外部实体加载，这是防止XXE攻击的关键步骤
             //xmlReader.setFeature("http://apache.org/xml/features/disallow-doctype-decl",true);
             //构建一个包含XXE漏洞的字符串
             Stringxml="<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n"+
                     "<!DOCTYPE foo [\n"+
                     "<!ELEMENT foo ANY >\n"+
                     "<!ENTITY xxe SYSTEM \"http://localhost:8000\" >]>\n"+
                     "<creds>\n"+
                     "    <user>&xxe;</user>\n"+
                     "    <pass>mypass</pass>\n"+
                     "</creds>";

             //使用InputSource包装XML字符串
             InputSourceinputSource=newInputSource();
             inputSource.setCharacterStream(newjava.io.StringReader(xml));

             //解析XML
             xmlReader.parse(inputSource);
         }
         catch (Exceptione) {
             e.printStackTrace();
         }
     }
 }
```

运行该代码

![image-20250608162756275](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKZzt09HSxpubKtyfHKZHnOfuUAS2XZKqfibqAqicVSVwVr05gDoGlxBXA/640?wx_fmt=png&from=appmsg)

![image-20250608162959326](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKtIQYc8aU1KfNLPCb5O6B6S4glJpys5BsW5XIBSNvlOXdIXIOiatmWJQ/640?wx_fmt=png&from=appmsg)

红色框出来的，就是我们payload的位置

通过启用

```
 xmlReader.setFeature("http://apache.org/xml/features/disallow-doctype-decl",true);
```

来防止XXE漏洞，此时再运行代码

![image-20250608163026314](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKJSeO10Jyo1z7Be6ibFic6icB2nHseB7ibchAk0OkVk4MSovuy07l4x3wLg/640?wx_fmt=png&from=appmsg)

### SAXBuilder 解析文件

其实后续的原理和第一个都是一样的，只不过采取了不一样的办法来解析XML

![image-20250608171640729](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK9CvfjV7Hd7sKYrY73mFI245HyICI1qsPe1BSH4PrDckMFbicJiaNC6UA/640?wx_fmt=png&from=appmsg)

这个代码要进⾏⼀个maven导⼊，导⼊⼀个依赖：

进来找  saxBuilder.build     SAXBuilder

![image-20250608171359179](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKPB1Nf3Qh3jXYc9Y6qgEAJibhtrLF4QtbR6X1szkozRKBkFqnCpEbj8g/640?wx_fmt=png&from=appmsg)

这里通过 build 来构建 xml ，让他执行

### SAXReader解析XML内容

**`Document document = reader.read(new StringReader(xml));`**

![image-20250608171757132](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK1Boqx8QP9Uu3hlk0E9WuzGrvOmbRaqp6HAvPm6hSvP8siaZVO62hnwA/640?wx_fmt=png&from=appmsg)

这种方式通过 read 来解析XML

同样要进⾏导⼊相关的依赖

![image-20250608171847076](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKK3iaYHuDyPURllurhuz8OicI183fKPVAiajiaw4xJE8GYqoNcVqkEhy2bg/640?wx_fmt=png&from=appmsg)

### SAXParserFactory解析XML⽂件

![image-20250608171954407](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK1cRMtEw8mfb9icmTAvibPDsMw8Xv3yNMmOcfO3DqelfVFQxofV0ibhDCw/640?wx_fmt=png&from=appmsg)

### DocumentBuilderFactory解析xml内容

![image-20250608172105508](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKsia3eIQf9RoNicpoPWxVJMMnS3BNlzUbR3KIicr0BHmk5nxjvljaWvcSA/640?wx_fmt=png&from=appmsg)

### 实际案例

进入源码，找到 WEB-INF 的 web.xml  文件，去找 url-pattern

![image-20250608181417952](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK2vjuWKiag2eIp9HJaTrBoQny4FdMzWxxFIWueIsaNf2z5BKLjd5n0Xg/640?wx_fmt=png&from=appmsg)

在这一行代码之前，所有的 url-pattern 就和  `<url-pattern>*.option</url-pattern>` 是一样的，这种的就没必要去看了，因为根本找不到一对一的目的类，当然，还有一个全站过滤的

![image-20250608181619286](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK6d3fMH0xoEOtqNZ9RsCBpnYrlWGVGuoQ6OLcOrrRz1WMCtdcJMXAmA/640?wx_fmt=png&from=appmsg)

但是我们看上面的注释，这个全站过滤的是为了给Spring提供编码转换功能的，所以其实也没用，就长下面这样

![image-20250608181813894](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKAicALbibLByNibNYDzw3Uo8HTlpxrpMsIJpxdw3Opicu51OjP5C0iaFjKCQ/640?wx_fmt=png&from=appmsg)

所以我们继续寻找 url-pattern，先到刚刚的  picCheck 里去看看

![image-20250608181951034](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKTibljcO64LBVFzmFVe5d62gmLRk3BRmHXYtdmckt2G4b8WagkYpCnmQ/640?wx_fmt=png&from=appmsg)

![image-20250608182132314](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKX62nHbD57eDKDxqQcPicVic3XDUQUvuQgt2cXEdib8ibHx4fyD0kibhMTEw/640?wx_fmt=png&from=appmsg)

![image-20250608182147683](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKBeYcumqYyI1UMpPOTkubqxeDrHDONmiawxVZicHm7jWXPrGSPic1icm74w/640?wx_fmt=png&from=appmsg)

![image-20250608182203059](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKAia7zjJgHPMJHL601m8xHCibbtROgtZyj4ygFpMADXqicBC5MXRic7ymgA/640?wx_fmt=png&from=appmsg)

OK，几个关键字都没有，然后再看了一眼代码，确实什么都没有

继续往下找 url-pattern

![image-20250608182306903](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKWHANW4ey8tjoflic1Hic3zrb0EHBZkPxp7FUw4mYqRPAUIMp4wYdhj2w/640?wx_fmt=png&from=appmsg)

![image-20250608182335822](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKjKQenVFAhm69p8HdT5GuDFheqjaSFCWI4yoWQ25cQg9zLBmIvO5tzA/640?wx_fmt=png&from=appmsg)

继续

![image-20250608182404031](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKFI3fEqbQgxic0ibPy014Qzwic4FpVGia5P6AZLoZkicJDTfrtrl9cYVlvVQ/640?wx_fmt=png&from=appmsg)

![image-20250608182442437](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKIQ81OweFQwz9O6ZKKLUw9UIEU0uuRxsf3pN3V0KPA5W7L5BcgPyDZQ/640?wx_fmt=png&from=appmsg)

继续

![image-20250608182525764](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAK00OH8qic2wbYEUZHbegBJzQ6Tk4u2aRX9ib2jLXzWMPfMyorUxIayEdg/640?wx_fmt=png&from=appmsg)

![image-20250608183031152](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKPCPv3BnT7uKj2TqW7DBib3neC0hPPPXu5XEek6k0BRe2VUkDYeau63A/640?wx_fmt=png&from=appmsg)

![image-20250608183009949](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoRQYAUNYmdapJSvzvIuhbAKicxPu9aoHkyg4MQdy1d0RQzaR1QUwphdr40yPSHqIZg2KicpbjpC4KUQ/640?wx_fmt=png&from=appmsg)

获取xml数据并解析，将解析后的结果返回输出

这不就是吗

## SSRF漏洞审计

在JAVA当中⽀持的协议  file ftp mailto http https jar netdoc

该漏洞触发点，一般有以下六点：

```
 HttpURLConnection.getInputStream
 URLConnection.getInputStream
 HttpVlient.execute
 Request.Get.execute
 Request.Post.execute
 URL.openStream
```

### HttpURLConnection.getInputStream案例代码

**`HttpURLConnection connection = (HttpURLConnection) url.openConnection();`**

```
 packagemain.java;

 importjava.io.BufferedReader;
 importjava.io.InputStreamReader;
 importjava.net.HttpURLConnection;
 importjava.net.URL;

 publicclassSSRFVulnerableExample {

     publicstaticvoidmain(String[] args) {
         try {
             //从⽤户输⼊获取URL
             StringtargetUrl="http://localhost:8000";    //这⾥应该是⽤户输⼊的URL
             URLurl=newURL(targetUrl);
             HttpURLConnectionconnection= (HttpURLConnection) url.openConnection();

             //获取输⼊流并读取响应
             try (BufferedReader...