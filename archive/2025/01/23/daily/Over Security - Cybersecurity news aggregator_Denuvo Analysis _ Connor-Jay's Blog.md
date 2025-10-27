---
title: Denuvo Analysis | Connor-Jay's Blog
url: https://connorjaydunn.github.io/blog/posts/denuvo-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-23
fetch_date: 2025-10-06T20:13:42.574894
---

# Denuvo Analysis | Connor-Jay's Blog

[![](/blog/images/avatar.png)](https://connorjaydunn.github.io/blog/)

[# Connor-Jay's Blog](https://connorjaydunn.github.io/blog/)

### A 3rd Year Computer Science Student

[**Home**](/blog/)
|
[**About**](/blog/about/)
|
[**Posts**](/blog/posts/)

---

# Denuvo Analysis

**Posted on
2025-01-21**
 • 3805 words
 • 18 minute read

# Foreword

This post is intended for educational purposes only. Denuvo is arguably the most successful digital rights management solution to have ever existed, and is therefore an interest to many. This blog contains a large amount of my personal notes and correspondence with other reverse engineers (see [kudos](#kudos)) which contains information about the recent iterations of Denuvo, lots of which I haven’t seen shared publicly before.

I mean no harm towards Irdeto and thus certain information will be redacted from this post.

# Denuvo

![](denuvo.logo.png)

Denuvo is an anti-tamper and digital rights management system (DRM). It is primarily used to protect digital media such as video games from piracy and reverse engineering efforts. Unlike traditional DRM systems, Denuvo employs a wide range of unique techniques and checks to confirm the integrity of both the game’s code and licensed user.

# The General Idea

The core idea behind Denuvo is nothing new. It can only be described as a semi-online DRM for reasons that will become clear shortly. The general idea is as follows:

**(1)** User boots program.exe for the first time.

**(2)** Before any original game code is executed, Denuvo will collect hardware identification information regarding the current system, and prepare it for sending over the internet.

**(3)** program.exe then sends this hardware information to a Denuvo hosted server. What occurs at the server is obviously a mystery, but it likely applies reversible mathematical functions to combine the “stolen constants” (more on those later) with the hardware information provided by program.exe. The server then sends this now mixed information, we will refer to this as “the license file”, back to program.exe.

**(4)** Once program.exe receives the license file, a local copy is created that program.exe can refer to on future boots; removing the need for another online request to be made (hence the use of “semi-online” earlier).

**(5)** program.exe will be redirected to the original entry point (OEP) and begin executing the actual game code. During this time, program.exe will collect hardware information at runtime and attempt to decrypt stolen constants from the license file. These now decrypted constants will then be used to execute “original game instructions”.

If it wasn’t made clear already, the game will effectively end up performing user integrity checks. This is due to the fact that if the hardware information collected at runtime is not the equal to that of which was used to create the license file on the Denuvo server, then an incorrect stolen constant will be decrypted and the game will likely suffer (most of the time this is a direct crash).

# A More Technical Explanation

This section will investigate each protection mechanism and user integrity check more thoroughly. Remember, there is far more to Denuvo that what is outlined here.

## General Idea Revisited

### License File

When Denuvo is first added to a binary, certain functions in that game are selected to become “protected”. All this means is that the function itself will be executed inside of a virtual machine, and select parts of certain instructions will be removed entirely from the binary. The license file is simply all of these removed bytes combined together and combined with the user’s hardware identification via reversible mathematical functions. It is important that whatever operations are applied are reversible, otherwise the client would have no way of decrypting and getting the original constant.

### License DWORDs

Since there are multiple stolen instructions, prior to handling execution over to the OEP, Denuvo will write select parts of the license file into DWORDs, scattered around the .vm section (.vm being the PE section which contains the VM code). Each DWORD, we will nick “License DWORD”, is effectively a single instruction that was removed from the binary, combined with the hardware identification information of the customer.

### Encrypted Constant / Removed Instruction Example

In order to make the idea concrete, I will show an example of how instructions are “removed” from the binary. Assume we have the following function:

```
add(int, int):
	push  rbp
	mov  rbp, rsp
	mov  DWORD  PTR [rbp-4], edi
	mov  DWORD  PTR [rbp-8], esi
	mov  edx, DWORD  PTR [rbp-4]
	mov  eax, DWORD  PTR [rbp-8]
	add  eax, edx
	pop  rbp
	ret
```

It is trivial to see that there exist parts of instructions that will never change once compiled. For instance:

```
mov  DWORD  PTR [rbp-4], edi
```

Here we are writing the contents of the 32-bit register, *EDI*, into *[RBP-4]*. In this case, Denuvo would strip the binary of the constant *-4* and store it on their server. Now, the only way for anyone to access this constant, which would be required for a successful execution of *add(int, int)*, would be to request a license file from Denuvo as that would contain the license DWORDs, which contain the encrypted constant *-4* (recall that the license file contains the constants mixed with hardware identification). Furthermore, Denuvo will convert the entire function, *add(int, int)*, into bytecode that only their virtual machine can understand. Present in this bytecode, there exists code which acts like a wrapper around the removed instruction. This wrapper is responsible for the following:

**(1)** Collect the corresponding hardware information at runtime (the specific hardware information that was mixed in with the constant).

**(2)** Read the corresponding license DWORD that contains the encrypted constant for this particular function.

**(3)** Perform a series of mathematical operations using the license DWORD and the hardware identification collected at runtime to retrieve the value of *-4*. This should be the inverse of whatever the server did.

**(4)** Execute the original instruction with the now decrypted constant.

Recall from a previous section, if the hardware identification collected at runtime does not align with that which was used on the Denuvo server to encrypt the constant, then **(3)** will likely yield a result that is not equal to *-4*; causing undefined behaviour.

## User Integrity Checks

I will now highlight all of the vectors Denuvo use to verify the integrity of the system executing the protected binary. By the nature of the protection, at least one instance of each check must be sent to the server when requesting for a license file.

### Pre-OEP Checks

After reading the previous section(s), you may be wondering what happens if a user’s hardware identification changes (e.g. Windows update, new CPU, etc). Denuvo account for this using special checks which execute just before handing control to the OEP. They will simply perform some constant decryptions but instead of using said constant to execute an instruction, they will check if it is equal to what it should be (these are the only checks that do this, everything else assumes that the decrypted constant is correct and acts accordingly). If the result is not as expected, Denuvo will delete the locally saved license file and request a new one from the Denuvo server; basically a repeat of the process described in [The General Idea](#the-general-idea)

### KUSER\_SHARED\_DATA

[KUSER\_SHARED\_DATA](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-kuser_shared_data) is a single page of, [now read-only](https://msrc.microsoft.com/blog/2022/04/randomizing-the-kuser_shared_data-structure-on-windows/), memory (4096 bytes) that is mapped into every process running on a Windows machine. It contains information that processes may wish to access, such as the...