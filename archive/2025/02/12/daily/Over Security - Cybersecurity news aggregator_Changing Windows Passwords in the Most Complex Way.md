---
title: Changing Windows Passwords in the Most Complex Way
url: https://decoder.cloud/2025/02/11/changing-windows-passwords-in-the-most-complex-way/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-12
fetch_date: 2025-10-06T20:38:13.059454
---

# Changing Windows Passwords in the Most Complex Way

# [Decoder's Blog](https://decoder.cloud/ "Decoder's Blog")

Decoder's Blog

[Skip to content](#content "Skip to content")

* [Home](/)
* [Decoder’s Blog](https://decoder.cloud/)
* [Contact](https://decoder.cloud/contact/)

Search for:

Posted on [February 11, 2025](https://decoder.cloud/2025/02/11/changing-windows-passwords-in-the-most-complex-way/) by [Decoder](https://decoder.cloud/author/decoderblogblog/)

# Changing Windows Passwords in the Most Complex Way

Why write a post about changing Windows passwords programmatically when so many built-in and third-party tools already let us do it effortlessly? The answer is simple: curiosity. It drives us to understand the underlying mechanisms of the systems we interact with, explore hidden parts, and sometimes even uncover unintended behaviors or security flaws. This post isn’t just about changing passwords; I tried to “embrace” the hacker mindset, diving into system internals and sharing my journey.

Disclaimer: What I’m writing about has maybe been documented elsewhere. I’m hardly a genius or a world-class security researcher with a mind sharper than a quantum computer. All I have is curiosity, decades of experience, and an undying love for diving deep despite being at an age where I should probably be more focused on retirement and leisurely activities. 😔

## The easy way

Besides using ready-made tools, one of the API calls that performs all the magic is *NetUserSetInfo* in **NetApi32.dl**l, the same call used by many tools behind the scenes.

It uses the (old) MS-SAMR protocol, which permits you to change local and Domain Accounts, along with MS-ADTS, MS-KILE, MS-NRPC, etc…

A detailed description of *NetUserSetInfo* can be found [here](https://learn.microsoft.com/en-us/windows/win32/api/lmaccess/nf-lmaccess-netusersetinfo). In our case, we are more interested in the USER\_INFO\_1003 structure:

```
typedef struct _USER_INFO_1003 {
  LPWSTR usri1003_password;
} USER_INFO_1003, *PUSER_INFO_1003, *LPUSER_INFO_1003;
```

Which is used for changing the password of a specific account:

```
userInfo.usri1003_password = (wchar_t*)new_password;

// Call NetUserSetInfo to update the password
ret= NetUserSetInfo(server, account, 1003, (LPBYTE)&userInfo, NULL);
```

That’s it! You can change any user or computer account password on any machine. If the server is a Domain Controller, the AD password will be updated; otherwise, the password stored in the local SAM database will be changed.

## the complex way

But what’s happening behind the scenes? A quick Wireshark analysis, filtered for the SAMR protocol, reveals the process in action:

![](https://decoder.cloud/wp-content/uploads/2025/02/image-11.png?w=1024)

It uses the **SetUserInfo2** RPC call to communicate with the destination server. This call is part of the **MS-SAMR** protocol and is defined in the [IDL](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/1cd138b9-cc1b-4706-b115-49e53189e32e) file

```
 // opnum 58
 long
 SamrSetInformationUser2(
     [in] SAMPR_HANDLE UserHandle,
     [in] USER_INFORMATION_CLASS UserInformationClass,
     [in, switch_is(UserInformationClass)]
         PSAMPR_USER_INFO_BUFFER Buffer
     );
```

We are interested in the USER\_INTERNAL8\_INFORMATION

```
  typedef struct _SAMPR_USER_INTERNAL8_INFORMATION
  {
      SAMPR_USER_ALL_INFORMATION I1;
      SAMPR_ENCRYPTED_PASSWORD_AES UserPassword;
  } 	SAMPR_USER_INTERNAL8_INFORMATION;
```

the **UserPassword** is defined as follows:

```
 typedef struct _SAMPR_ENCRYPTED_PASSWORD_AES
 {
     UCHAR AuthData[64];
     UCHAR Salt[16];
     ULONG cbCipher;
     PUCHAR Cipher;
     ULONGLONG PBKDF2Iterations;
 } 	SAMPR_ENCRYPTED_PASSWORD_AES;
```

The new password must be encrypted with AES before being sent to the server.

![](https://decoder.cloud/wp-content/uploads/2025/02/image-12.png?w=1024)

Now let’s take a closer look at how we can get there:

![](https://decoder.cloud/wp-content/uploads/2025/02/image-1.png?w=1024)

The function *SampEncryptClearPasswordWithSessionKeyAES* seems to do all the magic, but it’s not exported in **samlib.dll**:

![](https://decoder.cloud/wp-content/uploads/2025/02/image-2.png?w=986)

*Note: Before calling SampEncryptClearPasswordWithSessionKeyAES, several other function calls are made, such as verifying password restrictions and checking whether AES should be used. However, we can safely skip them for our purpose.*

Loading a function that is not exported should not be a big problem; we could search for specific patterns in the DLL to get the function address:

![](https://decoder.cloud/wp-content/uploads/2025/02/image-3.png?w=1024)

And these patterns would be enough:

```
BYTE pattern[] = { 0x40, 0x53, 0x55, 0x56, 0x57, 0x41, 0x57, 0x48, 0x83, 0xEC,0x70,0x48,0x8b };
```

But what parameters should we pass to the function? By reversing the function into pseudo-C code using Ghidra, we can see that the first parameter is the handle of the user account we want to modify. This is evident because it is passed to *SystemFunction028()*, which returns the SMB session key (more on later).

![](https://decoder.cloud/wp-content/uploads/2025/02/image-5.png?w=981)

The second and the third parameters are the cleartext password and the resulting encrypted password passed to the function  *SampEncryptClearPasswordAESWorker()*:

![](https://decoder.cloud/wp-content/uploads/2025/02/image-6.png?w=1024)

After analyzing the code and conducting several tests, it turned out that the input password is a pointer to a *UNICODE\_STRING*, while the output is a pointer to the *SAMPR\_ENCRYPTED\_PASSWORD\_AES* structure we encountered earlier.

At this point, we have all the pieces we need:

1. Open a connection to the server using *SamrConnect5()*.
2. Open a connection to the domain with *SamrOpenDomain()*, passing the domain SID.
3. Open a connection to the target user with *SamrOpenUser()*, passing the user’s RID to obtain the *userHandle* of the target user.
4. Create a *UNICODE\_STRING* (`uString`) containing the new password.
5. Declare a *SAMPR\_ENCRYPTED\_PASSWORD\_AES* (`uAES`).
6. Locate and load the non-exported *SampEncryptClearPasswordWithSessionKeyAES* function.
7. Pass all these parameters to *SampEncryptClearPasswordWithSessionKeyAES(userHandle, &uString, &uAES)*.

If everything works correctly, we should get a populated *uAES* structure.

Now, we just need to:

* Declare a *SAMPR\_USER\_INTERNAL8\_INFORMATION* variable.
* Assign *uAES* to *UserPassword*.
* Set *SAMPR\_USER\_ALL\_INFORMATION* to `1`, which indicates that we want to change the NT password.

```
memset(&us, 0, sizeof(us));
memcpy(us.Internal8.UserPassword.Salt, uAES.Salt, 16);
memcpy(us.Internal8.UserPassword.AuthData, uAES.AuthData, 64);
us.Internal8.UserPassword.cbCipher = uAES.cbCipher;
us.Internal8.UserPassword.PBKDF2Iterations = 0;
us.Internal8.I1.WhichFields = toBigEndian(1);
us.Internal8.UserPassword.Cipher = uAES.Cipher
status = SamrSetInformationUser2(userHandle, (USER_INFORMATION_CLASS)32, &us);
```

But during the compilation, we will get an error:

![](https://decoder.cloud/wp-content/uploads/2025/02/image-9.png?w=645)

We are missing the *PSAMPR\_SERVER\_NAME\_bind()* function, which should handle the RPC connection. In fact, this function is in the **samlib.dll** but not exported, and I could not find any incoming calls to this one. Anyway, we have to setup the transport and this could be performed directly by us. As written in the MS-SAMR [Transport section](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/084da2e7-0ba0-44fc-8f17-e8a200c69eb5), if we want to use S*amrSetInformationUser2* we have to use named pipes **ncacn\_np** as the protocol sequence and the **\pipe\samr** endpoint

![](https://decoder.cloud/wp-content/uploads/2025/02/image-28.png?w=1018)

And finally, it worked 😉

![](https://decoder.cloud/wp-content/uploads/2025/02/image-8.png?w=1024)

Let’s test if we can bypass password restrictions given that we omitted all t...