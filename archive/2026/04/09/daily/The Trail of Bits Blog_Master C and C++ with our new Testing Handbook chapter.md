---
title: Master C and C++ with our new Testing Handbook chapter
url: https://blog.trailofbits.com/2026/04/09/master-c-and-c-with-our-new-testing-handbook-chapter/
source: The Trail of Bits Blog
date: 2026-04-09
fetch_date: 2026-04-10T04:45:03.912133
---

# Master C and C++ with our new Testing Handbook chapter

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Master C and C++ with our new Testing Handbook chapter

[Graham Sutherland](/authors/graham-sutherland/), [Paweł Płatek](/authors/pawe%C5%82-p%C5%82atek/)

April 09, 2026

[c/c++](/categories/c/c%2B%2B/), [testing handbook](/categories/testing-handbook/), [application-security](/categories/application-security/)

Page content

* [What’s in the chapter](#whats-in-the-chapter)
* [Test your review skills](#test-your-review-skills)
  + [The many quirks of Linux libc](#the-many-quirks-of-linux-libc)
  + [Windows driver registry gotchas](#windows-driver-registry-gotchas)
* [We’re not done yet](#were-not-done-yet)

We added a new chapter to our Testing Handbook: [a comprehensive security checklist for C and C++ code](https://appsec.guide/docs/languages/c-cpp/). We’ve identified a broad range of common bug classes, known footguns, and API gotchas across C and C++ codebases and organized them into sections covering Linux, Windows, and seccomp. Whereas other handbook chapters focus on static and dynamic analysis, this chapter offers a strong basis for manual code review.

LLM enthusiasts rejoice: we’re also developing a Claude skill based on this new chapter. It will turn the checklist into bug-finding prompts that an LLM can run against a codebase, and it’ll be platform and threat-model aware. Be sure to give it a try when we release it.

And after reading the chapter, you can test your C/C++ review skills against two challenges at the end of this post. Be in the [first 10 to submit correct answers](http://trailofbits.com/c-whats-wrong-challenge/) to win Trail of Bits swag!

## What’s in the chapter

The chapter covers five areas: general bug classes, Linux usermode and kernel, Windows usermode and kernel, and seccomp/BPF sandboxes. It starts with language-level issues in the bug classes section—memory safety, integer errors, type confusion, compiler-introduced bugs—and gets progressively more environment-specific.

The Linux usermode section focuses on libc gotchas. This section is also applicable to most POSIX systems. It ranges from well-known problems with string methods, to somewhat less known caveats around privilege dropping and environment variable handling. The Linux kernel is a complicated beast, and no checklist could cover even a part of its intricacies. However, our new Testing Handbook chapter can give you a starting point to bootstrap manual reviews of drivers and modules.

The Windows sections cover DLL planting, unquoted path vulnerabilities in `CreateProcess`, and path traversal issues. This last bug class includes concerns like [WorstFit Unicode bugs](https://devco.re/blog/2025/01/09/worstfit-unveiling-hidden-transformers-in-windows-ansi/), where characters outside the basic ANSI set can be reinterpreted in ways that bypass path checks entirely. The kernel section addresses driver-specific concerns such as device access controls, denial of service through improper spinlock usage, security issues arising from passing handles from usermode to kernelmode, and various sharp edges in Windows kernel APIs.

Linux [seccomp](https://man7.org/linux/man-pages/man2/seccomp.2.html) and [BPF](https://man7.org/linux/man-pages/man2/bpf.2.html) features are often used for sandboxing. While more modern tools like [Landlock](https://docs.kernel.org/userspace-api/landlock.html) and [namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) exist for this task, we still see a combination of these older features during audits. And we always uncover a lot of issues. The new Testing Handbook chapter covers sandbox bypasses we’ve seen, like `io_uring` syscalls that execute without the BPF filter ever seeing them, the [`CLONE_UNTRACED`](https://man7.org/linux/man-pages/man2/clone.2.html) flag that lets a tracee effectively disable seccomp filters, and memory-level race conditions in ptrace-based sandboxes.

## Test your review skills

We’ve provided two challenges below that contain real bug classes from the checklist. Try to spot the issues, then [submit your answers](http://trailofbits.com/c-whats-wrong-challenge). If you’re in the first 10 to submit correct answers, you’ll receive Trail of Bits swag. The challenge will close April 17, so get your answers in before then.

Stuck? Don’t worry. We’ll be publishing the answers in a follow-up blog post, so don’t forget to #like and #subscribe, by which we mean [add our RSS feed to your reader](https://blog.trailofbits.com/index.xml).

### The many quirks of Linux libc

In this simple ping program, there are two libc gotchas that make the program trivially exploitable. Can you find and explain the issues? If you can’t, check out the handbook chapter. Both bugs are covered in the Linux usermode section.

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define ALLOWED_IP "127.3.3.1"

int main() {
    char ip_addr[128];
    struct in_addr to_ping_host, trusted_host;

    // get address
    if (!fgets(ip_addr, sizeof(ip_addr), stdin))
        return 1;
    ip_addr[strcspn(ip_addr, "\n")] = 0;

    // verify address
    if (!inet_aton(ip_addr, &to_ping_host))
        return 1;
    char *ip_addr_resolved = inet_ntoa(to_ping_host);

    // prevent SSRF
    if ((ntohl(to_ping_host.s_addr) >> 24) == 127)
        return 1;

    // only allowed
    if (!inet_aton(ALLOWED_IP, &trusted_host))
        return 1;
    char *trusted_resolved = inet_ntoa(trusted_host);

    if (strcmp(ip_addr_resolved, trusted_resolved) != 0)
        return 1;

    // ping
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "ping '%s'", ip_addr);
    system(cmd);
    return 0;
}
```

### Windows driver registry gotchas

This Windows Driver Framework (WDF) driver request handler queries product version values from the registry. There are several bugs here, including an easy-to-exploit denial of service, but one of them leads to kernel code execution by messing with the registry values. Can you figure out the bug and how to exploit it?

```
NTSTATUS
InitServiceCallback(
  _In_ WDFREQUEST Request
)
{
  NTSTATUS status;
  PWCHAR regPath = NULL;
  size_t bufferLength = 0;

  // fetch the product registry path from the request
  status = WdfRequestRetrieveInputBuffer(Request, 4, &regPath, &bufferLength);
  if (!NT_SUCCESS(status))
  {
    TraceEvents(
      TRACE_LEVEL_ERROR,
      TRACE_QUEUE,
      "%!FUNC! Failed to retrieve input buffer. Status: %d", (int)status
    );
    return status;
  }
  /* check that the buffer size is a null-terminated
     Unicode (UTF-16) string of a sensible size */
  if (bufferLength < 4 ||
    bufferLength > 512 ||
    (bufferLength % 2) != 0 ||
    regPath[(bufferLength / 2) - 1] != L'\0')
  {
    TraceEvents(
      TRACE_LEVEL_ERROR,
      TRACE_QUEUE,
      "%!FUNC! Buffer length %d was incorrect.", (int)bufferLength
    );
    return STATUS_INVALID_PARAMETER;
  }

  ProductVersionInfo version = { 0 };
  HandlerCallback handlerCallback = NewCallback;
  int readValue = 0;
  // read the major version from the registry
  RTL_QUERY_REGISTRY_TABLE regQueryTable[2];
  RtlZeroMemory(regQueryTable, sizeof(RTL_QUERY_REGISTRY_TABLE) * 2);
  regQueryTable[0].Name = L"MajorVersion";
  regQueryTable[0].EntryContext = &readValue;
  regQueryTable[0].Flags = RTL_QUERY_REGISTRY_DIRECT;
  regQueryTable[0].QueryRoutine = NULL;
  status = RtlQueryRegistryValues(
    RTL_REGISTRY_ABSOLUTE,
    regPath,
    regQueryTable,
    NULL,
    NULL
  );
  if (!NT_SUCCESS(status))
  {
    TraceEvents(
      TRACE_LEVEL_ERROR,
      TRACE_QUEUE,
      "%!FUNC! Failed to query registry. Status: %d", (int)status
    );
    return status;
  }
  TraceEvents(
    TRACE_LEVEL_INFORMATION,
    TRACE_QUEUE,
    "%!FUNC! Major version is %d",
    (int)readValue
  );
  version.Major = readValue;
  if (version.Major < 3)
  {
    // versions prior to 3.0 need an additional check
...