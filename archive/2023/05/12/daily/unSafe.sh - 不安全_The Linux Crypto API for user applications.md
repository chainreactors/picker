---
title: The Linux Crypto API for user applications
url: https://buaq.net/go-162927.html
source: unSafe.sh - 不安全
date: 2023-05-12
fetch_date: 2025-10-04T11:38:17.301650
---

# The Linux Crypto API for user applications

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

The Linux Crypto API for user applications

Loading...
*2023-5-11 21:0:58
Author: [blog.cloudflare.com(查看原文)](/jump-162927.htm)
阅读量:28
收藏*

---

Loading...

* [![Oxana Kharitonova](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/Oxana-Kharitonova.png)](https://blog.cloudflare.com/author/oxana/)

![The Linux Crypto API for user applications.](data:image/png;base64...)

In this post we will explore Linux Crypto API for user applications and try to understand its pros and cons.

The Linux Kernel Crypto API was introduced in [October 2002](https://lwn.net/Articles/14197/?ref=blog.cloudflare.com). It was initially designed to satisfy internal needs, mostly for [IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/?ref=blog.cloudflare.com). However, in addition to the kernel itself, user space applications can benefit from it.

If we apply the basic definition of an [API](https://www.cloudflare.com/learning/security/api/what-is-an-api/?ref=blog.cloudflare.com) to our case, we will have the kernel on one side and our application on the other. The application needs to send data, i.e. plaintext or ciphertext, and get encrypted/decrypted text in response from the kernel. To communicate with the kernel we need to make a system call. Also, before starting the data exchange, we need to agree on some cryptographic parameters, at least the selected crypto algorithm and key length. These constraints, along with all supported algorithms, can be found in the `/proc/crypto` virtual file.

Below is a short excerpt from my `/proc/crypto` looking at `ctr(aes)`. In the examples, we will use the AES cipher in CTR mode, further we will give more details about the algorithm itself.

```
name         : ctr(aes)
driver       : ctr(aes-generic)
module       : ctr
priority     : 100
refcnt       : 1
selftest     : passed
internal     : no
type         : skcipher
async        : no
blocksize    : 1
min keysize  : 16
max keysize  : 32
ivsize       : 16
chunksize    : 16
walksize     : 16

name         : ctr(aes)
driver       : ctr(aes-aesni)
module       : ctr
priority     : 300
refcnt       : 1
selftest     : passed
internal     : no
type         : skcipher
async        : no
blocksize    : 1
min keysize  : 16
max keysize  : 32
ivsize       : 16
chunksize    : 16
walksize     : 16

name         : ctr(aes)
driver       : ctr-aes-aesni
module       : aesni_intel
priority     : 400
refcnt       : 1
selftest     : passed
internal     : no
type         : skcipher
async        : yes
blocksize    : 1
min keysize  : 16
max keysize  : 32
ivsize       : 16
chunksize    : 16
walksize     : 16
```

In the output above, there are three config blocks. The kernel may provide several implementations of the same algorithm depending on the CPU architecture, available hardware, presence of crypto accelerators etc.

We can pick the implementation based on the algorithm name or the driver name. The algorithm name is not unique, but the driver name is. If we use the algorithm name, the driver with the highest priority will be chosen for us, which in theory should provide the best cryptographic performance in this context. Let’s see the performance of different implementations of AES-CTR encryption. I use the [libkcapi library](https://github.com/smuellerDD/libkcapi?ref=blog.cloudflare.com): it’s a lightweight wrapper for the kernel crypto API which also provides built-in speed tests. We will examine [these tests](https://github.com/smuellerDD/libkcapi/blob/master/speed-test/cryptoperf-skcipher.c?ref=blog.cloudflare.com#L228-L238).

```
$ kcapi-speed -c "AES(G) CTR(G) 128" -b 1024 -t 10
AES(G) CTR(G) 128   	|d|	1024 bytes|          	149.80 MB/s|153361 ops/s
AES(G) CTR(G) 128   	|e|	1024 bytes|          	159.76 MB/s|163567 ops/s

$ kcapi-speed -c "AES(AESNI) CTR(ASM) 128" -b 1024 -t 10
AES(AESNI) CTR(ASM) 128 |d|	1024 bytes|          	343.10 MB/s|351332 ops/s
AES(AESNI) CTR(ASM) 128 |e|	1024 bytes|         	310.100 MB/s|318425 ops/s

$ kcapi-speed -c "AES(AESNI) CTR(G) 128" -b 1024 -t 10
AES(AESNI) CTR(G) 128   |d|	1024 bytes|          	155.37 MB/s|159088 ops/s
AES(AESNI) CTR(G) 128   |e|	1024 bytes|          	172.94 MB/s|177054 ops/s
```

Here and later ignore the absolute numbers, as they depend on the environment where the tests were running. Rather look at the relationship between the numbers.

The [x86 AES instructions](https://en.wikipedia.org/wiki/AES_instruction_set?ref=blog.cloudflare.com) showed the best results, twice as fast vs the generic portable C implementation. As expected, this implementation has the highest priority in the `/proc/crypto`. We will use only this one later.

This brief introduction can be rephrased as: “I can ask the kernel to encrypt or decrypt data from my application”. But, why do I need it?

## Why do I need it?

In our previous blog post [Linux Kernel Key Retention Service](https://blog.cloudflare.com/the-linux-kernel-key-retention-service-and-why-you-should-use-it-in-your-next-application/) we talked a lot about cryptographic key protection. We concluded that the best Linux option is to store [cryptographic keys](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/?ref=blog.cloudflare.com) in the kernel space and restrict the access to a limited number of applications. However, if all our cryptography is processed in user space, potentially damaging code still has access to the raw key material. We have to think wisely about using the key: what part of the code has access to it, don’t log it accidentally, how the open-source libraries manage it and if the memory is purged after using it. We may need to support a dedicated process to not have a key in network-facing code. Thus, many things need to be done for security, and for each application which works with cryptography. And even after all these precautionary measures, the best of the best are subject to bugs and vulnerabilities. [OpenSSL](https://en.wikipedia.org/wiki/OpenSSL?ref=blog.cloudflare.com), the most known and widely used cryptographic library in user space, [has had a few problems in its security](https://blog.cloudflare.com/cloudflare-is-not-affected-by-the-openssl-vulnerabilities-cve-2022-3602-and-cve-2022-37/).

Can we move all the cryptography to the kernel and help solve these problems? Looks like it! Our [recent patch](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=7984ceb134bf31aa9a597f10ed52d831d5aede14&ref=blog.cloudflare.com) to upstream extended the key types which can be used in symmetric encryption in the Crypto API directly from the Linux Kernel Key Retention Service.

But nothing is free. There will be some overhead for the system calls and data copying between user and kernel spaces. So, the next question is how fast it is.

## Is it fast?

To answer this question we need to have some baseline to compare with. OpenSSL would be the best as it’s used all around the Internet. OpenSSL provides a good composite of toolkits, including C-functions, a console utility and various speed tests. For the sake of equality, we will ignore the built-in tests and write our own tests using OpenSSL C-functions. We want the same data to be processed and the same logic parts to be measured in both cases (Kernel versus OpenSSL).

So, the task: write a benchmark for AES-CTR-128 encrypting data split in chunks. Make implementations for the Kernel Crypto API and OpenSSL.

### About AES-CTR-128

AES stands for [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard?ref=blog.cloudflare.com). It is a bl...