---
title: Ubuntu 25.04 is now sched_ext ready
url: http://arighi.blogspot.com/2025/02/ubuntu-2504-is-now-schedext-ready.html
source: arighi's blog
date: 2025-02-15
fetch_date: 2025-10-06T20:35:10.363672
---

# Ubuntu 25.04 is now sched_ext ready

# [arighi's blog](http://arighi.blogspot.com/)

## Friday, February 14, 2025

### Ubuntu 25.04 is now sched\_ext ready

Ubuntu 25.04 *Plucky Puffin* now ships a linux-generic kernel
based on **6.12**, which means that **sched\_ext** is
supported out of the box! 🎉

This allows Ubuntu users to easily run multiple pluggable BPF
schedulers at runtime, without needing to recompile a custom kernel.

## Check your kernel version first

Before diving in, make sure you are actually running a 6.12 (or
newer) kernel:

```
$ uname -r
```

If you see something like this:

```
6.12.0-15-generic
```

You’re good to go!

## Examples

You can install and run `scx_bpfland`, a
scheduler designed to improve system responsiveness:

```
$ cargo install scx_bpfland
$ sudo ~/.cargo/bin/scx_bpfland
```

Then simply press CTRL+c to stop the program and restore the default
kernel scheduler.

If you’re looking for a scheduler optimized for gaming, you can try
`scx_lavd`:

```
$ cargo install scx_lavd
$ sudo ~/.cargo/bin/scx_lavd
```

For audio, multimedia, or soft real-time workloads,
`scx_flash` might be a better fit:

```
$ cargo install scx_flash
$ sudo ~/.cargo/bin/scx_flash
```

Alternatively, you can try `scx_rusty`, a hybrid scheduler
with a user-space load-balancer written in Rust:

```
$ cargo install scx_rusty
$ sudo ~/.cargo/bin/scx_rusty
```

And if you’re feeling brave, you can try `scx_rustland`, a
scheduler fully implemented in Rust that runs as a regular user-space
process:

```
$ cargo install scx_rustland
$ sudo ~/.cargo/bin/scx_rustland
```

That’s it! You’re now running a `sched_ext` scheduler on
your Ubuntu system.

## What’s next?

Apart from always improving and optimizing these schedulers, we are also
focusing at better integrating them into the major Linux
distributions, through proper packaging, etc.

In the future, it would be nice to have application-driven
schedulers, where apps can directly request a specific scheduler, that is
automatically loaded by a system daemon. For example, imagine Steam
automatically loading `scx_lavd`, Chrome requesting
`scx_bpfland`, or a web server reverting to the default
kernel scheduler, all of this dynamically, adapting to the particular workload's needs.

Posted by

[arighi](https://www.blogger.com/profile/15223521151492879497 "author profile")

at
[7:48 PM](http://arighi.blogspot.com/2025/02/ubuntu-2504-is-now-schedext-ready.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=4397409626710913610&postID=6731005776079198879&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=6731005776079198879&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=6731005776079198879&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=6731005776079198879&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=6731005776079198879&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=4397409626710913610&postID=6731005776079198879&target=pinterest "Share to Pinterest")

#### No comments:

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4397409626710913610/6731005776079198879)

[Newer Post](http://arighi.blogspot.com/2025/05/revamping-my-linux-kernel-scheduler-in.html "Newer Post")

[Older Post](http://arighi.blogspot.com/2025/01/accelerating-micro-vm-boot-time-with.html "Older Post")
[Home](http://arighi.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](http://arighi.blogspot.com/feeds/6731005776079198879/comments/default)

## Blog Archive

* [May](http://arighi.blogspot.com/2025/05/) (1)
* [February](http://arighi.blogspot.com/2025/02/) (1)
* [January](http://arighi.blogspot.com/2025/01/) (1)
* [September](http://arighi.blogspot.com/2024/09/) (1)
* [August](http://arighi.blogspot.com/2024/08/) (1)
* [May](http://arighi.blogspot.com/2024/05/) (1)
* [April](http://arighi.blogspot.com/2024/04/) (1)
* [March](http://arighi.blogspot.com/2024/03/) (1)
* [February](http://arighi.blogspot.com/2024/02/) (1)
* [July](http://arighi.blogspot.com/2023/07/) (1)
* [August](http://arighi.blogspot.com/2019/08/) (1)
* [December](http://arighi.blogspot.com/2018/12/) (1)
* [August](http://arighi.blogspot.com/2013/08/) (1)
* [May](http://arighi.blogspot.com/2013/05/) (1)
* [August](http://arighi.blogspot.com/2011/08/) (2)
* [January](http://arighi.blogspot.com/2011/01/) (2)
* [September](http://arighi.blogspot.com/2009/09/) (1)
* [June](http://arighi.blogspot.com/2009/06/) (2)
* [May](http://arighi.blogspot.com/2009/05/) (2)
* [April](http://arighi.blogspot.com/2009/04/) (2)
* [March](http://arighi.blogspot.com/2009/03/) (1)
* [January](http://arighi.blogspot.com/2009/01/) (2)
* [December](http://arighi.blogspot.com/2008/12/) (1)
* [October](http://arighi.blogspot.com/2008/10/) (5)
* [July](http://arighi.blogspot.com/2008/07/) (1)
* [May](http://arighi.blogspot.com/2008/05/) (2)
* [March](http://arighi.blogspot.com/2008/03/) (5)
* [February](http://arighi.blogspot.com/2008/02/) (1)
* [January](http://arighi.blogspot.com/2008/01/) (4)
* [October](http://arighi.blogspot.com/2007/10/) (1)
* [May](http://arighi.blogspot.com/2007/05/) (4)
* [April](http://arighi.blogspot.com/2007/04/) (3)
* [March](http://arighi.blogspot.com/2007/03/) (6)
* [February](http://arighi.blogspot.com/2007/02/) (2)

Andrea Righi - Principal System Software Engineer @ NVIDIA. Simple theme. Powered by [Blogger](https://www.blogger.com).