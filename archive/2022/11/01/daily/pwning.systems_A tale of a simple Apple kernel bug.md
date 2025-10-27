---
title: A tale of a simple Apple kernel bug
url: https://pwning.systems/posts/easy-apple-kernel-bug/
source: pwning.systems
date: 2022-11-01
fetch_date: 2025-10-03T21:24:41.254369
---

# A tale of a simple Apple kernel bug

[pwning.systems](/)

menu

* [About](/about)
* [Bugs](/bugs)
* [Links](/links)
* [RSS](/index.xml)

* [About](/about)
* [Bugs](/bugs)
* [Links](/links)
* [RSS](/index.xml)

# [A tale of a simple Apple kernel bug](https://pwning.systems/posts/easy-apple-kernel-bug/)

2022-10-31
:: Jordy Zomer

#[kernel](https://pwning.systems/tags/kernel/)
#[apple](https://pwning.systems/tags/apple/)
#[vulnerability](https://pwning.systems/tags/vulnerability/)

Earlier this year, I discovered a flaw in [XNU](https://en.wikipedia.org/wiki/XNU), which is the kernel that Apple uses on both macOS and iOS. While it’s not a particularly complicated flaw, I wanted to explain how I discovered it and how it works, both so that I can motivate others and so that they can learn from my discovery.

Within the [memdev.c](https://github.com/apple-open-source/macos/blob/master/xnu/bsd/dev/memdev.c) file (the ramdisk device driver), I found the source of the vulnerability, which was a write/read operation that exceeded the allowed range. Why are ramdisks such an intriguing target to look at? If you identify a bug in the driver, it may give you the ability to execute code in the kernel. Additionally, on some systems, you may be able to construct ramdisks with particular settings such that it is mapped to [physical memory](https://en.wikibooks.org/wiki/Operating_System_Design/Physical_Memory), which may give you the ability to read and write data to physical memory.

In order for us to understand the bug, we will first have to figure out what `uimove` is.

Data can be moved between user space and kernel space with the help of the `uiomove()` function. To a large extent, it is comparable to an I/O vector.

The `uimove()` function requires three parameters: the location of the destination buffer, the size of the buffer, and a pointer to the `uio` structure.

The `uio` structure looks like this:

```
struct uio	{
     struct  iovec *uio_iov;	     /*	scatter/gather list */
     int     uio_iovcnt;	     /*	length of scatter/gather list */
     off_t   uio_offset;	     /*	offset in target object	*/
     ssize_t uio_resid;		     /*	remaining bytes	to copy	*/
     enum    uio_seg uio_segflg;     /*	address	space */
     enum    uio_rw uio_rw;	     /*	operation */
     struct  thread *uio_td;	     /*	owner */
};
```

Once you know how this function works, you can probably foresee the potential problems that could arise. For example what happens when you put a size argument that’s bigger than the destination buffer. This is what I started searching for.

When we take a look at the `uio` struct, we notice that it contains two fields that relevant to our interest: `uio_resid` and `uio_offset`. Where `uio_resid` refers to the number of bytes that still need to be copied and `uio_offset` specifies the position inside the buffer that will be used as the destination.

Therefore, the first thing that I would try would be to search for locations where `uio_resid` is used in the size parameter. And this is when [Weggli](https://github.com/googleprojectzero/weggli) entered the picture!

I started exploring with a simple weggli query like this:

`weggli -u -R func=uiomove '$func(_,_,_);' ./`

This would search for all calls to functions that contain the word `uiomove` anywhere in the name of the function. This gave a bunch of results, but I was too lazy to go through them manually.

After that, I attempted to make the query a little more specific by checking to see if the word `resid` was included in the size argument anywhere. Unfortunately, this did not provide any results; however, after a little bit of fiddling around, I discovered that it produces results if the `resid` variable is included in a sub-expression of the size argument like seen here:

`weggli -u -R func=uiomove -R 'resid=resid' '$func(_,_($resid),_);' ./`

This gave two results, one of them containing `min()` so I didn’t bother looking at that. The other one however seemed promising:

```
./xnu/./bsd/dev/memdev.c:208
static int
mdevrw(dev_t dev, struct uio *uio, __unused int ioflag)
..
                        uio->uio_segflg = UIO_PHYS_USERSPACE32;
                } else {
                        uio->uio_segflg = UIO_PHYS_USERSPACE;
                }
        }
        status = uiomove64(mdata, (int)uio_resid(uio), uio);    /* Move the data */
        uio->uio_segflg = saveflag;                                                     /* Restore the flag */

        return status;
}
```

So the [mdevrw](https://github.com/apple-open-source/macos/blob/master/xnu/bsd/dev/memdev.c#L209) function appears to use something with `resid` in the size argument. However it’s not using `uio->uio_resid`, apparently `uio_resid()` is just a macro that returns `uio->uio_resid`. So that works as well :')

So I took a look at the memdev driver’s mdevrw function.

```
static int
mdevrw(dev_t dev, struct uio *uio, __unused int ioflag)
{
        int                     status;
        addr64_t                mdata;
        int                     devid;
        enum uio_seg    saveflag;

        devid = minor(dev);                                                                     /* Get minor device number */

        if (devid >= NB_MAX_MDEVICES) {
                return ENXIO;                                                                 /* Not valid */
        }
        if (!(mdev[devid].mdFlags & mdInited)) {
                return ENXIO;                                 /* Have we actually been defined yet? */
        }
        mdata = ((addr64_t)mdev[devid].mdBase << 12) + uio->uio_offset; /* Point to the area in "file" */

        saveflag = uio->uio_segflg;                                                     /* Remember what the request is */
#if LP64_DEBUG
        if (UIO_IS_USER_SPACE(uio) == 0 && UIO_IS_SYS_SPACE(uio) == 0) {
                panic("mdevrw - invalid uio_segflg");
        }
#endif /* LP64_DEBUG */
        /* Make sure we are moving from physical ram if physical device */
        if (mdev[devid].mdFlags & mdPhys) {
                if (uio->uio_segflg == UIO_USERSPACE64) {
                        uio->uio_segflg = UIO_PHYS_USERSPACE64;
                } else if (uio->uio_segflg == UIO_USERSPACE32) {
                        uio->uio_segflg = UIO_PHYS_USERSPACE32;
                } else {
                        uio->uio_segflg = UIO_PHYS_USERSPACE;
                }
        }
        status = uiomove64(mdata, (int)uio_resid(uio), uio);    /* Move the data */
        uio->uio_segflg = saveflag;                                                     /* Restore the flag */

        return status;
}
```

When we examine this function, we can plainly see that there is no size check, which indicates that we are dealing with a read and a write of an arbitrary size to and from the kernel (This is because the user decides wether they want to read or write, based on the syscall they use).

Next to that there’s one other thing that sparked my interest, did you see this line?

`mdata = ((addr64_t)mdev[devid].mdBase << 12) + uio->uio_offset;`

Yes, that’s right. It doesn’t perform any size checks, but it still uses the user-provided offset to figure out where the destination is.

At this point, it appears that we are dealing with an issue that involves reading and writing data on an arbitrary offset of an arbitrary size. Looks like a textbook bug!

Simply opening the device, reading from it, or writing to it will cause this problem to be triggered. The only catch is that you need to have unsandboxed code execution and be logged in as root in order to be able to exploit this problem. Therefore, it’s not a severe issue, but it might be beneficial nonetheless in a full-chain

After I reported this problem to Apple, I happened to come across a proof-of-concept [tweet](https://twitter.com/littlelailo/status/1518613427480145922) for the bug on Twitter because someone was diffing the patches which was fun.

The vulnerability, which is now known as CVE-2022-267...