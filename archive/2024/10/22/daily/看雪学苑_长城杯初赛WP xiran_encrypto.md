---
title: 长城杯初赛WP xiran_encrypto
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578861&idx=2&sn=f845fdaa326e6167847d6c0beb82b62d&chksm=b18ddf2786fa5631b121f9ceb7fa7a5ec003a77eb8c053f6dd877c0b6ba8fdc85ccc71b9c278&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-22
fetch_date: 2025-10-06T18:51:44.338121
---

# 长城杯初赛WP xiran_encrypto

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOQqRW1IZvI9sYoSrkB0a3eEB6OXSibV2ERQVVtoNsaOJsrbMqo9lyPeA/0?wx_fmt=jpeg)

# 长城杯初赛WP xiran\_encrypto

SleepAlone

看雪学苑

该题为正常ctf题与恶意脚本相结合的题目，cha为常规的re题目，clickme为恶意样本，在cha中拿到信息，然后根据clickme的逻辑解密。

cha的核心为比较经过换表base64然后与自己xor之后与内存中的32字节相比较

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOSj881fQXwWXLnMwFgufc9ph7AoiazZibyx0syzZzWDYD05QAruQgxziaw/640?wx_fmt=png&from=appmsg)

求解思路:

1.DFS爆破，因为前面的字节会影响后面的状态

2.利用前面的数据求和信息，筛选唯一解

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaONn8s2Bz4QyiaDywoCiaM4LRb0anHOV5XmqlbBnW8Ddr5ziadBW3Lgp8FA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOlZIzSOqkiauxPZU4LqMc4zWBYyRJLqAfuuUBflM0u6AhrraxOZPAH0w/640?wx_fmt=png&from=appmsg)

爆破脚本：

```
convert_table = b'APet8BQfu9CRgv+DShw/ETixFUjyGVkzHWl0IXm1JYn2KZo3Lap4Mbq5Ncr6Ods7'
encrypted_flag = [0xD9, 0x40, 0x6F, 0xCA, 0x3D, 0x8F, 0x53, 0xB1, 0x8B, 0x34,
  0x92, 0x8E, 0xF7, 0x19, 0x94, 0x61, 0x68, 0x71, 0x55, 0xB6,
  0xCE, 0x5B, 0x71, 0x1A, 0x79, 0x42, 0x9D, 0x02, 0x93, 0x38,
  0xAD, 0x1F, 0xD3, 0x24, 0x48, 0xFF, 0x21, 0xA2, 0x24, 0xBE,
  0x95, 0x3A, 0xC1, 0xD2]

def convert(flag,index):
    group = (index // 4) * 3
    if index % 4 == 0:
        return convert_table[flag[group] >> 2]
    if index % 4 == 1:
        return convert_table[(flag[group] << 4 & 0x30) + (flag[group + 1] >> 4)]
    if index % 4 == 2:
        return convert_table[(flag[group + 1] << 2 & 0x3c) + (flag[group + 2] >> 6)]
    if index % 4 == 3:
        return convert_table[flag[group + 2] & 0x3f]

def brup(flag):
    cur_len = len(flag)
    if cur_len != 0:
        res = flag[cur_len-1] ^ convert(flag,cur_len-1)
        if res != encrypted_flag[cur_len-1]:
            return
    if cur_len == 32:
        sum = 0
        for i in range(len(flag)):
            sum = 19*sum + flag[i]
        sum = sum & 0xffffffff
        if sum == 0xD033A96A:
            for i in flag:
                print(i,end=',')
        return
    for i in range(256):
        flag.append(i)
        brup(flag)
        flag.pop()

flag = bytearray()
brup(flag)
```

#

# clickme

clickme为babyuk家族，主要加密逻辑也类似。

核心加密逻辑在main\_encrypt\_file中：

1. 根据curve25519算法（随机私钥和对应的公钥，共享密钥） 产生key nonce
2. 根据key，nonce 产生cipher（golang\_org\_x\_crypto\_chacha20\_newUnauthenticatedCipher）
3. xorKeyStream加密文件

1. 每0xA00000加密0x100000
2. 加密整个文件
3. 如果文件大小 < 0x1400000
4. 如果文件大小 > 0x1400000
5. 最后写入32字节公钥和固定标识

解密脚本：

```
package main

import (
    "crypto/sha256"
    "os"

    "golang.org/x/crypto/chacha20"
    "golang.org/x/crypto/curve25519"
)

func main() {

    file, err := os.OpenFile("flag.png.xiran",os.O_RDWR,0)
    if err != nil {
        panic(err)
    }

    fileinfo,err :=  file.Stat()
    if err != nil {
        panic(err)
    }

    filesize := fileinfo.Size()
    var start  int64  =  0
    end := filesize

    privateKeyBob := [32]byte{144,16,46,165,100,230,124,220,241,66,166,239,164,119,237,82,49,23,47,236,139,107,73,98,43,49,237,80,249,117,245,115}

    publicKeyAlice := make([]byte,32,32)

    offset,err := file.Seek(filesize-32-6,0)
    if err != nil {
        panic(err)
    }

    file.ReadAt(publicKeyAlice,offset)

    var sharedKeyAlice [32]byte
    curve25519.ScalarMult(&sharedKeyAlice, &privateKeyBob, (*[32]byte)(publicKeyAlice))

    var key [32]byte= sha256.Sum256(sharedKeyAlice[:])
    var res [32]byte = sha256.Sum256(key[:])
    nonce := res[10:22]

    cipher, err :=  chacha20.NewUnauthenticatedCipher(key[:],nonce)
    if err != nil {
        panic(err)
    }

    buffer := make([]byte, 0x100000,0x100000)

    for start < end {
        file.ReadAt(buffer,start)
        cipher.XORKeyStream(buffer,buffer)
        file.WriteAt(buffer,start)
        start += 0xA00000
    }

    if err := file.Close(); err != nil {
        panic(err)
    }

}
```

#

# 一些思考

cha中的私钥如果纯静态的分析 只有爆破才行 能不能在cha运行时把 私钥dump出来？

在尝试的过程中发现cha中，在.init\_array中存在一个特殊的初始化函数，在这个函数中做了两个（或者一个）反调试：

1.ptrace(PTRACE\_TRACEME) == -1 退出

2.读取某个内存中的值若为0 则退出（前面有个call 清除这个内存处的值）

在bypass这两个点之后，进入main之后 发现私钥对应的内存实际为0，这也和在ida中找不到它的xref呼应，我觉得这里作者的意思就是故意让程序运行不到main，所以正确做法只能爆破，不然直接进内存dump太简单了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Gg00pteL01boyHHAZkxpDPgicYEbic99Tq1lev88UuPADEIvUA4PyumGaibOeY8kMCs9FbEnbouZ58g/640?wx_fmt=png&from=appmsg)

看雪ID：SleepAlone

*https://bbs.kanxue.com/user-home-950548.htm*

\*本文为看雪论坛优秀文章，由 SleepAlone 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Er3I7ngTeRiagnpVsnQNBOznYEPFDbgACIPrns8Y0zmpqdGz5eJeZOD5secWYnUGCicdQKydHO5QSA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578361&idx=4&sn=4bafaf25a32aec59423e734707d17692&chksm=b18ddd3386fa5425f67022a2718d09a9000ca4cdde95f8ef76f649c665a1d7d691b9cd9ce668&scene=21#wechat_redirect)

# 往期推荐

1、[记录一次BlackObfuscator去混淆流程](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578441&idx=2&sn=7c13fd31edd2d6b5fe28749bca0e38f5&chksm=b18dde8386fa5795823e3f4ed6f2d6b8cbced7fc240ecf4af74f7de2f3157337bbf0d31baf33&scene=21#wechat_redirect)

2、[libEnccryptor vm 还原的探索](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578361&idx=2&sn=ef71b4dd800e90cb472fb7ed8484b8c4&chksm=b18ddd3386fa5425d7b5b72ffe3933161af3eaa6e8d83bed1413804d05d621d8ae42cd499012&scene=21#wechat_redirect)

3、[PHP PWN 入门调试](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578281&idx=2&sn=7ea01ef1bd9b7fd3646a0ff3eb0301a2&chksm=b18ddde386fa54f548e8c64e737d24f9d2e3f5607b80ac042f79fa0df8301fbb2a30e1500971&scene=21#wechat_redirect)

4、[记录一次\*\*App H5逆向](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458578091&idx=2&sn=9d5d28e1f03d16dd1b2c72adc42c1cbb&chksm=b18ddc2186fa55376bedf18a504b799ef3424223728b3a8ff3eac586d6ca3a0852c27c21a4af&scene=21#wechat_redirect)

5、[CAN协议分析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458577983&idx=2&sn=ecc8784d0787b770919741ce649bd197&chksm=b18ddcb586fa55a336b1123f9bc159fcdaa8aeb3f0e28bc4f8dc30eb7850ae8299d90858ec04&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOD1zWHhoGfX2uQZP77uicPSvQ6RM9BjVqiblHOQQWfXJUNfqWdp99sp7A/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOD1zWHhoGfX2uQZP77uicPSvQ6RM9BjVqiblHOQQWfXJUNfqWdp99sp7A/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOD1zWHhoGfX2uQZP77uicPSvQ6RM9BjVqiblHOQQWfXJUNfqWdp99sp7A/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8HV4oXy9xTchZtvHHCULqiaOcA9IqwcP7iaIbzxzmmb3e4JZWfwhJH4xRBxVlrqHSjfBn05vqqrLjCA/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过