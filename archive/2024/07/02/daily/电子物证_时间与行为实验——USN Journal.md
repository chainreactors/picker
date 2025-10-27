---
title: 时间与行为实验——USN Journal
url: https://mp.weixin.qq.com/s?__biz=MzAwNDcwMDgzMA==&mid=2651047616&idx=2&sn=492233eff608e2311e65a985682ca0f5&chksm=80d08931b7a700270e982354760218e8f55155c063e823a958f0e7488438321f0d897bb0a841&scene=58&subscene=0#rd
source: 电子物证
date: 2024-07-02
fetch_date: 2025-10-06T17:45:57.361567
---

# 时间与行为实验——USN Journal

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dDhDhftpRFuGnZ1AjXz91fiauzRBWEXEgNInQeVdqQZ9mZciaHRD07Riaz3d443O3t6I9AIK1t5HfoqxvTpq1PtLw/0?wx_fmt=jpeg)

# 时间与行为实验——USN Journal

电子物证

以下文章来源于法律人的微实验
，作者曾善美

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5pBmURQwu9w6O3qPB4Jlq7uzBiaPia5Wl7R4hUH3JjCumg/0)

**法律人的微实验**
.

法律中的技术，法律人的微实验

![](https://mmbiz.qpic.cn/mmbiz_png/3HB9HkhOZE6ia1uqqUVU8lW5NcibymMwGfPo7faxXmng4L1R0JjrTI4Jvia1wLbpsyy3JnWeziajq0Vic5Z19miarIOw/640?wx_fmt=png)

大家好！今天的小课堂又开始啦！

前面介绍了电子文件的各种时间

今天我们来讲讲**USN Journal时间与行为实验**

一起来看看吧！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kibet0icEt5EVDMZ7qrWhqwhkr6k5zOe8xBicbQsicepEteiasFjzNTkSN7Xb0cqFRRTA20sZRLvffiaWa4FcYuNB5Ow/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/3HB9HkhOZE6ia1uqqUVU8lW5NcibymMwGfPo7faxXmng4L1R0JjrTI4Jvia1wLbpsyy3JnWeziajq0Vic5Z19miarIOw/640?wx_fmt=png)

**Windows NTFS USN Journal介绍**

微软发布Windows 2000时，建立NTFS 5.0的同时，加入了USN Journal ( Update Sequence Number Journal ) ，也称作 Change Journal。

每个 NTFS volume 对应一个 USN Journal，存储在 NTFS metafile 的 $Extend$UsnJrnl 中。

当这个功能启用时，USN Journal 会记录文件和目录的创建、删除、修改、重命名和加解密操作。

Windows 7/8/10下，C盘的USN默认启用usn journal。

![](https://mmbiz.qpic.cn/mmbiz_png/3HB9HkhOZE6ia1uqqUVU8lW5NcibymMwGfPo7faxXmng4L1R0JjrTI4Jvia1wLbpsyy3JnWeziajq0Vic5Z19miarIOw/640?wx_fmt=png)

示

例

**查看USN是否开启**

以管理员身份运行cmd，执行fsutil usn queryjournal c/d:   命令，即可查看USN日志是否开启。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibet0icEt5EVDMZ7qrWhqwhkr6k5zOe8xK0nO2YZQxYoIDszJ46Yaxf7Qic5dVxibJgR446n3oibJpxAkAjHO5ZHgg/640?wx_fmt=png)

**如上图命令结果所示，C盘开启了USN日志，D盘未开启**

![](https://mmbiz.qpic.cn/mmbiz_png/3HB9HkhOZE6ia1uqqUVU8lW5NcibymMwGfPo7faxXmng4L1R0JjrTI4Jvia1wLbpsyy3JnWeziajq0Vic5Z19miarIOw/640?wx_fmt=png)

**usn journal深入理解**

**学习内容**

通过usn journal理解：目录、文件、快捷方式的创建和删除过程、时间、关联性。

**实验一**

1. 在C盘（因为C盘开启了USN日志）根目录下，创建一个目录，命名为zuel58

2. 在zuel58目录下，建立一个TXT文本文件，命名为58notepat.txt

3. 打开58notepat.txt ，输入123456，保存，关闭

4. 删除58notepat.txt

5. 删除zuel58目录

6. 清空回收站

**实验分析**

**Step1：****调用xways，创建案件，添加存储设备——逻辑磁盘C盘（注意磁盘快照中，选择解析文件元数据，包含对$UsnJrnl:$J解析、预览的功能）**

**注意：没有xway时，可以直接分析网盘中提供的实验usn journal日志文件**

**Step2: 在$Extent下找到$UsnJrnl，再双击进去找到$J**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibet0icEt5EVDMZ7qrWhqwhkr6k5zOe8xrcKE3CZlyIEcBUrtXrqqSDIaAZE4shrNUGxjwibZa56wibyR0NdnXHDg/640?wx_fmt=png)

**Step3. 预览$J文件，通过快捷方式CTRL+F在文件中搜索，总结如下相关日志内容。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibet0icEt5EVDMZ7qrWhqwhkr6k5zOe8xs1JKjzbydgKmOCxBq0sgFFpFT3VXiavK6RLMu8Q2jPB06GPZOp26NpA/640?wx_fmt=png)

**回收站的工作方式，请结合推文：[回收站的工作原理及故事](http://mp.weixin.qq.com/s?__biz=Mzg5NTIxMTY2MA==&mid=2247484670&idx=1&sn=90a31901ab09dcbf7c5999cb7d3524c6&chksm=c012851df7650c0b2d36edaac3918085f57f8754afdd23cffedcf21d7659f0990a6b1380ff43&scene=21#wechat_redirect)  同步理解。**

**快捷方式的工作方式，请结合推文：[快捷方式中的时间](http://mp.weixin.qq.com/s?__biz=Mzg5NTIxMTY2MA==&mid=2247484681&idx=1&sn=2b85b4ec5ea6c560d48f77cda306ccba&chksm=c01284eaf7650dfc9bc87226164b054b6496114de3e70b918512b0014dc0ca16ec4ba8612489&scene=21#wechat_redirect)   同步理解**

**Step4. 总结**

 通过该实验，可以了解文件夹/文件在新建、编辑、删除等操作过程中的生命周期

![](https://mmbiz.qpic.cn/mmbiz_png/3HB9HkhOZE6ia1uqqUVU8lW5NcibymMwGfPo7faxXmng4L1R0JjrTI4Jvia1wLbpsyy3JnWeziajq0Vic5Z19miarIOw/640?wx_fmt=png)

**时间的应用案例**

**Windows ntfs系统usn journal的应用**

1. 获取文件的历史操作记录，即使文件已被删除；

2. 确定文件的创建、删除时间（各种文件的生命周期）；

3.  辅助排除非法证据 。

**故事：排除非法证据（发现造假行为）**

**实验内容：**
     **通过$UsnJrnl日志分析特定文件（myfile.xlsx）造假行为。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibet0icEt5EVDMZ7qrWhqwhkr6k5zOe8xuOSDlGibBxzn9HnQt4C1UQ7MbQplRGcODfA7lO6bhZyYxdt9Cv1Cz4w/640?wx_fmt=png)

【图片来源：郭永健老师PPT】

**实验分析：**

**观察如上USN Journal日志，正常的日志记录时间顺序的**，图中的日志从2022年突然跳到2015年，又回到2022年，此为异常，可以推断系统时间有修改的痕迹（系统时间应该是从2022/06/15日修改至2015/07/13日）。

因此，2015/07/13出现的myfile.xlsx文件创建痕迹不正常。

今天的推文就到这里啦

关于usn journal的知识点可不止于此哦

大家快去探索探索呀

我们下次再见哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dDhDhftpRFuouuxbQ44msKkdjic0C8WOQrHEN6rex1hiblHTTIpApR8safvHvB9zXorQTMStvvyN2zO8xjOJd5vg/0?wx_fmt=png)

电子物证

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dDhDhftpRFuouuxbQ44msKkdjic0C8WOQrHEN6rex1hiblHTTIpApR8safvHvB9zXorQTMStvvyN2zO8xjOJd5vg/0?wx_fmt=png)

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