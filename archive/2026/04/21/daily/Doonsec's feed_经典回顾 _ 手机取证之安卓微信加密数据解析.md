---
title: 经典回顾 | 手机取证之安卓微信加密数据解析
url: https://mp.weixin.qq.com/s/_fJnd364HzmL3sb8jba53g
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:40:16.673572
---

# 经典回顾 | 手机取证之安卓微信加密数据解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GibJafX2SsNpyRsEHHbIm42pc8H6icQl0oXjNSDzks0gcObzznja3k95xbWksJftMRsWia2JTUJqNz0VTvO8YEW2hlDwsrp4Sw46k8ic0zfKJ8I/0?wx_fmt=jpeg)

# 经典回顾 | 手机取证之安卓微信加密数据解析

原创

取证者联盟
取证者联盟

取证者联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前文回顾：[经典回顾 | 手机取证之安卓微信数据分布](https://mp.weixin.qq.com/s?__biz=Mzg4MzEwMDAyNw==&mid=2247485577&idx=1&sn=1eeb810590e7b67e904345550111432a&scene=21#wechat_redirect)

一、EnMicroMsg.db

### EnMicroMsg.db是一个加密的SQLite文件，加密方式已经公开，解密密钥为手机IMEI与微信uin组合后计算其MD5值取前7位，因此只要得到手机的IMEI和微信的uin即可解密。这也是众多手机取证软件所采用的的方法，这里不做赘述。

###

使用sqlcipher打开EnMicroMsg.db，在弹出的窗口中输入密钥，即可看到明文内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNp7cPj1icQhmDUKUIjhERiaGeyCE31fI0w5ywAZ1eJwEKV0kXazrdVxUFY3TqicMryutyCbI5l9Fc9BpjZpv4nRtPqZSibXmMyuwibY/640?wx_fmt=png&from=appmsg)

重要数据表及其字段内容包括：

（1）userinfo：用户基本信息，如微信号（Stevenpi）、昵称（Steven）、qq邮箱（87\*\*\*\*\*08@qq.com）、手机号（186\*\*\*\*1128）、QQ号（87\*\*\*\*\*08）、地区信息（上海虹口）以及个性签名、最近一次登录时间（UNIX时间戳）等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNpvYiaGTdfficCeWWiaJGI9yIlUVLp1HWmXeCokMVScrmlVxfCZ7W8sAECaNnkdXSOGThj40vicicykTIxUSuFoM7riadOxicqKL0Rklo/640?wx_fmt=png&from=appmsg)

（2）userinfo2：其他用户信息，与使用功能数量有关，多则可达数百项，主要包括：

最近登录的微信账号（USERINFO\_LAST\_LOGIN\_USERNAME\_STRING）；

头像小图URL（USERINFO\_SELFINFO\_SMALLIMGURL\_STRING）；

首次安装版本（USERINFO\_INSTALL\_FIRST\_CLIENT\_VERSION\_INT）；

首次安装时间（USERINFO\_INSTALL\_FIRST\_TIME\_LONG）；

数据库大小（USERINFO\_HEAVY\_USER\_REPORT\_TYPE\_DB\_SIZE\_LONG）；

群组数（USERINFO\_HEAVY\_USER\_REPORT\_TYPE\_DB\_CHATROOM\_LONG）；

消息数（USERINFO\_HEAVY\_USER\_REPORT\_TYPE\_DB\_MESSAGE\_LONG）；

通讯对象数（USERINFO\_HEAVY\_USER\_REPORT\_TYPE\_DB\_CONTACT\_LONG）；

会话数（USERINFO\_HEAVY\_USER\_REPORT\_TYPE\_DB\_CONVERSATION\_LONG）；

钱包零钱通余额（USERINFO\_WALLET\_LQT\_ENTRY\_WORDING\_STRING）；

更新时间（USERINFO\_UPDATE\_UPDATE\_TIME\_LONG）；

更新版本（USERINFO\_UPDATE\_UPDATE\_VERION\_LONG）；

最近登录账号头像路径（USERINFO\_LAST\_LOGIN\_AVATAR\_PATH\_STRING）；

最近使用的位置（USERINFO\_LAST\_LOCATION\_STRING）；

实名认证（USERINFO\_WALLET\_RELEAY\_NAME\_BALANCE\_CONTENT\_STRING）；

面对面收款实名（USERINFO\_WALLET\_F2F\_COLLECT\_TRUE\_NAME\_STRING）；

银行卡明细URL（USERINFO\_WALLET\_BANKCARD\_DETAIL\_URL\_STRING）。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNpKOwibnsK6lpkWKzia0Bib6Rfe000purUKdQhEZ4SshM1yuuWyKHlzdoRp0ibrZbqTazQ2BQiaq1DibmYicP2okxia92pUQ9ibwsiczib6oU/640?wx_fmt=png&from=appmsg)

(3) BizChatUserInfo：企业账号信息，包括企业账号ID、名称、该用户在企业中的名称、头像/简介/添加成员链接等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNr34mMMbOzYpUpMOX1wOnPSHxblaFYsJAtxqd0JTHwlrhmoyY17Xh0MQ37I2hp9RCbTucBzYspm6jNSuz3hKFrJbMqDgbF3Uvo/640?wx_fmt=png&from=appmsg)

(4) MediaDuplication：多媒体文件信息，包括文件的MD5值、大小、路径和创建时间等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNrkqbJ88l2ykAvibpxia6wIcs81HmGDQjQWIgC47IiamnWv0OtaUeCxLRkia8njCf1drNWJLDeNtOzuD4y4icYia62FCHx9702uXbvib8/640?wx_fmt=png&from=appmsg)

(5) voiceinfo：语音信息，包括语音文件名称、语音发送者微信号、语音长度以及时间属性等。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNprPGwQhPfIa06TmewxxEMeGbhyUnqLibBJloxVNLO2vvkj6IbfZ1MokGBacFOsjZS8ibl798SxeY9DyOHliagYCr8mY6X9zEUYf0/640?wx_fmt=png&from=appmsg)

(6) ImgInfo2:图片信息，包括消息ID、长度、大图路径、缩略图路径、创建时间、原图MD5等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNq52uAKWDrz30A7EQqJbmW0gdBZ8uVqcxKlquUiaOKJqLQvH8tloh0Q9fEEkLLQmT6qWm50hjnNZwcMOsGWXglZgkmw4m04WO2E/640?wx_fmt=png&from=appmsg)

(7) videoinfo2：视频信息，包括文件名、大小、长度、消息ID、时间属性、对应用户ID（个人或群）等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNrE9bX7gFYTJjcJwicSubuB4ickD9w0w2bcD2c9G3o8iaBTzwuFPKsibOz7wTvMTdvwVNrpeZdKPvMzoECpTmeYOFG9N1VWZHUMz7U/640?wx_fmt=png&from=appmsg)

(8) VideoHash：视频哈希，包括视频文件的大小、创建时间、原始路径等。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNrPYibzNh2blxqns0RZVweSI6hF6viasRWhiacQ4TMgsngIFdFWiaJv6tr5c1IVVYAXboEBcsKYiaEMozzEickVUlKrnHWQ9iczRrgfl8/640?wx_fmt=png&from=appmsg)

(9) WalletUserInfo：钱包用户信息，包括用户的uin（退出登录的为空）、真实姓名、面对面支付链接、零钱通信息、认证类型等。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNryQ0gNMPC6z2ibt7EKWwZ7U7KetlEUGqLlGjVIao3z62cuQbnT1AWdXG8JT8QkF1Z6RB2ITIqAHdYrYVoxlvqsZicHNcRG31kQw/640?wx_fmt=png&from=appmsg)

(10) WalletLuckyMoney：红包信息，包括接收总量、状态、时间等。

(11) WalletBankcard：钱包银行卡信息，包括银行名称、银行卡类型、尾号、单次转账限额、单日转账限额、转账时间等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNpKvtibicxN4icGGReic6ST8ibnPqFDfBzbD3xH3GVSZDoSOvPbMP99cZ4VWJkmYZnTrrBVJURafQmVXpyeqRSvDYjaMiaOgUTN3iaEgA/640?wx_fmt=png&from=appmsg)

(12) bottleinfo1：漂流瓶信息，记录捡到的所有漂流瓶，包括ID、类型、语音长度、文字内容、创建时间等。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNpZLvn6tyiaBkHSicicjXzcxPpH0hhdVWwYKl7qVUlK6ZATInDGG1stUJe92B3KlDEGeBnQ80L7sqBwL2zHrOa5dbYcufJrbJYThM/640?wx_fmt=png&from=appmsg)

(13) bottlemessage：漂流瓶消息，记录进入临时会话窗口的漂流瓶数据，表中内容与上表类似。rbottlecoversation

(14) chatroom：群组，包括群ID、群成员列表（微信号）、显示名（默认显示成员备注名）、群主（微信号），自己的群内备注名等。奇怪的是，该表中没有记录自定义的群名称和群公告。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNpGnhUzm82ILU23jtiaLr0KcM9bNLx7A7mmCYKkibfqabicvIPAMHmY9rCU61C8DRqbIWFEKr4eIBMyMI39BE5Dp0hUI2VicUDfNec/640?wx_fmt=png&from=appmsg)

(15) rconversation：会话，以相同聊天对象的消息合并为一组，包括会话内消息数、会话对象ID（含群ID）、未读消息数、会话时间、内容等。目前conversation表为空，不再存储相关数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNo82iaiaVwOKUdIGAbCK8Shfl80ehF175wWItjrRKz5BWEz14IFZGZWqQAwklgylS6UsjCuQic9uJiajfGnQz3oIn0qTtoMUhqyPicM/640?wx_fmt=png&from=appmsg)

(16) message：聊天记录，包括点对点消息（发送者微信号、消息内容、时间）和群组消息（群ID、消息内容、时间），多媒体文件存储路径等。QQ离线消息单独存储在qmessage表中。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNo1fI3uxlicWGWCRbKQkxLvuia08KSwefz3AZZqc4BxPqGYUAKiaPWeRJ2h2y9XtZmpP6uaXxzV8lFmbb2oictWx7n16LAElYRqSEg/640?wx_fmt=png&from=appmsg)

(17)ContactLabel：联系人标签，主要记录自定义的联系人分组标签，包括标签名、拼音（全称和缩写）以及创建时间等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNowxrdpnzQJVq7lnet9qSMX2xdFm4JsOV82IicwOsvkABlIsatQbAwfJqhHlNHkNNoKicBoE3ZwrsvicUjTXRnrCUlh4Pkfro4voE/640?wx_fmt=png&from=appmsg)

(18)rcontact：通讯对象（与userinfo2中的数量对应），指的是好友、公众号、小程序及群成员去重后的总和，还包括已经被删除的曾经好友。主要字段包括微信号（ID）、别名、备注名、昵称等。目前contact表为空，不再存储相关数据。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNrRRhd162Q6q44Jhs7dm1ecZCmyo4SXIkplGc9ib1jjLzCRWApZmVeVjFyPOg3eNMxLA8NA83KviaAvRDzOl9ry0hokSJjgib5jRI/640?wx_fmt=png&from=appmsg)

上表中，type（类型）字段用于区分对象类型，常见类型对应分类：

|  |  |  |  |
| --- | --- | --- | --- |
| 0 | 小程序 | 1 | 公众号 |
| 2 | 群组 | 3 | 好友 |
| 4 | 群成员 | 6 | 未通过的群好友 |
| 7 | 互为好友的群好友 | 11 | 加入黑名单的人 |
| 33 | 微信应用及辅助功能 | 67 | 设为星标的好友 |
| 256 | 已删除的好友 | 259 | 不让对方看我的朋友圈 |
| 2049 | 自己的公众号 | 32768 | 账号已不存在 |
| 32771 | 可能是小号 | 65539 | 不看对方的朋友圈 |

(19)bottlecontact：漂流瓶联系人，专门存储捡到的漂流瓶主信息，字段与上述通讯对象相同。

(20)DeletedConversationInfo：删除会话信息，包括会话对象微信号或群ID、漂流瓶ID（该功能已取消）及其最近顺序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNoF0fv9wyGCXwCS8lx9XtW1Il2UmYgXOd0lddEugFbhBuMmBRc6OLrEriavVaXTVH7UiamZ8QLqM36niacvZ3a22A5FlBWmZomBc0/640?wx_fmt=png&from=appmsg)

### 二、 enFavorite.db

enFavorite.db文件的解密密钥与EnMicroMsg.db相同，同理解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNrs7Fb5bACTgDeSSKdkkJwl1pHWLkjHy7qXw3tsLpOo33KSs809uHMld0cB8s5Dlpen1icXdmqCtppNactEfVM8XFoDBdAjlpp4/640?wx_fmt=png&from=appmsg)

   关键数据主要集中在FavSearchInfo和FavItemInfo表中，对应分析可以获得收藏内容的本地ID、内容、标签、时间、发送与接收者等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNoRSIZPSHymSVnL6xKkibwPts98uRQV5Whnic9tGU7voMtTmmWN1OAvib6cVw1CmHLhqmwJwWkm7HqD0AXaiagLLpcJs72Yh2dEUOA/640?wx_fmt=png&from=appmsg)

 通过手机取证软件，可以快速友好的获得上述结果：

![](https://mmbiz.qpic.cn/mmbiz_png/GibJafX2SsNrhXUjFE8wmRqBAwRN9BibibibFUiaAcpicLPfiaGyGZBBVhzM4UIeyYL7PCy3rFImLHZ9duiaqbLjiciab4uLd2bS041LtC1Z0f3L1mxdc/640?wx_fmt=png&from=appmsg)

### 三、 WxFileIndex.db

WxFileIndex.db文件的解密密钥也与EnMicroMsg.db相同，同理解密后可以得到如图所示的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GibJafX2SsNpicNBAsGGNPxnSb1QKYIYB8ss1ynRrm1qVsCd18E8Yiakdic6WDa9YsTTFP0WbZfobrkaAkptiadILBVzwcW9p5ck5u5ncV3F9GfI/640?wx_fmt=png&from=appmsg)

该文件记录了微信聊天涉及的文件附件的情况，各字段含义分析如下：

（1）msgId：消息ID，同一来源的记录（点对点聊天时的同一个微信账号或群聊时的同一群）具有同一个ID。

（2）username：发送者，点对点聊天时对应发送者微信号（上图Stevenpi即为发送者微信号），群聊时对应群ID。

（3）msgType：消息类型，每种文件对应一个数字，比如语音音频对应34、图片对应3、文件对应49、视频对应62等等。

（4）msgSubType：消息子类，用于区分同一类型文件的多种形态，如图片的原图、缩略图、预览图等。

（5）path：文件的存储路径。

（6）size：文件大小，大小为0的情况比较常见的是由于缩略图没有点开预览或原图没有下载，也有些记录与微信数据某些生成机制有关。

（7）msgtime：产生该条记录的时间，通过UNIX时间戳记录，转换后可以获得准确的北京时间。

下期预告：手机取证之安卓微信数据恢复

![](https...