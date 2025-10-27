---
title: 针对top chunk的一些特殊攻击手法
url: https://buaq.net/go-170952.html
source: unSafe.sh - 不安全
date: 2023-07-02
fetch_date: 2025-10-04T11:51:09.245098
---

# 针对top chunk的一些特殊攻击手法

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/6d7aa348536de7297a006ac43f4469a3.jpg)

针对top chunk的一些特殊攻击手法

介绍house of force 主要利用 top chunk 的漏洞通过修改topchunk\_size来进行攻击利用 top chunk 分割的漏洞来申请任
*2023-7-1 15:29:0
Author: [xz.aliyun.com(查看原文)](/jump-170952.htm)
阅读量:24
收藏*

---

## 介绍

house of force 主要利用 top chunk 的漏洞

## top chunk的分割机制和利用方法

```
victim = av->top; /* 获取addr of top chunk */
size   = chunksize(victim); /* 获取top chunk size */
if ((unsigned long) (size) >= (unsigned long) (nb + MINSIZE))
{
    remainder_size = size - nb; /* 计算剩下的size */
    remainder      = chunk_at_offset(victim, nb);
    av->top        = remainder; /* 修改top chunk */
    set_head(victim, nb | PREV_INUSE |
            (av != &main_arena ? NON_MAIN_ARENA : 0)); /* 设置top chunk的头 */
    set_head(remainder, remainder_size | PREV_INUSE); /* 设置剩下chunk的头 */

    check_malloced_chunk(av, victim, nb);
    void *p = chunk2mem(victim);
    alloc_perturb(p, bytes);
    return p;
}
```

只有 top chunk 的 size 大于等于申请的 size，才会有后续操作
top chunk大小检查时用的数据类型是 unsigned long，如果能通过一些漏洞（比如堆溢出）将 top chunk 的 size 字段篡改成 -1 或者 0xffffffffffffffff，那么在做这个检查时，size 就变成了无符号整数中最大的值，这样一来，不管用户申请多大的堆空间都可以满足条件，此外，虽然此处的检查中，用户申请的大小也被当做无符号整型对待，但是在后面扩展 top chunk 的时候是作为 int 对待的

## 利用条件

用户能够篡改 top chunk 的 size 字段（篡改为负数或很大值）
用户可以申请任意大小的堆内存（包括负数）

### libc-2.23

```
/* Try to use top chunk */
  /* Require that there be a remainder, ensuring top always exists  */
  if ( (remainder_size = chunksize(top(ar_ptr)) - nb) < (long)MINSIZE)
  {

    /* If the request is big and there are not yet too many regions,
       and we would otherwise need to extend, try to use mmap instead.  */
    if ((unsigned long)nb >= (unsigned long)mmap_threshold &&
        n_mmaps < n_mmaps_max &&
        (victim = mmap_chunk(nb)) != 0)
      return victim;
      /* 如果申请字节超过“topchunk->size”,调用mmap_chunk */

    /* Try to extend */
    malloc_extend_top(ar_ptr, nb);
    if ((remainder_size = chunksize(top(ar_ptr)) - nb) < (long)MINSIZE)
    {

      /* A last attempt: when we are out of address space in a
         non-main arena, try mmap anyway, as long as it is allowed at
         all.  */
      if (ar_ptr != &main_arena &&
          n_mmaps_max > 0 &&
          (victim = mmap_chunk(nb)) != 0)
        return victim;
        /* 如果,第一次调用mmap_chunk没有成功,则再调用一次 */

      return 0; /* propagate failure */
    }
  }
  victim = top(ar_ptr);
  set_head(victim, nb | PREV_INUSE); /* 设置top chunk的头 */
  top(ar_ptr) = chunk_at_offset(victim, nb);
  set_head(top(ar_ptr), remainder_size | PREV_INUSE); /* 设置剩下chunk的头 */
  check_malloced_chunk(ar_ptr, victim, nb); /* 这个检查几乎没有影响 */
  return victim;
```

通过“topchunk->size”判断是否调用“mmap\_chunk”
完全可以打 House Of Force

### libc-2.27

```
if (av != &main_arena)
    {
      heap_info *old_heap, *heap;
      size_t old_heap_size;

      /* First try to extend the current heap. */
      old_heap = heap_for_ptr (old_top);
      old_heap_size = old_heap->size;
      if ((long) (MINSIZE + nb - old_size) > 0
          /* top chunk不够用，grow_heap扩展top chunk的空间 */
          /* 要打House Of Force,这个if一定不成立(old_size非常大) */
          && grow_heap (old_heap, MINSIZE + nb - old_size) == 0)
        {
          av->system_mem += old_heap->size - old_heap_size;
          set_head (old_top, (((char *) old_heap + old_heap->size) - (char *) old_top)
                    | PREV_INUSE);
        }
      else if ((heap = new_heap (nb + (MINSIZE + sizeof (*heap)), mp_.top_pad)))
        {
          /* Use a newly allocated heap.  */
          heap->ar_ptr = av;
          heap->prev = old_heap;
          av->system_mem += heap->size;
          /* Set up the new top.  */
          top (av) = chunk_at_offset (heap, sizeof (*heap));
          set_head (top (av), (heap->size - sizeof (*heap)) | PREV_INUSE);

          /* Setup fencepost and free the old top chunk with a multiple of
             MALLOC_ALIGNMENT in size. */
          /* The fencepost takes at least MINSIZE bytes, because it might
             become the top chunk again later.  Note that a footer is set
             up, too, although the chunk is marked in use. */
          old_size = (old_size - MINSIZE) & ~MALLOC_ALIGN_MASK;
          set_head (chunk_at_offset (old_top, old_size + 2 * SIZE_SZ), 0 | PREV_INUSE);
          if (old_size >= MINSIZE) /* 需要分割 */
            {
              set_head (chunk_at_offset (old_top, old_size), (2 * SIZE_SZ) | PREV_INUSE);
              set_foot (chunk_at_offset (old_top, old_size), (2 * SIZE_SZ));
              set_head (old_top, old_size | PREV_INUSE | NON_MAIN_ARENA);
              _int_free (av, old_top, 1);
            }
          else /* 不需要分割 */
            {
              set_head (old_top, (old_size + 2 * SIZE_SZ) | PREV_INUSE);
              set_foot (old_top, (old_size + 2 * SIZE_SZ));
            }
        }
      else if (!tried_mmap)
        /* We can at least try to use to mmap memory.  */
        goto try_mmap;
    }
................
```

程序复杂了不少，也多了许多检查：

```
static void
do_check_chunk (mstate av, mchunkptr p)
{
  unsigned long sz = chunksize (p);
  /* min and max possible addresses assuming contiguous allocation */
  char *max_address = (char *) (av->top) + chunksize (av->top);
  char *min_address = max_address - av->system_mem;
    /* 这里就是问题的关键 */
    /* 因为“topchunk->size”被设置得非常大，所以max_address和min_address也非常大 */
    /* 这个设置范围的操作打死了House Of Force */

  if (!chunk_is_mmapped (p))
    {
      /* Has legal address ... */
      if (p != av->top)
        {
          if (contiguous (av))
            {
              assert (((char *) p) >= min_address);
              /* 因为min_address非常大，重新申请的chunk地址不可能大于它 */
              assert (((char *) p + sz) <= ((char *) (av->top)));
            }
        }
      else
        {
          /* top size is always at least MINSIZE */
          assert ((unsigned long) (sz) >= MINSIZE);
          /* top predecessor always marked inuse */
          assert (prev_inuse (p));
        }
    }
  else if (!DUMPED_MAIN_ARENA_CHUNK (p))
    {
      /* address is outside main heap  */
      if (contiguous (av) && av->top != initial_top (av))
        {
          assert (((char *) p) < min_address || ((char *) p) >= max_address);
        }
      /* chunk is page-aligned */
      assert (((prev_size (p) + sz) & (GLRO (dl_pagesize) - 1)) == 0);
      /* mem is aligned */
      assert (aligned_OK (chunk2mem (p)));
    }
}
```

House Of Force 只能在 libc-2.23 中生效，因为 libc-2.23 会在检查了“topchunk->size”后就进行分割，可以直接利用，而 libc-2.27 设置了一个“范围”，限制了申请chunk的地址范围，这样就导致 top chunk 无法分割到目标地址了

## Large bin 泄露 libc\_base

### 背景知识

在glibc堆初始化时会一次划出132KB的内存大小来供程序使用，也就是说我们提到tcache/fast/small/unsorted/large都是在这132KB（0x21000）基础上产生的。那么如果直接malloc超过132KB大小的话。系统会调用mmap在libc附近分配内存，经过测试虽然大于132KB可以让其分配在libc附近，但不达到一定大小，分配的内存地址和libc的偏移是不太确定的。这里借鉴了前辈的经验，分配0x200000的内存可以让偏移固定。

```
#include <stdio.h>
#include <stdlib.h>

int main()
{
    malloc(0x1);  // init heap
    // 0x200000 == 2097152
    long long * ptr = malloc(2097152);
    printf("mmap addr is %p\n", ptr);

    return 0;
}
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230630232735-a3d68d50-175a-1.png)

## gyctf\_2020\_force

### ida

![](https://xzfile.aliyuncs.com/media/upload/picture/20230630232757-b0e737ba-175a-1.png)

```
Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

```
void __fastcall __noreturn main(int a1, char **a2, char **a3)
{
  __int64 v3; // rax
  char s[256]; // [rsp+10h] [rbp-110h] BYREF
  unsigned __int64 v5; // [rsp+118h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  setbuf(stdin, 0LL);
  setbuf(stdout, 0LL);
  setbuf(stderr, 0LL);
  memset(s, 255, sizeof(s));
  wh...