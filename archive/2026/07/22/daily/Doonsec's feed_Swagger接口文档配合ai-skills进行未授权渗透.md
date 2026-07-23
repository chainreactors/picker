---
title: Swagger接口文档配合ai-skills进行未授权渗透
url: https://mp.weixin.qq.com/s/k7paNwesuC2Es-XUhO32ew
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:09:25.763061
---

# Swagger接口文档配合ai-skills进行未授权渗透

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EtvWPgXicyttSdOby1N2QibxQOmghpzjia8p5sojGaHauyBlXuIvdYqh9JUbFyzflR8Xo4Mibic2a4uxHsq8gukiaNXPicMnG3DDldwQg/0?wx_fmt=jpeg)

# Swagger接口文档配合ai-skills进行未授权渗透

湘南第一深情
湘南第一深情

湘安无事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

## **前言**

以前再跟学员沟通交流的时候，经常吐槽测试api接口文档会很麻烦。

现在我们不一样，有ai了，直接猛猛测试就完了。(由于上一篇文章被删除，重新写一下这个)

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsiaWB8x20YnfL5J8jmue4d1ZjESbbVf9XTxczJFBS3JdSgn7NL1nWk4GrcJfZFJY2Fdsv2AQfmuqf8iaFXxArcUuOLkKSeqXfXs/640?wx_fmt=png&from=appmsg)

但会有几个点要注意一下

```
1.里面有删除添加的接口，有没有提前约束好行为2.ai测试过程做了哪些操作不清楚3.ai也是有误报，那该怎么规范和避免错失漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtoZlw2O1TQgBwtpDWyMFb9DPxz7KD3icy9G0SKH2UvXInyNp1CGXe1zSyHO7Ppb9fycaQ0OWhognYTyPXoU4gibpbjeucjPVgdc/640?wx_fmt=png&from=appmsg)

## 古法挖洞与接口文档skills对比

我们再之前的讲接口文档那节课

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EuvqQTGvbMeKCwqp9gC4PcMIy3ibGUaCernuKb6Jyd1JLHgqYl2HXicgNss3jWZWibj8Uq77418o1hElFZG9vQYHeSr4FxOUDyGLw/640?wx_fmt=png&from=appmsg)

都是交大家直接梭哈的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsYibwrbsTXMAKMnkpBpAkFmsOE8XdaBCv1NA73mwQmUtqMKOf5d33LQcokjO8G2LMl9ib1g7xHXHceILgmxzF3ZyKiaTicNibMj5r0/640?wx_fmt=png&from=appmsg)

这里有很大的风险，会不小心访问到删除的接口，然后这里写了一个好用的skills,skills如下:

有两种情况:

1.直接给接口文档的url

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtF8SavADVy6RhYFSzQuiaIBQwCkamibuELg4L1ZDa6cX5dfRZmJtoJfySBicBglgmBZILvVKat0QugMhickSlsKLlsSCg3zah7Od8/640?wx_fmt=png&from=appmsg)

2.直接给接口文档的内容,可能会让你输入hos和baseapi。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvxTwRmxnPJZTwDlEy7rvYbIXDRB6p4VRib3uViaogt6H6y9bLP4RxGZ61eOicwGnPk3VCF9DRVia01VXic8oozLyO3RSAKWmMtAKTs/640?wx_fmt=png&from=appmsg)

用的codex，模型gpt5.4,不同的模型都会差别，最好安装的时候让他适配当前环境

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EufcjkJqeP6TGdiceRThZ5sLP7gwTTHlMeLAWKiaXZMY9PRkXAibDBcFQK9OXUicMb1OCUg1ricveGr9iaK6Pp4kkfFY6Jw7jwMWDAt0/640?wx_fmt=png&from=appmsg)

他会输出三个文件

```
域名_接口文档数据包.md （根据接口文档生成对应的数据包）域名_接口文档数据包_删改.md (只放删除和修改的数据包)各个接口数据包对应的curl命令（已经剔除了删改的接口，curl是方便ai去执行）
```

## 接口文档skills使用

sqg.com\_接口文档数据包.md是剔除了删除和修改的接口的，但是总是有误差的自己注意一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsKEXB70DDsjf0QjQHeR0FKs875byE0kxwnAdIpzKpCuzcAsMXlpKxTNScZMKia5uCEn9VbahzibOp09ia5LYzyUJQBcXZJw7hicKY/640?wx_fmt=png&from=appmsg)

sqg.com\_ 接口文档数据包删改.md是专门放删改的接口的，因为未授权可以操作修改删除的接口其实也是漏洞，也可以交的，只不过怕ai误操作全删除了

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtJoDicxjibha52LYCuzXAWBEicbstZI91PPrg4e8XffAhJNiciaMcPKH9gdBHZKteiaoRzAv1Pd5T2oV7I8ibnick9vvNWQ73svsJ0wV0/640?wx_fmt=png&from=appmsg)

sqg.com\_接口文档curl命令.md为了方便ai更好的测试哪些接口未授权或者直接给deepspeek自己测,这里一定要注意带值跑一篇和不带值跑一次

```
我有 sqg.gdit.edu.cn 的接口文档（curl 命令格式），请帮我：1. 分析以下接口中哪些是【未授权接口】（即无需登录凭证 / API Key / Token / 签名校验即可访问）2. 对每个接口的 curl 命令，将所有路径参数、查询参数、请求体参数都填充上合理的示例值（如 id=1, page=1, size=10 等）3. 最终输出可直接运行的 curl 命令，并标注哪些是未授权接口
```

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtJtvlGOvvOQwcAc7Hp11ZWBuMOibg1wfrMvd2ueBdiaeRicvJz8aZESfaCKBxgzClpAyaSItqmbGhMhic1LnE0n0a2REsKCf2nOlE/640?wx_fmt=png&from=appmsg)

ai就直接给我测试出结果了，文件上传漏洞+1，解放双手了。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvhqnlOgvez84ibibhZmqEqJ2wjQWynISPCXeQksPfTNU03viaibfU2gH4ltATcv5hwhHftG6GcH39AME2icicGuMZPxSdEowFkU0Tsw/640?wx_fmt=png&from=appmsg)

这不是简简单单

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EuOU9gUw92y2TAZdBib1vrfVOw5iaavicibT88DGbFricd4nf7CE3HyFLiaKRRPq98BA5OS0BpbHg5IT9pcpSwADzb6cmckjUEia3xGiaY/640?wx_fmt=png&from=appmsg)

还有未授权获取密码

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtfO57vS5BZ6jzybnrm18kJzZH8PfSBU7Or270NQ3Zo5EKOKMCCLZsIgzgGs2RYvoGNW3YJSTibpibszw5aPPz1fXEtCib1LicGdXE/640?wx_fmt=png&from=appmsg)

其实也可以修改这个用户的密码的，但是这个接口被我们剔除了，具体自己手动操作，不敢让ai测试

```
sqg.com_ 接口文档数据包删改.md
```

很多漏洞打包直接提交了，高危+1

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtibmbN2iaeMMsZW7NFR6RHuA9GVOjoxibsYFo9KDcLBWosw9vGtdG6UiaANVasQXbuYXDdQqgFSUsXmCDTOLrDejCJKsoPxM5Sp9k/640?wx_fmt=png&from=appmsg)

之前的文章被人猜出来是哪个src了，所以有点敏感删除了之前的文章，再这里向厂商道歉。我也不知道为什么厂商看出来了是他的资产，可能有人转发给厂商那边了，但确实我不应该违规，我以为修复了就可以发，我的问题，向厂商表示真诚的歉意。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Ev8XQPDRv0TQHxOjSibYgxcUdojk55NR6UibPeUYiazN8TStEvicOIsdc035Pdc9z0QvWnlweWh4XVrjH9iavpIicl0UhicS5lOg26hzY/640?wx_fmt=png&from=appmsg)

## ai挖洞交流和湘安内部漏洞库经典报告分享

上周给学员分享了这个接口文档的skill，上完课之后也在跟下面的学员交流了很多关于ai的问题，比如上下文会压缩导致ai变sb,下午的时候ai的模型普遍很拉。聊到了1.00钟，深情哥快抵不住了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Et1ls2EQQgsYQ6cscACvBveBY811h9gBxdXbe4s405ia6FQxBDVmeSJwWpr37NJM9YpeibmhSl800wCnHRLjDxfzlYp75qkHrW7k/640?wx_fmt=png&from=appmsg)

所以打算创建一个src+ai相关的群，并且给前100名发送我们从湘安内部漏洞库平台拿出来的一些漏洞。涉及到下面这些方面，就是一个知识库（湘安无事-漏洞报告分享+好用的工具分享（ai版））。当然前100名是有阅读权限，好的文章或者报告我们也会发到群里面的,群友也可以看的，偶尔也会进行技术交流分享。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvCGzhWbNn09R9dMXDQwkKLyBIB0TYTUUU7Kwf4coCXUK2zBWMI4REgciaXhYeYr338cpVjczSibFH6Uta5IMO975ETUxg8A3uY0/640?wx_fmt=png&from=appmsg)

```
1.分享湘安无事内部漏洞平台经典的漏洞报告：edu漏洞和赏金src漏洞2.收集各个cms的nday3.分享各种好用的工具4.ai挖洞小技巧分享
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvBHh2rZUibxbEO3t8zYpibaiaPS1j3dc2lq7YMJWZ09K1hiad13ONtDBiaKxGLDtqqXRtHzhoiaZMO9EGsyRNS3coiasxvuOKhQV9Xq4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Evu7IUnpvSmvl6HeCqRxfWZJO8e42YvQibvu4WWWjiaOtxex5PyfJHUcL8rbIyCCkMysylkQx6xVZG69w0QcVrnzYEUksltcBa8U/640?wx_fmt=png&from=appmsg)

当然只要是再湘安无事edu团队的同学直接滴滴sqg就好了，直接可以给你权限阅读，rank高的同学直接可以加入内部漏洞库平台。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Et270S2PvvF19ySV9MMhMtBRTlAouBiapCpftr5mTvCiaYqVVDkLTynGD2PUPWepm8jE79WKSsC4LEfEpbiczLtrDBhguKWDNLVia0/640?wx_fmt=png&from=appmsg)

## 深情版edu+src培训（暑假跟着深情哥愉快用ai挖洞吧）

深情哥这里是有edu+src培训,更新了ai的一些，将以前的思路和ai进行的结合，交大家如何使用ai挖edu或者挖赏金src,我们更注重交学员如何使用ai快速挖洞和学习ai的思路，而不是异想天开让ai猛猛出洞，这样子会让自己的渗透能力退化的，我们不能成为ai的奴隶，而是ai的注入。课表如下：(或者加我wx:azz\_789了解)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EsNy7Yq4OuVICfVGoKrBia1L0O6hvGPfxCB4NC8MaN8oaG1o0wu5RfYQ3rTdLImz9wCqe2iacBD4y5YQoMrnjXDpib41lWcAobFI0/640?wx_fmt=jpeg&from=appmsg)

```
https://www.yuque.com/denghanhan/qqby5b/tmde5e8qwdysm5zz?singleDoc# 《深情版edu+src培训课表(2688)且赠送审计版+ai版》
```

### 【edu漏洞挖掘实力展示top2】

湘安无事团队一直都是edu漏洞平台的top2如图，都是离不开深情哥和区长的培养。(学员专享：对于表现好的同学，贡献比较多的会打印团队证书发放)2023年到2025年的证书~

![](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EuIPicQbGGVwOvia4J3jQlStXP979PdvJMh7keWOtVlM9apWCCShbVw1JeibQtFCBIFSV9cqqKwV53SPGKXhfOjVtImic98FeeAW7U/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EsLxiciaWh0Eq27Rk1vImlict8CTxIo9qZWx9kCxqfsiaH4U9g5r6bNOVF1bsAnIUe8dDqVJMsat3Z24JZleicgXY78TvAKIgxCAc5M/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EswlfciaNCIicfsulBEdbKu3uJ8KZLqCJNwvCmCez59Nkr9Qx7FYLIZMia66bdQib4rj666tnhzqMgBmPd8CtiaoSlNSxoFNFfF84uM/640?wx_fmt=png&from=appmsg)

#### 深情哥edu漏洞挖掘成果

我们导师深情哥实力，深情哥edu漏洞平台top10发送证书奖励

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtHOVzvP2xXKYlDJstaDPq0T6ycFMrnY69GXq1kqhCIvCg6icsl9KYJiaOqGFdubWY8MGoryHV5kq4joSlWUY7BfIhU8bmVvMfe0/640?wx_fmt=png&from=appmsg)

深情哥都挖了快2000多个漏洞，难道还不能带飞嘛，嘿嘿。我的edu证书太多了，可以看后面放的截图。现在不怎么挖了，因为现在都是带学员挖edu漏洞~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuNAU2wInicibXIGUkpicNkTZ9su4AnFnzibsicSJ7zuljBIibdcdPibJO9SicbCHRRebnK2ezicoRCxI2Dk9S6H3LxETFFoVfWSNxvrV30/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsYcJjrguSgNEs4FhEh2UljuEgKdPRmJ39JCKK1oOKGdaDGxUHujyPqgTibLzly2SyGXbf6RIDuAWyCFBLc9FoYMh5jublQLeFE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtANShBwMWicZwt3Snzl5ZNDfx6umv5KJI1225oHFuiaS61VQqXxGSd9IGHTXwFvbHPEduIr0F2FYko0FxQwgp090B3M8arbTibOU/640?wx_fmt=png&from=appmsg)

#### 中国地质大学聘书

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EuibgUPAKsibESU8x7EvX0aGh7paNRlYGDDNgn1iaPdF1lJYms2E4fpIu8kDRNQMG8xzwIKRf10iaMQUYbhgWtKTF58leMDNyO7bXU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Esh2y2h0w0pqQOhKXUTY2dXMuj9AtyabaNxpibam59LlwnKAq6GzcYlq29ZOpzwXxvjrCqfdG8QSxajS8Kc59Xp0iaAkQBgJxAA0/640?wx_fmt=png&from=appmsg)

#### 各个学校的感谢信

![](https://mmbiz.qp...