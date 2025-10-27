---
title: 从匆匆的一瞥，到两小时泯灭（SQL注入）
url: https://buaq.net/go-163219.html
source: unSafe.sh - 不安全
date: 2023-05-14
fetch_date: 2025-10-04T11:37:44.812674
---

# 从匆匆的一瞥，到两小时泯灭（SQL注入）

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

![](https://8aqnet.cdn.bcebos.com/7503750e6a125122fd9fcb10f26599a4.jpg)

从匆匆的一瞥，到两小时泯灭（SQL注入）

@TOC昨天晚上分别开了我相识已久的女友，再度回到了单身狗身份，在这个双休的早上，电脑上看完了昨天还未看完的《银河护卫队1》，百无聊赖的打开了某一个网站，想找找是
*2023-5-13 18:36:0
Author: [xz.aliyun.com(查看原文)](/jump-163219.htm)
阅读量:121
收藏*

---

@[TOC](https://xz.aliyun.com/t/%E4%BB%8E%E5%8C%86%E5%8C%86%E7%9A%84%E4%B8%80%E7%9E%A5%EF%BC%8C%E5%88%B0%E4%B8%A4%E5%B0%8F%E6%97%B6%E6%B3%AF%E7%81%AD%EF%BC%88SQL%E6%B3%A8%E5%85%A5%EF%BC%89)

昨天晚上分别开了我相识已久的女友，再度回到了单身狗身份，在这个双休的早上，电脑上看完了昨天还未看完的《银河护卫队1》，百无聊赖的打开了某一个网站，想找找是否有啥好玩的东西，这一看，2个小时就这么没了。。。

## 用户名提示

登录界面在**账号**处，如果输入系统存在的账号，则**用户名**会返回对应的结果，没有则不返回。抓包看一下。

输入**admin**，返回了**admin**。这里我注意到一个参数 **SQL\_WHERE**。那这里我们大胆猜测一下，是不是有可能后面就是跟的要查询的账号名呢，只是这里做了相应处理。需要注意的是，值的最后面有两个`%3D`，这里懂的师傅，已经猜到是**base64**编码的，我当时也是这样想的，就拿去处理一下。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183653-135d24d8-f17a-1.png)
密文：

```
NGFkMzRkZWEyYjgxYzcyMWY0YTg3YTEzYzU5MzJmNTY5YzA3MWVjZDE2MGM3ZjIzZDNmYzliNDg1NTlmZGMxZg%3D%3D
```

第一步处理，UrlDecode解码

```
NGFkMzRkZWEyYjgxYzcyMWY0YTg3YTEzYzU5MzJmNTY5YzA3MWVjZDE2MGM3ZjIzZDNmYzliNDg1NTlmZGMxZg==
```

第二步处理，base64解码

```
4ad34dea2b81c721f4a87a13c5932f569c071ecd160c7f23d3fc9b48559fdc1f
```

这也看不出是个啥加密呀，就想着能不能去F12里找找思路。。

## jsBase64.js文件

打开网站之后按了下F12，看到以下截图，当中的**jsBase64.js**文件让我有了极大的兴趣，因为我看到了 **key** 和 **iv** ，心里咯噔一下，这不是洞就来了嘛。少说也是个配置文件泄露嘛。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183653-139b0db6-f17a-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183654-13df0cf0-f17a-1.png)
想着，既然我都知道这里是`aes`加密了，还暴露了`key`和`iv`，那不是马上就可以反推出刚刚的密文是什么了嘛！咱们说干就干，就将这段代码复制到了新文件中，准备传入明文admin来试试看能不能加密出刚刚的密文来。

## 手搓轮子（python）

突然惊醒，**js**我不会啊，不知道咋穿参进去，而且电脑也没有运行代码的环境，思来想去，js我不会，但是我会点**python**呀。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183654-1421646a-f17a-1.png)
网上参考了点**python**的**aes**解密，整了一个出来。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183654-14606c6e-f17a-1.png)

啪的一下很快啊，当时就给了我一个结果 `AND LOGID=‘admin’`。好家伙，这不是连着查询语句一起写这了嘛，搞不好这里还有SQL注入呢！！

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183655-14a32086-f17a-1.png)
秉着严谨的态度，我再次搞了三条高级测试语句加密之后传过去，探探虚实。

1.AND LOGID='test'
2.AND LOGID='test' AND 1=1
3.AND LOGID='test' AND 1=2
![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183655-14e10e5a-f17a-1.png)

1.1944b419abc5540fbed8e886ea1d68dcdda71cc9b1da8daba6096208727fa36e
2.1944b419abc5540fbed8e886ea1d68dc8c937b7e0c859960291e590322549066
3.1944b419abc5540fbed8e886ea1d68dcfdc8146dc3691809e7b75e7224b6451d

像前面一样，先 **base64编码**，在 **UrlEncode编码**。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183656-15212148-f17a-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183656-155c46ec-f17a-1.png)
![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183656-159d8576-f17a-1.png)

芜湖，起飞。这里**SQL注入**已经妥了。但是这里我应该怎么去弄点库名来证明呢，第一个想到**sqlmap**，但是**sqlmap**的自带**tamper**是没有这样复杂处理的脚本，看来还是只能自己写了。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183657-15cd1ca0-f17a-1.png)

## 反复搓轮子（python-tamper）

先打开了一个自带的脚本（**apostrophemask.py**），看看人家是咋写的。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183657-16090ee0-f17a-1.png)
为了让数据可以直接用，这里需要将 **payload** 做三次处理：

**AES加密**——**Base64编码**——**UrlDecode解码**

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183657-1640c3bc-f17a-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183658-169293ae-f17a-1.png)
哎嘿，跑出来了。武林中人讲究点到为止，关掉看鬼灭之刃去了。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230513183658-16bb5a1e-f17a-1.png)

文章来源: https://xz.aliyun.com/t/12524
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)