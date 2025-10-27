---
title: SSRF 漏洞自动化 寻找
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496832&idx=1&sn=5c72712e20772f2279b09ca9a748afc2&chksm=e8a5fee3dfd277f5990fbe3dfe7247c7dd7bf125a233ad4ec99a8afb49b1b2e29ae25f7866b6&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-13
fetch_date: 2025-10-06T20:09:08.618700
---

# SSRF 漏洞自动化 寻找

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6JGkozDWzXR46Koxav5LguUibnIkhicBle4V662pGc9vUI6l1RtkekicM2I1Zw86JMaHe6OIQUElhiaw/0?wx_fmt=jpeg)

# SSRF 漏洞自动化 寻找

真爱和自由

迪哥讲事

## 环境搭建

下载项目https://github.com/l4yn3/micro\_service\_seclab

然后放入 IDEA 即可，之后运行

这里主要研究 SSRFSSRF 的漏洞代码

```
package com.l4yn3.microserviceseclab.controller;

import com.squareup.okhttp.Call;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Response;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.apache.http.client.fluent.Request;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

@RestController
@RequestMapping(value = "/ssrf")
public class SSRFController {

    @RequestMapping(value = "/one")
    public String One(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            return connection.getResponseMessage();
        } catch (IOException var3) {
            System.out.println(var3);
            return "Hello";
        }
    }

    @RequestMapping(value = "/two")
    public String Two(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            HttpResponse response = Request.Get(String.valueOf(url)).execute().returnResponse();
            return response.toString();
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }

    @RequestMapping(value = "/three")
    public String Three(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            OkHttpClient client = new OkHttpClient();
            com.squareup.okhttp.Request request = new com.squareup.okhttp.Request.Builder().get().url(url).build();
            Call call = client.newCall(request);
            Response response = call.execute();
            return response.toString();
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }
    @RequestMapping(value = "/four")
    public String Four(@RequestParam(value = "url") String imageUrl) {
        try {
            DefaultHttpClient client = new DefaultHttpClient();
            HttpGet get = new HttpGet(imageUrl);
            HttpResponse response = client.execute(get);
            return response.toString();
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }

    @RequestMapping(value = "five")
    public String Five(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            InputStream inputStream = url.openStream();
            return String.valueOf(inputStream.read());
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }
}
```

但是这个不太明显我修改了一下这样更好观察

```
package com.l4yn3.microserviceseclab.controller;

import com.squareup.okhttp.Call;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Response;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.apache.http.client.fluent.Request;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

@RestController
@RequestMapping(value = "/ssrf")
public class SSRFController {

    @RequestMapping(value = "/one")
    public String One(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            return connection.getResponseMessage();
        } catch (IOException var3) {
            System.out.println(var3);
            return "Hello";
        }
    }

    @RequestMapping(value = "/two")
    public String Two(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            HttpResponse response = Request.Get(String.valueOf(url)).execute().returnResponse();
            return response.toString();
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }

    @RequestMapping(value = "/three")
    public String Three(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            OkHttpClient client = new OkHttpClient();
            com.squareup.okhttp.Request request = new com.squareup.okhttp.Request.Builder().get().url(url).build();
            Call call = client.newCall(request);
            Response response = call.execute();
            return response.toString();
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }
    @RequestMapping(value = "/four")
    public String Four(@RequestParam(value = "url") String imageUrl) {
        try {
            DefaultHttpClient client = new DefaultHttpClient();
            HttpGet get = new HttpGet(imageUrl);
            HttpResponse response = client.execute(get);
            return response.toString();
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }

    @RequestMapping(value = "five")
    public String Five(@RequestParam(value = "url") String imageUrl) {
        try {
            URL url = new URL(imageUrl);
            InputStream inputStream = url.openStream();
            return String.valueOf(inputStream.read());
        } catch (IOException var1) {
            System.out.println(var1);
            return "Hello";
        }
    }
}
```

```
http://127.0.0.1:8888/ssrf/one?url=http://www.baidu.com
```

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj6JGkozDWzXR46Koxav5LguCKsC4ghiaSr01Qub9G6x8trpInT9JFA2sORshd5NticV0oULxtPic7X7Q/640?wx_fmt=png&from=appmsg)成功

## 漏洞分析

我们首先需要看明白造成 SSRF 漏洞的类型

**HttpURLConnection 发起请求**

```
@RequestMapping(value = "/one")
public String One(@RequestParam(value = "url") String imageUrl) {
    try {
        URL url = new URL(imageUrl);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        return connection.getResponseMessage();
    } catch (IOException var3) {
        System.out.println(var3);
        return "Hello";
    }
}
```

HttpURLConnection 是 Java 标准库中的一个类，用于通过 URL 发起 HTTP 请求。这里直接将用户提供的 URL 用来创建连接，并发送 GET 请求

而且 URL 我们可以控制，造成了 ssrf

**Apache HttpClient**

```
@RequestMapping(value = "/two")
public String Two(@RequestParam(value = "url") String imageUrl) {
    try {
        URL url = new URL(imageUrl);
        HttpResponse response = Request.Get(String.valueOf(url)).execute().returnResponse();
        return response.toString();
    } catch (IOException var1) {
        System.out.println(var1);
        return "Hello";
    }
}
```

这里使用了 Apache HttpClient（通过 fluent API）发起 HTTP 请求。用户提供的 URL 被用来发起 GET 请求，并返回响应。

**OkHttp**

```
@RequestMapping(value = "/three")
public String Three(@RequestParam(value = "url") String imageUrl) {
    try {
        URL url = new URL(imageUrl);
        OkHttpClient client = new OkHttpClient();
        com.squareup.okhttp.Request request = new com.squ...