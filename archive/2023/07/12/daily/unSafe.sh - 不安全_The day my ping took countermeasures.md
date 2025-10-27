---
title: The day my ping took countermeasures
url: https://buaq.net/go-171754.html
source: unSafe.sh - 不安全
date: 2023-07-12
fetch_date: 2025-10-04T11:51:35.380990
---

# The day my ping took countermeasures

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

![](https://8aqnet.cdn.bcebos.com/649565fe310b6be89db49e229322a277.jpg)

The day my ping took countermeasures

Loading...
*2023-7-11 21:0:1
Author: [blog.cloudflare.com(查看原文)](/jump-171754.htm)
阅读量:24
收藏*

---

Loading...

* [![Marek Majkowski](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2017/03/b5967d6c687939594adb6992723d0529.jpeg)](https://blog.cloudflare.com/author/marek-majkowski/)

![The day my ping took countermeasures](https://blog.cloudflare.com/content/images/2023/07/unnamed-1.png)![](https://blog.cloudflare.com/content/images/2023/07/Screenshot-2023-07-11-at-13.30.23.png)

Once my holidays had passed, I found myself reluctantly reemerging into the world of the living. I powered on a corporate laptop, scared to check on my email inbox. However, before turning on the browser, obviously, I had to run a ping. Debugging the network is a mandatory first step after a boot, right? As expected, the network was perfectly healthy but what caught me off guard was this message:

![](https://blog.cloudflare.com/content/images/2023/07/image6.png)

I was not expecting **ping** to **take countermeasures** that early on in a day. Gosh, I wasn't expecting any countermeasures that Monday!

Once I got over the initial confusion, I took a deep breath and collected my thoughts. You don't have to be Sherlock Holmes to figure out what has happened. I'm really fast - I started **ping** *before* the system **NTP** daemon synchronized the time. In my case, the computer clock was rolled backward, confusing ping.

While this doesn't happen too often, a computer clock can be freely adjusted either forward or backward. However, it's pretty rare for a regular network utility, like ping, to try to manage a situation like this. It's even less common to call it "taking countermeasures". I would totally expect ping to just print a nonsensical time value and move on without hesitation.

Ping developers clearly put some thought into that. I wondered how far they went. Did they handle clock changes in both directions? Are the bad measurements excluded from the final statistics? How do they test the software?

I can't just walk past ping "taking countermeasures" on me. Now I have to understand what ping did and why.

### Understanding ping

An investigation like this starts with a quick glance at the source code:

```
 *			P I N G . C
 *
 * Using the InterNet Control Message Protocol (ICMP) "ECHO" facility,
 * measure round-trip-delays and packet loss across network paths.
 *
 * Author -
 *	Mike Muuss
 *	U. S. Army Ballistic Research Laboratory
 *	December, 1983
```

**Ping** goes back a long way. It was originally written by [Mike Muuss](https://en.wikipedia.org/wiki/Mike_Muuss) while at the U. S. Army Ballistic Research Laboratory, in 1983, before I was born. The code we're looking for is under [iputils/ping/ping\_common.c](https://github.com/iputils/iputils/blob/ee0a515e74b8d39fbe9b68f3309f0cb2586ccdd4/ping/ping_common.c#L746) gather\_statistics() function:

![](https://blog.cloudflare.com/content/images/2023/07/image5.png)

The code is straightforward: the message in question is printed when the measured RTT is negative. In this case ping resets the latency measurement to zero. Here you are: "taking countermeasures" is nothing more than just marking an erroneous measurement as if it was 0ms.

But what precisely does ping measure? Is it the wall clock? The [man page](https://man7.org/linux/man-pages/man8/ping.8.html) comes to the rescue. Ping has two modes.

The "old", -U mode, in which it uses the wall clock. This mode is less accurate (has more jitter). It calls **gettimeofday** before sending and after receiving the packet.

The "new", default, mode in which it uses "network time". It calls **gettimeofday** before sending, and gets the receive timestamp from a more accurate SO\_TIMESTAMP CMSG. More on this later.

### Tracing gettimeofday is hard

Let's start with a good old strace:

```
$ strace -e trace=gettimeofday,time,clock_gettime -f ping -n -c1 1.1 >/dev/null
... nil ...
```

It doesn't show any calls to **gettimeofday**. What is going on?

On modern Linux some syscalls are not true syscalls. Instead of jumping to the kernel space, which is slow, they remain in userspace and go to a special code page provided by the host kernel. This code page is called **vdso**. It's visible as a **.so** library to the program:

```
$ ldd `which ping` | grep vds
    linux-vdso.so.1 (0x00007ffff47f9000)
```

Calls to the **vdso** region are not syscalls, they remain in userspace and are super fast, but classic strace can't see them. For debugging it would be nice to turn off **vdso** and fall back to classic slow syscalls. It's easier said than done.

There is no way to prevent loading of the **vdso**. However there are two ways to convince a loaded program not to use it.

The first technique is about fooling glibc into thinking the **vdso** is not loaded. This case must be handled for compatibility with ancient Linux. When bootstrapping in a freshly run process, glibc inspects the [Auxiliary Vector](https://www.gnu.org/software/libc/manual/html_node/Auxiliary-Vector.html) provided by ELF loader. One of the parameters has the location of the **vdso** pointer, [the man page](https://man7.org/linux/man-pages/man7/vdso.7.html) gives this example:

```
void *vdso = (uintptr_t) getauxval(AT_SYSINFO_EHDR);
```

A technique proposed on [Stack Overflow](https://stackoverflow.com/a/63811017) works like that: let's hook on a program before **execve**() exits and overwrite the Auxiliary Vector AT\_SYSINFO\_EHDR parameter. Here's the [novdso.c](https://github.com/danteu/novdso/blob/master/novdso.c) code. However, the linked code doesn't quite work for me (one too many **kill(SIGSTOP)**), and has one bigger, fundamental flaw. To hook on **execve()** it uses **ptrace()** therefore doesn't work under our strace!

```
$ strace -f ./novdso ping 1.1 -c1 -n
...
[pid 69316] ptrace(PTRACE_TRACEME)  	= -1 EPERM (Operation not permitted)
```

While this technique of rewriting AT\_SYSINFO\_EHDR is pretty cool, it won't work for us. (I wonder if there is another way of doing that, but without ptrace. Maybe with some BPF? But that is another story.)

A second technique is to use **LD\_PRELOAD** and preload a trivial library overloading the functions in question, and forcing them to go to slow real syscalls. This works fine:

```
$ cat vdso_override.c
#include <sys/syscall.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

int gettimeofday(struct timeval *restrict tv, void *restrict tz) {
	return syscall(__NR_gettimeofday, (long)tv, (long)tz, 0, 0, 0, 0);
}

time_t time(time_t *tloc) {
	return syscall(__NR_time, (long)tloc, 0, 0, 0, 0, 0);
}

int clock_gettime(clockid_t clockid, struct timespec *tp) {
    return syscall(__NR_clock_gettime, (long)clockid, (long)tp, 0, 0, 0, 0);
}
```

To load it:

```
$ gcc -Wall -Wextra -fpic -shared -o vdso_override.so vdso_override.c

$ LD_PRELOAD=./vdso_override.so \
       strace -e trace=gettimeofday,clock_gettime,time \
       date

clock_gettime(CLOCK_REALTIME, {tv_sec=1688656245 ...}) = 0
Thu Jul  6 05:10:45 PM CEST 2023
+++ exited with 0 +++
```

Hurray! We can see the **clock\_gettime** call in **strace** output. Surely we'll also see **gettimeofday** from our **ping**, right?

Not so fast, it still doesn't quite work:

```
$ LD_PRELOAD=./vdso_override.so \
     strace -c -e trace=gettimeofday,time,clock_gettime -f \
     ping -n -c1 1.1 >/dev/null
... nil ...
```

### To suid or not to suid

I forgot that **ping** might need special permissions to ...