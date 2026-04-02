---
title: 利用邮箱漏洞寻找突破口打穿目标内网
url: https://mp.weixin.qq.com/s/K2W-Hfk90VakfG5gMwM5Aw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:27:08.354132
---

# 利用邮箱漏洞寻找突破口打穿目标内网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ianpxKPnLHoJKpVnahZCPMfyXuT2icLEG84YqPHHiawo1vibmhLrarM5P9j6OtK8DjS9eTjpicezZkU8D4NrW3q4w7a0NP9lSMavJibk0dsdk266M/0?wx_fmt=jpeg)

# 利用邮箱漏洞寻找突破口打穿目标内网

zkaq-flysheep
zkaq-flysheep

掌控安全EDU

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - flysheep 投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  **）****

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。

## 前言

今天，我要和大家分享一次有趣的省级HVV实战经验--某某航空公司。这次经历是我从打点到成功获取内网机器权限的完整过程，绝对让人耳目一新！如果我们不考虑近源攻击和钓鱼攻击等常见手段，那么这次的分享相较于传统漏洞攻击穿越边界的方法，充满了挑战和惊喜。

为了保护演习的机密性，里面的截图会经过一定的打码处理，敬请谅解。让我们一起开始此次渗透测试之旅吧！

## 邮箱账号密码遍历漏洞

通过演习组给定的目标域名，我利用网络空间测绘平台找到一些目标资产，其中一个邮件系统引起了我的注意。通过指纹分析为exchang服务器，之所以考虑对其进行测试，主要是登录界面没有验证码机制而且没有进行限速。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJP12Q4jCJPuk2zfoESJA2Bcv0Odpo8iblub79iaGWrEpb3MunLLNerqO2mgvssibkLFjdxu3ibFMrge8AjfYw4iaW5FnnlGaN0Rt6o/640?wx_fmt=png&from=appmsg)

通过常见用户名字典对exchang的枚举和爆破，最终成功获得2个账号/密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJ4z0vHMTfibRW7icCjNupOWdzWmahcO0hpOJ9CGw5eWCT4Qsb31rubzbMV3OUVUyO85ar9aBvCicms0SIaBvv64ITX7QQIyibmFeY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIvh3NkWQx1mSZGjJPpOFPxqNIaLP09xsicJJdpZf2TFlWdtRwKcg8ibb8xInTA3JMibpUZ5ZqZ4CCGLqEGPxacgxNHEc4RpQObGM/640?wx_fmt=png&from=appmsg)

两个用户分别具有不同的权限，不断翻找邮件内容看看有没有可以利用的东东

用户zhangyn

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLfYv7bak2EbTuW9dXlTia9fYLL91Z1S2iaADqUYlV3mO6svecJCncRxA2LCGaD4KSNpfbOr1iaH9T0GYBOnHxQERMicMsiaIibzQ0WE/640?wx_fmt=png&from=appmsg)

用户chenjun

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKhP5HSqDe6rKdKHcuUjeeSFrhYPlYSADJsic1C8dFu6NHj4jDQCddCOn76ejdvyQuSiaiaPLuzDI0thsdDORp8H62eo5P3vwnUIY/640?wx_fmt=png&from=appmsg)

## 利用VPN突破逻辑隔离进入内网

通过多次尝试发现使用账号zhangyn可以成功登录公司放置于DMZ区域的webvpn

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIq2Q2ic6UFDPg5VQfBeW83KVLyHRAF3u4Zt3TicOfywY0eYsTBwWDQyhhhP2yrxFicJRib0zL7ftc7gNJsBRp9DlyZqkgHFptrZds/640?wx_fmt=png&from=appmsg)

这样就通过VPN突破逻辑隔离顺利进入内网了

点击页面上的链接还可以成功访问内网的OA办公系统

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKGYSmEqXh373TrgvfrfAQ5DmGRZBAlaGicLyESmcAmvGYWP0pvwr6BiaEpg2Djj3oxWdAYbfob22GZWHl9XR6yo6r4fACeRibibpg/640?wx_fmt=png&from=appmsg)

点击webvpn的链接还可以进入公司单点登录sso，10段机器，里面有挺多的功能，舒服啊。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoI8CrHnLCvK9o6IrZnpDMy62Ls2l4xOztRKJLI2hlMTYOtzdK9vIWrvdzD8W8EFBYecTWuHZs2m7iak48feozcIoYsibvGK0PrSk/640?wx_fmt=png&from=appmsg)

## 核心业务网段渗透

挂上SSLVPN也同样能进入内网。继续在zhangyn的vpn中ping主站的域名，发现主站所在的内网网段是10.2.3.X网段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKFOoOrYQK780GEPWjlkhMuRtWwdxrQjQ6DzbiburIY2q8t7hXFJAFMlCI341wQmCUkhAudqIyr5TPZ86SYegGfqh4p5WB6V8Gc/640?wx_fmt=png&from=appmsg)

于是利用FSCAN扫描探测，但是奇怪的是发现该账号仅能访问4个主机地址，毕竟一个公司的内网是很大的，哪怕仅仅是办公内网也不可能仅仅只有4台机器。

通过询问组里有经![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKlztt5RvQLjtZnZCnMtNcuKATknwlGicpQEiaSKlJPl6lWPibHZEz0rNhUzBIuXTBcB3Zu8UA3HqEeoTejNbj9KCIaAwNiaNZXFy0/640?wx_fmt=png&from=appmsg)验的大佬，最终我们分析该账号是乘务组人员，it权限不高，所以能够访问的内网资源极其有限。

于是我又再次切换到之前的chenjun账号，这次发现可以访问更多10.2.3.X段的主机资源了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKYsYDrAXM6ysLsRQZM3WBxpdic6Lxpvw896T3IRVfhGG94FEiaK4tKB6sLJkubXhlLQMYc1TpoLrkGxIPDqq1hWiczEEVv1Orshw/640?wx_fmt=png&from=appmsg)

在这些扫描到的内网资源中，我首先通过常见的weblogic 反序列化漏洞获取1台主机root权限

运行控制系统

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKrtpfCf9RGnNQLeJsLPMJlicqILqRFYqX1gstPbMj7ezyWx0T2zPxCaRG4NfQHkaTrUGyU1j4AS4uam9hfaHROiaFacr40WPDWQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJt9ZaRJ35pdoQna4oUVDuBFyucTd2UxLeUT0ktyfMicSrNoE9CNVeUShzfdGiaicDyFRsiaaicwVZ1BnqaZkIccecnHMbKgCaIsl2w/640?wx_fmt=png&from=appmsg)

### 获取域控服务器权限

通过前期进入核心内网后扫描发现域控地址

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoI0PJXw8C4JXibfghGIAQ6vPfITQcx0grLgX1C8lDarLkjicSFJQjMIZ2XqPbNmkA3JXgvy8NeCKVHUSmaib3CczyzsibzNnS7BXPI/640?wx_fmt=png&from=appmsg)

可以通过nopac域漏洞获得域控权限

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJGkkbhpeLU548iburuMy1d6b53u5sBSWhQicDZhsRiaMHGM8LbuwNDcNvtHaJDKwfZwyyrrqFq41riaFeViccHfAAicwblETxlXoTCs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIWgg91qg52nlY67jedCYkDTE6fwMjz2tAP3g94529Ef9z5iaekLdyzjxQbCPiagskOavKckhUP2R4NGNeuQ8ibLbKhztVyb8jZJE/640?wx_fmt=png&from=appmsg)

添加域管账号后成功登录域控远程桌面

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoK1jCA12d4ElLykp7NoklaicXS7O9hhBxs1diaVfweH6W5SZN9tLTTBLaiaDaviaqGcr3IRBqDNK43PLwptXic16ZSiboYxyXx2chXn0/640?wx_fmt=png&from=appmsg)

### 通过资产列表锁定核心业务系统

通过域内用户查询查到运维部张XX的hash，解开获得明文，登录其邮箱

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJSWybBGibduFtI8976TLOzDskvpA9yzP8fAm5gNhRAWBiawcn5KL16yVBQLT1uuTGibhXo37NU7ic0e6yJF9wyrLc29b0Ss69bAIg/640?wx_fmt=png&from=appmsg)

获取信息资产列表，其中标注了重要系统。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIMKicmgqU9niafKLnu2m0aFx9ZpVIPt9CE5IJwfKfLB1JwsZr7rZfmzicUFacXEwn63VPh0G6Ej9Oj3BKVMFmLCmLXtkNQa2DnYk/640?wx_fmt=png&from=appmsg)

在域控中可以看到对应的重要服务器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJJMr4mZZibBJMozRXXDniaOQsnmxU1j0SWxIM6PbpfoB958xxueQcKlfVVCNW4hYaZRp0TrQ5rC9NANbfrqicWKL6p1grMbGdbVY/640?wx_fmt=png&from=appmsg)由于当前已有域管账号，因此可登录任意重要服务器，危害非常大。

演示登录WQAR系统10.2.3.X，wqar是无线地面快速存取记录器，为飞机维护和可靠性提供大量基础数据，重要性不言而喻，一旦被不法分子利用，会对旅客生命财产和社会安全造成严重的安全威胁。

### ![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKZx3kPicNyyxwzX357FJ4EcNjNd4LnJR59dqh9bfo9QkXZkg2wN0GRIKBzwzKc1oM7StULTGTxNDOzB2TibbTNW2ugOJb5T0CP4/640?wx_fmt=png&from=appmsg)

### 继续邮箱爆破获得更多弱口令账号

感觉有些敏感信息在邮箱里面传递，于是继续利用内网搜集到的各种信息形成新的用户字典，继续对邮箱爆破获得更多弱口令账号，下面是成功的6个

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLD3nat7mUvFxr6349OXViclMzSTGVP9EGYewicCvpYJ0N9pibb9MQ2J5T7UTpT3dtoHlibT4FQwpvtwo7iaiasV9hPicysw0lc2Cqdp4/640?wx_fmt=png&from=appmsg)

通过上面爆破获取的用户信息进入了若干办公后台

安全管理平台：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoICM2oyJOF4pxwmsibBMwDX2d8fRmC0rQ8MQQN4NoWxebSicUtcjbGqVCicDHXXNLwzl257x6jrGEKaXVlGqvoYShCNlvEoOPickco/640?wx_fmt=png&from=appmsg)

机组信息管理系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIN3hzR6jyn80x9SCj8l1EzSGVSdpAun0uXlZp8icd3S0Vjy9CKpls4iaFPIb3TjJOjuMLaIzBu228xt3jORzKxdoZurOf7DpssI/640?wx_fmt=png&from=appmsg)

危险品培训管理系统

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoINuNXCYBKf9QJTVxYA2wwAc34XSqKRPrkNC8cZDsJ7H1Vxe0iaLDxo6Ah9z87f5HahzzYCThTfBNN7KF0diaJvYq4S8y185061o/640?wx_fmt=png&from=appmsg)

XX控制运行网

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIpbvNIe8OEcpI8egmNleUBMUgcAAqCDyrwWT3WicTMXwO087YsfIR37UQAVV7jJGRUkEM84X5vOH4ReWzicU5k3QbEEo3NBfvTo/640?wx_fmt=png&from=appmsg)

磐石应用服务器

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJ5fmaUkibfibvrF84UKLk3unBziboL3OemU1IJBRv2RxWntbteHSLicp3rMDPhAALZjGBibXdOibZ5KIicOKSmXvictjkwVbthjicdoRDQ/640?wx_fmt=png&from=appmsg)

磐石媒体网关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLYmLeouQwXibZTc2KK0ZRAzHOxTFe7HriaeVdXKsk8OBnFQKSHKbuoWJggwXkSbo715Z4xcdPeCZYZNBtkyI6NbkKicnd2UtO0ibw/640?wx_fmt=png&from=appmsg)

### 通过弱口令爆破获得主机权限2台

[+] SSH:10.2.7.42:22:admin

[+] SSH:10.2.7.41:22:admin

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoK9zabicuU7djUCAm1ltl2VAny9GERdI5sINFUc7mQqibT0a0NBYkZqWWD0oqrvUYO5bYNUhFdq1ibh6siarlX03OsJVRGes3yzDg8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJO5DzG35Bnga8hbUs8ibBVaibLudv6M0B7kS2icT9AIiaibouUs0HH04nZmB1K8T3YhtnhDGdoic8GwTrzsgTBagEia7o2icVu49ruNpQ/640?wx_fmt=png&from=appmsg)

active mq后台管理员权限

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLUJZFAyHv6BuxXxw7eiaialBDuA0q8OVQcGQ52w1uduuCPp7loZ9gkHWhqByhAN7kbSCkgNJfPuC5N6vWRabxibPia94wfUJMxs1g/640?wx_fmt=png&from=appmsg)

## 新的网段收获

在该weblogic中发现主站内网地址并且可以连通。需要注意的是这里主站的内网ip地址变化到了10.0.2.X段（后面会说明该网段是核心内网段）

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJNTJIQdcCtPes4OM6lic1LUEfuwDmDOBvQKbrmtrKcy0...