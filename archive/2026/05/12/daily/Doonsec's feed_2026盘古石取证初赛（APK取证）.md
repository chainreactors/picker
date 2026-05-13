---
title: 2026盘古石取证初赛（APK取证）
url: https://mp.weixin.qq.com/s/LzLFYgOPb_G6un2dPZkf5w
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:13.704556
---

# 2026盘古石取证初赛（APK取证）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YdkQKXYKSBhjJzicU57KNqQvAaJotBKmsDVxmDdJDZOBm2Ticcq8TryJvfRftG8pnFvBnQ91zxAx4EbJr6gb9c7DDIicYqaFKVfxGuib71S9YYo/0?wx_fmt=jpeg)

# 2026盘古石取证初赛（APK取证）

原创

玫幽倩
玫幽倩

玫家大院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 题量太大了，不用ai感觉这个apk就能做一天，比赛的时候给ai直接梭完了

## 这边首先感谢鱼哥对本频道的大力支持✌

##

## 题目应该都没问题，至少网站上说都是对的，手机取证错太多了，只能单独放apk取证了

## APK取证

### 1.分析方俊朗phone.E01检材，筛选优质客户应用将用户查询记录存储在一个加密的本地数据库中。请问该加密数据库的文件名是什么？[答案格式：12\_abc.db]

题目说了这边是筛选优质客户，其实和手机取证最后一题一样的，先打开方俊朗的app列表看看

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgrEmvJcSDNVuyYUYrP7rjOSPja7mEcZ8n3xHxdBBVswnGicPQzMjRjOIpgHibiaExhzN7wdCHFGmt24eZb5zqiat49JL9x9zLc720/640?wx_fmt=png&from=appmsg "null")

一看就是这一个软件，我们可以看到包名为：com.example.predictor

根据这个包名我们去/data/data目录下进行搜索即可

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiag1iadzeoBl6HLnlMVZsribXptuZWVBvaLtqaOSgEMCiaWZ5ibA1xwpCaEqHsW5CkX6elO21X4LvWMTV35ZoEfK5u0PNibpB2aUpoc/640?wx_fmt=png&from=appmsg "null")

在/data/data下直接根据包名即可搜索到文件信息，而在/data/app下根据包名搜索即可得到对应apk，这对做APK取证很重要

我们到这个目录之下，题目问加密的本地数据库，那肯定是去databases里边进行查找了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhe4Z1EozyGHSEhy1Tpsut0qecaWBJYXdP9xbloMbQDw8hibGyLl4UWFgRPmZiccfTQ30Zo1HXTqd04ib98HGLgkZGEXxicjXAuUpc/640?wx_fmt=png&from=appmsg "null")

定位到数据库，就一个数据库文件

点一下发现确实加密的

所以文件名就是chat\_history.db

当然也可以去apk里边查找

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaYShDnBcgomzRDhs6OFpr8cE2pw901nxXuoNsS5KEWM4dibYIiaqfDRkYRIwibKyiaaBew8exynddo3pD8N58QuAL0EhfR6bgrB2o/640?wx_fmt=png&from=appmsg "null")

只是不太好找，更适合作为验证项验证答案

### 2.分析方俊朗phone.E01检材，该应用使用了哪种密钥派生算法来生成数据库加密密钥？请写出完整的算法标识名称。[答案格式：DFBDSDFGG123]

问我们这个密钥的派生算法了，那自然需要来看看配置文件并分析一下这一个apk文件了

先看看配置文件

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjDBkHeeDDhJLJiaI53qVuRMIqwdndPkqWGAzGpIPIp8hKzw4ykEpNjTUoIfaWQXaa6DTaaZMoiau5njS1ibia2LKPR0jeiaQyoWm4E/640?wx_fmt=png&from=appmsg "null")

可以看到说是PBKDF2加密，但这边只给了一个密钥版本，不是密钥派生方法，所以我们还是应该去apk查看

像之前说的，我们可以在/data/app下根据包名搜索即可得到对应apk

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjba0JJEsvwJYJRlwxjlWzEQicXLuswNXKTic2eNtO8ednLKuvhEzADwYwz3kJufSB9icmic3VGibr4eE2tgsXbEtD8PMo2SSb8ic8Zc/640?wx_fmt=png&from=appmsg "null")

提取出来放到雷电看看

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBg12Mvq4bQjaEVRiax4ZQFbDgvOXHSM4m2SsyznibT4icWiagich8RFsX1T9v0rWzhOzPyzfCM4wsNZqs42h2I6SQltvRwPw70cozRA/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBg1PjZVeYjMg3kwzQO3EcCe34jTlx61ubORnNQ6HjKCdLef5YMObd8fGtVDO48IqKygUQcEIOtjPRdJWdAfHNsXc6kx0QNFL4I/640?wx_fmt=png&from=appmsg "null")

安装大概界面长这样子，这边可以进行仿真查看，发现有三条记录

但是这三条记录意义不大，因此这边我就不介绍如何仿真的手机apk了，后边有需要再讲，我们还是进jadx看看

发现被加壳了

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgXGx9iaan8eneeDOU4Bo3xtqW0e0J90zgzzDEvj9qCoIibe0hKWxsumnc7HJDBKu3PR6siaLIqHnrMaIAialEDKVoO63OEGJqlfia4/640?wx_fmt=png&from=appmsg "null")

雷电进行脱壳后打开，真是层层加壳啊

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaP5NbAt0JjFBCf8B7Jm2Z6eInaIql0cfxVfP8bfDBLIJmeKQ1GAZAKdLRGsojBc5XicFKpIZBXjV4aZ8ft9SHtq84bH5T5fUPo/640?wx_fmt=png&from=appmsg "null")

搜索PBKDF2后，我们在0x76388f130000\_0x658c.dex找到了关键KeyDeriver

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBggmgG138Qtz1yLhoy4oy6uhvSdVssyEibjyjjM8yn5rCZeKk106SERY6M2eNYqMdy797y2MpVCCEA4ys4opZsKGmzvMfyBhMics/640?wx_fmt=png&from=appmsg "null")

在这边我们看到了整个主密钥的派生方法，获取三个盐值，组合种子，然后创建PBKDF2密钥

当然对于本题来说核心的还是这一句

```
SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
```

这是获取PBKDF2密钥工厂的实例，所以完整的算法标识名称是PBKDF2WithHmacSHA256

### 3.分析方俊朗phone.E01检材，该应用的密钥派生过程中使用了多少次迭代运算？[答案格式：345678]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiagib8Zg7JOicEs9YHIFyDOos2OQPvZ2NdmI0Ric74S5XfMU2u5cKYO7JcM0cxkeFLX0vop0ZwXdRia1kyq1kSTk9AOdxJufcG7w8I/640?wx_fmt=png&from=appmsg "null")

在上一题的配置文件/data/data/com.example.predictor/shared\_prefs/app\_config.xml可以看到这边写的很明确是进行了10000次迭代

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBialuumZdEwSkkvibZmwme5bf3bibSIGszuiah3m2JmGMv6fE4Pczia7pticUnQqmY2ibhAlHonibuyqKG3cfyzzbF6EKicWkpQqFibkgCuw/640?wx_fmt=png&from=appmsg "null")

当然apk里也自然有对应的记录存在

### 4.分析方俊朗phone.E01检材，该应用检测动态调试工具时探测了哪个本地端口号？[答案格式：64321]

后边的apk分析全部需要先脱壳再说

这边既然说是本地端口号，先搜一下127.0.0.1看看有没有收获

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjn94PT7pskrr0DLWhbOLFDnicdV2VESbqREdolPo6efUc6dzd0hPaiaia8p1Gleaug0zKAyLw5YTyf62aB5WibK8UynuOZR2IrLLk/640?wx_fmt=png&from=appmsg "null")

过滤出来两个端口

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhv1Z3IP3s1cwXqWxqdicAiazicRONkWLBH0eApicJ6l3QS0mic6YkSTT5pNMz6icV3X8qQiaq2ONyY8dFnHs7JhuJ2toGV15UOpBoIiak/640?wx_fmt=png&from=appmsg "null")

发现上边那条记录是Utils，是 ConstraintLayout 库内部的调试基础设施，帮助开发者理解和优化布局性能的

所以很大概率是下边那一个

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgg6AonkpuIPIeKM8vdQcU10ibhZDCMYPKreKLcr1s64HlHlnlH9PZjnVicVPwHxxwBlbK87LF5jSoDmA0Ey457hEGgDKyRORyNI/640?wx_fmt=png&from=appmsg "null")

这一个是SecurityManager的类，在反调试反逆向做了关键，很符合题目所说的检测动态调试工具，看上述代码可以看出这就是一个为检测frida注入痕迹的而开的端口，符合题意

所以本题答案即为27042

### 5.分析方俊朗phone.E01检材，该应用密钥由多个"盐值片段"拼接后派生而来。请问第一个盐值片段的具体内容是什么？[答案格式：SAltsaltsalt]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBh6BaMHrwTx37PicRwzGfjdLw6DWG0Uu9lkWsuUjPwY9smyJvhhAKRGPGDf4ZgbRqjuY4enOaZMyCMvJm9bDdEfzxs2y25jeicvs/640?wx_fmt=png&from=appmsg "null")

我们在KeyDeriver已经看到了应用密钥是这样子多个盐值片段拼接后派生而来

问第一个盐值片段，写的很清楚

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBh9kNic65bvWrNTiaSDibyjfnWRTjnHoVZydAvjLDnVbUnMYN8aEsv8Gy4YuJ05DicaDibMAMWdia6Qm4Fo6foL04TDYgWQSZ5nLsyy0/640?wx_fmt=png&from=appmsg "null")

就在下边，所以答案是Pr3d1ct0r

### 6.分析方俊朗phone.E01检材，当密钥派生过程出现异常时，应用会使用一个硬编码的备用密钥。请问该备用密钥的完整内容是什么？[答案格式：salt\_dlefe\_123\_dfefaf]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgsuuWH1bCXqLgv8nLscoTuVwIxZbRRJibibaZT1WAESYbeNn11kmibXHkU97kvBRux1zJnStwnbskftAxj9jr6fn4zdl5udd1bj8/640?wx_fmt=png&from=appmsg "null")

跟上边几题一样，就在密钥派生这部分写了异常的备用密钥，明文写在这边

f4ll8ack\_k3y\_2024\_pr3d1ct0r

### 7.分析方俊朗phone.E01检材，分析"优质客户预测"应用，该应用的安全检测模块通过检查一个特定的类名来判断设备是否安装了Hook框架。请问被检测的完整类名是什么？[答案格式：ru.foefn.DFeoagn.dfoandf.xoggdg]

题目已经说是和Hook框架相关了

因此我们可以对这些Hook框架相关的关键词进行搜索过滤

```
Xposed
Class.forName
Hook
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBg1LZmXtETabvGaDWwDrN38fr1D7Ryz6TrY6gy2o5LxIEPTkBEwXtLbgPL9M55Swsvmzt8qStMPXcwW7d7no6STbnHYwjQ6gdw/640?wx_fmt=png&from=appmsg "null")

发现Xposed存在线索，这是Android平台上最著名的Hook框架之一

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaib7r4QSLwYgEtnxE2tJdXsbFjMflcsDzUKqXVX8xlx2Tqz64XDdEfw6icM4WwtVlfynIo2X2lVwXredNmx8asWVGPSJImXkkMs/640?wx_fmt=png&from=appmsg "null")

步入后马上就能看见安全检测模块正是通过加载类de.robv.android.xposed.XposedBridge来检测是否设备安装了Xposed框架这种Hook框架

其实就在第四题的SecurityManager下边，毕竟都是作为安全检测，都在一起

所以这一题的答案是de.robv.android.xposed.XposedBridge

### 8.分析方俊朗phone.E01检材，该应用在偏好设置文件中存储了一个密钥校验值。请问存储该校验值的键名（key）是什么？[答案格式：ab\_dfefegad\_cadfeg]

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhXn7KcHDBFec7MybBdl8icZl9j0MrVE9Dg6ibeqeHdzG3JWd6Dn2gaBcXlnIwxh4ON7eDbV6bTJxSicZYhXH4Mg0tV7wLQ9vNYia0/640?wx_fmt=png&from=appmsg "null")

我们在一开始的配置文件这边可以看到类似字段

后边跟着一串值，key的名字是db\_integrity\_check，但不能确定这就是密钥检验值

我们得在jadx里边确认一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgic2ic0ZibOOsrl4DhS8KBNzYFQGZcvhdZ0tbH4ENU8CJia4DlOiaVCo3Y9KzU6c7MSbc7GaB95MYho3xcn2voaB8Bo3KL2ZmX7lbg/640?wx_fmt=png&from=appmsg "null")

搜索后可以在KeyDeriver找到它

可以看到这边是获取了MD5算法实例后，与key一起计算MD5散列值

```
"db_integrity_check", checksum
```

明显是把密钥检验值checksum放到了key：db\_integrity\_check中，所以本题答案是db\_integrity\_check

### 9.分析方俊朗phone.E01检材，该应用加密数据库中存储对话记录的数据表名是什么？[答案格式：liaotian\_dfelge]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiatyns7kOOEXicXEicCTwzQrTl2V81SWOia9tBKunoThlehOtZqpaiasc3VoeLibqa0IaPXdf1keZgxV9DB8lLyWn6cRPjiaeybXDsYs/640?wx_fmt=png&from=appmsg "null")

题目已经指明了本题的目标是这个应用的加密数据库

我们很容易就能在data路径下找到这个软件的/databases/chat\_history.db

但是不知道密码一下子打不开，我们去jadx看看能不能找到相关线索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaribgBMicRrUwkV1griaIIHia6yNsKGEaMWoOPcIUfMAqKSSuaQPnNXOMNqFuPFfvFso1qwDhOibibArhZsXpVExJkvic60kzBZgnxiaU/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBia9lpFfoCeA0TBedjRBPwI4oJeALicc2DhtcrfibicicdkV1uypQtVkrwMAiapAdWM0Y3Sq4W8WTGOGjgLq5guVYGfeKuiaibZBQ2LRoQ/640?wx_fmt=png&from=appmsg "null")

发现...