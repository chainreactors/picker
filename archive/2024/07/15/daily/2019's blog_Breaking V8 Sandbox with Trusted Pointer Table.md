---
title: Breaking V8 Sandbox with Trusted Pointer Table
url: https://mem2019.github.io/jekyll/update/2024/07/14/HITCON.html
source: 2019's blog
date: 2024-07-15
fetch_date: 2025-10-06T17:40:21.130037
---

# Breaking V8 Sandbox with Trusted Pointer Table

[2019's blog](/)

[About](/about/)

# Breaking V8 Sandbox with Trusted Pointer Table

Jul 14, 2024

Recently, I have submitted my academic paper to NDSS 2025. Now it’s time to take a break. Following the deadline is the HITCON CTF 2024, so as the break, why not take a look? I really haven’t played CTF for quite a long time. :)

During the two days, I spent my efforts on the V8 Sandbox challenge. Actually I haven’t worked on V8 for a while. It seems that the sandbox feature now has already been enabled and incorporated into the bug bounty program. This is also a chance for me to catch up to the new progress on the V8 security. :)

## 0x00 Abstract

The challenge provides two exploitation primitives: writing a 64-bit value to the entry of the trusted pointer table and leaking the base address of PIE. We can use the first primitive to fake a `WasmExportedFunctionData` instance, allowing us to set `rip` to an 8-byte value in the trusted memory region. To control the content in this region, we leverage the immediate number arguments of the bytecode instruction `AddSmi.ExtraWide`. We can set the `rip` to point to the immediate numbers in the RWX page, whose address can be leaked by the second primitive, to execute our shellcode.

## 0x01 Trusted Pointer Table

According to [the design documentation of V8 Sandbox](https://docs.google.com/document/d/1FM4fQmIhEqPG8uGp5o9A-mnPB5BOeScZYpkHjo0KKA8/edit#heading=h.5d6zvgc8i4uw), we can know that the trusted pointer table is used for storing the references to the trusted objects outside the sandbox. If a V8 object inside the sandbox needs to reference any trusted object, it stores a reference (i.e., index) to an entry of the trusted pointer table. The entry stores a pointer to the trusted object along with a tag value.

Some examples of the entries in the table are shown below. We can see that the high 16 bits are the tag, and the low 48 bits are the address to the V8 Object. In the example below, we `job` an entry containing pointer to a `WasmExportedFunctionData` instance. Another thing to note is that the first `0x2000` indices are read-only page, which seem to be unused.

```
gef➤  tel 0x007fff54010000
0x007fff54010000│+0x0000: 0x1b158f00040061 ("a"?)
0x007fff54010008│+0x0008: 0x001b158f00040181
0x007fff54010010│+0x0010: 0x001e158f0004021d
0x007fff54010018│+0x0018: 0x002b158f000402fd
0x007fff54010020│+0x0020: 0x002d158f00040321
0x007fff54010028│+0x0028: 0x001b158f00040369
0x007fff54010030│+0x0030: 0x001b158f000c0011
0x007fff54010038│+0x0038: 0x001b158f000403ad
0x007fff54010040│+0x0040: 0x80000000002009 ("\t "?)
0x007fff54010048│+0x0048: 0x8000000000200a ("\n "?)
gef➤  job 0x158f00040321 # Entry `+0x0020:`, low 48 bits are address.
0x158f00040321: [WasmExportedFunctionData]
 - map: 0x336300001e15 <Map[56](WASM_EXPORTED_FUNCTION_DATA_TYPE)>
 - func_ref: 0x336300199ed9 <Other heap object (WASM_FUNC_REF_TYPE)>
 - internal: 0x158f000402fd <Other heap object (WASM_INTERNAL_FUNCTION_TYPE)>
 - wrapper_code: 0x33630003c1b9 <Code BUILTIN JSToWasmWrapper>
 - js_promise_flags: 10
 - instance_data: 0x158f0004021d <Other heap object (WASM_TRUSTED_INSTANCE_DATA_TYPE)>
 - function_index: 0
 - signature: 0x555557fe5ea0
 - wrapper_budget: 1000
```

## 0x02 Faking Object

In this challenge, we can rewrite a table entry to an arbitrary value. After some trial, it seems that the only entry that may lead to the exploitation is the `WasmExportedFunctionData` shown above. I have also spent long time on other web-assembly object entries but none of them work. For example, I also tried `WasmInternalFunction` that is simpler and contains the web-assembly JIT code address directly (e.g., using `WebAssembly.Table` or calling the victim function in the web-assembly), but it seems that the JIT code address referenced by this entry is never used. The primary reason for this is that I didn’t know `Sandbox.base` can provide the base address of the sandboxed memory region, causing me to spend a lot of time in finding out how to fake an object using JIT immediate numbers on the RWX page whose address can be leaked by the provided PIE address, but this task is pretty hard especially the instance is as complex as `WasmExportedFunctionData`. Nonetheless, finally my teammate provides a PoC that informs me such leak.

The `Sandbox` instance provides many exploitation primitives, including arbitrary read and write in the sandboxed memory region. Therefore, we can easily fake a `WasmExportedFunctionData` instance in the sandboxed memory region, such as using a double array, and obtain the address of the faked object. We can simply copy the content from the `WasmExportedFunctionData`, except that we want the `internal` field to point to the correct address containing our controlled data. Besides, the field `signature` should also point to a buffer filled with zeros.

## 0x03 Controlling Trusted Region Content

The good news is that controlling `internal` field enables us to control `rip` because it reads a code address from the `internal` pointer and set it to `rip`, However, the bad news is that the field pointer is only an offset of the trusted memory region. In other words, we can only control the low 32 bits of the pointer, with the high 32 bits of the pointer being fixed to the base address of the trusted memory region.

Therefore, to control `rip`, we must somewhat be able to control some memory content in the trusted memory region, 8 bytes to be specific. However, it seems that most of the objects with content controllable are not in the trusted memory region but in the sandboxed memory region. After some investigation, we found that we may be able to control the arguments of `AddSmi.ExtraWide` to achieve such memory control. To be specific, the opcode contains two arguments: the first one is the immediate number we can control, and the second one is an index. I am not sure what the second argument is exactly, but the thing I notice is that it equals to the number of `AddSmi` appearing in the preceding part of the function. Therefore, if we insert `x` number of `AddSmi` instructions before `AddSmi.ExtraWide`, the value will be the `x`. Using this approach, we can control 6 bytes in the trusted region with two following bytes being zero. An example of `AddSmi.ExtraWide` is shown below. The bytes that can be used to set `rip` is in the bracket.

```
01 47 (c2 12 00 e0 55 55 00 00) AddSmi.ExtraWide [-536866110], [21845]
```

## 0x04 Executing Shellcode

Finally, we can set `rip` to our shellcode. We can use the similar approach I used [previously](https://mem2019.github.io/jekyll/update/2022/02/06/DiceCTF-Memory-Hole.html) to construct the shellcode inside the immediate number of a JIT JavaScript function. Fortunately directly copying function still gave the correct shellcode, since the offsets between the immediate numbers remain same after two years. The difference is that currently the JIT JavaScript function is stored in a RWX page whose address is not very random given the high 32 bits of base address of PIE, so we can set `rip` to the shellcode easily given such a leak.

It seems that in different platform, the offset of the shellcode with respect to the RWX page can be different. The problem does not appear in the original exploit that I used in the CTF, but appears in the simplified exploit that I prepared for this write-up. I am not sure why actually.

Finally, see the exploit [here](https://github.com/Mem2019/Mem2019.github.io/blob/master/codes/HITCON-2024.js).

## 2019's blog

* 2019's blog
* r3tr0spect2019@qq.com

* [Mem2019](https://github.com/Mem2019)

一位失败人士的blog