---
title: 青少年CTF S1·2026 公益赛wp
url: https://mp.weixin.qq.com/s/1LH6NxzsOaGpzQtkGXu30w
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:25:47.745629
---

# 青少年CTF S1·2026 公益赛wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dribnicsKeGgfcW8w3TlXu2764M7ibGosKlEYQSKgmM1RmSpMShHOvgGErdpcibjUN7ty6kWt9GzeKowey3KKySF8A5zRECZkaHrBlSMAxPtJ0U/0?wx_fmt=jpeg)

# 青少年CTF S1·2026 公益赛wp

叁玖owo
叁玖owo

小叶Sec

![]()

在小说阅读器中沉浸阅读

以下文章均来自叁玖大佬，叁玖owo，如有宝子想问的可以关注叁玖owo进行询问

# 前言

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgdEHC30NksaOqGTrwNibReNHeZdDlATLoPO04P3DtIApeVpNH8mgCxrDTRSHImJKEicvZvHVDkBeY13JuDe8ulsD4Ial3hOUt6zA/640?wx_fmt=png&from=appmsg)

比赛时间非常得长，有些题目上线了，中间也下了一些题目，但是后面好像就没有上新题目了。

队伍名字:flag  排名：15

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfyRR2b9ic5KUGfb5qGVwUltUvlVPz25dkGNPI5cYQ6siaQnHkBrr1PuJxMualicYyxCIm7IPtLfaVnGKIYK3EwSH101vERgJG3cU/640?wx_fmt=png&from=appmsg)

解题情况全解

# Misc

## 玫坏的压缩包

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgdoMKia7NY2wZLkTnzWZWxibORwopg9QdWpAkmxMWqkHJYjk3iatX49s1pY4uHvkJxPSiccutTCsmMMUU5WiaPXiaVuP6BPiajXcAgU2w/640?wx_fmt=png&from=appmsg)

压缩包是损坏的

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgdNicdjJEuDWTsiaI42LY2AYPmtW91NNRLmEFAJz8B2zb7OJNZY00b55VVUUwHkLd6WV8HMQfecwIzicjTAAXcnFtKMRKdqLHgdfA/640?wx_fmt=png&from=appmsg)

没有文件头，可以看到里面有word 补一下文件头就行

但是可以不用补直接binwalk就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgdg1PJckLukzLdc36QjNI7sBPbj0ncgQO1ywCYkkyf5xlyX61IM0NCjnXpNmA8J5dtRM2rZdtibd3QNedpURoCcL6TBnKib7dXwA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfkwh6a9aljnCmhXMyGycz5spPlMTIh0ePg1uDUQgJ31KFImhLwY4H3APHgYL3JphzmKvPEdFsTTJNw9AvRBln3UFrwHibyjsf4/640?wx_fmt=png&from=appmsg)

查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcicNJATlfZiceib4xapXPKYIJ8gF9HPN9B7KWfTVsWxHLvlGkxHBN6iaXUnvGP1ClibXxJ8kQJdoHdRpRfibvBksVtab9gtxn1JbS38/640?wx_fmt=png&from=appmsg)

document.xml

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgdAtS07J5v1LoHY9AJcsQDib6wxsTLdVd3khcxBpI4icJp1F0pHf82iamic8bcRJ7IOC8w3phe8s4PLYibuklWnzIH700DSSxNKss2o/640?wx_fmt=png&from=appmsg)

```
flag{w3_w111_411_60_fur7h3r_4nd_fur7h3r}
```

## Ollama Prompt Injection

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgc3iascawV3qT9YWsI4fwCAsa3JU4JXfKrRia2HhicjwgqJATiav8feOiaoh6pJScrPyLric1r7Nxha1OMyObGUZpSJTqtgochO8svKw/640?wx_fmt=png&from=appmsg)

看名字应该就是一个AI题目 nc无法连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgfb6icdjlhaL90icOD2yZEicxf0gkzoLV5UhAk76IemibquW0Rts53PnfVZ4q3eS09p4DTC9akQmwLe1ABDAic3vIBgZBodwRm2eE30/640?wx_fmt=png&from=appmsg)

通常 Ollama 的 API 默认监听在 11434 端口，这里被映射到了 55859

**获取模型列表**：使用 `/api/tags` 接口查看服务器上安装的模型。

```
http://challenge.qsnctf.com:55872/api/tags
或者 curl http://challenge.qsnctf.com:55872/api/tags
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeo0g8dG6ndNOpicrJTJe1HicQwdWJwbq6AohIulv7HibqDk8kwkGxw6GmZVXAqgSZaXYeicyMBKr5wWjgJ7KFZciakqNkh9U0iaBe80/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgdvsoFyorXUvzdB6QCS0jmavrrHibTt9mlcFtlBAu1QpsfuS5k4eFiaUMyg066cnemDzlkcusP0RdcyIQNAxdENOdlsbPzlRIeO0/640?wx_fmt=png&from=appmsg)

发现自定义模型：`ctf-model:latest`

**提取系统提示词**：使用 `/api/show` 接口导出该模型的详细配置，可能flag 作为系统预设指令藏在其中。

```
curl http://challenge.qsnctf.com:55872/api/show -d '{"name": "ctf-model:latest"}'
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeQkpVFBBhAEQBcBNAnnzzsfARyKqodZTxiasI93bxkEBJr2kFScjCnUDr0lMaznlXLtoNg0WoQu03BqfoC9icEia3pbPvzxYA6WM/640?wx_fmt=png&from=appmsg)

或者使用 HackBar 插件

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgc6MUgn0nqwUSwsIDCKSAfvmtP4KWCLicmCCiawLsrxaQoL7mXbuFg5H2gGLUXO0xvH6icmpDGFyMiaYUTianazj0jDH191tH3WLxwk/640?wx_fmt=png&from=appmsg)

```
qsnctf{de7199c3085c47028de9cbae460dd2c7}
```

## 哦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgctv36ua8JlyELCzWMXewfoRWnKz8CQrhEOHJYjckueIqjTxgEeKDd1G5opWoYaJsT7vRGyicBxgiaGC7RtWaOs1vLAqJslhugCs/640?wx_fmt=png&from=appmsg)

一个哦010查看内容

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfNYEQ9XdKAILdn0J5xktVFJLhgy0hibd2xJ4Xayknic9ZUQAicCYnv3XPCX48ILUJaxlbumBGgn7KKCSTmFwNQ30Xn7EVjicnC8mg/640?wx_fmt=png&from=appmsg)

可以发现pk头但是被反转了 按照8字节反转回来

py3脚本

```
import struct

def solve():
    input_file = "哦"
    output_file = "flag.zip"

    try:
        with open(input_file, 'rb') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"找不到文件: {input_file}，请确认文件名或路径。")
        return

    recovered_data = bytearray()

    # 全文按8字节块反转的
    chunk_size = 8

    for i in range(0, len(content), chunk_size):
        chunk = content[i : i + chunk_size]
        recovered_data.extend(chunk[::-1])

    with open(output_file, 'wb') as f:
        f.write(recovered_data)

    print(f"处理完成！已生成文件: {output_file}")
    print(" flag.zip 。")

if __name__ == '__main__':
    solve()
```

有加密

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfd32dib1GnB0dOkjpeOONAKcDe8BokVkeWoZzUYwTia3QibPAg3ibibzXbQakGRj5dxicNziaCFbs82Oj5WtBP1s7VUVExSFbqMKFicx8/640?wx_fmt=png&from=appmsg)

不是伪加密，爆破无解，只能已知明文进行爆破了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgdSYM8XgQRmw5C69BywnXpfbYZMtMTVEU87PmOYoENFRGXFlLYDBH4iaqdl5sbqby1mrZic55ZY8UvHiaqnuxISqjnSzcWRqW4Jh0/640?wx_fmt=png&from=appmsg)

```
bkcrack.exe -C flag.zip -c a.png -x 0 89504E470D0A1A0A0000000D49484452
```

```
d590788c b34e73fb 40e733d1
```

有key了直接解压

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcwGyvXkbbWxQAiaib0DrGPvTvA7l87gHrRKnIEBtsaAVFraC97tWwYl9fFVRyrt8JnwOHrEoPriat4DhNNichOk3y8I6H1F4M0OZQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/dribnicsKeGgf13n5VOicvlLruxtbvmNl0GsnajAnYsY36u5pXicG0MuZj2MXPRUEBI4GK73YiaNyG2tjOIPNWhcrRia4TNwxC8BgMwXpiaibicJo0A4/640?wx_fmt=jpeg&from=appmsg)

图片进行foremost可以得到两张图片进行双图盲水印

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgfMibnD4Exzpib71BVTWJcxJvAibEpn4sPVibBHbk6pOVic1KRXpGJoZ2iaYKNhYpncVibrQEyWZajvQxw8Ak8pWZ3I0rMu1s0pv3bVrM/640?wx_fmt=png&from=appmsg)

```
python bwmforpy3.py decode 2.png 1.png 3.png
```

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgfmw1KWtuRHdfBz4taAxzu0akdtKjWo3bBFR7jnyGgrFKKxRlM3ECa7m3ias39bwOz4NDqmCf4gE1ZnLBNGwGpeCSEEpicKND0ok/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgd91NxwSL0yicFszrkMBa51DnEWKpAWiaXp1icyrhI9hgxzxh6Ua2WXf4oSnVapSQVichiae1OMej60aTLkjNKPZE5DFHUgTbxibe1gc/640?wx_fmt=png&from=appmsg)

```
flag{01d38cf8-e6f9-11f0-8fcd-11155d4a}
```

## qr

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgczrjskaDxNlUKFaJdeFXYzRJcwfW4AmmVOLJZVE8ricibHUHUzepmZpth2YSNZlBmyWXIZLCuHO0ozBNhmc1c8PkUkpYuADtsl0/640?wx_fmt=png&from=appmsg)

缩小就行

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeTtneWKqD7gUvibrGGOuryE8r4vsaT6mticzrLG9FKSicFhkT9w8icboLg2VB7xa011Wk2eJBc4zUq3oHzF3ugGn1kze8HjWMeGS8/640?wx_fmt=png&from=appmsg)

手机扫码或者改变颜色电脑可以扫码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGge9FdcjzZTC3lg8KRKRu4Xb3Jsa8EzU8LAKIyra6gYu7miayH5M3Bj6M8x5u8XSG08OqoEib2picNyY25x8aKQb8ssqTBHA10I99M/640?wx_fmt=png&from=appmsg)

```
flag{56876aae7cb7b98a3756bac05c6b6675}
```

## QSNCTF

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcAzAFG2AIOSOvXtLLd7J6myTU7weYGBMseaU6QbPm4LFTicXcnxEFicicctAL48DHqHzBURLeJIavX3IM4MyJR2sxdU2aTbomBE8/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgcia5iceQkoBqibdCPicXWAsDT67hAOU8t8pjiaoAxsmIibsVwyqPQRz58BWpcicdDT1WcaQ7xmJcJ08jiaMGxjIYIESR5BtN1tOmbiaicqs/640?wx_fmt=png&from=appmsg)

## 灵异事件

![](https://mmbiz.qpic.cn/mmbiz_png/dribnicsKeGgeffmjwsqtybz4woRvgony9ToqWtpp5FUqWSgugR8KwicDK62XsV5JOzkYYaKXic4ZLibWUQSo4vtzibaXmbuC5FUvrp3zHHj4ykcM/640?wx_fmt=png&from=appmsg)

```
0110011001101100011000010110011101111011001101000110010000110010001101000011011101100001011000110011001100110001001101100110001000110001011000110110011000110111011001010110011000110101001100110110000100110001001101010011100101100011001100110011000000110001001101100110001001100001011000100011100101111101
```

二进制转ASCII

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgf533YghjIic5ysRmoiaLgepymNZoR1oUM3kwh1LYlybd0ibGDURBiaepplNAkoLYH37RDoOOwgVU5OsdbrrGO2iajCIWQBX0X9Wh5c/640?wx_fmt=png&from=appmsg)

```
flag{4d247ac316b1cf7ef53a159c3016bab9}
```

## 找到呆唯

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dribnicsKeGgdVYDyu8RFf5O54MsBNdJw4BZlko3UOxSYXGe4hdET7fflxOfc3ygmS7zKwAJMcvtUfj19RJ8sX9qt...