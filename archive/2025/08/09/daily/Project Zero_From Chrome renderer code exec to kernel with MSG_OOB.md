---
title: From Chrome renderer code exec to kernel with MSG_OOB
url: https://googleprojectzero.blogspot.com/2025/08/from-chrome-renderer-code-exec-to-kernel.html
source: Project Zero
date: 2025-08-09
fetch_date: 2025-10-07T00:47:48.730681
---

# From Chrome renderer code exec to kernel with MSG_OOB

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Friday, August 8, 2025

### From Chrome renderer code exec to kernel with MSG\_OOB

Posted by Jann Horn, Google Project Zero

# Introduction

In early June, I was reviewing a new Linux kernel feature when I learned about the MSG\_OOB feature supported by stream-oriented UNIX domain sockets. I reviewed the implementation of MSG\_OOB, and discovered [a security bug](https://project-zero.issues.chromium.org/issues/423023990) (CVE-2025-38236) affecting Linux >=6.9. I reported the bug to Linux, and it [got fixed](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id%3D32ca245464e1479bfea8592b9db227fdc1641705). Interestingly, while the MSG\_OOB feature is not used by Chrome, it was exposed in the Chrome renderer sandbox. (Since then, sending MSG\_OOB messages [has been blocked in Chrome renderers](https://chromium-review.googlesource.com/c/chromium/src/%2B/6711812) in response to this issue.)

The bug is pretty easy to trigger; the following sequence results in UAF:

char dummy;

int socks[2];

socketpair(AF\_UNIX, SOCK\_STREAM, 0, socks);

send(socks[1], "A", 1, MSG\_OOB);

recv(socks[0], &dummy, 1, MSG\_OOB);

send(socks[1], "A", 1, MSG\_OOB);

recv(socks[0], &dummy, 1, MSG\_OOB);

send(socks[1], "A", 1, MSG\_OOB);

recv(socks[0], &dummy, 1, 0);

recv(socks[0], &dummy, 1, MSG\_OOB);

I was curious to explore how hard it is to actually exploit such a bug from inside the Chrome Linux Desktop renderer sandbox on an x86-64 Debian Trixie system, escalating privileges directly from native code execution in the renderer to the kernel. Even if the bug is reachable, how hard is it to find useful primitives for heap object reallocation, delay injection, and so on?

The exploit code [is posted on our bugtracker](https://project-zero.issues.chromium.org/423023990#attachment67577205); you may want to reference it while following along with this post.

# Backstory: The feature

Support for using MSG\_OOB with AF\_UNIX stream sockets was added in 2021 with [commit 314001f0bf92 ("af\_unix: Add OOB support", landed in Linux 5.15)](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id%3D314001f0bf92). With this feature, it is possible to send a single byte of "out-of-band" data that the recipient can read ahead of the rest of the data. The feature is very limited - out-of-band data is always a single byte, and there can only be a single pending byte of out-of-band data at a time. (Sending two out-of-band messages one after another causes the first one to be turned into a normal in-band message.) This feature is used almost nowhere except in Oracle products, as discussed on [an email thread](https://lore.kernel.org/netdev/bef45d8e-35b7-42e4-bf6c-768da5b6d8f2%40oracle.com/) from 2024 where removal of the feature was proposed; yet it is enabled by default when AF\_UNIX socket support is enabled in the kernel config, and it wasn't even possible to disable MSG\_OOB support until [commit 5155cbcdbf03 ("af\_unix: Add a prompt to CONFIG\_AF\_UNIX\_OOB")](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id%3D5155cbcdbf03f207095f9a3794942a25aa7e5f58) landed in December 2024.

Because the Chrome renderer sandbox allows stream-oriented UNIX domain sockets and didn't filter the flags arguments of send()/recv() functions, this esoteric feature was usable inside the sandbox.

When a message (represented by a socket buffer / struct sk\_buff, short SKB) is sent between two connected stream-oriented sockets, the message is added to the ->sk\_receive\_queue of the receiving socket, which is a linked list. An SKB has a length field ->len describing the length of data contained within it (counting both data in the SKB's "head buffer" as well as data indirectly referenced by the SKB in other ways). An SKB also contains some scratch space that can be used by the subsystem currently owning the SKB (char cb[48] in struct sk\_buff); UNIX domain sockets access this scratch space with the helper #define UNIXCB(skb) (\*(struct unix\_skb\_parms \*)&((skb)->cb)), and one of the things they store in there is a field u32 consumed which stores the number of bytes of the SKB that have already been read from the socket. UNIX domain sockets count the remaining length of an SKB with the helper unix\_skb\_len(), which returns skb->len - UNIXCB(skb).consumed.

MSG\_OOB messages (sent with something like send(sockfd, &message\_byte, 1, MSG\_OOB), which goes through queue\_oob() in the kernel) are also added to the ->sk\_receive\_queue just like normal messages; but to allow the receiving socket to access the latest out-of-band message ahead of the rest of the queue, the ->oob\_skb pointer of the receiving socket is updated to point to this message. When the receiving socket receives an OOB message with something like recv(sockfd, &received\_byte, 1, MSG\_OOB) (implemented in unix\_stream\_recv\_urg()), the corresponding socket buffer stays on the ->sk\_receive\_queue, but its consumed field is incremented, causing its remaining length (unix\_skb\_len()) to become 0, and the ->oob\_skb pointer is cleared; the normal receive path will have to deal with this when encountering the remaining-length-0 SKB.

This means that the normal recv() path (unix\_stream\_read\_generic()), which runs when recv() is called without MSG\_OOB, must be able to deal with remaining-length-0 SKBs and must take care to clear the ->oob\_skb pointer when it deletes an OOB SKB. manage\_oob() is supposed to take care of this. Essentially, when the normal receive path obtains an SKB from the ->sk\_receive\_queue, it calls manage\_oob() to take care of all the fixing-up required to deal with the OOB mechanism; manage\_oob() will then return the first SKB that contains at least 1 byte of remaining data, and manage\_oob() ensures that this SKB is no longer referenced as ->oob\_skb. unix\_stream\_read\_generic() can then proceed as if the OOB mechanism didn't exist.

# Backstory: The bug, and what led to it

In mid-2024, a userspace API inconsistency was discovered, where recv() could spuriously return 0 (which normally signals end-of-file) when trying to read from a socket with a receive queue that contains a remaining-length-0 SKB left behind by receiving an OOB SKB. [The fix for this issue](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id%3D93c99f21db36) introduced two closely related security issues that can lead to UAF; it was marked as fixing a bug introduced by the original MSG\_OOB implementation, but luckily was actually only backported to Linux 6.9.8, so the buggy fix did not land in older LTS kernel branches.

After the buggy fix, manage\_oob() looked as follows:

static struct sk\_buff \*manage\_oob(struct sk\_buff \*skb, struct sock \*sk,

                                  int flags, int copied)

{

        struct unix\_sock \*u = unix\_sk(sk);

        if (!unix\_skb\_len(skb)) {

                struct sk\_buff \*unlinked\_skb = NULL;

                spin\_lock(&sk->sk\_receive\_queue.lock);

                if (copied) {

                        skb = NULL;

                } else if (flags & MSG\_PEEK) {

                        skb = skb\_peek\_next(skb, &sk->sk\_receive\_queue);

                } else {

                        unlinked\_skb = skb;

                        skb = skb\_peek\_next(skb, &sk->sk\_receive\_queue);

                        \_\_skb\_unlink(unlinked\_skb, &sk->sk\_receive\_queue);

                }

                spin\_unlock(&sk->sk\_receive\_queue.lock);

                consume\_skb(unlinked\_skb);

        } else {

                struct sk\_buff \*unlinked\_skb = NULL;

                spin\_lock(&sk->sk\_receive\_queue.lock);

                if (skb == u->oob\_skb) {

                        if (copied) {

                                skb = NULL;

                       ...