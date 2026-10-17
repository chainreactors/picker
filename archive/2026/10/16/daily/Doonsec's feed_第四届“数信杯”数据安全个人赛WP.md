---
title: 第四届“数信杯”数据安全个人赛WP
url: https://mp.weixin.qq.com/s/2IZRCoshwWapDXGVa3tM5w
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:24:45.576717
---

# 第四届“数信杯”数据安全个人赛WP

# 第四届“数信杯”数据安全个人赛WP

原创

Thanatos
Thanatos

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqkr05RiabYgq0o8R3lLIKKMStmM6Y47iaVkwTuMfw0XGvfsYwJgAqwLyOuD2MH23akI5diaTiaGShDSUDdYVIbwSW7FVzzIGUTPbE/640?wx_fmt=png&from=appmsg)

## 概述

本文是第四届“数信杯”数据安全大赛·数据安全个人赛（初赛）的解题记录合集，按题目类型编排，共收录16道题（均为上午“数据安全个人赛”题目）。每篇包含题目信息、分析过程、复现脚本与最终结论。

本文只做格式整理与合并，各题的解题过程、脚本、结论均保持原作者内容不变；涉及动态容器/靶机的题目Flag已脱敏，静态题目的Flag见各题结尾。

### 赛事信息

* 赛事：第四届“数信杯”数据安全大赛——数据安全个人赛（初赛·非学生组）
* 时间：2026年10月16日
* 主办：第四届“数信杯”数据安全大赛组委会
* 平台：`https://shuxinbei.clsadp.com:8000/#/event/3`
* 形式：个人赛
* 题目类型：签到、Web、AI安全、数据安全、工控安全、量子安全、无人机安全、Reverse、Misc

### 收录题目一览

| 类型 | 题目 | 分值 |
| --- | --- | --- |
| 签到 | minesweeper | 100 |
| Web | 某企业AI Meeting Minutes门户网站 | — |
| AI安全 | 审片室里的第二张脸 | 200 |
| 数据安全 | Linux Kernel Cow | — |
| 工控安全 | MMS | 200 |
| 工控安全 | 可曾听闻一键日卫星Q1 | 100 |
| 工控安全 | 可曾听闻一键日卫星Q2 | 300 |
| 工控安全 | 可曾听闻一键日卫星Q3 | 200 |
| 量子安全 | 量子门的多维身份 | 300 |
| 量子安全 | 量子幽灵的复数密码 | — |
| 无人机安全 | 天空在撒谎 | — |
| 无人机安全 | Domain 42 | — |
| Reverse | 八证词 | 200 |
| Reverse | 折叠端口 | 300 |
| Misc | 宏安全审计 | 100 |
| Misc | Vector Secrets | 200 |

## 签到

### minesweeper

#### 基本情况

题目类型misc(签到)，100分。没有附件，只给了一个HTTP服务地址，打开就是一个扫雷页面：80行80列、1200颗雷。题面是"今天天气很好，我们一起扫雷的喵"。

页面上右键会弹提示"没拿到flag之前，禁止插旗"，双击已翻开的数字可以自动推理展开安全格。页面加载了crypto.js和app.js两个脚本，所以这题的核心应该在前端逻辑里。

#### 前端分析（一个精心设计的幌子）

把两个脚本读一遍。

crypto.js里自己实现了一套密码学：

1、SHA-256（手写）

2、一个xorshift风格的PRNG，四字状态，返回值做了uint32截断

3、genSbox()：用PRNG对0..255做Fisher-Yates洗牌，得到一个S-box

4、decRound(rnd, cst)：一轮解密。先由密钥和轮号派生S-box的逆、一个位置置换、一段XOR密钥流，然后对密文依次做S-box逆代换、异或、逆置换

5、getKey()：把两个字节数组分别异或0xAA、0x55还原出字符串密钥，结果是Th3\_T4bl3\_K33p3r\_2026

6、getFakeCT()：把一串ASCII十六进制字符转成26字节密文

app.js里：每扫开一个安全格就调用一次decRound(ROUNDS-1-scr, cst)，其中ROUNDS = 80\*80-1200 = 5200。也就是扫完全部安全格，就跑满5200轮，最后用TextDecoder把cst解码显示出来。另外还挂了一个window.runClientDecrypt()，作用就是直接跑满5200轮。

看到这里，第一反应是把这套解密搬到Python跑一遍。把SHA-256换成hashlib，把PRNG、genSbox、decRound逐行翻译（注意JS里>>>0、<<的uint32/int32语义），跑5200轮后解码，得到：

FLAG{REDACTED}

假flag。注意密文那个函数名getFakeCT——fake ciphertext。作者把整条前端解密链路都做成了幌子，这条路上拿到的永远是假flag。

#### 关键突破

真正的提示藏在app.js末尾的注释里：

"每扫开一格，猫脸变换就逆推一轮。5200轮之后，真相自现。去看看flag.png。你每点一次，它就清晰一分。"

这句话点明了三件事：进度是记在服务器上的；服务器把进度"画"进了flag.png；进度越高，图片里的flag越清晰。前端那5200轮只是一个动画效果，真正的状态在服务端。

那就直接和服务器交互。探测到的接口：

1、GET /progress → {"step": 0, "rounds": 5200}，返回当前进度

2、POST /progress，body是{"step": N}，推进进度

3、POST /reset，重置进度

4、GET /flag.png，返回一张365x365的PNG

这里有个坑：POST /progress做了节流，一次最多只能推进100（服务端取min(请求值,当前值+100)，而且不回退）。所以想一步POST 5200是没用的，只能老老实实连续POST 52次，每次+100，把进度从0推到5200。

推到5200的那一次，服务端返回里多了两个字段：done和secret。secret是一句提示："猫脸变换已全部解开。真相不在代码里，在一张图中——你每扫开一格，它就清晰一分。现在去看看吧。"

这时候再GET /flag.png，图片从10620字节的噪声图变成了4920字节，中间一行清清楚楚写着真flag。

#### 利用/还原思路

整个还原过程可以完全脚本化：

1、先POST /reset重置（如果实例没有这个接口就跳过）

2、循环GET /progress，只要没到5200，就POST一个min(当前+100, 5200)，直到进度到顶

3、GET /flag.png保存下来

4、从图片里把那一行flag文字识别出来

第4步本可以交给OCR，但实测小字号下tesseract不稳定，直接读会读错好几个字符（例如把9读成8、把}读成{）。换个思路：这张图是服务端用Python画的，字体就是Pillow自带的默认字体ImageFont.load\_default()。验证方法很直接——用同一个字体把候选字符串渲染成位图，再和图片里那行文字做逐像素比对，结果完全一致（IoU = 1.0）。既然字体是确定且可复现的，就完全不需要外部OCR，直接用Pillow自带字体做模板匹配来解码：

1、先把图片里那一行文字裁出来。底部那条进度条是整行深色（行方向深色像素数接近满宽），按阈值排除掉；剩下在图片上半部分最密的一条横带，就是flag文字

2、用ImageFont.load\_default()把字符集flag{}0123456789abcdef里每个字符都渲染成小位图模板，同时记下每个字符的墨迹偏移和步进宽度

3、从左到右贪心匹配：在每个位置试所有候选字符，把它们按各自的墨迹偏移贴上去，统计在当前窗口内的像素差，取差值最小的字符，然后按这个字符的步进宽度把游标推进

4、贪心在首尾两个字符上偶尔会认错（比如首字符f和a、末字符}和{容易混），所以最后用已知的flag格式flag{...}重建外层：把花括号内部的内容抽出来、只保留十六进制字符，再套回flag{...}，和原图比对一次，只有更匹配才采用

这样，最终脚本只吃题目地址，不硬编码任何答案，一键就能跑出flag。

#### 脚本运行命令

Windows：python solve.py

WSL：python3 solve.py

脚本默认读取脚本同目录下的flag.png；脚本顶部TARGET填题目地址。若靶机已经下线，脚本会提示"live server unavailable"并直接对同目录已有的flag.png做解码。

#### 脚本

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# minesweeper（签到）：crypto.js 解出的是假 flag（getFakeCT）；真 flag 由服务端画进
# flag.png。主线：POST /progress 每次最多 +100 推到 5200 → 下载 flag.png →
# 用 Pillow 自带字体做模板匹配读字（免 OCR）。
# ...（省略：完整模板匹配与逐像素打分实现，见原始脚本）
import re, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFont

TARGET = ""            # <-- 题目地址
ROUNDS, STEP_CAP = 5200, 100
CHARSET = "flag{}0123456789abcdef"

def http(url, data=None):
    req = urllib.request.Request(url, method="POST"if data else"GET")
    if data:
        req.add_header("Content-Type", "application/json"); req.data = data.encode()
    return urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")

def drive_to_full():
    """服务端限速：一次最多 +100，只能连推 52 次。"""
    http(TARGET + "/reset", "")                       # 有些实例没有 /reset，忽略
    whileTrue:
        cur = int(re.search(r'"step"\s*:\s*(\d+)', http(TARGET + "/progress")).group(1))
        if cur >= ROUNDS:
            return
        http(TARGET + "/progress", '{"step":%d}' % min(cur + STEP_CAP, ROUNDS))

def find_text_bitmap(img):
    """排除底部整行深色的进度条，取上半部最密的一条横带作为 flag 文字行。"""
    # ...（省略：按行像素密度切横带、裁紧致位图的实现）
    return np.array(img.convert("L")) < 128

def decode(R, font):
    """从左到右贪心匹配：每位置取像素差最小的字符，按步进宽度推进游标。"""
    # ...（省略：模板构建、容形 IoU 打分、基线搜索与 flag{...} 外层重建）
    return"flag{...}", 1.0

def main():
    drive_to_full()
    open("flag.png", "wb").write(urllib.request.urlopen(TARGET + "/flag.png", timeout=15).read())
    text, iou = decode(find_text_bitmap(Image.open("flag.png")), ImageFont.load_default())
    print("[*] decoded (IoU=%.3f): %s" % (iou, text))
    print("[+] FLAG: %s" % re.search(r"flag\{[0-9a-fA-F]+\}", text).group(0))

if __name__ == "__main__":
    main()
```

#### 运行输出

```
[*] target: http://<题目地址>
[*] progress 100 -> {"ok": true, "step": 100}
[*] progress 200 -> {"ok": true, "step": 200}
...（中间省略，每次 +100）
[*] progress 5100 -> {"ok": true, "step": 5100}
[*] progress 5200 -> {"ok": true, "step": 5200, "done": true, "secret": "..."}
[*] saved flag.png (4920 bytes)
[*] text bitmap: 204x11
[*] decoded (IoU=1.000): flag{xxxxx}
[+] FLAG: flag{xxxxx}
```

## Web

### 某企业AI Meeting Minutes门户网站

> 目标：`http://x/`（前序实例`http://x/`在利用中途实例下线，逻辑完全相同）**最终FLAG：`flag{REDACTED}`**Flag位置：`/root/flag`（`-rw-r--r-- root root 39`），仅root可读。

---

#### 攻击链总览

```
 ① 侦察    SPA 落地页，JS 里发现 /index.php
 ② 源码泄露 index.php 自身源码藏在隐藏 <pre>；注释指向 phpinfo.html 泄露扩展/版本
 ③ 类实例化 ReflectionClass + newInstanceArgs
           SimpleXMLElement(dataIsURL=1) 当文件读取器 → config.php 的 $secret
           Imagick(...) 当图像/文件处理原语
 ④ 任意写   POST multipart 生成 /tmp/phpXXXXXX + Imagick("vid:msl:/tmp/php*")
           MSL 用 inline: 读 + gray: 写 → 灰度 PNG 像素即任意字节 → 落地 webshell
 ⑤ RCE      www-data（disable_functions / open_basedir 皆空），但 /root 为 drwx------ ⇒ 需提权
 ⑥ 提权点   x:6379 上以 root 运行的 redis-server（口令在 redis.conf）
 ⑦ root RCE 靶机自带 gcc，现场编译恶意 Redis 模块 → MODULE LOAD，OnLoad 以 root 执行
 ⑧ 取数     读 /root/flag
```

---

#### 目标信息

| 项 | 值 |
| --- | --- |
| 入口 | `http://x/` |
| 真实题目入口 | `/index.php` |
| 泄露页面 | `/phpinfo.html` |
| Web服务器 | Apache/2.4.65 (Debian) |
| Linux | Debian 12 (bookworm)，`x86_64`，Docker容器（`/.dockerenv`存在） |
| PHP模块 | Imagick(ImageMagick 6.9.11)、Phar、PDO、SQLite3、SimpleXML、SimpleXML等 |
| 关键配置 | `display_errors=On` ；`disable_functions`**空**；`open_basedir`**空** |
| 危险可用类 | `Imagick` 、`ImagickDraw`、`SimpleXMLElement`、`SQLite3`、`Phar`、`SplFileObject` |
| 内部服务 | `redis-server x:6379` （**以root运行**，Redis 7.0.15） |
| 目标侧工具链 | `gcc` 12.2 / `g++` / `make` / `python3` / `perl` / `curl` / `wget` / `openssl` |

---

#### 阶段一：侦察

##### 站点是SPA，翻JS找「异物」

```
curl -s -i "http://x/" | head -40
curl -s "http://x/assets/index-D2J4gXat.js" -o index.js
grep -aoiE '"[^"]*\.php"' index.js | sort -u
```

整个bundle是React内部代码+一个AI Meeting Minutes落地页文案， 唯一有用的字符串是\*\*`index.php`\*\*。

##### 目录/敏感文件探测

```
for p in robots.txt .git/HEAD .env flag flag.txt index.js.map admin backup \
         phpinfo.php phpinfo.html info.php config.php config.php.bak; do
  printf "%-20s %s\n" "$p" "$(curl -s -o /dev/null -w '%{http_code} %{size_download}' \
      --max-time 15 "http://x/$p")"
done
```

命中：`phpinfo.html` → **200 / 207297**（环境信息全泄露）。

```
curl -s "http://x/phpinfo.html" -o phpinfo.html
# 从 phpinfo 中提取：
#   - Architecture: x86_64
#   - ImageMagick ve...