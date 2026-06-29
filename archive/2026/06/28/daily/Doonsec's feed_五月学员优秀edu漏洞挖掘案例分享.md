---
title: 五月学员优秀edu漏洞挖掘案例分享
url: https://mp.weixin.qq.com/s/uuVbj65Lyk9DqZAbehW7Rg
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:31:28.724924
---

# 五月学员优秀edu漏洞挖掘案例分享

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EucGnnlqJ8NVsIO8icicXr6hChRhMVQ1Rl3EUOfgjdMl4Fd0XxP07N2IUATkGAxq1ylSyVrsXpoDQYcqAQdVDm03fXVr6CRjYRkI/0?wx_fmt=jpeg)

# 五月学员优秀edu漏洞挖掘案例分享

深情哥
深情哥

湘安无事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。**

## **前言**

上个月有几位学员和成员再湘安内部平台名列前茅，给top3的学员和成员都发送了kfc奖励。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Esj4VSHf9tibTr9xppJHibaOUBSKdiaw9Vu8URVesf1PuicETf7adZbepgbwRugoeddpJX95nk5ibGGTl9ddFgm2zT1Ju8wAZUX7qIw/640?wx_fmt=png&from=appmsg)

所以我们来看看他们的优秀案例吧

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Evn0dquH9ib81HEAmyb7bwzOgySM8hg4cW37uGOXCH2o0DfeMgjbm5Azg3hpPnZ7V8PEc6XuTqkeLVkzpUicUJDnjH3ynjZc4TibU/640?wx_fmt=png&from=appmsg)

## 记一次未授权访问到接管大量学校管理员账号＋SQL注入的经历

故事的开始是煮包在复现一个SQL注入案例，下面这个小程序是存在SQL注入的
微信搜索\*\*\*小学，找到这个服务号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvQTicXc9qpdzpxCOI3LjTIf18zBrXEDroib3EAewLsem8B4ia2aOPAhHibpB0kqFGchH7odh99bLg1MROnPcGic9eIdwfh5GF0YubY/640?wx_fmt=png&from=appmsg)

点击\*\*小学抓包发现有四个包都存在注入，接口是不一样的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Euc3yUgrdFDkNa3OfNOScK5ydFL6KCaGzrjahbCOpJE8p0fbg2G7Bg44ZUFNSgiacy01AkSwfaxGMY4OvtOR5x3XnzygmqEsibuU/640?wx_fmt=png&from=appmsg)

本来故事到这里，就应该结束了，但是煮包测试的时候，习惯看一下bp的插件，打开TsojanScan插件，可以看到存在swagger-ui api接口文档泄露漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtB9W8t2J1Avos16kDw4RfQQpmAJSYibImCDvmpSVBrKdnUXBhRaj3wSoEmQtbtibxrIhU6sU2icpDgnymNgWwysEGmpbVrCRwERY/640?wx_fmt=png&from=appmsg)

# 未授权访问漏洞，可以看到接口文档的路径，再次进行拼接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Ev1YgxicDhBEHHYVjU1uu1xtMHcH5jgfpLFHHbYmEmIys9wnxVsaWoc0fYRSgNXluoD9y9z9ib4jRaq6NPfWfUw2mOHtjEFYD83E/640?wx_fmt=png&from=appmsg)

可以看到所有的api接口路径，大量接口存在未授权访问，下面这个路径存在未授权访问，泄露了其他学校管理员的手机号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsI0XW1K28KduqdnXSnkyfibr6cvmAOu0VicTgBIkvIH6ut6qI6pCELOiauw5ib84M4Cgib0PiawrIeoxt1Ke8YBfZ6PH4V4G6m8GIm8/640?wx_fmt=png&from=appmsg)

搞到这里，煮包也是交了edusrc,准备拿个1rank美美下播的,毕竟是复现过程中出现的，也没有太高的奢望，但是理想是丰满的，现实是骨感的，漏洞不够敏感，危害不足

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtDaLMgc23MKgXwVx1BibkfemHA9Lia7gJcVefgcNjr3ofVLicrFeiap1bkBt6ERprIH7DJuebuallRUMYQtHkFnUgYulQKXQf4mfM/640?wx_fmt=png&from=appmsg)

这就很难受了，难道要耻辱下播了吗？但是煮包不甘心，毕竟这个系统又有SQL注入，还有未授权访问，肯定还有漏洞，于是打开hunter，搜了一下这个网站

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvibtnePnbLJnsn3WiaqqSceLAKrLSiapPlVCLttiabdEbNgWQVRgVy8boI5bAse3v8GmcptRwXwETZFTZWHaYFQz1I31MGnrKqK8g/640?wx_fmt=png&from=appmsg)

点进去发现需要手机号登录，还记得之前未授权访问获取的管理员手机号不，这个时候派上大用场了

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtgrDUcoc1XvhRwue8ictzPibHSI4HHxtUzc0Xjjiaj50RUwMvEQ47CSznKBVsyFWouqic0paOxOq74jWpyXWhfxQIBLgDxgEc2Q0w/640?wx_fmt=png&from=appmsg)

直接试了一手弱口令123456

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtoUsgCLT3Ogic6Hsn7UkMD0s3rFO2Qx4dCQibqKIiaYVibhEMdribRedLeVb6Ce2xA7eRQAsFqZQ3UmxXEVFdDI2AOcTOCFOia49KNE/640?wx_fmt=png&from=appmsg)

没想到成功接管了管理员账号，并且权限还挺高的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EursZia8L2ck07IeKZd9KFZB05BZ9BoWkmw3yPzV6qTBcBV2RUdVarP1t3zCfaib5DEF9TZUfxRo4ER12a3dxbgpZPu4t84RMlOc/640?wx_fmt=png&from=appmsg)

信息管理里面存在大量敏感信息

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EukkHxzJtCzrY4qhsgd6XtibHvrJEm3Zv3PhBNb5NY304lyuCJVLrIjkT5XAINYtcxPKrXusCt4oEgh3eatNKZ4mkclibpiccEaC8/640?wx_fmt=png&from=appmsg)

其他学校的思路都是一样的，把未授权访问获取的管理员账号都尝试一下，最后也是成功接管了七个管理员账号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Et6wRz1JPTnV5jUtkGuq9sSdqsZBZXtwZsiaMMTSj4Uh5Cc3CROxo4WBYCStluI7mOz3hicHIwGCMNDAVByicV1BMcIJEbTPCLlSg/640?wx_fmt=png&from=appmsg)

都进后台了，煮包觉得还是要测一测的，点击考勤管理里面的学生考勤

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Etkn9gC3p2k8LEn7awjwU3JxYMQiccDEltBict0K69dewIsp0ibdVYrGRcOZWEsEdZZV5gbkn0VcOGgTX1LXLOdV041ovDUsCE1lE/640?wx_fmt=png&from=appmsg)

点击新增，备注处存在XSS漏洞，输入XSSpayload：

```
<div onmouseover="alert('XSS')">Hover over me</div>
```

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvQMNxqG4ibbc2DNnTXlTtWoXC5oicuguPC6vKia9zfzKPaRNoNo5gBNCkZUib6k0Lic1vqKujF2BHF5HLqc0U3qUkZtFStSj8HQ8Sk/640?wx_fmt=png&from=appmsg)

点击提交，鼠标悬停，出现弹窗，存在XSS漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Etje1pMsFBtqbFe7jqAcveibk6dxlHaUsWknoiaFU8tfiatwPjNy60CeSnTm2g5KSUWMHXx6YK4laIFibMdrJg6j2aGlX8NqVdWH3g/640?wx_fmt=png&from=appmsg)

整个系统的功能点均存在该类型的XSS漏洞，最后也是成功拿下3个XSS漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Ev3njqLNgh6ibygm9icKz2lsXa2dgiaic9Tn0uXdfAT2jqwgrzgGosO2iaVPicDbAzAeAYq1cPVhRtgOy9EGTvXhicSGCpB9iaj2icsteOQ/640?wx_fmt=png&from=appmsg)

## 供应链思路拿下其他学校

故事的开始是煮包不是在复现一个服务号的SQL注入案例嘛，然后煮包想了一下既然这个学校存在SQL注入，那接管的其他学校应该也存在SQL注入，煮包就去微信搜了一下其他的学校的服务号

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Et7dr3M6pq0z22FW31SEsDZFerTpZllFdic1G1xaTxTic9FPz5GGrRplLZiaRmZBsg1yk4bs9PYAqezLQhN3pgtibzibV6JakEvnx5U/640?wx_fmt=png&from=appmsg)

结果还真让煮包搜到了好几个学校也有类似的服务号，套路和复现的案例是一模一样的，也是智\*校园处存在SQL注入

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Ev4GmBvdhonRKaUBDic4IkOvJvjVywStv6kChwKo38fX7UsRKgFxgjSyoWsiaWjcFVM6W8TaiaK6hllpfDvj33OSm0ticiaQ3ticvfiao/640?wx_fmt=png&from=appmsg)

报错注入成功注入出user，四个注入都是一模一样的，就不一一展示了

```
125-updatexml (1, user,1)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuWOtoVLonENfq6jbvJ4GB42CZa8X8E4vMicO4H0XP4c7pWGkOvbP0Km4on8PPSZ4vrKSMwtrlgUMTskzjhCbyw9et6JAEqEYg8/640?wx_fmt=png&from=appmsg)

最后也是成功拿下六个站的SQL注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvJ1w1tvY5APIibw820eHJMhf2D3AvPlZzVJKjV9mMIPmbALdmBPn2OibTaatkrEfiaD4dgJcMUGM5WUXfbhWW08wQhZwVos6yewQ/640?wx_fmt=png&from=appmsg)

## 成果展示

弱口令由于是同一个系统下的网站，审核的时候全都给的是中危1rank

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Evjj4sm7F47o88Pt3AncuXDwCfmgVtj9aDibX19Giclx8JOYiclZYFEAPkk0mna5YCIJHFlR3ohxQUVZfl7PxItHVBV90LHJdu75s/640?wx_fmt=png&from=appmsg)

SQL注入由于是不同学校的服务号，所以每个都给了中危2rank

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EuDhFqptMFWTjoHEjkCYEf3FoJgJibiagia3vKYCbs5y3c1BxlWU6PPp5uLHDftpuSm6QcKFSBdCF2rg3bJz8DzHnj50MXROIe0iaM/640?wx_fmt=png&from=appmsg)

最后也是一个系统刷了二十多rank，所以说复现案例的时候一定要细心一点，说不定就能挖到更深的东西

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Es4OjSy4hmV7WqpNsEc1FANQtPgl5QV5EtLQnBZw9cJPqZ44ricUHeZaNy7Gyibl0bbz4iaZRIdV8gib5dqV8JMEHDAcY0VRefqqI4/640?wx_fmt=png&from=appmsg)

总结：故事的最后，总结一下这次挖洞的心得吧

```
1.用bp的时候，可以多看看插件，说不定就有惊喜2.漏洞被驳回的时候，不要灰心，想想如何进一步深入利用3.小程序和web是有关联的，有的时候小程序挖不到，可以去web看看有没有方向有的时候web端挖到了漏洞，也可以考虑一下是否能够在小程序或者服务号进一步利用4.漏洞也是相关联的，未授权获取到的管理员手机号可能不够敏感但是弱口令的时候却能派上大用场
```

往期文章

[记一次edu攻防演练又拿下top2(湘安无事ai辅助版)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495313&idx=1&sn=c5de1dd35d54b28a9e1349ac16c58dc5&scene=21#wechat_redirect)

[2026最新版burp破解教程+ai操作burp挖洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495278&idx=1&sn=37563ab9c3aa7dbd0032d668c444579c&scene=21#wechat_redirect)

[湘安无事首推的0基础web安全课程](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495233&idx=1&sn=c213276f0a0e3114fadb2ee693967c5b&scene=21#wechat_redirect)

[学员挖掘母校实战案例+4月湘安漏洞库平台优秀实战案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495226&idx=1&sn=964c5d38716a725c251affa609579d9c&scene=21#wechat_redirect)

[从逆向加密逻辑到一键明文改包：我的 Yakit Hotpatch Skill 实战](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495182&idx=1&sn=c00c7fed753d2eb5c28c7609ce1706e6&scene=21#wechat_redirect)

["深入探究JWT：解锁身份验证的挖洞小技巧"](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495180&idx=1&sn=6d13c243db60ec14db5c9e8dae12b8b0&scene=21#wechat_redirect)

[敏感信息泄露漏洞总结：深情哥提醒你aksk正在“裸奔”](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495067&idx=1&sn=47d93faf7fa2632bdedef8da9396bf04&scene=21#wechat_redirect)

[985–edu证书案例之有意思的报告](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495097&idx=1&sn=dcb8c4a665b2030bf0e86d042f687ef6&scene=21#wechat_redirect)

[五一弯道超车！深情版Edu+SRC培训限时低价，文末免费抽奖(两份kfc+五个无影激活码)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495149&idx=1&sn=9250a9e7ac52ec71c4a492ec77645426&scene=21#wechat_redirect)

[记母校漏洞测试一次waf绕过经历](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494963&idx=1&sn=a3402602ab048ef32c1bc7f36d702dde&scene=21#wechat_redirect)

[Codex-AI 道德审查绕过进行js逆向](https://mp....