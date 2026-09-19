---
title: 当黑客把路边那台Flock摄像头拆回家后
url: https://mp.weixin.qq.com/s/hQWwbnbnbYNOq3KSwj_JAA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:52:19.707121
---

# 当黑客把路边那台Flock摄像头拆回家后

# 当黑客把路边那台Flock摄像头拆回家后

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

一家叫Flock Safety的公司，做的是自动车牌识别（ALPR）设备，美国不少小镇和警局都在装。

Flock Safety 靠自动车牌识别（ALPR）设备在美国快速扩张，把摄像头架在路边抓拍车辆，再把记录接入一张全国联网的搜索库，截至 2026 年已有约 4000 个警局部署超过 13 万台摄像头，Alpharetta 一个小城的画面就能被两千多家机构调取，还曝出地方警员替 ICE 查车牌、得州警员为一名自行堕胎女性跨州搜车等滥用事件，隐私争议随之引爆。

面对这种扩散，美国各地的反对者从 2025 年底开始行动，有人朝摄像头开枪、用卡车撞、拿锯子锯断杆子、泼油漆，到 2026 年 8 月已有超过 160 台 Flock 摄像头被物理破坏，明尼苏达 Winona 一镇就有 8 台被偷走不补装，加州甚至有人专门开车 150 英里去拆。

而佛州 Oviedo 警局用 3D 打印假摄像头钓鱼抓破坏者、把一名拿修枝剪砍假摄像头的年轻人控了三项重罪，最后因为假摄像头不值 1000 美元又降回轻罪，成了一段执法翻车的插曲。

与此同时，政策层面的反弹更成规模，2026 年以来已有约 100 个城市解约或拒绝续约，明尼苏达 Twin Cities、麻省、科州出现整片区连锁退出，解约理由高度一致，即数据一旦进入 Flock 全国网，连联邦机构都能跨地区搜而本地根本管不住，佐治亚还有居民提起集体诉讼、参议员 Josh Hawley 启动国会调查，Hood County 的治安官甚至自己称这套系统是 "无证监控" 而主动关停。

总之，这个事情黑鸟一直持续在关注，最近一个自称stegan0gram的黑客组织直接把一台摄像头从杆子上卸了下来，带回驻地做了一次近乎完整的数据拷贝，然后把这些文件交给了媒体。下面这些数字和细节，就来自被拆下来的那台设备本身。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDogyqxNiawAUSFc7H70ctiaH5fxk83Bibl3oclm6GZ7anSyxF5yLA2QmqghDgTN4sQfXdGK2Qk0C5vs38BcjzUqsSiandeYO7mHOV8/640?wx_fmt=png&from=appmsg)

Flock的摄像头架在道路上方，每有车经过就拍照，把图片和附带数据通过蜂窝网络传回公司服务器。真正读车牌、判断车色品牌型号的事，并不在摄像头本地完成，而是放在云端，识别完再把带时间戳的记录交回采购它的当地机构。

问题在于这套系统背后还牵着一张全国联网的大网，在佐治亚州Alpharetta，官方记录显示同一批摄像头拍的画面，两千多家机构都能调，除了各地警局，还包括大学、机场，甚至联邦总务署的监察长办公室。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpTIibibtbB7nSRriaObmjEAwULuendJcfk082mrMjiaRIuvWWhOkiaO8KbTrUj9eRdftvkmIibp9vdjCcBDqPcbmRGabuNw2yJYBk9M/640?wx_fmt=png&from=appmsg)

这张全国网一直是卖点，也是争议的源头。此前媒体已经曝出，地方警员会替移民与海关执法局（ICE）在全国库里查车牌，哪怕当地立过法不许跟移民部门合作；得州还有警员为了找一名自行堕胎的女性，在全国摄像头网络里搜过她的车。这些事凑到一起，让越来越多美国人开始琢磨，家门口到底要不要装这玩意儿。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDprPlGCo7JtqnPhqiaqnDdvkLUjh8scCCKB92tyOXRf26A40rXB6NHpAIhuia9OKp7V9solFBpVGNDaNianYrFo4CVBAboUO6Yd4c/640?wx_fmt=png&from=appmsg)

早在stegan0gram之前，安全研究员Jon“GainSec”Gaines就自己掏钱买了一台Falcon/Sparrow型号的车牌识别机，从2025年初开始做了一轮完整的硬件逆向。他反复声明所有测试都在自购设备上做，没碰过任何正在服役的机器。拆开外壳，里面的硬件并不神秘：核心是一块Lantronix旗下Intrinsyc做的Open-Q 624A SoM（系统级模块），上面跑的是Android Things 8.1，本质上就是Android的裁剪版，处理器是高通APQ8053，和同期一批中端手机用的是同一颗芯片，旁边配eMMC存储和LPDDR3内存。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrrgTDp5dt09BYrIa3ne0c9GdK0bSBIYic1zpn2r51BvyE3VicR1Yo4BPn4vtzyxvWbxexKX3WFDkB13jibA7FU4ibsIlr6s3hI5WM/640?wx_fmt=jpeg)

GainSec公开的两种硬件批次，上下两块主板用的是同一套SoM，区别只在是否预留了micro-usb接口

市面上能见到两个硬件批次，一批在板上留了micro-usb口，另一批这个位置是空焊盘。空焊盘那批想调试，要么找SoM原厂买一块开发板，要么自己动手焊线。Gaines把这套从原厂文档反推接口的做法戏称为“跳蚤市场供应链攻击”，其实就是直接找芯片厂商要datasheet（数据手册），照着图纸量焊点、对线路，没费多大功夫就摸清了所有测试点。

真正有意思的是它的启动流程。这块板子上有个dip switch（拨码开关），拨到ON位置再按住按键开机，就能进fastboot模式；从fastboot可以重启进recovery，再从recovery进EDL（Emergency Download，紧急下载模式）。Gaines跑了一下fastboot getvar all，输出里两行字很扎眼：unlocked:yes和secure:no，意思是bootloader已经解锁，安全启动（secure boot）压根没开。boot镜像虽然带着AVB（Android Verified Boot）的校验尾标，却根本没人去验。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDoFeIW88XykalwW48ibQTK3mrohJrxSLDic5v6F6SphRLPn7kDm14qu4SYKv061kORva7U11oWndllcCiaz6aFicmb8k5EfIJdmDZ4/640?wx_fmt=jpeg)

通过EDL模式直接dump boot分区和system分区的终端记录，整块eMMC内容可以明文读出来

走到这一步，root就水到渠成了。标准做法是用EDL模式把boot分区整个dump下来，拿magiskboot解包，在cmdline（内核启动参数）里加一句init=/bin/sh，重新打包刷回去，开机之后系统会直接把init进程替换成一个root权限的shell，连selinux都不用关。Gaines公开的截图里，adb shell进去提示符直接是#，getprop一行行打出来：Android版本8.1.0，内核3.18.71，厂商QUALCOMM，构建指纹是msm8953\_32-user/release-keys。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrReuDycaphd6LDgknZVGGXYTodqicdZ0enoIJsYnBmJebV8iaAjalE1sV8jCVSRwm2uRiaUVqEnrHChgHib7p6FKAhShHc9DyC4Nc/640?wx_fmt=png)

拿到root权限后的终端截图，getprop显示设备跑的是Android 8.1.0，内核版本3.18.71

他在这批研究里报了一堆漏洞，其中编号CVE-2025-47824那条最根本：这块SoM缺Flash/eMMC加密，对应CWE编号CWE-1326，也就是硬件里缺一个改不动的信任根。谁只要进了EDL模式，就能把整块eMMC按字节明文dump出来，system分区拿debugfs打开就能直接列目录。披露的时间线是这样的：2025年2月8日Gaines第一次联系Flock，2月10日收到回复，3月7日Flock主动为其中10个漏洞申请了CVE编号，5月5日Flock发了官方PR文章淡化影响，6月19日研究博客公开，6月27日第一批CVE编号正式公布。

Flock当时的回应很关键，也很有代表性。公司承认漏洞存在，但强调这些问题必须物理接触设备才能利用，而且就算真有人把设备拆了，“仍然拿不到录像”，因为图片传到云端之后本地只留很短时间。也就是说，厂商的安全模型压在两个前提上：设备挂在杆子上没人碰，而且本地不留东西。stegan0gram后来干的事，恰恰把这两个前提同时掀翻了。

stegan0gram一伙人拿到摄像头之后，路子跟GainSec差不多，但目标更直接。他们进到设备的Android系统里，发现存储被切成几个分区（partition），其中一部分压根没加密，包括一个叫vendor的分区和一个叫media的分区。关键是media分区里还藏着另一块加密区的密钥（encryption key），拿到这把钥匙，那些被锁住的视频照片就全开了。最敏感的那部分存储还是没打开，但剩下的内容已经足够看清这台设备平时在忙什么。

这台摄像头的处理器跟一台中端手机差不多，上面跑着大约二十个Flock自研应用，分工很细：有的盯着画面里有没有东西在动，有的负责拍照，有的给物体分类，有的把数据传出去，还有的接收远程更新。整套流程读下来是这样的：画面里一有东西动，摄像头就连拍一串照片，一辆普通车开过，平均产生约28张图，多的时候超过100张。这些照片用不同曝光拍，为的是既把车牌拍清楚，也把周围场景拍清楚；软件再从这堆照片里挑出可用的帧裁好，连着其他信息一起发回Flock服务器。本地摄像头不读车牌，也不判断车色品牌型号，这些判断都在云端做。

恢复出来的日志只覆盖了大约二十一天的活跃记录，中间还有断点，更早的日志要么被覆盖，要么损坏读不出来。就这二十一天，这台摄像头拍了约50200辆车，生成约160万张图。平均下来每天记约3300辆车，最高一天4454辆。当然这些数字跟装在哪关系很大，车多车少差得远，但单台设备二十一天就攒了一百六十万张图，这个量级本身就值得人停下来想想。

摄像头里跑的物体检测模型，明确把人列为一个类别。软件一旦在画面里认出“人”，就会记下这个人在画面里的位置，以及模型对这次判断的置信度（confidence）。为了验证模型到底能看到什么，我们把摄像头里的模型文件抠出来，拿测试图片和设备里恢复出来的录像去跑，结果模型毫不含糊地认出了人，包括一张记者的自拍。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrl8ERBr8gKOzaTpcfq54qP4ia5mPkia82J4QeSQQn8wX4hWp5aqcQh8l0ZugTNfCCgePcDicRN793ibJWnfCQurErzpaDZVKDUNxc/640?wx_fmt=jpeg)

把记者自拍喂给摄像头内置模型，person类别直接把人框了出来

研究人员又把模型跑完设备里存的27321段短视频，这些片段都是一两秒长的MP4，分辨率1024乘768，没声音，跟车辆经过时那串高分辨率连拍照片是两套独立数据。结果11段里检出了人，全都是骑摩托车的骑手。检出这么少其实不奇怪，摄像头架在道路上方俯拍车道，本来就不太拍得到行人。

测试还暴露了车牌检测器的能力。内置模型有时会把保险杠贴纸、经销商广告框和其他图案错当成车牌，像裁车牌一样把它们裁下来存好。最典型的一段视频里，一辆摩托车从镜头前过，检测器居然把骑手尾包上的一块美国国旗补丁当成车牌框了下来。下面这张分析截图里，橙色框标着licensePlate，其中一个框住的就是那块国旗贴标，旁边红色框标着person，蓝色框标着vehicle，数字是模型给出的置信度。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDppw6TPZV1LmYMtUD3z8HQ4M4lib9vJyGz05vhDzaHkxuliadV4W8JhXjLv00GvYlictqOVNiaqdQqPbR4UukMicTibcKpUMaNpHAjmI/640?wx_fmt=jpeg)

分析截图里，车牌检测器把摩托车骑手尾包上的美国国旗补丁误识别为车牌

最后回到最关键的问题，那它有没有在做人脸识别，这是最敏感的问题，目前看答案是否定的。Flock一直说自家摄像头不做人脸识别，这次翻遍摄像头软件，除了Android自带的那部分默认能力之外，没发现任何专门的人脸识别模块，而那部分自带能力看起来也没启用、没在用。也就是说，现阶段这台设备的边界是“知道画面里有人”，而不是“认出这人是谁”，但物体检测这一层已经在本地跑起来了。

摄像头端只是系统的一头，另一头是Flock给警方用的软件，现在叫OS Investigate，以前叫Nightshift。今年八月这软件的前端代码也被人翻了出来，拼出来的界面显示，它可以把摄像头拍到的记录跟警方档案、商业数据合在一起，找出经常一起出现的两辆车，或者按行动轨迹搜人。摄像头负责“看见”，这套软件负责“找人”，两头拼起来才是完整系统。

这也是为什么全国联网一直让隐私倡导者坐不住。一台摄像头拍下的车，几分钟后可能出现在几千公里外某个警局的搜索框里，而被拍的人完全不知情。Alpharetta那两千多家可访问机构里，有些跟本地治安根本八竿子打不着，这个系统把“看见”和“调取”之间的距离压成了零。

Flock发言人回应说，未经授权拆除和改动Flock摄像头是违法的。被问到设备里存着解密密钥这件事，对方说公司有公开的漏洞披露政策，欢迎安全研究员走正规渠道上报，但他们没收到过相关报告，凭现有信息还不足以评估这些说法。黑客那边倒是很坦白，说被调查是现实顾虑，自己也尽量低调，只不过“与其砸掉它们，为什么不把它们逆向工程（reverse engineering）掉，看看那些监视我们的人到底藏了什么”。

罗得岛州Pawtucket镇那位曾公开反对自家警局装Flock摄像头的前警官Noel Pichardo，他理解这些人的愤怒，但也担心砸设备反而帮了倒忙。在他看来，这种vigilante（私刑式）行动只会让警方和州里更加认定这套工具非装不可；州里越是装听不见居民的反对，类似的事只会越多。

恢复出来的日志还顺手暴露了这台设备的工程状态。它一直在跟存储较劲，日志里记了超过27000次“no space left on device”（设备存储空间不足）报错，都是在存全分辨率照片时弹出来的，伴随的还有数以万计的相关错误、崩溃和重启。但同一台设备又有一套近乎搞笑的心跳机制，大约每两分钟就有一段代码确认摄像头还活着，然后在日志里写下一句“Who's a good boy?!”，恢复出来的日志里这种话出现了12000多次。真要重启的时候，另一个服务会在日志里留个告别：“A reboot was requested! ¡Adiós, Amigos!”

把一台路边监控设备从杆子上卸下来再开机看里面，本身违法，这一点没争议。但它确实让公众第一次有机会拿设备自己的日志和代码去对一对，一家公司和采购它的警方对外描述的系统，跟设备实际跑起来的系统之间，到底差了多少。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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