---
title: ubuntu下php扩展的曲线救国计划
url: https://h4ck.org.cn/2023/03/ubuntu%e4%b8%8bphp%e6%89%a9%e5%b1%95%e7%9a%84%e6%9b%b2%e7%ba%bf%e6%95%91%e5%9b%bd%e8%ae%a1%e5%88%92/
source: obaby@mars
date: 2023-03-30
fetch_date: 2025-10-04T11:06:19.693649
---

# ubuntu下php扩展的曲线救国计划

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[Linux『Linux』](https://h4ck.org.cn/cats/xtxg/linux%E3%80%8Elinux%E3%80%8F)

# ubuntu下php扩展的曲线救国计划

2023年3月29日
[12 条评论](https://h4ck.org.cn/2023/03/11695#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/75393a5a20868e710f022fcdea2d3576.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/75393a5a20868e710f022fcdea2d3576.jpg)

每次更换服务器，后续都会有很多的事情需要去处理。有的是服务器本身的问题，有的是各种配置问题。所以不到万不得已实在是不想更换服务器，下午看到杜老师的留言提到了litespeed cache，于是登录后台看了一眼，发现原来的redis缓存配置没有生效。问题也很容易定位，那就是没有安装php的redis扩展。正常的话通过apt就可以安装，但是问题出现了，工控机上php 和php-fpm不是同一个版本。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230329220025.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230329220025.png)

通过apt安装直接安装了php8.1版本，php-fpm加载不了。问题是我并不记得安装8版本的php，所以这个版本不知道是什么时候安装上的。其实出现这个问题在最开始配置jieba分词的扩展的时候就发现这个问题了，最终通过把服务器的so文件下载下来直接替换实现的。同理，这次也采用了同样的办法在虚拟机上编译了一个redis.so放到扩展目录配置php.ini实现加载。

既然这个问题解决了，顺便想到了之前后台提示的exif和imagick插件的问题，于是想着一块解决。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230329212305.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230329212305.png)

这个主要是为了解决姐姐的强迫症，不过由于现在的服务器没法创建快照，所以一切操作都得务必小心，免得需要把整个系统重装，那代价就高了。exif通过编译拷贝的方法解决了，但是到了imagic的时候这个办法行不通了：

```
obaby@h4ck:~/lnmp1.9$ sudo lnmp php-fpm restart
+-------------------------------------------+
|    Manager for LNMP, Written by Licess    |
+-------------------------------------------+
|              https://lnmp.org             |
+-------------------------------------------+
Gracefully shutting down php-fpm . done
Starting php-fpm [29-Mar-2023 21:23:31] NOTICE: PHP message: PHP Warning:  PHP Startup: Unable to load dynamic library 'imagick.so' (tried: /usr/local/php/lib/php/extensions/no-debug-non-zts-20190902/imagick.so (libMagickWand-6.Q16.so.6: cannot open shared object file: No such file or directory), /usr/local/php/lib/php/extensions/no-debug-non-zts-20190902/imagick.so.so (/usr/local/php/lib/php/extensions/no-debug-non-zts-20190902/imagick.so.so: cannot open shared object file: No such file or directory)) in Unknown on line 0
 done
```

看提示是缺少libMagickWand-6.Q16.so这个文件，但是搜索了一下并没有找到这个文件。本来就想放弃了，结果看了下虚拟机的日志，发现列出了php-imagic扩展的依赖：

```
dbuser@ubuntu:~/redis-5.2.1$ sudo apt install  php7.4-imagick
Reading package lists... Done
Building dependency tree
Reading state information... Done
Note, selecting 'php-imagick' instead of 'php7.4-imagick'
The following packages were automatically installed and are no longer required:
  linux-headers-5.13.0-39-generic linux-headers-5.15.0-46-generic linux-hwe-5.13-headers-5.13.0-39
  linux-hwe-5.15-headers-5.15.0-46 linux-image-5.13.0-39-generic linux-image-5.15.0-46-generic linux-modules-5.13.0-39-generic
  linux-modules-5.15.0-46-generic linux-modules-extra-5.13.0-39-generic linux-modules-extra-5.15.0-46-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  gsfonts imagemagick-6-common libfftw3-double3 liblqr-1-0 libmagickcore-6.q16-6 libmagickwand-6.q16-6 ttf-dejavu-core
Suggested packages:
  libfftw3-bin libfftw3-dev libmagickcore-6.q16-6-extra
The following NEW packages will be installed:
  gsfonts imagemagick-6-common libfftw3-double3 liblqr-1-0 libmagickcore-6.q16-6 libmagickwand-6.q16-6 php-imagick
  ttf-dejavu-core
0 upgraded, 8 newly installed, 0 to remove and 217 not upgraded.
Need to get 5,987 kB of archives.
After this operation, 16.5 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

关键是这两行：

```
The following additional packages will be installed:
  gsfonts imagemagick-6-common libfftw3-double3 liblqr-1-0 libmagickcore-6.q16-6 libmagickwand-6.q16-6 ttf-dejavu-core
```

既然知道了依赖项，那么就可以直接安装这些组建了(最后一个不需要)：

```
sudo apt install gsfonts imagemagick-6-common libfftw3-double3 liblqr-1-0 libmagickcore-6.q16-6 libmagickwand-6.q16-6
```

安装之后重新启用扩展的imagick扩展就ok啦：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230329214121.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230329214121.png)

已经找不到原有的扩展提示了，通过php探针也可以看到加载的扩展生效了：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230329220943.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230329220943.png)

另外说下几个网页上的方法我都失败了：

1.添加php源 sudo add-apt-repository -r ppa:jczaplicki/xenial-php74-temp

添加之后无法访问，直接删除了

2.源码编译，由于php和php-fpm版本不一致导致编译的扩展没法加载（这个和我的系统环境有关系）

3.使用虚拟机的源替换服务器源（自己探索），最终也是失败了，同样是由于php版本导致的。

```
obaby@h4ck:~/lnmp1.9$ sudo apt install php7.4-fpm
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 php-common : Breaks: php7.4-common but 7.4.3-4ubuntu2.18 is to be installed
E: Unable to correct problems, you have held broken packages.
obaby@h4ck:~/lnmp1.9$ sudo apt install php7.4-common
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 php-common : Breaks: php7.4-common but 7.4.3-4ubuntu2.18 is to be installed
E: Unable to correct problems, you have held broken packages.
```

基本错误是一环套一环，解决不了，所以最终采用了曲线救国的方式，那就是异地编译打包，本地安装配置。整体说来虽然麻烦点，但是问题是解决了。这个目前来说看来就比较ok啦，也没什么太大问题。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《ubuntu下php扩展的曲线救国计划》](https://h4ck.org.cn/2023/03/11695)
\* 本文链接：<https://h4ck.org.cn/2023/03/11695>
\* 短链接：<https://oba.by/?p=11695>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[exif](https://h4ck.org.cn/tags/exif)[imagick](https://h4ck.org.cn/tags/imagick)[php](https://h4ck.org.cn/tags/php)[redis](https://h4ck.org.cn/tags/redis)[ubuntu](https://h4ck.org.cn/tags/ubuntu)

[Previous Post](https://h4ck.org.cn/2023/04/11727)
[Next Post](https://h4ck.org.cn/2023/03/11678)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年3月26日

#### [php-fpm开启opcache缓存](https://h4ck.org.cn/2023/03/11620)

2020年1月13日

#### [ubuntu 18.04 pip3 install mysqlclient](https://h4ck.org.cn/2020/01/6746)

2020年9月13日

#### [更新Blog服务器配置](https://h4ck.org.cn/2020/09/7441)

### 12 comments

1. ![](https://gg.lang.bi/avatar/898a5dc2af6086170c841c729a84c959c7fdc38a0c090e2edc7ebafd0c0ef9c4?s=64&d=identicon&r=r) **[小熊](https://www.saphead.cn/)**说道：

   [2023年3月30日 12:07](h...