---
title: Introducing oniux: Kernel-level Tor isolation for any Linux app
url: https://blog.torproject.org/introducing-oniux-tor-isolation-using-linux-namespaces/
source: Tor Project blog
date: 2025-05-15
fetch_date: 2025-10-06T22:29:44.708654
---

# Introducing oniux: Kernel-level Tor isolation for any Linux app

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Introducing oniux: Kernel-level Tor isolation for any Linux app

by [cve](/author/cve)
| May 14, 2025

![](/introducing-oniux-tor-isolation-using-linux-namespaces/lead.png)

When launching privacy-critical apps and services, developers want to make sure that every packet really only goes through Tor. One mistyped proxy settingâor a single system-call outside the SOCKS wrapperâand your data is suddenly on the line.

That's why today, we are excited to introduce *oniux*: a small command-line utility providing Tor network isolation for third-party applications using Linux namespaces. Built on Arti, and onionmasq, oniux drop-ships any Linux program into its own network namespace to route it through Tor and strips away the potential for data leaks. If your work, activism, or research demands rock-solid traffic isolation, oniux delivers it.

# What are Linux namespaces? ð§

Namespaces are an isolation feature found in the Linux kernel that were introduced around the year 2000. They provide a secure way of isolating a certain part of an application from the rest of the system. Namespaces come in various forms and shapes. Some examples include network namespaces, mount namespaces, process namespaces, and a few more; each of them isolating a certain amount of system resources from an application.

What do we mean by **system resources**? In Linux, system resources are available globally by all applications on the system. The most notable example of this is probably your operating system clock, but there are many other areas as well, such as the list of all processes, the file system, and the list of users.

Namespaces *containerize* a certain part of an application from the rest of the operating system; this is exactly what Docker uses in order to provide its isolation primitives.

# Tor + Namespaces = â¤ï¸

As outlined above, namespaces are a powerful feature that gives us the ability to isolate Tor network access of an arbitrary application. We put each application in a network namespace that doesn't provide access to system-wide network interfaces (such as eth0), and instead provides a custom network interface onion0.

This allows us to isolate an arbitrary application over Tor in the most secure way possible software-wise, namely by relying on a security primitive offered by the operating system kernel. Unlike SOCKS, the application cannot accidentally leak data by failing to make some connection via the configured SOCKS, which may happen due to a mistake by the developer.

# oniux vs. torsocks

You may have also heard of a tool with a similar goal, known as
[`torsocks`](https://gitlab.torproject.org/tpo/core/torsocks), which works by
overwriting all network-related libc functions in a way to route traffic over a
SOCKS proxy offered by Tor. While this approach is a bit more cross-platform,
it has the notable downside that applications making system calls *not* through
a dynamically linked libc, either with malicious intent or not, will leak data.
Most notably, this excludes support for purely static binaries and applications
from the Zig ecosystem.

The following provides a basic comparison on *oniux* vs *torsocks*:

| *oniux* | *torsocks* |
| --- | --- |
| Standalone application | Requires running Tor daemon |
| Uses Linux namespaces | Uses an ld.so preload hack |
| Works on all applications | Only works on applications making system calls through libc |
| Malicious application cannot leak | Malicious application can leak by making a system call through raw assembly |
| Linux only | Cross-platform |
| New and experimental | Battle-proven for over 15 years |
| Uses Arti as its engine | Uses CTor as its engine |
| Written in Rust | Written in C |

# How can I use *oniux*? ð§

First, you need a Linux system with a Rust toolchain installed.
Afterwards, you can install *oniux* with the following command:

```
$ cargo install --git https://gitlab.torproject.org/tpo/core/oniux --tag v0.4.0 oniux
```

Once that is done, you are ready to go for using *oniux*! ð

Using *oniux* is straightforward:

```
# Perform a simple HTTPS query using oniux!
$ oniux curl https://icanhazip.com
<A TOR EXIT NODE IP ADDRESS>

# oniux also supports IPv6 of course!
$ oniux curl -6 https://ipv6.icanhazip.com
<A TOR EXIT NODE IPv6 ADDRESS>

# Tor without onion services is like a car without an engine ...
$ oniux curl http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/index.html

# You can also enable logging if you are a nerd. ð¤
$ RUST_LOG=debug oniux curl https://icanhazip.com

# If you want, you can "torify" your entire shell, isolating all processes within!
$ oniux bash

# If you are in a desktop environment, you can isolate graphical applications too!
$ oniux hexchat
```

# How does this work internally? âï¸

*oniux* works by immediately spawning a child process using the `clone(2)`
system call, which is isolated in its own network, mount, PID, and user
namespace. This process then mounts its own copy of `/proc` followed by UID
and GID mappings to the respective UID and GID of the parent process.

Afterwards, it creates a temporary file with nameserver entries which will then
be bind mounted onto `/etc/resolv.conf`, so that applications running within
will use a custom name resolver that supports resolving through Tor.

Next, the child process utilizes
[onionmasq](https://gitlab.torproject.org/tpo/core/onionmasq) to create a TUN
interface named `onion0` followed by some `rtnetlink(7)` operations required to
set up the interface, such as assigning IP addresses.

Then, the child process sends the file descriptor of the TUN interface over
a Unix Domain socket to the parent process, who has been waiting for this
message ever since executing the initial `clone(2)`.

Once that is done, the child process drops all of its capabilities which
were acquired as part of being the root process in the user namespace.

Finally, the command supplied by the user is executed using facilities
provided by the Rust standard library.

# *oniux* is experimental â ï¸

Although this section should not discourage you from using *oniux*, you should
keep in mind that this is a relatively new feature which uses new Tor software,
such as *Arti* and *onionmasq*.

While things are already working as expected at the moment, tools such as
*torsocks* have been around for over 15 years, giving them more experience on
the battlefield.

But we do want to reach a similar state with oniux, so please go ahead and
check it out!

# Credits

Many thanks to the developers of
[`smoltcp`](https://github.com/smoltcp-rs/smoltcp), which is a Rust crate that
implements a full IP stack in Rust -- something, we make heavy use of.

Also many thanks go to `7ppKb5bW`, who taught us on how this can implemented
without the use of `capabilities(7)` by using `user_namespaces(7)` properly.

Last but not least, many thanks to all people and organizations who support Tor financially. The Tor Project, Inc. is a 501(c)(3) nonprofit advancing human rights and defending privacy online through free software and open networks. The oniux release is powered by a community of supporters. Please consider donating today to continue advancing our work that makes privacy possible.

[![Donate Button](/introducing-oniux-tor-isolation-using-linux-namespaces/button-large-black.png)](https://torproject.org/donate/donate-bp2-sc2025)

* [announcements](/category/announcements)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/introducing-oniux-tor-isolation-using-linux-namespaces/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/introducing-oniux-tor-isolati...