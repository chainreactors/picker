---
title: WindowsProtocolTestSuites v4.26.9.0
url: https://kitploit.com/en/posts/github-microsoft-windowsprotocoltestsuites-42690
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:59.317066
---

# WindowsProtocolTestSuites v4.26.9.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13962/73b04682fd55192ef22811edabf2922c2a4c21c31970d87a30facd047f9f7e18.png)

New releaseSep 4, 2026

# WindowsProtocolTestSuites v4.26.9.0

⭐⭐ Join us at SNIA SDC for the SMB3 IO Lab (September 28 - October 1, 2026), see upcoming Interoperability Events

Share

# Windows Protocol Test Suites

**Windows Protocol Test Suites** provide interoperability testing against the implementation of Windows open specifications including File Services, Identity Management, Remote Desktop and etc.

Originally developed for in-house testing of the Microsoft Open Specifications, Microsoft Protocol Test Suites have been used extensively during Plugfests and interoperability labs to test against partner implementations.
A Test Suite evaluates whether a protocol or protocol family implementation meets certain interoperability requirements.
Test Suites do not cover every protocol requirement and in no way certify an implementation, even if all tests pass.
However, each test suite provides users with a useful indication of interoperability.

* **File Server Family Test Suite**. It is designed to test implementations of file server protocol family including [MS-SMB2], [MS-DFSC], [MS-SWN], [MS-FSRVP], [MS-FSA], [MS-FSCC], [MS-RSVD] and [MS-SQOS].
  To get started with File Server test suite, you can refer to the [File Server Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/FileServer/docs/FileServerUserGuide.md). To create a disposable Azure test environment, use the [File Server Azure automated deployment](https://github.com/microsoft/windowsprotocoltestsuites/blob/main/TestSuites/FileServer/azure-automation/README.md).
* **RDP Client Family Test Suite**. It provides interoperability testing for client implementation of RDP family protocols including [MS-RDPBCGR], [MS-RDPEDISP], [MS-RDPEDYC], [MS-RDPEGFX], [MS-RDPEGT], [MS-RDPEI], [MS-RDPEMT], [MS-RDPEUDP], [MS-RDPEUSB], [MS-RDPEVOR] and [MS-RDPRFX]. To get started with RDP Client test suite, you can refer to the [RDP Client Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/RDP/Client/docs/RDP_ClientUserGuide.md)
* **RDP Server Family Test Suite**. It provides interoperability testing for server implementation of RDP family protocols including [MS-RDPBCGR], [MS-RDPEDYC], [MS-RDPEMT] and [MS-RDPELE]. To get started with RDP Server test suite, you can refer to the [RDP Server Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/RDP/Server/Docs/RDP_ServerUserGuide.md)
* **Kerberos Server Test Suite**. It is designed to test server implementations of Kerberos protocols including [MS-KILE], [MS-KKDCP] and [MS-PAC]. To get started with Kerberos Server test suite, you can refer to the [Kerberos Server Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/Kerberos/docs/Kerberos_ServerUserGuide.md)
* **SMBD Server Test Suite**. It is designed to test the implementations of SMB2&3 direct (RDMA) protocol, as specified in [MS-SMBD] and [MS-SMB2]. To get started with SMBD Server test suite, you can refer to the [SMBD Server Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/MS-SMBD/docs/MS-SMBD_ServerUserGuide.md)
* **Branch Cache Test Suite**. It is designed to test the implementations of [MS-PCCRTP], [MS-PCCRR], [MS-PCHC] and [MS-PCCRC] protocol. To get started with Branch Cache test suite, you can refer to the [Branch Cache Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/BranchCache/docs/BranchCache_UserGuide.md)
* **AZOD Test Suite**. It is designed to test the implementations of [MS-AZOD] protocol. To get started with AZOD test suite, you can refer to the [AZOD Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/MS-AZOD/docs/MS-AZOD_ODUserGuide.md)
* **ADFamily Test Suite**. It is designed to test the implementations of the Active Directory protocols including [MS-ADA1], [MS-ADA2], [MS-ADA3], [MS-ADLS], [MS-ADSC], [MS-ADTS], [MS-APDS], [MS-DRSR], [MS-FRS2], [MS-LSAD], [MS-LSAT], [MS-SAMR] and [MS-NRPC]. To get started with ADFamily test suite, you can refer to the [ADFamily Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/ADFamily/docs/ADFamily_ServerUserGuide.md)
* **ADFSPIP Client Test Suite**. It is designed to test the implementations of ADFS Proxy and Web Application Proxy integration, as described in [MS-ADFSPIP]. To get started with ADFSPIP Client test suite, you can refer to the [ADFSPIP Client Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/MS-ADFSPIP/Docs/MS-ADFSPIP_ClientUserGuide.md)
* **ADOD Test Suite**. It is designed to test the implementations of [MS-ADOD] protocol. To get started with ADOD test suite, you can refer to the [ADOD Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/MS-ADOD/Docs/MS-ADOD_ODUserGuide.md)
* **XCA Test Suite**. It is designed to test the implementations of [MS-XCA] protocol. To get started with XCA test suite, you can refer to the [XCA Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/MS-XCA/docs/MS-XCA_TestSuiteUserGuide.md)
* **WSP Test Suite**. It is designed to test the implementations of [MS-WSP] protocol. To get started with WSP test suite, you can refer to the [WSP Test Suite User Guide](https://github.com/microsoft/WindowsProtocolTestSuites/blob/main/TestSuites/MS-WSP/docs/MS-WSP_TestSuiteUserGuide.md)

## Components

Windows Protocol Test Suites contain below components:

* **CommonScripts**. Common scripts used by each test suite. Normally they're used to deploy the environment.
* **ProtoSDK**. The protocol library used by each test suite. It provides the data structures of the protocol messages, the methods to encode and decode the messages, the methods to send and receive messages and etc.
* **TestSuites**. All Test Suites code and documents are saved here and categorized by folder representing each test suite.
* **ProtocolTestManager**. A tool to help you configure and run test suites.

## Prerequisites

**Windows Protocol Test Suites** are based on [.NET](https://dotnet.microsoft.com/) so they can be developed and run across different platforms.
You should install the software listed below based on your testing purpose, including their own dependencies.

1. .NET and related components

   a. For Windows, Linux and macOS, install [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0/) to build or run test suites.

   b. For those who work on Windows and prefer IDE, install [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) or higher ([Visual Studio 2022 Community](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=17) recommended), together with these individual components from the installer:

   | Section | Individual Component in Visual Studio 2022 | Run Windows Protocol Test Suites | Build Windows Protocol Test Suites from source code |
   | --- | --- | --- | --- |
   | .NET | .NET SDK | Required | Required |
   | Compilers, build tools, and runtime | C# and Visual Basic Roslyn compilers |  | Required |
   | Compilers, build tools, and runtime | MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest) |  | Required[1](#footnote1) |
   | Compilers, build tools, and runtime | C++/CLI support fo...