---
title: DIDCTF-2023龙信杯
url: https://mp.weixin.qq.com/s/fTjEuA_aiyJOhH2MoAe0qg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:28:49.785950
---

# DIDCTF-2023龙信杯

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoa2Bht1MFgEXUlJcIRsDTrD5ibdJoj5ElueVdaxmibmgo02elt8f6odXDg/0?wx_fmt=jpeg)

# DIDCTF-2023龙信杯

原创

北渚

南有禾木

![]()

在小说阅读器中沉浸阅读

# 前言

记录DIDCTF中2023龙信杯的题目，之前只做了流量分析题，这次把题目都做一下。

# **案情介绍**

2023年9月，某公安机关指挥中心接受害人报案：通过即时通讯工具添加认识一位叫“周微”的女人，两人谈论甚欢，确定网上恋爱关系，后邀约裸聊，受害人上钩后，“周微”和受害人进行裸聊，整个过程被涉诈团伙录音录像。同时周倩以自己做直播“涨粉”为由，引导受害人下载其事先制作好的木马APP，受害人安装该APP后，嫌疑人利用录制的视频和受害人的通讯录做要挟，从而实施诈骗。 公安机关接警后，通过技术手段抓取了一段流量包，且通过公安机关的侦查与分析，锁定了该诈骗团伙的业务窝点，据了解，该团伙成员通过Telegram 联系ETH币商收币，双方在线上确定好了交易时间和交易金额（交易额为300万人民币），并先由卖币方转0.5个ETH到买币方钱包。双方人员碰头后，商定分两笔交易交割，第一笔交易价值100万的虚拟货币、第二笔交易价值200万的虚拟货币。第一笔100万的币从卖币方的地址转到中转地址（由中间人控制），再由中转地址转到买币方提供的收币地址，买币方收到币后将带来的100万现金给卖币方清点，第一笔交易完成。 犯罪分子开始第二笔交易时，被警方当场截获。并将相关嫌疑人抓获，扣押安卓手机1部，笔记本电脑1台，调证服务器2台，以上检材以分别制作了镜像。检材清单见附件。请结合案情，对上述检材进行勘验与分析，完成以下题目。

**检材下载**

下载链接：https://pan.baidu.com/s/1ITyZI5uZHrvF7ara0JRNzQ?pwd=8a0z

哈希值：`请查看文件`

挂载/解压密码：`RLEQc2Xe65Q5GiCuRNMFrw==`

**下载附件，压缩包解压后得到dd文件，直接用VeraCrypt挂载。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaFMcCQjT98yOSDXwqNjI0dIp1bot6tzWYzJhtzfLuricRtVdf64PTTOA/640?wx_fmt=png&from=appmsg)

# 手机取证

## 1、分析涉案手机的设备标识是\_\_\_。（标准格式：12345678）

用AXIOM读取提供的镜像什么都没读出来，查阅了一下有人说只有官方提供的工具才能识别这个镜像……

本来准备放弃了，然后突然发现给镜像加个tar后缀，直接解压竟然能得到文件系统：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaclz4IR03SZHlHNCib8IToU3hQ54icZTmMiap2urIpIq9ickzOD39XxDAZw/640?wx_fmt=png&from=appmsg)

找到`\data\com.miui.systemAdSolution\shared_prefs\mi_stat_pref.xml`文件：

```
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <long name="l_t" value="1668587722100" />
    <long name="netSpeedTotalRxBytes" value="981048" />
    <float name="netSpeed" value="0.86430424" />
    <string name="serial">85069625</string>
    <long name="s_t" value="1668587722055" />
    <long name="e_t" value="388297" />
    <long name="net_speed_time_stamp" value="1668594655369" />
</map>
```

标识：`85069625`

## 2、确认嫌疑人首次安装目标 APP 的安装时间是\_\_。（标准格式：2023-09-13.11:32:23）

上面解压镜像得到的文件系统直接导入AXIOM能识别了，那就可以继续了……

看了一圈已安装的应用，感觉就这个`lx.tiantian.com`比较可疑：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoa6ePoGFucQfuI5187nkN4icD87J9ZFxUd8F0e2EKdht21DuqibHhekcPg/640?wx_fmt=png&from=appmsg)

查看其文件夹的创建时间：`2022-11-16 19:11:26`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaRIticMp2adov9sfibP3UAmLN48UmsepK8p7Z0hSbib9GZPiaLycGIW0SYQ/640?wx_fmt=png&from=appmsg)

## 3、此检材共连接过\_\_个 WiFi。（标准格式：1）

共`6`个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaibu691vuSnIkFiah8jTvyDXDlIQia3cvQyXx5FFxxTXWu1nHCiau4Uic5Zw/640?wx_fmt=png&from=appmsg)

## 4、嫌疑人手机短信记录中未读的短信共有\_\_条。（标准格式：12）

原本还发愁怎么知道短信是已读还是未读，然后发现有一列专门标注了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaP7ZQW2ibiaXbMTCTMEvCe5iaqdg2E1loxaP1YA6wpgNqlUOb1g5hiaB1bQ/640?wx_fmt=png&from=appmsg)

数了一下，总共`17`条（这个工具不知道为什么每条会出现两遍，34条除以2就是17条）

## 5、嫌疑人检材手机在浏览器中下载海报背景图的网址是\_\_\_。（标准格式：http://www.baidu.com/admin/index.html）

把几个浏览器的历史记录看了一遍，在夸克中找到了：`http://m.ziyuanhu.com/pics/1725.html`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaCh8c2XjkjtuTZibpHWxQVrqVx3w0EF19AO2TABQehfCPza5sIfhZcGg/640?wx_fmt=png&from=appmsg)

## 6、分析涉案海报的推广 ID 是。（标准格式：123456）

首先访问了那个地址，看到了海报的样式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoa5HA4kXF9icibLHibOicMQpXkCOv72Lz3qRlFBe9UoxVxps1eWLlUZ4YX1A/640?wx_fmt=png&from=appmsg)

然后在镜像的所有图片中找到了这张：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaCBaIzzgXZ7sH9icKRXw8bh2G3rQ6OeeqiaC0gTWZ5vr6MRvCprSt3ASw/640?wx_fmt=png&from=appmsg)

图片中出现了一串数字：`114092`

## 7、嫌疑人通过短信群发去推广 APP，请问收件人中有\_\_个号码是无效的。（标准格式：12）

从短信内容中看到有一个号码是发送失败了的，显示`要发送的号码无法接收彩信`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoao8TGicic89zVCgHNzerFLFCyN2t3zvzlibhW8F2CicW3F8q6yMo0cBbcbA/640?wx_fmt=png&from=appmsg)

所以是`1`个。

## 8、通过分析，嫌疑人推送的微信账号是 \_\_。（标准格式：Lx20230916）

QQ的聊天记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoarcc0ibWd7E2cyYZnbjpNX8Rx9pHsJVNdQpZDcsshBib8bFb8AHvxkCgg/640?wx_fmt=png&from=appmsg)

微信账号：`Gq20221101`

## 9、校验嫌疑人使用的 “变声器” APK 的包名是。（标准格式：com.baidu.com）

从`应用程序活动情况`中看到了变声器：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaUaZJPiaWv8Th8blbod8Bzp3XD41PeIdmzVkvicB0hz7R3WZHYugMfNWg/640?wx_fmt=png&from=appmsg)

所以包名是：`com.chuci.voice`

## 10、号商的联系人注册 APP 的 ID 是\_。（标准格式：12345678）

与号商的联系是在蝙蝠通讯软件里，找到了卖号相关的聊天记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaCibNuwTD0mIVFUld4C1yOdVJbBkWxFQAnict213DkygujKN45Hn8p22w/640?wx_fmt=png&from=appmsg)

卖家的号：`36991915`

## 11、嫌疑人于 2022 年 11 月份在\_\_\_城市。（标准格式：成都）

从手机的相册中的拍摄的照片中找到信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoa2uq0HXgDkZBtXicNcYuGWWpwtCBnPja5djyS0JwosdPib0yicreEMACMQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaWTHblUwwZ3XLFkCZAhykfw10WjqA9GXXAyNmcicxHSfUxv3AHGNL3FQ/640?wx_fmt=png&from=appmsg)

根据图片的经纬度定位到`苏州`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaA6ZiciaRwRO5QzAzBxYvjfKQY1WL2K5DOVRo8gibDLlG7ibHnsE46obMpw/640?wx_fmt=png&from=appmsg)

## 12、嫌疑人共购买\_\_\_个 QQ 号。（标准格式：1）

还是从聊天记录里，先三个，后五个：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaC2iavWziak91zjw5DhHQDjLpxcLeYE6fBOq4Lg6NqY01FKbh6GLokMRQ/640?wx_fmt=png&from=appmsg)

总共`8`个

# APK

## 13、分析手机镜像，导出涉案 apk，此 apk 的 md5 值是。（标准格式：abc123）

首先找到这个APP的安装包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoahBbMYrEINUdd06RibG0YmtkZWYJJeHIAtqJhlibuNrRDE0GkcIGwT0Zw/640?wx_fmt=png&from=appmsg)

这个`market_2.db`是小米的应用市场中安装过的APP的历史记录的文件，`\data\com.xiaomi.market\databases\market_2.db`

从这里面看到source\_dir是`/data/app/~~bHUuRhDnXQeY4lr91PUg_Q==/lx.tiantian.com-xNCYppevFdsIGg_NlIP03A==/base.apk`

这个题问的是md5值，直接这里记录的就有：`d56e1574c1e48375256510c58c2e92e5`

## 14、分析该 apk，apk 的包名是。（标准格式：com.qqj.123）

包名那就是这个package\_name呗：`lx.tiantian.com`

## 15、分析该 apk，app 的内部版本号是 \_\_。（标准格式：1.1）

根据上面找到的路径：`/data/app/~~bHUuRhDnXQeY4lr91PUg_Q==/lx.tiantian.com-xNCYppevFdsIGg_NlIP03A==/base.apk`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaJSwZib1KCGujicjpeFyibSer7SPj2CrH5TPSjr3vaZIxlw0mWyNm5o4Qg/640?wx_fmt=png&from=appmsg)

把它导出来，扔到jadx中，开始分析……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaGlltwpfTmdxib9xwwvlZwyr6Nyu9ibto8bPPFda9nTQmqO8KoADGmyicg/640?wx_fmt=png&from=appmsg)

版本：`1.0`

## 16、分析该 apk，请问该 apk 最高支持运行的安卓版本是\_\_\_。（标准格式：11）

这个其实不懂，然后去查了一下：

```
看 AndroidManifest.xml，这是唯一权威来源。

关键字段
在 AndroidManifest.xml 中，重点看这一行：

<uses-sdk
    android:minSdkVersion="21"
    android:targetSdkVersion="28"
    android:maxSdkVersion="33" />

含义解释：

字段 含义
minSdkVersion 最低支持的 Android 版本
targetSdkVersion 开发时适配的版本
maxSdkVersion 最高支持版本
```

然后找到了这一行：

`<uses-sdk android:minSdkVersion="18" android:targetSdkVersion="32"/>`

然后又查了一下，32对应的就是Android的`12`

## 17、分析该 apk，app 的主函数入口是\_。（标准格式：com.qqj.123.MainActivity）

还是`AndroidManifest.xml`文件，在里面找到了：

`<activity  android:name="lx.tiantian.com.activity.MainActivity"  android:exported="true">`

所以主函数入口：`lx.tiantian.com.activity.MainActivity`

## 18、分析该 apk，请问窃取短信的权限名称是。（标准格式：android.permission.NETWORK）

APP要求的所有权限：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoaHgdP4L2ibTQ0PSIicwnrU1WksrZxbm0icqNzibgZ2bVr135mDu0ibUAQrAQ/640?wx_fmt=png&from=appmsg)

短信相关的就是`android.permission.READ_SMS`

啊，答案竟然是`android.permission.READ_CONTACTS`，contact不是通讯录么

## 19、APP 使用的 OPPO 的 appkey 值是。（标准格式：AB-12345678）

`AndroidManifest.xml`文件的下边：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoam8ic6RDYFibneyniaaic0pIlDasnic36ZSxnTBcUm6yHl36FibF0icRJcGzcQ/640?wx_fmt=png&from=appmsg)

appkey是`OP-264m10v633PC8ws8cwOOc4c0w`

## 20、分析 apk 源码，该 APK 后台地址是。（标准格式：com.qqj.123）

从`MainActivity`中看到了BASE\_URL：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7Nt4w9GAT5hOw1maxVgtDoahYz9icozmCnk8YBIpOYNzEI1DLkY0zxibjxGrYZPspbj7TFo4cg73nzQ/640?wx_fmt=png&from=appms...