---
title: Solo: A Pixel 6 Pro Story (When one bug is all you need)
url: https://starlabs.sg/blog/2025/06-solo-a-pixel-6-pro-story-when-one-bug-is-all-you-need/
source: Blogs on STAR Labs
date: 2025-06-06
fetch_date: 2025-10-06T22:51:50.635328
---

# Solo: A Pixel 6 Pro Story (When one bug is all you need)

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Solo: A Pixel 6 Pro Story (When one bug is all you need)

June 5, 2025 · 36 min · Lin Ze Wei

Table of Contents

* [Table of Contents](#table-of-contents)
* [Root Cause Analysis](#root-cause-analysis)
  + [CVE-2023-48409](#cve-2023-48409)
  + [What is `CONFIG_HARDENED_USERCOPY`?](#what-is-config_hardened_usercopy)
  + [The Missing Piece: CVE-2023-26083](#the-missing-piece-cve-2023-26083)
* [One Bug to Root](#one-bug-to-root)
  + [Physmap Spraying](#physmap-spraying)
  + [Pagetable Spraying](#pagetable-spraying)
  + [From Physical to Virtual: Converting Our Primitive](#from-physical-to-virtual-converting-our-primitive)
* [Android’s Unique Challenges](#androids-unique-challenges)
  + [Bypassing Android’s App Sandbox](#bypassing-androids-app-sandbox)
  + [Disabling SELinux Enforcement](#disabling-selinux-enforcement)
* [A Surprise Discovery](#a-surprise-discovery)
  + [Understanding the Timeline Stream Leak](#understanding-the-timeline-stream-leak)
  + [Command Stream Frontend](#command-stream-frontend)
  + [The Golden Object: `kbase_context`](#the-golden-object-kbase_context)
  + [Cleaning Up: Making the Exploit Practical](#cleaning-up-making-the-exploit-practical)
* [Conclusion](#conclusion)
* [References](#references)

During my internship I was tasked to analyze a [Mali GPU exploit](https://github.com/0x36/Pixel_GPU_Exploit) on Pixel 7/8 devices and adapt it to make it work on another device: the Pixel 6 Pro.

While the exploit process itself is relatively straightforward to reproduce (in theory we just need to find the correct symbol offsets and signatures for our target device), what’s interesting about Pixel 6 Pro is that [it uses a different Mali GPU from the Pixel 7/8](https://github.com/0x36/Pixel_GPU_Exploit/issues/6), which lacked support for a feature that one of the two vulnerabilities within the exploit relied on:

![pixel-6-issue](/blog/2025/images/Solo-A-Pixel-6-Pro-Story-01.png)

But wait, do we actually need both bugs to work?

## Table of Contents[#](#table-of-contents)

* [Root Cause Analysis](#root-cause-analysis)
  + [CVE-2023-48409](#cve-2023-48409)
  + [What is `CONFIG_HARDENED_USERCOPY`?](#what-is-config_hardened_usercopy)
  + [The Missing Piece: CVE-2023-26083](#the-missing-piece-cve-2023-26083)
* [One Bug to Root](#one-bug-to-root)
  + [Physmap Spraying](#physmap-spraying)
  + [Pagetable Spraying](#pagetable-spraying)
  + [From Physical to Virtual: Converting Our Primitive](#from-physical-to-virtual-converting-our-primitive)
* [Android’s Unique Challenges](#androids-unique-challenges)
  + [Bypassing Android’s App Sandbox](#bypassing-androids-app-sandbox)
  + [Disabling SELinux Enforcement](#disabling-selinux-enforcement)
* [A Surprise Discovery](#a-surprise-discovery)
  + [Understanding the Timeline Stream Leak](#understanding-the-timeline-stream-leak)
  + [Command Stream Frontend](#command-stream-frontend)
  + [The Golden Object: `kbase_context`](#the-golden-object-kbase_context)
  + [Cleaning Up: Making the Exploit Practical](#cleaning-up-making-the-exploit-practical)
* [Conclusion](#conclusion)
* [References](#references)

## Root Cause Analysis[#](#root-cause-analysis)

### CVE-2023-48409[#](#cve-2023-48409)

Here, we will first be taking a deep dive into the *other* vulnerability: CVE-2023-48409, which seems to be more readily exploitable. This CVE is covered in the [December 2023 Pixel Security Bulletin](https://source.android.com/docs/security/bulletin/pixel/2023-12-01); referencing the internal Bug ID, we can actually locate the [exact patch](https://android.googlesource.com/kernel/google-modules/gpu/%2B/5dec6c2a0b1693a51f7a5ab8c8667fb545e535ac%5E%21/#F0) for our device, verifying that the vulnerability is indeed fixed for December 2023 SPL onwards. As such, we will be rolling back our device version to an earlier patch, `UP1A.231005.007` in our case:

```
raven:/ $ uname -a
Linux localhost 5.10.157-android13-4-00001-g5c7ff5dc7aac-ab10381520 #1 SMP PREEMPT Fri Jun 23 18:30:49 UTC 2023 aarch64 Toybox
raven:/ $ getprop ro.build.fingerprint
google/raven/raven:14/UP1A.231005.007/10754064:user/release-keys
```

From the [description](https://nvd.nist.gov/vuln/detail/cve-2023-48409):

> In `gpu_pixel_handle_buffer_liveness_update_ioctl` of `private/google-modules/gpu/mali_kbase/mali_kbase_core_linux.c`, there is a possible out of bounds write due to an integer overflow. This could lead to local escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.

The vulnerability is caused by an integer overflow when calculating the size of a kernel object allocated in preparation for an operation (very descriptively, handling a liveness update) within the GPU driver:

```
int gpu_pixel_handle_buffer_liveness_update_ioctl(struct kbase_context* kctx,
                                                  struct kbase_ioctl_buffer_liveness_update* update)
{
	int err = 0;
	struct gpu_slc_liveness_update_info info;
	u64* buff;

	/* Compute the sizes of the user space arrays that we need to copy */
	u64 const buffer_info_size = sizeof(u64) * update->buffer_count;			// [1]
	u64 const live_ranges_size =
	    sizeof(struct kbase_pixel_gpu_slc_liveness_mark) * update->live_ranges_count;
	/* Nothing to do */
	if (!buffer_info_size || !live_ranges_size)
		goto done;

	/* Guard against nullptr */
	if (!update->live_ranges_address || !update->buffer_va_address || !update->buffer_sizes_address)
		goto done;
	/* Allocate the memory we require to copy from user space */
	buff = kmalloc(buffer_info_size * 2 + live_ranges_size, GFP_KERNEL);			// [2]

	/* Set up the info struct by pointing into the allocation. All 8 byte aligned */
	info = (struct gpu_slc_liveness_update_info){						// [3]
	    .buffer_va = buff,
	    .buffer_sizes = buff + update->buffer_count,
	    .live_ranges = (struct kbase_pixel_gpu_slc_liveness_mark*)(buff + update->buffer_count * 2),
	    .live_ranges_count = update->live_ranges_count,
	};
	/* Copy the data from user space */
	err =
	    copy_from_user(info.live_ranges, u64_to_user_ptr(update->live_ranges_address), live_ranges_size);
	if (err) {
		dev_err(kctx->kbdev->dev, "pixel: failed to copy live ranges");
		err = -EFAULT;
		goto done;									// [4]
	}

...

done:
	kfree(buff);
	return err;
}
```

Specifically, we are able to specify two `u64`s: `buffer_count` and `live_ranges_count`, such that the driver allocates an object via `kmalloc(GFP_KERNEL)` ([2]), which is supposed to house 3 consecutive buffers, all of which are directly user-controllable ([3]):

* `buffer_sizes`, with size `sizeof(u64) * buffer_count`
* `buffer_va`, with size `sizeof(u64) * buffer_count`
* `live_ranges`, with size `sizeof(struct kbase_pixel_gpu_slc_liveness_mark) * update->live_ranges_count` (the struct is 4 bytes)

Focusing on the `live_ranges` buffer:

* Allocated object size: `8*buffer_count*2 + 4*live_ranges_count` ([1] and [2])
* Offset from allocated object: `+ 8*buffer_count*2` ([1] and [3])

In this case, if the values are crafted such that `8*buffer_count*2 + 4*live_ranges_count = (1<<64) + <object_size>`, our `live_ranges` buffer will be located `4*live_ranges_count - <object_size>` bytes before the allocated object. And fortunately since `live_ranges` is written to first, we can cause an invalid memory access midway through the write to abort the whole operation early without writing to the other two buffers (which have very blatantly invalid bounds) ...