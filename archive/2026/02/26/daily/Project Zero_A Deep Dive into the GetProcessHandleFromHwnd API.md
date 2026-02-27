---
title: A Deep Dive into the GetProcessHandleFromHwnd API
url: https://projectzero.google/2026/02/gphfh-deep-dive.html
source: Project Zero
date: 2026-02-26
fetch_date: 2026-02-27T04:08:55.644779
---

# A Deep Dive into the GetProcessHandleFromHwnd API

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# A Deep Dive into the GetProcessHandleFromHwnd API

[2026-Feb-26](/2026/02/gphfh-deep-dive.html "Permalink to this post")
James Forshaw

In my previous blog post I mentioned the [`GetProcessHandleFromHwnd`](https://learn.microsoft.com/en-us/windows/win32/winauto/getprocesshandlefromhwnd) API. This was an API I didnât know existed until I found a publicly disclosed [UAC bypass](https://github.com/R41N3RZUF477/QuickAssist_UAC_Bypass) using the Quick Assist UI Access application. This API looked interesting so I thought I should take a closer look.

I typically start by reading the documentation for an API I donât know about, assuming itâs documented at all. It can give you an idea of how long the API has existed as well as its security properties. The documentationâs remarks contain the following three statements that I thought were interesting:

*If the caller has UIAccess, however, they can use a windows hook to inject code into the target process, and from within the target process, send a handle back to the caller.*

*GetProcessHandleFromHwnd is a convenience function that uses this technique to obtain the handle of the process that owns the specified HWND.*

*Note that it only succeeds in cases where the caller and target process are running as the same user.*

The interesting thing about these statements is none of them are completely true. Firstly as the previous blog post outlined itâs not sufficient to have UI Access enabled to use windows hooks, you need to have the same or greater integrity level as the target process. Secondly, if you go and look at how `GetProcessHandleFromHwnd` is implemented in Windows 11 itâs a Win32k kernel function which opens the process directly, not using windows hooks. And finally, the fact that the Quick Assist bypass which uses the API still works with Administrator Protection means the processes can be running as different users.

Of course some of the factual inaccuracies might be changes made to UAC and UI Access over the years since Vista was released. Therefore I thought itâd be interesting to do a quick bit of code archaeology to see how this API has changed over the years and perhaps find some interesting behaviors.

## The First Version

The first version of the API exists in Vista, implemented in the `oleacc.dll` library. The documentation claims it was supported back in Windows XP, but that makes little sense for what the API was designed for. Checking a copy of the library from XP SP3 doesnât show the API, so we can assume the documentation is incorrect. The API first tries to open the process directly, but if that fails itâll use a windows hook exactly as the documentation described.

The `oleacc.dll` library with the hook will be loaded into the process associated with the window using the `SetWindowsHookEx` API and specifying the thread ID parameter. However it still wonât do anything until a custom window message, `WM_OLEACC_HOOK` is sent to the window. The hook function is roughly as follows (Iâve removed error checking):

```
void HandleHookMessage(CWPSTRUCT *cwp) {
  UINT msg = RegisterWindowMessage(L"WM_OLEACC_HOOK");
  if (cwp->message != msg)
	return;
  WCHAR name[64];
  wParam = cwp->wParam;
  StringCchPrintf(name, _countof(name),
                   L"OLEACC_HOOK_SHMEM_%d_%d", wParam,
                   cwp->lParam);
  HANDLE mapping = OpenFileMapping(FILE_MAP_READ |
                                   FILE_MAP_WRITE, FALSE,
                                   name);
  DWORD* buffer = (DWORD*)MapViewOfFile(mapping,
           FILE_MAP_READ | FILE_MAP_WRITE,
		0, 0, sizeof(DWORD));
  HANDLE caller = OpenProcess(PROCESS_DUP_HANDLE, FALSE,
                              cwp->wParam);
  HANDLE current = OpenProcess(PROCESS_DUP_HANDLE |
			  PROCESS_VM_OPERATION | PROCESS_VM_READ |
			  PROCESS_VM_WRITE | SYNCHRONIZE,
                   FALSE, GetCurrentProcessId());
  HANDLE dup;
  DuplicateHandle(CurrentProcess, current, caller, &dup,
                  0, 0, DUPLICATE_SAME_ACCESS);
  InterlockedExchange(buffer, (DWORD)dup);
  // Cleanup handles etc.
}
```

The message parameters are the process ID of the caller, who wants to open the process handle and an incrementing counter. These parameters are used to open a named memory section to transfer the duplicated handle value back to the caller. A copy of the current process handle is then opened with a limited set of access rights and duplicated to the caller. Finally the handle value is copied into the shared memory and the message handler returns. The caller of the API can now pick up the duplicated handle and use it as desired.

This code might explain a few additional things about the API documentation. If the two processes are running as different users itâs possible that the target process wonât be able to open the caller for `PROCESS_DUP_HANDLE` access and the transfer will fail. While the API does set the integrity level of the shared memory it doesnât set the DACL so that will also prevent it being opened by a different user. Of course if the target process was running as an administrator, like in the UAC case, it almost certainly will have access to both the caller process as well as the shared memory making this a moot point.

One minor change was made in Windows 7, the hook function was moved out of the main `oleacc.dll` library into its own binary, `oleacchooks.dll`. The hook function is exposed as ordinal 1 in the export table with no name. This DLL still exists on the latest version of Windows 11 even though the API has since moved into the kernel and thereâs no longer any users.

## The Second Version

The second version of the API doesnât appear until well into Windows 10âs lifetime, in version 1803. This version is where the API was moved into a Win32k kernel function. The kernel API is exposed as `NtUserGetWindowProcessHandle` from `win32kfull.sys`. Itâs roughly implemented as follows:

```
HANDLE NtUserGetWindowProcessHandle(HWND hWnd,
                                    ACCESS_MASK DesiredAccess) {
  WND* wnd = ValidateHwnd(Wnd);
  if (!wnd) {
    return NULL;
  }
  THREADINFO* curr_thread =
                W32GetThreadWin32Thread(KeGetCurrentThread());
  THREADINFO* win_thread = wnd->Thread;;
  if (curr_thread->Desktop != win_thread->Desktop) {
     goto access_denied;
  }

  PROCESSINFO* win_process = win_thread->ppi;
  PROCESSINFO* curr_process = curr_thread->ppi;
  if (gbEnforceUIPI) {
    if (!CheckAccess(curr_process->UIPIInfo,
                     win_process->UIPIInfo)) {
      if (!curr_process->HasUiAccessFlag) {
        goto access_denied;
      }
    }
  }
  else if (win_thread->AuthId != curr_thread->AuthId) {
    goto access_denied;
  }
  if (win_thread->TIF_flags & (TIF_SYSTEMTHREAD |
                                TIF_CSRSSTHREAD)) {
    goto access_denied;
  }

  KPROCESS process = NULL;
  DWORD process_id = PsGetThreadProcessId(win_thread->KThread);
  PsLookupProcessByProcessId(process_id, &process);
  HANDLE handle = NULL;
  ObOpenObjectByPointer(process, 0, NULL, DesiredAccess,
    PsProcessType, KernelMode, &handle);
  return handle;

access_denied:
  UserSetLastError(ERROR_ACCESS_DENIED);
  return NULL;
}
```

One thing to note with the new API is it takes an `ACCESS_MASK` to specify what access the caller wants on the process handle. This is different from the old implementation where the access desired was a fixed value. The window handle is validated and used to lookup the Win32k `THREADI...