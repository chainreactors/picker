---
title: SQL注入
url: https://www.freebuf.com/articles/web/421981.html
source: FreeBuf网络安全行业门户
date: 2025-02-18
fetch_date: 2025-10-06T20:39:24.197035
---

# SQL注入

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

SQL注入

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

SQL注入

2025-07-26 10:57:01

所属地 北京

**SQL注入（SQL Injection）是一种常见的Web安全漏洞，形成的主要原因是web应用程序在接收相关数据参数时未做好过滤，将其直接带入到数据库中查询，导致攻击者可以拼接执行构造的SQL语句。那什么是SQL了？结构化查询语言（Structured Query Language，缩写：SQL），是一种关系型数据库查询的标准编程语言，用于存取数据以及查询、更新、删除和管理关系型数据库（即SQL是一种数据库查询语言）**

## union注入

![1739771792_67b2cf9049cdc90375acc.png!small?1739771793083](https://image.3001.net/images/20250217/1739771792_67b2cf9049cdc90375acc.png!small?1739771793083)

![1739771813_67b2cfa50bd7c4fba3c0f.png!small?1739771814248](https://image.3001.net/images/20250217/1739771813_67b2cfa50bd7c4fba3c0f.png!small?1739771814248)

![1739771844_67b2cfc4ae4806aa63d68.png!small?1739771845127](https://image.3001.net/images/20250217/1739771844_67b2cfc4ae4806aa63d68.png!small?1739771845127)

![1739771901_67b2cffd7e4e1e106a4b9.png!small?1739771902313](https://image.3001.net/images/20250217/1739771901_67b2cffd7e4e1e106a4b9.png!small?1739771902313)

![1739771928_67b2d0182eda98758908e.png!small?1739771928925](https://image.3001.net/images/20250217/1739771928_67b2d0182eda98758908e.png!small?1739771928925)

![1739771886_67b2cfeeb75d97baa8221.png!small?1739771887879](https://image.3001.net/images/20250217/1739771886_67b2cfeeb75d97baa8221.png!small?1739771887879)

![1739771949_67b2d02dd9f2acdd769c8.png!small?1739771950635](https://image.3001.net/images/20250217/1739771949_67b2d02dd9f2acdd769c8.png!small?1739771950635)

**总结：**

![1739771996_67b2d05c38ea5d56ed50c.png!small?1739771996771](https://image.3001.net/images/20250217/1739771996_67b2d05c38ea5d56ed50c.png!small?1739771996771)

## **报错注入：**

![1739772023_67b2d0775ff15186ce806.png!small?1739772024549](https://image.3001.net/images/20250217/1739772023_67b2d0775ff15186ce806.png!small?1739772024549)

![1739772033_67b2d0814146bf8ce4a16.png!small?1739772035780](https://image.3001.net/images/20250217/1739772033_67b2d0814146bf8ce4a16.png!small?1739772035780)

### **extractValue() 报错注入**

![1739772060_67b2d09c1d3c85684922b.png!small?1739772061681](https://image.3001.net/images/20250217/1739772060_67b2d09c1d3c85684922b.png!small?1739772061681)

![1739772078_67b2d0ae0765fd75d3741.png!small?1739772079169](https://image.3001.net/images/20250217/1739772078_67b2d0ae0765fd75d3741.png!small?1739772079169)

![1739772091_67b2d0bb5626838d1a067.png!small?1739772092271](https://image.3001.net/images/20250217/1739772091_67b2d0bb5626838d1a067.png!small?1739772092271)

![1739772112_67b2d0d052b8c93357407.png!small?1739772112860](https://image.3001.net/images/20250217/1739772112_67b2d0d052b8c93357407.png!small?1739772112860)

concat用法concat（1,2）输出为12，将第一个和第二个连接起来为了让路径报错

![1739772132_67b2d0e421cb49b19f461.png!small?1739772133097](https://image.3001.net/images/20250217/1739772132_67b2d0e421cb49b19f461.png!small?1739772133097)

![1739772151_67b2d0f73c7dd08079d67.png!small?1739772152162](https://image.3001.net/images/20250217/1739772151_67b2d0f73c7dd08079d67.png!small?1739772152162)

### updatexml报错注入

![1739772240_67b2d150611bbd6006a6b.png!small?1739772241516](https://image.3001.net/images/20250217/1739772240_67b2d150611bbd6006a6b.png!small?1739772241516)

![1739772254_67b2d15e10bede6339114.png!small?1739772254666](https://image.3001.net/images/20250217/1739772254_67b2d15e10bede6339114.png!small?1739772254666)

![1739772264_67b2d1685ed583057be63.png!small?1739772264893](https://image.3001.net/images/20250217/1739772264_67b2d1685ed583057be63.png!small?1739772264893)

![1739772275_67b2d173254e25892b179.png!small?1739772275842](https://image.3001.net/images/20250217/1739772275_67b2d173254e25892b179.png!small?1739772275842)

### floor报错

| 函数 | 作用 |
| --- | --- |
| rand（） | 随机返回0~1之间的小数 |
| floor（） | 小数向下取整数 |
| ceiling（） | 小数向上取整数 |
| concat\_ws（） | 将括号内数据用第一个字段连接起来 |
| as | 别名 |
| group by | 分组 |
| count（） | 汇总统计数量 |
| limit | 这里用于显示指定行数 |

![1739772354_67b2d1c2093db2a0ab7b9.png!small?1739772355800](https://image.3001.net/images/20250217/1739772354_67b2d1c2093db2a0ab7b9.png!small?1739772355800)

![1739772365_67b2d1cd993e23b5ab438.png!small?1739772366872](https://image.3001.net/images/20250217/1739772365_67b2d1cd993e23b5ab438.png!small?1739772366872)

![1739772375_67b2d1d70bb2d5dcbab6f.png!small?1739772376135](https://image.3001.net/images/20250217/1739772375_67b2d1d70bb2d5dcbab6f.png!small?1739772376135)

![1739772388_67b2d1e492fe886d1a404.png!small?1739772389231](https://image.3001.net/images/20250217/1739772388_67b2d1e492fe886d1a404.png!small?1739772389231)

![1739772401_67b2d1f1950fb5773471c.png!small?1739772403030](https://image.3001.net/images/20250217/1739772401_67b2d1f1950fb5773471c.png!small?1739772403030)

## 布尔盲注

盲注：页面没有报错[回显](https://so.csdn.net/so/search?q=%E5%9B%9E%E6%98%BE&spm=1001.2101.3001.7020)，不知道数据库具体返回值的情况，对数据库中的内容进行猜解，实行sql注入

布尔盲注：web页面只返回True、False两种类型；利用页面返回不同，逐个猜解数据

![1739772434_67b2d212342e02afca5e9.png!small?1739772434783](https://image.3001.net/images/20250217/1739772434_67b2d212342e02afca5e9.png!small?1739772434783)

有真假两种类型的页面

| ascii（） | 转换为对应的ASCII码值 |
| --- | --- |

![1739772455_67b2d2279edf6aa2c373b.png!small?1739772456168](https://image.3001.net/images/20250217/1739772455_67b2d2279edf6aa2c373b.png!small?1739772456168)

![1739772466_67b2d2322c0e83e3f4eb8.png!small?1739772467205](https://image.3001.net/images/20250217/1739772466_67b2d2322c0e83e3f4eb8.png!small?1739772467205)

subdtr（查询语句，第几个字符，显示几个）

![1739772486_67b2d2466cd96d3fb0f64.png!small?1739772488276](https://image.3001.net/images/20250217/1739772486_67b2d2466cd96d3fb0f64.png!small?1739772488276)

?id=1' and ascii(substr('语句',1,1))>97 --+

**ASCII表**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ASCII值** | **控制字符** | **ASCII值** | **控制字符** | **ASCII值** | **控制字符** | **ASCII值** | **控制字符** |
| 0 | NUL | 32 | (space) | 64 | @ | 96 | 、 |
| 1 | SOH | 33 | ！ | 65 | A | 97 | a |
| 2 | STX | 34 | ” | 66 | B | 98 | b |
| 3 | ETX | 35 | # | 67 | C | 99 | c |
| 4 | EOT | 36 | $ | 68 | D | 100 | d |
| 5 | ENQ | 37 | % | 69 | E | 101 | e |
| 6 | ACK | 38 | & | 70 | F | 102 | f |
| 7 | BEL | 39 | ' | 71 | G | 103 | g |
| 8 | BS | 40 | ( | 72 | H | 104 | h |
| 9 | HT | 41 | ) | 73 | I | 105 | i |
| 10 | LF | 42 | \* | 74 | J | 106 | j |
| 11 | VT | 43 | + | 75 | K | 107 | k |
| 12 | FF | 44 | , | 76 | L | 108 | l |
| 13 | CR | 45 | - | 77 | M | 109 | m |
| 14 | SO | 46 | . | 78 | N | 110 | n |
| 15 | SI | 47 | / | 79 | O | 111 | o |
| 16 | DLE | 48 | 0 | 80 | P | 112 | p |
| 17 | DCI | 49 | 1 | 81 | Q | 113 | q |
| 18 | DC2 | 50 | 2 | 82 | R | 114 | r |
| 19 | DC3 | 51 | 3 | 83 | X | 115 | s |
| 20 | DC4 | 52 | 4 | 84 | T | 116 | t |
| 21 | NAK | 53 | 5 | 85 | U | 117 | u |
| 22 | SYN | 54 | 6 | 86 | V | 118 | v |
| 23 | TB | 55 | 7 | 87 | W | 119 | w |
| 24 | CAN | 56 | 8 | 88 | X | 120 | x |
| 25 | EM | 57 | 9 | 89 | Y | 121 | y |
| 26 | SUB | 58 | : | 90 | Z | 122 | z |
| 27 | ESC | 59 | ; | 91 | [ | 123 | { |
| 28 | FS | 60 | < | 92 | \ | 124 | | |
| 29 | GS | 61 | = | 93 | ] | 125 | } |
| 30 | RS | 62 | > | 94 | ^ | 126 | ~ |
| 31 | US | 63 | ? | 95 | — | 127 | DEL |

![1739772600_67b2d2b8238f6fcd0746d.png!small?1739772600933](https://image.3001.net/images/20250217/1739772600_67b2d2b8238f6fcd0746d.png!small?1739772600933)

布尔盲注闭合符...