---
title: 【CTF脚步】CRC图片宽高-PNG图片高度宽度CRC爆破脚本
url: https://www.secpulse.com/archives/195360.html
source: 安全脉搏
date: 2023-02-07
fetch_date: 2025-10-04T05:50:20.227998
---

# 【CTF脚步】CRC图片宽高-PNG图片高度宽度CRC爆破脚本

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 【CTF脚步】CRC图片宽高-PNG图片高度宽度CRC爆破脚本

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279)

2023-02-06

13,853

# 什么是CRC

这里的CRC指的是CRC32，也就是PNG图片的一个效验位，是一种不可逆运算，类似于MD5，作为数据效验或效验文件的完整性使用。

[![image-20230205022248738.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image-20230205022248738-1024x697.png "image-20230205022248738-1024x697.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image-20230205022248738.png)

使用010 Editor打开一个PNG图片，`89 50 4E 47 0D 0A 1A 0A` (0h行0-7这8个)是PNG的固定文件头（啊？别告诉我还不知道在哪里，第一行粉底白字看到了吧）。

`00 00 00 0D`是文件头数据块标示IDCH。

`49 48 44 52`是IHDR。

接下来第二行前8个hex数据都是表示宽高的：`00 00 07 80 00 00 09 5F`，这里表示宽度为07 80，高度为09 5F，这两组数据转换为10进制就是1920x2399。

`08 02 00 00 00`这5个字节依次为Bit depth，ColorType，Compression method，Filter method，Interlace method

接下来的4组（16个）Hex组成的则是CRC校验码，我这里是`13 97 08 36`

CRC的原理，就是由IDCH和IHDR共十七位字节进行crc计算得到的。

# 爆破宽高

有的CTF题目会修改PNG图片的宽高，这在没有CRC检测的国内软件或Windows的图片看来是正常的。

但是一旦在Linux、MacOs等打开，则会出现报错。

前面提到了CRC的原理，我们借鉴网络上的脚本进行了修改。

```
import struct
import zlib

def hexStr2bytes(s):
    b = b""
    for i in range(0,len(s),2):
        temp = s[i:i+2]
        b +=struct.pack("B",int(temp,16))
    return b

str1="49484452"  # IHDR
width = "0x0780"
height = "0x0095E" # 高度与上面的不统一
str2="0802000000" # Bit depth，ColorType，Compression method，Filter method，Interlace method
crc32 = "0x13970836"
add_num = 2000 # 最大宽高，合理修改快速出flag
bytes1=hexStr2bytes(str1)
bytes2=hexStr2bytes(str2)
wid = int(width,16)
hei = int(height,16)

for w in range(wid,wid+add_num):
    for h in range(hei,hei+add_num):
        width = hex(w)[2:].rjust(8,'0')
        height = hex(h)[2:].rjust(8,'0')
        bytes_temp=hexStr2bytes(width+height)
        if eval(hex(zlib.crc32(bytes1+bytes_temp+bytes2))) == eval(crc32):
            print(hex(w),hex(h))
            break
    if eval(hex(zlib.crc32(bytes1+bytes_temp+bytes2))) == eval(crc32):
        # print(hex(w),hex(h))
        break
```

上面的脚本参考案例（前人）是引用了<https://blog.csdn.net/weixin_44145452/article/details/109612189>，摸着他建的墙，我才得以趟过这条河。

不过也对他的脚步进行了优化和改良，修改了一些代码问题、逻辑问题等。

[![image-20230205030429447.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image-20230205030429447-905x1024.png "image-20230205030429447-905x1024.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/image-20230205030429447.png)

后续我们也会给这个脚本增加到qsnctf库中，努力整合。

**本文作者：[青少年CTF](newpage/author?author_id=49279)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195360.html**](https://www.secpulse.com/archives/195360.html)

Tags: [​CRC](https://www.secpulse.com/archives/tag/%E2%80%8Bcrc)、[MD5](https://www.secpulse.com/archives/tag/md5)、[爆破脚本](https://www.secpulse.com/archives/tag/%E7%88%86%E7%A0%B4%E8%84%9A%E6%9C%AC)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![软件安全之CRC检测](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199210-1681875935-300x144.png)

  软件安全之CRC检测](https://www.secpulse.com/archives/199212.html "详细阅读 软件安全之CRC检测")
* [![《羊了个羊》升级后，黑客们还能过第二关吗？](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/09/1663830914061-300x214.png)

  《羊了个羊》升级后，黑客们还能过第二关吗…](https://www.secpulse.com/archives/187552.html "详细阅读 《羊了个羊》升级后，黑客们还能过第二关吗？")
* [![APP应用安全检测](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/03/1648707513-300x197.png)

  APP应用安全检测](https://www.secpulse.com/archives/176058.html "详细阅读 APP应用安全检测")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670568845919.png)](https://www.secpulse.com/newpage/author?author_id=49279aaa) | [青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279) | |
| 文章数：8 | 积分： 60 |
|  | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](https://www.huodongxing.com/event/5569026023500)

#### 2020-11-29

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 2020-11-27

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect)

#### 2020-09-24

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/event/csdisummit)

#### 2020-09-23

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http://www.energydataexpo.cn)

#### 2020-07-31

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.net.cn/main/detail?postId=83)

#### 2020-04-15

[看雪.安恒 2020 KC...