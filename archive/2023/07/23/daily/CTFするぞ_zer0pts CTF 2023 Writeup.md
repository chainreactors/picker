---
title: zer0pts CTF 2023 Writeup
url: https://ptr-yudai.hatenablog.com/entry/2023/07/22/184044
source: CTFするぞ
date: 2023-07-23
fetch_date: 2025-10-04T11:51:41.332215
---

# zer0pts CTF 2023 Writeup

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_source=blogs_topright_button&utm_medium=button&utm_campaign=subscribe_blog)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2023-07-22](https://ptr-yudai.hatenablog.com/archive/2023/07/22)

# [zer0pts CTF 2023 Writeup](https://ptr-yudai.hatenablog.com/entry/2023/07/22/184044)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

# Introduction

This article is my writeups for zer0pts CTF 2023. Thank you for playing!

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20230719/20230719003038.png)

Final Scoreboard

* [Introduction](#Introduction)
* [pwn](#pwn)
  + [aush](#aush)
    - [Background](#Background)
    - [Challenge](#Challenge)
    - [Solution](#Solution)
  + [qjail](#qjail)
    - [Background](#Background-1)
    - [Challenge](#Challenge-1)
    - [Solution](#Solution-1)
  + [BrainJIT](#BrainJIT)
    - [Background](#Background-2)
    - [Challenge](#Challenge-2)
    - [Solution](#Solution-2)
  + [WISE](#WISE)
    - [Background](#Background-3)
    - [Challenge](#Challenge-3)
    - [Solution](#Solution-3)
  + [sharr](#sharr)
    - [Background](#Background-4)
    - [Challenge](#Challenge-4)
    - [Solution](#Solution-4)
  + [Himitsu Note](#Himitsu-Note)
    - [Background](#Background-5)
    - [Challenge](#Challenge-5)
    - [Solution](#Solution-5)
* [reversing](#reversing)
  + [decompile me](#decompile-me)
    - [Background](#Background-6)
    - [Challenge](#Challenge-6)
    - [Solution](#Solution-6)
  + [mimikyu](#mimikyu)
    - [Background](#Background-7)
    - [Challenge](#Challenge-7)
    - [Solution](#Solution-7)
  + [topology](#topology)
    - [Background](#Background-8)
    - [Challenge](#Challenge-8)
    - [Solution](#Solution-8)
  + [fvm](#fvm)
    - [Background](#Background-9)
    - [Challenge](#Challenge-9)
    - [Solution](#Solution-9)
* [crypto](#crypto)
  + [SquareRNG](#SquareRNG)
    - [Background](#Background-10)
    - [Challenge](#Challenge-10)
* [web](#web)
  + [ScoreShare](#ScoreShare)
    - [Background](#Background-11)
    - [Challenge](#Challenge-11)
    - [Solution](#Solution-10)
* [misc](#misc)
  + [NetFS 1](#NetFS-1)
    - [Background](#Background-12)
    - [Challenge](#Challenge-12)
    - [Solution](#Solution-11)
  + [NetFS 2](#NetFS-2)
    - [Background](#Background-13)
    - [Challenge](#Challenge-13)
    - [Solution](#Solution-12)

# pwn

## aush

### Background

It is sometimes frustrating for pwners that the shell cannot be spawned when the environment variables passed to `execve` are corrupted. I wrote a pwn challenge based on this experience.

### Challenge

This program implements simple authentication of a username and password. Both the password and the username are initialized from `/dev/urandom`, so they cannot be predicted.

```
int setup(char *passbuf, size_t passlen, char *userbuf, size_t userlen) {
  int ret, fd;

  // TODO: change it to password/username file
  if ((fd = open("/dev/urandom", O_RDONLY)) == -1)
    return 1;
  ret  = read(fd, passbuf, passlen) != passlen;
  ret |= read(fd, userbuf, userlen) != userlen;
  close(fd);
  return ret;
}
```

All mitigations are enabled.

```
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

### Solution

The [vulnerability](https://d.hatena.ne.jp/keyword/vulnerability) is simple: there is a stack buffer overflow both in the input of the username and password.

```
#define LEN_USER 0x10
#define LEN_PASS 0x20
...
  char inpuser[LEN_USER+1] = { 0 };
  char inppass[LEN_PASS+1] = { 0 };
  char username[LEN_USER] = { 0 };
  char password[LEN_PASS] = { 0 };
...
  /* Check username */
  write(STDOUT_FILENO, "Username: ", 10);
  if (read(STDIN_FILENO, inpuser, 0x200) <= 0)
    return 1;
...
  /* Check password */
  write(STDOUT_FILENO, "Password: ", 10);
  if (read(STDIN_FILENO, inppass, 0x200) <= 0)
    return 1;
```

However, because stack canaries are enabled and we do not have the address, we cannot simply overwrite the return address.

Checking the order of each buffer on the stack, we see that they are arranged in the following order: "username", "input username", "password", "input password". Therefore, if the input username overflows, we can overwrite the password. However, the correct username cannot be overwritten, so we cannot bypass the username authentication.

In addition to the buffer overflow [vulnerability](https://d.hatena.ne.jp/keyword/vulnerability), there is another issue. If authentication fails, a message is displayed using cowsay as follows:

```
  if (memcmp(username, inpuser, LEN_USER) != 0) {
    args[0] = "/usr/games/cowsay";
    args[1] = "Invalid username";
    args[2] = NULL;
    execve(args[0], args, envp);
  }
```

Because `execve` calls cowsay, if authentication fails, the process changes into cowsay and exits. However, if `execve` fails for some reason, the execution will reach the path where the authentication is successful. So, how can we fail `execve`?

`envp` is passed as the third argument to `execve`. The environment variable array is located at the high address of the stack, so we can destroy it with a stack buffer overflow. However, if `envp` is simply destroyed, `execve` to spawn a shell will also fail. It needs to be fixed appropriately.

Therefore, both username and password authentication can be bypassed by the following steps:

1. Overwrite the password with the username input and destroy the environment variable pointer.
2. While sending the password overwritten in step 1, repair the environment variable pointer to an address that can be recognized as a string array.

I controlled the lower 2 or 3 bytes of the environment variable pointer to do this. Alternatively, setting `envp` to NULL in step 2 will also allow the shell's `execve` to work.

[github.com](https://github.com/zer0pts/zer0pts-ctf-2023-public/tree/master/pwn/aush/solution)

## qjail

### Background

Qiling is useful, but there are many things I don't like about it, so I decided to have participants pwn it.

### Challenge

The program has a very simple buffer overflow [vulnerability](https://d.hatena.ne.jp/keyword/vulnerability) as follows.

```
#include <stdio.h>

int main() {
  char name[0x100];
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  puts("Enter something");
  scanf("%s", name);
  return 0;
}
```

However, all mitigations are enabled.

```
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

Of course, we cannot bypass these mitigations. However, the unusual part of this challenge is that Qiling is used to execute the program.

```
#!/usr/bin/env python3
import qiling
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <ELF>")
        sys.exit(1)

    cmd = ['./lib/ld-2.31.so', '--library-path', '/lib', sys.argv[1]]
    ql = qiling.Qiling(cmd, console=False, rootfs='.')
    ql.run()
```

The flag is mounted in the rootfs of Qiling, and there is no need to escape from Qiling.

### Solution

The three mitigations that makes it hard to exploit the [vulnerability](https://d.hatena.ne.jp/keyword/vulnerability) are ASLR, PIE, and Stack Canary. Let's experiment how Qiling treats each of them.

Compile a program that dumps addresses and stack contents, and run it with Qiling.

```
int main(int argc, char **argv) {
  unsigned long buf[2];
  printf("main=%p / system=%p\n", main, system);
  for (int i = 0; i < 8; i++)
    printf("+%02x...