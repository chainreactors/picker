---
title: 2026年最新 Kali Linux 安装教程（附VMware虚拟机安装包和Kali Linux IOS镜像）
url: https://mp.weixin.qq.com/s/JK58WVyIq7vmMk3B8KtgDg
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:02.889677
---

# 2026年最新 Kali Linux 安装教程（附VMware虚拟机安装包和Kali Linux IOS镜像）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbUqDUQYzmfNZfAic8lIgwXkoHElbMwiaw9oPTicjwGTh4CG8jQnerSzWtg/0?wx_fmt=jpeg)

# 2026年最新 Kali Linux 安装教程（附VMware虚拟机安装包和Kali Linux IOS镜像）

原创

W不懂安全

W不懂安全

![]()

在小说阅读器中沉浸阅读

水一期，原本我的VMware虚拟机中装着Kali Linux，但是因为版本有点旧了，导致拉取一些文件经常提示缺少官方密钥，我也尝试过更新系统，但如果不解决密钥问题，执行更新命令会中断，索性直接删除重装，借着这个机会来写一期安装教程。

Kali Linux 是目前最流行的安全测试系统之一，所有学习网络安全的人员无一例外都认识，不认识的出去罚站。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_39@2x.png)

直接在实体机上安装风险较高，也不够灵活。本次就在VMware虚拟机中来进行安装操作，这样不仅安全可靠，还方便快照和环境还原。

所用到的VMware16安装包（含激活码）我已经整理好放到了网盘，后台私信：“VMware” 就能获取到网盘链接。

Kali的IOS镜像因为是IOS格式的，网盘不支持分享，所以需要下载的话，只能是去官网下载了。

```
https://www.kali.org/get-kali/#kali-installer-images
```

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbhF5erfEibRYJhiczaGMNOTfJ6dK8erykoic3wXINXcu9yjIJcHnj9uQeQ/640?wx_fmt=png&from=appmsg)

安装好虚拟机之后，启动。

点击上方菜单栏，找到"文件" → "新建虚拟机"，或者快捷键“Ctrl+N”。

选择自定义，然后下一步。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbKIuTicX0wbgztT89oFNy3dbhcFtrP9t8NCj2IjSpN4SP6V6fK4KAzyg/640?wx_fmt=png&from=appmsg)

直接下一步。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnb36saA5nLyus5mPJ6YYC303t4zGPxcaH23XNULHm4vuyiaeFFplicO0qw/640?wx_fmt=png&from=appmsg)

选择“稍后安装操作系统”。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbKGdaa6434Jic6AUQYA9xwCjgXUS5VO2AbrM872EBxQOAYwYX5IMGZIQ/640?wx_fmt=png&from=appmsg)

选择客户机操作系统这里选择“Linux”的Debian 64位版本，不要选择非64位的，更不要错选操作系统版本。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbNERsFxYuBfYohnbbvBxzvicRGoDbxp21GIKJQcGg1015yFy6CrBJibxg/640?wx_fmt=png&from=appmsg)

命名虚拟机和虚拟机位置，名称和位置不要有中文，磁盘可以选择其它盘。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbyC9QICKNNNCpzPoYrAlja0w170yDX7ngalictsW6FnVoXqWkJvKJ9lA/640?wx_fmt=png&from=appmsg)

处理器配置建议是：2G2核，低的话可能会慢，比较版本一直在更新，系统的工具也在不断变化，其实也用不了这么多，1G1核也可以，只是用起来可能慢点。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbxoXn0dPurKQ1WuaBRI6hMscNWy8CrzjQIZJ252YajKOicibQicl7ibdziag/640?wx_fmt=png&from=appmsg)

虚拟机内存就用默认的 2G。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbVO1Sb81sdoD1ic7g7iasRwiaZjVGFYPA0huTYxu3vaicQCib3ATCvIOVdzQ/640?wx_fmt=png&from=appmsg)

网络类型这里我用NAT，网络类型最常用的 NAT 和 桥接。

* NAT 模式：虚拟机通过宿主机上网，相当于“蹭”宿主机的网络。虚拟机可以访问外网，但局域网内的其他设备一般无法直接访问虚拟机，配置简单，适合新手和日常使用。
* 桥接模式：虚拟机和宿主机处在同一个局域网中，虚拟机会像一台独立的真实电脑一样，从路由器获取 IP 地址，局域网内的其他设备可以直接访问虚拟机，更适合做实验或测试。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbsxOCkkHdyt7KFjCjGUlQr16sxMBsD7VpqnaxrficiavkQjuRgaGWRvQQ/640?wx_fmt=png&from=appmsg)

下方三个图片中的选项都是默认即可，直接下一步。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbl418BiceGshxW5CY40K73tzcN5RgEW8FmeAlSl2Bc1CEiakTJGibiaDPVw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbhiaEklRiaFekFZwlNwNP6r9ZFibaUicQMD4UsiaFmoUHXO5VPkEfPRhyzag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbfN9FUZu6gRH2xLp4Qeg0rKI48uB4dgDxZsfYpQy5HmT3PRwgdyx6ng/640?wx_fmt=png&from=appmsg)

磁盘容量最好不要低于20G，我这里给到50G，因为我分配的磁盘容量比较多，所以多给点，至于下方三个虚拟磁盘的选项，最好选择“拆分成多个文件”。

* 拆分成多个文件：虚拟磁盘会被拆成多个小文件，方便移动、复制和备份，对日常使用影响不大，适合大多数用户。
* 存储为单个文件：所有磁盘数据集中在一个大文件中，性能略好，但文件过大，不方便拷贝和迁移。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbR15G6ArZVPRYQUDJvMBDhpU3gz5kpJPCZVgFl8DK0GiaRUuVhHcXwkA/640?wx_fmt=png&from=appmsg)

直接下一步，不要修改。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbtZrutRro1CFzQNaoZVhPAibn1NsxnnE5GdTprfM7ozpjrwGf6WHefwg/640?wx_fmt=png&from=appmsg)

选择“自定义硬件”。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbMW4MUooK0ysuJtPdxibfQerr6GgGk2JMoN5JfUyV0V7TGxLOJFQAibnQ/640?wx_fmt=png&from=appmsg)

点击“新CD/DVD”，选择“使用ISO映像文件”，然后浏览你下载的IOS包。之后点击确定。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbTVe1HzETmN52I2ZibtBRE9QM8XQF8ybYUMaGPXQWjwaiaBpBSt9iaFZcQ/640?wx_fmt=png&from=appmsg)

启动虚拟机。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnb1x3umjlBiasreug0hkGibalnsal1JmyYHkMJb7LwKdnMcVeF8IaQI5xA/640?wx_fmt=png&from=appmsg)

选择“Graphical install”，意思是图形安装，然后回车。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbsGRg3n3e5R3Ob5bZlhHLra14bN1V67ebFDS2aRWIuYplicicJTSjYyYQ/640?wx_fmt=png&from=appmsg)

选择语言，然后“continue”继续。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbuZozjQy8BWsRaRfQoJ5MAsZZnUvD4JIC1Rg4oaYSjqq8hQjNeicMUag/640?wx_fmt=png&from=appmsg)

继续。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbIN4NpzjGhicz5WoLOJQDicUyibCOyrHovm5IKqg38AwxBGNbMQKoUdktw/640?wx_fmt=png&from=appmsg)

配置键盘这里我推荐选择“美式键盘”。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbjr0FpXjkA1KLt2p2FuykcB4xPLJGZrkNBzbSHlibQdEoQWHRRZgIAcw/640?wx_fmt=png&from=appmsg)

等待扫描安装。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbnW7OGDIjUiaz0123Q8NJRf4N6D6mueuKDjqF4nur9MotlFxTmTJTiaCQ/640?wx_fmt=png&from=appmsg)

主机名自定义，默认也行。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnb1gaibIFv3mAS8ZOibMOeib6UsLzt4nC08S4q1sXfkIEt6G8sufqjWNruQ/640?wx_fmt=png&from=appmsg)

域名这里不用填，直接点击继续。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbYHuicW6UneXTycLUvibBAwgniaJwAFXBoYog4Eic56icX2ByhZe1nlv8S3w/640?wx_fmt=png&from=appmsg)

设置用户和密码，这里让你输入一个新用户是一个普通用户，非root的用户。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbp3C44BU453B1yCdRRNoAMvO2lgHA8PCvMicnA9yM3CoksDQk8JCQV8w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbpnsexSGZexHtBXzszZ76tnD5MvwafkGM07IBvlG4TU4qFgrxFzthXA/640?wx_fmt=png&from=appmsg)

之后设置一个密码。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnblNdP1dGujzQj18yaQoRAuzDSw3icU4HZoGcT66zDFiakLyskJ4vkdphw/640?wx_fmt=png&from=appmsg)

磁盘分区选择第一个“使用整个磁盘”。

* **使用整个磁盘（推荐）：自动完成分区，操作最简单，适合大多数用户和新手，虚拟机环境下直接使用不会有风险。**
* **使用整个磁盘并配置 LVM：在自动分区的基础上使用 LVM，方便后期调整磁盘大小，一般不需要，适合有经验的用户。**
* **使用整个磁盘并配置加密的 LVM：在 LVM 的基础上增加磁盘加密，安全性更高，但安装和使用都更复杂。**
* **手动：完全手动分区，适合对 Linux 分区结构非常熟悉的用户。**

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbBVwj7p733aSFKCSuiaS1VZyib9UCtB2GRicV9d8nicHq8AvQCLI9dvAwkg/640?wx_fmt=png&from=appmsg)

要分区的磁盘默认即可。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbn4JwAjSp5iaPWVU17D5bFXvcjicPWF9uCYJE36z4HXjSLGuOsjZqbiayQ/640?wx_fmt=png&from=appmsg)

分区方案选择“所有文件放在同一分区中”。

* **将所有文件放在同一个分区中（推荐）：系统和用户文件都在同一个分区里，结构最简单，最不容易出问题，适合虚拟机环境和新手使用。**
* **将 `/home` 放在单独的分区：适合长期使用、需要频繁重装系统但保留用户数据的场景。**
* **将 `/home`、`/var` 和 `/tmp` 分别放在单独的分区：更偏服务器或生产环境，管理复杂，不适合新手。**
* **将 `/var` 和 `/srv` 单独分区：同样主要用于服务器场景，一般用不到。**
* **swap < 1GB / 小磁盘 分区方案：适合服务器或磁盘空间非常小的特殊情况。**

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbpaOpzl3SicFtWXs5q4Wo8vq6UC1o7VTn3IuvialxDa6ibiacGHwQVmotPA/640?wx_fmt=png&from=appmsg)

选择“完成分区操作并将修改写入磁盘”。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbTv9KBibO8fLnibeWicjxsnhHP9RiamK4vZ0XQCQJfGzNgBPEib8tqHek3IA/640?wx_fmt=png&from=appmsg)

选择是。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbzIibC5ibia6GgwNEOUbAmb7TfFTictMsQ3EeCATcfUWwxmOkZrMzhosYCQ/640?wx_fmt=png&from=appmsg)

之后开始安装基本系统。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbjoj6sjvn8Bo1OAyAUXOQbycvTWcro4mMSoBHo1lJWlLhOhnxYhzibqw/640?wx_fmt=png&from=appmsg)

软件选择这里默认即可。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnblm0YQOv4xXL1JOu2NlCnHIHkic1kRDrQPhEgmoyJtLPgjicmzQ2JyOxg/640?wx_fmt=png&from=appmsg)

等待安装软件 ing....

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnblLyHG1FmT9u0ADc5ckZvQkTJxb4aalxR3KrZricruPP87gwMFepvKAA/640?wx_fmt=png&from=appmsg)

安装 GRUB 启动引导器这里选择“是”。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1TicicIvdOjrYpLTgrl1DfcXnbGIHv1iaCL4fwKuymlCS4jrXjlKkO5MmH73Uo9fPDsdFCAZhBvLic2JibA/640?wx_fmt=png&from=appmsg)

选择引导路径。

![](https://mmbiz.qpic.cn/mmbiz_png/Y4...