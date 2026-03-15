---
title: 注册表被“记事本”劫持？镜像劫持 + Winlogon 持久化
url: https://mp.weixin.qq.com/s/NLLtW42CCACp_fDYL3gdVg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:24:35.048347
---

# 注册表被“记事本”劫持？镜像劫持 + Winlogon 持久化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/H6RmIowwbs6dMdyIpyTjB5kicMZKeGxQQ26UicTB0PgibHd7iclK0SILbojlGtpW8cKKxklpKVUia304ryYlMPUqiaDyR1fPJjibiac1KLdDniaSVHRk/0?wx_fmt=jpeg)

# 注册表被“记事本”劫持？镜像劫持 + Winlogon 持久化

原创

weiqin
weiqin

大仙安全说

![]()

在小说阅读器中沉浸阅读

点击蓝字，关注我们

关

注

![](https://mmbiz.qpic.cn/mmbiz_png/oZN2pbzJKdWUK3Ne8uSjJibGEKUc8s8FbE3ibZ4mjQicF2gDe1DTSIqmWKU5YsEtQgKubRf5IySO9NkDcr1valibkw/640?wx_fmt=png)

免责声明

大仙安全说的技术文章仅供参考，此文所提供的信息只为网络安全人员进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他! ! !

在日常的安全运维中，我们偶尔会遇到一些看似荒诞却又暗藏玄机的现象。比如，当你双击注册表编辑器准备排查系统问题时，屏幕上弹出来的不是熟悉的注册表窗口，而是一个充满乱码内容的记事本！

![](https://mmecoa.qpic.cn/mmecoa_png/41rzoAia9zheaqOiavPK2XqnRNVnwlNq77H0XW8EFHCnRjTraricDOlK3vqUoT38nCX0EciaTKKLUEma36onLiaZbTQ/640?wx_fmt=png)

**01**

**注册表变成了记事本**

一位同事反馈他的电脑出现异常：想打开注册表编辑器修改一个设置，结果双击 regedit.exe 后，系统没有打开注册表，反而启动了一个乱码的记事本程序。他以为是自己误操作，但尝试多次依然如此。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs5OSIJMzWaXgvbwttHKUSOJolaVvhUhso40XwH5Z5kRqEJtdb5CEMBNQEiaoDjwIs016CHNXiafYfq31ujKTiajhE2jfZ2wiaoicRSg/640?wx_fmt=png)

当他试图打开 msconfig（系统配置）时，同样弹出了记事本。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs52PWJQ9e6Bl9Al9BX0U5xf5NWjB9YNJtoibE496PW9AXgjgfjnnY2oTFib28dg83azgjRN2bZKk4aPC2ia3g1ia6aiaxJfWhrSUUM4/640?wx_fmt=png)

**02**

**System Informer初探**

使用了强大的系统进程管理工具，System Informer，快速浏览进程列表，发现有几个进程名称比较可疑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs5fz3JMwJlOqJgicibePLiafXx40ibvVg2j9JvQypl8Z9Ydr6Fibc0mMZEt4qiaA5HX4iasKx1jaQqqgsGr3FmzmZWPCSu5AWDZdrnxSM/640?wx_fmt=png)

**03**

**Autoruns发现异常**

在 Autoruns 窗口中，在“Logon”选项卡下发现两个异常条目。显然恶意软件通过修改注册表和添加启动项实现了自启动。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs48gc13WnCL0hKTtPxVVUBsqo0HcxbTx02iaTNIHnXgQ4QSzgzx13kg00EL5IMVTKQI3Am6QVf6qFJC2EvM9iaBPnoLBsKj4ib9y8/640?wx_fmt=png)

**04**

**Procmon深入分析**

虽然我们已经找到了一些可疑点，但还不足以完整还原恶意软件的攻击链。接下来使用 Process Monitor，这款工具可以实时监控系统的进程/线程、文件系统、注册表等所有活动。

***一：进程树分析***

通过查看进程树，我们发现tux.exe下面有四个子进程并且 EmangEloh.exe也创建了多个子进程；与System Informer分析吻合。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs6fJNhDibqCzoFTicftcomDBUIibs8Xa4b2ZWhice0zyhttVlOZHZZMScGg7pICHZvgfickFeTNicRAmNxFggGzibBCia3nEAM6ruXuq8U/640?wx_fmt=png)

***二：文件操作汇总***

在文件操作汇总中，确认了之前发现的那些目录下确实被写入了多个文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs49eiaUhIR1SicA50VXBL6y5K3sO49MHWt8o1AIeH0qoxJuictYvKnrrMTVC93w54hoaiboc4cnvZQHC8tFtMozR8U6h1I2ib8hqu9U/640?wx_fmt=png)

***三：注册表操作汇总***

在注册表操作汇总中，更是看到了大量的写入和修改。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs76HCqoiaG9YRCicNxYZEM7rWU864PKbmcnEdfLVyPo6so2LulRo1ZJXkticZWqicvdVIwZYVUK8o7pUaGcDzQrXSUBVmWtr9saWYg/640?wx_fmt=png)

**05**

**Noriben快速取证**

一个基于轻量级沙盒分析脚本。它可以将捕获的行为自动整理成清晰的报告。运行 Noriben 后，模拟操作几分钟，生成报告。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs4vwO8JSY4f4dGTJUsDupT1IzdgDceFfYeb6MXZLrLhynRt2WG0icyW88RzNAhrzpYmRTtYngia49wWcAaIQOiaIicKWpmERzWicI38/640?wx_fmt=png)

***一：进程创建***

与与procmon分析一致，只不过是文本的形式，更加方便些。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs4hXibphAv14n5ia0qpbia7MWrNez93c53L8TtpN9iaIdibw7wMXAWcsicRgsbzYsBlIm1v7Kdjk1wVdKkh8MaLeflP7b4Rlicw5XLVfo/640?wx_fmt=png)

***二：文件创建列表***

创建了一堆的文件

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs6WnW0Qt0FOLUlmVgicUibdSRQh8nPlIibYIHyb1X6yMJLx7Cr6XHxlVEiavrhYibWl3pQMdyP2LRmJsUWR3vL3z6PSgxDlmVQSxic74/640?wx_fmt=png)

***三：注册表列表发现根本问题***

（1）在 Noriben 的注册表修改列表中，我们找到了两个极为关键的条目，Winlogon Shell 和 Userinit 被修改（实现持久化）

```
[RegSetValue] smss.exe:5248 > HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell  =  explorer.exe, "C:\Users\admin\AppData\Roaming\Microsoft\Windows\Templates\O74747Z\TuxO74747Z.exe[RegSetValue] smss.exe:5248 > HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit  =  C:\Windows\system32\userinit.exe , "C:\Windows\M46840\Ja67031bLay.com
```

这两个注册表项控制了用户登录时启动的 Shell 和 Userinit 程序。恶意软件将自己的路径追加在后面，导致每次用户登录都会自动运行它的恶意程序。这是一种非常隐蔽且持久的启动方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs7NaiaaPjjvNyRq8cXTVFBgezkEhxd6vHI5diald9nGjJGuRF5ZTUWW2CqqqFL4IQfHv2T4Lb223Scicegu2tgctGRZyxmrdrrxTs/640?wx_fmt=png)

（2）导致注册表打开是记事本的元凶

```
[RegSetValue] EmangEloh.exe:5340 > HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\msconfig.exe\debugger  =  C:\Windows\notepad.exe[RegSetValue] EmangEloh.exe:5340 > HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\regedit.exe\debugger  =  C:\Windows\notepad.exe
```

恶意软件在 Image File Execution Options 项下为 msconfig.exe 和 regedit.exe 分别创建了 debugger 值，将其指向 notepad.exe。当用户尝试启动这些程序时，系统会转而启动 debugger 指定的程序（记事本），从而阻止了系统工具的正常运行。这就是为什么打开注册表却弹出记事本的原因。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs5XKyibIT4BNtNIxCQXrvbiaqhz9J72zoNK4icH96IsV1Ck9NtDpk2Dic5staTb684yIsK7hDQRYzFXwt7aaCUZYPXZ0LgmjLGrwUw/640?wx_fmt=png)

**06**

**修复系统**

现在已经找到了病因，接下来就是修复。恶意软件为了阻止修复系统而额外设置的一道障碍。它可能通过修改组策略或注册表权限，禁止了所有用户（包括管理员）对注册表的修改。

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs5qlO0ib1zJ2DevAXr68zdMVDurnGEZaPENNAf1XSv0W6KDQ5lR5uuGk3cCsXKnOvBlJ9sycUlBiaNLrrACCEuZEbLFpJchf2PeA/640?wx_fmt=png)

使用 PowerShell 绕过限制

```
Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\regedit.exe" -ForceRemove-Item -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\msconfig.exe" -Forc
```

最后，根据之前发现的可疑文件路径，逐一删除恶意文件。为防止文件被占用，可以先结束相关进程（使用 System Informer 或 taskkill）。重启系统后，再次运行 Autoruns 和 Noriben 检查，确认没有异常自启动和注册表修改，系统恢复正常

**07**

**总结**

1.映像劫持：通过修改 Image File Execution Options 下的 Debugger 值，使系统工具（如注册表编辑器、MSConfig）被重定向到记事本，从而阻止用户进行诊断和清除。

2.Winlogon 持久化：通过修改 Shell 和 Userinit 注册表项，在用户登录时自动启动恶意程序，实现长期驻留。

3.多文件分散隐藏：恶意文件被存放在随机命名的文件夹中，以混淆视听。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0FR0MLn8jepbllc2psMbAnk0SA9ibNCnd3Picpv1ibAIicNv0ibt9azaRxN5ibCMXC8xyjQeUDpXrMjgGjQ/640?wx_fmt=png)

在恶意样本动态分析过程中，务必在点击运行样本前就开启各类监控工具（如 Procmon、Noriben 等），以确保完整捕获其行为。需要说明的是，本文侧重于恶意样本动态分析技术，与应急响应的实战场景存在一定区别。本文所有操作均在隔离实验环境中进行，涉及的可执行文件均为测试样本，请勿在真实环境中尝试。

感谢关注大仙安全说

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs5Z9YYreb8LonZ0EKcxDIfILgz4JlpI06HusCS54yAIACRFm9N83cRX3lRvYDIvcqTj5pBj1oAn2XjKpRRTU21IYaaeibaAuARs/640?wx_fmt=png)

**添加好友注明来意**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0Eghr41R49Dsaibt7QQtMcrDaRXfz1W7bnr1Ajjd8ia3xhsylXhcJcze1tic4XKZcrn5LFSm3rTicZBhg/640?wx_fmt=png)

**公众号丨大仙安全说**

**VX丨weiqin\_6666**

**长按关注**

《往期阅读》

[注册表被锁、任务管理器打不开？“Debugger=0”引发的](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485084&idx=1&sn=0b44a18056390d9ae175eac9e980096e&scene=21#wechat_redirect)

[实战拆解：Autoruns揪出隐藏的计划任务木马](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485083&idx=1&sn=899a620666440c37d664f3ca04823acb&scene=21#wechat_redirect)

[零基础也能分析病毒！Noriben新手入门指南](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485048&idx=1&sn=930f31e639608dd45717ac99f907307c&scene=21#wechat_redirect)

[使用 Sysmon 如何精准捕获“银狐”域名](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484781&idx=1&sn=4b361739b4fffda6ebdbba7b412fb61c&scene=21#wechat_redirect)

[使用 DNSQuerySniffer 揪出隐蔽钓鱼请求](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484778&idx=1&sn=277c154e55ac14a63430109329b0b2c2&scene=21#wechat_redirect)

[整个网安圈子，谁还没用过Procmon](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484724&idx=1&sn=0e6aa9c5cf1eeca183f2152105301dfd&scene=21#wechat_redirect)

相关话题：

#网络安全#黑客#网安圈子#应急响应#应急工具#大仙安全说#promon#Noriben#恶意样本分析

求点赞

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FZMB3vsw4wxyNMbXwC42FoG8KmicxOYyR9Em8f5BFRia2jia66l1HibEyCKXqUq6bGLUCj7uDtZS58pg/640?wx_fmt=gif)

求分享

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FZMB3vsw4wxyNMbXwC42FoHFSQRwicdBWfDiaNibTtUyQ2lPiaicDV5pZaUgZTzY3TJQ3ZbmR1Tj5iciaYg/640?wx_fmt=gif)

求喜欢

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FZMB3vsw4wxyNMbXwC42FoAV9dDSmbcAxOs8iaCgcpDEBjGNObDFpgTXjZSyjr9DzTgMblPrUYILA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/afo75o4gacpFHp4O7KXstEGdnGtCnk9v1azmwLFNoS3XPibDA2mw0MKuDbLj96h4eNIdOKXRicDicTn4PiciagBpZWQ/0?wx_fmt=png)

大仙安全说

向上滑动看下一个

知道了

![]()...