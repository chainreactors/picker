---
title: 用友某产品最新版前台RCE
url: https://mp.weixin.qq.com/s/XSB9-MZ-kNiUwU65era8BQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:40.657510
---

# 用友某产品最新版前台RCE

# 用友某产品最新版前台RCE

原创

ptr
ptr

UpRoot

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

入口断点，发现\*.do结尾的路由会经过nccloud.framework.web.action.entry.EntryController#doPost转发并且不会进行鉴权。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pch3JQlDkkMjLCPibhHuOq0yQdy5qfHJCUDiaQBbNHrvdU4kh13wZN9cJiaz6to9OhRN3u8ia3GNQcia75hic0gZHicgr7n7gqkjoP0R8/640?wx_fmt=png&from=appmsg)

进一步跟进来到nccloud.framework.web.action.entry.Dispatcher#doAction，可以了解到最原始的一个请求`/nccloud/platform/total/switch.do`其是由`/platform/total/switch`三个部分组成的，其动作的实现类是nccloud.web.platform.gzip.action.QueryTotalSwitchAction。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pd6ZV4NYpicSiahyLo5BpZCybvWUNfdsnu5ZicjXibaMmVjTica0PBs137jlaGsWqByKNicmR91EUWVZ98iabIo2G92KZwvnXSGDtsTvs/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pde8Lia73ia8HrfiaQPicvEhPM7eWicd1KFYL4D6icCNggetkibuPY3Mkcv4MniaoHA1DzPLeghy4zMJuEcccI5PcAHxlkJxia9RuYrXPcc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pfYyxLMjPHYyrE5xkoyphXIUWdPuNeOhbicxe8z9PRhA1K0ibsJrEumx7Vg0S0VicUpfVXf18iaKWo3BeZWrQUB0IYKIicPDL6NSWbU/640?wx_fmt=png&from=appmsg)

通过类定位jar包，我们可以找到action的配置文件，由此，我们对于基本的路由形式心里便有了基本的认知了。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pepX0bmwAHRNUF389fqQHuC7877mjqiapk2hKqpH32WbkDgnrMnSgJSbHVBL6VdlCibKLU0icTxuJHM56vkQXLRdTkjlh1jibLs6wY/640?wx_fmt=png&from=appmsg)

如果是正在进行红队评估，追求效率，不妨以此入口，寻找破局的办法。

我们重点关注可以通过EntryController进行转发的action并且该action的具体实现办法不会做强鉴权（如session、token等），从中寻找我们想要的sink点。

通过大量时间的寻找，我们可以定位到nccloud.web.hr.login.action.HRPubBusinessInternalAction#doAction鉴权较弱可被绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pent7S16HIHECgpxlUIpY5WqfLE5U6b9pvvEue1Woe2g0er5JHpTyN4DIjibMbyvqRjtDAianpYd931cMdPpcLMcn4LAUStuluBY/640?wx_fmt=png&from=appmsg)

并且该类具备对类初始化和调用类方法的能力。但前提是被初始化的类需要是AbstractInternalDataFactory的子类。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pebU4souBQ5LEsSkBgSPfT3ib8NS8Hw0S1Lt4ZEEKogTRptxky7KT10Fqxt4Pll6CIu97WL8aW1zfm3ymYZrkW7iaFFlDlPhptcE/640?wx_fmt=png&from=appmsg)

不妨以该点进行展开，发散，寻找哪些类是AbstractInternalDataFactory的子类，并且具备可以用来rce的能力。

由此，我们定位到了nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory。

nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory#dataOperate方法内部可调用如下两个方法。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pdBl3icSbmoOecbxb9VsSVL72apzkFT1iaibA0nCUkyqFeK3xSo7zIqKlNMAsYBy9RkY18oHd0IahUx08sNIcJCagRwuMl3lP1Qcg/640?wx_fmt=png&from=appmsg)

对于nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory#downLoad方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pedmFDRJicrkqqJlxKXGOPyiaTNJxQoTfriaApnulViauNpWTSU3kxUIB1HickOiaXnLFSwNZnLg6FQdnfVIAODE7pNtAP2os1DB4dx4/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pdeImdcic8N4F2Jr7iaOz4I3NDHVLibtZZ75vCrMfkp6IdXAhvsJ2rd3BykNOIA3Gx4PheAUUNkqdObcW11Ro3HwnbAHslKfjibmJM/640?wx_fmt=png&from=appmsg)

这里先从字面上理解rtf后缀的文件是什么？bing搜索后了解到是富文本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pdBqzpBtl6hULXN4YDUkQJ77gAiaHxNnt9ooWPbBickt8ibdR6ic6klRpZWcVE0EOD8l8icPKcJZOnic7QEeymR04C9IHISblRnn655w/640?wx_fmt=png&from=appmsg)

那downLoad方法大概想表达的意思是把doc转成rtf这种富文本的形式。我们继续跟进nc.itf.hr.tools.rtf.IGenerateRTFDocument#createRtfFile看看有没有操作空间。

来到nc.impl.hr.tools.rtf.RtfCommonGenerator#createRtfFile，继续跟进nc.impl.hr.tools.rtf.RtfCommonGenerator#buildRtfFile看看是怎么build这个rtf的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pcl4Ts0p4sOvsx82gMwJz4uR4OhklZK9Zs6HrdOGR7Bzc8enEUEamSFmU7Zx90Mv0eDm6ZTC43kEBKiam7LjWib3EL2BQFpk83Jc/640?wx_fmt=png&from=appmsg)

来到nc.impl.hr.tools.rtf.RtfCommonGenerator#buildRtfFile，我们豁然开朗。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pc6o8sJ0W4FVxfXduwLzrwH9zaH7BFkuca6t0kibHGujJXSxKY53uoXT8GSOOsaBggGKOZfdBsMxq8DTyx1IVJBh2pu031Wtj2s/640?wx_fmt=png&from=appmsg)

标准的Velocity\_SSTI。（具体能不能r，我们后续debug分析就好了，此处是我们看到了破局的点。）

回到nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory#downLoad这个入口，我们看看这个数据流从哪可以填进去。

重点关注vo这个JavaBean，它承载了我们想要的主要数据。

```
bytes = ((IGenerateRTFDocument)ServiceLocator.find(IGenerateRTFDocument.class)).createRtfFile(context, pk_psnjob, "psndoc", vo, (String[])null);
```

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pfI6nj98mwxPNXEdI9blgibXwMy8amVIjFAryNYTbqeBkxHRWcu93YA9seI1yOklExdkyckW75kLLMsEEXnpXPSza5KMGyM89BY/640?wx_fmt=png&from=appmsg)

vo是通过`bai.queryByPk(pk_rpt_def)`赋值的，重点分析nc.itf.hi.IRptQueryService#queryByPk做了什么事情。

那这里，我随便输入了个pk\_rpt\_def的值，最后得到的结果是null。由此，我们有了个初步的结论，vo是由查询并赋值得到的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7peCJnFV09ex59NOX8WoExoDjGf0LkIete6ESRvZm6oGt8hKP4cyUR6r6PYtpSRyLGyGbTobwKjbz2zSkw5UyTib0Vqj3GQOymgM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pcEAVVxYnpJFO4DTzxwfpqDgZULxbamjamaHzq8BIg9WPgWINc7NJI7rwW0jNicFhxOTuphdSibgNEPfL6gGwswrPLAznoheORjo/640?wx_fmt=png&from=appmsg)

进而，我们的思路转变为：外部可控的pk\_rpt\_def参数，它是什么？其值如何获得？是否可以伪造？

带着这个疑问，来分析该类中的另一个方法：nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory#upLoad，它也引用了pk\_rpt\_def参数。

外部传入该参数后同样是进入nc.itf.hi.IRptQueryService#queryByPk查询，那由此我们可以推断出pk\_rpt\_def参数是表中的字段的值。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pek7edIxJURtsg7wibNKSvA19GYAt7EnBvL75qatbAAI7qeg4GlPnST7yrQqcOEcYhVx6ZjBiaemJ1PckdBRJERSstfhpSlLib5GM/640?wx_fmt=png&from=appmsg)

这次我们仔细分析一下这个查询逻辑，看看是去哪个表里面查的，pk\_rpt\_def是固定的还是动态生成的。

此处，拿数据源，datasource外部传参而来，由此，我们这里需要知道一个点：需要一个接口可以返回系统的数据源（前台是有这样的接口，本文不会提及）。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pcvp84TDl5IfcXMQkjqmFaTsDofiaHqVw2Xw3o1Oxr0E4x4rQLBnplQGK2P6oIZqjsibXd97aNEPibdXXDZAF82wmCfqGc1mrrmb8/640?wx_fmt=png&from=appmsg)

随后，参数被送入hr\_rpt\_def表进行查询，取值判断是否存在。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pdk1CBiaxic3hU3uNQ8JZPUSLJBOaiavNWDkvSZKKDUJfQj2ANnzOSiaR0ojrNhsn0zxgX2UPSqKK7EcxWYCPOOCEqMdjUazyJ5UF0/640?wx_fmt=png&from=appmsg)

我们去数据库中查看hr\_rpt\_def表中的键值情况。

找到了我们想要的pk\_rpt\_def。（注意，此处出厂配置如下，我验证过别的目标值也是如此。如果不一致，我们借助一个前台sql注入，即可拿到表中的值的，这里也可以透露一点，是存在这样的注入的，本文不再提及。）

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7peFX2Z5tAN3n6hA77jNF6w2s60vxX72WYcBnbYBTUKO7f0m9PwYm5CREvhXUkM5l9bGreVPb2v3Upj5dsGPNJppE4YlicyFVruQ/640?wx_fmt=png&from=appmsg)

由此，我们获得了一批rk\_rpt\_def。

```
1001Z710000000000JB3
1001Z710000000000R7Q
1001Z710000000000R9D
1001Z710000000000RA5
1001Z710000000000RB5
1001Z710000000000RBP
1001Z710000000000RCA
1001Z710000000000RCW
1001Z71000000000DNII
```

从前文中，我们已经了解到nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory#downLoad是用来消费vo这个javabean的，那我们这里完全可以大胆的去猜，十步之内必有解药，那nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory#upLoad是用来生产vo这个javabean的。

大胆猜想，细心求证。我们带着正确的rk\_rpt\_def去走完整个nccloud.web.hrhi.rptdef.factory.RtfDownloadFactory#upLoad逻辑。

方法的开始是从请求中拿到文件并转为流。注意这里的request.readFiles()，其内部实现是接收文件上传表单。

由此，得到一个点：构造的数据包需要是文件上传表单的形式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pcyZwJZgu4eu1dJiaib3IlibXEt1UmuoRjXFbnia2OwGaWkjHIJjqbsq0lYXKM9CnUt91ukibIRAbpvrUerjSDkV76Y5hd2SGXmjBdI/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pftuEdk7dIRNdKHHdfYC0TgPec29aOT3Vym77iavzJwTIia1DTwgWhmURQl1icLBhHNVricYxD0VBbsVoE7VBMF4qJMmMdCWfFWlqg/640?wx_fmt=png&from=appmsg)

随后就是根据传入的rk\_rpt\_def参数去给vo赋值了。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pfic420Dac9NYdoTnuZbIpficw38FIoCA47ZAFMQk41ZUHbFuLdUF6iahVOfQJrMK8DYFsibaUwEjjv1yptlhffUUDtjqgOyjD34y8/640?wx_fmt=png&from=appmsg)

接着，针对上传的文件流进行保存，我们来看看这一块的逻辑是怎么样的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7peRpmY6Wsp5peFwAFcoxGD5oeKs1VX6W4xoNW9u0EIWTArPXeiaria8ibzPg271kbK64iaALdqnNxVy9CcOpSumKs97auGaENECF2k/640?wx_fmt=png&from=appmsg)

将文件写入到用友产品的临时目录下，其实这里也可以认为是一个鸡肋的任意文件上传，没法解析。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pcyiaiaibImCIZ8VETJCaZk1iazzGSmgSZbtrPI4ib9uCadH8phWP106POBDibNdJlj1qzuVdcw3bjyWtCAUUwk0xTzsqic5fBK7Il8cE/640?wx_fmt=png&from=appmsg)

从磁盘中读取文件并转为字节数组存起来，这里就存到vo这个javabean中了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pcHtaKYzahSUyicj2HUbDJoj5SwGvBPS9ODlKTw7EbkLhK14HS0pia5WMdc8lPbGKPkA4uAUdJ71AHbrjBCgudlK6ojLLTdYEZN4/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pcJWoaRud3UH5ZAIvfuabqNk99KsdlBicya6iaEb0ia5kSYbNIiaj2tf3WET5PgekwQjJanf5eIrurnbQlWvg78AGq3Gu4EcickuMe8/640?wx_fmt=png&from=appmsg)

前文我们了解到了vo是javabean同数据库相联系起来，在这个方法的结尾，我们来看看vo的值如何。

![](https://mmb...