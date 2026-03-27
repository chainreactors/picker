---
title: 2026数字中国创新大赛数字安全赛道暨三明市第六届\"红明谷”杯大赛WP
url: https://mp.weixin.qq.com/s/vb1VXXni3HPy8Dv2Hw2n3w
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:31:07.653931
---

# 2026数字中国创新大赛数字安全赛道暨三明市第六届\"红明谷”杯大赛WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQoCkSfKHTib7rok6DKu8ISjwYs0G9PkpQIMk3KUhYDsSjfXaOOIq1MLhcedDBK1hjavZNJjk9nl93U8AjNGSAmEOIJvpzJQ3o1w/0?wx_fmt=jpeg)

# 2026数字中国创新大赛数字安全赛道暨三明市第六届"红明谷”杯大赛WP

原创

佚名
佚名

星宇Sec

![]()

在小说阅读器中沉浸阅读

比赛概述

主办单位：数字中国建设峰会组委会

承办单位：福建省数据管理局三明市人民政府

协办单位：三明市发展和改革委员会(数据管理局)

支持单位：数字中国研究院(福建)上海数据研究院有限公司

比赛日程

2026年3月26日 10:00-15:00 CTF实操答题

2026年3月26日 10:00-15:00 提交解题思路

共计13道赛题，其中包含6道Misc，1道Crypto，1道Reverse，2道PWB，3道Web。本次大赛要求所有参赛选手对比赛所使用的电脑进行屏幕录制

Misc

Stream-Capture

题目内容：

在一次针对内网异常行为的流量审计中，安全团队截获了一段来自未知主机的加密数据流，请尝试找到其中隐藏的信息。

先看协议统计与 UDP 会话：

```
tshark -r capture.pcapng -q -z io,phstshark -r capture.pcapng -q -z conv,udp
```

可见主要 UDP 会话为：

```
192.168.31.192:33314 <-> 192.168.31.191:47998
```

约11MB，主数据流，这基本就是题目提示的关键流

抽取该流前几包十六进制可看到：

* UDP payload常见长度约1408 bytes
* payload前部存在固定格式头
* 在头后可见H.264起始码 00 00 00 01

继续做字段观察后发现：

* bytes[2:4]（大端）可作为包序号（从 0 递增）
* 末尾有少量重复序号（重传/乱序）
* 去重后序号范围约0~7960（共7961包）

因此重组策略为：

1. 仅取 udp.srcport == 47998 的包
2. 取 payload
3. 用 bytes[2:4]作为排序键
4. 重复序号保留首个
5. 剥离头部（本题cut=32最稳定）
6. 顺序拼接为裸H264流。

自动化重组脚本：

```
import subprocessimport osimport cv2import mathimport numpy as npfrom collections import OrderedDictPCAP = "capture.pcapng"OUT_H264 = "stream_cut32.h264"HEADER_CUT = 32def export_packets():    cmd = [        "tshark", "-r", PCAP,        "-T", "fields",        "-E", "separator=\t",        "-E", "occurrence=f",        "-e", "udp.srcport",        "-e", "data",    ]    out = subprocess.check_output(cmd, text=True, encoding="utf-8", errors="ignore")    packets = []    for line in out.splitlines():        parts = line.split("\t")        if len(parts) < 2:            continue        sport, data = (parts + ["", ""])[:2]        if sport != "47998" or not data:            continue        raw = bytes.fromhex(data)        if len(raw) <= HEADER_CUT:            continue        seq = int.from_bytes(raw[2:4], "big")        packets.append((seq, raw))    return packetsdef rebuild_h264(packets):    seen = OrderedDict()    for seq, raw in packets:        if seq not in seen:            seen[seq] = raw    ordered = [seen[k] for k in sorted(seen.keys())]    with open(OUT_H264, "wb") as f:        for raw in ordered:            f.write(raw[HEADER_CUT:])    return len(ordered)def dump_contact_sheet(video_path, out_jpg="contact_sheet.jpg", step=20):    cap = cv2.VideoCapture(video_path)    frames = []    idx = 0    while True:        ok, frame = cap.read()        if not ok:            break        if idx % step == 0:            thumb = cv2.resize(frame, (480, 270))            cv2.putText(                thumb, str(idx), (10, 28),                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA            )            frames.append(thumb)        idx += 1    cap.release()    if not frames:        return 0    cols = 5    rows = math.ceil(len(frames) / cols)    canvas = np.zeros((rows * 270, cols * 480, 3), dtype=np.uint8)    for i, fr in enumerate(frames):        r, c = divmod(i, cols)        canvas[r*270:(r+1)*270, c*480:(c+1)*480] = fr    cv2.imwrite(out_jpg, canvas)    return idxdef save_key_frame(video_path, frame_id=300, out_png="frame300.png"):    cap = cv2.VideoCapture(video_path)    idx = 0    saved = False    while True:        ok, frame = cap.read()        if not ok:            break        if idx == frame_id:            cv2.imwrite(out_png, frame)            saved = True            break        idx += 1    cap.release()    return savedif __name__ == "__main__":    packets = export_packets()    unique_count = rebuild_h264(packets)    total_frames = dump_contact_sheet(OUT_H264, "contact_cut32.jpg", step=20)    hit = save_key_frame(OUT_H264, frame_id=300, out_png="f300.png")    print(f"raw packets: {len(packets)}")    print(f"unique seq packets: {unique_count}")    print(f"decoded frames: {total_frames}")    print(f"key frame saved: {hit}")
```

在解码后视频的约第300帧左上角可见明文：

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQrDaTyWnjIkHcVCwcibFJNOLo6TwYz8526l7FNRbNmS4vpNef24zXncneyXu53NS1DiaNrM95wKVghnf8CicXkZAnwhs7OMEGEibC4/640?wx_fmt=png&from=appmsg)

Model-Entropy

题目内容：

这是一个看似常规的开源情感分析模型，其核心逻辑与加载过程均能通过初步的安全性审查。然而，审计人员在评估其权重分布时发现，本应承载海量语义特征的Embedding层在参数规模上存在显著的异常缩减。请针对该模型文件剖析其内部存在的隐蔽信息。

题目目录如下：

* sentiment\_analysis.ipynb
* sentiment\_model.npz

本题的关键不是去跑模型做分类，而是去判断模型是否真的是一个正常可用的模型

排查顺序如下：

1. 确认权重格式
2. 阅读 notebook，核对模型结构和加载逻辑
3. 直接检查npz内部数组名、形状、数值范围
4. 验证模型是否真的具备 notebook 中描述的效果
5. 对异常层的底层二进制表示做隐写提取
6. 还原密文并继续解码，得到最终flag

打开sentiment\_analysis.ipynb后，可以看到模型并不是真正的 NLP Embedding 模型，而是一个非常简单的两层 MLP：

```
def forward(X, p):    h = relu(X @ p['embedding_layer'] + p['hidden_bias'])    return softmax(h @ p['output_layer'] + p['output_bias'])
```

模型结构是：

```
Input(18) -> Dense(20, ReLU) -> Dense(2, Softmax)
```

也就是说，所谓的embedding\_layer其实只是一个18x20的全连接权重矩阵，并不是真正意义上的词向量 Embedding

直接读取模型参数：

```
import numpy as npwith np.load("sentiment_model.npz") as data:    for k in data.files:        arr = data[k]        print(k, arr.shape, arr.dtype)
```

输出为：

```
embedding_layer (18, 20) float32hidden_bias (20,) float32output_layer (20, 2) float32output_bias (2,) float32
```

这里最异常的地方是：

embedding\_layer只有18 x 20 = 360个float32

对于题目描述中的“应承载海量语义特征的 Embedding 层”来说，这个规模小得不正常

这说明：模型描述存在伪装或者这一层很可能被拿来充当隐写载体

题目 notebook 声称模型在合成数据上能达到约92%准确率，但按原 notebook 的逻辑重新跑一遍后，实际准确率只有0.49125

换句话说，sentiment\_model.npz的主要用途不是推理，而是藏信息

因为 npz 容器本身结构正常，没有额外文件、注释、尾部垃圾数据，所以隐藏信息大概率埋在浮点参数本身的二进制位里。

对于 float32，最自然的隐写方式就是：

* 取最低有效位 LSB
* 取若干低位拼接成字节流

而embedding\_layer 一共有360个float32，如果每个数取1个最低位，那么总共就是：360 bit = 45 byte

提取脚本如下：

```
import numpy as nparr = np.load("sentiment_model.npz")["embedding_layer"]u = arr.view(np.uint32).ravel()bits = [(x & 1) for x in u]ct = bytes(    sum(bits[i + j] << j for j in range(8))    for i in range(0, len(bits) // 8 * 8, 8))print(ct)print(ct.rstrip(b"\x00"))
```

得到的 45 字节内容去掉结尾零填充后为：

```
!$.4/~*-faqv~7&q{~`uyx~mtq|~a!)fav{7b"5
```

由于flag以”flag{“开头，可以利用已知明文攻击

```
ct = b'!$.4/~*-fa\x7fqv~7&q{~`uyx~mtq|~a!\x7f)fav\x7f{7b\"5'pt = b'flag{'key = bytes([ct[i] ^ pt[i] for i in range(len(pt))])print(key)
```

得到密钥：GHOST

可以看出这是一个长度为5的循环异或密钥

完整解密脚本如下：

```
import numpy as nparr = np.load("sentiment_model.npz")["embedding_layer"]u = arr.view(np.uint32).ravel()bits = [(x & 1) for x in u]ct = bytes(    sum(bits[i + j] << j for j in range(8))    for i in range(0, len(bits) // 8 * 8, 8)).rstrip(b"\x00")key = b"GHOST"pt = bytes(c ^ key[i % len(key)] for i, c in enumerate(ct))print("cipher =", ct)print("key    =", key)print("plain  =", pt.decode())
```

输出：

```
cipher = b'!$.4/~*-fa\x7fqv~7&q{~`uyx~mtq|~a!\x7f)fav\x7f{7b"5'key    = b'GHOST'plain  = flag{XXXXXXXXXXXXXXXXXXXXX}
```

DataVault\_V3

题目内容：

欢迎来到 DataVault V3 —— 采用高级信封加密的下一代企业云端数据保险箱。我们吸取了历史教训，在最新的V3企业版中引入了Apache网关反向代理，并升级了基于Python的高级URL白名单过滤机制。旧版本系统已被标记为‘安全销毁’。然而，传闻中那把本该随数据一同消亡的‘幽灵密钥’，似乎仍潜伏在底层内网的某个角落。你能穿透重重防御，让幽灵密钥现身，并取回被封印的数据吗？

本题的攻击链由四个核心环节组成，涉及 Web 漏洞利用与密码学攻击的结合：

1. Apache 路径穿越 (CVE-2021-41773)：利用配置不当的 Apache 代理读取系统文件与配置文件
2. 隐藏接口发现：通过信息收集获取包含加密数据的快照
3. SSRF绕过与内网探测：利用十进制 IP 绕过 Python URL 白名单，访问内网 KMS 服务
4. 密码学攻击 (CTR密钥流重用)：利用KMS固定的 CTR 密钥流，通过选择明文攻击（全零DEK）获取Keystream，进而异或恢复原始密钥并解密 AES-GCM 数据。

路径穿越与信息收集

访问目标服务 http://xx.xx.xx.xx:1234/，页面提示使用了 Apache 防火墙和 Python 过滤机制。由于题目明确提到 Apache 网关，且版本可能存在已知漏洞，我们首先尝试 Apache 2.4.49 的经典路径穿越漏洞（CVE-2021-41773）

通过构造特殊的 URL 路径 /assets/.%2e/.%2e/.%2e/.%2e/，我们成功读取了 /etc/passwd 文件

随后，我们利用该漏洞读取了Apache的配置文件 /usr/local/apache2/conf/httpd.conf，发现了关键的反向代理配置：

```
Alias /assets/ "/usr/local/apache2/htdocs/"ProxyPass /assets/ !ProxyPass / http://127.0.0.1:8080/
```

这表明所有非/assets/的请求都被代理到了本地的8080端口，即后端的 Python 应用。

获取加密快照

在对后端 Python 应用的路由进行探测时，我们发现了一个隐藏的 API 接口/api/v1/backup/snapshot。访问该接口，我们获取到了被封印的数据快照：

```
curl -s http://xx.xx.xx.xx:1234/api/v1/backup/snapshot
```

返回的 JSON 数据如下：

|  |  |  |
| --- | --- | --- |
| 字段 | 值 | 说明 |
| enc\_data | 7e172f82011d7f238e544f16d160fccbdc4c2f39026cac98c1ea38337d2bbbbfd99b14e1fbcc0f7e97b7 | AES-GCM 加密后的数据 |
| enc\_dek | a41b57d6ca0ee2f72e2ce59cc7226f42558a0d7eec2b7ef9c9da9a83...