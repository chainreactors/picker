---
title: edk2 edk2-stable202608
url: https://kitploit.com/en/posts/github-tianocore-edk2-edk2-stable202608
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:50:54.740431
---

# edk2 edk2-stable202608

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/8456/25506adaf423b13d3b880533b356d4f4d070e4fd0a5ae1ab20cf764d8e0598aa.png)

New releaseAug 21, 2026

# edk2 edk2-stable202608

Cross-platform firmware development environment implementing UEFI and PI specifications. Provides build tools, cryptographic libraries, and virtual platform support for hardware and embedded systems security.

Share

# ============== EDK II Project

A modern, feature-rich, cross-platform firmware development
environment for the UEFI and PI specifications from [www.uefi.org](http://www.uefi.org).

.. image:: <https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftianocore%2Fedk2-pytool-extensions%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.%5B'requires-python'%5D&style=for-the-badge&logo=python&logoColor=ffd343&label=Minimum%20Python%20Version%20for%20CI&color=3776ab&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F>
:alt: CI Minimum Python Version

It is recommended to install this Python version to run the full set of scripts that enable CI in the project.

Other Python requirements for build can be found in the `EDK II Build Instructions <https://www.tianocore.org/tianocore-wiki.github.io/build-tooling/build-workflows/edk_ii_tools_list.html>`\_\_.

## Core CI Build Status

====================================== ================= ================ ===================
Host Type & Toolchain Build Status Test Status Code Coverage
====================================== ================= ================ ===================
Windows\_VS\_ |WindowsCiBuild| |WindowsCiTest| |WindowsCiCoverage|
Ubuntu\_GCC\_ |UbuntuCiBuild| |UbuntuCiTest| |UbuntuCiCoverage|
Windows\_CLANGPDB\_ |WinClgCiBuild| |WinClgCiTest| |WinClgCiCoverage|
Ubuntu\_CLANGPDB\_ |UbuClgCiBuild| |UbuClgCiTest| |UbuClgCiCoverage|
Ubuntu\_CLANGDWARF\_ |UbuCdwCiBuild| |UbuCdwCiTest| |UbuCdwCiCoverage|
====================================== ================= ================ ===================

`More CI Build information <.pytool/Readme.md>`\_\_

## Platform CI Build Status

Microsoft Windows Visual Studio (VS)

root@kitploit:~

```

============================= ================= ============= ============= ==============
 Toolchain                    CONFIG            DEBUG         RELEASE       NOOPT
============================= ================= ============= ============= ==============
EmulatorPkg_Win_VS_           | X64             |em64d|       |em64r|       |em64n|
|                             | X64 FULL        |em64fd|      |em64fr|      |em64fn|
OvmfPkg_Win_VS_               | X64             |op64d|       |op64r|       |op64n|
============================= ================= ============= ============= ==============

Microsoft Windows CLANGPDB
``````````````````````````

============================= ================= ============= ============= ==============
 Toolchain                    CONFIG            DEBUG         RELEASE       NOOPT
============================= ================= ============= ============= ==============
EmulatorPkg_Win_CLANGPDB_     | X64             |emW64cd|     |emW64cr|     |emW64cn|
|                             | X64 FULL        |emW64cfd|    |emW64cfr|    |emW64cfn|
============================= ================= ============= ============= ==============

Ubuntu GCC
``````````

============================= ================= ============= ============= ==============
 Toolchain                    CONFIG            DEBUG         RELEASE       NOOPT
============================= ================= ============= ============= ==============
ArmVirtPkg_Ubuntu_GCC_        | AARCH64         |avAArch64du| |avAArch64ru| |avAArch64nu|
EmulatorPkg_Ubuntu_GCC_       | X64             |em64du|      |em64ru|      |em64nu|
|                             | X64 FULL        |em64fdu|     |em64fru|     |em64fnu|
OvmfPkg_Ubuntu_GCC_           | X64             |op64du|      |op64ru|      |op64nu|
============================= ================= ============= ============= ==============

|TCBZ_2639|_ - EmulatorPkg Ubuntu GCC Segfaults during execution.

Ubuntu CLANGPDB
```````````````

============================= ================= ============== ============== ==============
 Toolchain                    CONFIG            DEBUG          RELEASE        NOOPT
============================= ================= ============== ============== ==============
ArmVirtPkg_Ubuntu_CLANGPDB_   | AARCH64         |avAArch64cpu| |avAArch64rpu| |avAArch64npu|
OvmfPkg_Ubuntu_CLANGPDB_      | X64             |opU64cpd|     |opU64cpr|     |opU64cpn|
============================= ================= ============== ============== ==============

Ubuntu CLANGDWARF
`````````````````

============================== ================= ============== ============== ==============
 Toolchain                     CONFIG            DEBUG          RELEASE        NOOPT
============================== ================= ============== ============== ==============
ArmVirtPkg_Ubuntu_CLANGDWARF_  | AARCH64         |avAArch64cdu| |avAArch64rdu| |avAArch64ndu|
EmulatorPkg_Ubuntu_CLANGDWARF_ | X64             |emU64cdd|     |emU64cdr|     |emU64cdn|
|                              | X64 FULL        |emU64cdfd|    |emU64cdfr|    |emU64cdfn|
OvmfPkg_Ubuntu_CLANGDWARF_     | X64             |opU64cdd|     |opU64cdr|     |opU64cdn|
============================== ================= ============== ============== ==============

`More ArmVirtPkg CI Build Information <ArmVirtPkg/PlatformCI/ReadMe.md>`__

`More EmulatorPkg CI Build Information <EmulatorPkg/PlatformCI/ReadMe.md>`__

`More OvmfPkg CI Build Information <OvmfPkg/PlatformCI/ReadMe.md>`__

License Details
---------------

The majority of the content in the EDK II open source project uses a
`BSD-2-Clause Plus Patent License <License.txt>`__. The EDK II open
source project contains the following components that are covered by additional
licenses:

-  `BaseTools/Plugin/CodeQL/analyze <https://www.apache.org/licenses/LICENSE-2.0>`__
-  `BaseTools/Source/C/LzmaCompress <BaseTools/Source/C/LzmaCompress/LZMA-SDK-README.txt>`__
-  `BaseTools/Source/C/VfrCompile/Pccts <BaseTools/Source/C/VfrCompile/Pccts/RIGHTS>`__
-  `CryptoPkg/Library/BaseCryptLib/SysCall/inet_pton.c <CryptoPkg/Library/BaseCryptLib/SysCall/inet_pton.c>`__
-  `CryptoPkg/Library/Include/crypto/dso_conf.h <https://github.com/openssl/openssl/blob/e2e09d9fba1187f8d6aafaa34d4172f56f1ffb72/LICENSE>`__
-  `CryptoPkg/Library/Include/openssl/opensslconf.h <https://github.com/openssl/openssl/blob/e2e09d9fba1187f8d6aafaa34d4172f56f1ffb72/LICENSE>`__
-  `MdeModulePkg/Library/LzmaCustomDecompressLib <MdeModulePkg/Library/LzmaCustomDecompressLib/LZMA-SDK-README.txt>`__
-  `OvmfPkg <OvmfPkg/License.txt>`__

The EDK II open source project uses content from upstream projects as git submodules
that are covered by additional licenses.

-  `BaseTools/Source/C/BrotliCompress/brotli <https://github.com/google/brotli/blob/666c3280cc11dc433c303d79a83d4ffbdd12cc8d/LICENSE>`__
-  `CryptoPkg/Library/OpensslLib/openssl <https://github.com/openssl/openssl/blob/e2e09d9fba1187f8d6aafaa34d4172f56f1ffb72/LICENSE>`__
-  `CryptoPkg/Library/MbedTlsLib/mbedtls <https://github.com/Mbed-TLS/mbedtls/blob/8c89224991adff88d53cd380f42a2baa36f91454/LICENSE>`__
-  `MdeModulePkg/Library/BrotliCustomDecompressLib/brotli <https://github.com/google/brotli/blob/666c3280cc11dc433c303d79a83d4ffbdd12cc8d/LICENSE>`__
-  `MdeModulePkg/Universal/RegularExpressionDxe/oniguruma <https://github.com/kkos/oniguruma/blob/abfc8ff81df4067f309032467785e06975678f0d/COPYING>`__
-  `UnitTestFrameworkPkg/Library/Cm...