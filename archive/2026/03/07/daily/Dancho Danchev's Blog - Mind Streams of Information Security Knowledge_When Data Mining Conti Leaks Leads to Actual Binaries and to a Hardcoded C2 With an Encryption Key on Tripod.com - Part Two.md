---
title: When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Two
url: https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-03-07
fetch_date: 2026-03-08T04:07:23.262756
---

# When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Two

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Saturday, March 07, 2026

### When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Two

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0PWyussQ4Zr3yLtB3RIagHvLRY3yrVfSt9DC9OaF2mJDomOO580X43e7t7OuDqrD5T8Ye1oCj0HwHZvxdjcJZvOxODchV0qk4EL47hosNjmwxPqQa90eg8Ffi65NNpgkQQPSoFOCYX6pojE1_wpZ4Bhi0c4sE0rersewVRSeotjS4q_WBKKGT/s320/Misc_3300.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0PWyussQ4Zr3yLtB3RIagHvLRY3yrVfSt9DC9OaF2mJDomOO580X43e7t7OuDqrD5T8Ye1oCj0HwHZvxdjcJZvOxODchV0qk4EL47hosNjmwxPqQa90eg8Ffi65NNpgkQQPSoFOCYX6pojE1_wpZ4Bhi0c4sE0rersewVRSeotjS4q_WBKKGT/s772/Misc_3300.png)

Dear blog readers,

Continuing the second part of my original "[When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Two](https://ddanchev.blogspot.com/2026/02/when-data-mining-conti-leaks-leads-to.html)" post in this second post I'll proceed and move on with the next [Conti ransomware](https://ddanchev.blogspot.com/search?q=conti) sample which I originally obtained on my own by directly data mining [Conti Leaks](https://archive.org/details/rewards-for-justice-01) with a lot of success looking for URLs hosting or known to have been hosting or referencing malicious software.

The URL (**hxxp://dylanengineeringservices[.]com/3.exe**) and the [malicious software](https://ddanchev.blogspot.com/2022/06/a-compilation-of-known-conti-ransomware_21.html) in question is the [second binary](https://ddanchev.blogspot.com/2022/06/a-compilation-of-known-conti-ransomware_21.html) which I'm analyzing using [Vector35's BinaryNinja](https://binary.ninja/) which is SideKick AI assisted where I spend one day successfully decrypting and analyzing the payload where I also used [Unpac.me](http://Unpac.me) to extract all the relevant resources for the purpose of this analysis.

I'll continue processing and working on the remaining Conti ransomware samples and I'll continue elaborating on my findings.

**Here are the results:**

COMPLETE DECRYPTION CHAIN ANALYSIS:

1. RESOURCE EXTRACTION (0x404366):
   - Loads resource 0x4B60 (RT\_RCDATA type 0xA)
   - Resource contains 212,804 bytes of encrypted payload
   - Located at 0x4393a8 in .rsrc section

2. ANTI-ANALYSIS CHECKS:
   - taskmgr.exe detection (0x404405): Checks if Task Manager is loaded
   - VirtualAllocExNuma with node 64 (0x404430): Anti-VM technique
   - Allocates PAGE\_EXECUTE\_READWRITE memory for decrypted payload

3. RC4 DECRYPTION (0x4044A8):
   - Calls rc4\_decrypt\_payload at 0x401380
   - Uses 41-byte key: 'HKqRAMz5ss5VYiFYXBczKtqCE5lQXrX2A17RPm6b1' from
0x422164
   - Custom RC4 with 78,357-byte S-box (0x13215)
   - Decrypts 212,804 bytes in-place to allocated buffer

4. PAYLOAD EXECUTION (0x4044B0):
   - Executes decrypted PE via 'call key\_length' (buffer pointer)
   - Decrypted payload: 458,752 bytes (binary\_03.bin)
   - Entry point: 0x406222
   - Compilation: 2020-07-29 17:30:41 UTC
   - MFC-based x86 executable

5. DYNAMIC EXTRACTION:
   - Breakpoint at 0x4044AD captures decrypted payload in memory
   - Buffer address stored in EBP register (dereferenced pointer)
   - Successfully extracted via x32dbg memory dump

NOTE: The 8-byte key '5Yx6fR2P' at 0x404244 is NOT used for decryption.
It's copied to stack but never referenced in the actual RC4 call.

Decrypts .rsrc section using RC4 key
'HKqRAMz5ss5VYiFYXBczKtqCE5lQXrX2A17RPm6b1' (41 bytes) and loads 6 embedded PE files. Initializes COM and searches for Login.CRemoteLogin class. Second-stage payload loader.

STORAGE MECHANISMS IDENTIFIED

### 1. Registry Storage (Primary Method)

Function Chain:

```
sub_4169d9 (0x4169d9) → sub_417d4c (0x417d4c) → sub_417cb8 (0x417cb8)
```

Registry Path Structure:

```
HKEY_CURRENT_USER\software\<app_name>\<section>\<value_name>
```

Technical Details:

* Root Key: HKEY\_CURRENT\_USER (0x80000001)
* Base Path: "software" (string at 0x41c3f0)
* App Name: Stored at object offset 0x7c (dynamically determined)
* Section Name: Stored at object offset 0x90 (e.g., "Settings")
* Access Rights: 0x2001F (KEY\_ALL\_ACCESS - full read/write)
* Data Type: REG\_DWORD (4-byte integer values)
* Format String: "%d" at 0x41c114 (converts credentials to decimal)

Example Registry Structure:

```
HKEY_CURRENT_USER\software\LoginClient\Settings\PreviewPages =
```

```
<credential_data>
```

```
HKEY_CURRENT_USER\software\LoginClient\<section>\<key> = <value>
```

APIs Used:

* RegOpenKeyExA - Opens "software" key
* RegCreateKeyExA - Creates app and section subkeys
* RegSetValueExA - Writes credential data
* RegCloseKey - Closes handles

---

### 2. INI File Storage (Fallback Method)

Function: sub\_4182b3 at 0x4182b3 (INI path initialization)

File Path Construction:

```
GetModuleFileNameA() → "C:\path\to\LoginClient.EXE"
```

```
Strip extension → "C:\path\to\LoginClient"
```

```
Append ".INI" → "C:\path\to\LoginClient.INI"
```

Storage Location:

* Path: Same directory as executable
* Filename: <executable\_name>.INI (e.g., LoginClient.INI)
* Path Storage: Object offset 0x90
* String Reference: ".INI" at 0x41c638

INI File Format:

```
[Section]
```

```
Key=Value
```

APIs Used:

* GetModuleFileNameA - Gets executable path
* WritePrivateProfileStringA - Writes to INI file
* lstrcpyA, lstrcatA - String manipulation

Additional Files Created:

* Help File: <executable\_name>.HLP at offset 0x8C

---

## 🔐 DATA ENCRYPTION ANALYSIS

### ❌ NO ENCRYPTION DETECTED

Evidence:

1. Direct Storage: RegSetValueExA writes raw DWORD values
2. Format String: "%d" converts integers to decimal plaintext
3. No Crypto APIs: No calls to CryptEncrypt, CryptDecrypt, or crypto libraries
4. No Key Derivation: No PBKDF2, bcrypt, or hashing functions
5. Plaintext INI: WritePrivateProfileStringA writes unencrypted strings

Credential Format:

* Registry: 4-byte integer (REG\_DWORD) - likely user ID or hash reference
* INI File: Decimal string representation of integer value
* No Obfuscation: Direct storage without encoding or encryption

---

## 📖 READ OPERATIONS (CREDENTIAL VALIDATION)

### Validation Function Chain:

```
sub_4048e0 (0x4048e0) → sub_4054e0 (0x4054e0) → sub_418bcd (0x418bcd)
```

```
→ sub_4186a6 (0x4186a6)
```

Validation Process:

1. User Input: Captures User ID and Password from GUI
2. Database Query: Calls sub\_4054e0 with credentials
3. Comparison: Compares input against stored values
4. Result Display:
   * ✅ Success: "User ID and password matched successfully."
   * ❌ Failure: "User ID or password cannot be matched to the database."

Read APIs (Likely):

* RegQueryValueExA - Reads from Registry
* GetPrivateProfileStringA - Reads from INI file
* Comparison at 0x422338 (data reference)

---

## 🗃️ DATABASE FORMAT

### Storage Architecture:

Object Structure (MFC-based):

```
struct CredentialStorage {
```

```
    // Offset 0x7c: Storage mode flag
```

```
    //   0 = INI file mode
```

```
    //   non-zero = Registry mode (contains app name string)
```

```

```

```
    // Offset 0x8C: Help file path pointer
```

```
    char* help_file_path;
```

```

```

```
    // Offset 0x90: INI file path OR registry section name
```

```
    char* ini_path_or_section;
```

```

```

```
    // Offset 0xB4: Credential data value
```

```
    int32_t credential_value;
```

```
};
```

CRUD Operations:

| Operation | Function | Success Message | Failure Message |
| --- | --- | --- | ---...