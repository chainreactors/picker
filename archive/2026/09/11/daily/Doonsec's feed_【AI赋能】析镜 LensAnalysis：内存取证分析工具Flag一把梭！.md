---
title: 【AI赋能】析镜 LensAnalysis：内存取证分析工具Flag一把梭！
url: https://mp.weixin.qq.com/s/ZfNPaHkdS6S93tRzhYwwIg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:46:30.110023
---

# 【AI赋能】析镜 LensAnalysis：内存取证分析工具Flag一把梭！

# 【AI赋能】析镜 LensAnalysis：内存取证分析工具Flag一把梭！

原创

hilyary
hilyary

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

01

0x1 析镜 LensAnalysis：内存取证分析工具Flag一把梭！

# 析镜 LensAnalysis

今天给大家介绍一款专业的内存取证分析工具——**析镜 LensAnalysis**。

基于 Volatility 3 的图形化内存取证工具，面向安全研究、CTF 竞赛、教学和应急响应场景。析镜支持 Windows、Linux、macOS 内存镜像分析，并提供传统插件操作与「小析」AI 辅助分析两套工作流。

GitHub工具项目地址链接：https://github.com/hilyary/LensAnalysis

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWchT6t2yj7AH6ogxQUxTT0vWu2evUgWIcdj5Nq8YEjSTSKSMo6G2ZiceTGEVbOnu3pqLsJQSpKevmz9GotyEtxxqeV09BbgjYY/640?wx_fmt=png&from=appmsg)

下载链接如下：

https://github.com/hilyary/LensAnalysis/releases/tag/1.0.8

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QViaAHia3arlR880XTt58ue9wEg8xe7Hb4HyRVWyZ6OFibRCpsnGh1DTw41ic4FEu5J0neHs2ibqADr5W964o9KPgPlFcAXVZk9jXQE/640?wx_fmt=png&from=appmsg)

* Windows：`LensAnalysis-Windows-1.0.7.exe`
* macOS：`LensAnalysis-macOS-1.0.7.dmg`

工具打开界面如下：

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QV8JXibpTh0GZVBYD9pKKL5UTfsIJV57X4Oh07gmNAabH1vENmvSbkLSZfux8gVl8pdsWhRcVBwL7ljynanzUk05wlz97EZhJTs/640?wx_fmt=png&from=appmsg)

### 镜像主界面

![析镜主界面](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWefSickicpT4hLJS3khBfKsZsqDufUtiakqk5KYYzOibTSEnfL8LicEWCxQPcKicE95LeYQOuCc12erOeZFGZfyFmGScXYS0XrrmYiaU/640?wx_fmt=png&from=appmsg)

### 加载镜像

![加载内存镜像](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QW4k74Qe0rJTEa6vrTVNXSHTpsjlicTJKicCaUiaYP2XFG3EIO6Em8tt1VzuWJLKHlOibcmsEwCt2nxHnic1W8aETMxNxLZT0ynOt0A/640?wx_fmt=png&from=appmsg)

### 符号表管理

![符号表管理](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVcMYd8rR60IqAIw3jAiaDdq2Jrpf1nX0bvpnytTt2eRZiaX0fsLYClDkLicYjKV76KSSBnzu5v3TibxVUtNb92EibXJgdn7sjV0LTU/640?wx_fmt=png&from=appmsg)

### 插件执行结果

![插件执行结果](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QV6812QSTfbNqUDDYgf1taSjibNLds7qWmR0dsglNibWKg9byeX4jLDE1mibNN3OGhULvrJoTHhBqH22PEWdkwN0RqibgeqaMTxYDk/640?wx_fmt=png&from=appmsg)

### Flag 搜索

![Flag 搜索](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QX4TIZfFJQyAjPFy2lbqmj6JkYZfXvVLItorXZw1GjibRlX53jEcKgBUuEHealyWzqV9EpmZsk8NEOFzEz8CLRHMYzfotibo5Fjg/640?wx_fmt=png&from=appmsg)

### AI自动化- CTF

配置大模型的api key即可，官网的和中转站的都可以

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QXXaqdtWpX28g1QwhZCNBiax2Zy6dMgZCnm0udZFXURI4V537o1Idtpqc3By6QJMJa4mSlPNctowem1qVzrBdC8tajicjoaNibMWM/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/mcko8AHj6QXjb4OwrC4Pc3Du5nkiaicx5Vl1xAhicGMtrWsEFVb3hia21Ga8RVfLicYy5IxKn4XAOMkFgsyQH8bcPQEhGxaOdNmxia64S25SG9XCw/640?wx_fmt=webp&from=appmsg)

## 核心能力

### 图形化取证

* 镜像加载、系统识别、符号表状态检查和插件分类导航
* 插件结果表格、分页搜索、高级多条件筛选和数据导出
* 文件扫描分层可视化，按目录逐级浏览文件和子目录
* 插件结果按镜像自动缓存，相同镜像可直接复用
* Markdown、HTML、Word 取证报告
* HTTP、HTTPS、SOCKS5 代理配置

### 小析 AI 助手

* 使用自然语言查询镜像、插件缓存和取证结果
* 支持常用大模型供应商、第三方 API 服务及 OpenAI-compatible 接口
* 支持保存多份模型配置、连接测试、模型列表获取和当前配置切换
* 可加载镜像、运行插件、安装符号表、Dump 进程、导出或提取文件、解密数据，以及打开文件和定位目录
* 支持分析计划、线索索引、案件时间线和 AI 取证报告
* 支持手动确认与用户主动授权后的自动确认，并可查看进度、取消当前插件
* AI 对话按镜像保存；重新加载相同镜像后，可继续查看和使用历史记录
* 支持搜索、进入和删除其他镜像的历史对话

### Windows 内存镜像

* 进程：`pslist`、`pstree`、`psscan`、`dlllist`、`handles`、`cmdline`
* 网络：`netscan`、`netstat`
* 注册表：`hivelist`、`printkey`、`certificates`、`userassist`
* 文件：`filescan`、文件提取、事件日志提取
* 恶意代码：`malfind`、`ldrmodules`、`hollowprocesses` 等
* 凭据：`hashdump`、`lsadump`、`cachedump`
* 服务与系统：`svcscan`、`getsids`、`envars` 等

### Linux 内存镜像

* 进程：`pslist`、`pstree`、`psscan`、`psaux`、`envars`
* 网络：`sockstat`、`ip_addr`、`ip_link`
* 文件：`lsof`、`elfs`、`mountinfo`、`pagecache`
* 内核与安全检查：`lsmod`、`check_modules`、`check_syscall`、`check_idt`
* Bash 历史、内存映射和恶意代码检测
* Linux 符号表下载或自动制作

### macOS 内存镜像

* 进程：`pslist`、`pstree`、`psaux`、`envars`
* 网络：`netstat`、`ifconfig`、`socket_filters`
* 文件：`lsof`、`list_files`、`mount`
* 系统与内核：`lsmod`、`dmesg`、`kevents`、`timers`、`vfsevents`
* 系统调用、Sysctl、陷阱表和恶意代码检查

### CTF 与线索搜索

* 常见 Flag 格式搜索
* 自定义正则表达式搜索
* 可打印字符串提取
* 搜索结果缓存和历史记录

02

0x2 培训课程介绍

26

**SRC漏洞挖掘培训课程**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4)

**1.课程价格目前是575（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**

**2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨**

**3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️**

**4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！**

**5.上课结束后，会把视频录播+课件笔记一起打包发直播群！**

**6.哔哩哔哩SRC课程公开课，链接🔗直达：**

**https://space.bilibili.com/642258933**

SRC课程详情🔎：[学了一堆理论，还是挖不到漏洞？你缺的是实战！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247509869&idx=1&sn=4bd678e9f9c864300cc2426432a8c967&scene=21#wechat_redirect)

内部小圈子知识星球详情🔎：[50 元封顶！渗透攻防 + SRC 漏洞星球限时开放！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247509408&idx=1&sn=2e12452dfc2d34631af5109af28a6758&scene=21#wechat_redirect)

欢迎关注公众号：神农Sec，报名咨询添加VX：routing\_love

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QVcCkxIUpaBmNic17zibGfXMWrr9z89gE0DFtbOu3QYzD5d62zsp6qwc38Pssk60mLq8VKthcMOmctVlHU716S5G4KYmrKVrEj5c/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

开课快五个月时间，课程目前已经累计加入了980+个学员了，课程培训招生任火热持续中，师傅们对于我们课程感兴趣的，想要学习技术，找工作的可以咨询我报名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVmdLBDlbl5p4Teyw5qqFOIFTIUxIxRay83I5qDXG690XI61gRj8MXTvTaibC4q2cCb1CbM4XS2FK6X4KYhPTX2ibgvA363YYwcE/640?wx_fmt=png&from=appmsg)

课程培训记录📝，每次上车在1-3小时之间，上课包括课程内部群大家交流氛围很好！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QV7iczVHowN13BzCTraG8jDUoe5hluiaZ90RUy7FjW398DictcrZhHrYpMgw4polRqvlGua6iakYdARPI3Jkiahhjvrvkviblm19U4F0/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

课程上课笔记课件📒都会打包给师傅们，笔记都非常详细，很多几k价格的培训机构哪怕是课件笔记都没有的，我这里都是下课第一时间把录播+笔记打包发给大家！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWbRV4mBn8GZHrvHocPMYYcBuAM3gyIKOM0SicBWQhywMehkXInvEerRLySOPPMzEmM2GLSlOMFREx6QItqtCgCibGs2MeY6yvu0/640?wx_fmt=png&from=appmsg)

平常也都会给学员进行一些项目发布，包括后面的工作、护网内推等，经常上麦交流，大家互相学习，简历优化等。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXvjjkgJibDEUhdDjErjibiangGsN0rqb0Av59xfyxBbDrTMNdfIAhNXlx0HQKvxIVBIEGAAbYrEENzd77j65asejlD4a50Sb4U7o/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

SRC漏洞挖掘课程培训已经两个星期了，期间也是创建了“回本小群”，希望学员回本越来越多，创建这个群主要是鼓励学员学习进步，以及不定时发小项目！

最后也是希望大家都可以赚钱，找到好工作🎉

![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUjicD1ml52JIKiaC0KzmffYUhukEfTvBDicflk3SfpDFLiaulGW6VyI7TqvKdxJyjZlttZswjdByut5a2BicIIJ4dbibBXjiam4ibVJOo/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

培训时间不长，感谢🙏师傅们的喜报，很开心看到师傅们给我分享自己的成果，希望师傅们越来越强！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUMAtEWv3xXZPDsGBRhESmwGRciaasCGibU8TtbP2U0YVZPBdf5tlLqpWAtQKBh5oFwgETyvicKBeW1JSsekAyJ5cbRlSdjooQkSM/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUrS4N68nZ0EyE76Wkib7ZDrpnZWw2Q1RJQvFEdIOu5XvFGCwpz9lziabKyo9C9d5ZiamibuSXlibhXLHb7b8QJhqEIs3hXvqktkkyA/640?wx_fmt=png&from=appmsg)

平常也会分享项目，下面是一些学员项目成果，群里报课的学员都是不抽成的，主要是帮助学员进行回本，让大家都可以进步！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWS8lR4pmzZrczwr6YjtG48EqF9q4FlAUH78M7DXkiboqF8Q1HkeWJLzpFPOQBToO3auj8r4rU9x3fuafXUDVMEcFj5EI6U3P9w/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23)

上课结束后，会把视频录播+课件笔记一起打包发直播群

**「神农安全」**知识星球目前已经累计2500+网络安全爱好者的加入！

后面也是小圈子做大起来了，师傅们也都喜欢看我文章，想着给大家教下src漏洞挖掘思路，所以自己花了很长时间做了✨课件和课表，都是纯自己手搓的，大家也可以看下课表的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthM2sjuWQFbmvWv79V058KwI0DswFF9LysewGtULj81Vp5bX9nTEK78A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVhliaOc71FnQLZjEUB2QiavqaRdiaaAN25Gb1HNADIy0cYvIIHC46za7Ab6sibRKvKG...