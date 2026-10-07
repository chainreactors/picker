---
title: 0xGame 2026 wp
url: https://mp.weixin.qq.com/s/y8wmryysRmnE29_G0NXtbA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:53:50.069476
---

# 0xGame 2026 wp

# 0xGame 2026 wp

原创

onepanda
onepanda

OnePanda-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**OnePanada-Sec 招新啦**

**招新要求**

* 热爱网络安全，喜欢 CTF；
* 拥有 CTF 比赛经验，有较好比赛成绩的；
* 乐于奉献、热爱分享，愿意提升自己同时帮助他人；
* 时间允许参加各类赛事，服从战队管理与安排；
* 各类比赛获奖者、能力出众者视情况考量；
* 未参与其他高校联队；
* 大一同学视情况放宽资历要求。

**联系方式**

请将个人简历发送至以下邮箱：

简历邮箱：2638726415@qq.com

#

# 0xGame

# 第一轮

差一道pwn的题目没时间做到，到处旅游去了哈哈哈哈

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOvyqewtvqf5aBicVnDuKiasbuHAG8YsX9Od8eudB8uFyDicOlU0N6lzZo90jyEg9aoesA3qA6cey12Nlk3FE7yHwD8gMRUam2loqU/640?wx_fmt=png&from=appmsg)

web

### ATP代码实验

说的是禁止粘贴直接js禁用即可，然后就可以复制粘贴了

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOs1Fob3kVZ2rvcegkBfHW1E3dOwIEeMV6mhTNkLiaL2LqgqYXSeyPwNGbcGxj60aaf9jmHXgfHRm2zDiaicjSOltmpfLbeGKgpYPo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOtYiaX1KnR9Oa29ZfG1EuaOlLcJTiaibE3WHoHicaicM6QHictBiaZp39IgsHfAmLqA4zSib98bhgGlvahZeRvRibbrS7DUXQSmud3oPzZ8/640?wx_fmt=png&from=appmsg)

flag：0xGame{bd2e0f07-8229-4399-800b-b508c8e17553}

### 奶蛙的博客

通过页面发现碎片哪里有字母把所有提取出来，开始想的直接python提取结果被页面隐藏了，直接在控制台提取

```
 (async () => {        const base = ”http://8000-50180549-8042-42ef-8025-60bc58a0d2bf.challenge.ctfplus.cn/page?id=”;        let result = ””;        for (let i = 1; i <= 124; i++) {          try {            const res = await fetch(base + i);            const html = await res.text();            const doc = new DOMParser().parseFromString(html, ”text/html”);            const el = doc.querySelector(”.flag-fragment”);            const letter = el ? el.innerText.trim() : ”?”;            result += letter;            console.log(`id=${i} -> ${letter}`);          } catch (e) {            console.log(`id=${i} 失败: ${e}`);          }        }        console.log(”拼接结果:”);        console.log(result);      })();
```

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOufZEibVOUTbz0W8PoxUofCVj2jFSCqiaWnegJ9fFaYM3pQakwQib9LdmhkE5ia07fcibic6mWcXEiayS6ToHHa2TBkicMH3IHyP6YftLo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOs0K4axRnIHDC98psBtzXzZgfhZGiavY93uv43Od1iaTL1VRfkIA0WQXROVbTywRwRr35XfEWZibHdLnRrXgqicHkNSpiawDcsaibYFk/640?wx_fmt=png&from=appmsg)

拿到：

H4sIAAAAAAAA/wTAwQ2AMAgF0JXaADM4xo9BbQ+UA0GrMe7uK/eyjv11rpNhfLYu0OBpAvYNWsxIU0AXxYMjuA3yBGsUEWQnVE8Kp/z+AAAA//+XJ0P/SwAAAA==

这是一个base64+gzip的压缩的数据，所以不能直接base64解密

```
import base64, gzip     s = ”H4sIAAAAAAAA/wTAwQ2AMAgF0JXaADM4xo9BbQ+UA0GrMe7uK/eyjv11rpNhfLYu0OBpAvYNWsxIU0AXxYMjuA3yBGsUEWQnVE8Kp/z+AAAA//+XJ0P/SwAAAA==”data = base64.b64decode(s)print(gzip.decompress(data).decode())
```

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuyQTkGsLCG3APwpLiaP3gPTXJwICjKnkAW409jzvaKIKKjtV6IRhLFtfjGR9qqNzNuCoTs8ft5qzHb8TWiaRZbYyMDN6Ss0iarjU/640?wx_fmt=png&from=appmsg)

flag：0xGame{n41w4\_l4ugh5\_cr4wl5\_4nd\_c0ll3ct5\_3v3ry\_fr4gm3nt\_4cr055\_th3\_1nt3rn3t}

### ez\_64

首页直接展示了 PHP 源码。关键逻辑是从 GET 参数 c 取命令，只允许由 /?. fla64 中字符组成，然后传给 system() 执行：

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOtDB6wsMckMfgCBtlic3bof6p4EmTU2ib5VJJIS9IQSsVlYzibDg1D7foNRg9f5VZhogCmyia0icBB5Ho3AIQ3vAcVicNkODICibnKxso/640?wx_fmt=png&from=appmsg)

白名单禁掉了命令字母，但允许 /、?、. 等字符，因此可以用 shell glob 通配符匹配可执行文件和目标路径。利用 /usr/bin/base64 读取 PHP 文件，再对输出进行 Base64 解码即可。

```
/?c=/???/?a???4%20/?a?/???/????/????.???
```

其中：

* `/???/?a???4可匹配/usr/bin/base64`
* `/?a?/???/????/????.???可匹配/var/www/html/index.php`

拿到base64编码的flag

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuWcibibHsnpBYuzx31ibRrYYXibBbAoXTDPzxtMvCqOgAFiaQNLqjb4QOsrLiakCUKKDHn3G4BOmaNNudmZywZva2vZM4CwRBv1mqRk/640?wx_fmt=png&from=appmsg)

base64解密出来：

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOvhtiavbpdVTFsYC2zl6F5qEibCJ1YiaXWbRwUUlDkf0fib7RpbYyEIgNBrX4tGcMicjibDibsJ5yx9sCcAHQGTf7NwQAznf9eI8AyV08/640?wx_fmt=png&from=appmsg)

flag：0xGame{e2708ed1-9b91-4db7-a741-120fb617b7dd}

### 欢迎来到CTF的世界

在pdf中找到base64编码的flag

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuxd3WPMYhMdvwwal28184q0WZlBfaY5PseJY2hMia3QBapImI9HTdq9H83VWJZYqiaT43ow5mYCMr4ssoaHv8NiaSUj6q4E39Gyk/640?wx_fmt=png&from=appmsg)

直接base64解密即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOvtNOeibv2qpdCMsgvHKVVjQlaoxSavyIVUgj4haYzn7brKptjK7lcaUPibk0NpzjQb7jWIpo4yEqHwTSJVPDFQ3LADDSD9BOcB4/640?wx_fmt=png&from=appmsg)

flag：0xGame{welcome\_t0\_the\_w0rld\_of\_CTF!}

### 错位的签名

通过guest，guest123登录成功

发现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOswdnbqB0dFAiaTRwf3Rk2ibIcwLTmtPI8H2YnwEjdsyQ4cZtDVLhmYwCQoxRpe6uduMzZicpUsYw47sn59o4U1fwwILUMxm4WVEU/640?wx_fmt=png&from=appmsg)

访问公钥，页面公开了 admin 用于 RS256 验签的 RSA 公钥。

提示题目环境使用 APISIX 3.16.0，并引导关注 JWT 的 alg 字段：系统既信任公钥，又信任 token 头中的算法时，可能出现算法混淆。

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOsF4ic4QibjIKMnwsXWqIxliaJFMUqQcC3ibmlxlribelalVF7vWunvPorkb0JN7hOCrdAokAk4BVvwKq8tUvAW9XL1CCibWStMWp2ib0/640?wx_fmt=png&from=appmsg)

点击flag页面出现jwt，权限不够就是提权成管理员呗

直接开始做，将 token 头中的算法设为 HS256，并把公开的 RSA 公钥内容作为 HMAC 密钥；payload 中将用户标识和角色设为 admin：

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOtQ0RquOPiazTuTdB2ur5PWKsXHyEUFdFgJjReJlib9PXA2X5jPNezZeianz8JcdDWjl6rErFajtqxU3E8ZzWRCTKZBokzqcX9bks/640?wx_fmt=png&from=appmsg)

替换jwt

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOsAUZicINViagvxwgHke33M4EcLF7xnh3icmZrIGviaaFQQl2CP44EFVxd0VsAshg26UKGtsWIGROPSFgRL8FMUfh50G070MXpsGics/640?wx_fmt=png&from=appmsg)

flag：0xGame{0ad8255d-37f9-4466-b904-9495d445d762}

### 渲染如呼吸一样简单

考SSTI

{{ 7\*7 }}返回49

说明模板表达式会被执行，SSTI 存在

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOtEKAV91PT9NjB3C9JLEvn5JHVNBbYDBQMxKZOS9B06rchCKFJBYPFYfibR0rDwMZBKiczHa6tQAYzHQCL40RA9lR7cOjmcOtCII/640?wx_fmt=png&from=appmsg)

返回空白，说明当前环境里 cycler 的 globals 中没有直接暴露 os，或者被过滤

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuM13r1fYGHCib9juqxNPlB7icBanolcbTic2ZDia1tImCE2CqebLDiaamtNLkaDXicy3s0L4GeZxtBh5d2BZGkiamWWA5fA6nRCicTUMI/640?wx_fmt=png&from=appmsg)

在返回的类列表中，发现了几个关键类：

```
<class 'os\.\_wrap\_close'\><class 'flask\.ctx\.AppContext'\><class 'flask\.ctx\.RequestContext'\><class 'werkzeug\.test\.Client'\>
```

优先尝试 os.\_wrap\_close：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOubJXgVVu0UuX0W0oKoo7tPElQq6iaI9iaIEr4WGRmqnln3PcN9QuxffQ3vm9iagiatYD7WOR4ucrgPIAO08Noiaay5P4E45tlChTkw/640?wx_fmt=png&from=appmsg)

仍然空白，说明该类的 globals 里没有 popen 或 os

没有出路直接转向查看 AppContext 的 init.globals

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOtNJWD4JzyppcmrD982arMAflbp9A2LtCZUDjqEib9UDWgSvugU7OLJpZIT7McHcD40yDZomiagxE6Ep6jialnWLMhwWc5er5f9E0/640?wx_fmt=png&from=appmsg)

返回的 globals 里包含完整的，有了 import，就可以直接导入 os 执行命令。

直接执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOtXfpf7EXtUjyhDNxl10CY7ibWTfC3CdX2U7mkOBjTfN4rFSYT43nYUfndxoNXB8rqPSGbkvYcgnsqnFwbcJsccnoRV9h5FpSaU/640?wx_fmt=png&from=appmsg)

命令执行成功，当前用户是 ctf

列根目录

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOt5qEWxnfYLTHf1ibsyVSMINyzdeJ79Q6ksWXYsn9Vf7fPx2RJ1RtpG8zlBb7MycMFic5tySPC1fyybDN67J7IiaibwkwA7uagfxII/640?wx_fmt=png&from=appmsg)

存在 /flag

直接读取发现是空白

查看下权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOs56j431v43n5PwR8ghM3bymb8ybY58nkTos8ud4MeNcZABABsn4Byiczwz68icXW4rKxdT49MXhm6C9OamEUwWXq6eiabkibEDPwc/640?wx_fmt=png&from=appmsg)

/flag 权限是 0400，属主 root，当前用户 ctf 没有读权限

寻找 Flag 来源，查看启动脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOsrcLClxWUfvicCDwiaAsJkmvjaiaQ3CkcqhJPc9via9walS5ICn0fEK8jHhGdqxt4prsV0ORf3GToHBRaGo137QNaptv6KXNjZADo/640?wx_fmt=png&from=appmsg)

关键信息：

* Flag 来自环境变量 FLAG
* 启动时写入 /flag 并设为 root:root 0400
* 之后用 gosu ctf 降权运行应用

也就是说，环境变量 FLAG 仍然保留在进程环境中，可以直接读取。

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOsiaCQDAcepia5lrcQXMibpr6TcweWmPFicmDXnggNRgEsV9fUskdm5qEdbLapRSMgIAEHJfgciccFUqEGIInNhXDZ7ze9UdQDT0v4A/640?wx_fmt=png&from=appmsg)

flag：0xGame{dea90ae2-f8ec-4cc1-aa87-d0339e5771b0}

### 一切的开始

直接dirsearch开扫

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOszDKN6voqvrpX1dMXX7gk1NVfhL3abg6b1uWA7NM0H2iboWMJkVeoJcAfTGcXyjJOXIWuIgR9ZzDsHhq0HZkXQd7r6Prw1sdpw/640?wx_fmt=png&from=appmsg)

发现robots.txt

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOsHQroDiaEcvibFfAdPm8lRLFYBag3eszGWG89Icp3HhRvfKsmC7XaAGFkjqOtxro1s1hpRHqjqHNQV0GpYZzDmeTEMYMTQy4l7o/640?wx_fmt=png&from=appmsg)

访问给的网址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D...