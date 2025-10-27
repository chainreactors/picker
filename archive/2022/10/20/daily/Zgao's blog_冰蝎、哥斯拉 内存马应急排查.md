---
title: 冰蝎、哥斯拉 内存马应急排查
url: https://zgao.top/%e5%86%b0%e8%9d%8e%e3%80%81%e5%93%a5%e6%96%af%e6%8b%89-%e5%86%85%e5%ad%98%e9%a9%ac%e5%ba%94%e6%80%a5%e6%8e%92%e6%9f%a5/
source: Zgao's blog
date: 2022-10-20
fetch_date: 2025-10-03T20:20:10.395232
---

# 冰蝎、哥斯拉 内存马应急排查

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 冰蝎、哥斯拉 内存马应急排查

* [首页](https://zgao.top)
* [冰蝎、哥斯拉 内存马应急排查](https://zgao.top:443/%E5%86%B0%E8%9D%8E%E3%80%81%E5%93%A5%E6%96%AF%E6%8B%89-%E5%86%85%E5%AD%98%E9%A9%AC%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5/)

[10月 19, 2022](https://zgao.top/2022/10/)

### 冰蝎、哥斯拉 内存马应急排查

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/%E5%86%B0%E8%9D%8E%E3%80%81%E5%93%A5%E6%96%AF%E6%8B%89-%E5%86%85%E5%AD%98%E9%A9%AC%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5/)

内存马的排查方式汇总。内存马的原理分析网上有很多文章，这里就不介绍了。通过实验分析如何在实战环境中快速定位内存马。

文章目录

[ ]

* [实验环境](#%E5%AE%9E%E9%AA%8C%E7%8E%AF%E5%A2%83 "实验环境")
* [环境搭建](#%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA "环境搭建")
  + [安装tomcat](#%E5%AE%89%E8%A3%85tomcat "安装tomcat")
  + [安装 Arthas](#%E5%AE%89%E8%A3%85_Arthas "安装 Arthas")
* [哥斯拉 内存马](#%E5%93%A5%E6%96%AF%E6%8B%89_%E5%86%85%E5%AD%98%E9%A9%AC "哥斯拉 内存马")
  + [FilterShell](#FilterShell "FilterShell")
  + [MemoryShell](#MemoryShell "MemoryShell")
* [冰蝎 内存马](#%E5%86%B0%E8%9D%8E_%E5%86%85%E5%AD%98%E9%A9%AC "冰蝎 内存马")
* [heapdump 内存排查](#heapdump_%E5%86%85%E5%AD%98%E6%8E%92%E6%9F%A5 "heapdump 内存排查")
* [Arthas 排查内存马命令总结](#Arthas_%E6%8E%92%E6%9F%A5%E5%86%85%E5%AD%98%E9%A9%AC%E5%91%BD%E4%BB%A4%E6%80%BB%E7%BB%93 "Arthas 排查内存马命令总结")
  + [注意事项](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9 "注意事项")

## 实验环境

* Centos / tomcat 7.0.76
* 冰蝎v4.0.5
* 哥斯拉v4.0.1
* Arthas 3.6.6

## 环境搭建

### 安装tomcat

通过yum安装tomcat。

```
yum install -y tomcat tomcat-webapps tomcat-admin-webapps
systemctl start tomcat
```

启动后访问8080端口，看到tomcat起来了。

![](https://zgao.top/wp-content/uploads/2022/10/image-33-1024x391.png)

### 安装 Arthas

<https://github.com/alibaba/arthas/releases>

下载压缩包解压执行

```
wget https://github.com/alibaba/arthas/releases/download/arthas-all-3.6.6/arthas-bin.zip
unzip arthas-bin.zip
java -jar arthas-boot.jar
```

![](https://zgao.top/wp-content/uploads/2022/10/image-37-1024x521.png)

## 哥斯拉 内存马

用哥斯拉生成🐴。

![](https://zgao.top/wp-content/uploads/2022/10/image-34-1024x443.png)

放到网站根目录下面。

![](https://zgao.top/wp-content/uploads/2022/10/image-35-1024x537.png)

植入内存马之前查看内存中mbean信息。

```
 mbean | grep "name=/"
```

![](https://zgao.top/wp-content/uploads/2022/10/image-38-1024x473.png)

### FilterShell

连上哥斯拉的webshell可以看到提供了memoryShell和FilterShell两种🐴。

![](https://zgao.top/wp-content/uploads/2022/10/image-39-1024x636.png)
![](https://zgao.top/wp-content/uploads/2022/10/image-40-1024x481.png)

可以看到哥斯拉的Filter内存马name中都带有时间戳。

```
sc *.Filter
sc -d org.apache.coyote.SerializationConfig
```

![](https://zgao.top/wp-content/uploads/2022/10/image-41-864x1024.png)

使用jad反编译我们认为可疑的类。

```
jad org.apache.coyote.SerializationConfig
```

![](https://zgao.top/wp-content/uploads/2022/10/image-43-1024x949.png)
![](https://zgao.top/wp-content/uploads/2022/10/image-44-1024x703.png)

代码中大量运用invoke反射来实现。

### MemoryShell

![](https://zgao.top/wp-content/uploads/2022/10/image-45-1024x554.png)

添加该内存马后通过mbean可以看到多了几个servlet。

```
mbean | grep "name=/"
sc *.Servlet
```

![](https://zgao.top/wp-content/uploads/2022/10/image-46-1024x370.png)
![](https://zgao.top/wp-content/uploads/2022/10/image-47-1024x624.png)

可疑的classloader。

![](https://zgao.top/wp-content/uploads/2022/10/image-48-1024x425.png)

## 冰蝎 内存马

冰蝎内存马由于对底层函数做了hook的操作，所以特征更弱一些。

先生成冰蝎4.0的服务端。

![](https://zgao.top/wp-content/uploads/2022/10/image-49-1024x681.png)

上传后连接注入内存马。

![](https://zgao.top/wp-content/uploads/2022/10/image-50-1024x501.png)

开启冰蝎的防检测功能。

![](https://zgao.top/wp-content/uploads/2022/10/image-51-1024x376.png)

连上内存马。

![](https://zgao.top/wp-content/uploads/2022/10/image-52-1024x507.png)

冰蝎的classloader。

![](https://zgao.top/wp-content/uploads/2022/10/image-53-1024x441.png)
![](https://zgao.top/wp-content/uploads/2022/10/image-54-1024x720.png)

冰蝎🐴属于Servlet类型的，不过并不是加载内存马之后才有的，而是连接冰蝎服务端的时候就有的。

反编译冰蝎的马，可以看到明显AES加密的key。

![](https://zgao.top/wp-content/uploads/2022/10/image-55-1024x669.png)

但是有个终极排查思路，就是内存dump。

## heapdump 内存排查

不管冰蝎的内存马如何hook，但是内存🐴肯定是在内存中的。并且访问的时候是有路由映射的。那么内存dump出来的文件肯定会有记录。

```
heapdump
strings /var/cache/tomcat/temp/heapdump2022-10-19-12-464292342944555007800.hprof | grep "POST /"
```

![](https://zgao.top/wp-content/uploads/2022/10/image-56-1024x625.png)

还有另外一种方法排查冰蝎内存🐴，就是查找内存中web目录的可疑路径。

```
strings /var/cache/tomcat/temp/heapdump2022-10-19-12-464292342944555007800.hprof | grep -E "/webapps/.*?\!" | sort -u
```

![](https://zgao.top/wp-content/uploads/2022/10/image-57-1024x429.png)

## Arthas 排查内存马命令总结

```
classloader
sc *.Filter
sc *.Servlet
jad
heapdump
```

### 注意事项

使用Arthas可能会遇到下面的报错。

Unable to open socket file: target process not responding or HotSpot VM not loaded

![](https://zgao.top/wp-content/uploads/2022/10/image-58-1024x369.png)

该报错是因为tomcat是以tomcat用户运行的，而我们用arthas是用root用户运行的。JVM 只能 attach 同样用户下的 java 进程。

使用runuser命令即可以tomcat用户运行arthas。

```
runuser -l tomcat -c "java -jar /usr/share/tomcat/arthas-boot.jar"
```

![](https://zgao.top/wp-content/uploads/2022/10/image-59-1024x488.png)

Post Views: 7,333

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 3条评论

###### novvv 发布于12:51 上午 - 11月 9, 2023

[root@coco tomcat]# runuser -l tomcat -c “java -jar /usr/share/tomcat/arthas-boot.jar”
This account is currently not available.
哭了。一样的centos7 x64 这个缓解解决不了了

[回复](https://zgao.top/%E5%86%B0%E8%9D%8E%E3%80%81%E5%93%A5%E6%96%AF%E6%8B%89-%E5%86%85%E5%AD%98%E9%A9%AC%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5/?replytocom=6182#respond)

###### 匿名 发布于10:06 上午 - 11月 9, 2023

说明你系统上没有tomcat这个用户，你可以随便指定一个其他低权用户运行

[回复](https://zgao.top/%E5%86%B0%E8%9D%8E%E3%80%81%E5%93%A5%E6%96%AF%E6%8B%89-%E5%86%85%E5%AD%98%E9%A9%AC%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5/?replytocom=6185#respond)

###### kiki 发布于8:56 下午 - 11月 12, 2022

大佬 P站下载视频的插件已失效，跪求您更新新版本。22.11.12留。

[回复](https://zgao.top/%E5%86%B0%E8%9D%8E%E3%80%81%E5%93%A5%E6%96%AF%E6%8B%89-%E5%86%85%E5%AD%98%E9%A9%AC%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5/?replytocom=4245#respond)

### 发表评论 [取消回复](/%E5%86%B0%E8%9D%8E%E3%80%81%E5%93%A5%E6%96%AF%E6%8B%89-%E5%86%85%E5%AD%98%E9%A9%AC%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5/#respond)

Δ

版权©2020 Author By : Zgao