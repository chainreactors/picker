---
title: 电信联通手机免流教程（0基础教程） - 阿浩的小破站
url: https://buaq.net/go-145422.html
source: unSafe.sh - 不安全
date: 2023-01-14
fetch_date: 2025-10-04T03:51:14.691216
---

# 电信联通手机免流教程（0基础教程） - 阿浩的小破站

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

![](https://8aqnet.cdn.bcebos.com/98083e00ca938350227b6a5a78ab3214.jpg)

电信联通手机免流教程（0基础教程） - 阿浩的小破站

07/07
*2023-1-13 19:47:48
Author: [www.winhow.top(查看原文)](/jump-145422.htm)
阅读量:57
收藏*

---

![阿浩](data:image/png;base64...)

07/07

本文最后更新于2022年07月07日，已超过189天没有更新，若内容或图片失效，请留言反馈。

#### 注意事项

此教程的内容具有时效性，可以你看到制片教程的时候部分的内容已经失效了，所以请根据实际情况操作。

#### 前言

免流最省钱的是电信，最方便的方法的是联通。至于移动不好意思官方已经把路堵死了，可以如果你的套餐中没有免流的应用你可以考虑新办一张其他运营商的电话卡了。

#### 准备工作

1、一张联通/电信的电话卡

2、一个服务器带宽和流量根据你的用来确定，地区最好是中国内地、香港、台湾、韩国、日本这几个地方，因为这几个地方的延迟比较低，使用起来的体验会比较好。（或者是一个免流的节点）

#### 免流节点搭建（已经有免流节点的可以跳过这步）

连接上服务器后先更换内核开启BBRPlus加速

```
wget -N --no-check-certificate "https://github.000060000.xyz/tcpx.sh" && chmod +x tcpx.sh && ./tcpx.sh   #先选择9进入卸载内核模式，然后再选择5更新内核
```

在安装完成重启服务器的之后可以再次执行上面的命令查看是否开启了BBRPuls加速

再进行v2-ui的安装

```
bash <(curl -Ls https://blog.sprov.xyz/v2-ui.sh)
```

安装完成之后通过 `http://你的IP:65432`  访问面板，默认用户名密码： `admin`
Ps：如果无法访问请看一下防火墙是否放行对应端口
在左侧列表中，选择账号列表，然后点击+添加节点，按照下面添加一个默认的ws节点，端口、路径、请求头先不修改。
![l5b6cxa2.png](https://winhow.top/usr/uploads/2022/07/919766751.png "l5b6cxa2.png")
添加完成之后你可以使用手机的V2rayNG扫描添加节点或者通过链接导入节点测试节点是否可用
![l5b6d7xn.png](https://winhow.top/usr/uploads/2022/07/2367668846.png "l5b6d7xn.png")
点击开启开关后点击测试链接如果是图情况就表示你的节点已经可用了，延时越低你在使用网络是就越流畅
![l5b6djwb.png](https://winhow.top/usr/uploads/2022/07/2778937444.png "l5b6djwb.png")
如果是下面这种情况就表示你的节点有问题， 你需要检查一下
![l5b6dp9a.png](https://winhow.top/usr/uploads/2022/07/3701957981.png "l5b6dp9a.png")

#### 免流配置修改

首先免流是分地区的(按照电话卡办理的地方划分)，不同的省份有不同的要求，所对应的配置也是不一样的，所以要是我的配置你不可以使用可以在网上搜索一下你电话卡归属地的配置。

虽然是免流但是存在跳点（还是会出现一部分流量免流一部分没有免），根据测试得出tcp+http是跳点最少的协议，ws先对来说多一点，一部分还是和免流的host和地区的不同网络情况想对应的

免流的host我可以用你不一定就可以用所以需要自己慢慢的试，或者找同地区的小伙伴看看什么配置比较好

##### 联通免流host列表

```
pull.free.video.10010.com #手厅直播

live.v.wo.cn #沃直播

wscdn.wbalf01.xiaoka.tv #bilibili #22卡

tobe.vip.weibo.com #微博 #bilibili #22卡

cn-fjqz-cmcc-v-02.bilivideo.com #bilibili #22卡

upos-tf-all-js.bilivideo.com #bilibili #22卡

szextshort.weixin.qq.com 80 #联通

wx.qlogo.cn #联通大王卡

dns.weixin.qq.com #大王卡 #腾讯大王卡

vipts.tc.qq.com #大王卡 #腾讯大王卡
```

##### 电信免流host列表

```
a.189.cn #电信停机卡全国通用A

wapzt.189.cn #电信停机卡全国通用B

webwebfenxi.189.cn:9000 #电信停机卡全国通用C

wapsd.189.cn #山东电信停机卡

service.sh.189.cn #上海电信停机卡

wapjx.189.cn #江西电信停机卡

h5.nty.tv189.com #天翼视讯

vod3.nty.tv189.cn #天翼视讯

open.4g.play.cn #爱玩4G

ltetp.tv189.com #爱看4G

hb.10000shequ.com #湖北电信

hb.10000shequ.com:8081 #湖北电信

dy3.nty.tv189.cn 电信天翼

ltewap.tv189.com 电信天翼

tp.nty.tv189.com #电信天翼
```

我以我自己的联通卡为例子，在host的地方填入 `pull.free.video.10010.com` 作为免流的混淆，因为我所在的地区随意的端口都是可以免流的所以我就不改端口的配置，部分地区需要修改成80、8080或者 其他端口才可以免流需要注意。
![l5b6fkis.png](https://winhow.top/usr/uploads/2022/07/2648416951.png "l5b6fkis.png")
保存修改再次将节点导入到软件中测试是否可以连接

再将路由设置中的预定义规则改成全局
![l5b6frj9.png](https://winhow.top/usr/uploads/2022/07/1963823078.png "l5b6frj9.png")
接下来就可以下载一个20M左右的小文件，或者是正常使用一段时间产生一些流量。一个小时之后看看是免流部分是否有增加，如果有免流就会像我一样在免费流量和总部分有增加。
![l5b6fzkf.png](https://winhow.top/usr/uploads/2022/07/310566467.png "l5b6fzkf.png")
一个节点中的host可以添加多个，对应不同运营商你可以添加不同的hots

#### 关于5G是否免流

5G是否免流是大家非常好奇的问题，正常情况下如果你不办理5G流量包，使用5G的手机一样是可以免流的，5G只是一个通信方式只要套餐是4G的就行。

但是如果你的手机号码被加入到了5G SA网络中就一样不免流，在这种情况中无论是你是否使用和5G相关的产品都是不免流的，是否被加入到SA网络中你可以致电客服进行询问。

这里的SA不是指的你手机中的SA是运营商后台中的手机号码计费和流量验证方式，如果开通了就改变了原先的流量计费和验证方式免流自然就失效了。一般开通了就不能取消了，不过听说可以和客服对线取消，这个就各凭能力了。

文章来源: https://www.winhow.top/archives/128/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)