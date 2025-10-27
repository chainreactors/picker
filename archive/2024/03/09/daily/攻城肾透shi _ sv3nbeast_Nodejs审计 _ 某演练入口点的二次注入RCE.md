---
title: Nodejs审计 | 某演练入口点的二次注入RCE
url: https://www.svenbeast.com/post/b_Y7hJQKj/
source: 攻城肾透shi | sv3nbeast
date: 2024-03-09
fetch_date: 2025-10-04T12:07:30.661347
---

# Nodejs审计 | 某演练入口点的二次注入RCE

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)
[ ]

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

Dark

\u6697\u9ED1

☰ Menu

☰ 菜单

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)

# Nodejs审计 | 某演练入口点的二次注入RCE

Author:
[斯文](/)

Date: 2024-03-08
Reading Time:5.9 mins
words:1614

Category:
[审计](https://www.svenbeast.com/tag/YzSDJjXj4/)
[Nodejs](https://www.svenbeast.com/tag/lRqSQSbjdR/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

share:

作者:
[斯文](/)
日期: 2024-03-08
阅读时间:5.9 分钟
字数:1614
分类:
[审计](https://www.svenbeast.com/tag/YzSDJjXj4/)
[Nodejs](https://www.svenbeast.com/tag/lRqSQSbjdR/)
[笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

分享:

## 0x01 背景

​ 之前举行过的云资产的演练又开始了，目前拥有目标某设备的老版本前台RCE漏洞，但本次因某些原因不允许使用此漏洞，所以入口点需要重新找，准备找个新洞，记录nodejs审计过程如下

## 0x02 审计

### 1.前期过程

​ 首先我的想法是寻找那种简单的命令注入漏洞，因为之前的洞就蛮简单的，我做了如下操作，目的是定位调用了命令执行函数的路由文件

```
grep -rl "child_process" --include=\*.js .
```

![image-20240306153951101](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202403061539661.png)

​ 然后首先看的是ping功能，很简单的定义路由，接参，然后传入命令执行函数中，但发现存在正则过滤，由于正则我都是现记现忘，重新看了下，写死了\d限制了其他字符，所以漏洞不存在

![image-20240306154513368](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202403061549421.png)

​ 接着过了一遍筛选出来的所有存在命令注入函数的路由，没发现能用的，有的看着代码是存在漏洞但是当用在目标网站上是不存在漏洞的，推测是目标更新了版本进行修复漏洞（这里还没有去跟踪各个函数调用链深挖）

​ 随即又搜了下nodejs的文章知道了还可以寻找代码执行漏洞，也就是eval函数，eval参数可控时直接进行导入命令执行进行调用就行

```
http://localhost:3000/?abc=require('child_process').execSync('open -a Calculator.app', { encoding: 'utf8' })
```

![image-20240306155641844](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202403061556330.png)

​ grep大法之故技重施，实际就有2个route文件存在eval，当然别的文件也是耗费精力看了但没东西，就不讲了，后续在反推eval函数代码执行的调用链中同时找到一个命令注入漏洞

```
grep -rl "eval" --include=\*.js .
```

![image-20240306160716095](http://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202403061625264.png)

* + [0x01 背景](#0x01-%E8%83%8C%E6%99%AF)
  + [0x02 审计](#0x02-%E5%AE%A1%E8%AE%A1)
    - [1.前期过程](#1%E5%89%8D%E6%9C%9F%E8%BF%87%E7%A8%8B)
    - [2.代码执行](#2%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)
      * [2.1 getRegexPattern()](#21-getregexpattern)
      * [2.2 getNodevalueBynodeType()](#22-getnodevaluebynodetype)
      * [2.3 getRelationNodeandLinks()](#23-getrelationnodeandlinks)
      * [2.4 execGetNostructureNodeAndLinks()](#24-execgetnostructurenodeandlinks)
      * [2.5 router.post](#25-routerpost)
        + [2.5.1 splitrelationsBystructure()](#251-splitrelationsbystructure)
        + [2.5.2 通过前端定位添加关系规则功能](#252-%E9%80%9A%E8%BF%87%E5%89%8D%E7%AB%AF%E5%AE%9A%E4%BD%8D%E6%B7%BB%E5%8A%A0%E5%85%B3%E7%B3%BB%E8%A7%84%E5%88%99%E5%8A%9F%E8%83%BD)
      * [2.6 漏洞利用](#26-%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8)
    - [3.命令执行](#3%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C)
      * [3.1 generateToCsv()](#31-generatetocsv)

Author:
斯文

Permalink:
<https://www.svenbeast.com/post/b_Y7hJQKj/>

License:
MIT License

作   者:
斯文

永久链接:
<https://www.svenbeast.com/post/b_Y7hJQKj/>

协   议:
MIT License

Tag(s):

[# 审计](https://www.svenbeast.com/tag/YzSDJjXj4/)
[# Nodejs](https://www.svenbeast.com/tag/lRqSQSbjdR/)
[# 笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

back

标签:

[# 审计](https://www.svenbeast.com/tag/YzSDJjXj4/)
[# Nodejs](https://www.svenbeast.com/tag/lRqSQSbjdR/)
[# 笔记](https://www.svenbeast.com/tag/rwt8EXIMSg/)

返回

[Java工具 | JMG添加自定义内存马](https://www.svenbeast.com/post/HDu5nl4VC/)
[Java点滴 | interface&implements](https://www.svenbeast.com/post/5MkJJ8OB9/)

赏  ![support](https://www.svenbeast.com/media/images/alipay.png)**支付宝**   ![support](https://www.svenbeast.com/media/images/wechat.png)**微信**

[京ICP备19028185号](http://beian.miit.gov.cn/)

攻城肾透shi | sv3nbeast ©Copyright
 ![dandan](https://i.loli.net/2020/03/31/kG71rUoEW5YQq4h.gif)

/\*
\*/

召唤伊斯特瓦尔