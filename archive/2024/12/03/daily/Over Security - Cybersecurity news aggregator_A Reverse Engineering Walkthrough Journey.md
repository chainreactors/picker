---
title: A Reverse Engineering Walkthrough Journey
url: https://www.hacktivesecurity.com/index.php/2024/11/04/a-reverse-engineering-walkthrough-journey/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-03
fetch_date: 2025-10-06T19:41:37.510724
---

# A Reverse Engineering Walkthrough Journey

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Reverse Engineering](https://www.hacktivesecurity.com/blog/category/reverse-engineering/)
* A Reverse Engineering Walkthrough Journey

[Reverse Engineering](https://www.hacktivesecurity.com/blog/category/reverse-engineering/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/Image-1.jpeg)

\_ [November 4, 2024](https://www.hacktivesecurity.com/blog/2024/11/04/a-reverse-engineering-walkthrough-journey/)\_ [Alessandro Groppo](https://www.hacktivesecurity.com/blog/author/kiks/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2024/11/04/a-reverse-engineering-walkthrough-journey/#respond)

### A Reverse Engineering Walkthrough Journey

## Introduction

This blog post is about a manually Reverse Engineered challenge we have written for this year [NoHat24](https://www.nohat.it/) security conference. The conference was a blast and we also did our best to contribute also with a [worskhop](https://www.nohat.it/workshops#alessandro_groppo) on Linux Kernel Fuzzing.

The challenge is a compiled C/C++ binary that implements a custom TCP protocol that can be reversed and exploited to obtain the flag. The blog post objective is to guide a beginner person with a step by step and detailed walkthrough of the whole Reverse Engineering journey, dealing with a statically compiled binary. For the best experience, it is highly suggested to download the target binary from [here](https://github.com/hacktivesec/nohat24-blog-references/blob/main/re/challenge) and try to replicate described steps.

## The beginning of the journey

First things first, let’s see what our binary is with a simple `file` command:

```
$ file challenge
challenge: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=975594a6398b8d39078294cbd2a09f100dfd6643, for GNU/Linux 3.2.0, stripped
```

We can immediately take some notes on few things that are interesting for the reverse engineering phase: the binary is **static** (e.g. not linked with dynamic libraries) and **stripped** (e.g. no symbols). Both things will make it harder to understand the inner logic of the targeted program.

Also, the `strings` utility suggests that we are dealing with C++ too:

```
$ strings challenge | grep std
# ...
std::bad_alloc
std::bad_array_new_length
std::bad_cast
std::bad_typeid
std::allocator
std::basic_string
std::string
# ...
```

### First approach

After having opened the binary in Ghidra and having identified its `main` function (`FUN_00405b16`) , it is possible to understand the first behaviors through logging strings:

```
undefined8 FUN_00405b16(void)
{
  undefined4 uVar1;
  int iVar2;
  undefined8 uVar3;
  long in_FS_OFFSET;
  undefined4 local_48;
  undefined4 local_44;
  int local_40;
  int local_3c;
  undefined2 local_38;
  undefined2 local_36;
  undefined4 local_34;
  undefined local_28 [24];
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_40 = FUN_00524bf0(2,1,0);
  local_48 = 1;
  uVar1 = FUN_0051b890(0);
  FUN_004cf660(uVar1);
  if (local_40 < 0) {
    uVar3 = FUN_00476a40(&DAT_005caba0,"Failed to create socket");
    FUN_004753c0(uVar3,FUN_00476340);
  }
  else {
    iVar2 = FUN_00524bb0(local_40,1,2,&local_48,4);
    if (iVar2 < 0) {
      uVar3 = FUN_00476a40(&DAT_005caba0,"Failed to setsockopt on socket");
      FUN_004753c0(uVar3,FUN_00476340);
    }
    else {
      thunk_FUN_004ef5e0(&local_38,0,0x10);
      local_38 = 2;
      local_34 = 0;
      local_36 = FUN_005257d0(0x51);
      iVar2 = FUN_005249d0(local_40,&local_38,0x10);
      if (iVar2 < 0) {
        uVar3 = FUN_00476a40(&DAT_005caba0,"Bind failed");
        FUN_004753c0(uVar3,FUN_00476340);
        FUN_005216a0(local_40);
      }
      else {
        iVar2 = FUN_00524a00(local_40,5);
        if (-1 < iVar2) {
          uVar3 = FUN_00476a40(&DAT_005cacc0,"Server listening..");
          FUN_004753c0(uVar3,FUN_00476340);
          do {
            while( true ) {
              local_44 = 0x10;
              local_3c = FUN_00524930(local_40,local_28,&local_44);
              if (-1 < local_3c) break;
              uVar3 = FUN_00476a40(&DAT_005caba0,"Accept failed");
              FUN_004753c0(uVar3,FUN_00476340);
            }
            uVar3 = FUN_00476a40(&DAT_005cacc0,"Connection accepted");
            FUN_004753c0(uVar3,FUN_00476340);
            FUN_0040597c(local_3c);
            FUN_005216a0(local_3c);
          } while( true );
        }
        uVar3 = FUN_00...