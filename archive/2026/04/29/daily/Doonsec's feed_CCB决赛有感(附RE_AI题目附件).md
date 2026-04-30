---
title: CCB决赛有感(附RE/AI题目附件)
url: https://mp.weixin.qq.com/s/yL69Ee2pmFD2AMe6YX6RQQ
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:25:37.477795
---

# CCB决赛有感(附RE/AI题目附件)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t82dBKQ1X0NDicwq7YCXVMgGicrkk0ACTSiax3ibAsVaZsZFNic5BiaKFAg7GDpjhrn45yYDsnL4WxVJOgiahGsGV0qUdDnLPicr1m0UEXsHj8aVmf0/0?wx_fmt=jpeg)

# CCB决赛有感(附RE/AI题目附件)

原创

EuSRC安全实验室
EuSRC安全实验室

EuSRC安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

“赛场很大,灯光很亮,茶歇很好吃  Ψ(￣∀￣)Ψ”

![](https://mmbiz.qpic.cn/mmbiz_jpg/t82dBKQ1X0PDlFdq1k0P0HmL7rI2XcxZbaUOzBtdm9lS1MGGkw4T9EKMW0B5ibSXxicAcT9CdmuNAEPOxDHBaCicAFqWCqPkDHeoq0S7DZic4GA/640?wx_fmt=jpeg&from=appmsg)

真是吃了没有pwn手的亏了,java基础也太薄弱了.....

话说,现场大佬好多，膜拜膜拜....

来张赛场照

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t82dBKQ1X0M1wibcxYzqppx7FuFcRWkjEjT8RsiaN5IpuxLfyNdicoEIa2ia7AfU25lRlJ5LMtcacfE3oNwpgyVaQZUPMX71GOE6FS1G5Gcpg94/640?wx_fmt=jpeg&from=appmsg)

### 实网渗透：

扫目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/t82dBKQ1X0PM6mQ6dsLUdGqkOLWI0qaN00MTpkgx067iazOgQ6NicTN8Tey3gjMmp1vgRqicFEfzRTrD4jyt7TeKnXVjlgrhlH4gMhlX3XL0Xg/640?wx_fmt=png&from=appmsg)

找到一个schema.sql文件

![](https://mmbiz.qpic.cn/mmbiz_png/t82dBKQ1X0M4ibMibOHfuf8LwQJNeUWutA4pPxibBxgCZsOHvb00g0PYLEVMeSf9poPngJpbsRghXfNsDwR5vGtNRrMT9BG4SY6hyzlI5x11DY/640?wx_fmt=png&from=appmsg)

找到账号密码,后台文件上传点上传文件，抓包修改后缀为php,成功拿到初步shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/t82dBKQ1X0Pcuib0NndlbmJCAw1kTlDRWmS4JtibINQcfccfKgNnEHQjtHyTqSeNW8tDyPHsKgAAgmo575m8bHkgO6kmJQR9EYWgsr2653Fuc/640?wx_fmt=png&from=appmsg)

上线 supershell ，发现find有suid权限，直接提权

```
find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/t82dBKQ1X0M6OTdia4RqFWIMabkIfPvfcmSHNE9KNJZcxNRBFcibvANJEibwqSMef7VKicjZLich4UT7ZEDNiac8br1LbE8fH0Dec3btHdAZFeooU/640?wx_fmt=png&from=appmsg)

```
/usr/bin/find . -exec /bin/bash -p \; -quit
```

![](https://mmbiz.qpic.cn/mmbiz_png/t82dBKQ1X0MbxRAmeSmVjicxg7iaca6c2s1l6tHnnRgWmViaxO7JrgF8MTZJR3smV5ricYJpJUMFicVe1ZSvP6ribXicaWG2PSj0CDbLvianbCxWYfs/640?wx_fmt=png&from=appmsg)

拿到flag了,后面fscan扫描拿到一个app.java和一个protokms（一个邮件网关的软件）一下触及到盲区了...潦草退场了。

### 专项能力赛

**DokiLogic**

下载题目附件给了一个Renpy的游戏，打开就提示让输出answer,再没什么东西。 在路径下找到一个`scrpit.rpyc`文件不出意外就是flag的逻辑所在了

![](https://mmbiz.qpic.cn/mmbiz_png/t82dBKQ1X0P0oOZmEWlKBHyTsTYKA2g5CkQNOBInez03NXVn9jPe7xbJiclIS40JgmdRSIw36mAbHevo8FUoGGDia4lD3Ficic2bEuAPdjnPMzA/640?wx_fmt=png&from=appmsg)

但是!我没有解密这个文件的脚本 /(ㄒoㄒ)/~~ ,以下来自赛后复现....

用unrpyc解密rpyc:https://github.com/CensoredUsername/unrpyc

拿到script.rpy

![](https://mmbiz.qpic.cn/mmbiz_png/t82dBKQ1X0OQvpBdjxyaVziaE0YJCZ2CdK60I32zkckuJDMVia2IAdkGnqBAGf3ZUVCnGhlB66pmgDsT1F761ISOXUflib6w4ia1TbBd72QMovo/640?wx_fmt=png&from=appmsg)
> 重点逻辑就是,主程序运行后会释放一个1.exe,然后
>
> 捕获其输出，在游戏开始时要求输入一个字符串，将该字符串每个字符与 35 异或后，与之前捕获的 exe 输出比较，若相等则提示用
>
> flag{输入}
>
> 格式提交，否则重试。
>
> 因此，正确的输入就是 exe 输出与 35 再次异或的结果
>
> 直接把硬编码的1.exe粘出来用python脚本直接获取输出然后异或就可以拿到flag了，我就说怎么这么多解.... 还是储备太少了,没有解密脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/t82dBKQ1X0O36WyPOChF1Qdj846nAbnWQPh0pOs1Yd7gJTyZK6a5ibQictZ8FmPxgcqbuVy5hn6hy29H8smlN8IBpaCUyBGvdXUDCibxvraJdY/640?wx_fmt=png&from=appmsg)

附上exp

```
import subprocess
import os

_f = b'MZ\x90\x00...'  # rpy里的_f也就是1.exe的硬编码数据

with open('temp.exe', 'wb') as f:
    f.write(_f)

output = subprocess.run('temp.exe', stdout=subprocess.PIPE).stdout.decode('latin-1')
os.remove('temp.exe')

flag_input = "".join(chr(ord(c) ^ 35) for c in output)
print(f'flag{{{flag_input}}}')
```

**最后的最后,公众号后台回复:CCB2026拿题目附件(RE/AI)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wTgfNmLSQExP6LGf6MM3kLr1ticVeDjnQCdQfiaRnxmAHcwcsicUV42E3rzG6UhcsVH2r9jd1OSrE5slKERm3INSg/0?wx_fmt=png)

EuSRC安全实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wTgfNmLSQExP6LGf6MM3kLr1ticVeDjnQCdQfiaRnxmAHcwcsicUV42E3rzG6UhcsVH2r9jd1OSrE5slKERm3INSg/0?wx_fmt=png)

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