---
title: The Segment Memory Model and How It Works in Windows x64
url: http://antonioparata.blogspot.com/2023/01/the-segment-memory-model-and-how-it.html
source: Over Security - Cybersecurity news aggregator
date: 2023-01-03
fetch_date: 2025-10-04T02:55:31.717511
---

# The Segment Memory Model and How It Works in Windows x64

# [Secure coding and more](http://antonioparata.blogspot.com/)

## lunedì 2 gennaio 2023

### The Segmented Memory Model and How It Works in Windows x64

I created this post as part of my jouring in getting more acquainted with the Intel architecture. Segmentation is a very important topic in the Intel architecture, so here is my contribution. For my experiment I'll use a x64 Windows 10 running in a VM attached to a kernel debugger.

## Mode of Operations

The first step is to identify the processor mode of operation. x64 supports various modes and memory models. Let's try to identify the current one. This information is stored in the 32-bit **CR0** control register ([1]), under the flag **PE** stored at position 0 (position 0 is the least significant bit (LSB), that is, the right-most bit). If this bit is set, we are running in **protected mode**, otherwise we are running in **real-address mode**. Let's use the kernel debugger to perform this check as shown in Figure 1.

```
kd> .formats cr0
Evaluate expression:
  Hex:     00000000`80050031
  Decimal: 2147811377
  Decimal (unsigned) : 2147811377
  Octal:   0000000000020001200061
  Binary:  00000000 00000000 00000000 00000000 10000000 00000101 00000000 00110001
  Chars:   .......1
  Time:    ***** Invalid
  Float:   low -4.59246e-040 high 0
  Double:  1.06116e-314Figure 1. Operation Mode Identification
```

The **CR0.PE** bit is set to 1, so we are running in **protected mode** using a segmented memory model (you might also notice that the **CR0.PG** bit, at position 31 is set, indicating that we are also using paging). We can also check the sub-mode operation by inspecting the **IA32\_EFER** Machine Specific Register (MSR) (0xC0000080) ([2]), and checking the **LME** (bit position 8) and **LMA** (bit position 10) flags. You can see the result in Figure 2.

```
kd> rdmsr 0xC0000080
msr[c0000080] = 00000000`00000d01
kd> .formats 00000000`00000d01
Evaluate expression:
  Hex:     00000000`00000d01
  Decimal: 3329
  Decimal (unsigned) : 3329
  Octal:   0000000000000000006401
  Binary:  00000000 00000000 00000000 00000000 00000000 00000000 00001101 00000001
  Chars:   ........
  Time:    Thu Jan  1 01:55:29 1970
  Float:   low 4.66492e-042 high 0
  Double:  1.64474e-320Figure 2. Operation Sub-Mode Identification
```

The **IA32\_EFER.LMA** and **IA32\_EFER.LME** bits are set, so we are running in **IA-32e sub-mode** (64-bit). This information will be used later in the text.

## Segmented Memory Model

The Segmented Memory Model accesses the memory by using the segment concept. A segment provides information on how to translate a given address. According to the executed instruction, a different segment is involved (eg. for **call** instruction the code segment is used, instead, for the **push** and **pop** instructions the stack segment is used). The Intel architecture defines a total of six segment registers: **CS**, **DS**, **ES**, **SS**, **GS**, and **FS**. For example, the **CS** segment (code segment) is used when a **call** instruction is executed. Let's see how this works with a practical example, let's consider the instruction in Figure 3.

```
00007FFD42C7D5C1 | E8 1A000000  | call kernelbase.7FFD42C7D5E0Figure 3. How Segmentation Works
```

The **call** instruction uses the value **1A000000** to specify the address of the function to execute. Since we are in a x64 bit operation mode, the value is RIP-relative, this explains why the function address in the disassembly is 0x7FFD42C7D5E0 (0x7FFD42C7D5C1 (RIP) + 0x1a (offset) + 0x05 (instruction size)). In addition to the mentioned value, the value of the **CS** segment is also used. The combination of the **CS** with the function address is called the **logical address**. The segment value is then used to translate the **logical address** into what is known as the **virtual address** (this process is described in the next section). Since our system is using paging, and additional translation step is performed to translate the **virtual address** into the **physical address** (this topic is not covered in this post). All the translation steps are represented in Figure 4.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbunDGGhRyQZ27zQvTdFMFG_YUCSznqj-EfOfyBvIdzuIJWvri4ghOwtklC-fjJFNwX6R-WihRfEUKI0AE-PRTB6QR3CMo9ypRa_tjfVjTNp3NDCd4UCIs1KtqGxir_wzO58YhxCOnqgSCUSWSvCOP9w1x6DQeDzuPp7S6IGWwdoJIER2X6GkyAOyV-w/s320/post_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbunDGGhRyQZ27zQvTdFMFG_YUCSznqj-EfOfyBvIdzuIJWvri4ghOwtklC-fjJFNwX6R-WihRfEUKI0AE-PRTB6QR3CMo9ypRa_tjfVjTNp3NDCd4UCIs1KtqGxir_wzO58YhxCOnqgSCUSWSvCOP9w1x6DQeDzuPp7S6IGWwdoJIER2X6GkyAOyV-w/s591/post_1.png)Figure 4. Logical to Physical Address Translation

## How Segmentation Works

The segment registers are 16-bit registers whose structure is reported in Figure 5.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSWydd6QZs6-rbS99WdYDdsRJH1fHI_WdRBbezGGeb5BSiXniAJ_mfHi2J2Ny97H1jM8RZ7xG3KUBiqYTVKRRrpfSwJ18pfQlX5Su33bvhK1IBiD_O9Hu5kC_0GfzQUhSm_NL2N3aB6imEn7QKDFvXJSDn3MdSH8v8LQFFfV5w5ugVFIJYXCM2_lLI1Q/s320/post_3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSWydd6QZs6-rbS99WdYDdsRJH1fHI_WdRBbezGGeb5BSiXniAJ_mfHi2J2Ny97H1jM8RZ7xG3KUBiqYTVKRRrpfSwJ18pfQlX5Su33bvhK1IBiD_O9Hu5kC_0GfzQUhSm_NL2N3aB6imEn7QKDFvXJSDn3MdSH8v8LQFFfV5w5ugVFIJYXCM2_lLI1Q/s589/post_3.png)Figure 5. Segment Selector Format

The **Index** field is used as an index in a table that contains information on all the available segments. The **TI** flag indicates which table must be used, and the Request Privilege Level (RPL) field specifies the protection level of the code requesting access to a specific segment. The possible protection level values are: 0, 1, 2 and 3, and are often represented as protection rings, where ring 0 is the most privileged (where the kernel mode code is executed) and ring 3 is the least privileged (where user mode code is executed).

The two tables that contain information on the segments are the **Global Descriptor Table (GDT)** and the **Local Descriptor Table (LDT)**. The registers **GDTR** and **LDTR** contain the base address of the respective table. In the latest Windows versions, the LDT is no more used, so the TI flag will always be 0. The GDT is an array of segment descriptors, where each segment descriptor is typically represented by the 64-bit structure reported in Figure 6.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh56CQFTf2jw5dk-nS9gAcrcsIZ7SLngVYM26SR4HUrm-lHkXQYebENkMjvnjJS6sCPZOV92-9wHk5zvhLBI1DdJ-DZIM_hoI90ztfMocutqYDdW6MpoGZ4Z-dzQQJiqiFxBB-qEjfYOcPnRXuccWF8Vs3dP98oJVtQS84R4TS_JpMZO7TNgJj_jwlAmA/s320/post_4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh56CQFTf2jw5dk-nS9gAcrcsIZ7SLngVYM26SR4HUrm-lHkXQYebENkMjvnjJS6sCPZOV92-9wHk5zvhLBI1DdJ-DZIM_hoI90ztfMocutqYDdW6MpoGZ4Z-dzQQJiqiFxBB-qEjfYOcPnRXuccWF8Vs3dP98oJVtQS84R4TS_JpMZO7TNgJj_jwlAmA/s588/post_4.png)Figure 6. Segment Descriptor Format

Given the segment descriptor definition, we can now explain how the **logical address** to **virtual address** translation is performed. The **Base** field is added to the **logical address** in order to obtain the **virtual address**. This process is described in Figure 7.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRMMbZiFG6LoYCet7QdDH9wfhoC4MWBQDPFfVohM7Q_kBU8temSKE-ICBLxqlPRlahHf8GcyMTSU1Bb6sc1DM8FEjJHQFzm_sQh3ng98BZ5rH571DJ23Ks7Lm2CdwomVJm-ZN3hOJm7Axr3so-d81NW_gHuhkOP-nNx4kJJdxMx6VhYt__1oH66OidsA/s320/post_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRMMbZiFG6LoYCet7QdDH9wfhoC4MWBQDPFfVohM7Q_kBU8temSKE-ICBLxqlPRlahHf8GcyMTSU1Bb6sc1DM8FEjJHQFzm_sQh3ng98BZ5rH571DJ23Ks7Lm2CdwomVJm-ZN3hOJm7Axr3so-d81NW_gHuhkOP-nNx4kJJdxMx6VhYt__1oH66OidsA/s587/post_2.png)Figure 7. Segment Descriptor Usage in Address Translation

A very important field is **DPL**. It indicates the privilege level of the code running in that segment, for example, a **DPL** value of ...