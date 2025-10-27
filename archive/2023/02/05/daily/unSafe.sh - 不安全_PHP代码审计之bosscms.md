---
title: PHP代码审计之bosscms
url: https://buaq.net/go-147943.html
source: unSafe.sh - 不安全
date: 2023-02-05
fetch_date: 2025-10-04T05:45:06.601309
---

# PHP代码审计之bosscms

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/4f6099f92f4dcd4ebb8f2a48899f3a9d.jpg)

PHP代码审计之bosscms

路由分析：第一步首先去找到index.php文件，上面定义了一些常量，这里的常量决定了该index.php路由。我们接着去看enter.php文件。
*2023-2-4 12:56:0
Author: [xz.aliyun.com(查看原文)](/jump-147943.htm)
阅读量:33
收藏*

---

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204120829-94e256b2-a441-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204120841-9baf4ac2-a441-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204120857-a5ac9ca0-a441-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204120921-b390dc1e-a441-1.png)

路由分析：

在该文件中定义了一些常量，包含了into.class.php文件并调用了 into 类下的 load() 方
法。我们继续跟进该方法
![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121010-d0cfc466-a441-1.png)

我们继续跟进 load\_class() 方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121039-e2533e3e-a441-1.png)

在load\_class()方法中需要传入四个参数，第一个参数 $type 是判断该功能点是前台功能点还是后台功能
点，也就是决定代码19行的$type路径是在哪个文件夹下，由于SYSTEM\_PATH常量定义为system目录
$mold 参数定位功能目录， $part 决定调用目录下哪个
php文件， $func 则是定位文件下调用的方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121107-f2f22ad4-a441-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121116-f85ca044-a441-1.png)

## 1.ueditor编辑器文件上传漏洞

我们在后台查看功能点的时候，发现一处可以编辑上传类型的地方，这里添加一个允许上传后缀.php，
这里可以添加成功。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121156-100baf50-a442-1.png)

进行.php文件的上传，但这里提示后缀名不允许上传，
这里我们去抓包查看。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121210-18448b1a-a442-1.png)

通过路由找到对应源码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121229-24108f02-a442-1.png)

这里调用了controller.php，6-10行定义了常量也就是路由的走向，通过包含 enter.php 调用路由文件
进行路由选择，也就是我们上面分析的路由。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121250-303e9594-a442-1.png)

通过路由找到功能点文件ueditor.php下ueditor类下的init()方法,上面的路由中传入了
uploadimage ,分支的选择是通过读取config[]来进行选择的，config的内容是从哪里获取的
![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121311-3d08d2bc-a442-1.png)

在类的最上面通过 \_\_construct() 调用 load\_json() 方法进行 config 内容的获取，
继续跟进load\_json()方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121346-51e39762-a442-1.png)

通过前面传入的config.json获取该json文件中的文件内容。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121413-62264714-a442-1.png)

前面action中传入了uploadimage，所以进入了该分支，并调用了上面的uploadimage()方法
我们接着上面继续跟进分支中的uploadimage()方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121435-6eb96da8-a442-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121500-7e0850c6-a442-1.png)

在 uploadimage() 方法中使用$FILES接上上传文件，而这里调用的upload::files()方法才是上传的关
键，我们继续跟进files()方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121528-8ec08fbe-a442-1.png)

向上追溯的时候，我们发现要想上传文件这里需要满足两个条件：

1. in\_array($ext,$extension) ,
2. (!$type || ($type&& !$in) 。
   我们首先去看第一个条件 $ext 在 $extension 数组中，我们继续向上追溯
   ![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121557-9fa7d382-a442-1.png)

从这里我们发现 $ext 是获取我们上传的后缀名，而这里的 $extension 是从哪里获取到的呢
全局搜索 upload\_extension 可以发现该处正是我们上面通过自定义设置的.php后缀，所以
第一个条件是满足的。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121616-ab0c5068-a442-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121634-b625457c-a442-1.png)

而第二个条件 (!$type || ($type && !$in) 我们只需满足一个条件即可 !$type=true 或者
($type=true && !$in=true) ， !$type=true 那么$type的值为NULL即可。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121903-0eedd552-a443-1.png)

我们全局搜索extension中定义的类型，发现extension.json文件中定义了我们上传的类型

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121929-1dfb02ae-a443-1.png)

所以想要实现php文件的上传，我们需要传入的type类型为code才行

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204121946-2895cfd2-a443-1.png)

我们全局查看files()方法调用，发现该处功能点传入的类型中有code，我们跟进该方法进行查看。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122001-31178f74-a443-1.png)

而在uploadfile()方法中就一目了然了，该处调用files()方法并且可以上传code类型下的后缀文件，而
code下包含我们想要上传的.php后缀。所以此处功能点满足上面的两个条件可以实现任意文件上传。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122020-3c9cc7e2-a443-1.png)

### 漏洞复现：

在编辑器上传附件的地方，找到一个使用编辑器的地方，通过附
件上传.php文件，这也就满足了第二个条件此处调用了uploadfile()方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122035-45c5c3dc-a443-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122049-4e1783f4-a443-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122103-55f676b6-a443-1.png)

## 2.任意文件删除漏洞

我们继续查看ueditor.class.php文件时发现该文件下还存在一个delete()方法，这个是编辑
器中删除文件的一个方法，我们去分析一下该方法。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122142-6d547970-a443-1.png)

通过全局搜索store\_type发现该处功能为设置存储方式，默认为0，所以上面默认会走dir类下的delete()
方法。从功能点也不难找到

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122202-7928b2ca-a443-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122209-7dd7d2ba-a443-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122219-8359075e-a443-1.png)

由于在上面只通过正则限制我们开头必须为upload这里很好绕过，我们跟进dir类下的delete()方法查看
该方法：
传入的path参数经过replace()方法后直接进行了unlink()删除，所以我们继续跟进
replace()方法查看该方法是否存在过滤

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122318-a6c98ace-a443-1.png)

这里的replace()方法并未做过滤，而是一些路径的优化。所以这里的path就可以控制造成任意文件删除。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122330-ade981a6-a443-1.png)

### 漏洞复现：

我们可以直接构造出该方法的路由

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122348-b886a0e4-a443-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122355-bd092ab0-a443-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122402-c0e32a78-a443-1.png)

## 3.目录遍历漏洞

我们接着翻找 ueditor.class.php 文件下的方法时，找到一处 lists() 方法，在代码327行处
$folder 参数是通过GET传入且没有进行任何过滤就拼接到$path路径中。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122444-d9c582f2-a443-1.png)

在read()方法中我们可以看到代码129-130行通过opendir()、readdir()打开目录并读取目录中的内容，
而上面的replace()方法我们在上面任意文件删除也进行了分析，是做路径优化的。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122514-ec08f732-a443-1.png)

我们在回到lists()方法中，由于该方法通过路由不能直接调用，所以我们去查看lists()的调用情况，我们
发现有三处调用了lists()方法

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122628-17e02722-a444-1.png)

我们找到一处 listfile() 方法进行分析，在该方法的312行处调用了lists()方法，那这里的传入的
$path参数 config['fileManagerListPath'] 指的是什么呢？

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122648-239ce960-a444-1.png)

我们去全局搜索 fileManagerListPath ，找到该值是upload/路径，也就是说上面要读取的文件是
upload目录下的文件，我们从上面的分析中可以知道lists()方法中传入的 $folder 参数没有进行过滤就
拼接到 $path 中所以这里是存在目录遍历的。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122702-2bfee39c-a444-1.png)

那我们如何进行调用 listfile() 方法实现目录遍历呢，我们知道 ueditor.class.php 的路由是
![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122731-3daf3740-a444-1.png)

通过同级目录下的controller.php进行方法的调用的通过路由我们知道首先要调用这里的init()方法，在该方法中通过传入action参数实现类中方法的调用。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122804-515bc024-a444-1.png)

### 漏洞复现：

使用这个接口进行漏洞复现
GET /system/extend/ueditor/php/controller.php?action=listfile&folder=../../../ HTTP/1.1

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122844-694f8c42-a444-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122855-6fac5c6e-a444-1.png)

## 4.任意文件下载漏洞

在测试功能点的时候我们发现 安全设置- 数据备份- 备份列表- 下载处存在一处任意文件下载，我
们抓包去分析该处下载功能点。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122922-7f7c988e-a444-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230204122932-85c544b6-a444-1.png)

通过上面的路由分析我们不难找到这里的 download() 方法，这里通过66行GET传入 id 参数,在67行将
传入的id参数拼接到路径中，这里的sql为上面定义的路径,最后在代码73行处使用readfile()函数进行文
件读取。

![](https://xzfile.a...