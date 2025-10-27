---
title: 解决win7嵌入式系统无法DoublePulsar问题
url: https://www.anquanke.com/post/id/285776
source: 安全客-有思想的安全新媒体
date: 2023-02-17
fetch_date: 2025-10-04T06:49:50.632368
---

# 解决win7嵌入式系统无法DoublePulsar问题

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 解决win7嵌入式系统无法DoublePulsar问题

阅读量**1057712**

发布时间 : 2023-02-16 17:30:52

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 0x01 前言

渗透过程中总是会遇到千奇百怪的问题，比如前段时间内网横向时用MS17010打台win7，EternalBlue已经提示win了，可是DoublePulsar就是死活一直报错，最后我查阅大量资料，终于解决了这个问题，于是就有了这篇文章。

## 0x02 踩坑

内网横向，扫到几个MS17010能打

![]()

操起家伙对其发起猛烈的进攻，一路披荆斩棘（回车），畅通无阻，EternalBlue成功

![]()

然后后面的剧情就是DoublePulsar一路火花带闪电，啪一下，shell就弹回来了，然而意外发生了

![]()

报了个错 ：`ERROR unrecognized OS string`

## 0x03 填坑过程

一开始我以为是x86x64的问题，试了几次发现还是不行，上网搜了一下，看到一篇文章有详细解释了这个错误，标题叫：《修補DoublePulsar支持攻擊Windows Embedded系統》（自行搜索一下）

看完后感觉顿悟了，`Windows Embedded Standard 7601 Service Pack 1`是win7嵌入式系统，工具无法准确判断出win7嵌入式系统，需要反编译修改源码，但是作者没放出修改版的exe，绝知此事要躬行！

把DoublePulsar拖入ida，位置在：`工具目录\windows\payloads\Doublepulsar-1.3.1.exe`，最好先做个备份以免修改出bug还原不了

![]()

拖进来后界面如上，然后敲一下空格键，找到原作者说的`0x0040376C`位置

![]()

然后右键，选择Graph view，得到图形结构

![]()

从图形中可以看出，如果目标计算机正在运行Windows 7，它将走左边的路径，然后继续检测其结构是x86还是x64。如果目标不是Windows 7，它将采取右边路径并执行其他OS检查。由于没有检查Windows Embedded，程序最终输出错误消息`[-] ERROR unrecognized OS string`

因此只需要将指令`jz short loc_403641`修改为`jnz short loc_403641`来强制程序走左边的路径

Edit > Patch program > Change byte 将第一个74（jz操作码）修改成75（jnz操作码）

![]()

![]()

最后创建一个dif文件就可以保存关闭ida了，File > Produce file > Create DIF file…

![]()

直接保存的exe是不能使用的，还需要用脚本修补修改后的exe，原文作者的脚本链接已经404了，找了很久，这里就直接贴出来了：

```
#!/usr/bin/env python
# Small IDA .dif patcher
import re
from sys import argv,exit

def patch(file, dif, revert=False):
    code = open(file,'rb').read()
    dif = open(dif,'r').read()
    m = re.findall('([0-9a-fA-F]+): ([0-9a-fA-F]+) ([0-9a-fA-F]+)', dif)
    for offset,orig,new in m:
        o, orig, new = int(offset,16), orig.decode('hex'), new.decode('hex')
        if revert:
            if code[o]==new:
                code = code[:o]+orig+code[o+1:]
            else:
                raise Exception("patched byte at %s is not %02X" % (offset, ord(new)))
        else:
            if code[o]==orig:
                code = code[:o]+new+code[o+1:]
            else:
                raise Exception("original byte at %s is not %02X" % (offset, ord(orig)))
    open(file,'wb').write(code)

def main():
    if len(argv)<3:
        print "Usage: %s <binary> <IDA.dif file> [revert]" % (argv[0])
        print "Applies given IDA .dif file to patch binary; use revert to revert patch."
        exit(0)

    file, dif, revert = argv[1], argv[2], False
    if len(argv)>3:
        revert = True
        print "Reverting patch %r on file %r" % (dif, file)
    else:
        print "Patching file %r with %r" % (file, dif)

    try:
        patch(file, dif, revert)
        print "Done"
    except Exception, e:
        print "Error: %s" % str(e)
        exit(1)

if __name__ == "__main__":
    main()
```

然后命令执行修补一下exe

![]()

最后我们把生成的exe拖到工具目录下，重新执行DoublePulsar，完美解决

![]()![]()

公众号回复： DoublePulsar 获取修改后的exe

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**黑客前沿**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/285776](/post/id/285776)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [利用工具](/tag/%E5%88%A9%E7%94%A8%E5%B7%A5%E5%85%B7)

**+1**25赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)黑客前沿

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=167984)

[黑客前沿](/member.html?memberId=167984)

这个人太懒了，签名都懒得写一个

* 文章
* **5**

* 粉丝
* **1**

### TA的文章

* ##### [CVE-2023-0669 GoAnywhereMFT反序列化漏洞复现](/post/id/286390)

  2023-02-17 15:30:42
* ##### [解决win7嵌入式系统无法DoublePulsar问题](/post/id/285776)

  2023-02-16 17:30:52
* ##### [导出域用户hash姿势总结](/post/id/286257)

  2023-02-15 17:30:43
* ##### [小皮面板RCE复现](/post/id/286115)

  2023-02-14 17:30:38
* ##### [实战记录之曲线救国](/post/id/284600)

  2023-01-11 17:30:42

### 相关文章

* ##### [NSIC网络安全智能中心，重塑企业数据安全新范式](/post/id/308646)

  2025-06-23 10:17:20
* ##### [企业安全的工作沟通与交流平台，吱吱守护企业通讯安全](/post/id/307470)

  2025-05-22 14:49:44
* ##### [CVE-2025-25014（CVSS 9.1）：Kibana的原型污染为代码执行打开了大门](/post/id/307127)

  2025-05-07 15:47:13
* ##### [重大升级| SecGPT V2.0：打造真正“懂安全”的大模型](/post/id/306612)

  2025-04-23 10:35:22
* ##### [PolarDB分布式版V2.0：安全可靠的集中分布式一体化数据库管理软件](/post/id/303161)

  2025-03-26 16:07:18
* ##### [DeepSeek本地化部署有风险！快来看看你中招了吗?](/post/id/304555)

  2025-03-12 11:24:50
* ##### [java 代码审计工具铲子 SAST 的使用](/post/id/301382)

  2024-11-12 17:48:09

### 热门推荐

文章目录

* [0x01 前言](#h2-0)
* [0x02 踩坑](#h2-1)
* [0x03 填坑过程](#h2-2)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)