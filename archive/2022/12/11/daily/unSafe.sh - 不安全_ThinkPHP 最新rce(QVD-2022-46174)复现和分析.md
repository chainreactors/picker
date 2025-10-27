---
title: ThinkPHP 最新rce(QVD-2022-46174)复现和分析
url: https://buaq.net/go-139514.html
source: unSafe.sh - 不安全
date: 2022-12-11
fetch_date: 2025-10-04T01:10:21.111523
---

# ThinkPHP 最新rce(QVD-2022-46174)复现和分析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/62542c0ffb03dbd22558b4203bf8cbed.jpg)

ThinkPHP 最新rce(QVD-2022-46174)复现和分析

昨晚到处都是关于thinkphp rce漏洞的消息，所以今天想着分析复现一下我这里用的是一款基于thinkphp5开发的程序进行测试，漏洞成功利用需要think
*2022-12-10 22:25:0
Author: [xz.aliyun.com(查看原文)](/jump-139514.htm)
阅读量:227
收藏*

---

昨晚到处都是关于thinkphp rce漏洞的消息，所以今天想着分析复现一下

我这里用的是一款基于thinkphp5开发的程序进行测试，漏洞成功利用需要thinkphp开启多语言模式

## 利用一

**直接文件包含：**

## 利用二

使用pearcmd在/tmp文件夹下创建文件再进行包含，前提是php安装了pearcmd,并且开启了register\_argc\_argv选项，这里有疑问参见[P神博客](https://www.leavesongs.com/PENETRATION/docker-php-include-getshell.html "P神博客")
首先创建文件

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210215511-43cdad60-7892-1.png)
再包含

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210215522-4a27e0f4-7892-1.png)

thinkphp程序初始化都会运行/thinkphp/library/think/app.php的initialize()函数，函数中使用this->loadLangPack()获取语言包
![](https://xzfile.aliyuncs.com/media/upload/picture/20221210215848-c4ecb9cc-7892-1.png)
进入loadLangPack看一下
![](https://xzfile.aliyuncs.com/media/upload/picture/20221210221126-890628b0-7894-1.png)
可以看到当设置多语言模式后，执行$this->lang->detect()检测语言，进入/thinkphp/library/think/lang.php detect()函数
![](https://xzfile.aliyuncs.com/media/upload/picture/20221210221305-c3d266a2-7894-1.png)
程序会按照顺序通过url，cookie或浏览器获取语言设置，我们在lang中输入payload，此时payload被赋值给为参数$langSet。回到loadLangPack函数，下一步执行$this->request->setLangset($this->lang->range());设置语言，再执行load函数进行加载。
![](https://xzfile.aliyuncs.com/media/upload/picture/20221210221927-a78a9996-7895-1.png)
可以看到load函数的参数是由目录和langset参数拼接构造的，并且**没有对传入参数进行过滤和限制**。
跟进/thinkphp/library/think/lang.php的load函数，参数传递给了$file，漏洞触发位于标识位置，**函数对传入的file参数直接进行了包含操作，造成文件包含漏洞**

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210222055-dc11af88-7895-1.png)

文章来源: https://xz.aliyun.com/t/11940
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)