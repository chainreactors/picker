---
title: tcache bin利用总结
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493159&idx=1&sn=077a4046dfd44ceca20840cf9c64e4f8&chksm=b18e906d86f9197b2fdbfb1df93ba8fb495a0d9e5b16a39347a72c7bf17428aff61615b973ac&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-27
fetch_date: 2025-10-04T04:58:52.126798
---

# tcache bin利用总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8H7XO5WDldlrI1X6NZwcPLclATXFWLYqLz41ecJcTwHicJOIpXWIeTN16ZIG3FaMiabKibXp6VdTeItg/0?wx_fmt=jpeg)

# tcache bin利用总结

kotoriseed

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDud63Mvg9u2d8TmNrnxrfNiajprkuSJ9ft0FxfWoDSwej3jM5H7Wh7Mng/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：kotoriseed

```
一

# tcache bin概述
```

在libc2.26及之后，glibc引入了tcache机制，目的是为了使多线程下的堆分配有更高的效率。

## **libc2.26**

最初版本的tcache引入了这两个结构体。

```
/* We overlay this structure on the user-data portion of a chunk when the chunk is stored in the per-thread cache.  */typedef struct tcache_entry{  struct tcache_entry *next;} tcache_entry;
```

```
/* There is one of these for each thread, which contains the per-thread cache (hence "tcache_perthread_struct").  Keeping overall size low is mildly important.  Note that COUNTS and ENTRIES are redundant (we could have just counted the linked list each time), this is for performance reasons.  */typedef struct tcache_perthread_struct{  char counts[TCACHE_MAX_BINS];  tcache_entry *entries[TCACHE_MAX_BINS];} tcache_perthread_struct;
static __thread tcache_perthread_struct *tcache = NULL;
```

从以上部分可以看出，他是类似于fastbin的一种单链表结构。

除此之外，还有两个重要函数：

```
static voidtcache_put (mchunkptr chunk, size_t tc_idx){  tcache_entry *e = (tcache_entry *) chunk2mem (chunk);  assert (tc_idx < TCACHE_MAX_BINS);  e->next = tcache->entries[tc_idx];  tcache->entries[tc_idx] = e;  ++(tcache->counts[tc_idx]);}
```

tcache\_put会在\_int\_free函数的开头被调用，尝试将对应freed chunk优先放入tcache bin中。

因为有TCACHE\_MAX\_BINS的限制（类似于fastbin的global\_max\_fast去限制fastbinsY数组），0x400及以上的chunk并不会放入tcache bin。

并且每条单链表上最多有mp\_.tcache\_count个chunk，该值默认为7。

而且这里应该注意，tcache\_entry \*e = (tcache\_entry \*) chunk2mem(chunk);这里调用了chunk2mem这个宏，所以tcache链表串起来的是对应chunk的userdata的位置。

```
static void *tcache_get (size_t tc_idx){  tcache_entry *e = tcache->entries[tc_idx];  assert (tc_idx < TCACHE_MAX_BINS);  assert (tcache->entries[tc_idx] > 0);  tcache->entries[tc_idx] = e->next;  --(tcache->counts[tc_idx]);  return (void *) e;}
```

tcache\_get会在\_int\_malloc的开头被调用，尝试从tcache bin里面拿对应的chunk。

这里给出一个demo程序来简单看一下tcache：![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuHYIcxmvicweKJw6Q2BK5IfpEhFufAS2FiajowODavqLpic1Kj0P5gV95A/640?wx_fmt=png)

编译语句：

gcc -o demo ./demo.c -no-pie

在puts处下断点，查看bins情况![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDupkdNs0SiawBL9UpNC70x1vE6XUw1icBlibp28j6836KCp3A0p8v7bml2Q/640?wx_fmt=png)

可以看到，0x30和0x40的tcache bin被放入了7个chunk的时候，再次free这两个size的chunk，都进到了fastbin里面。

## **libc2.29+**

(注：在2.27的高版本同样也具有相关检测)

在libc2.29之后，tcacbe\_entry结构体中加入了一个key指针。

```
typedef struct tcache_entry{  struct tcache_entry *next;  /* This field exists to detect double frees.  */  struct tcache_perthread_struct *key;} tcache_entry;
```

next对应了malloc\_chunk中的fd那个位置，key对应了bk的位置。

tcache\_put函数针对key有了相关的更新：

```
static __always_inline voidtcache_put(mchunkptr chunk, size_t tc_idx){  tcache_entry *e = (tcache_entry *)chunk2mem(chunk);
  /* Mark this chunk as "in the tcache" so the test in _int_free will     detect a double free.  */  e->key = tcache;
  e->next = tcache->entries[tc_idx];  tcache->entries[tc_idx] = e;
  ++(tcache->counts[tc_idx]);}
```

由于这个key的加入，tcachebin的double free检测有了更新：

```
size_t tc_idx = csize2tidx(size);
if (tcache != NULL && tc_idx < mp_.tcache_bins){  /* Check to see if it's already in the tcache.  */  tcache_entry *e = (tcache_entry *)chunk2mem(p);
  if (__glibc_unlikely(e->key == tcache))  {    tcache_entry *tmp;    LIBC_PROBE(memory_tcache_double_free, 2, e, tc_idx);  //这里会以一定的概率去遍历链表    for (tmp = tcache->entries[tc_idx]; tmp; tmp = tmp->next)      if (tmp == e)        malloc_printerr("free(): double free detected in tcache 2");  }
  if (tcache->counts[tc_idx] < mp_.tcache_count)  {    tcache_put(p, tc_idx);    return;  }}
```

这里只是初步过一遍，后面会结合对应版本的源码讲具体攻击手法。

```
二

攻击手法
```

在tcache机制加入的初期，问题其实是非常多的，他的安全性甚至还不如fastbin，这就导致了非常多的利用可以轻易达成。

## **tcache poisoning**

###

### **介绍**

类似于fastbin attack，不过目前的tcache并没有检查next指向的chunk的size是否合法，所以直接伪造next指针为想要修改的地址就好了。

这里在libc2.27下做一个演示：![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuKAJwWZDvNFIhvJlA3nfiaFoTVllfbEAkWWlRDvRT9CiavU4tia1hxy9Ag/640?wx_fmt=png)

注：在hijack b的next指针之前，先free掉了一个相同大小的chunk，这是因为在该版本下有一个检查，

assert (tcache->counts[tc\_idx] > 0);

运行结果如下：![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDu1icUkcPvQmkJL5gXwiabjicSQiatTSXicZC7pibOdIlDGcdS9uewXHxbfFSw/640?wx_fmt=png)

### **tcache poisoning at 2.34+**

在2.34以及之后的版本中，libc对fastbin和tcache bin的fd指针位置进行了宏操作来保护地址。

```
/* Safe-Linking:   Use randomness from ASLR (mmap_base) to protect single-linked lists   of Fast-Bins and TCache.  That is, mask the "next" pointers of the   lists' chunks, and also perform allocation alignment checks on them.   This mechanism reduces the risk of pointer hijacking, as was done with   Safe-Unlinking in the double-linked lists of Small-Bins.   It assumes a minimum page size of 4096 bytes (12 bits).  Systems with   larger pages provide less entropy, although the pointer mangling   still works.  */#define PROTECT_PTR(pos, ptr) \  ((__typeof (ptr)) ((((size_t) pos) >> 12) ^ ((size_t) ptr)))#define REVEAL_PTR(ptr)  PROTECT_PTR (&ptr, ptr)
```

劫持方法并没有太大的改变，这一部分手动分析即可。

（例题参考：ByteCTF-2022 mini\_http2）

### **例题**

####

#### **HITCON 2018 baby\_tcache**

环境是libc2.27的，保护全开。（为了方便本地演示，调试时关掉了本机的ALSR）![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuytrNMP9z5Rh4zXmOjsiatyPjr8367nhk6npAk0QVp2b3RlJEM0uAvYA/640?wx_fmt=png)

主菜单只有两个功能，创建堆和释放堆，并没有可以用来leak信息的show功能。

漏洞非常直白：![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDufnXLkI2lfYeyjEYk9PWp7NjSOIx6wWQS7btiasJWliaxoqkdDCBy8M3A/640?wx_fmt=png)

在read结束过后有一个off by null。

由于没有可以用于leak的函数，这里会用到一个IO\_FILE的技巧：劫持 \_IO\_2\_1\_stdout\_

虽然程序一开始用setbuf关闭了缓冲区， 但我们还是可以修改\_IO\_2\_1\_stdout\_的\_flags成员来让程序误以为存在缓冲。

因为程序调用了大量的puts函数，而puts会调用\_IO\_new\_file\_xsputn--> \_IO\_new\_file\_overflow

-->\_IO\_do\_write

```
int_IO_new_file_overflow (_IO_FILE *f, int ch){  if (f->_flags & _IO_NO_WRITES)    {      f->_flags |= _IO_ERR_SEEN;      __set_errno (EBADF);      return EOF;    }  /* If currently reading or no buffer allocated. */  if ((f->_flags & _IO_CURRENTLY_PUTTING) == 0 || f->_IO_write_base == NULL)    {      :      :    }  if (ch == EOF)    return _IO_do_write (f, f->_IO_write_base,             f->_IO_write_ptr - f->_IO_write_base);
```

```
static_IO_size_tnew_do_write (_IO_FILE *fp, const char *data, _IO_size_t to_do){  _IO_size_t count;  if (fp->_flags & _IO_IS_APPENDING)    /* On a system without a proper O_APPEND implementation,       you would need to sys_seek(0, SEEK_END) here, but is       not needed nor desirable for Unix- or Posix-like systems.       Instead, just indicate that offset (before and after) is       unpredictable. */    fp->_offset = _IO_pos_BAD;  else if (fp->_IO_read_end != fp->_IO_write_base)    {     ............    }  count = _IO_SYSWRITE (fp, data, to_do);
```

总的来说，要使程序认为stdout仍具有缓冲区，需要满足：

* !(f->\_flags & \_IO\_NO\_WRITES)
* f->\_flags & \_IO\_CURRENTLY\_PUTTING
* fp->\_flags & \_IO\_IS\_APPENDING

即：

```
_flags = 0xfbad0000  // Magic number_flags & = ~_IO_NO_WRITES // _flags = 0xfbad0000_flags | = _IO_CURRENTLY_PUTTING // _flags = 0xfbad0800_flags | = _IO_IS_APPENDING // _flags = 0xfbad1800
```

\_flags满足过后，就会输出\_IO\_2\_1\_stdout\_中\_IO\_write\_base到\_IO\_write\_ptr之间的内容。

leak的思路有了之后，先构造overlap chunk，

```
create(0x4f0) # 0create(0x30) # 1 # 多用几个tcache范围内不同的size，方便free的时候能精准指向目标create(0x40) # 2create(0x50) # 3create(0x60) # 4 # 用于取消下一个chunk的prev_inuse bit，触发unlinkcreate(0x4f0) # 5create(0x60, p64(0xdeadbeef)) # 6 # 防止和top chunk合并delete(4)pay = b'a'*0x60 + p64(0x660) # prev_size指向chunk 0create(0x68, pay) # 4delete(1) # 准备进行tcache poisoningdelete(0) # 使合并的对象能绕过unlink检查delete(5) # 触发合并
```

接着free掉chunk 4（其实chunk2和chunk3也行），为接下来拿到libcbase之后劫持\_\_free\_hook做准备。

然后申请0x500的chunk，切割unsortedbin...