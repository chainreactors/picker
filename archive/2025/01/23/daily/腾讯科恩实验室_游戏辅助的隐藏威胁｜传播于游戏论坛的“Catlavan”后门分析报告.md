---
title: 游戏辅助的隐藏威胁｜传播于游戏论坛的“Catlavan”后门分析报告
url: https://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247512659&idx=1&sn=ca99588eed415d2fdbdd87c4e666b662&chksm=fbfe8e56cc89074039ffcc9bb0544c3f4285b0fb28a480034307d88019f5b1fa8e610a5e494e&scene=58&subscene=0#rd
source: 腾讯科恩实验室
date: 2025-01-23
fetch_date: 2025-10-06T20:11:04.249065
---

# 游戏辅助的隐藏威胁｜传播于游戏论坛的“Catlavan”后门分析报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufIZWoicNtSX0kcqXmRkHjQp7S0r2xTLE2JKRJBRyOQPHLYbLFNeGLKQg/0?wx_fmt=jpeg)

# 游戏辅助的隐藏威胁｜传播于游戏论坛的“Catlavan”后门分析报告

腾讯威胁情报中心

腾讯科恩实验室

随着网络游戏用户规模的扩大，针对游戏的外挂和辅助灰产业日益壮大。与此同时也有不少木马团伙利用外挂辅助传播木马，此前腾讯云安全威胁情报中心已发现多起通过外挂传播恶意木马的案例。

2024年BinaryAI的恶意文件检测引擎创新性地探索了一套基于语义化的查杀引擎技术：

[BinaryAI更新布告｜摆脱特征码和特征工程束缚，语义化恶意文件检测功能上线](https://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247511896&idx=1&sn=17f4962ddd9b42727e3a499ea79b39f6&scene=21#wechat_redirect)，通过大模型相关技术实现端到端文件检测，利用这项能力我们发现一起针对俄语环境戏辅助用户的攻击，我们根据同源分析关联到本次样本在传播时位于Catlavan压缩包中，因此将相关攻击样本命名为“Catlavan”后门。截止分析时在VirusTotal上未发现其他安全软件检出该样本。

1.详细分析

**1.1.**一阶段Loader：LiveRuch.exe

### 1.1.1.BinaryAI分析结果

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufBlFj3esnKxYLiaSgTDSBxqgBgbEniaiapNtMegAskicrCIOECyZ8nZ6Qrw/640?wx_fmt=png&from=appmsg)

分析链接：*https://www.binaryai.cn/analysis/9e6bb9f5be0a22e89d16c2a830c0fc97d6a1c839fb1467fbfeddb1d051536e69*

### 1.1.2.行为拆解

### 样本首先根据SID判断自身是否以管理员身份启动：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufkjwEur49ZDvkNh1VL3d8DLoXYUHkKMHnT51b3bQnibL1RhepkuwGSug/640?wx_fmt=png&from=appmsg)

如果不是则调用ShellExecuteExA重新请求管理员权限运行并退出：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufapnQIGmUedNvn82FaMOP59Q3XaG78POSe3aucqugNBo95kaO7vLsSQ/640?wx_fmt=png&from=appmsg)

如果是管理员权限则从93.185.157[.]131/file/runtime\_broker.exe 下载第二阶段的server到本地Temp目录，并创建runtime\_broker.exe进程：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufgib2GbQKcCSSxsmdoNMpiboQRMIzFjV84ZWnMMQXrjQ2oC7Llfibgv1Ag/640?wx_fmt=png&from=appmsg)

截止分析时，VT暂无杀毒引擎查杀：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufl1zKcZsCAwm8K8LnVvEG5bTRRAl6A0tUy9zvzS9MfbKqfYna4w8WyA/640?wx_fmt=png&from=appmsg)

**1.2.二**阶段Server：runtime\_broker.exe

### 1.2.1.BinaryAI分析结果

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufzTQdAhZIGJUvbdibl09OhK2zvHmbSqjicjdFQ3ZVt4Z9dfj7unWfnSBQ/640?wx_fmt=png&from=appmsg)

该Server启动后会窃取用户信息，并通过Telegram向攻击者发送日志。分析链接：*https://www.binaryai.cn/analysis/c5f915d44aecc5b56f55e9d2635b9dbb1c4d6f018c5d11d6912c800b29420d13*

### 1.2.2.行为拆解

样本启动后首先调用Telegram接口，向目标tg账号发送日志：

chat\_id：7174999938

使用俄语："Начало выполнения программы" (”程序开始执行“)：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufS0Fn6BS5icSuZklcicwibzg9mUIVpJUWB8F2bAEuRwpu2Ee7UqLRiaUz2Q/640?wx_fmt=png&from=appmsg)

然后会创建一个线程，在该线程中显示伪造的错误消息框，欺骗用户点击：

标题："Ошибка обновления"（“更新错误”）

内容： "Не удалось установить обновление. Код ошибки: 0x80070002"（“无法安装更新。错误代码：0x80070002”）

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufZkWpib0vLSJMS29tvibYuJNrQzz6ynr4D2CDlEhriaXHUXD4rGrkzAb3w/640?wx_fmt=png&from=appmsg)

当用户点击确定按钮后，向远程Telegram账号发送消息：

“Пользователь нажал ОК на фейковое сообщение об ошибке” （“用户在虚假错误消息上单击“确定”）

然后开始执行窃密操作，先向目标Telegram账号发送日志：

“Начало процесса архивации“ （”开始归档过程“）

首先获取环境变量AppData，并在该路径下递归查找Desktop目录，如果找到，向远程tg发送日志 ：

“Найдена папка：{path}”（“找到的文件夹：{path}”）

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufeef8bwqsqwM1gEQeHEglJoibIlIA5NKYEvfEibCv6L41yOQ3CqkQjGvA/640?wx_fmt=png&from=appmsg)

然后以当前时间戳命名在temp目录下创建一个zip文件，将Desktop目录下的所有文件进行压缩打包，处理过程中记录进度并发送日志到Telegram账号（每处理 1000 个文件记录一次日志）zip文件名格式：temp\_年月日\_时分秒.zip。

Telegram日志：

“Обработано файлов: xx/yy“ （”已处理文件：已处理/总文件“）

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufH8NBgFEUj2VeasopegCzNassyibjzaoibAaykkuIsZ3b373m499yia2nw/640?wx_fmt=png&from=appmsg)

如果在打包过程中写入压缩包失败，则会通过taskkill命令结束掉telegram.exe(占用文件的进程)

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufbgHvsMFNbeiadKLnN6pqgm6jh3Udb6cebTsyibToeQwlnuamPgcNialXg/640?wx_fmt=png&from=appmsg)

打包结束后向Telegram账号发送日志：

”Архив создан успешно” ("存档创建成功")。

最后，该server文件会连接C2，将该zip文件上传到远程sftp服务器的指定目录下：/var/www/html/files/。

SFTP用户名和密码被硬编码在后门中：SFTP\_HOST = '93.185.157.131'。

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufJWDWDB06S8rfC599p3qqUwYibiaEvWwibtf4batD1MFyicPoxdKIJaLwsw/640?wx_fmt=png&from=appmsg)

并向Telegram账号发送日志：

Архив успешно загружен на сервер!\nСсылка для скачивания: {download\_url}

归档已成功上传，下载连接：（sftp路径）

最终向Telegram账号发送日志，并结束进程：

"Задача выполнена успешно, завершение работы" （“任务成功完成，关闭”）

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufvucibVDKYFKjx8M1FEZCu6Z8ZGxfPX4XFFZdIISfkODicn6Gxr472UUA/640?wx_fmt=png&from=appmsg)

截止分析时，未发现其他安全软件查杀：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufVS2EuytMhIkGEJd1hpV8FL4gPNJIxLUTrxDZHCgt2U1UAzqjV5qZPw/640?wx_fmt=png&from=appmsg)

2.溯源分析

经溯源发现，攻击开始时间为2024年12月。攻击者构造了一个Minecraft游戏的辅助工具(实际是一个后门文件)，并在俄语游戏圈的BBS论坛等网站分享传播：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufYetlvNGIsb0fusf2bO4DIa0LOb9aU6MHnJzFMVPFdiazRRXewCPTIcA/640?wx_fmt=png&from=appmsg)

诱导用户关闭安全软件：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufMwpmTT6icEr3pSGF44mgIZbJarsh45v7arYicU4K96g6gZiblscL7ibv3g/640?wx_fmt=png&from=appmsg)

通过我们的智能分析系统我们也发现了一批同源样本。除了以上功能外，还可接受tg bot指令，完成以下功能：

|  |  |
| --- | --- |
| 指令 | 功能 |
| screen | 屏幕截图 |
| webcheck | 开启受害者直播 |
| dannie | 上传Telegram目录下的所有文件到SFTP |

其中webcheck功能在国内环境比较少见，攻击者通过执行第三方开源工具ffmpeg，启动一个屏幕录制流并将其推送到一个 RTMP 服务器，其他人可以访问该连接进行观看：

![](https://mmbiz.qpic.cn/mmbiz_png/6AoQM3RKCWVDVGpibgbHuEmn0ROvefPufydrPPibEl5WZibeEvtDCqvOCGfDJfSPxt8QFYRQAVibBx1oF5qNvQcZ6Q/640?wx_fmt=png&from=appmsg)

3.总结

腾讯云安全威胁情报团队建议大家需要提高警惕，按照如下方式以防范此类攻击：

* 谨慎使用游戏外挂，辅助，破解等灰色软件。
* 下载腾讯电脑管家（https://guanjia.qq.com/）开启主动防御模块并定时查杀。

4.IOC

C2：

93.185.157.131

telegram bot token:

7484681692:AAHvE1a6KYWG0gAZVcEFfo04OwRLugyuaZg

telegram chat\_id：

7174999938

**关联样本MD5:**

|  |
| --- |
| 1715eeafe4b6815512a9340247879fed |
| e06fddabb932da32ca73b7b45d58c550 |
| eaca483033147ba545a3b2b7a99eb74e |
| c5fe5a0b425e1fcb29f29ef08c7420b2 |
| f0893580a8e046791d4ae9550ea8dcd7 |
| 14ed2e5b463d4bfd881ea13d2f916daa |
| dc9889a22e61bb7c2dc0d828ff87c2aa |
| 011168b05b03a217e8c99d8d76d60226 |
| 2d1e734747b57d5be759a0e1b6718f92 |
| 80982d24bb0ae98fb9b1a0358ad630e6 |
| fa64f20d588cf7336263ee21545894ba |
| ca90ecb6e05efe45f80b7528c6de8c37 |
| 04fca4013e1342c431ae86fbcb6f9508 |
| ea7121969f3d56a4bfcb07be8d579c12 |
| 1ee4db2b8a18b5d0ac4a77dd78d1372d |
| a586df5cabc6ad093bfe2620c3476846 |
| b3ebf8d0319283484c96a31f5b0a28aa |
| e9fd00277d28bfa921757f9b16881777 |
| ed683a3b87065ff2fd50ce8fcb1bc8d2 |
| 166d83e8026a98d954aef2599d8bc129 |

**产品体验**

阅读原文或前往官网  *https://tix.qq.com/*

了解更多腾讯云安全威胁情报中心产品矩阵

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoericeibR9Via8lKsXBGe86PNOO29563lc14hN34D4ibbIeAjn8H388NjENBlYQibdA9GCW708MbsgxwqnWA/0?wx_fmt=png)

腾讯科恩实验室

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zZKnUibvoericeibR9Via8lKsXBGe86PNOO29563lc14hN34D4ibbIeAjn8H388NjENBlYQibdA9GCW708MbsgxwqnWA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过