---
title: UDRL, SleepMask, and BeaconGate
url: https://rastamouse.me/udrl-sleepmask-and-beacongate/
source: Rasta Mouse
date: 2024-12-01
fetch_date: 2025-10-06T19:37:22.338678
---

# UDRL, SleepMask, and BeaconGate

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

30 Nov 2024

7 min read

# UDRL, SleepMask, and BeaconGate

I've been looking into Cobalt Strike's UDRL, SleepMask, and BeaconGate features over the last couple of days. It took me some time to understand the relationship between these capabilities, so the aim of this post is to provide a concise overview for those looking into these aspects of Beacon, and hopefully provide a leg-up for developers. Each of these features can be used independently to bring custom evasion capabilities to different parts of Beacon, but perhaps more interestingly, they can also interoperate to some degree.

## User-Defined Reflective Loader

Beacon is nothing more than a Windows DLL that needs to be loaded into a process to run. There are multiple ways to do this, but Beacon is designed after Stephen Fewer's [Reflective DLL Injection](https://github.com/stephenfewer/ReflectiveDLLInjection) technique. This is a DLL that's responsible for loading itself by implementing its own PE loader. The DLL exports a function called *ReflectiveLoader*, which when called, walks over its own image and maps a new copy of itself into memory. It must satisfy the DLL's runtime requirements by resolving its import table and performing relocations etc. It then locates and executes its entry point, DllMain, at which point, Beacon is up and running.

The behaviour of the reflective loader can be influenced via Malleable C2. For example, one of the things `stage.obfuscate` does is instruct the reflective loader to map Beacon into memory without its headers. There are other options such as `stage.allocator`, which changes the API used to allocate new memory for Beacon; `stage.magic_pe` overrides the PE character marker in Beacon's NT Headers; and `stage.stomppe` instructs the reflective loader to stomp the `MZ`, `PE`, and `e_lfanew` values after it maps Beacon into memory.

The User-Defined Reflective Loader (UDRL) allows operators to replace Beacon's default reflective loader with their own custom implementation. This allows them to go above and beyond the customisations exposed by Malleable C2. Want to use an allocation API that isn't available in `stage.allocator`? No problem. Want to stomp more bytes than `stage.magic_mz` permits? Go for it.

This is the structure of what a very basic UDRL could look like (lots of code excluded for brevity).

```
extern "C" {
#pragma code_seg(".text$a")
    ULONG_PTR __cdecl ReflectiveLoader() {
        // determine start address of loader
#ifdef _WIN64
        void* loaderStart = &ReflectiveLoader;
#elif _WIN32
        void* loaderStart = (char*)GetLocation() - 0xE;
#endif
        // determine base address of Beacon DLL
        ULONG_PTR rawDllBaseAddress = FindBufferBaseAddress();

        // parse NTHeaders
        PIMAGE_DOS_HEADER rawDllDosHeader = (PIMAGE_DOS_HEADER)rawDllBaseAddress;
        PIMAGE_NT_HEADERS rawDllNtHeader = (PIMAGE_NT_HEADERS)(rawDllBaseAddress + rawDllDosHeader->e_lfanew);

        // resolve the functions needed by the loader
        _PPEB pebAddress = GetPEBAddress();
        WINDOWSAPIS winApi = { 0 };
        if (!ResolveBaseLoaderFunctions(pebAddress, &winApi)) {
            return NULL;
        }

        // allocate memory for Beacon, yolo RWX
        ULONG_PTR loadedDllBaseAddress = (ULONG_PTR)winApi.VirtualAlloc(NULL, rawDllNtHeader->OptionalHeader.SizeOfImage, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);
        if (loadedDllBaseAddress == NULL) {
            return NULL;
        }

        // map sections
        if (!CopyPESections(rawDllBaseAddress, loadedDllBaseAddress)) {
            return NULL;
        };

        // resolve Beacon's import table...
        ResolveImports(rawDllNtHeader, loadedDllBaseAddress, &winApi);

        // perform relocations...
        ProcessRelocations(rawDllNtHeader, loadedDllBaseAddress);

        // calculate Beacon's entry point
        ULONG_PTR entryPoint = loadedDllBaseAddress + rawDllNtHeader->OptionalHeader.AddressOfEntryPoint;

        // flush instruction cache to avoid stale code being used
        winApi.NtFlushInstructionCache((HANDLE)-1, NULL, 0);

        // call Beacon's entrypoints
        ((DLLMAIN)entryPoint)((HINSTANCE)loadedDllBaseAddress, DLL_PROCESS_ATTACH, NULL);
        ((DLLMAIN)entryPoint)((HINSTANCE)loaderStart, DLL_BEACON_START, NULL);

        // return address of entry point to caller
        return entryPoint;
    }
}
```

ReflectiveLoader.cpp

One caveat to be aware of when using a UDRL is that any options that are defined in the `stage` block of the loaded C2 profile will be ignored. This is by design because the philosophy of the UDRL is to put the developer in the driving seat. However, this can cause confusion when using the default Sleep Mask, because it does use `stage.userwx` as a hint when masking and unmasking Beacon memory. For instance, if `stage.userwx` is set to `true` but a UDRL allocates memory as R/RW/RX (as appropriate for each section), the Sleep Mask will either be unable to mask all of Beacon's section (leaving them in the clear) or it will try to and simply crash because it didn't know it needed to make memory writeable first.

As an aside, it's also worth noting that this UDRL is not the same reflective loader used for Beacon's fork & run post-ex commands (execute-assembly, powerpick, etc). Operators can write a custom post-ex UDRL to replace the default one (they're nearly identical). However, in the same way that a custom UDRL ignores options from the `stage` block of Malleable C2; a custom post-ex UDRL ignores options from the `post-ex` block.

## Custom Sleep Masks

The issue of memory allocations can be completely mitigated when using a custom Sleep Mask and UDRL because a UDRL can actually pass information about memory it has allocated to the Sleep Mask, via Beacon. This can not only include memory allocated for Beacon's sections (.data, .text, etc) but also any custom memory allocations a developer wishes to make.

This data is provided via an `ALLOCATED_MEMORY_REGION` structure.

```
typedef struct _ALLOCATED_MEMORY_REGION {
    ALLOCATED_MEMORY_PURPOSE Purpose;      // A label to indicate the purpose of the allocated memory
    PVOID  AllocationBase;                 // The base address of the allocated memory block
    SIZE_T RegionSize;                     // The size of the allocated memory block
    DWORD Type;                            // The type of memory allocated
    ALLOCATED_MEMORY_SECTION Sections[8];  // An array of section information structures
    ALLOCATED_MEMORY_CLEANUP_INFORMATION CleanupInformation; // Information required to cleanup the allocation
} ALLOCATED_MEMORY_REGION, *PALLOCATED_MEMORY_REGION;

typedef struct {
    ALLOCATED_MEMORY_REGION AllocatedMemoryRegions[6];
} ALLOCATED_MEMORY, *PALLOCATED_MEMORY;
```

BeaconUserData.h

This is then passed to Beacon by calling DllMain with a 'reason' of `DLL_BEACON_USER_DATA`, prior to calling with `DLL_BEACON_START`.

```
// pass Beacon User Data (BUD) to Beacon
((DLLMAIN)entryPoint)(0, DLL_BEACON_USER_DATA, &userData);

// call Beacon's entrypoints
((DLLMAIN)entryPoint)((HINSTANCE)loadedDllBaseAddress, DLL_PROCESS_ATTACH, NULL);
((DLLMAIN)entryPoint)((HINSTANCE)loaderStart, DLL_BEACON_START, NULL);
```

ReflectiveLoader.cpp

When Beacon is ready to sleep, execution is passed to the Sleep Mask with a `PSLEEPMASK_INFO` structure.

```
void sleep_mask(PSLEEPMASK_INFO info, PFUNCTION_CALL funcCall)
```

The allocated memory data is available inside the `BEACON_INFO` structure, which can be looped over and handled as desired.

```
info->beacon_info.allocatedMemory.AllocatedMemoryRegions
```

## System Calls

Developers can also replace Beacon's default syscall resolver (which I believe is based on SysWhispers3(?)) with something else entirely (Hell's Gate, Halo's Gate, Tartarus' Gate, RecycledGate, etc). Resolve the syscall numbers and function pointers in the UDRL, and populate th...