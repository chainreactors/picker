---
title: 实战中的WebService利⽤⽅法
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496952&idx=1&sn=fdb338f5ff8cf421424cfcc5c01bfbb7&chksm=e8a5fe9bdfd2778d4c2584e6f5e6b3ce81120dca35669befee62af7d00ae7ada9b06c0dc02fe&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-27
fetch_date: 2025-10-06T20:09:13.915908
---

# 实战中的WebService利⽤⽅法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7Eosn2YvRIpfuuBbR4WIWic2xNCMGMhayoAI1picKmDAe1FHDibA5aSiawFicQQ6iazfcZqx5IxcFT000w/0?wx_fmt=jpeg)

# 实战中的WebService利⽤⽅法

迪哥讲事

编者荐语：

这种类型的站点往往存在的问题不少

以下文章来源于洪椒攻防实验室
，作者Reig

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6Ij8UBqaXuqBZiasK1vj7ocf4Vv3Dj4jeY2IjKUmATZHA/0)

**洪椒攻防实验室**
.

隶属于交通运输信息安全中心，专注于交通运输行业红蓝对抗、WEB安全渗透测试，定期分享原创漏洞挖掘、攻防实战文章。

```
声明：该公众号大部分文章来自作者日常学习笔记，未经授权，严禁转载，如需转载，联系洪椒攻防实验室公众号。请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。
```

## 0x00 前言

    接口相关的测试，http 协议的接口大家平常基础的很多，基本上问题不大。webservice 接口如何测试呢？

### 什么是web service?

    通俗来讲 soap 协议开发的接口对应的服务就是web service接口，通过 SOAP 在 Web上 提供的软件服务，使用 WSDL 文件进行说明，并通过 UDDI 进行注册。有以下几个特点

    基于Web的服务：

* 服务器端整出一些资源让客户端应用访问（获取数据）
* 一个跨语言、跨平台的规范（抽象）
* 多个跨平台、跨语言的应用间通信整合的方案（实际）

    http 协议开发的接口对应的服务，我们叫http service。

### SOAP 协议是什么？

> Webservice是基于 SOAP 协议传输数据，SOAP 又是一种简单的基于 XML 的协议，它使应用程序通过 HTTP 来交换信息。
>
> WSDL(Web Services Description Language)基于XML语言，用于描述Web Service及其函数、参数和返回值。它是WebService客户端和服务器端能理解的标准格式。
>
> 基于 XML 的，所以 WSDL 既是机器可阅读的，又是人可阅的，这将是一个很大的好处。——可以视为接口文档。

* wsdl示例：http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl

## 0x01 渗透测试中的WebService

    在渗透测试过程中，会通过扫目录或者是其他方式得到各种的WebService页面：

* IIS的webserver![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mzM5KHhjsccsNesEszRFT9YO2Au6AcK4dMfm6SmIpscgXUgkdvpt4hw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8miaUCegXyaicnLDrv6w6I6xiayA2ibGVmLUk1AiasSpHFcn6aHMGXtqIMfyQ/640?wx_fmt=png&from=appmsg)
* java的：![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mB5ctF0eYYohpcM5r2QLsFUib2dAaRH4Dq9RZbIgucMVg6m9MmrVzHtA/640?wx_fmt=png&from=appmsg)

## 0x02 怎么测试呢？

    许多文章都是写的使用postman、WSDigger、soapui等等，但我觉得这些都是给开发人员用的。

    作为一名渗透测试工程师、当然还是burpsuite使用的最顺手了。burp官方提供了一个测试工具：Wsdler，在burp的Bapp Store就可以直接安装

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m3eWvMsT6fxekcTO2GdOdDLE2w7icliaxJ9SOicqrXnOn8odzFxXfgmwKw/640?wx_fmt=png&from=appmsg)

    wsdl接口打开是这样的：http://xxxx.com/services/UserService?wsdl

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8muicibmwgUW9KUSkDTibdAoEAibBph3ahcibKHpH17p8EjY14iarN4ExVGypQ/640?wx_fmt=png&from=appmsg)

    在burp里找到请求消息，然后右键选择Extensions、选择Wsdler就可以了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m9XhzicbYs34mSQ3FogcktTv78ukS2MDOrx4s4g5MFbb47Fx9z6WhEjw/640?wx_fmt=png&from=appmsg)

    然后会在wsdler模块得到像下面这种：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mTJ9IPv2cIyS6C2lGymazMtNXcxTFRe4rCQibZ6iaticzcZMHodicqOvX4A/640?wx_fmt=png&from=appmsg)

    工具会自动生产xml格式的请求包，标注的地方是需要我们根据具体接口信息去构造的。

    个人很喜欢这种Web servers，因为里面的wsdl接口大多数会存在未授权漏洞（个人觉得，遇到十个有七八个存在未授权）。

    IIS的webserver大部分可以直接在页面进行调试的，比如：

http://xxxxxx:83/WebService.asmx?op=homemenu

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m5ib3dTPBWadsumh1TMpqNyWxvVECOiabibJHiaM3icmX0ahZVLNNzBL2fPg/640?wx_fmt=png&from=appmsg)

    输入admin即可获取数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mNGPnjOCZqTaU1zhq7Aic7new6myEGUVjkYAvwpmHdzvThkyL6MZ1aBw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8miarfFzXb0L4MNR1DXKRBia2VibV4HDlqCibpia9BJ1yic01YsouOprzykCag/640?wx_fmt=png&from=appmsg)

    页面直接调试就基本上看到的是正常的post请求，但如果页面没有调试的webserver该怎么测试呢？

    从页面看到的请求是http://xxxxx.com:83/WebService.asmx

    这种其实是支持SOAP协议的，直接将请求变为WebService.asmx?wsdl即可![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mTujvQZwIbVjFhNib3ugmf6bXZX05TSdrJgicdSnZLvOlQRsyIgSZcMOQ/640?wx_fmt=png&from=appmsg)    然后再利用burp工具wsdler自动生成xm格式请求、一样的可以获取数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m5NGTZDT8t01Sj4KaG2ibaadaDUwwm5RKCMjtKhBOtbia8LpesdfJ4jicQ/640?wx_fmt=png&from=appmsg)

    除了正常获取数据，还可以测试SQL注入、XXE等，根据web service有什么接口进行具体测试![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m38Hyn6hpEH9I6uqNXx2PSv6PQuUmgbK8w3C8ibnYok3pOVejrOT0cmA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mPibAtwuF6dJfBvklfFSGbrMAMMkUqkB4E3Yeq2xrfTBic8icv28zkD9Bg/640?wx_fmt=png&from=appmsg)

    sqlmap一把梭即可，运气好有文件上传时，直接构造上传getshell。

## 0x03 案例1

    这是一次某次hw中的实战案例，目标存在一个iis的web server页面![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mHspU9uby5qBiceqLGHgXsiaLQBvE2M5JQuU4XBqt8HicdibnuhEq8I2nHw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m2mQAIibmsYxHiaHmNCqpTCHWufZVd9jiafH5KHb3iafEia6zUfekg9ZkoPA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m9q2iaCicx6Cvm3ibY9qGa18nVJtcGHRcjtRfejJ0R6IZqwdia3p3PXrWdA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mll6nXiaUDvFHgOXHEOkibf2BstlPCiaMMOspKmg5KAZ0QOUgic6QpsCiaQA/640?wx_fmt=png&from=appmsg)    还可以对物联网设备进行控制：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mG9Wl9QFGCezCycdzXaibCZskgkayO1uicibaHI1AX2onQt8Q7mQnica4zA/640?wx_fmt=png&from=appmsg)

    然后某个接口存在SQL注入，直接os-shell获取权限，powershell上线进入内网，打穿出局

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mUiaBdPb4TicXzDUw4A4q0RL8fT91tw0m7fkROaDrAHiburex6QIvVQBrA/640?wx_fmt=png&from=appmsg)

## 0x04 案例2

    某次渗透测试中，目标单位OA系统存在Web server，发现存在一个用户接口queryUsers

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mFrMP25Dtk3IGLO2vNBgIfxhicyuqdT1waGMcrLAar723ryOibPsv4dQw/640?wx_fmt=png&from=appmsg)

    wsdler工具自动生成xml格式，需要自行构造参数，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8m421emGGicqic3BcBGj4DJnNca7FFQRPSKKR5qvCFhb2Q4M9pLCX1pXrg/640?wx_fmt=png&from=appmsg)

    参数有userid、userName、orgSysCode，优先尝试userid=1，username=admin，其他不知道的参数可以留空，发包测试、可以看到并没有返回数据，可能构造的不对，各位师傅遇到了自行尝试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mah8U99ybw6y2mXeGDxaJfE8kmXGdRpojubUYeiabALEPvdN2PySUzqw/640?wx_fmt=png&from=appmsg)

    笔者个人习惯(也算是一点小经验吧)，在遇到这种涉及page、size参数的，我索性直接将其他参数删掉，只保留page、size参数，往往会出东西：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mWl2d35lGmUSicTmXf2tA3Jz79jFV45lj9eyCTibg3W5mq0CXCAh5rOuA/640?wx_fmt=png&from=appmsg)

    直接获取所有的用户信息，再利用id查询密码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mML7YpgZ7r6NMPmlTuia0HibzodoSb3Y4GMXQPOFQSwHPxuAlbco6RRQA/640?wx_fmt=png&from=appmsg)

    直接获取OA系统所有的账号密码，md5解密即可登陆系统获取大量敏感信息。

## 0x05 案例3

    某次SRC项目挖掘中遇到一个asp.net的站点，不存在目录遍历漏洞，但是是怎么发现存在WebService的呢？

    搜索接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mzaIML1UA6xsTr4dgbMTriaKyJlX7owxgP0iaiaXkdxttuezZIgHCOQNVQ/640?wx_fmt=png&from=appmsg)

    发现接口是/Services/xxxx.asmx，直接访问显示拒绝访问：![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mO28licicLqIQEDUGov7gNic1YAcMGEib4EJPd3kM4uQCele3WpDgxrf8kA/640?wx_fmt=png&from=appmsg)

    但是在xxxx.asmx后面加上?wsdl，即可获取到所有接口：![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mDf1kXH8QRxSdrc5ynGYCH4iay68wsyB0ANf3SOFR6UIF0HiaXYcnQucg/640?wx_fmt=png&from=appmsg)

    再利用burpsuite自带工具wsdler生成数据包，直接获取敏感信息。![](https://mmbiz.qpic.cn/sz_mmbiz_png/LxQLSKM9eAKsKoiaY7IMRE1lQb1ATeA8mvW9MSsucQQmfQT5DQO3vnAKzDICxLjRtGDQ6rUdgHicibAZlQaYBvkHw/640?wx_fmt=png&from=appmsg)

## 0x06 总结

    WebService测试还是比较简单的，主要就是根据有哪些接口、然后再针对的进行测试。而且大多数存在未授权和SQL注入，个人还是很喜欢遇到WebService的（特别是IIS，很容易有注入）。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIz...