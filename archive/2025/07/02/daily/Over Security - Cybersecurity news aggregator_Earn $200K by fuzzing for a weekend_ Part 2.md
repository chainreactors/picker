---
title: Earn $200K by fuzzing for a weekend: Part 2
url: https://secret.club/2022/05/11/fuzzing-solana-2.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:08.143557
---

# Earn $200K by fuzzing for a weekend: Part 2

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Earn $200K by fuzzing for a weekend: Part 2

![main authors image](/assets/author_img/addison.jpg)  [addison](/author/addison)

 May 11, 2022

---

Below are the writeups for two vulnerabilities I discovered in [Solana rBPF](https://github.com/solana-labs/rbpf), a self-described “Rust virtual machine and JIT compiler for eBPF programs”. These vulnerabilities were responsibly disclosed according to Solana’s [Security Policy](https://github.com/solana-labs/solana/security/policy) and I have permission from the engineers and from the Solana Head of Business Development to publish these vulnerabilities as shown below.

In [part 1](fuzzing-solana.html), I discussed the development of the fuzzers. Here, I will discuss the vulnerabilities as I discovered them and the process of reporting them to Solana.

## [Bug 1: Resource exhaustion](#bug-1-resource-exhaustion)

The first bug I reported to Solana was exceptionally tricky; it only occurs in highly specific circumstances, and the fact that the fuzzer discovered it at all is a testament to the incredible complexity of inputs a fuzzer can discover through repeated trials. The relevant crash was found in approximately two hours of fuzzer start.

### [Initial Investigation](#initial-investigation)

The input that triggered the crash disassembles to the following assembly:

```
entrypoint:
  r0 = r0 + 255
  if r0 <= 8355838 goto -2
  r9 = r3 >> 3
  call -1
```

For *whatever* reason, this particular set of instructions causes a memory leak.

When executed, this program does the following steps, roughly:

1. increase r0 (which starts at 0) by 255
2. jump back to the previous instruction if r0 is less than or equal to 8355838
   * this, in tandem with the first step, will cause the loop to execute 32767 times (a total of 65534 instructions)
3. set r9 to r3 \* 2^3, which is going to be zero because r3 starts at zero
4. calls a nonexistent function
   * the nonexistent function should trigger an unknown symbol error

What stood out to me about this particular test case is how incredibly specific it was; varying the addition of 255 or 8355838 by even a small amount caused the leak to disappear. It was then I remembered [the following line from my fuzzer](https://github.com/solana-labs/rbpf/blob/afaf17c527368dc165f6cb11110190142aed235f/fuzz/fuzz_targets/smart_jit_diff.rs#L71):

```
let mut jit_meter = TestInstructionMeter { remaining: 1 << 16 };
```

`remaining`, here, refers to the number of instructions remaining before the program is forceably terminated. As a result, the leaking program was running out this meter at exactly the `call` instruction.

#### [A faulty optimisation](#a-faulty-optimisation)

[There is a wall of text at line 420 of jit.rs](https://github.com/solana-labs/rbpf/blob/e8b4a0accd1c4eb45c055e87718f03db7f52218e/src/jit.rs#L420) which suitably describes an optimisation that Solana applied in order to reduce the frequency at which they need to update the instruction meter.

The short version is that they only update or check the instruction meter when they reach the end of a block or a call in order to reduce the amount of times they update and check the meter. This optimisation is totally reasonable; we don’t care if we run out of instructions at the middle of a block because the subsequent instructions are still “safe”, and if we ever hit an exit that’s the end of a block anyway. In other words, this optimisation should have no effect on the final state of the program.

The issue can be seen in [the patch for the vulnerability](https://github.com/solana-labs/rbpf/pull/261/files#diff-7d39efd566d08b201d1e747f11b3909be0d39fd3d4c89cfd28e0b21bab3ec27aR1275), where the maintainer moved line 1279 to line 1275. To understand why that’s relevant, let’s walk through our execution again:

1. increase r0 (which starts at 0) by 255
2. jump back to the previous instruction if r0 is less than or equal to 8355838
   * this, in tandem with the first step, will cause the loop to execute 32767 times (a total of 65534 instructions)
   * our meter updates here
3. set r9 to r3 \* 2^3, which is going to be zero because r3 starts at zero
4. calls a nonexistent function
   * the nonexistent function should trigger an unknown symbol error, but that doesn’t happen because our meter updates here and emits a max instructions exceeded error

However, based on the original order of the instructions, what happens in the call is the following:

1. invoke the call, which fails because the symbol is unresolved
2. to report the unresolved symbol, we invoke that [`report_unresolved_symbol`](https://github.com/solana-labs/rbpf/blob/786d4f7fe17c252bbfd3b6e89d954defa89c0003/src/elf.rs#L315) function, which returns the name of the symbol invoked (or “Unknown”) in a heap-allocated string
3. the pc is updated
4. the instruction count is validated, which *overwrites* the unresolved symbol error and [terminates execution](https://github.com/solana-labs/rbpf/blob/786d4f7fe17c252bbfd3b6e89d954defa89c0003/src/jit.rs#L477)

Because the unresolved symbol error is merely overwritten, the value is never passed to the Rust code which invoked the JIT program. As a result, the reference to the heap-allocated String is lost and never dropped. Thus: any pointer to that heap allocation is lost and will never be freed, leading to the leak.

That being said, the leak is only seven bytes per execution of the program. Without causing a larger leak, this isn’t particularly exploitable.

### [Weaponisation](#weaponisation)

Let’s take a closer look at [`report_unresolved_symbol`](https://github.com/solana-labs/rbpf/blob/786d4f7fe17c252bbfd3b6e89d954defa89c0003/src/elf.rs#L315).

  report\_unresolved\_symbol source

```
pub fn report_unresolved_symbol(&self, insn_offset: usize) -> Result<u64, EbpfError<E>> {
    let file_offset = insn_offset
        .saturating_mul(ebpf::INSN_SIZE)
        .saturating_add(self.text_section_info.offset_range.start as usize);

    let mut name = "Unknown";
    if let Ok(elf) = Elf::parse(self.elf_bytes.as_slice()) {
        for relocation in &elf.dynrels {
            match BpfRelocationType::from_x86_relocation_type(relocation.r_type) {
                Some(BpfRelocationType::R_Bpf_64_32) | Some(BpfRelocationType::R_Bpf_64_64) => {
                    if relocation.r_offset as usize == file_offset {
                        let sym = elf
                            .dynsyms
                            .get(relocation.r_sym)
                            .ok_or(ElfError::UnknownSymbol(relocation.r_sym))?;
                        name = elf
                            .dynstrtab
                            .get_at(sym.st_name)
                            .ok_or(ElfError::UnknownSymbol(sym.st_name))?;
                    }
                }
                _ => (),
            }
        }
    }
    Err(ElfError::UnresolvedSymbol(
        name.to_string(),
        file_offset
            .checked_div(ebpf::INSN_SIZE)
            .and_then(|offset| offset.checked_add(ebpf::ELF_INSN_DUMP_OFFSET))
            .unwrap_or(ebpf::ELF_INSN_DUMP_OFFSET),
        file_offset,
    )
    .into())
}
```

Note how the `name` is the string which becomes heap allocated. The value of the name is determined by a relocation lookup in the ELF, which we can actually control if we compile our own malicious ELF. Even though the fuzzer only tests the JIT operations, [one of the intended ways to load a BPF program is as an ELF](https://github.com/solana-labs/rbpf/blob/786d4f7fe17c252bbfd3b6e89d954defa89c0003/src/elf.rs#L1277), so it seems like something that would certainly be in scope.

#### [Crafting the malicious ELF](#crafting-the-malicious-elf)

To create an unresolved relocation in BPF, it’s actually quite simple. We just need to create a function with a very, very long name that isn’t actually defined, only declared. To do so, I created two files to craft the malicious ELF:

  evil.h

`evil.h` is far too ...