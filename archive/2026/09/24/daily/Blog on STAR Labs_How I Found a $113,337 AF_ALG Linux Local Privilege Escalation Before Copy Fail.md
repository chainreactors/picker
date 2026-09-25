---
title: How I Found a $113,337 AF_ALG Linux Local Privilege Escalation Before Copy Fail
url: https://starlabs.sg/blog/2026/09-how-i-found-a-113337-af_alg-linux-local-privilege-escalation-before-copy-fail/
source: Blog on STAR Labs
date: 2026-09-24
fetch_date: 2026-09-25T06:51:53.985914
---

# How I Found a $113,337 AF_ALG Linux Local Privilege Escalation Before Copy Fail

[![STAR Labs](/images/logo.png)](/)

[About](/about/)
[Services](/services/)
[Advisories](/advisories/)
[Blog](/blog/)
[Achievements](/achievements/)
[Publications](/publications/)
[Team](/team/)
[RSS](/index.xml)

MENU

Research
September 24, 2026
By Muhammad Alifa Ramdhan
19 min read

# How I Found a $113,337 AF\_ALG Linux Local Privilege Escalation Before Copy Fail

In 2025, I found an AF\_ALG vulnerability in the Linux kernel that allowed an ordinary user to escalate privileges to root. This is a retrospective on how I found CVE-2025-39964 and how we developed the exploit, before Copy Fail drew wider attention to AF\_ALG in 2026.

> Muhammad Alifa Ramdhan discovered CVE-2025-39964 while conducting research at STAR Labs. Credit also goes to his colleague Billy Jheng Bing-Jhong, who helped complete the exploit chain. Ramdhan wrote this article for [publication on IDNSEC](https://idnsec.com/research/linux-local-privilege-escalation-with-af-alg/). The vulnerability was responsibly disclosed to Linux kernel maintainers and used as a Google kernelCTF submission, earning a **$113,337.00 USD** reward.

AF\_ALG is a Linux kernel feature that exposes an API for cryptographic encryption and decryption. A userspace program interacts with the API, and the kernel performs the requested operation.

The vulnerability occurs while AF\_ALG handles input from a userspace program. By understanding how that mechanism works, an out-of-bounds access can be exploited to turn an ordinary user into root. The same vulnerability can also be used to escape a Docker container and obtain root on the host. As it turned out, the vulnerable code had been present in Linux since around 2011.

## Linux Kernel Attack Surface

Readers may remember [Copy Fail](https://copy.fail/), disclosed in 2026 and later recognized alongside DirtyFrag for [Best Privilege Escalation Bug at the 2026 Pwnie Awards](https://risky.biz/risky-bulletin-pwnie-awards-2026-winners/). It also uses AF\_ALG, but the bug in this article is different. Copy Fail is a straight-line logic flaw in the AEAD path, while CVE-2025-39964 is a race between writers sharing an AF\_ALG socket. I found this race while reviewing the source around September 2025, before Copy Fail was disclosed.

I work in vulnerability research and spend a great deal of time looking for vulnerabilities in operating systems, including the Linux kernel. At the time, my goal was to use the finding for kernelCTF, a Google program that rewards researchers who can demonstrate an LPE exploit against the latest stable Linux kernel.

To develop a Linux kernel LPE exploit, a researcher first has to audit code and subsystems that form the kernel’s attack surface. For example, the well-known Dirty COW vulnerability was in the `mm` subsystem, while Dirty Pipe was found in `fs/pipe`.

While looking for the next interesting attack surface to audit, I found [AF\_ALG](https://docs.kernel.org/crypto/userspace-if.html). The first thing that caught my attention in its documentation was that AF\_ALG can be reached directly from unprivileged userspace through the socket API. From a kernel exploitation perspective, this is attractive because no privilege or special configuration is required to reach the kernel code. What made it even more interesting to me was that, as far as I could determine, no previous kernelCTF submission had used a vulnerability in AF\_ALG as its entry point.

### Interacting with AF\_ALG

To interact with AF\_ALG, a userspace program calls [`socket(2)`](https://man7.org/linux/man-pages/man2/socket.2.html) to obtain an AF\_ALG socket file descriptor and `bind(2)` to select an algorithm. The following selects AES-CBC through the AF\_ALG API.

```
int tfmfd = socket(AF_ALG, SOCK_SEQPACKET, 0);
struct sockaddr_alg sa = {
      .salg_family = AF_ALG,
      .salg_type = "skcipher", /* symmetric key cipher */
      .salg_name = "cbc(aes)", /* AES in CBC mode */
};
bind(tfmfd, (struct sockaddr *)&sa, sizeof(sa));
```

For AES-CBC, the kernel also needs an AES key, which can be set with `setsockopt()`.

```
unsigned char key[32] = {0}; /* 256 bit key */
setsockopt(tfmfd, SOL_ALG, ALG_SET_KEY, key, sizeof(key));
```

After setting the key, the program calls `accept()`, which returns another file descriptor ready for encryption or decryption operations.

```
int opfd = accept(tfmfd, NULL, 0);
```

The program performs an encryption or decryption operation by calling `sendmsg()` on `opfd`. In the message header’s control field, it can supply the IV and the requested operation, along with the bytes to process.

```
char cbuf[CMSG_SPACE(sizeof(__u32)) +
          CMSG_SPACE(sizeof(struct af_alg_iv) + 16)] = {0};

struct iovec iov = {
    .iov_base = buf,
    .iov_len = 0x1000,
};

struct msghdr msgh = {
    .msg_iov = &iov,
    .msg_iovlen = 1,
    .msg_control = cbuf,
    .msg_controllen = sizeof(cbuf),
};

struct cmsghdr *cmsg = CMSG_FIRSTHDR(&msgh);
cmsg->cmsg_level = SOL_ALG;
cmsg->cmsg_type = ALG_SET_OP;
cmsg->cmsg_len = CMSG_LEN(sizeof(__u32));
*(__u32 *)CMSG_DATA(cmsg) = ALG_OP_ENCRYPT;

cmsg = CMSG_NXTHDR(&msgh, cmsg);
cmsg->cmsg_level = SOL_ALG;
cmsg->cmsg_type = ALG_SET_IV;
cmsg->cmsg_len = CMSG_LEN(sizeof(struct af_alg_iv) + 16);

struct af_alg_iv *alg_iv = (void *)CMSG_DATA(cmsg);
alg_iv->ivlen = 16;
memset(alg_iv->iv, 0x01, 16);

ssize_t n = sendmsg(opfd, &msgh, MSG_MORE);
```

This first `sendmsg()` call initializes the IV, selects encryption with `ALG_OP_ENCRYPT`, and supplies `0x1000` bytes for the kernel to process. The `MSG_MORE` flag tells the kernel that the input is not yet complete, so the program may call `sendmsg()` again and append more data to the previous input. When a later `sendmsg()` call omits `MSG_MORE`, the kernel stops waiting for additional input. The program can then call `read()`, `recv()`, or `recvmsg()` on `opfd` to request the encryption and obtain its result.

## AF\_ALG Internals

I use Linux kernel v6.12.44 as the reference for this analysis because it was the version on which I performed the bug hunting and exploit development. The source discussed below is available in [`crypto/af_alg.c`](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/crypto/af_alg.c?h=v6.12.44), [`crypto/algif_skcipher.c`](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/crypto/algif_skcipher.c?h=v6.12.44), and [`include/crypto/if_alg.h`](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/include/crypto/if_alg.h?h=v6.12.44).

Before going deeper into the source, there is one important point to understand. Calling `sendmsg()` on AF\_ALG does not immediately perform the encryption. The kernel first collects the user-supplied data in a TX scatter-gather list. Only when the user calls `recvmsg()` does the kernel create a crypto request and use the previously collected data as input.

The flow can be simplified as follows:
![AF_ALG data flow from sendmsg until ciphertext is returned to userspace](/blog/2026/images/AF_ALG-Linux-Local-Privilege-Escalation-Before-Copy-Fail-af-alg-data-flow.svg "AF_ALG data flow")

For an `skcipher` algorithm, the initial `sendmsg()` handler is `skcipher_sendmsg()`. It obtains the IV size for the selected cipher and forwards the entire input-handling process to `af_alg_sendmsg()`.

```
unsigned int ivsize = crypto_skcipher_ivsize(tfm);
return af_alg_sendmsg(sock, msg, size, ivsize);
```

This means that most of the machinery that receives user input, allocates buffers, and retains state across `sendmsg()` calls resides in this function:

```
int af_alg_sendmsg(struct socket *sock, struct msghdr *msg,
                   size_t size, unsigned int ivsize)
```

The `msg` parameter holds the user data and control messages, `size` is the length of the input, and `ivsize` is the IV size required by the selected cipher. AES-CBC uses a 16-byte IV regardless of whether the key is AES-128, AES-192, or AES-256.

At the beginning of the function, AF\_ALG processes the cont...