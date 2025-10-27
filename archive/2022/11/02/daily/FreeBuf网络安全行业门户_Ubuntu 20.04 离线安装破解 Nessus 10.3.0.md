---
title: Ubuntu 20.04 离线安装破解 Nessus 10.3.0
url: https://www.freebuf.com/sectool/348481.html
source: FreeBuf网络安全行业门户
date: 2022-11-02
fetch_date: 2025-10-03T21:32:29.637345
---

# Ubuntu 20.04 离线安装破解 Nessus 10.3.0

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Ubuntu 20.04 离线安装破解 Nessus 10.3.0

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

Ubuntu 20.04 离线安装破解 Nessus 10.3.0

2022-11-01 16:10:37

所属地 浙江省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## ****起源：****

自己由于学习漏扫需要安装Nessus。在网上一直没有看到Ubuntu上的Nessus (Pro)破解教程，于是仿照已有的Linux上Nessus破解教程（主要是Kali上的Nessus 8.15版本）进行破解，在过程中踩了几个坑。Nessus在Ubuntu上的发行版和Kali上的不同，所以破解过程也略有不同。现整理出一套破解教程，供大家用于学习和研究。

破解时间：2022年10月20日，所用安装包是目前最新。

破解成功预览：

![1666582534_6356080633d6efc9cebc9.png!small?1666582535474](https://image.3001.net/images/20221024/1666582534_6356080633d6efc9cebc9.png!small?1666582535474)

![1666582544_63560810a036e8d77c512.png!small?1666582544534](https://image.3001.net/images/20221024/1666582544_63560810a036e8d77c512.png!small?1666582544534)

![1666582550_635608162aa5a93082ca3.png!small?1666582550155](https://image.3001.net/images/20221024/1666582550_635608162aa5a93082ca3.png!small?1666582550155)

## ****特此声明：****

本文仅可作为学习和研究使用，禁止被用于任何商业活动！由于读者传播、言论或操作带来的经济损失和政治责任，与本文作者无关！转载需注明来源！

## ****准备工作：****

1. Linux Ubuntu 20.04 操作系统
2. 至少5GB存储空间
3. 开启翻墙，科学网上冲浪

4. Nessus 10.3.0 Ubuntu amd64 发行版，或其他版本，建议选择最新发行版

下载地址：<https://www.tenable.com/downloads/nessus>

5. 注意：安装和破解过程不需要重启电脑/虚拟机，在安装破解过程中，请勿断电、关机或重启。

## ****疑问解答：****

1. Nessus 官网上同时有10.x和8.x 两代发行版，并都标为最新版，我该选择哪个？

选择10.x版本。

网上很多教程是针对8.x版本的破解，在10.x上并不适用，但是本作者亲自摸索出一种破解方法，对8.x和10.x版本都有效。

关于两代的区别：10.x版本包含更多设计，且提供更多平台上的支持。出于历史和法律原因，Tenable必须对Nessus 8.x 版本提供相当长一段时间的支持。所以官网会出现8代和10代同时有最新发行版。

2. 我的电脑（虚拟机）是其他系统，可以用此教程破解吗？

Linux 都可以，破解过程基本相同；Windows作者还没有试过。

## ****运行环境：****

Ubuntu 20.04，我这里使用的是 VMware 虚拟机

虚拟机VMware安装Ubuntu 20.04教程：

<https://blog.csdn.net/weixin_41805734/article/details/120698714>

## ****安装教程：****

1. 在准备工作中，我们获得了Nessus安装包Nessus-10.3.0-ubuntu1404\_amd64.deb（或你下载的版本），放在Ubuntu的任意文件夹下

![1666582577_63560831c1ca1615df40d.png!small?1666582578553](https://image.3001.net/images/20221024/1666582577_63560831c1ca1615df40d.png!small?1666582578553)

2. 在Ubuntu中安装Nessus-10.3.0-ubuntu1404\_amd64.deb

首先切换到root用户，然后执行dpkg -i Nessus-10.3.0-ubuntu1404\_amd64.deb

![1666582581_635608355d6305108e179.png!small?1666582581922](https://image.3001.net/images/20221024/1666582581_635608355d6305108e179.png!small?1666582581922)

3. 安装完成后，启动Nessus

/bin/systemctl start nessusd.service

该命令无回显

![1666582594_6356084208004224694c9.png!small?1666582594189](https://image.3001.net/images/20221024/1666582594_6356084208004224694c9.png!small?1666582594189)

4. 访问网址https://localhost:8834/，注意：Nessus使用SSL协议，所以必须加上前缀https。这里浏览器提示我们有安全风险，我们点击“高级”，再点击“接受风险并继续”

![1666582597_6356084586cd68973bb73.png!small?1666582597560](https://image.3001.net/images/20221024/1666582597_6356084586cd68973bb73.png!small?1666582597560)

5. 可能会需要初始化一段时间，初始化完成后，选择Managed Scanner，点击Continue

![1666582602_6356084acbb6faf73fa82.png!small](https://image.3001.net/images/20221024/1666582602_6356084acbb6faf73fa82.png!small)

![1666582611_63560853b5669a299e66e.png!small?1666582611821](https://image.3001.net/images/20221024/1666582611_63560853b5669a299e66e.png!small?1666582611821)

6. 在下拉列表中选择Tenable.sc，点击Continue

补充：sc为Security Center，Tenable.sc为Tenable Security Center，包含功能设计最多，因此选择该项

![1666582617_63560859a97eb9717afe1.png!small](https://image.3001.net/images/20221024/1666582617_63560859a97eb9717afe1.png!small)![1666582627_635608634bf400ccad46a.png!small?1666582627269](https://image.3001.net/images/20221024/1666582627_635608634bf400ccad46a.png!small?1666582627269)

7. 创建账户和密码

![1666582633_63560869dc6a5aaccc60e.png!small?1666582635230](https://image.3001.net/images/20221024/1666582633_63560869dc6a5aaccc60e.png!small?1666582635230)

8. 等待初始化，这个过程耗时几分钟

![1666582640_635608703c83a6f2f6742.png!small?1666582640490](https://image.3001.net/images/20221024/1666582640_635608703c83a6f2f6742.png!small?1666582640490)

9. 初始化完成后，输入刚才创建的账号和密码，登入Nessus

![1666582646_6356087654a60973257b0.png!small?1666582646074](https://image.3001.net/images/20221024/1666582646_6356087654a60973257b0.png!small?1666582646074)

可以看到，Nessus并没有为我们提供Scan功能，而且Plugin Set为N/A，即没有插件集，下面开始破解。

## ****破解准备：获取离线license和插件包****

1. 获得Nessus软件的挑战码

/opt/nessus/sbin/nessuscli fetch --challenge

![1666582696_635608a89191a0c68ebd8.png!small?1666582696239](https://image.3001.net/images/20221024/1666582696_635608a89191a0c68ebd8.png!small?1666582696239)

2. 在官网上获得激活码，这里需输入邮箱，邮箱可反复使用

<https://www.tenable.com/products/nessus/nessus-essentials>

![1666582699_635608ab81adee3813ddd.png!small?1666582699234](https://image.3001.net/images/20221024/1666582699_635608ab81adee3813ddd.png!small?1666582699234)

![1666582701_635608ad36069cdabf228.png!small](https://image.3001.net/images/20221024/1666582701_635608ad36069cdabf228.png!small)

3. 访问网站<https://plugins.nessus.org/v2/offline.php>，在其中输入刚才获得的挑战码和激活码，点击subimt，获取license和插件包

![1666582726_635608c62d4617b0ef481.png!small?1666582725848](https://image.3001.net/images/20221024/1666582726_635608c62d4617b0ef481.png!small?1666582725848)

![1666582727_635608c7b7eb47f94ce72.png!small?1666582727550](https://image.3001.net/images/20221024/1666582727_635608c7b7eb47f94ce72.png!small?1666582727550)

4. 这里提供了两个下载项，上面的是最新插件包all-2.0.tar.gz，下面的是license文件nessus.license，把他们下载并拷贝到Ubuntu的任意文件夹下

![1666582730_635608ca611a3c54a6da4.png!small?1666582729971](https://image.3001.net/images/20221024/1666582730_635608ca611a3c54a6da4.png!small?1666582729971)

## ****破解教程：****

破解任务：

我们虽然安装了Nessus，但是Nessus并没有为我们提供扫描功能，所以我们的破解要完成：①绕过在线认证，获取扫描功能；②解除其他限制。

1. 停止Nessus服务

systemctl stop nessusd.service

![1666582754_635608e29188272d2340e.png!small?1666582754212](https://image.3001.net/images/20221024/1666582754_635608e29188272d2340e.png!small?1666582754212)

2. 离线注册

/opt/nessus/sbin/nessuscli fetch --register-offline /yourpath/nessus.license

其中yourpath为之前获得的许可文件nessus.license路径

![1666582757_635608e531c3e14b51320.png!small?1666582756848](https://image.3001.net/images/20221024/1666582757_635608e531c3e14b51320.png!small?1666582756848)

3. 离线更新插件

/opt/nessus/sbin/nessuscli update /yourpath/all-2.0.tar.gz

其中yourpath为插件包all-2.0.tar.gz文件路径

![1666582759_635608e781d04861a2457.png!small?1666582759154](https://image.3001.net/images/20221024/1666582759_635608e781d04861a2457.png!small?1666582759154)

4. 设置刚才下载的插件只读，该过程执行时间稍微有点长，因为插件数达15W+

find /opt/nessus/lib/nessus/plugins/ -name "\*.\*" | xargs -i chattr +i {} #设置plugins全文件只读

![1666582761_635608e99f6849df306d3.png!small?1666582761381](https://image.3001.net/images/20221024/1666582761_635608e99f6849df306d3.png!small?1666582761381)

5. 取消插件目录下plugin\_feed\_info.inc文件的只读

chattr -i /opt/nessus/lib/nessus/plugins/plugin\_feed\_info.inc #取消inc文件的只读

![1666582763_635608eb79810b413e69d.png!small?1666582763142](https://image.3001.net/images/20221024/1666582763_635608eb79810b413e69d.png!small?1666582763142)

6. 查看插件集信息

cat /opt/nessus/lib/nessus/plugins/plugin\_feed\_info.inc

![1666582775_635608f7d252f889392f3.png!small?1666582775534](https://image.3001.net/images/20221024/1666582775_635608f7d252f889392f3.png!small?1666582775534)

记住里面的PLUGIN\_SET的数字

7. 编译配置文件内容

vi /opt/nessus/lib/nessus/plugins/plugin\_feed\_info.inc

将内容修改为：

PLUGIN\_SET = "XXXXXX";

PLUGIN\_FEED = "ProfessionalFeed (Direct)";

PLUGI...