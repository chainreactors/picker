---
title: Islands of Invariance
url: https://rastamouse.me/islands-of-invariance/
source: Rasta Mouse
date: 2026-03-04
fetch_date: 2026-03-05T04:07:37.268611
---

# Islands of Invariance

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

04 Mar 2026

6 min read

# Islands of Invariance

In my post [Cracking the Crystal Palace](https://rastamouse.me/cracking-the-crystal-palace/), I explored several aspects of Crystal Palace that remain unchanged after `+optimize` and `+mutate` passes have been performed. These are "islands of invariance", or to put it another way, predicatable parts of Crystal Palace output that don't change, and can therefore be used as a basis for writing YARA rules.

ℹ️

As an aside, `__resolve_hook` works slightly differently now, so the specific rule in that post is no longer applicable.

Since then, an entire YARA generator has been built into Crystal Palace, which automatically emits signatures based on these invariances. There are two ways to generate them, depending on how you use Crystal Palace. The first is via the Java API, the second is via the `link` tool.

The following example is from the [Simple RDLL](https://tradecraftgarden.org/simple.html) loader.

```
$ ./link ../tcg/simple_rdll/loader.spec demo/test.x64.dll out.bin -g cpl.yar
```

```
rule TCG_5c837b65 {
	meta:
		date = "2026-03-04"
		arch_context = "x64"
		scan_context = "file, memory"
		os = "windows"
		generator = "Crystal Palace"
	strings:
		// ----------------------------------------
		// Function: go
		// ----------------------------------------
		/*
		 * E8 62 04 00 00                call SizeOfDLL
		 * 89 C0                         mov eax, eax
		 * 41 B9 40 00 00 00             mov r9d, 0x40
		 * 41 B8 00 30 00 00             mov r8d, 0x3000
		 * (Score: 45)
		 */
		$r0_go = { E8 ?? ?? ?? ?? 89 C0 41 B9 40 00 00 00 41 B8 00 30 00 00 }

		// ----------------------------------------
		// Function: findModuleByHash
		// ----------------------------------------
		/*
		 * 4D 8B 42 50                   mov r8, qword ptr [r10+0x50]
		 * 41 0F B7 42 48                movzx eax, word ptr [r10+0x48]
		 * 83 E8 01                      sub eax, 1
		 * 0F B7 C0                      movzx eax, ax
		 * (Score: 52)
		 */
		$r1_findModuleByHash = { 4D 8B 42 50 41 0F B7 42 48 83 E8 01 0F B7 C0 }

		// ----------------------------------------
		// Function: findFunctionByHash
		// ----------------------------------------
		/*
		 * 49 01 DB                      add r11, rbx
		 * 45 8B 43 20                   mov r8d, dword ptr [r11+0x20]
		 * 49 01 D8                      add r8, rbx
		 * 45 8B 4B 24                   mov r9d, dword ptr [r11+0x24]
		 * (Score: 72)
		 */
		$r2_findFunctionByHash = { 49 01 DB 45 8B 43 20 49 01 D8 45 8B 4B 24 }

		/*
		 * 41 0F B7 11                   movzx edx, word ptr [r9]
		 * 41 8B 43 1C                   mov eax, dword ptr [r11+0x1C]
		 * 48 8D 14 93                   lea rdx, [rbx+rdx*4]
		 * 8B 04 02                      mov eax, dword ptr [rdx+rax]
		 * (Score: 60)
		 */
		$r3_findFunctionByHash = { 41 0F B7 11 41 8B 43 1C 48 8D 14 93 8B 04 02 }

		// ----------------------------------------
		// Function: ProcessRelocation
		// ----------------------------------------
		/*
		 * 41 8B 41 04                   mov eax, dword ptr [r9+4]
		 * 48 83 E8 08                   sub rax, 8
		 * 48 D1 E8                      shr rax, 1
		 * 49 8D 51 08                   lea rdx, [r9+8]
		 * (Score: 54)
		 */
		$r4_ProcessRelocation = { 41 8B 41 04 48 83 E8 08 48 D1 E8 49 8D 51 08 }

		/*
		 * 4D 89 D3                      mov r11, r10
		 * 49 C1 EB 10                   shr r11, 0x10
		 * 8D 40 FF                      lea eax, [rax-1]
		 * 49 8D 4C 41 0A                lea rcx, [r9+rax*2+0xA]
		 * (Score: 77)
		 */
		$r5_ProcessRelocation = { 4D 89 D3 49 C1 EB 10 8D 40 FF 49 8D 4C 41 0A }

		// ----------------------------------------
		// Function: ProcessRelocations
		// ----------------------------------------
		/*
		 * 48 89 F1                      mov rcx, rsi
		 * E8 2C FF FF FF                call ProcessRelocation
		 * 8B 43 04                      mov eax, dword ptr [rbx+4]
		 * 48 01 C3                      add rbx, rax
		 * 83 7B 04 00                   cmp dword ptr [rbx+4], 0
		 * (Score: 42)
		 */
		$r6_ProcessRelocations = { 48 89 F1 E8 ?? ?? ?? ?? 8B 43 04 48 01 C3 83 7B 04 00 }

		// ----------------------------------------
		// Function: ProcessImport
		// ----------------------------------------
		/*
		 * 41 8B 49 0C                   mov ecx, dword ptr [r9+0xC]
		 * 4C 01 C1                      add rcx, r8
		 * FF 17                         call qword ptr [rdi]
		 * 49 89 C4                      mov r12, rax
		 * 8B 5E 10                      mov ebx, dword ptr [rsi+0x10]
		 * (Score: 74)
		 */
		$r7_ProcessImport = { 41 8B 49 0C 4C 01 C1 FF 17 49 89 C4 8B 5E 10 }

		/*
		 * 4C 89 E1                      mov rcx, r12
		 * FF 57 08                      call qword ptr [rdi+8]
		 * 48 89 DA                      mov rdx, rbx
		 * 48 89 43 F8                   mov qword ptr [rbx-8], rax
		 * (Score: 40)
		 */
		$r8_ProcessImport = { 4C 89 E1 FF 57 08 48 89 DA 48 89 43 F8 }

		// ----------------------------------------
		// Function: ParseDLL
		// ----------------------------------------
		/*
		 * 48 01 C1                      add rcx, rax
		 * 48 89 4A 08                   mov qword ptr [rdx+8], rcx
		 * 48 83 C1 18                   add rcx, 0x18
		 * 48 89 4A 10                   mov qword ptr [rdx+0x10], rcx
		 * (Score: 74)
		 */
		$r9_ParseDLL = { 48 01 C1 48 89 4A 08 48 83 C1 18 48 89 4A 10 }

	condition:
		5 of them
}
```

The resulting rule can be used to scan PIC on disk:

```
C:\>Tools\yara\yara64.exe -s Tools\cp\cpl.yar Tools\cp\out.bin
TCG_5c837b65 Tools\cp\out.bin
0x28:$r0_go: E8 86 04 00 00 89 C0 41 B9 40 00 00 00 41 B8 00 30 00 00
0x1d8:$r1_findModuleByHash: 4D 8B 42 50 41 0F B7 42 48 83 E8 01 0F B7 C0
0x222:$r2_findFunctionByHash: 49 01 DB 45 8B 43 20 49 01 D8 45 8B 4B 24
0x261:$r3_findFunctionByHash: 41 0F B7 11 41 8B 43 1C 48 8D 14 93 8B 04 02
0x292:$r4_ProcessRelocation: 41 8B 41 04 48 83 E8 08 48 D1 E8 49 8D 51 08
0x2a5:$r5_ProcessRelocation: 4D 89 D3 49 C1 EB 10 8D 40 FF 49 8D 4C 41 0A
0x353:$r6_ProcessRelocations: 48 89 F1 E8 2C FF FF FF 8B 43 04 48 01 C3 83 7B 04 00
0x385:$r7_ProcessImport: 41 8B 49 0C 4C 01 C1 FF 17 49 89 C4 8B 5E 10
0x3ad:$r8_ProcessImport: 4C 89 E1 FF 57 08 48 89 DA 48 89 43 F8
0x3f0:$r8_ProcessImport: 4C 89 E1 FF 57 08 48 89 DA 48 89 43 F8
0x498:$r9_ParseDLL: 48 01 C1 48 89 4A 08 48 83 C1 18 48 89 4A 10
```

Or in a running process:

```
C:\>Tools\yara\yara64.exe -s Tools\cp\cpl.yar 28256
TCG_5c837b65 28256
0x1c1627f0028:$r0_go: E8 86 04 00 00 89 C0 41 B9 40 00 00 00 41 B8 00 30 00 00
0x1c1627f01d8:$r1_findModuleByHash: 4D 8B 42 50 41 0F B7 42 48 83 E8 01 0F B7 C0
0x1c1627f0222:$r2_findFunctionByHash: 49 01 DB 45 8B 43 20 49 01 D8 45 8B 4B 24
0x1c1627f0261:$r3_findFunctionByHash: 41 0F B7 11 41 8B 43 1C 48 8D 14 93 8B 04 02
0x1c1627f0292:$r4_ProcessRelocation: 41 8B 41 04 48 83 E8 08 48 D1 E8 49 8D 51 08
0x1c1627f02a5:$r5_ProcessRelocation: 4D 89 D3 49 C1 EB 10 8D 40 FF 49 8D 4C 41 0A
0x1c1627f0353:$r6_ProcessRelocations: 48 89 F1 E8 2C FF FF FF 8B 43 04 48 01 C3 83 7B 04 00
0x1c1627f0385:$r7_ProcessImport: 41 8B 49 0C 4C 01 C1 FF 17 49 89 C4 8B 5E 10
0x1c1627f03ad:$r8_ProcessImport: 4C 89 E1 FF 57 08 48 89 DA 48 89 43 F8
0x1c1627f03f0:$r8_ProcessImport: 4C 89 E1 FF 57 08 48 89 DA 48 89 43 F8
0x1c1627f0498:$r9_ParseDLL: 48 01 C1 48 89 4A 08 48 83 C1 18 48 89 4A 10
```

A new `ised` command has been added in the latest release, which helps push back against these invariances. It works by providing a means of inserting or replacing specific assembly instructions at a target pattern. The syntax is:

`ised [verb] [pattern] [$CODE] [+options]`

The two valid verbs are `insert` and `replace`. `insert` is used to add `$CODE` before or after the `pattern` (as controlled by the `+first`, `+before`, `+last`, and `+after` options). `replace` simply overwrites the `pattern` with `$CODE`.

The `pattern` can be based on specific strings that match Crystal Palace...