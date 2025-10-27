---
title: ChatGPT 写 PoC，拿下漏洞！
url: https://www.4hou.com/posts/1p1j
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-30
fetch_date: 2025-10-04T11:06:05.303485
---

# ChatGPT 写 PoC，拿下漏洞！

ChatGPT 写 PoC，拿下漏洞！ - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# ChatGPT 写 PoC，拿下漏洞！

Goby
[行业](https://www.4hou.com/category/industry)
2023-03-29 11:51:03

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)107220

收藏

导语：ChatGPT 编写 PoC。

## ![微信图片_20230324193309.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061463648990.jpeg "1680061463648990.jpeg")

## 0×01 前言

ChatGPT（Chat Generative Pre-trained Transformer）是当今备受瞩目的智能AI[聊天机器人](https://www.zhihu.com/search?q=%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2955441877%7D)之一。它不仅能够实现基本的语言交流，还具备许多强大的功能，例如文章撰写、代码[脚本编写](https://www.zhihu.com/search?q=%E8%84%9A%E6%9C%AC%E7%BC%96%E5%86%99&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2955441877%7D)、翻译等等。那么我们是否可以利用 ChatGpt 去辅助我们完成一些工作呢？比如当一个产品存在安全风险需要漏洞检测时，我们就需要编写对应的POC来实现。目前进行多次验证，我们初步证实了这个实验的可行性，可以训练 ChatGPT 去编写简单的 PoC，但是它对细节的把控并不够完善，例如对输出内容进行匹配的[正则表达式](https://www.zhihu.com/search?q=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2955441877%7D)的编写和一些复杂逻辑的处理等存在一定的误差，还需要人工干预修改处理。另外我们利用比对的方式验证了 ChatGPT 的一些安全猜想和训练模型的准确性。如下是将其与 Goby 实战化[网络攻防工具](https://www.zhihu.com/search?q=%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2%E5%B7%A5%E5%85%B7&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2955441877%7D)所结合进行利用检测的实现效果：

![11.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680060953184544.gif "1680060953184544.gif")

## 0×02 训练过程

我们利用 ChatGPT 与 Goby 结合编写 PoC 与 EXP 有两种方法：半自动编写和全自动编写（过程中使用 ChatGPT-Plus 账号）。

半自动编写利用 ChatGPT 进行语言格式转换，转换后生成的代码可能存在细节问题，需要进一步排错完善，最后修改对应的语句和函数内容完成 PoC 与 EXP 的编写。

全自动编写通过将使用到的代码模板、漏洞详细信息给到 ChatGPT，让它自动生成对应模板的 PoC，在给出详细信息时需要注意信息的完整与准确。目前可以实现自动编写简单的 PoC，对于EXP来说还需要进一步训练 ChatGPT 对 Goby [内置函数](https://www.zhihu.com/search?q=%E5%86%85%E7%BD%AE%E5%87%BD%E6%95%B0&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2955441877%7D)的使用等。

## 0×03 CVE-2010-2861

Adobe ColdFusion 是一款高效的网络应用服务器[开发环境](https://www.zhihu.com/search?q=%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2955441877%7D)。Adobe ColdFusion 9.0.1 及之前版本的管理控制台中存在多个目录遍历漏洞。远程攻击者可借助向 /CFIDE/administrator/enter.cfm 和 /CFIDE/administrator/archives/index.cfm 等发送的 locale 参数读取任意文件。

### 3.1 半自动编写

首先尝试让 ChatGPT 将 CVE-2010-2861 目录遍历漏洞的 Python 格式 EXP 转换为 Go 语言格式的代码，这样可以利用 ChatGPT 代替人工完成代码解释及代码转换的过程。

我们在漏洞公开平台中选取该漏洞的 EXP 代码：

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061021273667.png "1680061021273667.png")

在使用 ChatGPT 将相应漏洞的 EXP 代码转换之前，先演示一下原始 Python 代码的执行效果，具体如下：

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061037154587.png "1680061037154587.png")

开始转化格式：

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061045146709.png "1680061045146709.png")

此外，他还提供了该程序的使用方法。然而，每次 ChatGPT 的回答都可能不完全相同。此前的回答中并没有详细说明函数的具体用法，但在另一个回答中给出了以下解释：（如果需要，可在问题中增加“并介绍函数的具体用法”）

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061053103451.png "1680061053103451.png")

最后进行代码调试后，发现无法立即使用，未能成功读取所需的文件内容：

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061060435653.png "1680061060435653.png")

那么就需要开始排错，以下是排错过程：

检查正则匹配后字符串是否为空：

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061082169218.png "1680061082169218.png")

![图片8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061073151873.png "1680061073151873.png")

检查返回包内容是否正常，有无所需内容，如下返回数据包显示正常：

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061088635407.png "1680061088635407.png")

判断正则表达式有问题，无法匹配到对应内容：

通过排查发现正则表达式中没有正确匹配，因此无法将文件的内容正确取出，做出以下修改，修改后内容具体如下：

![](https://pic1.zhimg.com/80/v2-dcba1f021eb563e7ef2099ba4943ff58_720w.webp)

修改前：

![](https://pic1.zhimg.com/80/v2-a92ae18d513390d5028be0a55b5ae660_720w.webp)

最终执行结果，完成 Python—Go 的转化：

![图片12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061100468718.png "1680061100468718.png")

前面我们已经成功将 Python 格式的EXP转换为了 Go 语言格式，现在尝试将其转换为 Goby 格式的 PoC 和 EXP。

由于 Goby 使用的是基于 Go 语言开发的自研漏洞框架，为方便用户使用，其中已有很多内置函数可供用户使用，所以只需要利用上述部分代码即可完成 PoC 和 EXP，以下是 EXP 修改的大致说明与详细内容：

![图片13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061111160592.png "1680061111160592.png")

![图片14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061121173707.png "1680061121173707.png")

修改 import 内容：

![图片15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061128757917.png "1680061128757917.png")

由于生成的 EXP 在命令行使用时需要手动输入参数：

![图片16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061134161008.png "1680061134161008.png")

那么在 PoC 转化时，需要重新定义常量，并利用 Goby 中的 httpclient.FixUrl.IP 与 httpclient.FixUrl.Port 获取测试的 IP 和端口号，确定测试的文件路径 path：

![](https://pic3.zhimg.com/80/v2-30d482944c9af418008b6de813f0a20a_720w.webp)

接着在 PoC 中添加条件判断语句，判断漏洞存在的特征，并返回 true（有漏洞）：

![](https://pic2.zhimg.com/80/v2-ca6dff12db0a08ce23cb71a569e6ef01_720w.webp)

最后删除多余的输出打印代码即可完成 PoC 转化，如：

![](https://pic2.zhimg.com/80/v2-005aab76ecab3ddb3ea05e876f1618e1_720w.webp)

EXP 转化时，需重新定义变量，利用 Goby 中的 expResult.HostInfo.IP 与 expResult.HostInfo.Port 获取测试的IP和端口号，利用 ss.Params["filePath"]. (string) 获取用户输入的 EXP 参数——测试文件路径 filePath：

![图片20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061154130977.png "1680061154130977.png")

接着在 EXP 代码中添加条件判断语句，判断 EXP 是否执行成功，并输出 EXP 执行结果，完成 EXP 转化：

![图片21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061169113420.png "1680061169113420.png")

### 3.2 全自动编写

在使用 ChatGPT 与人工相结合编写后，我们进一步尝试使用它来撰写 Goby 格式的 PoC。

首先将 Goby 格式的模板给出：

![图片22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061163185668.png "1680061163185668.png")

接着将漏洞的编号、产品、类型、Url、漏洞文件、参数和判断成功条件给出，说明相关的字段格式，我们最终得到了下面的代码，它已经可以通过 Goby 前端的编译，并可以成功地生成简单的 PoC：

![图片23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061247441952.png "1680061247441952.png")

模型训练初步完成，继续使用第二个案例验证模型完善程度：

![图片24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230329/1680061255153828.png "1680061255153828.png")

发现 Name 字段还是存在格式错误，再次训练修改（若验证中 Name 字段等输出正确，那么即可跳过此纠错步骤）：

![图片25.png](https://img.4hou.com/...