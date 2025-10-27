---
title: timwhitez starred I-Wanna-Get-All
url: https://buaq.net/go-241641.html
source: unSafe.sh - 不安全
date: 2024-05-27
fetch_date: 2025-10-06T16:49:06.568691
---

# timwhitez starred I-Wanna-Get-All

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

![](https://8aqnet.cdn.bcebos.com/05e22ac4eeab5f9b8a19714ef9241eee.jpg)

timwhitez starred I-Wanna-Get-All

介绍目前集成281漏洞，包括nday、1day（未公开poc）java环境java version "1.8.0\_121"Java(TM) SE Runtime Environment (b
*2024-5-26 22:16:9
Author: [github.com(查看原文)](/jump-241641.htm)
阅读量:38
收藏*

---

#### 介绍

目前集成288漏洞，包括nday、1day（未公开poc）

java环境
java version "1.8.0\_121"
Java(TM) SE Runtime Environment (build 1.8.0\_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)

基于Apt-T00ls二次开发工具，I Wanna Get All 安全工具, 严禁一切未授权漏洞扫描攻击

使用工具或文章转发用于其他途径，请备注作者及工具地址来源。

使用工具前建议判断系统指纹框架，部分漏洞为接口探测存活判断是否成功，实际利用情况以执行情况为准

很多误报还需要完善，欢迎各位提issues

#### 更新

更新功能：dnslog配置、Jeecg token配置

更新Jeecg-Boot模块，内置16个漏洞

[![image-20240223101114978](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/jeecgcheck.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/jeecgcheck.png)

[![image-20240223101114978](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/dnslog.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/dnslog.png)

#### ATT模块

```
    1. 用友serial漏洞大部分为接口探测，请ATT根据实际情况进行判断
    2. 部分漏洞为确保准确性，请先进行检测，再进行点击执行利用
    3. 使用ALL进行漏洞探测时，由于多线程等其他原因会产生误报
    4. 文件上传漏洞，上传文件后执行进行上传，并使CMD栏为空，请先检测尝试上传后再利用
    5. 命令执行漏洞利用CMD写入命令后进行执行。
    6. 清屏按钮可清除除URL地址外所有信息
    7. 根据执行结果提示并选择其他模块利用
    8. POC模块目前集成poc情况共近230余个，包含至今HVV、goby纰漏漏洞(因poc集中管理可能出现误报，请配置代理抓包判断)，如下:
       (1).用友NC&反序列化接口----------------------------------fofa:title="YONYOU NC"
       (2).用友GRP--------------------------------------------fofa:app="yonyou-GRP-U8"
       (3).用友NCCloud----------------------------------------fofa:body="nccloud"
       (4).用友tplus------------------------------------------fofa:app="畅捷通-TPlus"
       (5).用友U8C--------------------------------------------fofa:app="用友-U8-Cloud"
       (6).用友ufida------------------------------------------fofa:body="ufida.ico"
       (7).泛微Ecology----------------------------------------fofa:app="泛微-协同办公OA"
       (8).泛微Emobile----------------------------------------fofa:title="移动管理平台-企业管理"
       (9).泛微Eoffice----------------------------------------fofa:app="泛微-EOffice"
       (10).蓝凌OA--------------------------------------------fofa:app="Landray-OA系统"
       (11).蓝凌EIS-------------------------------------------fofa:app="Landray-EIS智慧协同平台"
       (12).万户OA--------------------------------------------fofa:body="/defaultroot/"
       (13).致远A6A8------------------------------------------fofa:app="致远互联-OA"
       (14).致远MServer---------------------------------------fofa:body="/mobile_portal/"
       (15).致远yyoa------------------------------------------fofa:body="yyoa" && app="致远互联-OA"
       (16).通达OA--------------------------------------------fofa:app="TDXK-通达OA"
       (17).帆软组件-------------------------------------------fofa:"Powered by 帆软"
       (18).金蝶Apusic----------------------------------------fofa:header="Apusic"
       (19).金蝶EAS-------------------------------------------fofa:app="Kingdee-EAS"
       (20).金蝶云OA------------------------------------------fofa:app="金蝶云星空-管理中心"
       (21).金和OA--------------------------------------------fofa:app="金和网络-金和OA"
       (22).红帆OA--------------------------------------------fofa:app="红帆-ioffice"
       (23).宏景HCM--------------------------------------------fofa:app="HJSOFT-HCM"
       (24).亿赛通---------------------------------------------fofa:app="亿赛通-电子文档安全管理系统"
       (23).飞企互联-------------------------------------------fofa:app="FE-协作平台"
```

##### 示例1：

用友NC 漏洞检测 (选择OA类型 -- 选择漏洞 -- 输入URL -- 检测)

[![image-20240223102241624](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223102241624.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223102241624.png)

用友NC 漏洞利用(选择OA类型 -- 选择漏洞 -- 输入URL -- 输入命令 -- 执行)

[![image-20240223102353236](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223102353236.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223102353236.png)

用友NC 文件上传(选择OA类型 -- 选择漏洞 -- 输入URL -- 上传文件 -- 执行)

[![image-20240223102904034](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223102904034.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223102904034.png)

#### MemShell模块

```
    1. 支持冰蝎3.0、哥斯拉、蚁剑、suo5、cmdecho、neoReGeorg、自定义内存马
    2.  支持输出源码、Base64、hex、gzip格式payload
    3. 用友NC反序列化 集成接口反序列化（测试环境）
    4.  用友U8C反序列化 集接口反序列化（测试环境）
    5. 亿赛通XStream反序列化 集接口反序列化（测试环境）
    6.  用友NC内存马支持bypass脏数据传入，默认为100字节
```

[![image-20240223103147463](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223103147463.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223103147463.png)

##### 示例2：

(\*ActionHandlerSevlet及其他接口均使用CC6NC链注入）

用友NC冰蝎内存马

[![image-20240223105521102](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223105521102.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223105521102.png)

用友NC 哥斯拉内存马注入

[![image-20240223105914972](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223105914972.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223105914972.png)

用友NC cmdEcho内存马注入

[![image-20240223110035708](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223110035708.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223110035708.png)

用友NC 自定义内存马注入(使用蚁剑ClassByte字节码)，输入类名、Base64编码字节码、脏数据(可选)

[![image-20240223110851090](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223110851090.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223110851090.png)

其余功能均可实现，不做展示。

##### 示例3：

用友U8Cloud 冰蝎内存马注入（其余内存马均可实现注入）

[![image-20240223111206672](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223111206672.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223111206672.png)

用友U8Cloud cmdEcho内存马注入

[![image-20240223111318555](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223111318555.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223111318555.png)

##### 示例4：

冰蝎内存马payload 源码、base64 payload等生成展示(用友NC示例)

[![image-20240223104122068](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223104122068.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223104122068.png)

[![image-20240223104220406](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223104220406.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223104220406.png)

#### Sqlmap模块

​ 根据提示输入内容执行，集成调用sqlmap

[![image-20240223111623212](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223111623212.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223111623212.png)

##### 示例5：

泛微CheckServer-Sql注入，检测漏洞存在后，将payload字段下内容保存为req文件，使用sqlmap模块构造参数

[![image-20240223130450098](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223130450098.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223130450098.png)

[![image-20240223131531476](https://github.com/R4gd0ll/I-Wanna-Get-All/raw/main/images/image-20240223131531476.png)](https://github.com/R4gd0ll/I-Wanna-Get-All/blob/main/images/image-20240223131531476.png)

#### Crypt模块

```
    1. 各类OA加解密
    2.  各类编码解码
    3. Class类反编译、class字节码生成(base64格式、gzip-base64格式)
    4.  class反编译仅文件读取、base64格式(yv66)、gzip-base64格式(H4sI)可反编译
```

##### 示例6

用友NC数据库密码 加解密

[![image-20240223134600563](https://github.com/R4gd0ll/I-Wan...