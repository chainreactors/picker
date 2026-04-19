---
title: 某rce漏洞挖掘等案例分享
url: https://mp.weixin.qq.com/s/0L240Zrl3a8S4OxGA6gczQ
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:46:14.833949
---

# 某rce漏洞挖掘等案例分享

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQuGbtQbANM31ic3CltKrMgH3DkzPUiapibCsLXfuD9WOxqjFq26FEziciadaQc97E8JGdyjriaNnkyUjiau6VFPSajwRjoDzNh3Pw42U/0?wx_fmt=jpeg)

# 某rce漏洞挖掘等案例分享

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于陌笙不太懂安全
，作者陌笙

![](http://wx.qlogo.cn/mmhead/00GYaClAoOo0M6vWibfxlTevuZgVm0LYDLUBfRh5aYicqq4IEibjicq8Ea4RCDIITyYCew89YflS348/0)

**陌笙不太懂安全**
.

web安全知识分享,渗透测试,SRC,CTF,等优质内容分享学习！

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

## 信息收集

拿到公司名字之后使用一些收集方法拿到主域名

然后批量获取子域名探活之后去探测指纹，然后针对测试或者手动挖掘

## 漏洞挖掘

使用ehole探测之后对重点资产手动过一过

发现这个资产

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQVBBPkWPrZ1B0WC8NT6aTzJgjdSv6z3NxBKiaFFvpLco6GTdI3fNM2IWq77cKbxicyISQsgic82jYW0xJAuibmjBC8N6rltKcruCk/640?wx_fmt=png&from=appmsg)

依旧登录框，常规方法测一测

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR3tv2CRPkfj33NwSOuMiaIkC1kQ4KhyubgL0fmojciaMGw3njUGJTlSqw61Y64NVzib2ufUe7lWxuJbwEg8YaBscgX0kLxFcpTFo/640?wx_fmt=png&from=appmsg)

但是不要墨守成规，根据实际情况变化思路，比如这个站点的突破

输入手机号和密码直接说手机号或密码有误

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQSm1LvNVTibicibJVV0IOvOxdowoR4sT7ymMTYj5IKcZxRhAz3oqDh7o5ZylsMQpXlWYQiaQTXic64t7dF1lqicIrLaYLsNsLGhWhGA/640?wx_fmt=png&from=appmsg)

应该不存在用户名枚举

固定密码爆一手

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQN5iaGVWVM367pLNcNDGA2IcpfIqaC27CpzYbAicR7b2Gm76XTXetVmibU8FoibIs3t6V0e90NBOkicGoTmweVFRseb6vzMkW2Pf5I/640?wx_fmt=png&from=appmsg)

一个都没爆出来

但是注意到页面上有这个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQPKEdFX4aTINf16v3E7ZIr3vKkpeZvuBclZicVCneCiagL9bSzuJ6SATI9h3J7l5j8Qyp56LWchtLZ0u6bURzX1uHhne7qLrDM8/640?wx_fmt=png&from=appmsg)

技术支持的手机号，直接固定这个手机号爆破

但是有时候他不会这么明显，这个时候我们就可以看插件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQLZgOLleA8f1D5pwEuIWCjicRfe2jr4pVUKz5HMvQTnLsxPJRgnFRZZdJoK1VeuvDickUHAc6Nxic02O2r7ABCibHpCCWJlfGrl74/640?wx_fmt=png&from=appmsg)

试一下常见的口令top10000

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRh2Iop3C3paOuicgfCm2qibVvpicroaAZ6gaTpTSrt80QuNZ7w2PY2V7IMD6tEjTajmR4QCk0icvxqYLVMpDgCwpPzvUOW6pFALqY/640?wx_fmt=png&from=appmsg)

这里直接给密码爆破出来了，而且还爆破出了框架

这里就有点坑，如果没爆出真实密码是看不到shiro框架的，可以看到所有流量历史没有一个提示shiro指纹的。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQq2kX7utCzvXXAll6O6fic9vaAbZDOoCBIPNdFJpe89SlYiaQUmPJpnXLicJfK94xAicNA6BdEqWaKbGP28ticoAI1WeXlWOUibEqOc/640?wx_fmt=png&from=appmsg)

Shiro的常见知识

```
Shiro反序列化漏洞原理
Apache Shiro框架提供了记住密码的功能（RememberMe），用户登录成功后会生成经过加密并编码的cookie。在服务端对rememberMe的cookie值，先base64解码然后AES解密再反序列化，就导致了反序列化RCE漏洞那么，Payload产生的过程：命令=>序列化=>AES加密=>base64编码=>RememberMe Cookie值在整个漏洞利用过程中，比较重要的是AES加密的密钥如果没有修改默认的密钥那么就很容易就知道密钥了
利用过程构造Payload：攻击者首先需要将恶意代码序列化为字节流。AES加密：然后，使用Shiro默认的AES密钥对这个字节流进行加密。Base64编码：接着，对加密后的字节流进行Base64编码，使其可以作为cookie值的一部分。设置Cookie：最后，将这个Base64编码后的值设置为rememberMe cookie的值，并将其发送给目标服务器。当目标服务器接收到这个恶意的rememberMe cookie时，它会尝试对其进行解密和反序列化，从而触发漏洞，执行攻击者指定的恶意代码。
Shiro550与Shiro721的区别Shiro550：这个漏洞利用了已知密钥碰撞,不需要真实的rememberMe cookie，只需要有足够的密钥库来尝试碰撞。Shiro721：在这个版本中，AES加密的密钥不再是硬编码的，而是系统随机生成的。这使得攻击者很难直接猜到正确的密钥。然而仍然可以利用登录后的有效rememberMe cookie作为Padding Oracle Attack的前缀，通过精心构造的cookie值来实现反序列化漏洞攻击
状态变化
- 未登录状态：请求包的cookie中没有rememberMe字段，返回包set-Cookie里也没有deleteMe字段。- 登录失败：无论是否勾选RememberMe，返回包都会有rememberMe=deleteMe字段。- 不勾选RememberMe登录成功：返回包set-Cookie会有rememberMe=deleteMe字段，但后续请求中Cookie不会有rememberMe字段。- 勾选RememberMe登录成功：返回包set-Cookie会有rememberMe=deleteMe字段和rememberMe字段，后续请求中Cookie也会有rememberMe字段。
```

我们重点看这个状态变化，常见情况即使登录失败，也会返回rememberMe=deleteMe，但是这里隐藏了，所以我们登录失败是看不到的，问题是工具怎么在没登录成功的情况下识别到指纹的，并且爆破出了密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQicvHDibia5BRkwHBfxOC5mvZCT85bGvZauErAmYwFA7oB3A6Cqefbsaf4jSDm4Bcy2pEfZnfZibtPrfm6qPoK68FFygp7AnZjRicM/640?wx_fmt=png&from=appmsg)

去学了一下发现，工具会自动发送这个字段rememberMe=yes，然后返回这个rememberMe=deleteMe; ,来进行判断

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSiaLhYddAWiaTXVJsfDgeQRiaH52u40XbxiawvdOvrkpibqB5szjZ8P1mRbt0zUCOjia8UNibibKqM0UNgoWb7BaACyqXrjQRfMEtDK8Y/640?wx_fmt=png&from=appmsg)

我们使用burp来试试

不加之前

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRf0mH3HFGXA44fUNAOQrWdFoEOxNQap04humrCLMicW9OyEXLs1ETK13rrHxbSntrNvNT5PSPjQ1KSVwKQ4mxicpF7vYbbS0UcQ/640?wx_fmt=png&from=appmsg)

加了之后

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSzoglDEAgLLak0tdmTzCdL8ZmMqrQ4DticS61eDsBXSDEQ8Hamzgc38V0Fcib8zrKaIVgJvdvhnVzK5a5hnYBqPqmoicjgY2SnEU/640?wx_fmt=png&from=appmsg)

发现这种方法确实可以

后续直接使用key配合工具进行梭哈

先使用这个工具进行梭哈

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTR9Mynkf1LAE5OTz1AIZx0ibqZJ0rockU0RoM5aicgywIJRqxnNydzicahy35JZ4eGDVdBl6fzzkntfY1RelyybDd3aQibP0p38ws/640?wx_fmt=png&from=appmsg)

可以看到会说密钥错误，cbc和gcm都用过了，如果你只有这一个工具，正常情况就跑了，但是我习惯用多个工具进行测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRfbbv7r0D7XUDgtbgiaS8pwJatVlicQUD1RTbuvNaD5ic9UDRBJAcibuHRzvDoMO6zicM7jWkQDpjmLe1DlGib1qSjcxhupiaKKNomQY/640?wx_fmt=png&from=appmsg)

这个工具就直接成功了，我们继续爆破利用链进行验证，cb1可以利用而且有回显

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRX8z3bw31PYXHOghfHNvTT3ZMcgN78R30puG3a1VSx3W613gUTyicJEJeZtoZrRHNgEeVvLNXrHXMo9YQIYpUiadencvrDaY0kM/640?wx_fmt=png&from=appmsg)

我们直接尝试命令执行whoami

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCicGricVHibNzZmiaRMYAOAg7YzCpf4aIhKicTg6J2rmm5C1U1JMxgHJxYjngb6N9oOomv1icNEiauFx5rQVEUcyQyYVP3apOmdicWBA/640?wx_fmt=png&from=appmsg)

可以看到成功执行,点到为止，所以在利用工具梭哈的时候还是多试几个靠谱一点

shiro除了常见的这个rce还有权限绕过，没有突破点的话，这个也可以注意一下，但是这里试了几个没有

```
CVE-2020-1957客户端请求URL: /xxx/..;/admin/Shrio 内部处理得到校验URL为 /xxxx/..,校验通过SpringBoot 处理 /xxx/..;/admin/ , 最终请求 /admin/, 成功访问了后台请求。
CVE-2020-11989客户端请求URL: /;/test/admin/pageShrio 内部处理得到校验URL为/,校验通过SpringBoot最终请求 /admin/page, 成功访问了后台请求。
CVE-2020-13933客户端请求URL:/admin/;pageShrio 内部处理得到校验URL为/admin/,校验通过SpringBoot最终请求 /admin/;page, 成功访问了后台请求。
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTwDvy3zUY90AvbxjYSdshiayEpQvt9ibtlyB4EGT3F8Maib438uFILKPRT22oVYvuAtHLjLUfdKoCk1zB8BrTIo0ZMvAUNdTKxtI/640?wx_fmt=png&from=appmsg)

后续进入后台正常测试即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRruYW7Qib1YS329p9X6ibRcHsTJZ8LoyeNBDL3gIdau4H0lGhGgzSWF7IKnibTfyP8NJa2dbFVQ6FLbq6Kxde5RUibuLLQicsME4Wg/640?wx_fmt=png&from=appmsg)

后续没啥了，就有个上传点比较有意思

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFOxhMNs6HFxsthOgCnt4fWvcQD553GEJwqZ2F72z8Xr4nSQNrglkiaXkKwXeX5tTADX5OeJOoFWMJHWWkXJJ2FwOXpXzEukN4/640?wx_fmt=png&from=appmsg)

文件名字能控制，尝试xss

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRfDH0n0K8HpVK9Y8R4LpzFKjWRErS4bXGe1lIYHMj7ZWKlnB9MIVQaDQeD0sHUfJkY0ExxYiabyDibVTA3p4ZXNT8YyqHanV5nU/640?wx_fmt=png&from=appmsg)

但是有waf

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSl55eYw8v0HRXknEI0gVP78MEhq4fTswFxU4a9ZZia4pX1YAJtDE22iamgWRHWricgKMgmib0HqWQEMlZqAaaElDhhaAGFOicibMCQs/640?wx_fmt=png&from=appmsg)

不过也是一种思路，这个点竟然连这个pdf都水不了，用迅捷做的，都没弹窗。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ0WfCS9ibA4YlykdnWnhSO5ZZTiaWDGvKd02NcP3QjBrsXzdbSXCaYc52Zhbpck3vZHzrgBp6aCHD4WYNPHXmwibMESKSHib53dkA/640?wx_fmt=png&from=appmsg)

后面测试完了之后，后台也就一个csrf创建项目,一个druid页面，但是这个不是未授权，需要登录之后才能看到

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTlY5ygJMEDb7yL00QTic4d4rhD2ezdw4qGBPoBFFyv69K0jQiceaia9ljCdBpxjicoAflVRGTko1U4dBY1KicVACjrSamKzl9HPYAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQuCGuP5EFXiaSuhj4DstlNhAtgyprcL0Sffmgm5sAOo2k2kQSlD0vnrQiaDFDribFUENP49ib7zS7LtGicIV06jicmdmrjNRc45JUeg/640?wx_fmt=png&from=appmsg)

session页面有东西看能不能登录其他用户

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRvNFSYr4y4htmwwA56E6ibOE8xucKRF89NpiaAujmTYGDMcdoCrdkR3J8oq1LSfTFFOzdYricFgCcm5ib3F7OiaiaVMyaW85HGsUAos/640?wx_fmt=png&from=appmsg)

使用工具获取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSiaaCRXazfq0WOsp9Q5gAXbIKmQQzJkuHSdibl2VicialFsr9W0emma0cGAjU4S1Lcfsltc3ma27bAFt1ogO8GK6JDAqPia6fWjBDI/640?wx_fmt=png&from=appmsg)

不太行

直接复制，然后找一些需要登录后才能进行操作的功能点进行fuzz

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSYczbeemgl5mVX0hUMGQianEYLkBVgQiahAialu20oLCjtH1k9JTtuoCc1avicRLhaucb0QNxLHKxNKNg8jv2EhDiawI9s6fj7AAts/640?wx_fmt=png&from=appmsg)

比如这个上传点

如果不登录，会重定向不能上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQQjeVB9D0nRSTIELmr9RpfnibZb26a5MzMa5Xvv6kGaYicJF9HMWib1ozWUtGdpSWOscYhtnRLC6rMkqr1elWicbmNana4BLm8vZU/640?wx_fmt=png&from=...