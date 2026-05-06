---
title: C/C++ checklist challenges, solved
url: https://blog.trailofbits.com/2026/05/05/c/c-checklist-challenges-solved/
source: The Trail of Bits Blog
date: 2026-05-05
fetch_date: 2026-05-06T05:09:13.827435
---

# C/C++ checklist challenges, solved

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# C/C++ checklist challenges, solved

[Graham Sutherland](/authors/graham-sutherland/), [Paweł Płatek](/authors/pawe%C5%82-p%C5%82atek/)

May 05, 2026

[c/c++](/categories/c/c%2B%2B/), [testing handbook](/categories/testing-handbook/), [large-language-models](/categories/large-language-models/)

Page content

* [The Linux ping program challenge](#the-linux-ping-program-challenge)
* [The Windows driver registry challenge](#the-windows-driver-registry-challenge)
  + [An attacker-controlled registry path](#an-attacker-controlled-registry-path)
  + [Missing type checks with RTL\_QUERY\_REGISTRY\_DIRECT](#missing-type-checks-with-rtl_query_registry_direct)
  + [A first attempt at exploitation](#a-first-attempt-at-exploitation)
  + [Finding writable keys in trusted hives](#finding-writable-keys-in-trusted-hives)
  + [A string is a type of integer, right?](#a-string-is-a-type-of-integer-right)
  + [A fully controlled stack overwrite with REG\_BINARY](#a-fully-controlled-stack-overwrite-with-reg_binary)
* [Your turn](#your-turn)

We recently added a [C/C++ security checklist](https://appsec.guide/docs/languages/c-cpp/) to the Testing Handbook and [challenged readers to spot the bugs in two code samples](https://blog.trailofbits.com/2026/04/09/master-c-and-c-with-our-new-testing-handbook-chapter/): a deceptively simple Linux ping program and a Windows driver registry handler. If you found the `inet_ntoa` global buffer gotcha or the missing `RTL_QUERY_REGISTRY_TYPECHECK` flag, nice work. If not, here’s a full walkthrough of both challenges, plus a deep dive into how the Windows registry type confusion escalates from a local denial of service to a kernel write primitive.

Since we first released the new C/C++ security checklist, we also developed a new Claude skill, [c-review](https://github.com/trailofbits/skills/tree/main/plugins/c-review). It turns the checklist into bug-finding prompts that an LLM can run against a codebase. It’s also platform and threat-model aware. Run these commands to install the skill:

```
claude skills add-marketplace https://github.com/trailofbits/skills
claude skills enable c-review --marketplace trailofbits/skills
```

## The Linux ping program challenge

The Linux warmup challenge we showed you in the last blog post has an obvious command injection issue.

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

There are three validations that have to be bypassed before the `system` call can be reached with malicious inputs:

1. The [`inet_aton` function](https://man7.org/linux/man-pages/man3/inet.3.html) “converts the Internet host address from the IPv4 numbers-and-dots notation into binary form” and “returns nonzero if the address is valid, zero if not.” Theoretically, if we provide an invalid IPv4 string as input, then the program should return early.
2. The `ntohl` call aims to prevent server-side request forgery (SSRF) attacks by disallowing addresses in 127.0.0.0/8 range.
3. The parsed IP address is normalized with an `inet_ntoa` call and compared against the `ALLOWED_IP`. We are only allowed to ping localhost, which should not be possible given the SSRF check (making the code effectively broken with this configuration).

The issue with the `inet_aton` function is that it [accepts trailing garbage](https://sourceware.org/bugzilla/show_bug.cgi?id=20018). This behavior is not documented on its man page, making it a likely source of vulnerabilities. In our challenge, one can simply send “127.0.0.1 ‘; anything #” as valid input.

The gotcha with `inet_ntoa` is that it returns a pointer to a global buffer. Therefore, subsequent calls to the function overwrite previous outputs. In the challenge, `ip_addr_resolved` and `trusted_resolved` are the same pointer. When we provide “1.2.3.4” as input, `ip_addr_resolved` points to the string “1.2.3.4”, the SSRF check passes, the second call to `inet_ntoa` makes the `ip_addr_resolved` pointer point to “127.3.3.1”, and so the `strcmp` check passes too.

There are a few more functions that return pointers to static buffers; these are documented in the new C/C++ Testing Handbook chapter.

## The Windows driver registry challenge

We showed you this Windows Driver Framework (WDF) request handler from a Windows driver and asked you to spot the bugs.

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
    RtlZeroMemory(regQueryTable, sizeof(RTL_QUERY_REGISTRY_TABLE) * 2);
    regQueryTable[0].Name = L"MinorVersion";
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
        "%!FUNC! Failed to query registry. Status: %d",
        (int)status
      );
      return status;
    }
    TraceEvents(
      TRACE_LEVEL_INFORMATION,
      TRACE_QUEUE,
      "%!FUNC! Minor version is %d", (int)readValue
    );
    version.Minor = readValue;
    if (!DoesVersionSupportNewCallback(version))
    {
      handlerCallback = OldCallback;
    }...