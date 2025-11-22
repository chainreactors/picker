---
title: 【万字】一文读懂Android APP抓包和反编译&frida脱壳&APP单/双向认证&Root隐藏绕过技巧
url: https://forum.butian.net/share/4651
source: 奇安信攻防社区
date: 2025-11-21
fetch_date: 2025-11-22T03:07:07.250114
---

# 【万字】一文读懂Android APP抓包和反编译&frida脱壳&APP单/双向认证&Root隐藏绕过技巧

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 【万字】一文读懂Android APP抓包和反编译&frida脱壳&APP单/双向认证&Root隐藏绕过技巧

* [移动安全](https://forum.butian.net/topic/50)

这篇文章主要是写AndroidAPP抓包和反编译&frida脱壳&APP单/双向认证绕过技巧相关的，总字数有一万字了。emmm之前学习安卓APP抓包，包括最近做APP的众测项目多，所以这里抽几天时间给师傅们分享下相关文章，因为网上这方面总结的文章很少，都是很多年前比较老的文章了，所以就想着分享一篇Android APP相关文章。

0x1 前言
------
哈咯，师傅们！这次又又又给大家分享文章来了，这篇文章主要是写AndroidAPP抓包和反编译&amp;frida脱壳&amp;APP单/双向认证绕过技巧相关的，总字数有一万字了。emmm之前学习安卓APP抓包，包括最近做APP的众测项目多，所以这里抽几天时间给师傅们分享下相关文章，因为网上这方面总结的文章很少，都是很多年前比较老的文章了，所以就想着分享一篇Android APP相关文章。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474343-228d21c9-b39f-4781-83c2-1698f2fa30c6.png "null")
然后这里师傅们可以看很多渗透测试工程师岗位的招聘，包括后面的工作中，都是需要移动端，Android、IOS进行相关APP测试。所以这里还是建议师傅们可以多学习下APP相关渗透测试，这个后面也是招聘的一个需求。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474429-cbd303e9-ce49-4576-aa55-2bc2ea2cffc9.png "null")
包括平常我们圈子接的一些渗透测试、众测项目，有时候也会有APP的资产，像这样的很多师傅们都没有真机，没有root，也没有安装一些hook模块插件，就导致很多师傅测试不了，抓不了APP数据包，所以这个还是蛮重要的。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474518-fa490716-c0a2-406c-a5df-566da6490d3a.png "null")
0x2 APP抓包
---------
### 一、浅谈
这里给师傅们来浅谈下APP抓包，因为这篇文章是一个大系列，得先从APP抓包开始写起。
抓包是流量分析的基础，也是安全研究重要的一环。抓包软件有很多种，如 Burpsuite、mitmproxy 以及 Fiddle，抓包方式常见的有设置系统代理、AP 热点抓包、透明代理等。不同方式有不同优缺点，也有不同的应用场景。相信很多安全研究者一定会遇到各种无法抓取流量的问题，本次就来简单总结一下 Android 环境中常用的抓包技术，包括一些应用常用的 SSLpinning、不走系统代理等对抗逆向技术。
这里考虑到很多师傅都是刚学习APP相关的，且没有买真机进行刷机root等操作，所以先拿模拟器给师傅们演示下操作，后续师傅们要是看完文章觉得感兴趣，建议买一个真机来测试下，体验感也是蛮不错的。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474616-7fa58699-bcb0-4b46-9bab-4b467abd2d35.png "null")
### 二、Android各版本抓包区别
Android抓包版本分为：Android&lt;7和Android≥7两个，其中以前的老版本比如Android6抓包是比较简单的，因为他导入证书师傅方便，直接可以把我们抓包工具，比如burpsuit、Yakit等证书直接导入"用户证书"里面即可。
但是Android≥7你这样导入，开启抓包，数据包是走不过去的，因为这样的导入证书方式安卓系统就不信任“用户证书”里面的证书，你直接安装到用户证书是无效的，他只信任“系统证书”里面的证书，并且系统证书都是 xxxx.0 这种格式。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474705-2531be60-39a7-42ce-9859-5f5e632502ed.png "null")
不过可以通过多种方式进行导入证书，上面这个截屏是小黄鸟自带的，导入以后也是使用集成化的xxxx.0格式的证书。需要将证书改造成 xxxxx.0 格式，然后再导入到系统证书里面。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474783-653340c2-2158-4683-b784-5965268e6596.png "null")
成功以后就是下面的样子，在信任凭据中系统和用户都有证书即可。
### 三、安装证书移动模块Move Certificate
#### 1、Move Certificate模块简介
这是一个`Magisk/KernelSU/APatch`模块，用于移动用户证书到系统证书。支持`Android 7-15` 如果手机是官方镜像，可能就需要借助模块，如果是自己编译的直接内置或者`remount`手动移一下就行了。
官方项目GitHub地址：<https://github.com/ys1231/MoveCertificate>，下载最新版本即可使用。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474868-234bcf45-8067-4403-88b1-3b270a8c1d30.png "null")
#### 2、Move Certificate模块安装
首先，我们下载下来以后是一个zip的压缩包。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936474974-1b66a4e8-2a73-4c5f-a708-e47655374895.png "null")
然后这里需要我们师傅们先安装adb功能，直接在自己电脑安装即可，这里师傅们可以直接使用我们下载的模拟器自带的adb，下面我是MUMU模拟器，给大家看下自带的（每个模拟器都自带）：
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475062-059e871f-8c65-43fd-98de-327afa7165af.png "null")
windows的电脑也是一样的，模拟器安装目录下都自带的，然后师傅们可以把这个加入到环境变量中，方便后续直接使用。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475134-f6c6b28b-97bc-4454-a383-3e4d6224dddb.png "null")
adb常用命令，前提得手机和电脑连接统一Wi-Fi，手机且开启了USB调试模式。
```php
~  adb push /MoveCertificate-v1.5.5.zip /sdcard/Download/ //电脑上传文件到手机
~  adb pull /sdcard/Download/ /电脑路径 //从手机上传文件到电脑
~  adb install /AppShare-4.0.5\(370\).apk //直接从电脑端，安装app软件
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475210-92252fd5-caa8-44c8-896f-441d414eb13b.png "null")
### 四、Magisk面具安装
安装了Magisk面具，也就相当于设备进行了root操作了，所以这里需要师傅们进行root操作刷机，可以在网上购买已经刷好了的二手手机，这里推荐Google的pixel3-4和小米的8-10，这几个手机都是公认目前最好用的几个刷机安卓手机了，安装的安卓版本基本上都是10-13之间了，版本太低和版本太高都不好操作，买这几个都是可以的。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475294-dba1fd67-306c-42ef-9776-b680290694e2.png "null")
一般买了像Google的pixel系列手机，大家也基本上知道你是买来做测试机，所以都有免费帮你刷root的服务，直接问卖家即可，发过来我们拿到手就是已经root了的，且Magisk面具都是已经安装好了的。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475365-0113fd3b-9950-4306-8d35-5f7c7a53ac1a.png "null")
然后下面就来给师傅们讲解下模拟器安装Magisk面具的操作，需要一个面具的安装包即可。GitHub下载地址：<https://github.com/topjohnwu/Magisk>
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475454-a439dc97-7fed-4434-afff-6bc0827ced1d.png "null")
下载之后是一个apk的格式，直接利用adb导入手机即可，双击即可安装跟手机一样的操作。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475538-fcbd4764-7a9c-4b84-bced-c60fa8cfa2c9.png "null")
还有一个就是大家常说的狐狸面具，其实功能和上面的一样，只是长的不一样，下面把需要用到的工具都百度网盘打包给大家来，需要的师傅直接下载即可。
```php
通过网盘分享的文件：狐狸面具+LSPosed
链接: https://pan.baidu.com/s/1bzdRMqxJdUb5shtHbervQA?pwd=src6 提取码: src6
--来自百度网盘超级会员v5的分享
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475620-845682be-dc80-4408-805d-411570667f4b.png "null")
安装教程，师傅看这个B站视频即可。
```php
【mumu模拟器root安装面具与lsposed框架，修改机型教程】 https://www.bilibili.com/video/BV1fRaUeGE37/?share\_source=copy\_web&vd\_source=268f8d699ac32cf11e9bdc248399c5bd
```
### 五、burpsuit&amp;Yakit证书生成
#### 1、前期准备
上面已经通过介绍，把证书移动安装模块和Magisk面具都已经安装完成了。现在给师傅们演示下模拟器的操作，然后开启模拟器，方便后面使用adb进行相关操作。
模拟器的硬盘切换成可写系统盘 模式：
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475693-8e90f6f8-24fe-467a-a564-add8411c74b8.png "null")
如果使用`adb devices`查看不到模拟器设备的话，我们可以手动开启一下 ADB：
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475829-fe33138a-ad2a-4af4-87dc-22a4b3467753.png "null")
查看 adb 的连接端口
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936475913-b181bae6-b119-437a-a8ab-d2c8ea32a79b.png "null")
这会开启一个局域网的 adb 连接，我们可以使用 connect 连连模拟器：
```php
adb devices //列出模拟器设备
adb connect 127.0.0.1:16384 //连接
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936476000-3ea6f29e-97cb-44ca-8b02-9dd08f4d549d.png "null")
这里再给大家看下要是真机该怎么操作，这个肯定是首先得root后的安卓手机，首先得一直连续按七次版本号，然后就可以开启开发者模式。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936476077-49dd2661-2153-4ca4-8375-503603fd5aec.png "null")
然后进入开发者模式，开启USB调试功能。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936476161-05e34a81-5103-4861-a26e-23c778e032e7.png "null")
#### 2、证书生成
先讲一个简单的模拟器证书生成和导入，直接不需要知道过程，几条命令就可以直接导入模拟器，进行抓包证书导入。
下载 burp 的证书，并将下载的 der 格式证书转换成 pem 格式，然后转换成 $hash.0 格式，通过 adb push 到模拟器上。
```php
# cer 证书转为 pem 证书
openssl x509 -inform DER -in cacert.der -out cacert.pem
# 获取证书的 hash 值
hash=$(openssl x509 -inform PEM -subject\_hash\_old -in cacert.pem | head -n 1)
# 将 pem 证书改成 hash + .0 的格式
new\_hash="${hash}.0"
mv cacert.pem "$new\_hash"
# 将证书直接放到系统证书文件夹下
adb push "$new\_hash" /system/etc/security/cacerts/
```
上面的操作直接在终端执行即可。
下面的演示，是真机上面的操作，真机且现在安卓版本高点的，都没有那么容易直接导入证书成功的，需要按照下面的步骤来。
Yakit安装证书到移动设备 ，导出证书。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936476229-5a9ef83c-8bcd-44e5-8d57-28e516e89bca.png "null")
下面命令，进行计算证书hash值
```php
openssl x509 -inform PEM -subject\_hash\_old -in yakit证书.crt.pem
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936476301-74e94d02-e6e6-45f6-a2d4-5073b0ffd911.png "null")
然后直接直接重新命名yakit证书.crt.pem ⇒ 10fb1fcc.0，因为安卓≥7手机证书必须得xxxx.0格式的。
下面是burpsuit导出证书
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936476380-a6276183-d325-4aa9-84ac-c2e18293c075.png "null")
导出为cer后缀，所以还需要多一个步骤，改成.pem格式。
```php
openssl x509 -inform DER -in cacert.cer -out cacert.pem //转换格式
openssl x509 -inform PEM -subject\_hash\_old -in cacert.pem //计算证书hash值
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762936476459-22784254-9244-42f5-a342-d3e4fa5acdc4.png "null")
/sdcard/Download/是pixel手机的下载目录，方便查找。
```php
~  adb push /MoveCertificate-v1.5.5.zip /sdcard/Downloa...