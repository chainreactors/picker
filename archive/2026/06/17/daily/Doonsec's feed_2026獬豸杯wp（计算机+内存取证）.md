---
title: 2026獬豸杯wp（计算机+内存取证）
url: https://mp.weixin.qq.com/s/bI53CgWqBqbOtY6qMxOs2Q
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:39.896042
---

# 2026獬豸杯wp（计算机+内存取证）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T5C6icTcSx9MrlfBDQYnbIXUDI2uXMHOTe9rItkYQfHzvaCpXNlG1l2xMWBmQf8Eyk43f0gTZyNpgcb7OofnbLDDVTIYAguzIgpGByBIStOs/0?wx_fmt=jpeg)

# 2026獬豸杯wp（计算机+内存取证）

原创

Serendipity
Serendipity

Serendipity的小屋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

检材密码：`EVJbYf&+eStnx5B+C^bj%YPSr)gr`

---

`首先感谢Joy佬（计算机）和玫幽倩大佬（内存）提供的思路![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_93@2x.png)`

## 计算机取证

### 1.请分析检材2：密码连续错误输入多少次数后，系统会自动锁定用户账户？

### 【答案格式：1】

**3**

直接win+R输入cmd，然后输入net accounts即可

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NwD8OjIQ1kZttEDToxGqFBSpP51WuMZ0mlunlXr8Ra9ey0WHsno2LROial4vWficW7dZQd6fiboOuCl7YfBr8CtPFe08MHg2RuH4/640?wx_fmt=png&from=appmsg "null")

或者是win+R输入gpedit.msc，查看账户策略

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MN2uwv6Xk61Ev55zkSiaricumWib7T6Jvz87goBfpbe10wnCyUSdRCgf8shj5maJ0aUpOXoXsnhSa1MvAEFoS7Y46dSia1AQkWnu8/640?wx_fmt=png&from=appmsg "null")

### 2.请分析检材2：检材中对应的微信 wxid 是多少？

### 【答案格式：wxid\_1a2b3c4d5e6f】

**wxid\_q1w2e3r4t5y6u7i8o9**

在文档中看到了微信数据文件

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9M7Ll5dZQQBqm5YyXgJTgtAtib6ibxUNOoyFLA2ibbMEpFgQSZWDHus0k9v05e8Sm98fGXRKPTwbRuH36O6JJ5Jiamd44mNTd2JdZU/640?wx_fmt=png&from=appmsg "null")

### 3.请分析检材2：E盘 BitLocker 恢复密钥末尾六位是多少？

### 【答案格式：616912】

**126269**

在微信数据目录下看到两张带二维码的图片

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MlPBLoTyzMd5BzQuf3dXznlyFJvkGa7CQS8zia8L9vLGQNEwJ4AHhTe8s5yH4GQBjwDIHty9vqfeRQej0icpxfxSEwdfctwpUhA/640?wx_fmt=png&from=appmsg "null")

扫描一下二维码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MhDuKz7b7uWTKTPibAbpIRvSwQIFVZm4Z2jy036LBOibsWzibVJCO60GTo1BfdeicOZ6NdKpJsf2icmazS4Mj8jGvqOKxvUGGAso0I/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Ofhyq0UClXDojrQWSo2zpJQhr55KNL52Mn1133WG50QZ15ljaYAEsTYhPVHkq69gicd8hRNaOGckTtSnu7NQbDtZZrEblbIJeU/640?wx_fmt=png&from=appmsg "null")

用第一张图片的密钥成功解开

### 4.请分析检材2：VC加密容器的外层加密卷密码是什么？

### 【答案格式：根据实际值填写】

**JHTJ！@#￥A313**

在D盘可以看到一个名称为1的1G文件，大概率就是VC容器了

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9Ot3Fm0r9tTEn1PxicXjZibCQzm3CibD9qnDxL35eBtVfsexfkca4edOe5LBInNvXDasyibj3RnbX3c9R269UvzqOHsZh4h7fDG99E/640?wx_fmt=png&from=appmsg "null")

同时该目录下有个1.png的图片，用记事本打开可以看到外层密码

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OCdqm9HoeCxOFYcmesUybhNQdRsYcnibAwcMtHs7aZAiag010lCYRjaduTXb1MiaiacxjA9wYj8j7AhslFe7jfnQicRZzbaYicOmRj0/640?wx_fmt=png&from=appmsg "null")

### 5.请分析检材2：带有“豆包AI生成”水印的图片一共有多少张？

### 【答案格式：1】

**6**

在图片这里看到了四张

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9PT4pQkBXA4cNu4GrMzeekicyZn8J0uuz38AC5PfybfjP3R6wqHFWGAMibicvngdxnDib0NsEDQQSVic9vRtcBQdeyibgYS0AibzNFKo4/640?wx_fmt=png&from=appmsg "null")

然后bitlocker密钥那里刚刚也有两张

### 6.请分析检材2：VC加密容器的隐藏加密卷密码是什么？

### 【答案格式：根据实际值填写】

**ClearSky@SecretSignal#SevenMileJasmine**

对上述豆包生成的四张图片进行分析，发现3.png中存在一张二维码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OPwueNKnjWa124qzxG4BUj13B41MBgnU7KfL9jUTicPfqicMEq8pomh8phvOtCEcribfjQPcJbyN2ynrJ7FZoHqXpeGmqm5FNL4A/640?wx_fmt=png&from=appmsg "null")

得到隐藏加密卷密码`ClearSky@SecretSignal#SevenMileJasmine`

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MVPX8wIsA9lRumQ6iaWazONVdYbOPsHwjpicgchNJYKwP1AEmby9ia6LicmkmxCQJVxGuZibcz0xmxdPAX3h1ED2gvnvsMicg9S4XtU/640?wx_fmt=png&from=appmsg "null")

### 7.请分析检材2：接上题，嫌疑人的接头暗号是什么？

### 【答案格式：根据实际值填写】

**步行九千米**

用隐藏卷密码挂载VC容器发现密码错误

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OSibUnafN9Eq7WcdMyzzN1ry4QL2UbJrz3yhGOmcibwjhtZ6mBhKFTxr6JlpONdOftAnib85l4N3DxDJIURaafdEl0eEoSXJeiauI/640?wx_fmt=png&from=appmsg "null")

看了joy的wp后发现，原来还需要桌面上的密钥文件。。。

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9P6hgdGH09f3fz7gOLTEQQ49qcbjicGdCTSlYJ1L6yojLfiavLzZZkVsTKOcFWbaam3k6UCtZVT3Iz8RcvV15HNzsKoBpo5QTJPE/640?wx_fmt=png&from=appmsg "null")

挂载后看到几个音频文件，应该是音频引写

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MWIYXkD72ZS5vGNad87GFh8Y0AhChgPKabibibnfIUkdVbSmHr2sT1ib1gRRVycmrBl9BONXe82Hdf7D8GNCDvhU4d75t06QibiagM/640?wx_fmt=png&from=appmsg "null")

用Audacity打开Secret Signal看一下频谱图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9P9iamFBlV4wfUNoSGsh3cxq5wjNDb7BoCghqFaUEb6Txcv9706hO069JvD3S1qDTnCPEHYI6mlTz6IwLFibJzY3X05vEjia78sNw/640?wx_fmt=png&from=appmsg "null")

### 8.请分析检材2：接上题，嫌疑人的接头地点在哪里？

### 【答案格式：天津117大厦201室】

**Taipei 101 building 502 room**

对这四张二进制图片文件进行分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9MFK3iaqWfeFu0ydX2ze0p0dhJ1cNuIHddiaiak9nEew91fMAFxeG7SY5LFQIEbYhnffn4FUGvJLQMMN1BiaQpbH3qHdNK6IGkzhI8/640?wx_fmt=png&from=appmsg "null")

```
import sys, iosys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import easyocr, cv2, numpy as npfrom itertools import permutations
XOR_KEY = 0xDAIMAGES = ['5.png', '6.png', '7.png', '8.png']
def extract(img_path, reader):    img = cv2.imread(img_path)    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 多种预处理    sources = [('orig', img)]    for t in [127, 150, 180]:        _, b = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)        sources.append((f't{t}', b))    sources.append(('inv', 255 - img))    # 提取所有8位二进制字符串    raw = []    for name, src in sources:        for bbox, text, conf in reader.readtext(src):            text = text.strip()            if all(c in '01' for c in text) and len(text) == 8:                pts = np.array(bbox, dtype=np.float64)                cy = pts[:, 1].mean()                raw.append((cy, text, conf))    # 按Y排序    raw.sort(key=lambda x: x[0])    # 聚类：Y坐标差<30的归为一组    groups = []    for cy, text, conf in raw:        placed = False        for g in groups:            if abs(cy - g[0][0]) < 30:                g.append((cy, text, conf))                placed = True                break        if not placed:            groups.append([(cy, text, conf)])    # 每组取置信度最高的文本    result = []    for g in groups:        best = max(g, key=lambda x: x[2])        result.append(best[1])    return result
def decode(bins):    return ''.join(chr(int(b,2)^XOR_KEY) if 32<=int(b,2)^XOR_KEY<127 else '?' for b in bins)
def main():    print("初始化OCR...")    reader = easyocr.Reader(['en'], gpu=False)    all_bins = []    for f in IMAGES:        bins = extract(f, reader)        print(f"{f}: {bins}")        all_bins.extend(bins)    # 暴力排列前7个，找最可读的结果    first7, rest = all_bins[:7], all_bins[7:]    best, best_msg = all_bins, decode(all_bins)    best_score = sum(c.isalpha() or c==' ' or c.isdigit() for c in best_msg)    for p in permutations(first7):        msg = decode(list(p) + rest)        score = sum(c.isalpha() or c==' ' or c.isdigit() for c in msg)        if score > best_score:            best, best_msg, best_score = list(p)+rest, msg, score    print(f"\n解码结果: {best_msg}")
if __name__ == '__main__':    main()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NBAGX2kRl1e0BA6xiarzgzxY2bszlzFOib4oFSu9hotbU6hU97ZtCEvUjnNYGrrpvUVypgYJsV1NeLutzW6xqbDtSX9KvhIasH0/640?wx_fmt=png&from=appmsg "null")

### 9.请分析检材2：木马残留样本中，核心信息窃取配置数量为多少？

### 【答案格式：1】

**5**

在E盘看到一个.c文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NadticTlJMEJLSutU4STNEgQGC1pCCib18icZiaqP1p19KPZicQoVEVPxwqriaGw1a4EpzHJyq6ZvOGKPElCXJqAAVWQq876SINBCws/640?wx_fmt=png&from=appmsg "null")

导出分析代码，识别出以下5类信息窃取功能

| 序号 | 窃取类型 | 配置标识 | 代码位置 |
| --- | --- | --- | --- |
| 1 | 键盘记录器 | `g_KEYLOG_PATH` ("keylog.dat") | 第43行 |
| 2 | 浏览器凭据 | `g_BROWSER_DB` ("Login Data") | 第58行 |
| 3 | Cookie窃取 | `g_COOKIE_DB` ("Cookies") | 第59行 |
| 4 | 屏幕截图 | `g_SCREENSHOT_DIR` | 第49行 |
| 5 | 进程注入窃取 | `SimulateProcessInjection()` | 第171-238行 |

### 10.请分析检材2：木马残留样本中，申请的内存保护标志是什么？

### 【答案格式：PAGE\_READWRITE (0x04)】

**PAGE\_EXECUTE\_READWRITE (0x40)**

主要的木马核心功能使用的是 PAGE\_EXECUTE\_READWRITE (0x40)

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NBab1m8GMjxvCp1ur6MamPcEe3Ub8IF3nY16M5wlM0Zn1SlticvqzPMibQxRTfW9cXoiaibdoBPBOktibagibxK0ibvxJvDYcdWLpdZE/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NNEYLFRFUHvyPDEvNXGEW0EvHD72VxVicLFJDdgDiax3dAT8NoDNnoMibpmKUBoJO2iaYnrKOkGc7rhFKv87qSJ0iaL3abGT454ef4/640?wx_fmt=png&from=appmsg "null")

### 11.请分析检材2：嫌疑人涉案交易使用的银行卡号是什么？

### 【答案格式：纯...