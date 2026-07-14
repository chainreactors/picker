---
title: 2026FIC决赛（全解）
url: https://mp.weixin.qq.com/s/_0NId2s1NpdV_xAA3AI04w
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:43:07.467206
---

# 2026FIC决赛（全解）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T5C6icTcSx9PwNYlJ66Csk8Yw9SY2wbmeyzojKIPHBH5PN8PMicvPuIuIpbdmTu3L8UHanVlhTicZ6TakIKayIs5wmcKEUTVxFS7ItS1ia0q3N8/0?wx_fmt=jpeg)

# 2026FIC决赛（全解）

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于Serendipity的小屋
，作者Serendipity

![](https://wx.qlogo.cn/mmhead/7SPO0mRJt6AuWgRC7FicX7WSwDDqk3ybZibph1OBulDITWricfrazCO8cKeh5caiaV4FWhjvZ86lEDM/0)

**Serendipity的小屋**
.

致力于每一次的赛后复盘，供大家交流分享
团队公众号：云影安全实验室

容器密码：`\/a15f5b1d-a9fbdb79-de9ee6bf-28b9fce1\/`

## 计算机部分

> 做了下计算机发现好多逆向，对于没有AI的我根本做不出来，还是得继续学习

### 1 分析计算机检材，嫌疑人telegram绑定的手机号为

### 【参考格式：110】

**14453319203**

火眼可以直接分析出来

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NlZUa6TCOvXiamkxiaFX3mXYQzbx0icgzTjlg1BkT9ibhWEugkqibuODiasN9RQI7c0F4JxkYe0NQlGZIPE5IhtdxbpOvyScryE5Ggg/640?wx_fmt=png&from=appmsg "null")

### 2 分析计算机检材，cherry studio工具配置的默认模型ip地址为

### 【参考格式：1.1.1.1】

**192.168.50.156**

仿真之后打开cherry studio，查看模型配置![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NIc1gCW0o2FRPOF5qs3x2iarzjwHNJiafVYiaagwiaF9pXeTzvlRUMDicoDwUPlYshz9RTth7a5E0WuzeGic2SdaFHAb3FMR6Q1Ram8/640?wx_fmt=png&from=appmsg "null")3 分析计算机检材，BitLocker的恢复密钥后6位

【参考格式：000000】

**414590**

看到桌面上有一个backup文件夹，打开看看

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NgArNYkDia9hZe5AmxyHRzW80fPLyHbpugB2PnprJSAcNDs5XVD0TEtTdeqSMszG2pN23A8ZVZ5AicTCjvnicFFryXbhSVBRJDmI/640?wx_fmt=png&from=appmsg "null")

有六张图片，拼图拼一下，在everything文件夹中有看到引写工具的提示

> 好了，我真得压力队友了😊

先拼图

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Nzh1AvvFiaNTbmVsktKOLYRdhBmdk9OXVs6qBoaOa18zTQOEickftvCBOpnVSZu9gcDvzmiaiaopuYF80VKM5wOmVbC96DbDDuMhM/640?wx_fmt=png&from=appmsg "null")

然后用引写工具打开，发现类似二维码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9ONo4yHwHF1LsNj2PK4gy62ibB5650pmxPOQAZRJt2BuLbO2pu0WfTbPicJGdhZTIRJT8khetvc4dpyTBz6gGq3AELuUsdialYeTU/640?wx_fmt=png&from=appmsg "null")

后面发现应该是截图像素点会变，那就一个一个放进去拼好

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PKQibatKp45DVyeAy3NFaCfBHiaXa8D7AW7dRQxkUTR5l4Iyd5LA8FV65RSx477IeAA4IHbvtJaG1wRQUauS2DFEY3WWXYPjWJk/640?wx_fmt=png&from=appmsg "null")

成功拼好

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NuOnG5PWDgcMibm8rZmVjZREsgNtxHcHzqr8kEicaz8aDCa1JrgzAerzhO5WiaMYQT5icvxZnibvibkaLM4tf8s4S2eS4OfkBB5qaj0/640?wx_fmt=png&from=appmsg "null")

扫码得到BitLocker的恢复密钥

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MP3oDZr51hTmUHS58ichvVNCibpcUnSADy2JgFeCbCyuVbSaOd93ZzJud0q3KB1bFWzWCCicibwWL4TvZ21l1D7pib6pXCwp3dYbpE/640?wx_fmt=png&from=appmsg "null")

### 4 分析计算机检材并找到proton邮箱的助记词，第一个单词为

### 【参考格式：bad】

**settle**

在D盘key文件夹下发现与题目相关文件![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Ps7ly5cichBNxpgVxQ1HqNIS6NCibR4B4HGSicAbicnwtC4Nic1KyYDlCuYicBMQ0T5SFYRhVP3PjvKZkcTfkQ8YHCPDqibWRS5kg6es/640?wx_fmt=png&from=appmsg "null")打开发现需要密码

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Ok34spqav2LDjkxBKqXuZkia3wVaIzMPsfslriaSjqFQrCEQJ0Ygicwgpibzr8YeSWTu71GPVHf4ECrkibXTVRV1QsPgKIxpibz3zEo/640?wx_fmt=png&from=appmsg "null")

passwarekit爆破一下（佬们有没有其他方法，这个得好久）![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PWA0ibQwicLxLQQTSAN0GQIgj3ya9rFrPtIvcV0wh28T0Sa32uvicZNAicFCFLnoLb4l1VzoaBa6QS1n2QySzibeUZxb4c9E53jKdU/640?wx_fmt=png&from=appmsg "null")打开pdf

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9P3ULsAIpdWhBzhVm86JfZqoHv5FcxzHiaPczXbGXOmK9PAxjPAtCoyGd9KQBZlloNz8ETricicXiaztjTtz6MzAOC5vDCW8q6Mnlc/640?wx_fmt=png&from=appmsg "null")

### 5 分析计算机检材，嫌疑人对zhuhu.fic网站发起攻击时，用户名user对应的密码为

### 【参考格式：123】

**1qazxsw2**

这个题比较恶心，在yakit里，打开yakit![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9N7gKyoYDibibI3TGvic8KsVb1lrhH7NeFicM1VFzR0gT2iakoicq0tz65eMKL0jUxIUyqXPGtgA4zCMibvMficciaYNpb7ibkVWSU0Q9KEA/640?wx_fmt=png&from=appmsg "null")查看历史记录，搜索zhuhu.fic

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OMvV7dXnZDPia2QRzc6TxuAXfTibYdvkcMh31WBdsDU9hXvjC2VRaibagcMAwsiaicicrXepicmYYwHjLHeg8mYEica4udzPh2Pn6B5tE/640?wx_fmt=png&from=appmsg "null")

### 6 分析计算机检材，嫌疑人对zhuhu.fic网站发起攻击时网站使用的jwt，其签名密钥为

### 【参考格式：123】

**admin666**

找到jwt

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NtQXbcppdAYrvSTKtRqVzQtdic2V0MG5D9ViaJTgto4q8O5je5dNaTa3x0kcK7TMHs2ODSy7eqXTwVlgHLYByEyRsB4okqmiblhs/640?wx_fmt=png&from=appmsg "null")

写脚本爆破一下

```
import hmacimport hashlibimport base64import sysimport time
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzc3NzAxMjc5fQ.fzH7mSgYvu0yv6SHCUhd36h4Vx9RhZdkSnOfz0Ptm84"
WORDLIST = "rockyou.txt"
def base64url_decode(s):    s += '=' * (4 - len(s) % 4)    return base64.urlsafe_b64decode(s)
def crack():    parts = TOKEN.split('.')    header_payload = f"{parts[0]}.{parts[1]}".encode()    target_sig = base64url_decode(parts[2])
    print(f"[*] Target JWT: {TOKEN[:60]}...")    print(f"[*] Algorithm: HS256")    print(f"[*] Wordlist: {WORDLIST}")    print(f"[*] Starting brute force...\n")
    start_time = time.time()    tried = 0
    try:        with open(WORDLIST, 'r', encoding='utf-8', errors='ignore') as f:            for line in f:   secret=line.strip()                if not secret:                    continue   tried+= 1   sig=hmac.new(secret.encode(),header_payload,hashlib.sha256).digest()                if hmac.compare_digest(sig, target_sig):   elapsed=time.time()-start_time                    print(f"[+] SECRET FOUND: {secret}")                    print(f"[+] Tried {tried} keys in {elapsed:.2f}s")                    return secret                if tried % 100000 == 0:   elapsed=time.time()-start_time   speed=tried/elapsed if elapsed > 0 else 0                    print(f"[*] Tried {tried} keys... ({speed:.0f} keys/s)")    except FileNotFoundError:        print(f"[-] Wordlist not found: {WORDLIST}")        print(f"    Please place rockyou.txt in the same directory.")        sys.exit(1)
    elapsed = time.time() - start_time    print(f"\n[-] Secret not found. Tried {tried} keys in {elapsed:.2f}s")    return None
if __name__ == "__main__":    crack()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MRQc3uvBA5f86fhjWBfFFNJMqOiaLQPyAb1J8MjHmbhed1FJWrd8cz4S1yoiakricQtvWBKcFUEgBoIWnXCoBWialoiakricSaov7QE/640?wx_fmt=png&from=appmsg "null")

### 7 分析计算机检材，嫌疑人对zhuhu.fic网站发起攻击时，使用的反弹shell中配置的外联服务器域名为

### 【参考格式：baidu.com】

**yutubi.top**

翻一翻就看到了

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9M8lABRWWySqd73FBib8gKONGBROe5a98QZNX8IibWhOGLb6TwLnyaa63tsHiconFXHnSzbiaibHNk8ITmWUf7luklkdnfUZHzsVMoY/640?wx_fmt=png&from=appmsg "null")

### 8 分析计算机检材，嫌疑人对zhuhu.fic网站发起攻击过程中，下载的住户信息文件密码为

### 【参考格式：123】

**kfcvme50xiexie**

翻一翻就可以看到，这个答案太有梗了😂
![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NeboiaYriab5eEX9eeruNSrFtSaASdm60ZkJzhxC293QTEtFAfwFyQ9WDYCGf2I8U6Tr0gSqYdiaIickavlQN43Nyn3RWkS1FCBmE/640?wx_fmt=png&from=appmsg "null")

### 9 搜索计算机检材，找到迷宫游戏中预设的最优路径，分析游戏中隐藏的密码

### 【参考格式：123】

**427d672e8b36c12343f8380628025677**

程序是一个 Electron 应用（`passkit-ProMaxPlus.exe`），核心代码打包在 `resources/app.asar` 中

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PELdXW1x62vJ0OCzBux9mhnndcE7ib5VkRFej3HfFibwib17gibEwU4bx8wTbb6d72SiazxasoMhjrnBL7cLyKQLfJ9Rh1AODicF81g/640?wx_fmt=png&from=appmsg "null")

使用 `@electron/asar` 工具解包：`npx -y @electron/asar extract resources/app.asar resources/app_extracted`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OcbBNcbG52CBZCla7dPTp1LxvVqiahowp5cKMziaAEiabYdfdAzAoO6uldHMFG7DiaEo0AvjkdFfD150ymtL3NStCIt5XXFduFGnE/640?wx_fmt=png&from=appmsg "null")

•`main.js` — Electron 主进程•`map.html` — 游戏前端页面（含完整游戏逻辑）•`map.txt` — 迷宫地图数据

分析一下map.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9P4PIBMF5wuibIjHSNyx9p2SVia0NcNVOibtJdcze5RrnnjmXECVicOhRYCjp00xAXVnicXHWC8dD3zseWKcqqOfic1I0757SsmhIQw8/640?wx_fmt=png&from=appmsg "null")

•第一行：`20 20` 表示 20行×20列 的迷宫•后续每行：每个数字是一个格子的墙壁信息（4位二进制）

•bit 0 (值1): 上墙 (top)•bit 1 (值2): 右墙 (right)•bit 2 (值4): 下墙 (bottom)•bit 3 (值8): 左墙 (left)

在 `map.html`，找到关键验证代码

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9ML4xxDLiaSiamGotv4gfkeqMtnUClKvRKlqzmSSLNibU4nkgiakeALeIELZH21R9WETZwIy6xGV9R6UyTwo68ayibXxHfzoZ5pYwds/640?wx_fmt=png&from=appmsg "null")

1.`logicPath` 记录玩家经过的每个格子坐标，格式为 `col,row`2.路径用 `|` 连接成字符串 `pathStr`3.对 `pathStr` 做两次 MD5，与硬编码值比较4.如果匹配（即走的是最优路...