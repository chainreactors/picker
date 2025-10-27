---
title: 精简版SDL落地实践 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17146534.html
source: 博客园 - 渗透测试中心
date: 2023-02-23
fetch_date: 2025-10-04T07:51:19.453015
---

# 精简版SDL落地实践 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [精简版SDL落地实践](https://www.cnblogs.com/backlion/p/17146534.html "发布于 2023-02-23 00:59")

## 一、前言

一般安全都属于运维部下面，和上家公司的运维总监聊过几次一些日常安全工作能不能融入到DevOps中，没多久因为各种原因离职。18年入职5月一家第三方支付公司，前半年在各种检查中度过，监管形势严峻加上大领导对安全的重视(主要还是监管)，所有部门19年的目标都和安全挂钩。由于支付公司需要面对各种监管机构的检查，部分安全做的比较完善，经过近一年对公司的熟悉发现应用安全方面比较薄弱。这部分业内比较好的解决方案就是SDL，和各厂商交流过之后决定自己照葫芦画瓢在公司一点一点推广。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005505851-1935601238.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712212713-c2466ec8-a4a8-1.png)

上图为标准版的SDL,由于运维采用DevOps体系，测试也使用自动化进行功能测试，版本迭代周期比较快,安全人手不足加上对SDL的威胁建模等方法也一头雾水、如果把安全在加入整个流程会严重影响交付时间。在这种情况调研了一些业内的一些做法，决定把SDL精简化 。精简版SDL如下：

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005506900-1241560024.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712212552-9267e2ae-a4a8-1.png).

## 二、精简版SDL落地实践

### 安全培训

SDL核心之一就是安全培训，所以在安全培训上我们做了安全编码、安全意识、安全知识库、安全SDK

#### 安全编码：

我们在网上找了一些java安全编码规范、产品安全设计及开发安全规范结合公司实际业务出了一版。
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005507712-1799677019.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712213113-51b222e6-a4a9-1.png)
因为各种监管机构对培训都有要求，借此推了一下安全培训，定期对开发和新员工入职的培训。
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005508666-156154663.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712213148-665e0b56-a4a9-1.png)

#### 安全意识：

公司有企业微信公众号，大部分员工都关注了，在公众号推广了一波。
[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005511575-1861001679.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712213307-95a52bf6-a4a9-1.png)
宣传完之后答题，答题满分送小礼品

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005512954-1257222268.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712213524-e6f6c884-a4a9-1.png)
因为人手不足，而功能测试和安全测试本质上有很多相通的地方，测试部门也比较配合，针对测试人员做了一些安全测试相关的培训，但是效果并不是太理想。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005513820-1671772662.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712213615-05c27d58-a4aa-1.png)

#### 安全知识库：

在漏洞修复过程中，开发很多不太了解漏洞原理、修复方案，所以我们建立了安全知识库，开发先到安全知识库查相关解决方法。找不到的再和安全人员沟通，安全人员对知识库不断更新，形成一个闭环。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005514543-574197297.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712213825-53035c72-a4aa-1.png)

#### 安全SDK

由于公司有架构部门，开发框架基本是架构部门提供。我们将一些常见的漏洞和架构部门沟通之后，让架构将一些漏洞修复方式用SDK实现，开发只需要导入JAR包，在配置文件中配置即可。其中也挺多坑的，需要慢慢优化。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005515341-1061280096.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712213911-6e5837d6-a4aa-1.png)

## 三、 安全需求设计

公司有项目立项系统，所有的项目立项都需要通过系统来进行立项，安全为必选项，评审会安全也必须要参与

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005516070-1183240391.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214038-a26137e4-a4aa-1.png)

这个时候基本上项目经理会找安全人员进行沟通，copy了一份VIP的产品安全设计规范，根据需求文档和项目经理确定安全需求。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005518167-302814842.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214146-caf2c1aa-a4aa-1.png)
确认好安全需求之后将按需求加入到需求文档，并确认安全测试时间，此流程只针对新项目，已经上线的项目的需求并未按照此流程，后续在安全测试时候会讲到这部分的项目是怎么做的。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005519575-917103671.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214259-f641994e-a4aa-1.png)

## 四、开发、安全测试

安全测试主要分为代码审计，漏洞扫描，手工安全测试。由此衍生出来的安全产品分为3类。DAST：动态应用程序安全测试 （wvs,appscan）、SAST：静态应用程序安全测试 (fortify,rips)、IAST：交互式应用程序安全测试 （seeker，雳鉴）,这三种产品的详细介绍可以参考[https://www.aqniu.com/learn/46910.html,下图为三种产品的测试结果对比。](https://www.aqniu.com/learn/46910.html%2C%E4%B8%8B%E5%9B%BE%E4%B8%BA%E4%B8%89%E7%A7%8D%E4%BA%A7%E5%93%81%E7%9A%84%E6%B5%8B%E8%AF%95%E7%BB%93%E6%9E%9C%E5%AF%B9%E6%AF%94%E3%80%82)

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005520614-1980739689.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214421-2764cb68-a4ab-1.png)
这几类产品实现了自动化可以继承到DevOps中。接下来我们将这些工具融入到开发测试阶段。
IAST的实现模式较多，常见的有代理模式、VPN、流量镜像、插桩模式，本文介绍最具代表性的2种模式，代理模式和插桩模式。一些调研过的产品如下图，具体测试结果就不公布了。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005521457-454737043.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214500-3e41c9f8-a4ab-1.png)

### 开发阶段

在对几类产品调研的时候发现IAST的插桩模式可以直接放到开发环境，开发环境和测试环境的代码区别主要还是在于application.yml配置文件，所以可以提前将该模式放到开发阶段。
开发写完代码提交到gitlab部署到开发环境启动应用的时候，开发需要验证一下功能是否可用，这个时候就可以检测出是否存在漏洞。
公司在测试环境使用rancher，把IAST的jar包放入到项目的gitlab,在部署的时候把代码拉到本地，通过修改Dockerfile文件把jar包添加到容器。

```
ADD shell/xxx.jar /home/app/xx/lib
```

由于公司项目基本统一使用spring-boot，所有的项目都通过一个start.sh脚本来启动应用，start.sh和Dockerfile一样需要添加到项目的gitlab，同时修改start.sh脚本文件即可。

```
-javaagent:$APP_HOME/lib/xx.jar  -jar $APP_HOME/app/*.jar --spring.profiles.active=dev >$APP_HOME/logs/startup.log 2>&1 &
```

测试项目如下，忽略错别字：

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005522132-529066295.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214648-7f102ace-a4ab-1.jpeg)

开发提交代码部署完之后，访问一下正常的功能即可在平台上看见是否存在漏洞。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005522696-404919098.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214726-9549b878-a4ab-1.jpeg)

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005523433-204390000.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214727-95e12d5c-a4ab-1.png)

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005524107-1209971798.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214730-97cb91c0-a4ab-1.jpeg)
部分产品同时还会检测第三方组件包。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005524868-632493352.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214744-a0216caa-a4ab-1.png)
公司使用harbor来对镜像进行当仓库镜像，项目部署完成之后会打包成一个镜像上传到harbor，harbor自带镜像扫描功能。

[![](https://img2023.cnblogs.com/blog/1049983/202302/1049983-20230223005525557-202407059.png)](https://xzfile.aliyuncs.com/media/upload/picture/20190712214830-bb7106b4-a4ab-1.png)

### 测试阶段

开发完成之后进入到测试阶段。这个阶段我们进行静态代码扫描，功能测试，安全测试。

#### 静态代码扫描

利用静态代码扫描工具对代码在编译之前进行扫描，并在静态...