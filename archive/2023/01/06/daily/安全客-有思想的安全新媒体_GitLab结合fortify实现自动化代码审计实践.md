---
title: GitLab结合fortify实现自动化代码审计实践
url: https://www.anquanke.com/post/id/284200
source: 安全客-有思想的安全新媒体
date: 2023-01-06
fetch_date: 2025-10-04T03:08:32.295779
---

# GitLab结合fortify实现自动化代码审计实践

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

# GitLab结合fortify实现自动化代码审计实践

阅读量**565681**

发布时间 : 2023-01-05 16:30:23

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 一、背景

在甲方做安全的同学可能会有一项代码审计的工作，通常需要从gitlab把代码拉取下来，然后使用代码审计工具进行扫描，然后对结果进行人工确认；

在这个流程中需要做的事情比较繁琐，比如说gitlab如何配置token、如何自动化把代码拉取到本地、如何调用fortify实现批量扫描等诸多繁琐问题。

本篇文章以甲方安全代码安全建设为主线，分享如何让代码审计工具自动化扫描gitlab仓库里的代码。并且提供了一个便捷的实验环境供大家测试。

> 本文实验中调用了多款代码审计工具（包含semgrep、fortify、墨菲、河马，其中fortify软件属于商业性质，本文章无法提供该软件，如需自备此软件并存放在主机/data/share/fortify目录），完成试验后可以看到各代码审计工具的效果对比。

## 二、准备环境

为了方便大家，我把我的实验gitlab地址直接共享出来，大家可以优先使用此共享环境。

```
URL：http://123.249.6.139:1880/
用户名：root
密码：qingtingtest
token：glpat-SMsSWy6xzB4x8B6rFryB
```

### 配置gitlab环境

为了真实模拟fortify扫描gitlab仓库的代码，我需要快速搭建一个gitlab仓库，这里实验docker的方式最为简单，只需要执行以下的命令

```
docker run --detach --hostname gitlab.thinkpad --publish 8443:443 --publish 880:80 --publish 222:22 --name gitlab --restart always --volume /data/gitlab/config:/etc/gitlab --volume /data/gitlab/logs:/var/log/gitlab --volume /data/gitlab/data:/var/opt/gitlab gitlab/gitlab-ce
```

命令执行之后，docker会自动拉取docker镜像，并创建一个gitlab的容器，服务启动之后会随机生成一个root用户的密码，可以通过以下命令查看root用户的初始化密码

```
docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

命令执行之后，可以在终端中看到如下所示密码

```
Password: UnSoOs7l8YN6dYDQRP/1/dzpKswF7dq7fpyhKBey95A=
```

现在可以使用浏览器访问gitlab的页面，访问地址是`http://x.x.x.x:880/`，然后浏览器会自动跳转到登录页面，如下图所示

![]()

在登录页面，我们在用户名处输入root，密码处输入刚才得到的密码；登录成功之后会自动跳转到工作台的首页，如下图所示。

![]()

### 创建API访问的token

为了让fortify能够访问到gitlab仓库的代码，我们需要创建一个token，用于API访问；在头像位置展开下拉菜单，选择preferences->Access Tokens ,填下相关参数，界面如下所示

![]()

创建完成，把生成的token复制出来，后续要用到

![]()

```
glpat-ggjo6Z6aQXWCZ2FNJcsz
```

gitlab搭建完后，默认里面有一个空项目，fortify无法扫除有价值的漏洞，为了方便测试，需要在新建项目的位置导入项目进去，打开URL地址
`http://10.1.1.140:880/projects/new#import_project`,然后选择`Repository by URL`，然后填入一个可以被拉取的仓库地址，这里我提供一个供大家实验，如下图所示

```
https://gitee.com/songboy/QingScan
```

![]()

导入项目之后，gitlab会自动拉取代码到服务器，如下图所示

![]()

## 三、配置参数

现在已经有了gitlab的实验环境，可以正式开始做实验，首先打开蜻蜓的市场页面，URL地址如下

```
http://qingting.starcross.cn/scenario/store
```

可能会提示要求登录，如果是首次进入蜻蜓安全控制台，扫描登录之后会自动注册

然后需要在服务器执行添加节点的shell命令，按照提示进行操作即可，如下图所示

![]()

现在回到市场页面，找到快速挖掘0day漏洞，在下方有个按钮，添加到工作流，如下图所示

![]()

添加到工作流之后，会看到工作流的信息，这里可以把gitlab的配置信息填写进去，需要点击进入编排流程，如下图所示

![]()

在编排工作流页面，上方有一个设置全局变量的小图标,按照提示配置必要参数，如下图所示

![]()

## 四、运行程序

运行全局变量完成之后，可以右键点击第一个节点，再次点估运行选项，就可以运行这个工作流，运行过程中节点状态会发生变化

![]()

节点会按照自上而下运行，运行过程中状态图标会一直旋转，当运行完成时，可以看到成功的小图标

![]()

运行完成之后，可以去数据中心查看运行结果，可以根据节点和任务ID等方式筛选，如下图所示

![]()

我选中fortify代码扫描节点，筛选出来的列表页面如下所示

![]()

在列表页面只展示了一小部分数据，可以点击查看按钮，在详情页查看详细的漏洞信息，用于审计标注，如下图所示。

![]()

上面节点的代码已经在GitHub中开源，有需要的小伙伴也可以在GitHub

```
https://github.com/StarCrossPortal/QingTing
```

GitHub地址：<https://github.com/StarCrossPortal/QingTing>

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**qingsongboy**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284200](/post/id/284200)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [代码审计](/tag/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1)
* [fortify](/tag/fortify)

**+1**0赞

收藏

![](https://p1.ssl.qhmsg.com/dm/200_200_100/t0165c1e612a26d7a12.jpg)qingsongboy

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhmsg.com/dm/200_200_100/t0165c1e612a26d7a12.jpg)](/member.html?memberId=128405)

[qingsongboy](/member.html?memberId=128405)

这个人太懒了，签名都懒得写一个

* 文章
* **7**

* 粉丝
* **2**

### TA的文章

* ##### [开源dolphin项目-ASM网络资产风险监测系统](/post/id/287246)

  2023-03-15 16:30:19
* ##### [高效率开发Web安全扫描器之路（一）](/post/id/283900)

  2023-01-06 14:00:19
* ##### [GitLab结合fortify实现自动化代码审计实践](/post/id/284200)

  2023-01-05 16:30:23
* ##### [蜻蜓低代码安全工具平台开发之路](/post/id/275235)

  2022-06-27 10:30:50
* ##### [CIS 2021网络安全创新大会《代码安全体系建设》实录](/post/id/270173)

  2022-05-30 15:30:57

### 相关文章

* ##### [完全零基础入门Fastjson系列漏洞（基础篇）](/post/id/288185)

  2025-06-10 10:33:12
* ##### [某塔强制绑定账号分析](/post/id/282486)

  2022-11-07 12:00:56
* ##### [代码审计之路之白盒挖掘机](/post/id/279501)

  2022-09-05 14:30:32
* ##### [PHP代码审计](/post/id/277446)

  2022-08-16 14:30:07
* ##### [代码审计实战](/post/id/276353)

  2022-07-15 10:31:25
* ##### [极致CMS建站系统代码审计之旅](/post/id/272911)

  2022-06-13 14:30:38
* ##### [CodeQL for VSCode搭建流程](/post/id/266823)

  2022-02-14 10:30:52

### 热门推荐

文章目录

* [一、背景](#h2-0)
* [二、准备环境](#h2-1)
  + [配置gitlab环境](#h3-2)
  + [创建API访问的token](#h3-3)
* [三、配置参数](#h2-4)
* [四、运行程序](#h2-5)

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