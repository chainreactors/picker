---
title: Windows Sockets: From Registered I/O to SYSTEM Privileges
url: https://blog.exodusintel.com/2024/12/02/windows-sockets-from-registered-i-o-to-system-privileges/
source: Exodus Intelligence
date: 2024-12-03
fetch_date: 2025-10-06T19:38:02.244427
---

# Windows Sockets: From Registered I/O to SYSTEM Privileges

[Skip to content](#content "Skip to content")

[![Exodus Intelligence](https://blog.exodusintel.com/wp-content/uploads/2018/10/exodus-final-logo-1_small.png "Exodus Intelligence")](https://blog.exodusintel.com/ "Exodus Intelligence")

Menu

* [Blog](https://blog.exodusintel.com/)
  + [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/)
  + [News](https://blog.exodusintel.com/category/news/)
  + [Training](https://blog.exodusintel.com/category/training/)
  + [Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/)
  + [Other](https://blog.exodusintel.com/category/other/)
* [Offerings](https://exodusintel.com/index.html)
* [Company](https://exodusintel.com/about.html)
* [Capabilities](https://exodusintel.com/zeroday.html)
* [Training](https://exodusintel.com/training.html)
* [Advisories](https://blog.exodusintel.com/advisories/)

[Exodus Blog](https://blog.exodusintel.com)

# Windows Sockets: From Registered I/O to SYSTEM Privileges

* [December 2, 2024](https://blog.exodusintel.com/2024/12/02/)
* [Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

By Luca Ginex

## Overview

This post discusses [CVE-2024-38193](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2024-38193), a use-after-free vulnerability in the afd.sys Windows driver. Specifically, the vulnerability is in the Registered I/O extension for Windows sockets. The vulnerability was patched in the [August 2024 Patch Tuesday](https://msrc.microsoft.com/update-guide/releaseNote/2024-Aug). This post describes the exploitation process for the vulnerability.

First, we give a general overview of the registered I/O extension for Winsock, describing the driver’s internal structures. We then analyze the vulnerability and proceed to detailing the exploitation strategy.

## Preliminaries

In this section we give a general overview of the registered I/O extension for Winsock and describe the relevant structures for registering I/O extensions.

### Winsock Registered I/O Extension

In Windows, the Registered I/O (RIO) extension can be used in socket programming in order to reduce the amount of system calls issued by userland programs while sending and receiving packets. The RIO extension workflow is as follows:

* The userland program registers huge buffers. The kernel then obtains kernel mappings for them.
* The userland program issues send and receive requests by using the receive and send buffer *slices* of the registered buffers.

If a userland program wants to use the Registered I/O extension for sockets, it has to create a socket via the `WSASocketA()` function.
The function’s prototype is as follows:

##

```

					SOCKET WSAAPI WSASocketA(
  [in] int                 af,
  [in] int                 type,
  [in] int                 protocol,
  [in] LPWSAPROTOCOL_INFOA lpProtocolInfo,
  [in] GROUP               g,
  [in] DWORD               dwFlags
);

```

The userland program has to specify the `WSA_FLAG_REGISTERED_IO` flag in the `dwFlags` argument of the call. The program then has to retrieve the function table for the RIO API. This table can be retrieved by issuing a `WSAIoctl()` call with the `SIO_GET_MULTIPLE_EXTENSION_FUNCTION_POINTER` IOCTL code. The call returns a `RIO_EXTENSION_FUNCTION_TABLE` structure. This table contains all the pointers to the RIO API. The definition of the structure is presented in the following code listing:

```

					typedef struct _RIO_EXTENSION_FUNCTION_TABLE {
  DWORD                         cbSize;
  LPFN_RIORECEIVE               RIOReceive;
  LPFN_RIORECEIVEEX             RIOReceiveEx;
  LPFN_RIOSEND                  RIOSend;
  LPFN_RIOSENDEX                RIOSendEx;
  LPFN_RIOCLOSECOMPLETIONQUEUE  RIOCloseCompletionQueue;
  LPFN_RIOCREATECOMPLETIONQUEUE RIOCreateCompletionQueue;
  LPFN_RIOCREATEREQUESTQUEUE    RIOCreateRequestQueue;
  LPFN_RIODEQUEUECOMPLETION     RIODequeueCompletion;
  LPFN_RIODEREGISTERBUFFER      RIODeregisterBuffer;
  LPFN_RIONOTIFY                RIONotify;
  LPFN_RIOREGISTERBUFFER        RIORegisterBuffer;
  LPFN_RIORESIZECOMPLETIONQUEUE RIOResizeCompletionQueue;
  LPFN_RIORESIZEREQUESTQUEUE    RIOResizeRequestQueue;
} RIO_EXTENSION_FUNCTION_TABLE, *PRIO_EXTENSION_FUNCTION_TABLE;

```

Once the function table is obtained, the program has to register the I/O buffers. These buffers will be used for all subsequent I/O operations. In order to do so, the `RIORegisterBuffer()` function must be called.

The function’s prototype is as follows:

```

					RIO_BUFFERID  RIORegisterBuffer(
  _In_ PCHAR DataBuffer,
  _In_ DWORD DataLength
);

```

The `DataBuffer` argument is a pointer to the buffer to be used and the `DataLength` argument is the size of the buffer. The function returns a `RIO\_BUFFERID` buffer descriptor, which is an opaque integer that identifies the registered buffer in the kernel.

In order to send or receive data from the socket, the `RIOSend()` and the `RIOReceive()` functions can be used. These functions accept a `RIO\_BUF` structure that describes a \*slice\* of the registered buffers to be used. The definition of the `RIO\_BUF` structure is as follows:

```

					typedef struct _RIO_BUF {
  RIO_BUFFERID BufferId;
  ULONG        Offset;
  ULONG        Length;
} RIO_BUF, *PRIO_BUF;

```

### Kernel Structures

Structure definitions are obtained by reverse engineering and may not accurately reflect structures defined in the source code. The recovered structure definition for the registered buffer is as follows:

```

					struct RIOBuffer {
  PMDL AssociatedMDL;
  _QWORD VirtualAddressBuffer;
  _DWORD LengthBuffer;
  _DWORD RefCount;
  _DWORD IsInvalid;
  _DWORD Unknown;
};

```

This kernel structure is used by the `afd.sys` driver to keep track of the registered buffer. It contains the following fields:

* `AssociatedMDL`: A pointer to the MDL that describes the userland buffer.
* `VirtualAddressBuffer`: A virtual kernel pointer that can be used by the kernel driver to write/read to the userland buffer.
* `LengthBuffer`: The size of the userland buffer.
* `RefCount`: Field that keeps track of the number of references to this buffer.
* `IsInvalid`: Field that encodes the state of the buffer. `0` means that it is in use, `1` means that it is freed and `2` means that it has to be
  freed.
* `Unknown`: Reserved.

The `afd.sys` driver keeps all the `RIOBuffer` structures in an array, one entry for each registered buffer. The `afd.sys` driver also creates, for efficiency reasons, a *cache* for the most recently used `RIOBuffer` elements of the array. Each entry in the cache has the following structure:

```

					struct CachedBuffer {
  _DWORD IdBuffer;
  _DWORD RefCount;
  RIOBuffer *BufferPtr;
};

```

It contains the following fields:

* `IdBuffer`: The integer identifier associated with the registered buffer.
* `RefCount`: Reference counter for the cached entry.
* `BufferPtr`: Pointer to the `RIOBuffer` structure this entry is mirroring.

The following image is a visual representation of the afd.sys RIO component.

![](https://blog.exodusintel.com/wp-content/uploads/2024/12/img1.png)

afd.sys RIO component

## Vulnerability

The use-after-free vulnerability is caused by a race condition between the `AfdRioGetAndCacheBuffer()` and `AfdRioDereferenceBuffer()` functions. The `AfdRioGetAndCacheBuffer()` function needs to access the registered buffers involved in send/receive operations, therefore it temporarily increments the reference counter of the involved registered buffers by using the `_InterlockedIncrement()`intrinsic function.

The `AfdRioDereferenceBuffer()` function is called when a usermode application calls the `RIODeregister()` API function. This function checks the reference counter’s value associated with the registered buffer that the usermode appl...