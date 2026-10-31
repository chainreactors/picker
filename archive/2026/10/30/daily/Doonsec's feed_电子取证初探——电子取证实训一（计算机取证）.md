---
title: 电子取证初探——电子取证实训一（计算机取证）
url: https://mp.weixin.qq.com/s/svCfOAHoWucN1mro3npl-w
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:44:40.367607
---

# 电子取证初探——电子取证实训一（计算机取证）

# 电子取证初探——电子取证实训一（计算机取证）

原创

是羊羊羊呀
是羊羊羊呀

羊羊羊的forensic

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

检材：Evidence.E01

取证软件：

1、X-Ways Forensics

第一题：在镜像Documents\Contacts.txt中记录的电子邮箱地址是什么？

使用X-Ways Forensics打开镜像文件，如下图。

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUTyQyq5JgrIicdLDsWNyxNNjQ9ccjbqfwTnjviaom4JyvwMsLUrSjH952I9gGT7OSNDMhn6R5skEribqhmS0JE3qeOn88FIoJ3B0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUrVfU7ia2icTeP4KtTIAufT0y9DmgYXNx7uChug1nRCiafXibSh8Phxvzu2Vnxgzy1iaELSCKQVecuxErzXj504S7gSwibWyt7ChHlY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwURjLGia0Yibvjy9p1BlZBngQc4Ieaaw5M0rgQjOziazVWAbw84dyR91dh7g1BmNWMWVzt9FJHO5nL6M4S19AjU8cv1pCiaOPbK3t4/640?wx_fmt=png&from=appmsg)

但是现在我们只能看到整体的镜像文件的十六进制信息，我们需要将镜像文件转换为可以读取内部文件的磁盘的形式。

点击将镜像文件转换为磁盘(A）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwVS2Q1TohQZIFKucYNCCxribib8Oy4ftaJfdyyC1ibY6Ucv5glG3PXTybPBWFxuQv1YlvpFowkUeEeNNpxJdf7jowGAD4pCwM980k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUYv3HvqE8JibfCUupfU8P0IxZeQXqvGTg7KvOSdTbNPjBuiaBHIibDvcz5ZH6BdqJt4LwFciceMsNseR3Gzytzj3AcIMh0wBGOgib0/640?wx_fmt=png&from=appmsg)

可以发现，镜像内部的结构已经明了，我们可以进入所有分区进行取证。

根据题意，我们需要找到对应的文件。Documents文件夹是Windows的常见路径之一，我们需要找到对应的Users文件夹下，即可顺利进入目标文件夹，找到文件。

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwV26snl0eQ5uCWGicTceLI7dZ33Uq7SGe7sE9Wb72daDNiadAiaibXWene2r0e9WiciaDI2d9D7pxuXeGQPA81619qt13v9wvzJbTqu0/640?wx_fmt=png&from=appmsg)

右击目标文件，选择Notepad打开，即可获得答案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwVHd207ULXGb17DXPAibfMdOX99PhkDGWBQicN7BWHE6bia52KiaOzIiae5SdoHXCyWVV70x0zofcKhoCSCUEYlcJQZhtGuQmEOGBTQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwXibdEDOznXTke8UvnfQkTF8R5QYOeN2fGKpHzq3iaZ9WGtITEWL4OFrg8YqiacTE14sgpFusmpYicHJ1iaO92RHt1mCIoZCzGRwyGo/640?wx_fmt=png&from=appmsg)

所以，第一题的答案是：support@police.cn

第二题：在镜像Images\Vacations.jpg的属性中，相机型号是什么？

与第一题同理，找到常见的图片文件夹即可获取目标文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXTKUePrGgMP7fwHb4fflYqlLEV3KV0mOniavS7Crsrg6V7zo3jy09oxVUktxlV5gLCUS7aBMq7SMgTeCrkSdiaH6gibzI8UicRFaY/640?wx_fmt=png&from=appmsg)

点击“详细”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWwy8lWuBjdficOcMVbZDDGoc8OSlkFnboBCzu4iagW8NT1hqR9QRt4ZefaYGO9KlQeDJg10iaxHQicoY3cgI3QHfelIMCmWhomeko/640?wx_fmt=png&from=appmsg)

就可以知道对应的型号:ZV-E10M2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXDYuLaOfdWUT7Z4c2djaald4ianmicD2sDnOIZULOlTGtVt1kbdqRicJpfkH7Im2oiaGDqrvfwGvDBUPpIamEOIBPKSEm19apKhico/640?wx_fmt=png&from=appmsg)

第三题：在镜像Documents\Report.docx的属性中，“最后修改的作者”是谁？

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwVmIrFSGCBq10yPb0sjFqyj97IOiamQpjoOOdib8Rb1LrpJl4pmbPzxoibeotzDtEgcy8Sp2U3dkFfIak1qAXEib3HhhAnslFYqroE/640?wx_fmt=png&from=appmsg)

用Word打开，点击“信息”，可以看见最后的修改作者。（晚安.）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwVg2S1eSG5gTbBLBCAoy22UjGHIekYLbJs1xYLYP8T9Bd4R2eLXnJ71WXnW4LTtGfRqq28MTPTibCWpymxd0ePZTOJAAZtSwpWo/640?wx_fmt=png&from=appmsg)

第四题：Projects\Secret.pdf的SHA256是多少？

导出文件，使用任意工具计算SHA256即可。

7C147CA7A2551620E374CB79062F3B582D6042D083267365D01B98C35646403A

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXwUkVF5K8EqlK0hVGjDCrJSLPYYCJdFk5kWL0mtG5me9Iu1XgMNDX6JGSwkJeUcyt0XOp3qQjfvwKD9icMZl2RlI5cjdHpgMMc/640?wx_fmt=png&from=appmsg)

第五题：王警官的电话号码？

第一题已找到答案，省略过程

1380013800

第六题：Vacations.jpg的拍摄日期？

与前面的题目同理，点击详细信息可以看到详细的拍摄时间参数。

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUslJ8MyJxE6Z5VQTOmXQW9wia8JribibCJzC0H6PFl8HGfSKPAZy4HfiaNYoia1Y9fgGwI9AeyYZU4tchoUicUibblrxnsQKVibwBxVKk/640?wx_fmt=png&from=appmsg)

 2025:10:11 19:21：20

第七题：Report.docx的创建内容日期？

与上面同理。省略。2025-10-20

第八题：Projects文件夹下（不含子文件夹）有多少个文件？

直接数就行，2.

第九题：第一个分区（EFI System）所在分区的SHA256是多少？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXJcsLRg2M34KRVzMibk39FjthPOCDM7K96Y3hB29dnl95gZkma3qNticxoqEGVUict24zqRRG6q8T3SXHZoib2LDLOI3EkfTeYSUA/640?wx_fmt=png&from=appmsg)

首先，我们进入对应的EFI分区。然后计算SHA256即可。

2B569FD5B63A12B20AE130C0262AF92E6FE4861D41B6E009413CC7CD8950FF7A

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWtn4SD2V5MMpjr63GCaj6DpDhHesrVW9ZH4aJehI8nuPMSEXyVkurj9uSr7wxzTxLqiaMIQficTO0LSHsEFuvJPxMvoxQmkcVFM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwWluEU0b0TqDfhalD3cZZJtgrS39xvvJz3qaKlh01Rggckibn3Dic5Z59bGybSKNywzTUkJrbzh4fsptictKqQhcON4zML9zbAb9o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUxnaAPUxjR3iaKhfNx58IzPlw9AL6icpQkia0uBBdkrTdXaibZNUnqibzRmOS2VZibia8IeCDSGibHyXPwmn60zu5Mpr6nPicWEJbMyyg4/640?wx_fmt=png&from=appmsg)

全部都做完啦，当时实训课还用了好多软件，最后发现一个X-ways就能全部搞定，主要还是对于软件的操作界面不太熟悉~（盘古石和火眼把我惯坏了）

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QWJfTdNVlxVt4bLeuM9MibfrqlR2wMplg7EjKX3SMMjMGFujGDibwrZMiaWK1Sn6j1hNQxjibvI774IKKV68n5zicuA/0?wx_fmt=png)

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