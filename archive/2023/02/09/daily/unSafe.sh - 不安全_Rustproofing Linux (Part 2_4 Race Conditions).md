---
title: Rustproofing Linux (Part 2/4 Race Conditions)
url: https://buaq.net/go-148547.html
source: unSafe.sh - 不安全
date: 2023-02-09
fetch_date: 2025-10-04T06:05:11.289476
---

# Rustproofing Linux (Part 2/4 Race Conditions)

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

![]()

Rustproofing Linux (Part 2/4 Race Conditions)

This is a four part blog post series that starts with Rustproofing Linux (Part 1/4 Leaking Addre
*2023-2-8 23:41:37
Author: [research.nccgroup.com(查看原文)](/jump-148547.htm)
阅读量:30
收藏*

---

This is a four part blog post series that starts with [Rustproofing Linux (Part 1/4 Leaking Addresses)](https://research.nccgroup.com/?p=18577).

This post uses a simple example to demonstrate a class of vulnerability that
we encounter quite frequently when auditing kernel drivers and firmware.
It’s a race condition, or more precisely a TOCTOU vulnerability.

The [complete
vulnerable C driver](https://github.com/nccgroup/rustproofing-linux/blob/main/vuln_race_device.c) is a bit more complex, but the parts that are
most relevant to the vulnerability are shown below:

```
struct file_state {
    u8 *buf;
    size_t buf_size;
};

static ssize_t vuln_write(struct file *filp, const char __user *buf, size_t count, loff_t *offset)
{
    struct file_state *state = filp->private_data;

    if (count == 0)
        return 0;

    if (state->buf_size < count)
        return -ENOSPC;

    if (copy_from_user(state->buf, buf, count) != 0)
        return -EFAULT;

    return count;
}

static long vuln_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)
{
    struct file_state *state = filp->private_data;

    switch (cmd) {
    case VULN_SETUP_BUF:
        if (arg == 0)
            return -EINVAL;

        state->buf = krealloc(state->buf, arg, GFP_KERNEL);
        if (state->buf == NULL)
            return -ENOMEM;

        state->buf_size = arg;
    }

    pr_err("error: wrong ioctl command: %#x\n", cmd);
    return -EINVAL;
}
```

C driver vulnerable to a race condition between
`ioctl` and `write` operations

Quickly summarised, the `vuln_write` function checks that
the kernel buffer is large enough to hold the attacker-provided
userspace data, then copies the data into the buffer. The
`vuln_ioctl` function reallocates a new buffer and sets its
size.

This would be fine, if only one thread calls these functions, but if
they’re called concurrently, a small buffer could be allocated in
`vuln_ioctl` while another thread is already processing
`vuln_write` and has successfully proceeded past the
`buf_size` check. There are a few variations how to trigger a
bug, but the root cause is the same – shared data is not properly
synchronised between threads.

If we run our [PoC](https://github.com/nccgroup/rustproofing-linux/blob/main/poc/poc_vuln_race_device.c)
for the C-language vulnerability, KASAN will complain as expected:

```
root@(none):/# /xxx/rustproofing-linux/poc/test.sh vuln_race_device
[   81.997668] vuln_race_device: loading out-of-tree module taints kernel.
[   82.032372] ==================================================================
[   82.034436] BUG: KASAN: slab-out-of-bounds in _copy_from_user+0x35/0x70
[   82.036122] Write of size 40 at addr ffff888001eacf00 by task poc_vuln_race_d/191
[...]
[   82.052548]  kasan_report+0xc1/0xf0
[   82.053580]  ? _copy_from_user+0x35/0x70
[   82.054706]  kasan_check_range+0x2bd/0x2e0
[   82.055881]  _copy_from_user+0x35/0x70
[   82.056919]  vuln_write+0x5b/0x80 [vuln_race_device]
```

PoC demonstrating an out of bounds write caused by a race
condition

The above problem may sound rather obvious, but we should keep in
mind many device drivers are often designed to be used by only one
process/thread, and testing might not cover even the simplest
multithreaded cases. As a result, this class of vulnerability is quite
prevalent in Linux kernel drivers.

The [fix](https://github.com/nccgroup/rustproofing-linux/blob/main/vuln_race_device_fixed.c)
is to simply add a mutex and make sure all operations on
`buf_size` and `buf` happen while the lock is
held.

## Porting to Rust With `Atomic`s

A [naïve
port](https://github.com/nccgroup/rustproofing-linux/blob/main/rust_vuln_race_device_v2_nocompile.rs) to Rust won’t even compile since the first argument to
`ioctl`/`write` isn’t mutable. The trick is to use
interior mutability, and simplest way to do this is to use atomics. The
above code could be [translated
into something](https://github.com/nccgroup/rustproofing-linux/blob/main/rust_vuln_race_device_v3_atomics.rs) that looks like the following:

```
struct RustVuln {
    buf: AtomicPtr<core::ffi::c_void>,
    buf_size: AtomicUsize,
}

    fn write(state: &Self, _: &File, data: &mut impl IoBufferReader, _offset: u64) -> Result<usize> {
        if data.is_empty() {
            return Ok(0);
        }

        if state.buf_size.load(Ordering::Relaxed) < data.len() {
            return Err(ENOSPC);
        }

        // SAFETY: 'buf' is allocated and big enough ('buf_size' check)
        unsafe { data.read_raw(state.buf.load(Ordering::Relaxed) as *mut u8, data.len())?; }

        Ok(data.len())
    }

    fn ioctl(state: &Self, _: &File, cmd: &mut IoctlCommand) -> Result<i32> {
        let (cmd, arg) = cmd.raw();
        match cmd {
            VULN_SETUP_BUF => {
                if arg == 0 {
                    return Err(EINVAL)
                }

                // SAFETY: only calling C's krealloc
                let newbuf = unsafe { bindings::krealloc(state.buf.load(Ordering::Relaxed), arg, bindings::GFP_KERNEL) };
                state.buf.store(newbuf, Ordering::Relaxed);
                state.buf_size.store(arg, Ordering::Relaxed);

                Ok(0)
            }
            _ => {
                pr_err!("error: wrong ioctl command: {:#x}\n", cmd);
                Err(EINVAL)
            }
        }
    }
```

Rust version of the driver with the same
vulnerability

The above code is a good example of how not to use atomics, so
hopefully readers of this blog post will not be tempted to do this. Of
course, this Rust version also exhibits the same buggy behaviour as the
C version. It should be clear that naïve ports to Rust require careful
management of critical sections or else race conditions may still
arise.

## Porting to Rust With a `Mutex`

Interior mutability (and thread safety) could also be achieved by
guarding data with a [Mutex](https://rust-for-linux.github.io/docs/kernel/sync/struct.Mutex.html).

Rust mutex syntax is quite neat. Data guarded by the mutex can only
ever be accessed when the mutex is locked, since the data is contained
inside the mutex. So I rewrote this driver to use Mutexes, which can be
seen in the [following
example](https://github.com/nccgroup/rustproofing-linux/blob/main/rust_vuln_race_device_v4_mutex.rs). Look for `.lock()` to see where the mutex is
locked:

```
struct RustVulnState {
    buf: *mut core::ffi::c_void,
    buf_size: usize,
}
// SAFETY: only used within Mutex, so it's safe to be accessed from multiple threads
unsafe impl Send for RustVulnState {}

struct RustVuln {
    mutable: Mutex<RustVulnState>,
}

    fn write(state: &Self, _: &File, data: &mut impl IoBufferReader, _offset: u64) -> Result<usize> {
        if data.is_empty() {
            return Ok(0);
        }

        if state.mutable.lock().buf_size < data.len() {
            return Err(ENOSPC);
        }

        // SAFETY: 'buf' is allocated and big enough ('buf_size' check)
        unsafe { data.read_raw(state.mutable.lock().buf as _, data.len())?; }

        Ok(data.len())
    }

    fn ioctl(state: &Self, _: &File, cmd: &mut IoctlCommand) -> Result<i32> {
        let (cmd, arg) = cmd.raw();
        match cmd {
            VULN_SETUP_BUF => {
                if arg == 0 {
                    return Err(EINVAL)
                }

                let mut mutable = state.mutable.lock();
                // SAFETY: onl...