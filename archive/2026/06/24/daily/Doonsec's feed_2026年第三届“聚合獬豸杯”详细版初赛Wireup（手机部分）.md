---
title: 2026年第三届“聚合獬豸杯”详细版初赛Wireup（手机部分）
url: https://mp.weixin.qq.com/s/c1ievCExth-u1cAQB1r7rA
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:03:41.779187
---

# 2026年第三届“聚合獬豸杯”详细版初赛Wireup（手机部分）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icicuurjDpOdIuAH4ygVz8gmManlHg9MRc2ibib2eP8NBQfpRUQKUYQa2kChxbgR0cCtths7uOMk7UNEicB6K7anuC9elueZ0hzDuUo/0?wx_fmt=jpeg)

# 2026年第三届“聚合獬豸杯”详细版初赛Wireup（手机部分）

原创

落寞的鱼
落寞的鱼

鱼影安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/iabIwdjuHp2WoekX6fnZ3APEKJwyvmf76EZ0Z309yU3fUicsMz4d7aZ7G41VxQPvKcqmzdqnYwcgWW0V6c8LZBiaQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击上方蓝字·关注我们

#

#

**前言：**

***今天这篇是獬豸手机部分，整体坐下来思路还是ok的！***

***100%正确率，主要是第10题比较坑，需要更新后仿真成功！***

***虽然不是首发，但是思路和方法还是有些不一样的，感谢观看！***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icicicvLtu4vKJleiaqG2Gia7XSsBayTIibqHicgRJ19ryP6pWAOfgNYrrukIHjT2Hib7UUoaAx9pLrhHLu4GzxBIzpgib76mKZBYyPKXL4/640?wx_fmt=png&from=appmsg)

```
容器密码：EVJbYf&+eStnx5B+C^bj%YPSr)gr检材哈希：82143788C36FCF1B4C549DD83514C2670A89C494F644F3A3C4FA415246EDD394casdn博客：https://blog.csdn.net/Aluxian_?type=blog知识星球：中高职技能大赛/数据安全真题专项（可进内部群）B站：https://space.bilibili.com/319081177?spm_id_from=333.1007.0.0vx：Yu1yuu1(欢迎交流学习/交流群/取证学习可以一对一指导)time：2026.6.24
```

手机部分（正确率100%）：

1. 请分析检材1：手机的序列号是什么？【答案格式：AB65CDEFG6HIJKLM,字母全部大写】

路径:adb/ksu/log/dmesg.log,搜索 serial 看到序列号

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icicwamaIbbhIibKpKy0ujMWvK3iawtFQO3rI3OhPlibo0IbmxK0CBN6TDhH8yYq1uohUSVq2rZC2S7Ur0k44Fp9kib1DJLsFOv0LTLE/640?wx_fmt=other&from=appmsg)

正确答案：AM69VKKVU4CMGELB

2.请分析检材1：该手机的具体型号是什么？【答案格式：小米17至尊版】

路径:/adb/lspd/log props.txt 日志配置文件

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icibcHnlIcqNMZ7OwaRZncjzfc8gLUerKjPoDH7wR12oaWTxTXSH2jGYWHewNptenrNjqNLuDwQZ8jGcP0ZMyxlIMsKB7zNHc3Os/640?wx_fmt=other&from=appmsg)

正确答案：一加Ace5至尊版

3. 请分析检材1：手机中已删除的联系人手机号码是什么？【答案格式：12345678910】

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/qK3m3mOz5icicqQJavlaC7SGJQ6iahnPORZfEF88td4Qo3IPtSohJLGBLWmhfa8YxovrHopiaLKPhP2HRiau2hs0SbY40QZjtUA59hd4ovW3eTBw/640?wx_fmt=other&from=appmsg)

正确答案：13696966666

4.请分析检材1：手机中找到密码本文件，计算其MD5哈希值，取后6位，字母大写。【答案格式：EF3898】

在图片中发现 常用密码 全局搜下 计算 md5

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icibyf6flvQgTO8dYYJNeicyZWfkVQ3Gor4QNu6HujDP6ARHZicibIpl1sE36BHmxkVlkjRnuQyKRmuWQgee0pUjEveKL0Gc9ic357n4/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5ic8IH38GZHQ2uMWZlVJXNiawVrMb8FjYrAAPmGZr4iaEg9nH9WfU52TK5jcxE1yibqdLX4dMfMicEu81WuCOu9SvcgVgicYibZKXRQXQE/640?wx_fmt=other&from=appmsg)

正确答案：AD3563

5.请分析检材1：嫌疑人下载的图片隐写工具名称是什么？【答案格式：outguess.zip，英文小写】

思路：看到题目格式.zip直接找 发现是steg隐写工具

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/qK3m3mOz5ic9G32N34wjrVxwWRR8HjyjYgdzLug5tb94Zh6E0V5pBY0vGqcFibtem4Se3yfRAFySsdNGlpja20DHZzZrEy4yUlOQMPrMpOzyo/640?wx_fmt=other&from=appmsg)

正确答案：steghide-0.5.1-win32.zip

6.请分析检材1：嫌疑人使用隐写工具进行文件隐写密码是什么？【答案格式：ABCD@202002】

查看相机有张不一样的图片，猜测是隐写的图片 还给了常用密码，应该是用里面的组合爆破密码这里跳转源文件，导出不然会失败，爆出密码：JHTJ@202605

```
steghide extract -sf important.jpg  #需要输入密码
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5ic9dG9vNfib4u5Aibiaibjzq6MeLFFic8qzUwTNBkVLCMRvmLibcw3icvYqic5cSuFCbIPcksGW8kH3kpYg8icDDP3sQcemiaW31o1SsEWsaQ/640?wx_fmt=other&from=appmsg)

```
import argparseimport subprocessfrom pathlib import Path

def load_passwords(path: Path):    raw = path.read_bytes()    for encoding in ("utf-8-sig", "gb18030", "utf-8", "latin-1"):        try:            text = raw.decode(encoding)            break        except UnicodeDecodeError:            continue    else:        text = raw.decode(errors="ignore")
    seen = set()    for line in text.splitlines():        password = line.strip()        if password and password not in seen:            seen.add(password)            yield password

def try_extract(steghide: Path, image: Path, password: str, out_file: Path):    if out_file.exists():        out_file.unlink()
    cmd = [        str(steghide),        "extract",        "-sf",        str(image),        "-p",        password,        "-xf",        str(out_file),        "-f",        "-q",    ]    return subprocess.run(cmd, capture_output=True, text=True)

def main():    parser = argparse.ArgumentParser(description="Bruteforce steghide password with a wordlist.")    parser.add_argument("--image", default=r"C:\Users\Desktop\important.jpg")    parser.add_argument("--wordlist", default=r"C:\Users\Desktop\常用密码.txt")    parser.add_argument("--steghide", default=r"C:\Users\Desktop\steghide\steghide.exe")    parser.add_argument("--outdir", default="steghide_important_bruteforce")    args = parser.parse_args()
    image = Path(args.image)    wordlist = Path(args.wordlist)    steghide = Path(args.steghide)    outdir = Path(args.outdir)    outdir.mkdir(parents=True, exist_ok=True)
    out_file = outdir / "extracted.bin"    passwords = list(load_passwords(wordlist))
    print(f"[*] image: {image}")    print(f"[*] wordlist: {wordlist}")    print(f"[*] passwords: {len(passwords)}")
    for index, password in enumerate(passwords, 1):        result = try_extract(steghide, image, password, out_file)        if result.returncode == 0 and out_file.exists() and out_file.stat().st_size > 0:            print("[+] FOUND")            print(f"[+] line: {index}")            print(f"[+] password: {password}")            print(f"[+] extracted: {out_file.resolve()}")            return 0
        if out_file.exists():            out_file.unlink()
        if index % 50 == 0:            print(f"[*] tried {index}/{len(passwords)}")
    print("[-] password not found")    return 1

if __name__ == "__main__":    raise SystemExit(main())
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5ic9TcM4xWu6tSSLibhf2OEOJNr75Zujic2YALfoia2UVqE0UksUwTGWX40e4XtZpfpBCrvCSs7SMc77jCwrI7dyl585qb4SNl9uFQE/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icib1lvxImDfGs8h7CHA2eP9DyYxEqfiauSicXd08cEaNc1ics1Xb1oyIcMVUNIoV4Yu4u34iamvWaibgUxOQTw2K0eGssYia4CyvbbJ7c/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/qK3m3mOz5icicHmjC3AL6W4dI1zw6awicF2DQHZCLM73v2H0C65ibVHq9iczOQp1FrvMZx86IuKfE2d08b6gbpRymkAVUpEgBbyTkt2n1zmUXCd4/640?wx_fmt=other&from=appmsg)

正确答案：JHTJ@202605

7. 请分析检材1：嫌疑人向数据贩子购买公民个人信息共计多少条？【答案格式：123】

简单看下APP认识的感觉就这三个聊天软件

```
org.telegram.messenger.web   #Teleqram包名uni.app.UNI04963C4  #i聊包名com.lianqujiaoyou.chat #连趣包
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icicLabwNnnmlZzh1m5HyyFpxgUzbghYoibgwSHarpUicic87USoiadJX8iaLicVQQTIQr4s8LyDGZVuu4PnmQTV2oIjbaut1c3NlvFBRs/640?wx_fmt=other&from=appmsg)

这里就去找数据库 仿真查看或者直接数据库查看内容：

Teleqram包路径下空的（直接排除）：

![image.png](https://mmbiz.qpic.cn/mmbiz_jpg/qK3m3mOz5ic9BbIFsSZq7p9VhKicGLMdnrCOlKZK5Y5nyiaictpcZbKuXOFIQ7zELZG5fnn3PUWmCdiaEFVvporyBNpIxM6plBK9ZtZbcTDWIWMM/640?wx_fmt=other&from=appmsg)

i 聊：

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icibNHibialK0peelhniaV1MsCicvnTrYCLicicwUDn4bV3Rb1VibbToPEB0BxKyEAOGU8cb3f1agOol9ibmceZmIibVsoxgLbXnhSHwIFxoE/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icibCvRO6eg3MXXGEicQfE2qwREibUibEFC5f0icvmFlDMZs27xRLwCeGLIkicmzG5xTAmvqh0j7YzhjuiaGOS0RPZ8GnAMcc0jyaDRibXc/640?wx_fmt=other&from=appmsg)

连趣：

搜包名,发现了配置文件 得到账号密码:1355997814/JHTJ88888 仿真

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icicxmBUEmctyibEzcHx64TyHpkxnYb2eHriaYoia237TeURPl1VLmODwibWGRJbg18bP2AWO9YZ7PiasKTSML0Eayl1Scg5cKJTSyiatU/640?wx_fmt=other&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5icibUbiaTA0v65icVMPo2iaaUKuzgvgIv4ZSwB81NquYrZVqyvZTXhvQuyOYia4RWxyhLAqLwarp4KI9M3mWP37eLP4xyia6B4XGgfnF8/640?wx_fmt=other&from=appmsg)

正确答案：100

8.请分析检材1：嫌疑人向数据贩子交易时使用的付款方式是什么？【答案格式：支付宝】

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5ic8LDj39yzahnVRgODs9QhEV7V6EROmax3gSYQhAfBZJqic0A9GQGIM42pD5MibQ7icic8pNWWuy48xG9JEdrA0uWgtmFibs5eyqQCPo/640?wx_fmt=other&from=appmsg)

正确答案：银行卡

9.请分析检材1：数据贩子交易过程中提供的银行卡号是多少？【答案格式：6222351234482925678】

同上

正确答案：6222355XXXX82923738

10.请分析检材1：接上题，嫌疑人所使用聊天工具的用户 ID 是多少？【答案格式：12345】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icibvR9JciadzNV8c7ibEjRED...