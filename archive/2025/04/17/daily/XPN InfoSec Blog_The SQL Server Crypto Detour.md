---
title: The SQL Server Crypto Detour
url: https://blog.xpnsec.com/the-sql-server-crypto-detour/
source: XPN InfoSec Blog
date: 2025-04-17
fetch_date: 2025-10-06T22:04:43.045385
---

# The SQL Server Crypto Detour

[![avatar](/images/profile-image.jpg)](https://blog.xpnsec.com)
[XPN's InfoSec Blog](https://blog.xpnsec.com)

Adam Chester

Hacker and Infosec Researcher

## [XPN InfoSec Blog](https://blog.xpnsec.com "XPN InfoSec Blog")

[« Back to home](https://blog.xpnsec.com "Back to homepage")

# [The SQL Server Crypto Detour](/the-sql-server-crypto-detour/)

Posted on

2025-04-16
Tagged in
[redteam](/tags#redteam), [sqlserver](/tags#sqlserver)

Update: The talk from SOCON 2025 can now be found [here](https://www.youtube.com/watch?v=RiOtfPM7i3U).

As part of my role as Service Architect here at SpecterOps, one of the things I’m tasked with is exploring all kinds of technologies to help those on assessments with advancing their engagement.

Not long after starting this new role, I was approached with an interesting problem. A SQL Server database backup for a ManageEngine’s ADSelfService Plus product had been recovered and, while the team had walked through the database recovery, SQL Server database encryption was in use. With a ticking clock, the request was clear… can we do anything to recover sensitive information from the database with only a .bak file available?

One of the things that I love about this job is getting to dig into various technologies and seeing the resulting research being used in real-time. After some research, we had decryption keys, a method of decrypting sensitive data, and DA credentials extracted and ready to go!

This post will explore how this was done, look at how SQL Server encryption works, introduce some new methods of brute-forcing database encryption keys, and show a mistake in ManageEngine’s ADSelfService product which allows compromised database backups to reveal privileged credentials.

## Manage Engine Protected Data

Let’s start with Manage Engine’s ADSelfService product. Documentation shows that Domain Admin credentials are likely present:

![image.png](https://assets.xpnsec.com/sql-server-crypto-detour/image1.png)

If we setup this tool in a lab environment, we find encrypted fields such as the below `USER_NAME` column:

![image.png](https://assets.xpnsec.com/sql-server-crypto-detour/image2.png)

Further, if we review the configuration of the database, we see that this is SQL Server’s builtin encryption functionality that is being used to protect these fields. So the mission is clear: we need to understand SQL Server Encryption before we can hope to retrieve this data in cleartext.

## SQL Server Encryption Overview

The root of the cryptography chain in SQL Server is the Service Master Key (SMK). This key is associated and stored in the `master` database for the server.

At a database layer, the Database Master Key (DMK) is the start of the encryption chain for each database. This diagram from Microsoft gives a brilliant visualisation of this in action:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image3.png)

For us to explore this encryption functionality, let’s run a few TSQL commands on a lab instance of SQL Server 2019.

First up, we create a new database and master key:

```
USE CryptoDB;
CREATE MASTER KEY ENCRYPTION BY PASSWORD='Password123'
```

We can then view our created master key with:

```
SELECT * FROM sys.symmetric_keys
```

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image4.png)

Now this doesn’t show the actual content of the master key. Instead, to see this, we can use the query to list encryption keys in a database:

```
SELECT * FROM sys.key_encryptions
```

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image5.png)

The `crypt_property` field shows our newly created master key in some form. We can also see that the `crypt_type` and `crypt_type_description` fields give a good indication as to each key’s type.

After searching Microsoft’s documentation for how these keys are actually stored, or ways that we can extract them, I found a few snippets of information:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image6.png)

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image6-2.png)

Unfortunately none of this is useful for our purpose, so into the disassembler and debugger I needed to go.

## Strap In Peeps.. We’re Going Low Level!

For this exercise, it usually makes sense to try and find a good lead as to the APIs that Microsoft SQL Server may use to handle encryption/decryption. My lab ran SQL Server 2017 on Microsoft Windows Server 2019 and installing WinDBG Preview was too much of a pain without access to the Windows Store, so I spun up API Monitor and hooked the Crypto APIs to see if anything indicated their use during cryptographic operations on SQL Server. We execute the TSQL to open the master key and:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image7.png)

As far as indicators go, this was a good one. We see that `BCryptHashData` was used along with a password provided during the opening of the database master key.

The important part for us is the call stack, which showed `sqllang.dll` and `sqlmin.dll` were prime candidates for reversing:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image8.png)

Symbols were available for both of these DLL’s are grabbed using `symchk.exe`:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image9.png)

## Service Master Key Encryption

Let’s look at how the Service Master Key is generated and stored on SQL Server. This is the root of the encryption chain as shown in Microsoft’s diagram, so if we can find a vulnerability here, or some method of cracking this key, everything else will fall!

We know that a Database Master Key is encrypted using the Service Master Key. We also know from Microsoft’s documentation that this is likely protected using the data protection APIs (DPAPIs), which means that if we add a breakpoint on `CryptUnprotectData` / `CryptProtectData` and create a new DMK, we are in with a shot of seeing where in SQL Server is responsible for using the SMK.

To create the new key we use:

```
CREATE MASTER KEY ENCRYPTION BY PASSWORD='Password123'
```

And we hit a breakpoint with a valuable stack trace:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image10.png)

Here we see two method calls which tell us a story:

`CSECDBMasterKey::Decrypt`

`CSECServiceMasterKey::Initialize`

This makes sense, because we know that the SMK is used to decrypt the DMK and the DPAPI should protect the SMK.

We can pull out the arguments to `CryptoUnprotectData` and find the following value being decrypted:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image11.png)

And if we use the following TSQL query:

```
SELECT * FROM master.sys.key_encryptions
```

We find that the encrypted SMK matches the encrypted key stored in the `master` database:

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image12.png)

Another caveat is a value passed to `CryptUnprotectData` as the optional entropy value. After a bit of digging, we find that this value is taken from the registry key:

```
HKLM\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL14.MSSQLSERVER\Security
```

![Untitled](https://assets.xpnsec.com/sql-server-crypto-detour/image13.png)

So what does this mean? Well, if you have execution rights on a machine running SQL Server, we can use the following C# to recover the SMK:

```
using System;
using System.Security.Cryptography;
using Microsoft.Win32;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Read registry key
            var rk = Registry.LocalMachine.OpenSubKey(@"SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL14.MSSQLSERVER\Security");
            byte[] entropy = (byte[])rk.GetValue("Entropy", new byte[] { 0x41 });

            // SQL Encrypted SMK (minus the first 8 bytes)
            byte[] encryptedData = new byte[]
            {
                0x01, 0x00, 0x00, 0x00, 0xD0, 0x8C, 0x9D, 0xDF, 0x01, 0x15...