---
title: When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Six
url: https://ddanchev.blogspot.com/2026/05/when-data-mining-conti-leaks-leads-to.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-05-02
fetch_date: 2026-05-03T05:29:04.902948
---

# When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Six

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Saturday, May 02, 2026

### When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Six

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX1imK8pZtR2_SL2wZw13u-i-Axy6yxuHvwqwDmXl4coW3ZhGwhltrfM_lq2SI5AbSBnUsDnSTXuDeicz5VtAb2dj_RwCUz3b_jTke-LEbwJYshPsdFJn25ScWMtZcn0agzLj9nqFoZJfZAs1UACqRmR9GU0Fvc9VIPRvn_W_IlI2ymilr4mzZ/s320/Conti_Ransomware_01.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgX1imK8pZtR2_SL2wZw13u-i-Axy6yxuHvwqwDmXl4coW3ZhGwhltrfM_lq2SI5AbSBnUsDnSTXuDeicz5VtAb2dj_RwCUz3b_jTke-LEbwJYshPsdFJn25ScWMtZcn0agzLj9nqFoZJfZAs1UACqRmR9GU0Fvc9VIPRvn_W_IlI2ymilr4mzZ/s376/Conti_Ransomware_01.png)

Dear blog readers,

Continuing my "[When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Five](https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to_25.html)" blog post series in this post I'll share my recent experience in reverse engineering yet another malicious software sample which belongs to Conti ransomware where what I did was the following which was to find out that the decryption key was actually stored in the encrypted file on the targeted host where the actual decryption key is stored in each and every encrypted by the malicious software sample file on the affected host.

The sample is from 2020 but it's still interesting and relevant to emphasize that files encrypted with this Conti ransomware sample can be decrypted without having to interact with the Conti Ransomware Gang.

Here's the [analysis](https://www.virustotal.com/gui/file/1ef1ff8b1e81815d13bdd293554ddf8b3e57490dd3ef4add7c2837ddc67f9c24/detection).

MD5: 42e106fd843b0e3585057c30424f695a

SHA-1: 7b7f0c029a3dcb34a7a448f05b43c5657dd0c471

SHA-256: 1ef1ff8b1e81815d13bdd293554ddf8b3e57490dd3ef4add7c2837ddc67f9c24

This is ransomware with the following key characteristics:

Initial Analysis:

1. Dynamic API Resolution: sub\_401000 (0x401000) loads multiple DLLs (Advapi32, Kernel32, Netapi32, Iphlpapi, Rstrtmgr, Ws2\_32, User32, Shlwapi) and resolves API functions using obfuscated strings, storing function pointers in global data variables.
2. Mutex-based Singleton: \_start creates a mutex with an obfuscated name to ensure only one instance runs.
3. Command-line Parsing: Processes command-line arguments to extract encryption parameters (likely encryption keys or configuration).
4. Multi-threaded Encryption: Creates multiple worker threads (sub\_417df0) to encrypt files in parallel.
5. File Enumeration:
   * Enumerates network shares (sub\_405000 with GetCommandLineW)
   * Enumerates local drives and network adapters
   * Recursively traverses directories
6. Restart Manager Integration: Uses Rstrtmgr.dll APIs to close file handles held by other processes before encryption.
7. Ransom Note Deployment: Drops ransom notes (likely ".x.x]x[x.xxx" which decodes to a filename) in encrypted directories.
8. Large Code Sections: Functions sub\_406170, sub\_407c30, sub\_40b850, and sub\_40fcf0 contain embedded data (likely encrypted configuration, ransom note templates, or cryptographic material).

Summary

This is a multi-threaded ransomware that encrypts files on local and network drives. Key characteristics:

### Capabilities:

* Dynamic API Resolution: Loads 8 DLLs and resolves ~100+ API functions using obfuscated strings
* Singleton Execution: Creates mutex to prevent multiple instances
* Multi-threaded Encryption: Spawns worker threads for parallel file encryption
* Network Propagation: Enumerates and encrypts network shares
* Restart Manager Integration: Uses Rstrtmgr.dll to unlock files held by other processes
* Selective Encryption: Filters files by extension (excludes system files)

### Ransom Note:

* Filename: HOW\_TO\_DECRYPT
* Contact Emails:
  + vadepkowsproc1972@protonmail.com
  + inficisi1972@protonmail.com
* Message: "The system is LOCKED. Do not use OTHER software. For DECRYPTOR write on the emails..."

### Encryption Details:

* Encryption keys/parameters stored in PE resources (RCDATA #101 and #102)
* Command-line parsing extracts encryption configuration
* Two encryption modes: full file encryption or partial (likely for large files)
* Likely appends .lckd extension to encrypted files

### Functions Renamed:

* main (0x405350) - Entry point
* resolve\_api\_functions (0x401000) - API resolution
* encrypt\_file (0x416d10) - File encryption routine
* encryption\_worker\_thread (0x417df0) - Worker thread
* drop\_ransom\_note (0x4060b0) - Ransom note deployment
* Plus 20+ other supporting functions

Encryption Process Analysis

### How Encryption Works:

1. Key Extraction (0x405438-0x4054d0):
   * Extracts encryption parameters from PE resources RCDATA #101 and #102
   * Converts parameters to wide strings and stores in globals g\_key\_param1 and g\_key\_param2
   * Sets g\_encryption\_mode (0=full file, 1=partial encryption)
2. RSA Public Key (0x41a008):
   * Hardcoded RSA-1024 public key blob (header: "RSA1")
   * Imported using CryptImportKey in crypto\_operation (0x417bdb)
3. File Encryption Flow:
   * Worker threads (encryption\_worker\_thread @ 0x417df0) process files from queue
   * For each file, crypto\_operation (0x417ba0):
     + Reads file data in 5MB chunks (0x500000 bytes)
     + Encrypts chunks using CryptEncrypt (0x417bff)
     + Writes encrypted data back to file
     + CRITICAL: Writes g\_key\_param1 and g\_key\_param2 to file header (0x416f58)
4. File Renaming:
   * Appends obfuscated extension (deobfuscates to ".lckd")
   * Original: file.txt → Encrypted: file.txt.lckd

---

## CRITICAL VULNERABILITIES FOUND:

### 1. 🔴 ENCRYPTION KEY WRITTEN TO FILES (CRITICAL)

Location: 0x416f58 in encrypt\_file

```
api_WriteFile(file_handle, g_key_param1, g_key_param2,
&bytes_written, 0)
```

Impact: The ransomware writes the encryption key parameters directly to the beginning of each encrypted file. If these parameters contain the actual symmetric key or sufficient key derivation material, victims can decrypt files without paying the ransom by:

1. Extracting the key from any encrypted file header
2. Using the same RSA public key (hardcoded at 0x41a008)
3. Reversing the encryption process

Exploitation: Analyze the first g\_key\_param2 bytes of any .lckd file to extract the key material.

---

### 2. 🟡 RSA-1024 Weak Cryptography (MEDIUM)

Location: 0x41a008 (rsa\_public\_key\_blob)

Issues:

* RSA-1024 deprecated since 2013 (NIST recommendation)
* Vulnerable to factorization with sufficient resources
* Hardcoded key provides perfect detection signature

---

### 3. 🟡 Race Condition in File Processing (MEDIUM)

Location: 0x417111 (file queue submission)

Issue: No synchronization prevents the same file from being encrypted multiple times if encountered through different paths (local drive + network share pointing to same location).

Impact: File corruption, double-encryption, inconsistent state.

---

### 4. 🟡 Buffer Overflow in Path Construction (MEDIUM)

Location: 0x416d2c in encrypt\_file

```
buffer_size = api_lstrlenW(path) * 2 + 6
```

Issue: No validation that concatenated paths won't exceed MAX\_PATH (260 chars). Long paths can cause buffer overflow.

---

### 5. 🟢 Predictable Mutex Name (LOW)

Location: 0x4053dd in main

Deobfuscated Mutex: ycL|\_ycL

Mitigation: Create this mutex before ransomware executes to prevent it from running:

```
CreateMutexA(NULL, TRUE...