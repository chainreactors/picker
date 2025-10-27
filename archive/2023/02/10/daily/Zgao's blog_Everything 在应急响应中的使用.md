---
title: Everything 在应急响应中的使用
url: https://zgao.top/everything-%e5%9c%a8%e5%ba%94%e6%80%a5%e5%93%8d%e5%ba%94%e4%b8%ad%e7%9a%84%e4%bd%bf%e7%94%a8/
source: Zgao's blog
date: 2023-02-10
fetch_date: 2025-10-04T06:12:04.132885
---

# Everything 在应急响应中的使用

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# Everything 在应急响应中的使用

* [首页](https://zgao.top)
* [Everything 在应急响应中的使用](https://zgao.top:443/everything-%E5%9C%A8%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E4%B8%AD%E7%9A%84%E4%BD%BF%E7%94%A8/)

[2月 9, 2023](https://zgao.top/2023/02/)

### Everything 在应急响应中的使用

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/everything-%E5%9C%A8%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E4%B8%AD%E7%9A%84%E4%BD%BF%E7%94%A8/)

在入侵排查过程中，检索最近的文件变动是非常重要的一个步骤。而Windows中并没有像Linux那样的find命令可以支持查找指定时间段内变动的文件。而命令行的everything（es）的出现刚好弥补了Windows命令行文件查找的功能。

文章目录

[ ]

* [安装everthing命令行版ES](#%E5%AE%89%E8%A3%85everthing%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%89%88ES "安装everthing命令行版ES")
* [ES 命令行注意事项](#ES_%E5%91%BD%E4%BB%A4%E8%A1%8C%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9 "ES 命令行注意事项")
  + [特殊符号转义](#%E7%89%B9%E6%AE%8A%E7%AC%A6%E5%8F%B7%E8%BD%AC%E4%B9%89 "特殊符号转义")
  + [优化查找优先级](#%E4%BC%98%E5%8C%96%E6%9F%A5%E6%89%BE%E4%BC%98%E5%85%88%E7%BA%A7 "优化查找优先级")
* [ES在应急排查中的常用选项](#ES%E5%9C%A8%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5%E4%B8%AD%E7%9A%84%E5%B8%B8%E7%94%A8%E9%80%89%E9%A1%B9 "ES在应急排查中的常用选项")
  + [应急排查常用参数](#%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5%E5%B8%B8%E7%94%A8%E5%8F%82%E6%95%B0 "应急排查常用参数")
  + [函数语法](#%E5%87%BD%E6%95%B0%E8%AF%AD%E6%B3%95 "函数语法")
  + [大小语法](#%E5%A4%A7%E5%B0%8F%E8%AF%AD%E6%B3%95 "大小语法")
  + [日期常数](#%E6%97%A5%E6%9C%9F%E5%B8%B8%E6%95%B0 "日期常数")
* [ES应急排查常用语句汇总](#ES%E5%BA%94%E6%80%A5%E6%8E%92%E6%9F%A5%E5%B8%B8%E7%94%A8%E8%AF%AD%E5%8F%A5%E6%B1%87%E6%80%BB "ES应急排查常用语句汇总")
  + [指定日期发生变动的txt文件，最多显示10个](#%E6%8C%87%E5%AE%9A%E6%97%A5%E6%9C%9F%E5%8F%91%E7%94%9F%E5%8F%98%E5%8A%A8%E7%9A%84txt%E6%96%87%E4%BB%B6%EF%BC%8C%E6%9C%80%E5%A4%9A%E6%98%BE%E7%A4%BA10%E4%B8%AA "指定日期发生变动的txt文件，最多显示10个")
  + [最近7天内发生变动且小于20kb的jsp文件](#%E6%9C%80%E8%BF%917%E5%A4%A9%E5%86%85%E5%8F%91%E7%94%9F%E5%8F%98%E5%8A%A8%E4%B8%94%E5%B0%8F%E4%BA%8E20kb%E7%9A%84jsp%E6%96%87%E4%BB%B6 "最近7天内发生变动且小于20kb的jsp文件")
  + [某时间段内被访问过且包含指定字符串的文件](#%E6%9F%90%E6%97%B6%E9%97%B4%E6%AE%B5%E5%86%85%E8%A2%AB%E8%AE%BF%E9%97%AE%E8%BF%87%E4%B8%94%E5%8C%85%E5%90%AB%E6%8C%87%E5%AE%9A%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%96%87%E4%BB%B6 "某时间段内被访问过且包含指定字符串的文件")
  + [某日期前创建且指定字符串开头文件名的日志文件](#%E6%9F%90%E6%97%A5%E6%9C%9F%E5%89%8D%E5%88%9B%E5%BB%BA%E4%B8%94%E6%8C%87%E5%AE%9A%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%BC%80%E5%A4%B4%E6%96%87%E4%BB%B6%E5%90%8D%E7%9A%84%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6 "某日期前创建且指定字符串开头文件名的日志文件")
  + [指定目录下的图片文件](#%E6%8C%87%E5%AE%9A%E7%9B%AE%E5%BD%95%E4%B8%8B%E7%9A%84%E5%9B%BE%E7%89%87%E6%96%87%E4%BB%B6 "指定目录下的图片文件")
  + [查找包含指定文件名的父文件夹](#%E6%9F%A5%E6%89%BE%E5%8C%85%E5%90%AB%E6%8C%87%E5%AE%9A%E6%96%87%E4%BB%B6%E5%90%8D%E7%9A%84%E7%88%B6%E6%96%87%E4%BB%B6%E5%A4%B9 "查找包含指定文件名的父文件夹")
  + [指定字符结尾的文件名](#%E6%8C%87%E5%AE%9A%E5%AD%97%E7%AC%A6%E7%BB%93%E5%B0%BE%E7%9A%84%E6%96%87%E4%BB%B6%E5%90%8D "指定字符结尾的文件名")
* [Everything 高级用法补充](#Everything_%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95%E8%A1%A5%E5%85%85 "Everything 高级用法补充")
  + [批量文件正则重命名](#%E6%89%B9%E9%87%8F%E6%96%87%E4%BB%B6%E6%AD%A3%E5%88%99%E9%87%8D%E5%91%BD%E5%90%8D "批量文件正则重命名")
* [文件时间QA](#%E6%96%87%E4%BB%B6%E6%97%B6%E9%97%B4QA "文件时间QA")
  + [Q:为什么有的文件修改时间早于创建时间？](#Q_%E4%B8%BA%E4%BB%80%E4%B9%88%E6%9C%89%E7%9A%84%E6%96%87%E4%BB%B6%E4%BF%AE%E6%94%B9%E6%97%B6%E9%97%B4%E6%97%A9%E4%BA%8E%E5%88%9B%E5%BB%BA%E6%97%B6%E9%97%B4%EF%BC%9F "Q:为什么有的文件修改时间早于创建时间？")

## 安装everthing命令行版ES

<https://www.voidtools.com/zh-cn/downloads/>

![](https://zgao.top/wp-content/uploads/2023/02/image-11-1024x429.png)

同时下载ES，放到 C:\Windows\System32\ 目录下。

![](https://zgao.top/wp-content/uploads/2023/02/image-12-1024x588.png)

可以在cmd中调用es就算安装成功。

注：命令行执行es需要先在后台运行everything。

![](https://zgao.top/wp-content/uploads/2023/02/image-13-1024x492.png)

## ES 命令行注意事项

### 特殊符号转义

命令行和GUI会有部分使用区别，一些特殊符号\ & | > < ^ 需要用双引号（”）来转义。例如查找最近的log文件变动的命令如下：

```
es ext:log dm:">20230101" dm:"<20230201"
```

### 优化查找优先级

es有从左到右的搜索优先级排序。比如同样的搜索规则，交换上面的顺序。

```
es dm:">20230101" dm:"<20230201" ext:log
```

虽然得到的结果是一样的，但是查找的速度慢很多。这里是先查找这一个月内变动的所有文件，再从中查找log的文件。

## ES在应急排查中的常用选项

### 应急排查常用参数

* path: 匹配路径和文件名.
* file:仅匹配文件.
* folder:仅匹配文件夹.
* child: 搜索包含匹配文件名文件的文件夹.
* parent: 搜索指定路径下的文件和文件夹 (不包含子文件夹).
* content: 搜索文本内容.
* count: 指定搜索结果最大值.
* da: 搜索指定访问时间的文件和文件夹.
* dc: 搜索指定创建日期的文件和文件夹.
* dm: 搜索指定修改日期的文件和文件夹.
* rc: 搜索指定最近修改日期的文件和文件夹.
* startwith: 搜索指定文本开头的文件.
* endwith: 搜索以指定文本结尾的文件 (包含扩展名).
* ext: 搜索和列表中指定的扩展名匹配的文件 (扩展名以分号分隔).
* size: 搜索指定大小的文件 (以字节为单位).

da、dc、dm分别对应的就是atime、ctime、mtime。

### 函数语法

* function:value 等于某设定值.
* function:<=value 小于等于某设定值.
* function:>=value 大于等于某设定值.
* function:start..end 在起始值和终止值的范围内.
* function:start-end 在起始值和终止值的范围内.

比如上面的

```
dm:">20230101" dm:"<20230201"
等价于
dm:"20230101..20230201"
等价于
dm:"20230101-20230201"
```

### 大小语法

size[kb|mb|gb]

```
size:">100kb" size:"<1mb"
等价于
size:"100kb-1mb"
```

### 日期常数

* today
* yesterday
* tomorrow
* [last|past|prev|current|this|coming|next] + [year|month|week]
* [last|past|prev|coming|next] + [x] +[years|months|weeks|days|hours|minutes|mins|seconds|secs]

后面的两个是指常量可以拼接。比如：

* 上周可以表示为：lastweek
* 过去三天可以表示为：last3days
* 当前这一个小时可以表示为：this1hours

## ES应急排查常用语句汇总

下面这些语句会尽量涵盖上面所有的常用参数，可以帮助进一步理解每个参数的含义和用法。

### 指定日期发生变动的txt文件，最多显示10个

```
es rc:"20230209"  ext:txt count:10
等价于
es dm:"20230209"  ext:txt count:10
```

![](https://zgao.top/wp-content/uploads/2023/02/image-14-1024x234.png)

这里测试rc和dm是等价的。

### 最近7天内发生变动且小于20kb的jsp文件

```
es ext:jsp dm:"last7days" size:"<20kb"
```

### 某时间段内被访问过且包含指定字符串的文件

比如查找2022年12月31号到2023年1月1号被访问的文件，包含eval关键字的php或asp文件。

```
es ext:php;asp da:"20221231-20230101" content:"eval"
```

### 某日期前创建且指定字符串开头文件名的日志文件

```
es ext:log startwith:"ydservice" dc:"<20230205"
```

![](https://zgao.top/wp-content/uploads/2023/02/image-15-1024x325.png)

### 指定目录下的图片文件

这里要分为两种情况：

包含目录下的子目录

```
es ext:jpg;png path:"C:\Program Files\"  count:5
```

不包含目录下的子目录

```
es ext:jpg;png path:"C:\Program Files\"  parent:"C:\Program Files\" count:5
```

![](https://zgao.top/wp-content/uploads/2023/02/image-17-1024x281.png)

这里也可以看出es是深度优先遍历的查找顺序。

### 查找包含指定文件名的父文件夹

```
es path:"C:\Program Files\" child:"test" count:1
```

![](https://zgao.top/wp-content/uploads/2023/02/image-18-1024x402.png)

### 指定字符结尾的文件名

有部分文件可能本身没有后缀名，比如aaa，bbb，ccc这种不知道格式的文件。此时再用ext就无法匹配了。

```
es endwith:"j" file: count:10
```

![](https://zgao.top/wp-content/uploads/2023/02/image-19-1024x348.png)

更多的使用就结合实际情况，按照需求排列组合参数进行查找即可。

## Everything 高级用法补充

### 批量文件正则重命名

![](https://zgao.top/wp-content/uploads/2023/02/image-21-1024x462.png)

比如我想把下面的文件重命名为其他的日期格式。

![](https://zgao.top/wp-content/uploads/2023/02/image-22-1024x623.png)

比如把日期格式从20230204转换成2023-02-04的格式，正则可以这样写。其中\1和\2分别表示为上面小括号的匹配内容。

```
原始文件名表达式：^ydservice\.2023(\d{2})(\d{2})\.log$
新文件名表达式：ydservice.2023-\1-\2.log
```

![](https://zgao.top/wp-content/uploads/2023/02/image-23.png)

## 文件时间QA

### Q:为什么有的文件修改时间早于创建时间？

A:当旧的文件拷贝到新的目录下，创建时间为当时拷贝的时间，但是修改时间仍然为之前修改的时间，也就是出现了修改时间早于创建时间的问题。

![](https://zgao.top/wp-content/uploads/2023/02/image-24.png)

Post Views: 2,223

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### 匿名 发布于7:07 下午 - 2月 10, 2023

老大，那个插件好像又不能抓取视频文件了

[回复](https://zgao.top/everything-%E5%9C%A8%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E4%B8%AD%E7%9A%84%E4%BD%BF%E7%94%A8/?replytocom=4901#respond)

### 发表评论 [取消回复](/everything-%E5%9C%A8%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94%E4%B8%AD%E7%9A%84%E4%BD%BF%E7%94%A8/#respond)

Δ

版权©2020 Author By : Zgao