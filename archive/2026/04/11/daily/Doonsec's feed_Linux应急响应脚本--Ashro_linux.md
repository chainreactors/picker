---
title: Linux应急响应脚本--Ashro_linux
url: https://mp.weixin.qq.com/s/lSkGD5JxqcUhQV1MIsQQ0Q
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:47:01.238953
---

# Linux应急响应脚本--Ashro_linux

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qkajCoyKpkCTmOfianGmfxFeBMJwzbBfibWTQruapbGToEYIl4khAIwiaB7UDiboAxhDIepnJZqsjl2ZicGiboT44IFDfcJKhNQUhdOSdhQgFOcQ4/0?wx_fmt=jpeg)

# Linux应急响应脚本--Ashro\_linux

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

本文只做学术研究使用，不可对真实未授权网站使用，如若非法他用，与平台和本文作者无关，需自行负责！

前言

已涉及的工具：

* [Linux应急响应综合工具--LinIR](https://mp.weixin.qq.com/s?__biz=Mzg5NjUxOTM3Mg==&mid=2247492108&idx=1&sn=ebf099e2a7740ae9d2997742097edec4&scene=21#wechat_redirect)
* [Linux应急响应综合工具--Linux\_safescan](https://mp.weixin.qq.com/s?__biz=Mzg5NjUxOTM3Mg==&mid=2247492117&idx=1&sn=dd411b335436be56926e864d7c514a9b&scene=21#wechat_redirect)
* [Linux应急响应综合工具--LovelyERes](https://mp.weixin.qq.com/s?__biz=Mzg5NjUxOTM3Mg==&mid=2247492230&idx=1&sn=dd1bbb5547f73ade1c5870a6fe2d17be&scene=21#wechat_redirect)
* Golin：[Windows应急响应综合工具](https://mp.weixin.qq.com/s?__biz=Mzg5NjUxOTM3Mg==&mid=2247492086&idx=1&sn=d1be453e31e34e03fd2f8223dc2aae8f&scene=21#wechat_redirect)

已涉及的脚本：

* [Linux应急响应脚本--Whoamifuck](https://mp.weixin.qq.com/s?__biz=Mzg5NjUxOTM3Mg==&mid=2247492326&idx=1&sn=211142c61da6639a47cd64666743ae96&scene=21#wechat_redirect)
* Ashro\_linux

项目

* 项目地址：https://github.com/Ashro-one/Ashro\_linux

详细功能

1.必须root权限运行
2.收集IP地址信息
3.查看正在登录的用户
4.查看/etc/passwd
5.检查是否存在超级用户
6.空口令账户检测
7.新增用户检查
8.新增用户组检查
9.检测sudoers文件中的用户权限
10.使用 visudo 命令查找具有 NOPASSWD 权限的用户
11.检查各账户下是否存在ssh登录公钥
12.账户密码文件权限检测
13.暴力破解攻击检测
14.查询正在监听的端口
15.检查建立的网络连接
16. 检查是否存在系统进程
17.检测存在那些守护进程
18.CPU和内存使用率最高的进程排查（超过20%）
19.检查是否存在隐藏进程
20.检查反弹壳类进程
21.将进程对应的可执行文件保存到指定目录--webshell--沙箱检测
22.系统命令hash值打包---威胁情报MD5对比
23.检查正在运行的服务
24.检查系统文件的权限变更（一周内）
25.收集历史命令
26.用户自定义启动项排查
27.系统自启动项排查
28.启动危险项排查
29.系统定时任务分析
30.用户定时任务分析
31.检查最近24小时内有改变的文件（误报会很多）
32.cpu情况分析（占用前5）
33.日志分析
34.日志审核是否开启
35.打包日志（/var/log/\*）全打包
36.安全日志分析（登录成功。登录失败，新增用户组）
37.message日志分析（传输文件情况）
38.cron日志分析（定时下载、定时执行）
39.btmp日志分析（错误登录日志）
40.lastlog日志分析（最后一次登录日志）
41.wtmp日志分析（历史登录本机用户）
42.Alias 后门检测
43.SSH 后门检测
44.SSH Wrapper 后门检测
45.检查 SSH 授权密钥文件是否包含可疑命令
46.检查特定目录中是否存在可疑文件
47.检查系统日志中是否包含可疑内容
48.防火墙配置检测

使用

* 加执行权限，然后直接运行Ashro\_linux.sh文件即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAWtILWlicqoGMHcAugWIjibVLkrCTTMKNXnBHTdhEpO6icia5uPzkRvBMrsWc2EoG3NA8JjR99FDOp8GDEaGwQukkLyEa3ibk8ygdc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkChXUWCAPWicq6j3XBRJRKicHtCVA1lamkQT8xad0eV8ZnQnGXosKn9iaX0rHvicY1dsD5q84YLKl0jMD9QoKibwstytbmBuUgcboxs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkC3LFXQIRwYYYtrvCicGhpDicleib7fNg9bvtEfFITLP8GlBrED7crzG4Uz2rSERf5ibOcN0lHtlfszsZqrDtbtnKA4r01Ktc26KwU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBiaJbWBQA7SFj2f9SAkxGic8Hg9X1WOaMl8cxedY45AWmFS7lra0sAINAicZPicNkMcRia8JiaZSiaChsauyR2iaZKXGJ0QibkPiaZ1eibNU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAibZf4hx68GsKZvZye9CqvAunDyJ93dibohzEN6LTz75sTImrYevZccicz5cGMCCz7a1kAg4t87OK7GnibPPtYPX3X19b5crVowq0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBAU3R314xnhwRR0gicXsA0EynaAe6r6k4J7XctrUIt4qTTShVQE2Rkmia1v64daZ5RXiaibrHibmPJ1Iia4IDSGnb3w1ia7QuWGhEbks/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDo9fic87RynQ5tjPHdAkF8qfibGlgIhUHD8jLJMPqXUH7CNMpMytXc1E2alY9ibnREGoQoRSV86fUeia5kbIf8Dnpl7CJOSM8NNkg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDDVD8hb6uZicfmYZIgu6vq6iaDBPdt2HBS6e2FrSu45glqwkpicmIYAKbE3e1QTAjibUzaWFJgXxicCBDcCuHq1ZtmnVr8ibA9vuRLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCLqibekmy3gY8GxEzHM0q3GV2CaDrsj9oEf5kQwDE7GBx9Atic5WzUGWGszDSXLlylFlIDVYbGpI9Ol5DmeF8CKFhkxaAEDMyZI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDTHyTaDpA3Q2Wyb5jrkd1qzLw6GosEGKb9QefpElFJyRktbv8RRFBgw92jvTJaUAvasMTANM1ibibjqqScia3PbicJ37MWpJcGhFo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBJf8N4icCVLpj5BDSuZcP47PiaHZKjuG8aFBOiaglSJfZDegUUV43fIrfiaUd0UhSMhmVMbbicIia5s0cw4r0Kwx3rh8ibkibSod4Zw3w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkD4zicxmjrGXRZhjz9qTBSWpTxLiaS3uPT8s6yu6wicibZqu0kuG1Y5YZcajH1LSzKjW0sCzSJ4picoJtvPr157R1LqGbO4RIJv8twI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAJo7e3ZJ7Vn6c3fSvpVoLZrw6SLiagy8lXYmkwl2O5RhnT8e3AqgRtUeGcicGn0YcffJdLicibyibeDnIzo8hoe8agd2ia6WYovRM1o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAw71MbySY4ECnVicxfjmcY7LpoQ5Nlx06okia9lRqexXD6RuiaZ4UGXtF0kYKOSY5fJB9cr6kVRl1Uuhk74wYT4uTmH8lySuChWs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCn186iaDbzpDG7Bzx4wz9AkCSHpcMeUpZ4lnrFHibBHj6ZQvhKib4XCZKQyHYkzZc57R4od0uF3eeBLG0ueCtIMibuGV89tq25Iibs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkAoMXTbVEpsf66jReBO8NCeEBCb350gVViak47YH7I1zle90w0ZWVeZg8zd3II0nL3E7yibfsaDAPW4MKY4qjsJHQfWc9eqfMxKE/640?wx_fmt=png&from=appmsg)

* 命令结果：/tmp/Ashro\_时间

+ check\_file文件夹：检查命令篡改

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCBPSxoqMaeNXiaG55Ip2VUL3yTN5eNrWY0hZwQny7yWMxwJcXma1JnPsV43CtjvxOXsmkXMJJuqso6tta1hEQ75j4EhPFuCjlk/640?wx_fmt=png&from=appmsg)

+ weibu\_md5.py：通过脚本获取系统上的命令配置文件的MD5值到check\_file/\*.csv文件中，进行微步的威胁情报查询，需要配置脚本中的自己api。脚本执行后会在当前目录生成结果文件。是否命令篡改结果一目了然（key收费）
+ danger\_file.txt：脚本执行后的高危结果，需要经验分析，不要一股脑就认为风险项

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCNFA4oEibUMCSXCHw8N2hcQ4hj9lDskvniasKOiaAjMdZ3s0ibaXld20HVopPHAtqPqPXNJY0leoQhX867yiciaRzhedQMCKq2W6cIo/640?wx_fmt=png&from=appmsg)

+ log文件夹：

- system\_log.zip：/var/log/\*文件夹内容打包的压缩包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAy0TdbtQlRFaBgnaia85ZiaNkBjQoNSlbG9kQoBG4R8WoK8YfJ83PsafwMibkCia1bictRicqyxKdCLqT98gu3gg2Tnyecxia0vwIZOw/640?wx_fmt=png&from=appmsg)

- Ashro\_checkresult.txt：脚本执行过程日志，这个比较友好可以从这里分析

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkA4b9JDe5xZSHzDnBq4C90gcUNspcxqg7ZSNrQD81fYUy9yVvBicOxUf2h3LWNIiatpzeppLFFXaCGZYmJFXdkmuL3N9k4wXYlT8/640?wx_fmt=png&from=appmsg)

+ webshell文件夹：检查可执行文件后门 执行脚本后会将当前系统中正在进行的进程其涉及到的可执行文件cp下来。dump下来沙箱检测即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCzHA7TDZEe9SMGGicwAQTeqQBXaClFyb2JsAdgnhmr4rljhlWeAUYAou1cKtsDty2M7SObZQicgE2mic6icCEYGgFB97yc2lbaH6g/640?wx_fmt=png&from=appmsg)

进阶

* 漏扫工具被截留到服务器上时候，还定位不到攻击者遗留的工具时

+ 例如ips上出现横向攻击10.16.5.134 时，可以执行如下命令
+ 他会查找全系统文件内容中的可能存在漏洞结果的文件位置
+ find / -type f -exec grep -l “10.16.5.134” {} \;

* 常用手敲命令快速盘点文件：

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBen1dw7S2B7ibF7O03hRAB5WUh7SmXZgLChQaKRQAaB0ojLIiaT28vjhBAPFYotXibGobpGUobGQ0XUia6ORuGWtoDoHUk56o4TUY/640?wx_fmt=png&from=appmsg)

+ 小技巧：Linux部分可结合Whoamifuck项目脚本的自定义命令配置检测参数，不用手敲直接一步出来（可借助AI把文件的内容改为Whoamifuck项目脚本的格式）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RycyD0uC9K3FoibQ01tEZGuibOZ3V0n635gHObOkMwIDIPiapmdmhho8uib89ulc9aCVfqtP7A8GZmHEQ/0?wx_fmt=png)

一个努力的学渣

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BqBKZfLY4RycyD0uC9K3FoibQ01tEZGuibOZ3V0n635gHObOkMwIDIPiapmdmhho8uib89ulc9aCVfqtP7A8GZmHEQ/0?wx_fmt=png)

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