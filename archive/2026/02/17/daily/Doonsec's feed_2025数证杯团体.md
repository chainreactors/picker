---
title: 2025数证杯团体
url: https://mp.weixin.qq.com/s/Ex7w6lJgi8qB4ECtskfYxg
source: Doonsec's feed
date: 2026-02-17
fetch_date: 2026-02-18T04:13:47.251559
---

# 2025数证杯团体

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KjibQZESCJoO8s9e4kYhuYdhXcjMMEAekJHcJAaJ7xYAK6bAlbvHgmhWbcxY5PdmsBjiahhyoh84sSlh91HcKMcMPmPJWFkOWaRrjqHHia1DBI/0?wx_fmt=jpeg)

# 2025数证杯团体

Serendipity的小屋

![]()

在小说阅读器中沉浸阅读

编者荐语：

荣幸受邀，还有好多知识不清晰，继续进一步学习。
Serendipity在这里祝大家新年快乐！

以下文章来源于一只mortal
，作者motalSerendipity

![](http://wx.qlogo.cn/mmhead/INk4JvWfe8V01v2IqprKYemViaibo12NfsjbVlFh8Gbwg86ofgHV3n4yNxPVEMk6TbboepUs5ficH0/0)

**一只mortal**
.

取证小白兼职CTF小白

## 容器密码

9@kZ3!xQ7&rT5#sF1%vD8^zA4(mB6)jN2~hY5+gC3dW9=eK7;fX4?vM1[oL6]tR3}uS8iP5\_bH7:zD1"nQ3'pF9lA2|sC6\wE4/rT8=vY1

## 特邀嘉宾：Serendipity

这次邀请特邀嘉宾Serendipity来为我们讲解计算机和移动终端部分！下期邀请神秘嘉宾来讲解EXE逆向部分！

## 负责部分

mortal：服务器，流量分析，数据分析，物联网部分

Serendipity：计算机，移动终端部分

邀请神秘嘉宾来讲解EXE逆向部分！尽请期待！

## 计算机部分

计算机取证请根据计算机检材，回答以下问题：

## 1、请分析计算机检材，计算检材原始磁盘的SHA256校验值为多少。（答案格式：英文全大写）

**4DB6F775FF1B31065F214147479302DEBBA44A88387A4E81FD9F9A3FA88C69E8**

挂载出来直接计算sha256即可，不能直接算镜像的哈希![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoP8mSGuxoSCBtDC6MWvicSNwKYekn4qT8EPtpqAicQzVrWiakc1lq07RrANeYQKwNzdibUxpOawc6TSEmbvYqBcdbIUZ0u2nict41Eg/640?wx_fmt=png&from=appmsg "null")

## 2、请分析计算机检材，用户在2025-10-17 09:19:25通过Everything文件搜索工具打开过哪个文件？请写出其文件名。（答案格式：包含后缀，大小写与实际需一致，如Abc.doc）

**IMG\_20220402\_085728.JPG**

这边在`C:\Users\admin\AppData\Roaming\Everything`中找到everything的搜索记录![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoMgaWGwqjBxJkRvoiaib5vuxITlicUmvQvIAZ0xG6tiariaJdUI1tufcYJbzuYUTVCaDoVYBibLGKWtOlhpVq8noPnbBzcm2m1CII5Lw/640?wx_fmt=png&from=appmsg "null")

打开文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoMRYCzPLscrkjSHibdCBoxtbwFgbnvM1MkyRdJJsoDtHyIKsllz1fJVtSt6sY6UABEXKF4biaEGvnRqzKv0icjib2KQjLgmqEzddr0/640?wx_fmt=png&from=appmsg "null")

得转换一下时间戳，查看哪一个符合题目要求

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoOAHdQR15Bj9kzaDBFOQ6RabATOPHg02joEwjPSGA7Ct4m15bOpza8zPI9F5meeHjsOglaVHEBvxzkmvxOLKEmBQibvfKa2hykw/640?wx_fmt=png&from=appmsg "null")

## 3、请分析计算机检材，驱动人生工具下载过的软件全称为？（答案格式：全民K歌）

**百贝浏览器**

打开驱动人生，在设置中找到软件的下载位置![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoM9WpVI70Sa8rcENsich5VgS0h4ufrQ2nBQf7iaGqibsMjwotvsGfXWsXzib84LgYB64I1icClmBniahYWLyMu1JhMQ512vX12kthZbE/640?wx_fmt=png&from=appmsg "null")

发现是空的，可能是修改路径前下载的![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoM1yGR18SSakxnICG0HagRShJ4cCeibGUG6Rb5iajJKB69RzX2nZkjlHFhrXibVYib8boKo04NL8gnY2Q8iaJdSvqwBjyvYDh4s7GQs/640?wx_fmt=png&from=appmsg "null")

那就打开everything搜索一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoPiaZ7SUq1T0GKGP1bLJR7gPHvkJkawFbjR1CITGCepUCKRF76uGcPovDAS4TsBoupW0Aga6S1mibq78SKbpZvhkdVoNxMg0WeibU/640?wx_fmt=png&from=appmsg "null")

发现C盘也有几个文件夹，挨个访问一下。在`C:\Program Files (x86)\DTLSoft\DriveTheLife`找到一个名为`downloadinfo`的数据库文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoOBGkUTC3E9Wmwiar9WYnO5AQZoyKKec2phHkGCyAb4b965fdEDkRtMexQqL3tiaiaXHdw5PiaiaDvoFHHamtTVpKTsrdFXSyPxJQ4E/640?wx_fmt=png&from=appmsg "null")

在浏览器访问一下这个url，会下载一个文件，打开安装包就是题目所要的答案

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoPtkSS06t2deKN7zrVwHib4BkUj94G2ngADjVk7JHEqyCmIECicia1aia92ia02efx0Pz2WeYxwibMBeVW4aErHXX3KVd2nxuwU3qibZU/640?wx_fmt=png&from=appmsg "null")

第二种方法是直接去找他的数据库

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoNq03M6wZsG3g5gMbQF1xHYm0R0yJz08eMtqL0Ragkq3gHg1BJ53egxgfvhF1v5vjbCia0vU3HBXiae7iacCODgeseAEQjBarttIk/640?wx_fmt=png&from=appmsg "null")

直接用XWF看即可

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoM5HuDu1YjvTxYjGd3dp2VUuOYMFJ8XbiajOYYBcy1UrZicdzlmHGpoMfmazC5Tqd23HlJXsMhDHb8DrlEibskEx3pNZ1icLyaCAWA/640?wx_fmt=png&from=appmsg "null")

## 4、请分析计算机检材，使用夸克浏览器搜索过什么内容？（答案格式：与实际一致）

**北京天气**

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoOrOlsj7YY8HaNicVwMKyWKkJ7t3IQMX28Nbg9797KFuI9vF8hojdsehJ3upZabQQxl84peeHF0uEBOa4mrEg1g2OIjADib0mNrQ/640?wx_fmt=png&from=appmsg "null")

## 5、请分析计算机检材，用户桌面背景的车牌号是多少？（答案格式：Abc123）

**FU86828X**

直接就可以看到

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoP6TsPhJ8lGZpIVZU5SdrFgLaBkNkupHRAebWprRD01jXx0ZkQH1QvmE8ibRoqiclba4qQoplpMAKgHybUaHMSFSicYsictyjSC63c/640?wx_fmt=png&from=appmsg "null")

## 6、请分析计算机检材，找出连接过的远程主机IP是什么？（答案格式：192.168.1.1）

**192.168.50.238**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoOAaiaLowg3JLxgGQ3iagZ46qgiaibDZq7ooSSsdasJeYNy3D9LlWZs5JmYUgkY3ZM52hvTLV1cnq0KXjphLcbSaiaPjsIb6Z8DQrVw/640?wx_fmt=png&from=appmsg "null")

## 7、请分析计算机检材，找出远程主机正在播放的视频内容标题。（答案格式：我为歌狂）

**黑猫警长**

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoPavd5Gu2ibCyMQnhonfhv0uDp2vRMkoGdMdsUUaWc8IrlPyib6iae5L7UAoBQurgjVicDRBa7utKv4mo8m8p5CibrgZofLm8ylzpXk/640?wx_fmt=png&from=appmsg "null")

## 8、请分析计算机检材，找出检材中插入的移动硬盘序列号。（答案格式：英文全大写）

**X778002T0SNDT5S**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoOibyKKAOHL9alUg4eoqDeh0CuPIR8fiaP0AicNOnIOgJCp5mwqygd57LGyUM1YI9ABU4C05ic7trib6mYcFUH7MugV7HfCVL74UB9U/640?wx_fmt=png&from=appmsg "null")

## 9、请分析计算机检材，在系统通知中Windows Defender弹出了几次通知？（答案格式：仅数字）

**3**

系统通知里面仅有三条

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoN5aGv0ZPt9xgpkiaUejibQPiafns5Jm7Z1MfWcfzyxuJfp1L0M7mHD04vmO326GNICKZcucWpGwycYv1oj8fQATUz3nfysB0rAn4/640?wx_fmt=png&from=appmsg "null")

## 10、请分析计算机检材，找出mac地址为00-0C-29-30-DE-E2的网卡连接IP地址是？（答案格式：192.168.1.1）

**192.168.22.128**

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoNuU0dIKGCGFwN3d7ZI3oMbFvzzrz2z8GbKvOHOdoG1icH8yUvJHC5GwtTFC5x6P2AwlheTKOm8jOAcLZzDP0hWdqVjOJ0mNH34/640?wx_fmt=png&from=appmsg "null")

## 11、请分析计算机检材，“重要.docx”中记录了标识符为“C2F01FB6...”的加密卷的恢复密钥，请写出该恢复密钥的后6位数字是什么？（答案格式：仅数字）

**554368**

打开文件，发现并没有C2F01FB6标识符，我们可以将文件后缀改成zip看一下

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoOa4CVwvmUKIuZfibPXpkAIX6GWyDYVovPrK6gFhGXGnDC4Fvk0MVibqWxfouQCZhS18kXWjudqXufvzpUABxVyC8vNrAVMKlb5I/640?wx_fmt=png&from=appmsg "null")

可以看到有两张图片，第二张图片就是我们需要的![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoOs3SZ9VcricVx9DwFvtYIgYVIfBz5oniaVANWoNW04kC2dCGeJViaics5kPJAddHGFxYmtBVuOaADoz6fjdp8AgktM8qRHwar1n7k/640?wx_fmt=png&from=appmsg "null")

## 12、请分析计算机检材，请找到用户曾经用微信发送过的jpg图片，写出图片中记录的ICQ号码。（答案格式：123456789）

**402974020**

在微信缓存目录`C:\Users\admin\Documents\WeChatFiles\wxid_909739298493\FileStorage\Image\2021-02`中找到图片![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoMR0J75g0u7KCibKCXCvGA1l1eXFnqQGfOHp59aVLia6OZnK1Y5hnXR2ibghUyr4nQzdKiaKLDtwYC0MMNG72Ehs9mJIOW9JTiaBUZI/640?wx_fmt=png&from=appmsg "null")

只不过这个图片被加密了,这里使用WeChat-image-decryption工具进行解密

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoOJs6cd4yPial4GxHibgwiabh5JtRaNhYbOLyBuch9G6HOORgibsvJu3x3eUakrSpqMKmS2aEN2SvA2mFrJZxUTwicDrvrkN3AaF77M/640?wx_fmt=png&from=appmsg "null")

## 13、请分析计算机检材，“rar备份“文件夹下有两个损坏的压缩文件，压缩包中图片记录的恢复密钥前6位数值为；“rar备份”文件夹中记录的恢复密钥前6位数值为？（答案格式：123456）

**031276**

将这两个文件放到010里面，发现这两个文件中0的位置是互补的

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoMGhzLCzkQibuvFwcQBR1ZHLl92alia5kNYZO8M0LX72rY6q5zianNbic74HF7skiaUNa9I1J9Qxs4XicRWibhobCkib7SoicgpINV86t4w/640?wx_fmt=png&from=appmsg "null")

选择比较文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoOdjhVLPF31tm4yyvpJQuJF0Rks5jhqQ6uCYqzmD9mEPYL710QayjSibFiayVUUVibC1IhR3yqVnicx2jKhnLy0zZpuicPcHxNftDzI/640?wx_fmt=png&from=appmsg "null")

然后拼凑一个新的文件，解压即可

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoPGjn3YUusD7qgu2ib5sndxsATcRIsBtge8DUUeiciaLgpeYuShmzoT2lnxZ7mJQlspVa67V5FggczLjyO9GAfBhau7YrJibmGGcrU/640?wx_fmt=png&from=appmsg "null")

## 14、请分析计算机检材，请找到加密容器文件，提取容器中的文件“key.pem”，计算其SHA1校验值，写出前6位。（答案格式：英文全大写）

**36D338**

在`D:\VeraCrypt\volumes`目录下找到加密容器文件![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoNibPq0iaDh3deyjjO32yILmkPR2G0Q6hRRiagxkCkTglpFGqQKSn01RTQ2614BsNT99pWyTFliahwuztFvH3k1hxOnXUWwrXmxF34/640?wx_fmt=png&from=appmsg "null")

在D盘中还看到了一个名为`memdump`的压缩包，里面是一个镜像文件

![](https://mmbiz.qpic.cn/mmbiz_png/KjibQZESCJoOm6uy0cAibDnVP8M6LVOicic4kVgVH2VqQQu83tU6asVq9DmibwgBUGouaibS7LSqo2eWicjdfc2ua9v0wvRpL9uSn5icOoMCI2ULtsQ/640?wx_fmt=png&from=appmsg "null")

感觉密码在镜像文件里，用lovelymen打开镜像看一下，搜索aaa.hc，找到密码`<font style="color:rgb(30, 41, 59);">WOWEIZUGUOXIANSHIYOU</font>`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KjibQZESCJoMg3LMTRr6JpXIib0H0FHppick0UXUFqH0RqQN19ZqibbicibGpuJw2yxNmSc8IOzGs78iatGdDicp24sTAhmrLhnM6dibuzEicpMrWzFps/640?wx_fmt=png&from=appmsg "null")

挂载之后看到key.pem

![](https://mmbiz.qpic.cn/sz_mmbiz_png/K...