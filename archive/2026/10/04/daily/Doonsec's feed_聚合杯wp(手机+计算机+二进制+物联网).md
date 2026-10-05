---
title: 聚合杯wp(手机+计算机+二进制+物联网)
url: https://mp.weixin.qq.com/s/dNKcqJFLl_8LpOz_c8BT8A
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:54:43.514507
---

# 聚合杯wp(手机+计算机+二进制+物联网)

# 聚合杯wp(手机+计算机+二进制+物联网)

原创

Qiuguo
Qiuguo

沉思安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

vc密码`2026JuheCup@SZ86#Jie46`

## 手机取证

1. **请分析手机检材，该设备对应的Android ID是什么？【答案格式：abcd12345ssd55135】**

**67e76c8034b21156**

![image-20260810211011666](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2uviaYfJCOI4qxUyXIC1Saib33Rz1BKdLRc6LaZX6aGATVhSLU9D9CqMck7ib7N8TP2b0aRso4MYMqzuRge3v2e29AIEQiblMedBicibQ/640?wx_fmt=png&from=appmsg)

2. **请分析手机检材，设备最后连接SSID为“JHTJ”无线网络的时间是什么？【答案格式：2000-01-01 01:01:01】**

**2026-05-11 12:52:46**

打开wifi，发现最后自动/手动连接时间都是空的

![image-20260810211021548](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2usiaXEurSiatJcJofRO9g9EmeuwrXUTQRU96KyicLof2wBmOiaibcgJianm9ZviaIkP0M86kdelejWIJlhbwB6e0oRIY2pMqbibDk3mJ3A/640?wx_fmt=png&from=appmsg)

右键-预览源文件，里面可以看到

code

<long name="LastConnectedTime" value="1778475166127" />

![image-20260811132629792](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2uuHM9zeLgW1PVTTxSgMiaE2uiaZAFNS3Ac2ar15dzZsiarOkfML4y5QwvmwBx0FQj6saMNZg5Qexf5xFQ6hrxNIAjROpsOcABuaHw/640?wx_fmt=png&from=appmsg)

转换一下时间戳，得到答案

3. **请分析手机检材，6月4日中签结果里“通合发债”对应的认购资金为多少元？【答案格式： 100】**

**1000**

比赛时全局搜索“通合发债”没命中，估计就是在图片里面了

当时比赛没找到，参考鱼影安全大佬的wp：

userdata.tar/userdata/data/data/com.ume.browser.hs/cache/image\_manager\_disk\_cache/dd324409382f45b802cecee724c27cd40c0aafd1debf43b7b4540241cee06573.0

![image-20260906162756804](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2uvl3RUZm0IhraaOGah74IzrSkIibIbicnASz0sjLUQqXFEhbUTzkcwSM9RORy0D84Mn4S4fCRCmiao3BwfvJWicliay8hic28RjE1uxk/640?wx_fmt=png&from=appmsg)

4. **请分析手机检材，找到存有AI软件生成提示词的文件，该文件的 MD5 哈希值是什么，取后6位？【答案格式：012345，小写】**

**e075be**

翻找data/media/0/

![image-20260811135331387](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2utVyhPqBwu6G1OqUjs6oFS1zuNF371OW5JjLZItgzRmz0RA4ItmbR55cq9DKXE5GTn8iaYC9SlS8K9dbQGslCkrIkW5qPnCePPY/640?wx_fmt=png&from=appmsg)

可以看到这是提示词文件

全局搜索“提示词”也可以找到

![image-20260908162221707](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2uuKFkUOqJe6TE9Jich5Df5Ux1wPyGBwtY9lyxQJ5T3P0rqrhPWS1C01U2s4WejibLrZTyHD0CQyFTnYCSZRawY7A7lfqJx2viaZEc/640?wx_fmt=png&from=appmsg)

5. **请分析手机检材，嫌疑人登录 “简记事” APP 所使用的邮箱账号是什么？【答案格式： abcdefghij@abcdef.com】**

**epka1dbwic@lnovic.com**

方法一：翻文件

userdata.tar/userdata/data/media/0/Android/data/com.minggo.notebook/files/MNoteBook/cache/cache\_defaultuser.data

![image-20260811140929832](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2usPNib9Ft0ibJxqx680brEynGMBxQib2AnhicaNu4ZY6temNiaayFaKapyH17Y9W1qNnvwGFibmEA9aVo38xVl0bY8bwfqRacya8kjOg/640?wx_fmt=png&from=appmsg)

方法二：手机仿真（方法详见之前盘古石取证那篇文章）

![image-20260811141130913](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2uspUSDhWYAUjSOLMx2NHPAS4ia3KxVVPwQcsg4LVXRj6kZsRj1fs90G8domHY8ZTicBLXAHrMaXKomSat7ibYwYAk8Zd5jw8iao4Go/640?wx_fmt=png&from=appmsg)

打开之后，设置里面可以看到名字很像邮箱，比赛现场看到这直接当答案上就行了

6. **请分析手机检材，嫌疑人使用DeepSeek生成挖矿赚大钱短视频提示词的时间是什么？【答案格式：yyyymmdd】**

**20260519**

翻开就能看到

![image-20260906165731000](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2utVVpBaLqR2fMOrwUrjpfyr9Qxn9WyUuaUSKN7FiadGdqDRqlKxmvM22l8oEyA40M6CKxGTqlbNfyic8fhZBf7dPRhQ36GW0ic2ibI/640?wx_fmt=png&from=appmsg)

7. **请分析手机检材，嫌疑人通过AI视频生成软件一共制作了多少条视频？【答案格式：8】**

**3**

其实比赛的时候翻相册只翻出来两个，当时也没太多时间去看，再结合下一题猜了一下

此处还是参考鱼影安全

userdata.tar/userdata/data/data/com.bytedance.dreamina/databases/dreamina.db

![image-20260906172908338](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2utPpLHYSPlqhUbgyibhWjibHTLfnqDDPkrO5zc4TZLTR37KO6E4tvXGYABu17G12tC278kKzZLKIddLK4x6ehT1dic0qmb6PibQMlk/640?wx_fmt=png&from=appmsg)

aigc\_data即AI Generated Content，一共是三条数据

8. **请分析手机检材，嫌疑人利用AI工具生成的视频里，有多少个被下载保存至本地？【答案格式：8】**

**2**

这个翻过相册，只有两个，也可以看数据库

![image-20260906173147234](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2usTiamYCWL5o6ts6dCjefnbwsiaQ07Alq6l8FryrznibjE0Wv8iaKRg7k0IJ5Ot7ygUkib0dRzqDdUiagibCnLZXzx9bTpkX0ibv4If0ZE/640?wx_fmt=png&from=appmsg)

这里看似有4个，其实只有两个视频，剩下的2个是视频的详细信息之类的文件

9. **请分析手机检材，history\_record\_id为35243399821068的视频生成所使用的模型名称是什么？【答案格式：seedance1.5pro，去除中间空格，所有字母均为小写】**

**seedance1.0fast**

同7题dreamina.db

![image-20260907102944007](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2uvh83b9Xia0tSMUg6FUuzFMmBVFn29oMZ3gRPQFVj1ZSlibfKeIVPL5JYXYEhgL0j8IB3D78Wtib2wTmLsZeNiashxTgwfheCBwGR0/640?wx_fmt=png&from=appmsg)

10. **请分析手机检材，嫌疑人用于引流的直播软件名称是什么？【答案格式：抖音】**

    **播城**

    找到这样一个可疑的软件，下载下来发现就是用来直播的软件

    ![image-20260907103709238](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2usLHzyPqicNBkibicnNscM7YcAQ2k0b0qI9q8h9rHic7Px45WMWvRibaYfM8qFl3XA8y6oaqZ5ZlAWJ1ia66Bu58ib9vOz3fJQFyC60ibw/640?wx_fmt=png&from=appmsg)
11. **请分析手机检材，直播软件内与昵称“默认昵称1921”的粉丝的聊天记录中，发送失败的消息共有多少条？【答案格式：8】**

    **1**

    其实仿真起来很容易就能看到，发送失败的有1条

    ![image-20260907103857600](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2uuvJqVtic0qrBxTicPR4seicCjBdBwFGfphCYSZpLjEmoo4Hdv2xqjr7L6ibXJXg6wheT9vKhyQz1V91Irz4cMUia829Xdr3nt121OE/640?wx_fmt=png&from=appmsg)

    但是下面这个不知道为啥不算发送失败

    ![image-20260907104652863](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2uvyjAu0hID2ezrFvXlfwvic0IHibgicye4EAGWcSesxF3fXwQKo5iagO3gzvQkf810KAZ4oyuruGtbicj2SPuVqTM4aWqxBxug02tOw/640?wx_fmt=png&from=appmsg)

    比赛的时候断网，仿真起来也看不到（弹出需要联网），只能翻数据库

    一开始以为发过两次的消息就是发送失败的，数出来有3个

    ![image-20260907111555072](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2uvKFZQnyulKaxqIX5ypyet2iaW9lHBURT9nHueFkib8LZRUoVlWzqwR2aGR2J36zkrdj3xTLliaapXccpzyVphZOyoYOE9D2zjrEU/640?wx_fmt=png&from=appmsg)

    这个status没看懂，2是发送成功，

    4为啥没显示在聊天记录？可能是删除

    7应该是系统默认发送的消息，证据就是上面的 ”默认昵称3971 关注了你“也是7

    AI分析说status为4是发送失败，阿巴阿巴，感觉有点争议吧
12. **请分析手机检材，售卖API服务的网站对应的端口号是什么？【答案格式：12345】**

    **27974**

    ![image-20260907112508108](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2us1LjntuPTVTZ73Umj1cOiciaLJbsuBeQaX2fJPzbNibGdhiamzr044kibDMCia1ibxj0kPfBEekWTIbicvWLNAuV7kJyABdFQ4fEvnBHs/640?wx_fmt=png&from=appmsg)

    ![image-20260907112539188](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2usxwtffr2oMDJ9Kgr1BrraeOIBX7obRSY43MiaclFj7PQ1TBcN80GJwgRqb7ib84qf4Uww3lFImxBOamLYD5gQpNuiaQdZJMTBJos/640?wx_fmt=png&from=appmsg)
13. **请分析手机检材，嫌疑人在直播软件中搜索过的关键词是什么？【答案格式：日入过万】**

    **如何引流**

    ![image-20260907112603740](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2uvbj4Ogs9LDzHmjMdY13qvYZtY8qJHuPCyiaFg1EB10PmutcIMVV292UkBnGfO0NWMLanibJtEeQJkob13ibDZ8f4ibliaRyLyKGNcg/640?wx_fmt=png&from=appmsg)

    userdata.tar/userdata/data/data/com.dbbjt.phonelive/files/mmkv/dbb\_ugc\_editor\_home\_history\_biz

    ![image-20260907113007012](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2usnf3poEJ6Bun3JiaY6qSFSCpwSgP3z4UFjJ9u1evZvxMicFv2iadzVCTIWkDY0cNDXOxID7kYLicxDvDNhxQuyP8hDrfd00hAwibx0/640?wx_fmt=png&from=appmsg)
14. **请分析手机检材，设备内安装的文件加密工具对应的应用包名是什么？【答案格式：com.tencent.com】**

    **com.aijiami.cn**

    名字就叫我爱加密，很明显了
15. **请分析手机检材，接上题，该加密软件所使用的加密方式是什么？【答案格式：md5】**

    **AES-256-CBC**

    ![image-20260907113203105](https://mmbiz.qpic.cn/mmbiz_png/tNS6iaKdc2uuozS2aGyKLXatwHo9Zcx3Hq381MiaiajNuGib0N63Kv7E24HI45ia9hBlicM6GUkuyKamTJ0giaXZIWrUzbqcb63Lvsib9ic7uicy9qy44/640?wx_fmt=png&from=appmsg)
16. **请分析手机检材，直播素材文件对应的加密密码是什么？【答案格式：根据实际值填写】**

    **JHCUP@20260604**

    吴少还是太超模了，赛场上这都能找到

    答案藏在音频里面

    userdata.tar/userdata/data/media/0/Recordings/record.wav

    内容大致为“我的KeePassDroid密码为JHCUP@2026，字母全部为大写”

    ![image-20260907184016622](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2utm4ibh2q9zuAjylIeHXia3pUUzvGWH0tASrhFwyTf9sibWK2ZaNkerOdM6SyBicY5orVtX0pdd91kQ9pBeDdmzKpjqAoC0IGPiaopY/640?wx_fmt=png&from=appmsg)

    然后用keepass密码数据库文件，搜索后缀为.kdbx即可

    userdata.tar\userdata\data\media\0\backup\keepass.kdbx

    解密出来

    ![image-20260908085234560](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2utgYPBFEVTWquYXCYJuOLuqkMNzeibWqnqzjRx0sx6Musicc9SfFm51biaZHCF7A004APYfX0MIgFclVZtPv8PDC4XgD9qjwjrUto/640?wx_fmt=png&from=appmsg)
17. **请分析手机检材，使用加解密软件解密后的文件后缀名是什么？【答案格式：txt】**

    **decrypted？mp4？tmp？**

    加密逻辑是：如果解密文件后缀是.encrypted，那么就恢复到原来的后缀，如1.png.encrypted→1.png

    但如果源文件后缀没有.encrypted，解密后会加上.decrypted，如1.png→1.png.decrypted

    ![image-20260907201025072](https://mmbiz.qpic.cn/sz_mmbiz_png/tNS6iaKdc2usbJj5lriaERzibICxHXNMWicBXqP0OX8jS5RU0zzSP8F0Ksyp990hAMVxeIbMR1Xf2lcia0g4rUwVePjT4eia0Gmicjyic27ytHSibzyM/640?wx_fmt=png&from=appmsg)

    自己找个文...