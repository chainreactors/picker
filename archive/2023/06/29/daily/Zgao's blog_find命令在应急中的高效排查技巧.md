---
title: find命令在应急中的高效排查技巧
url: https://zgao.top/find%e5%91%bd%e4%bb%a4%e5%9c%a8%e5%ba%94%e6%80%a5%e4%b8%ad%e7%9a%84%e9%ab%98%e6%95%88%e6%8e%92%e6%9f%a5%e6%8a%80%e5%b7%a7/
source: Zgao's blog
date: 2023-06-29
fetch_date: 2025-10-04T11:46:49.329563
---

# find命令在应急中的高效排查技巧

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# find命令在应急中的高效排查技巧

* [首页](https://zgao.top)
* [find命令在应急中的高效排查技巧](https://zgao.top:443/find%E5%91%BD%E4%BB%A4%E5%9C%A8%E5%BA%94%E6%80%A5%E4%B8%AD%E7%9A%84%E9%AB%98%E6%95%88%E6%8E%92%E6%9F%A5%E6%8A%80%E5%B7%A7/)

[6月 28, 2023](https://zgao.top/2023/06/)

### find命令在应急中的高效排查技巧

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/find%E5%91%BD%E4%BB%A4%E5%9C%A8%E5%BA%94%E6%80%A5%E4%B8%AD%E7%9A%84%E9%AB%98%E6%95%88%E6%8E%92%E6%9F%A5%E6%8A%80%E5%B7%A7/)

Linux应急响应中，find命令是用的最多的一个命令。分享一些鲜为人知的find命令排查技巧，熟练运用可以达到事半功倍的效果

文章目录

[ ]

* [find使用广度优先遍历查找文件](#find%E4%BD%BF%E7%94%A8%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E9%81%8D%E5%8E%86%E6%9F%A5%E6%89%BE%E6%96%87%E4%BB%B6 "find使用广度优先遍历查找文件")
  + [巧妙利用find命令的depth参数](#%E5%B7%A7%E5%A6%99%E5%88%A9%E7%94%A8find%E5%91%BD%E4%BB%A4%E7%9A%84depth%E5%8F%82%E6%95%B0 "巧妙利用find命令的depth参数")
  + [配合grep查找文件内关键字](#%E9%85%8D%E5%90%88grep%E6%9F%A5%E6%89%BE%E6%96%87%E4%BB%B6%E5%86%85%E5%85%B3%E9%94%AE%E5%AD%97 "配合grep查找文件内关键字")
* [find查找指定时间段内变动的文件](#find%E6%9F%A5%E6%89%BE%E6%8C%87%E5%AE%9A%E6%97%B6%E9%97%B4%E6%AE%B5%E5%86%85%E5%8F%98%E5%8A%A8%E7%9A%84%E6%96%87%E4%BB%B6 "find查找指定时间段内变动的文件")
  + [查找过去n天的文件变动](#%E6%9F%A5%E6%89%BE%E8%BF%87%E5%8E%BBn%E5%A4%A9%E7%9A%84%E6%96%87%E4%BB%B6%E5%8F%98%E5%8A%A8 "查找过去n天的文件变动")
* [find查找特定权限的文件](#find%E6%9F%A5%E6%89%BE%E7%89%B9%E5%AE%9A%E6%9D%83%E9%99%90%E7%9A%84%E6%96%87%E4%BB%B6 "find查找特定权限的文件")
  + [查找可执行文件](#%E6%9F%A5%E6%89%BE%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6 "查找可执行文件")
  + [查找带s位的文件](#%E6%9F%A5%E6%89%BE%E5%B8%A6s%E4%BD%8D%E7%9A%84%E6%96%87%E4%BB%B6 "查找带s位的文件")
  + [查找指定权限的文件](#%E6%9F%A5%E6%89%BE%E6%8C%87%E5%AE%9A%E6%9D%83%E9%99%90%E7%9A%84%E6%96%87%E4%BB%B6 "查找指定权限的文件")
* [find 目录取反](#find_%E7%9B%AE%E5%BD%95%E5%8F%96%E5%8F%8D "find 目录取反")
* [find 并行操作](#find_%E5%B9%B6%E8%A1%8C%E6%93%8D%E4%BD%9C "find 并行操作")
  + [find中 exec 的 + 和 \; 的区别？](#find%E4%B8%AD_exec_%E7%9A%84_%E5%92%8C_%E7%9A%84%E5%8C%BA%E5%88%AB%EF%BC%9F "find中 exec 的 + 和 \; 的区别？")
* [find 正则表达式搜索](#find_%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%90%9C%E7%B4%A2 "find 正则表达式搜索")
* [如何解决文件名存在空格导致的报错？](#%E5%A6%82%E4%BD%95%E8%A7%A3%E5%86%B3%E6%96%87%E4%BB%B6%E5%90%8D%E5%AD%98%E5%9C%A8%E7%A9%BA%E6%A0%BC%E5%AF%BC%E8%87%B4%E7%9A%84%E6%8A%A5%E9%94%99%EF%BC%9F "如何解决文件名存在空格导致的报错？")
* [如何在-exec sh -c ‘command’ 中嵌套使用单引号？](#%E5%A6%82%E4%BD%95%E5%9C%A8-exec_sh_-c_%E2%80%98command%E2%80%99_%E4%B8%AD%E5%B5%8C%E5%A5%97%E4%BD%BF%E7%94%A8%E5%8D%95%E5%BC%95%E5%8F%B7%EF%BC%9F "如何在-exec sh -c ‘command’ 中嵌套使用单引号？")

## find使用广度优先遍历查找文件

find命令默认是深度优先遍历，并且不支持广度优先遍历。

应急最头疼的点就在于，需要排查某些文件中的关键字，但是深度优先遍历使得find命令在某些很深的目录中做无用功，而且要搜索完才能进入到下一个一级目录，总是浪费大量时间。

有什么办法使得find支持广度优先遍历呢？

### 巧妙利用find命令的depth参数

find命令是支持查找目录的层级，比如 -mindepth 和 -maxdepth 参数，分别对应查找最少和最多的目录层级。

```
seq 1 10 | xargs -n2 -P5 sh -c 'find / -iname "xxx" -mindepth $1 -maxdepth $2 2>/dev/null' _
```

![](https://zgao.top/wp-content/uploads/2023/06/image-36-1024x381.png)

该命令相当于find查找指定层级的目录，比如第一次是在1-2层目录中查找，第二次在3-4层目录中匹配。上面的命令看起来会有点抽象，换成下面这种就好理解了。

```
[root@VM-4-7-centos ~]# seq 1 10 | xargs -n2
1 2
3 4
5 6
7 8
9 10
[root@VM-4-7-centos ~]# seq 1 10 | xargs -n2 sh -c 'echo find / -iname xxx -mindepth $1 -maxdepth $2 2>/dev/null' _
find / -iname xxx -mindepth 1 -maxdepth 2
find / -iname xxx -mindepth 3 -maxdepth 4
find / -iname xxx -mindepth 5 -maxdepth 6
find / -iname xxx -mindepth 7 -maxdepth 8
find / -iname xxx -mindepth 9 -maxdepth 10
```

xargs -P5 的是指 5个子进程同时执行，可提升查找速度。

seq 1 10 表示最多查找10层目录，可根据自身需要修改。

### 配合grep查找文件内关键字

```
seq 1 10 | xargs -n2 -P5 sh -c 'find / -type f -mindepth $1 -maxdepth $2 -exec grep -inl "keyword" {} 2>/dev/null \;' _
```

![](https://zgao.top/wp-content/uploads/2023/06/image-37-1024x681.png)

匹配成功后不会直接匹配的内容，而是打印文件的路径。对于不清楚特定关键字位于哪个文件时，该命令排查非常高效。

## find查找指定时间段内变动的文件

这也是我在排查中用的最多的一个选项。有时需要定位某一个时间段内的文件变动就需要用到 -newermt 选项。格式如下：

find / -newermt “开始时间” ! -newermt “截止时间”

注意中间的感叹号不能省略。

比如我要查找 2022年12月31日23:00 到 2023年1月1日1:00 期间发生变动的文件，条件看起来比较苛刻，但 -newermt 可以完全满足。命令如下：

```
find / -newermt "2022-12-31 23:00" ! -newermt "2023-01-01 01:00" 2>/dev/null
```

或者还可以输出文件的修改时间。

```
find / -newermt "2022-12-31 23:00" ! -newermt "2023-01-01 01:00" -exec ls -lh {} \; 2>/dev/null
```

![](https://zgao.top/wp-content/uploads/2023/06/image-38-1024x381.png)

### 查找过去n天的文件变动

比如查找过去3天内的文件变动，命令如下：

```
find / -type f -mtime -3
```

如果先查找3天前的文件变动则是：

```
find / -type f -mtime +3
```

## find查找特定权限的文件

### 查找可执行文件

```
 find /root -executable -type f  -exec ls -lh {} \; -quit
```

* -executable 指定可执行权限的文件
* -quit 匹配到第一个符合条件的文件就退出

### 查找带s位的文件

```
find / \( -perm -4000 -o -perm -2000 \) -type f -exec ls -lh {} \; 2>/dev/null
```

![](https://zgao.top/wp-content/uploads/2023/06/image-39-1024x442.png)

* `-perm -4000` 表示包含`setuid`位的文件
* `-perm -2000` 表示包含`setgid`位的文件
* -o 表示或的关系

为什么是-perm -4000 而不是-perm 4000，有何区别？

在 `find` 命令中使用 `-perm` 选项时，`-` 前缀有特殊的含义。`-perm -mode` 会匹配任何文件的权限中设置了任何 `mode` 指定的位的文件，而 `perm mode` 只会匹配文件权限完全等于 `mode` 的文件。

例如，`-perm -4000` 会匹配所有设置了 setuid 位的文件（不考虑其他权限位是什么），而 `-perm 4000` 会匹配文件权限完全为 `4000`（即只有 setuid 位被设置，其他所有权限位都没有被设置）的文件。

### 查找指定权限的文件

比如要查找系统中0700权限的文件，这里和上面的例子恰好相反，是完全匹配。

```
find / -perm 0700 -type f -exec ls -lh {} \; 2>/dev/null
```

![](https://zgao.top/wp-content/uploads/2023/06/image-40-1024x467.png)

## find 目录取反

应急排查中，往往需要排除掉部分指定的目录。比如查找根目录下的所有可执行文件，但排除/usr目录。

```
find / -path /usr -prune -o -type f -executable
```

在这个命令中，`-path /usr -prune -o` 表示如果路径是 `/usr`，则不搜索该路径，否则继续执行后面的命令。

![](https://zgao.top/wp-content/uploads/2023/06/image-41-1024x539.png)

如果要排除多个目录呢？

```
find / \( -path /usr -o -path /etc \) -prune -o -executable
```

这时候就需要括号把多个目录放在一起进行过滤。

## find 并行操作

以使用 `+` 代替 `\;` 来在 `find` 命令中执行并行操作。

比如排查完成之后需要把一些不同层级目录下的文件，统一打包回传。例如把 /targetDir 下面所有的可执行进行打包并压缩。

```
find /targetDir -type f -executable -exec tar -rvf executables.tar {} +
gzip executables.tar
```

![](https://zgao.top/wp-content/uploads/2023/06/image-42-1024x332.png)

或者首先找到所有的文件，然后一次性将它们添加到 tar 存档中。这样你就可以将存档压缩，而无需追加文件。注意`-print0` 和 `-0` 选项是用来处理文件名中可能包含的特殊字符（如空格或换行符）的。

```
find . -type f -executable -print0 | xargs -0 tar -czvf executables.tgz
```

但这种方式没有用到find的并行。

再举一个例子，要在一个目录中查找所有 `.jpg` 文件并将它们复制到另一个目录，`命令如下`：

```
find /path/to/dir -name "*.jpg" -exec cp {} /path/to/other/dir +
```

这将使用尽可能多的参数来调用 `cp`，而不是每找到一个文件就调用一次 `cp`。

### find中 exec 的 + 和 \; 的区别？

在 `find` 命令的 `-exec` 操作后面，可以用 \`;` 或 `+` 结束。

* 当使用 \`;` 结束时，对每个匹配到的文件，`find` 命令都会执行一次 `-exec` 后面指定的命令。如果找到了100个文件，那么命令就会执行100次。
* 当使用 `+` 结束时，`find` 命令会尽可能多地将匹配的文件名作为参数一次性传递给 `-exec` 后面指定的命令，这样命令可能只执行一次。

`+` 的方式通常更为高效，因为它减少了需要执行的命令的次数。然而，并非所有的命令都能接受多个文件作为参数，对于这种情况就需要使用 \`;` 的方式。

## find 正则表达式搜索

`-regex` 选项可以使用正则表达式进行搜索，而不仅仅是简单的文件名匹配。例如要查找png或者jpg结尾的文件。

```
find / -regex ".*\.\(jpg\|png\)$"
```

会同时找到所有的 `.jpg` 和 `.png` 文件，满足更复杂的查找需求。

## 如何解决文件名存在空格导致的报错？

比如查找文件的前10行是否包含@字符，如果文件名中包含空格，使用下面命令会出现报错。

```
find ./ -maxdepth 1 -name "*.txt" -exec sh -c 'head -10 $1 | grep -qF "@" && ls -lh $1 ' _ {} \;
```

![](https://zgao.top/wp-content/uploads/2023/09/image-24-1024x422.png)

正确的写法是文件名占位符加上双引号。

```
find ./ -maxdepth 1 -name "*.txt" -exec sh -c 'head -10 "$1" | grep -qF "@" && ls -lh "$1" ' _ {} \;
```

![](https://zgao.top/wp-content/uploads/2023/09/image-25-1024x323.png)

## 如何在-exec sh -c ‘command’ 中嵌套使用单引号？

例如想在-exec 中嵌套使用sed这里必须用到单引号的场景

```
sed -i 's/\t/ /g' inputfile
```

可以这样写。

```
find . -name "*.txt" -exec sh -c 'sed -i '\''s/\t/ /g'\'' {}' \;
```

在每个单引号之前再加上一个  **‘\’**

Post Views: 1,187

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/find%E5%91%BD%E4%BB%A4%E5%9C%A8%E5%BA%94%E6%80%A5%E4%B8%AD%E7%9...