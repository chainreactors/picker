---
title: 2024年中国工业互联网安全大赛智能家电赛道选拔赛 by Mini-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247510681&idx=1&sn=a7b25eae740e541f7d2898799f238ed5&chksm=e89d8241dfea0b573b9a8a8fa21328665ed140a851a7a6783c3429fe3d42bcfdb139fbaab984&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-07-15
fetch_date: 2025-10-06T17:40:32.915238
---

# 2024年中国工业互联网安全大赛智能家电赛道选拔赛 by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GT0SsVlhy4CDJHXXyUZHR5RTKggV8nNE2sqTNZB7d6RasJtudfEogyjA/0?wx_fmt=jpeg)

# 2024年中国工业互联网安全大赛智能家电赛道选拔赛 by Mini-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## 初步密码学

题目信息

```
import rsa

def rsaencode(m):
    # 生成RSA密钥对
    (pubkey, privkey) = rsa.newkeys(256)
    # 获取公钥和私钥参数
    n = pubkey.n
    print(n)
    e = pubkey.e
    print(e)
    c = rsa.encrypt(m, pubkey)
    return c

def add_one_to_ascii(data):
    result = bytearray()
    for byte in data:
        result.append(byte + 1)
    return bytes(result)

def xor_bytes(data, key):
    result = bytearray()
    for byte in data:
        result.append(byte ^ key)
    return bytes(result)

if __name__ == '__main__':
    # 使用公钥进行加密
    m=xor_bytes(add_one_to_ascii(x),12)
    c=rsaencode(m)
    print("加密后的密文:", c.hex())

#output
71484438965393396388835335667806052411397994375702758854090697767967524655627
65537
加密后的密文:0x515b50d7407f4f321ddea14d0d99e4134c285ee6b7b92b77f3ed65f32212a529
```

操作内容
已知n,e，n的比特256位，可使用yafu分解

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTaTFGT5m3y3EjRalXAWJX5TJQAH2YBxWuP28YFKdXUsRYJUhtBpfvSA/640?wx_fmt=png&from=appmsg)

攻击流量
得到p q后，常见思路解密即可

```
import rsa

def rsa_decode(c, pubkey):
    # 从公钥生成对应的私钥
    privkey = rsa.PrivateKey(pubkey.n, pubkey.e, pubkey.d, pubkey.p, pubkey.q)
    m = rsa.decrypt(c, privkey)
    return m

def subtract_one_from_ascii(data):
    result = bytearray()
    for byte in data:
        result.append(byte - 1)
    return bytes(result)

def xor_bytes(data, key):
    result = bytearray()
    for byte in data:
        result.append(byte ^ key)
    return bytes(result)

# RSA 公钥参数
n = 71484438965393396388835335667806052411397994375702758854090697767967524655627
e = 65537

# 加密后的密文 (已转换为字节)
ciphertext = bytes.fromhex('515b50d7407f4f321ddea14d0d99e4134c285ee6b7b92b77f3ed65f32212a529')

# 创建公钥对象
pubkey = rsa.PublicKey(n, e)

p = 895534711824738922785094048763390663
q = 79823191688166851259736970548355545692829
d = 19619308233067290551077729872542647104506154812668367156272584280826183049209
privkey = rsa.PrivateKey(n, e, d, p, q)

# 解密得到加密前的数据
decoded_data = rsa.decrypt(ciphertext, privkey)

# 逆向处理数据
decoded_data = xor_bytes(decoded_data, 12)
original_data = subtract_one_from_ascii(decoded_data)

print("解密后的原始明文:", original_data)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTNLzIwoUIjJEyuJnN55Ocrb1GqurYkutKofsia3eElibbwC9KryNMib3UA/640?wx_fmt=png&from=appmsg)

flag{954fbe80adb799}

## 恶意攻击流量

题目信息
应用系统被植入了恶意后门，并从流量中识别其中的flag，操作内容
我们判断找到了蚁剑流量，在153包里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTxoOTkOLF318fUHeqKIiaAploojz5hTibJqDnGpYrmzQjrIliaIBrJ8hRw/640?wx_fmt=png&from=appmsg)

使用base64解密，得到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTQPvTclU8LYJwfhRE0H4UTRgUP2B2vPFaIPRpdgHvXYl6mbTlv5E0pA/640?wx_fmt=png&from=appmsg)

```
cd "/var/www/html";echo ZmxhZ3szOTA4NEVFRjJEMjhFOTQxRjUzRTRBMUFBMUZBNjc2Nn0K|base64 -d > ./flag.txt;echo cc6288cd;pwd;echo 2ddc1cfd81
```

再使用base64解密
`ZmxhZ3szOTA4NEVFRjJEMjhFOTQxRjUzRTRBMUFBMUZBNjc2Nn0K` 得到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GT2ET2Om0oj7kabbXz6qaGQy4PHNcicL64PX3TPU24Fz7QeibFNhVNRWYQ/640?wx_fmt=png&from=appmsg)

flag{39084EEF2D28E941F53E4A1AA1FA6766}

## MQTT协议分析

题目信息
MQTT协议是一个基于客户端-服务器消息发布/订阅传输协议。MQTT协议具备轻量、简单、开放和易于实现等特点，使它适用范围非常广泛。附件中MQTT报文存在flag
操作内容
追踪tcp流，看到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTLVljP4eKRuSxl176opID8vHaTVbbcVtSOanicPPUN0icOOLACzQ3BZaQ/640?wx_fmt=png&from=appmsg)

将字符串组合起来，转16进制后得到

```
504b0304140001000000fb81e158591948f02000000014000000080000006d7174742e7478741b14fe05d941726530b707cce78a2bd8639d2ce0fdb7ce63270fe005a5f130ed504b01023f00140001000000fb81e158591948f020000000140000000800240000000000000020000000000000006d7174742e7478740a0020000000000001001800604005e48ecbda0100000000000000000000000000000000504b050600000000010001005a000000460000000000
```

使用cyberchef

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTjjqH25SHBOpkxG3EwAON7YkGHEhgkmzseKo1CibDmHKvJibqVVYLBYHA/640?wx_fmt=png&from=appmsg)

提取另存得到压缩包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTkapUNEic9PQznXdBu1VicLGGoUUVIKHeOk3hx3Mmlf3M7aLC76XRdsNg/640?wx_fmt=png&from=appmsg)

解码后的密码是 passwd\_mqtt\_6666 密码解压得到flag

flag{mqtt\_flag\_8888}

## 传感器异常

题目信息
工厂的温度传感器能存储一段时间内的读数，但最近存在异常读取的情况，请把具体Reference Numbe
操作内容
为了查找异常值，使用wireshark过滤器语法

```
modbus.reference_num >= 212
```

得到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTXz8XZwyyFsX7RgLLpPf790ibiaKYWJQ5y5GRkvC357X0F6gvia36qu1Aw/640?wx_fmt=png&from=appmsg)

Reference Number: 19934

flag{19934}

## re

查文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTZKbp1CMAGW0f7oOP4by0ibUq4JPjSqYboJ6DD4OYgakHlYDpuaibicYHA/640?wx_fmt=png&from=appmsg)

64位，查看ida反汇编

## 蓝牙数据分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTTYuJXTN2Yvp0sDvc0GqGy0AL32JNZj3lDL4ic2HtM3BumQCdqcW7Mow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTdrmvKDiaX8W9m5TbvXia2GTPiaamTOQNv0Dewz7UrHDCmJETWLhJCVNlABX9xkY8lunical7SzicUzDw/640?wx_fmt=png&from=appmsg)

将以上按顺序base64解密
依次拼接就好（f1,f2,f3顺序）
flag{
adsjopvap
349ls}

结束

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

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