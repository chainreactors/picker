---
title: 渗透测试|CobaltStrike-[Cat]-4.5-兔年快乐-猫猫版
url: https://www.nctry.com/2689.html
source: TRY博客
date: 2023-01-30
fetch_date: 2025-10-04T05:09:16.265908
---

# 渗透测试|CobaltStrike-[Cat]-4.5-兔年快乐-猫猫版

[![TRY博客](https://www.nctry.com/wp-content/uploads/2018/11/20181120_091128_42.png)](https://www.nctry.com)

* [随手记](https://www.nctry.com/xjb)
* [渗透学习](https://www.nctry.com/category/hacker)
* [本站友好作者](https://www.nctry.com/%E6%9C%AC%E7%AB%99%E5%8F%8B%E5%A5%BD%E4%BD%9C%E8%80%85)
* [隐私政策](https://www.nctry.com/privacy)
* [关于站长](https://www.nctry.com/about)
* [友链](https://www.nctry.com/link)

# 渗透测试|CobaltStrike-[Cat]-4.5-兔年快乐-猫猫版

[TRY](https://www.nctry.com/2689.html)

2023-01-29

384,194

[1,255](https://www.nctry.com/2689.html#comments)

# 至少我们曾经在一起过。

来自：一言

## CobaltStrike-[Cat]-4.5-兔年快乐

Ps:猫猫Cs:基于CobaltStrike4.5二开完成 (原dogcs4.4二开功能基本都有)

先祝大家新年快乐,去年推出了dogcs4.4,有很多朋友想要4.5版本的,就发布了个猫猫cs,自定义属于你自己的CobaltStrike,方便一些不会二开的朋友使用～

By: T00ls.com

## 相关配置

Java版本:11 运行前请先配置CatClient.properties

## 客户端

**github下载的自带java11环境,直接运行runcatcs.vbs即可(仅限windows),其他系统执行:java -jar cat\_client.jar client**

##### 配置文件说明(CatClient.properties)

| 配置名 | 配置说明 |
| --- | --- |
| CatClient.Version | 自定义版本号,需要和服务端一致.(别人拿到这个版本的cs信息,如果版本号不对,也无法登录TeamSever):String |
| CatClient.OpenAuth | 是否开启auth验证,需要和服务端对应(开启后安全性较高,但是客户端无法断线重连)：true,false |
| CatClient.InjectSelf | 是否注入自身,开启的话Desktop，Keylogger,Hashdump,PortScan,Mimikatz,PowerShellUnmanaged,Printscreen,Screenshot,Screenwatch会注入自身(开启后无法适配geacon\_pro)：true,false |
| CatClient.theme | 客户端主题配置,0是原版,1是白色,2是黑色 |
| CatClient.ini\_name | 自定义配置文件存放名称,防止被蜜罐读取 |
| stager.checksum-num | 关于stager的相关配置(强烈建议用profile文件自定义url) |
| stager.x86-num | 客户端和服务器需一致 |
| stager.x86-uri-len | 客户端和服务器需一致 |
| stager.x64-num | 客户端和服务器需一致 |
| stager.x64-uri-len | 客户端和服务器需一致 |

##### 相关截图

![](https://www.nctry.com/wp-content/uploads/2023/01/1.png)

## 服务端

```
推荐使用ubuntu18运行
sudo apt install openjdk-11-jre-headless
sudo apt install openjdk-11-jdk
```

**需Java11运行，运行前请先配置CatServer.properties**

##### 配置文件说明(CatServer.properties)

| 配置名 | 配置说明 |
| --- | --- |
| CatServer.Version | 自定义版本号,需要和客户端一致.(别人拿到这个版本的cs信息,如果版本号不对,也无法登录TeamSever)，可以是任意字符串 |
| CatServer.port | 服务端端口 |
| CatServer.store | TeamServer证书文件(需放当前目录) |
| CatServer.store-password | 证书密码 |
| CatServer.host | 服务器ip(可随意填写,只是客户端监听时候会默认显示的ip) |
| CatServer.password | 服务端密码 |
| CatServer.profile-name | profile文件名称 |
| CatServer.profile | 使用的profile文件,需放在当前目录下(所以必须使用profile启动) |
| CatServer.auth | 是否开启双重验证,需要和客户端一致:true,false |
| CatServer.authlog | 是否开启登录日志记录(只是在安全码正确,但是密码错误的情况下记录.):true,false |
| CatServer.googleauth | 开启双重验证后,再开启谷歌验证码:true,false |
| CatServer.googlekey | 谷歌二次验证的key(可用java -jar cat\_server.jar google 命令生成) |
| CatServer.safecode | 如果开启双重验证,但是关闭谷歌的话,就会启动安全码,固定不变(限制10位数) |
| CatServer.Iv | AES加密的iv值,方便类似geacon\_pro等重写的项目，限制为16位,切勿乱改,会出现无法上线问题(默认:abcdefghijklmnop) |
| stager.checksum-num | 关于stager的相关配置(强烈建议用profile文件自定义url) |
| stager.x86-num | 客户端和服务器需一致 |
| stager.x86-uri-len | 客户端和服务器需一致 |
| stager.x64-num | 客户端和服务器需一致 |
| stager.x64-uri-len | 客户端和服务器需一致 |

## 相关命令

```
运行服务端:
chmod 755 teamserver
./teamserver

获取google二次验证配置:
java -jar cat_server.jar google
（Ps:将获取到的SecretKey填入服务端配置中,把data:image/jpeg;base64...这一串复制到浏览器中打开,用谷歌验证器扫描）

运行cna脚本

(如果没开启二次验证)
java -jar cat_server.jar script [host] [port] [user] [password] [cna脚本]

(如果开启二次验证)
java -jar cat_server.jar script [host] [port] [user] [password] [二次验证的密码] [cna脚本]
```

## 一些二开说明

1. 去除ListenerConfig中的特征水印
2. 修改Stager Url（checksum8）校验算法
3. 修改默认登录int长度48879,让网上的爆破脚本无法爆破
4. 修改beacon配置信息的默认密钥,不会被默认的脚本获取到配置信息
5. 增加在线主机统计
6. 自定义bypass 360核晶模式:截图,Mimikatz,Hashdump等
7. 去掉遗留的暗桩bug
8. 可自定义修改默认配置文件存放文件名
9. 新加ip归宿地查询
10. 自定义双端版本号
11. 谷歌验证码或者安全码双重验证

## 下载地址

 [Github下载](https://www.nctry.com/go/?url=https://github.com/TryGOTry/CobaltStrike_Cat_4.5)

## 解压密码

此部分已被隐藏

[发表评论](#respond)并
刷新页面后方可查看

本文作者为[TRY](https://www.nctry.com/2689.html)，转载请注明。

[catcs](https://www.nctry.com/tag/catcs) [cobaltstrike](https://www.nctry.com/tag/cobaltstrike) [cs二开](https://www.nctry.com/tag/cs%E4%BA%8C%E5%BC%80)

24人点赞

发表评论
取消回复

昵称（必填）

邮箱（必填）

网址

表情
 图片
 链接
 代码

[x] 接收回复邮件通知
 提交评论

1. ![213](https://sdn.geekzu.org/avatar/a99ec0a7b943136314a883429480df9e?s=50&r=G&d=404 "213")

   213
   Lv 1

   谢谢！

   [#1241](https://www.nctry.com/2689.html/comment-page-63#comment-6901)

   2025-06-12 11:10
   [回复](/2689.html?replytocom=6901#respond)
2. ![chentie](https://sdn.geekzu.org/avatar/8792cbcd796c9768ff985baf5876ff81?s=50&r=G&d=404 "chentie")

   chentie
   Lv 1

   支持

   [#1242](https://www.nctry.com/2689.html/comment-page-63#comment-6910)

   2025-06-15 13:44
   [回复](/2689.html?replytocom=6910#respond)
3. ![xxxr](https://sdn.geekzu.org/avatar/129a73796695cd1bb24b30c13943b21d?s=50&r=G&d=404 "xxxr")

   xxxr
   Lv 1

   支持

   [#1243](https://www.nctry.com/2689.html/comment-page-63#comment-6912)

   2025-06-16 23:48
   [回复](/2689.html?replytocom=6912#respond)
4. ![qq](https://sdn.geekzu.org/avatar/cf42e765a3732978b287e031caa728fa?s=50&r=G&d=404 "qq")

   qq
   Lv 1

   謝謝分享

   [#1244](https://www.nctry.com/2689.html/comment-page-63#comment-6913)

   2025-06-17 15:03
   [回复](/2689.html?replytocom=6913#respond)
5. ![niubo1](https://sdn.geekzu.org/avatar/782830eebd13e10acf3b730518b5ac99?s=50&r=G&d=404 "niubo1")

   niubo1
   Lv 1

   真诚的感博主！！

   [#1245](https://www.nctry.com/2689.html/comment-page-63#comment-6914)

   2025-06-18 03:09
   [回复](/2689.html?replytocom=6914#respond)
6. ![大佬牛皮](https://sdn.geekzu.org/avatar/b2d7d2d13aed54c2ed7feb538b382b42?s=50&r=G&d=404 "大佬牛皮")

   大佬牛皮
   Lv 4

   感谢

   [#1246](https://www.nctry.com/2689.html/comment-page-63#comment-6916)

   2025-06-18 09:53
   [回复](/2689.html?replytocom=6916#respond)
7. ![aaa](https://sdn.geekzu.org/avatar/f5801a220a937a8f558eec133bb897ec?s=50&r=G&d=404 "aaa")

   aaa
   Lv 1

   感谢！！

   [#1247](https://www.nctry.com/2689.html/comment-page-63#comment-6918)

   2025-06-19 16:24
   [回复](/2689.html?replytocom=6918#respond)
8. ![今夜打老虎](https://sdn.geekzu.org/avatar/9535a9e3162dadedaebc56336d3c2c47?s=50&r=G&d=404 "今夜打老虎")

   今夜打老虎
   Lv 1

   求新的下载地址，谢谢佬

   [#1248](https://www.nctry.com/2689.html/comment-page-63#comment-6919)

   2025-06-22 01:59
   [回复](/2689.html?replytocom=6919#respond)
9. ![rva](https://sdn.geekzu.org/avatar/dbd8337834e63bc34916408cd562927c?s=50&r=G&d=404 "rva")

   rva
   Lv 1

   感谢

   [#1249](https://www.nctry.com/2689.html/comment-page-63#comment-6921)

   2025-06-24 17:45
   [回复](/2689.html?replytocom=6921#respond)
10. ![aaa](https://sdn.geekzu.org/avatar/fd6534f5de5909ebfcdc8bdaeb1b8fcd?s=50&r=G&d=404 "aaa")

    aaa
    Lv 1

    感谢！

    [#1250](https://www.nctry.com/2689.html/comment-page-63#comment-6926)

    2025-07-10 00:24
    [回复](/2689.html?replytocom=6926#respond)
11. ![www](https://sdn.geekzu.org/avatar/655fac0f248fae85b73f4d60bc534c68?s=50&r=G&d=404 "www")

    www
    Lv 1

    谢谢分享

    [#1251](https://www.nctry.com/2689.html/comment-page-63#comment-6929)

    2025-07-11 10:11
    [回复](/2689.html?replytocom=6929#respond)
12. ![xiaofm](https://sdn.geekzu.org/avatar/bb26ae6900890325795cd59550ba43ab?s=50&r=G&d=404 "xiaofm")

    xiaofm
    Lv 1

    谢谢分享

    [#1252](https://www.nctry.com/2689.html/comment-page-63#comment-6933)

    2025-07-17 19:04
    [回复](/2689.html?replytocom=6933#respond)
13. ![123](https://sdn.geekzu.org/avatar/b4bf4da9c4a9038c87baa4b01fd42556?s=50&r=G&d=404 "123")

    123
    Lv 1

    感谢大佬分享

    [#1253](https://www.nctry.com/2689.html/comment-page-63#comment-6946)

    2025-08-05 14:49
    [回复](/2689.html?replytocom=6946#respond)

[←](https://www.nctry.com/2689.html/comment-page-62#comments)
[1](https://www.nctry.com/2689.html/comment-page-1#comments)
…
[61](https://www.nctry.com/2689.html/comment-page-61#comments)
[62](https://www.nctry.com/2689.html/comment-page-62#comments)
63

分享

微信

微博

QQ

by:TRY

蜀ICP备18037281号-2| TRY博客 |
Copyright © nctry.com

夜间模式
[ ]

---

100