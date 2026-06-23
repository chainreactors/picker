---
title: 打开A页面但是跳转到B页面了？有可能是这个原因
url: https://mp.weixin.qq.com/s/z76li2eKbnWZA3XuRfjgWA
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:06:15.586096
---

# 打开A页面但是跳转到B页面了？有可能是这个原因

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QJTLZsy5trHyicNGyvD4uoT8k5RFM5syE6Fj3P1iachmGDZ19oRueGGEjpOp1GicQicdA6jBwrcMcVodfialRtricAEWzcvJibkmKCvdt2TiaNZEBibw/0?wx_fmt=jpeg)

# 打开A页面但是跳转到B页面了？有可能是这个原因

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# **免责声明：******严格禁止**对任何未授权系统/网络进行扫描、攻击或入侵。 禁止制作/传播恶意程序，禁止参与任何网络犯罪。如擅自将本文实验技术用于非法用途，一切法律后果及责任由行为人独立承担，与作者无关。******

# **浏览器劫持事件处置**

## **实验目的**

掌握windows下驱动级病毒处理过程

## **实验环境**

一台windows server 2012 r2 ，浏览器被首页劫持。无法更改。

## **实验原理**

通过驱动级工具，发现驱动级病毒。清除病毒，恢复系统。

## **实验步骤**

#### **一、观察劫持现象**

1、打开桌面上的chrome浏览器

发现浏览器首页域名为hp1.dhwz444.top

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGkPlXtZ0UA9wPUo5PRp4WuP3k5ZO1sekGR57mseS6hed2U0l8icczkiaN1fOGgESxPUiaHLas5RScib2cmhRvyNaiczicE87btNnVR0/640?wx_fmt=png&from=appmsg)

 然后快速的会跳转到 hao123.com

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trH99T8DpPm1M1GdXp3bVaVIAJDsgSIhce68XxgMM1pTHVnvAiaMO05kUQ8EFYODFBLLG6R2jAQVbXiaESxwsf5n57iaNmf51cQRC4/640?wx_fmt=png&from=appmsg)

2、打开IE浏览器

点击开始

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFpLI12KiauIOI5ySKc86xfIib21vico7aLaNfeez81eSagUqqyiaicmSuOibSlNkXgR0xXeQpYFWxoftRXYmA9A5JF6MpZcx1UhEn9Q/640?wx_fmt=png&from=appmsg)

点击IE浏览器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFTEibO428ADHJrzLyibq5HbZK5Q4aIYeUnEBTtVlALwmUXRAoZe4vQlImHWavPECAicdTbUib8pEAkcGDgNTDQkBGJDxIz8ib0nRwU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEic9oMIsaAib7ibz9S0ianiabk0iadbibZBfoQvpicoQndnJWWyxzqjT5bGInc3f9jxWEpYO3cGbL4reEicLicnAuEFXwls3Z5FMHzX25FE/640?wx_fmt=png&from=appmsg)

发现首页同样被劫持

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trE0rAfxlOT5SyGI8szJnkp0iakQK0YOkbXha5ucNvRn8UBFUFbIFzRBGXcffHNRGV2dovm1MUfOK4UarSicexpFZwZD4WvgnBprg/640?wx_fmt=png&from=appmsg)

#### **二、尝试手动恢复浏览器首页**

打开IE设置

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFHhjFAsTC3XujPdJ50dlggmEUcA8vsEIJEr0dSKKp2ho8zW6EEPVHpSxmAzSYIlCg8WCNyCEibbPo7wnRbnKMm5LAyaYX6icLPo/640?wx_fmt=png&from=appmsg)

选择Internet选项

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGrGeMYEUYq7Y6aEc1jJo3XFqXaibyXevXIyWwzsIFSicpABFA0Pwiamoia9gNicGWfEsrREYTcYgt68cxrz4FFYhp4ibJssXJS0EOy8/640?wx_fmt=png&from=appmsg)

使用新选项卡

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFWF9V9LLTIlrpdOZ1S5nBMXpkyiajn7egOj2tKpqcyEicoD7QKM0teKpmXZuIK7cqiciakPfh0VHpshNUJKk6ia1ZDicaGR8r0jz5mU/640?wx_fmt=png&from=appmsg)

关闭IE浏览器

再次打开IE浏览器，首页依然被劫持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trG4604HAN6FFOD8l3V016D8YuEdN22d3E6iaibmsibLWLFeI5z0xlwNs4T5Qa5cBhPoUicQicRDhIaZN3MicIB8opXvJQicFOhqic3tW2k/640?wx_fmt=png&from=appmsg)

#### **三、检查系统驱动**

1、使用微软套件autoruns工具

打开桌面tools文件夹，打开autoruns64.exe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFRd4ltblaYNxSwgicHq8ed7Te9oxjliaPNgbViaD7tYg8xNZQ5aHfJE9StCXOGeZjwBUbkH0DZGTsLFlLYgiaz1ibWWUN0qE3bI4icI/640?wx_fmt=png&from=appmsg)

同意申明

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trH5Amia5kgCryguaYLd3VRdoBdIkUf9ic77NySHrunOkicw1uuVZCUqiaU9iczRt0z5IlPFZCskpwrVrXBgfsrVE08lrcg69k60bhqI/640?wx_fmt=png&from=appmsg)

autoruns打开后会列出系统所有的开机加载项。**重点关注红色项、黄色项，或签名有问题的项**

如图，红框，标注的部分，显示为（Not verifiedt）Microsoft Corporation，说明这两个声称是微软的文件，但并没有获取微软的签名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFYtzD4L2hxpK6mT0Ns8KVamYLXWcOp4NJoiaUCibqicvNGQMSDqHYrABft0iby8aeRaFXo4v0dlZpEhzbBm6OarwBiaxVoAbj5BEWg/640?wx_fmt=png&from=appmsg)

尝试删除这两个文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEBrnDqHEkWb0l6oeVtp40OBnyndL5WGibhF5IdypvoFyEqshXb8FazhMzMwnf00hffIIKAZZAHVUvgTet0unGcavoLic4DXichkg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEpicCybx6xc5dp5cSoLIia21ClFiaDDnev5YU74AZrFqe1OmNA6Ge2AqQVkrlVx2lib4RwUahfxvCxnwsQYUZfKNUmdoy1JWliarfM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trERxuh7Dicuu6HbOVdR1ib8uuPMs3ayZ92HiaGfIvQl1vnXT7qicumqkq70QkfBmibE3fhWmFcTLXOr6Tb10GGBNNtAcY9X47Dy55e0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHJ5Qlevl1iaKXf5VczTiaKpkBSZ37DgkOMlVKicKAbyYdiaoPzznUMO4MibBcUOSDyW1WkInbnczJgtPSNqrNE4rxEyjeb3GLR15a0/640?wx_fmt=png&from=appmsg)

删除后刷新页面，发现这两个链接仍然存在。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFXibGUItTyIKMJskNKIG6ic16JhZUNQoBvepJAKYQpa5moll7Du17b1D2FNTFzQJd2WbuCP4V3d1lXqmNTqc7fsEa9hUWqGHTZc/640?wx_fmt=png&from=appmsg)

再次删除，提示标记为已删除

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFBbxXJzWIibmZhTnXbFBneIvTjfe6MQ1mJGWDYOQuhIBNzfyqGxXV9HyNBnfhKFD8ibEF5x0RNqot63SwmOKg31U0YQ0xFac2ZI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trH087gU2GKcg3vmuuHVic3lXibKRiazaCz5zG9PkZuuq7DbNYbJQhsqMM3P0m8IQwTnt5gMfmD3Uictzdia2q0tR2abUBTfspLOhK30/640?wx_fmt=png&from=appmsg)

#### **四、重启计算机，看能否删除上面两个驱动级服务。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHSCXR9bx6fbdGXlaarvPKz2PVuanW0lcLOktSgEoZdwzrVHk7pyp6WQGCoVKsVPnKn8EdgiaialybIPO1O9qCW5ltcG6Tpv1qVc/640?wx_fmt=png&from=appmsg)

再次打开autoruns ，观察发现仍然存在这两个服务。可以推定这两个服务一定是“非正常的”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGobsY2MC4icIQPJZmRoRrsohyjE6bgwCOyeCWxJcHoZzleB30tUOS5gCeMtKGcy6l90ic1Pndc03eGfq5EafqHLl68RyfBzEbeQ/640?wx_fmt=png&from=appmsg)

#### **五、尝试删除文件**

右键，选择jump to image，打开文件路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGOxwmCcHPNzQ9Gnn4R2fFY2UU658NMibRDBPFWfeQYDMzDuVMKOTatWcNnia0BnyZybGUvwQefWxVhplUL40oia9sEosh71sOcls/640?wx_fmt=png&from=appmsg)

发现无法直接看到文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trH13qgJibTssK5Mq1jHv6dqzR0jmgHO9uufu50o3iaicTus8CuP74psmgPMrgyzRMjeqtPpOkCj4PtGfSMrvMM0ccDwo7MH8bxBrk/640?wx_fmt=png&from=appmsg)

打开windows的隐藏文件与系统文件显示

查看选项

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trF7eYzHXzRGqqMXy3p78iaRm1NR3UIJrYwL79ToHNMqTyzicR27sgzSyAk2JNxNcbbYt1B0Axc0JmDusm6JsiaxXZQQC8F4yKEzUQ/640?wx_fmt=png&from=appmsg)

如图设置

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFKnEMcblnH4IEonMD2QJfcsbuqdHpyLE3JVs0TEQTeALY9qfCLCbA12T0c1PibQ5icqkFrl7KNAOLcTqZXRC0icsXcUGCGuAaqhc/640?wx_fmt=png&from=appmsg)

文件夹仍然为空。

此时可以断定此驱动服务为恶意程序。且hook了系统的api,隐藏自身。

#### **六、使用驱动级工具PC HUNTER进行对抗**

打开桌面PCHunter工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFaIASiaHPvMOBK6sticxMIvJ10iamoGyRqhoQE1BwzWsH8BM5XkjiaMibBJbYs1ZsWhsIENCNrgtDWQ00OPqdSfnOQ9KFMoRurmvlA/640?wx_fmt=png&from=appmsg)

查看驱动模块

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGgPZZDiaVsAWk1HRTr2MwEpjQMNSPS11iafiaW3htNhXibTOuuwRhZBnvUoJicqoHIYLQEaPIofMau8gm6RqXCYlPYEvpGfZcQnVAA/640?wx_fmt=png&from=appmsg)

可以发现PCHunter 检查驱动模块时，并没有校验签名，只是查看了文件信息。

记住这两个文件的路径，C:\USER\Administartor\AppData\Local\Microsoft\WindowsApps\

浏览文件，定位到这个路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trG9IlTqYYNAtzRHpoSiaZa1BcosnFEgqXhufK98hNRQ2ib6LEaAhf2oCSgA07OfcCBTH3P6UFAKPADfR0kZPRvk9NTnWaD39Y6CE/640?wx_fmt=png&from=appmsg)

删除文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFwmcyPgp7CichdkfPYWBjdh3QxvZUnlicUA2s26RZkRQyXwLOFXKfianTWzMvibc4BrGEia1PGMn2mTYSic6K2zGRFzF8jMUn4Kyquo/640?wx_fmt=png&from=appmsg)

观察发现无效，选中文件后，右键“删除后阻止文件再生”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEH40o2K6dTaNibKlSwF0ico1rH6U0X9dSe0ia2pBP87FuiagxhGnHaYr2bzDffZd8Icv0uibqZcBibMCQxule1soQZIs9rgzh21icVbM/640?wx_fmt=png&from=appmsg)

强制删除

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEzUrxsvS6tyfvHz92TgLreXwjI6FnZj7Xu6rMNTUibvGxnsQhfHHJj3aLNNicCATpr2wFNpS7Aruo7V61ggLeibkPqPwJvEAInfw/640?wx_fmt=png&from=appmsg)

强制删除目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHy1wPo40lNv7q2sicZJel5h3vWjA0nSco4DR3yBuvBicd6UeJhBzLkKMUKE2IV3RhM0eoMRP6U9VnoZOkYKmsvI2J0lJEiauLAlk/640?wx_fmt=png&from=appmsg)

再次重启系统。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGahe1gPqyqsD6TVUUVRMBdwUxXzz29ZKFR72fZwaKYluXiaeGLqKjtb3k1etdCgIibO8eLNdFh8R2gN9JKPCLauzKvvLpSz3DW8/640?wx_fmt=png&from=appmsg)

打开IE浏览器或chrome浏览器，首页已经恢复正常

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trESXq6kgltnGnSEVk374S9fcKIr6qbjHBcsTGVicAfQCWKdDMyrg6e3WQSUuUwBPMiaK9lcqM8Dic9BV3TaiaWsriapTSfpRQX4BHFA/640?wx_fmt=png&from=appmsg)

**到此，我们解决了病毒的释放驱动，及其启动文件的删除。**

接下来，进行注册表信息的清理，因为已删除相关文件，病毒对注册的表保护也没有了，直接删掉即

打开autoruns,删除相关注册表信息即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGBVVgkS5rptOuKZJUWO2OTXXeYIfMAdUnDB6iasgvqLXJibz2q062iaZdUqL...