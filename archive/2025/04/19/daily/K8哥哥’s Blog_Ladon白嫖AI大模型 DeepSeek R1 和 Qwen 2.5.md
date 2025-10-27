---
title: Ladon白嫖AI大模型 DeepSeek R1 和 Qwen 2.5
url: http://k8gege.org/p/freeai.html
source: K8哥哥’s Blog
date: 2025-04-19
fetch_date: 2025-10-06T22:06:30.360858
---

# Ladon白嫖AI大模型 DeepSeek R1 和 Qwen 2.5

[![logo](/../k8img/logo.png)

### K8哥哥](/ "K8gege")

## 没有绝对安全的系统

[K8哥哥’s Blog](http://k8gege.org)

* [Home](/)
* [Ladon](/Ladon/)
* [Code](/tags/Code/)
* [Exp](/tags/Exp/)
* [Tool](/tags/Tool/)
* [Music](https://k8music.github.io)
* [Archives](/archives/)
* [Friends](/friends/)
* [Rss](/atom.xml)

# AI未授权漏洞 利用Ladon白嫖DeepSeek 和 Qwen 2.5

[Exp](/categories/Exp/) [Ladon](/categories/Ladon/)

[DeepSeek](/tags/DeepSeek/) [Qwen 2.5](/tags/Qwen-2-5/)

2025/04/18

<%
Visit
%>

=============================================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### 免责声明

Ladon项目所涉及的技术、思路和工具仅供学习或授权渗透，非法用途后果自负。

### 漏洞编号

### 影响版本

Ollama部署大模型
DeepSeek R1
Qwen 2.5

### 应用指纹

app=“ollama”

### 漏洞简介

通过调用 DeepSeek R1 和 Qwen 2.5 API进行聊天，成功聊天，回显ISOK

#### 批量扫描

![使用http访问查看图片](http://k8gege.org/k8img/Ladon/freeai.png)

#### 批量结果

扫描1W只有478个，看来大部份还是设置授权的，单纯识别Ollama不等于能白嫖，这个和探测CMS页面存在就说有漏洞同理，目标刚好有，小白就认为扫描器牛逼，实际上靠的是运气。等过段时间目标补丁打得差不多，通过版本识别漏洞的工具，再扫提示有洞，但根本打不了。Ladon百分之99探测漏洞模块，均通过漏洞原理，能扫到大部分就能EXP打，个别漏洞采用版本，不确定存在漏洞会加?号
![使用http访问查看图片](http://k8gege.org/k8img/Ladon/deepseek.png)

### CS使用POC

|  |  |
| --- | --- |
| ``` 1 ``` | ``` beacon> Ladon http://192.168.1.8 FreeAI ``` |

PS: Cobalt Strike内存加载FreeAI

### 指定URL

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Ladon http://192.168.1.8 FreeAI ``` |

![使用http访问查看图片](http://k8gege.org/k8img/Ladon/freeai.png)

### 指定IP

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Ladon 192.168.1.8 FreeAI ``` |

### 批量URL

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Ladon url.txt FreeAI ``` |

PS：TXT可存放IP、IP:Port、URL等格式

![使用http访问查看图片](http://k8gege.org/k8img/Ladon/freeai.png)

### 批量IP

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Ladon ip.txt FreeAI Ladon noping ip.txt FreeAI ``` |

### 指定C段

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` Ladon 192.168.1.8/24 FreeAI Ladon noping 192.168.1.8/24 FreeAI  Ladon 192.168.1.8/24 FreeAI Ladon noping 192.168.1.8/24 FreeAI ``` |

### 指定B段

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` Ladon 192.168.1.8/b FreeAI Ladon noping 192.168.1.8/b FreeAI  Ladon 192.168.1.8/b FreeAI Ladon noping 192.168.1.8/b FreeAI ``` |

### 指定A段

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` Ladon 192.168.1.8/a FreeAI Ladon noping 192.168.1.8/a FreeAI  Ladon 192.168.1.8/a FreeAI Ladon noping 192.168.1.8/a FreeAI ``` |

### 批量C段

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` Ladon ip24.txt FreeAI Ladon ipc.txt FreeAI  Ladon noping ip24.txt FreeAI Ladon noping ipc.txt FreeAI ``` |

PS: TXT存放多个目标的C段IP

### 批量B段

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Ladon ip16.txt FreeAI Ladon noping ip16.txt FreeAI ``` |

PS: TXT存放多个目标的B段IP

### 批量网段

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Ladon cidr.txt FreeAI Ladon noping cidr.txt FreeAI ``` |

PS: TXT存放各种IP网段，全网无差别扫描

### 转载声明

K8博客文章随意转载，转载请注明出处！ © K8gege <http://k8gege.org>

![](../images/k8join2.png)

扫码加入K8小密圈

转载声明：
K8博客文章随意转载，转载请注明出处！ © [K8gege](http://k8gege.org)

[上一篇

Ladon CVE-2025-32433 Erlang/OTP SSH EXP](/p/CVE-2025-32433.html "Ladon CVE-2025-32433 Erlang/OTP SSH EXP")
[下一篇

Ladon ShiroEXP高效爆破Key 反序列化漏洞复现](/p/shiroexp.html "Ladon ShiroEXP高效爆破Key 反序列化漏洞复现")

### Table of Contents

1. [免责声明](#%E5%85%8D%E8%B4%A3%E5%A3%B0%E6%98%8E)
2. [漏洞编号](#%E6%BC%8F%E6%B4%9E%E7%BC%96%E5%8F%B7)
3. [影响版本](#%E5%BD%B1%E5%93%8D%E7%89%88%E6%9C%AC)
4. [应用指纹](#%E5%BA%94%E7%94%A8%E6%8C%87%E7%BA%B9)
5. [漏洞简介](#%E6%BC%8F%E6%B4%9E%E7%AE%80%E4%BB%8B)
   1. [批量扫描](#%E6%89%B9%E9%87%8F%E6%89%AB%E6%8F%8F)
   2. [批量结果](#%E6%89%B9%E9%87%8F%E7%BB%93%E6%9E%9C)
6. [CS使用POC](#CS%E4%BD%BF%E7%94%A8POC)
7. [指定URL](#%E6%8C%87%E5%AE%9AURL)
8. [指定IP](#%E6%8C%87%E5%AE%9AIP)
9. [批量URL](#%E6%89%B9%E9%87%8FURL)
10. [批量IP](#%E6%89%B9%E9%87%8FIP)
11. [指定C段](#%E6%8C%87%E5%AE%9AC%E6%AE%B5)
12. [指定B段](#%E6%8C%87%E5%AE%9AB%E6%AE%B5)
13. [指定A段](#%E6%8C%87%E5%AE%9AA%E6%AE%B5)
14. [批量C段](#%E6%89%B9%E9%87%8FC%E6%AE%B5)
15. [批量B段](#%E6%89%B9%E9%87%8FB%E6%AE%B5)
16. [批量网段](#%E6%89%B9%E9%87%8F%E7%BD%91%E6%AE%B5)

Total:

Copyright ©
2020
 |
Powered by [K8gege](//k8gege.org)