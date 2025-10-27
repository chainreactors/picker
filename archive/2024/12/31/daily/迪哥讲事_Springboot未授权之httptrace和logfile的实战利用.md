---
title: Springboot未授权之httptrace和logfile的实战利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496709&idx=1&sn=4459d412d70bafeeb2be8cead320a6a7&chksm=e8a5fe66dfd277702857ee0d63015aa040414468dd230e61c282b7b1d4a1b98f373acb856cf1&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-31
fetch_date: 2025-10-06T19:42:13.569315
---

# Springboot未授权之httptrace和logfile的实战利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7EMnuhicegYpVhJImPCfNJc2utnMF4majw8alBiaq617pM0BuicXfA0Gz5vEI8iayXgibcsyJmo4FMJsg/0?wx_fmt=jpeg)

# Springboot未授权之httptrace和logfile的实战利用

迪哥讲事

以下文章来源于洪椒攻防实验室
，作者Reig

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Ij8UBqaXuqBZiasK1vj7ocf4Vv3Dj4jeY2IjKUmATZHA/0)

**洪椒攻防实验室**
.

隶属于交通运输信息安全中心，专注于交通运输行业红蓝对抗、WEB安全渗透测试，定期分享原创漏洞挖掘、攻防实战文章。

```
S声明：该公众号大部分文章来自作者日常学习笔记，未经授权，严禁转载，如需转载，联系洪椒攻防实验室公众号。请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。
```

## 0x00 前言

      相信大家在很多项目中，不论是渗透测试还是攻防演练中都遇到过很多springboot的actuator未授权，但是大家基本上都主要是关注env、heapdump，还有容易造成命令执行的、gateway、hystrix.stream、jolokia等等，但是最近发现有的人很容易忽略httptrace和logfile接口。

## 0x00 httptrace

       httptrace可以记录每一个HTTP请求的信息，包括请求路径、请求参数、响应状态、返回参数、请求耗时等信息。一般会随着`SpringBoot Actuator`未授权同时出现。![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialllXuH3VW0hdfazJssN9pcdS2fC0XMnPqxZrREM6krMahKolJUyM8LA/640?wx_fmt=png&from=appmsg)       这个漏洞虽然不能直接RCE或者是拿到密码，但是我们可以获取cookie信息和接口地址，直接拼接接口和cookie就能获取后台数据。话不多说，直接上案例。

## 0x01 案例1

       测试某系统发现一个springboot未授权。`/env`里面还有一些redis、nacos的连接信息，但都是内网，外网没有开端口，用拿到的密码去撞了下admin账号的密码也没成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialIjlk29icQakQz8rzEjbkyvY2S8LBNicxicavXMdn6gaOPG6zZRPWcFAFQ/640?wx_fmt=png&from=appmsg)

`/actuator/mappings`下还有很多接口，很幸运的发现了大部分接口可以未授权：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialNia3TXIibjkPJOjHpRpddujpsqpBYmVQT9prRAQC3eePj8tDDUHfnhkw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialubicJkZGhEIAEXeTSwELOLfUbibqSE2nq5aXuerfznibUfOVX0uFXrVvA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialOdKFEvZ4NEDRUlAvPK8rqDq7K6VtSbxmVx3WkdSTAwDVmmKWej96zA/640?wx_fmt=png&from=appmsg)

       找了一个小时，就是没有发现能查询到用户密码的接口，只能查询到账号信息，很多接口都是参数未知的，查询不到东西，只能想办法拿到管理员账号。账号添加接口跟密码重置接口需要太多参数，构造不出来，又陷入了僵局。

       你们以为到这我就会放弃了吗？就会放弃了吗？？？不可能，绝对不可能！！！！既然没有账号，无法注册 但是可以使用某政务服务平台账号登陆(全国包括每个省市都有)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialCfjZgK1qsMvpV4bPSnJwHhaPeZ9AGx5oOdtnhwR0E7AiacCro3yYWibA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14Jxcial05mqTegwLUDdLra6R3MKS4soxWjEiaS8cWo9ic0ExuUlDjESt0OF5qNg/640?wx_fmt=png&from=appmsg)

       进入系统后发现加载了这么几个接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialfpqFJYaR4YK9HEDc9uPnC2Qd1wG9f2wqrzsJcxtmC5dicnEU7NKeTQg/640?wx_fmt=png&from=appmsg)

       getuser? 这不是一个活脱脱的越权吗？（接口本身就是未授权的）
直接查看id为2的管理员信息，没有什么有用的信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialRXD12lUGdMJDxM6GsWiamXIHoib2GLyczl9jShLib0iaIfbxfTHhsVWTxg/640?wx_fmt=png&from=appmsg)

       加载自己的信息，能看到自己的密码，但是无法解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialARZNENvI36JLE8AqHkwqwAOw9kfq7UJxzV2BGgNacb2x8syCI4ic7ag/640?wx_fmt=png&from=appmsg)

        尝试进行重置密码，看是否有漏洞，结果是无法自定义重置密码？？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialQ5AOy0gnhtAicaib4XjAywVeP2hdnQMJVr9pmfNRoLRyQ3tDbWEGuK0Q/640?wx_fmt=png&from=appmsg)

      咦？我刚刚是不是设置过密码？试想一下 能不能也给别人设置密码呢？往上翻burp历史，找到了自己设置密码的接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialGjWCqlJuON3BNlo9UaCtLzvs5RLiaItZgJZ4wEyibmcickIiamiaqLakg5A/640?wx_fmt=png&from=appmsg)

      能看到直接是设置自己密码，只需要有Access\_token即可。那么我们怎么拿到Access\_token呢？嘿嘿嘿，师傅们不要忘了，spingboot还有个接口，能看到所有的http请求信息，包括session、cookie等信息，那就是`/trace`，这个系统是`/httptrace`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialSqic2AGPdcC2v9zdfrIRerGbUL9KUDOBaAHE4CKL9phiaVkgJaAJeeUw/640?wx_fmt=png&from=appmsg)

       能看到刚刚自己的token信息，那我们是不是也能拿到别人或者管理员的token呢？往下翻就看到了别人的token，看一下信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialQnEMibEMd574kNK340tHrLcPHYYWicXysH6pPdULwpvLdFKdChhVf4uA/640?wx_fmt=png&from=appmsg)

      重置密码，登录系统：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialLkbdRcryTp1gdztB8gkqSCrdjl2N4iaibKbOHznnNXXPX97KzP3CYkEw/640?wx_fmt=png&from=appmsg)

权限不够高，如果管理员上线了，我们就肯定能通过`/httptrace`接口拿到他的token进行密码重置
         PS：这里特意测试了一下，账号退出后的token仍然有好几个小时的有效期。

       但是`/httptrace`接口是有限制的，如果业务量大，存的访问请求可能只有几分钟，如果业务量不大
可以存半天甚至好几天，特意用未授权的log日志接口查看了管理员的上线频率，蛮高的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14Jxcialial3KfTYQMcH5am9XQDlNVa2qCLPzQ8L7TRHPjkmsVyMaak7bpnvCibw/640?wx_fmt=png&from=appmsg)

        所以接下来的操作写个定时任务去请求/httptrace接口等待管理员上线，获取token，重置密码！

## 0x02 案例2

      最近的红队评估项目中遇到了某单位的一个nacos，存在CVE-2021-29441 Nacos权限认证绕过漏洞，当开启 Nacos 权限认证（nacos.core.auth.enabled=true）后，配置文件中存在默认值：

```
nacos.core.auth.server.identity.key=serverIdentity
nacos.core.auth.server.identity.value=security
```

     该硬编码导致攻击者可以构造携带该 key 和 value 的请求，从而绕过权限认证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialWjx5HN2vVJZmFdbpPeYh5KQgYXK0KMicaUV0h1rNJjgfHM0CA1Xw31g/640?wx_fmt=png&from=appmsg)

     直接添加账户，但是该账户是没有权限，看不到任何配置的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14Jxcialeoj13Ucvw2mkAPFtSCYNJW3O0nvBibCblvchqr3JcgzKxicbALvIxdxA/640?wx_fmt=png&from=appmsg)      这时候就想到了，默认配置下的nacos，除了存在认证绕过漏洞，还存在spring的Actuator未授权漏洞，如果存在env接口，大概率是能够从heapdump里得到nacos的jwt密钥的，然后进行构造正确的token。还有一个接口就是`/httptrace`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialX1HypKsleo6IibRGL0n7icZrEPzRml3H6yhYL5PVRSPCib7fbQRtPwGpw/640?wx_fmt=png&from=appmsg)

     跟上面一样的，通过获取token信息，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialTrRYp2sJAcqX1ssPVzsxz1icYUsSCy9CNibsf1870ASVXUmTgrLh53QQ/640?wx_fmt=png&from=appmsg)

      然后替换accessToken登录系统：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14Jxcialrvayz5ERYw7hPARd6RwzszJFbkFMmVLt3iaRL8iaFt0LZAiadkaClX8ibQ/640?wx_fmt=png&from=appmsg)

## 0x03 logfile

      Actuator未授权中的`/logfile`也是比较容易被忽略的接口，它记录了所有请求的日志。![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialmUVBrWfz3qS569dJcUOXosJ1NP32ywNMarDKFdRUIzjh69oWrXSiabg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKvFooRrSWBQDQHF14JxcialZuHwo5bSP1rbu43HDwASM3gaUrXt1te6g6fZ7VPoapnqYFOuQx9SyQ/640?wx_fmt=png&from=appmsg)

很多时候可以从logfile里面找到泄露的账号密码信息。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0...