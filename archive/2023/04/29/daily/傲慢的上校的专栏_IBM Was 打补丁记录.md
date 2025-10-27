---
title: IBM Was 打补丁记录
url: https://blog.csdn.net/aomandeshangxiao/article/details/130425908
source: 傲慢的上校的专栏
date: 2023-04-29
fetch_date: 2025-10-04T11:32:39.759205
---

# IBM Was 打补丁记录

# IBM Was 打补丁记录

原创
于 2023-04-28 15:22:56 发布
·
2.5k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

0

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

0
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#linux](https://so.csdn.net/so/search/s.do?q=linux&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#eclipse](https://so.csdn.net/so/search/s.do?q=eclipse&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#运维](https://so.csdn.net/so/search/s.do?q=%E8%BF%90%E7%BB%B4&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

编程感想
专栏收录该内容](https://blog.csdn.net/aomandeshangxiao/category_808037.html "编程感想")

8 篇文章

订阅专栏

![](https://i-operation.csdnimg.cn/images/a7311a21245d4888a669ca3155f1f4e5.png)该文详细介绍了如何通过FTP上传并解压ifph52925升级包，然后停止WebSphere应用服务器（AppSrv01和AppSrv02），切换到root用户进行升级操作。使用imcl命令安装升级包，并在完成后重启服务器以确保升级成功。

0、拷贝解压ifph52925升级包

通过FTP工具，把压缩包传到服务器，

```
unzip -d test01 9.0.0.0-ws-was-ifph52925.zip
```

1、停掉was 服务

```
ps -ef |grep was

kill -9 pid（上面查到was对应的pid）
```

或者

```
---- 停止AppSrv01(地址根据自己实际AppSrv01地址)
/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/stopServer.sh server1

---- 停止AppSrv02
/opt/IBM/WebSphere/AppServer/profiles/AppSrv02/bin/stopServer.sh server1
```

2、切换至root用户

su -root

3、进入到imcl目录下：

```
cd /opt/IBM/InstallationManager/eclipse/tools
```

4.查看可用升级包

```
./imcl listAvailableFixes  com.ibm.websphere.ND.v90_9.0.5001.20190828_0616 -repositories  /home/was/workspace/9.0.0.0-ws-was-ifph52925

--- /home/was/workspace/9.0.0.0-ws-was-ifph52925 为升级包解压路径
```

会看到如下图所示，可用升级包：    ![](https://i-blog.csdnimg.cn/blog_migrate/46654260c64f72b25d38064de37eefe5.png)

5、升级

```
imcl install 9.0.0.0-WS-WAS-IFPH52925_9.0.0.20230320_1005 -repositories /test01/was_905_FP9/repository.config -installationDirectory /opt/IBM/WebSphere/AppServer -acceptLicense

---- 解压升级包地址 /test01/was_905_FP9/repository.config，根据实际地址替换
```

升级成功会有对应提示。

6.重启Was，退出root用户，启动was服务

```
---- 启动AppSrv01(地址根据自己实际AppSrv01地址)
/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/startServer.sh server1

---- 启动AppSrv02
/opt/IBM/WebSphere/AppServer/profiles/AppSrv02/bin/startServer.sh server1
```

启动成功，即升级成功

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/d2d7957684914173b2ea5ac8d23c76be_aomandeshangxiao.jpg!1)

傲慢的上校](https://blog.csdn.net/aomandeshangxiao)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  0

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  0

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

[Kalibr标定单目+IMU 优化时间过长 报错Last step *was* a regression. Reverting反复回退](https://blog.csdn.net/ENXIJJ/article/details/144365051)

[ENXIJJ的博客](https://blog.csdn.net/ENXIJJ)

12-10
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1514

[利用kalibr标定imu+单目摄像头 硬件：3090虚拟机；森云单目摄像头（30hz）；](https://blog.csdn.net/ENXIJJ/article/details/144365051)

[Websphere静默*安装*与*打补丁*](https://blog.csdn.net/deccmtd/article/details/7023986)

11-29
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
4237

[今天远程*安装**安装*websphere的时候网络太不给力了.网上搜了下websphere原来可以静默*安装*.*记录*下来.以备后用.

静默*安装*程序:
先将websphere的*安装*程序上传到服务器,解压出来.
[root@localhost tarbag]# tar xvf *WAS*61\_base\_*linux*64.tar -C ../software/
进入websphere解压目录中的*WAS*目](https://blog.csdn.net/deccmtd/article/details/7023986)

参与评论
您还未登录，请先
登录
后发表或查看评论

[*WAS**补丁*说明,描述了*was**打补丁*的配置过程](https://download.csdn.net/download/zztp01/3451712)

07-18

[*WAS**补丁*说明,描述了*was**打补丁*的配置过程](https://download.csdn.net/download/zztp01/3451712)

[*WAS* ND 9.0*安装*手册](https://download.csdn.net/download/travelskybit/10700456)

10-03

[*WAS* ND 9.0*安装*手册，*安装*配置及*补丁*升级指南之windows操作系统篇](https://download.csdn.net/download/travelskybit/10700456)

[*WAS**打补丁*](https://blog.csdn.net/jackhexl/article/details/83663776)

[jackhexl的博客](https://blog.csdn.net/jackhexl)

06-30
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
641

[*打补丁*步骤： 1，下载*补丁*文件，具体下载地址为ftp://ftp.software.*ibm*.com/software/websphere/appserv /support/fixpacks/*was*61/cumulative/cf61017/AixPPC64/6.1.0-WS-*WAS*-AixPPC64-FP0000017.pak 2，下载*打补丁*的工具，具体下载地址为ftp://ftp.softwar...](https://blog.csdn.net/jackhexl/article/details/83663776)

[*IBM* *WAS*简介](https://blog.csdn.net/iteye_18534/article/details/82329952)

[亮剑](https://blog.csdn.net/iteye_18534)

05-11
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3817

[*IBM* *WAS*简介
*IBM* *WAS* 的全称是 *IBM* WebSphere Application Server ，和 Weblogic 一样 ，是 当前主流的 App Server （应用服务器）之一 。App Server 是运行 Java 企 业组 件的平台，构成了 应 用 软 件的主要运行 环 境。其他常用的 App Server 还有 ： Tomcat 、 Jboss 。*IBM*...](https://blog.csdn.net/iteye_18534/article/details/82329952)

[*WAS*系统*打补丁*的详细配置指南](https://wenku.csdn.net/doc/2m81her7jy)

[*WAS**打补丁*的配置过程通常涉及以下几个关键步骤： 1. 准备工作：在开始*安装**补丁*之前，需要了解当前*WAS*版本和*补丁*包的要求，*查看**补丁*说明文档，确定*补丁*是否适用于当前环境。备份好*WAS*配置和数据，确保在*补丁**安装*过程...](https://wenku.csdn.net/doc/2m81her7jy)

[WebSphere*补丁*升级](https://download.csdn.net/download/qq_35335755/10709437)

10-09

[WebSphere Application Server（简称WebSphere或*WAS*）是由*IBM*开发的一款高性能的企业级应用服务器产品，主要用于支持Java EE应用程序的部署和运行。随着技术的发展和安全性的提升，定期对WebSphere进行*补丁*升级显得...](https://download.csdn.net/download/qq_35335755/10709437)

[Websphere7*安装*及*打补丁**Linux*CentOSMysql数据源配置.pptx](https://download.csdn.net/download/SherryJin/88126386)

07-30

[【标题】: WebSphere 7在*Linux* CentOS系统中*安装*、*打补丁*以及配置MySQL数据源的教程 【描述】: 本教程详细介绍了如何在*Linux* CentOS操作系统上*安装*WebSphere Application Server 7，*打补丁*以及配置连接MySQL数据库...](https://download.csdn.net/download/SherryJin/88126386)

[*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.](https://download.csdn.net/download/flyfly98/2769017)

10-19

[*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.*IBM*\_*WAS*简介.](https://download.csdn.net/download/flyfly98/2769017)

[*IBM*\_*WAS*简介](https://download.csdn.net/download/fengkuang615/5119166)

03-07

[websphere它的特性进一步扩展了 WebSphere Application Server 平台的覆盖范围、运行时管理功能和应用程序部署选项，以帮助您降低成本和进一步发展企业。](https://download.csdn.net/download/fengkuang615/5119166)

[怎样给*was*6.1*打补丁*](https://download.csdn.net/download/xqiyi/1775234)

10-28

[给*was*6.1*打补丁*，包括下载，*打补丁*顺序](https://download.csdn.net/download...