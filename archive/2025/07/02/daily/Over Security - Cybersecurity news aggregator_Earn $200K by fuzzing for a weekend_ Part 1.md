---
title: Earn $200K by fuzzing for a weekend: Part 1
url: https://secret.club/2022/05/11/fuzzing-solana.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-02
fetch_date: 2025-10-06T23:56:07.196523
---

# Earn $200K by fuzzing for a weekend: Part 1

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Earn $200K by fuzzing for a weekend: Part 1

![main authors image](/assets/author_img/addison.jpg)  [addison](/author/addison)

 May 11, 2022

---

By applying well-known fuzzing techniques to a popular target, I found several bugs that in total yielded over $200K in bounties. In this article I will demonstrate how powerful fuzzing can be when applied to software which has not yet faced sufficient testing.

If you’re here just for the bug disclosures, see [Part 2](fuzzing-solana-2.html), though I encourage you all, even those who have not yet tried their hand at fuzzing, to read through this.

# [Exposition](#exposition)

A few friends and I ran a little Discord server (now a Matrix space) which in which we discussed security and vulnerability research techniques. One of the things we have running in the server is a bot which posts every single CVE as they come out. And, yeah, I read a lot of them.

One day, the bot posted something that caught my eye:

![](/assets/fuzzing-solana/rbpf-cve-screenshot.png)

![](/assets/fuzzing-solana/noticed-cve.png)

This marks the beginning of our timeline: January 28th. I had noticed this CVE in particular for two reasons:

* it was BPF, which I find to be an absurdly cool concept as it’s used in the Linux kernel (a JIT compiler in the kernel!!! what!!!)
* it was a JIT compiler written in Rust

This CVE showed up almost immediately after I had developed some relatively intensive fuzzing for some of my own Rust software (specifically, a [crate for verifying sokoban solutions](https://github.com/tamuctf/sokoban) where I had [observed similar issues](https://github.com/tamuctf/sokoban/commit/3f837557ea4b4656cd3dd4a0aab8815b343197b6#diff-b1a35a68f14e696205874893c07fd24fdb88882b47c23cc0e0c80a30c7d53759R37) and thought “that looks familiar”).

Knowing what I had learned from my experience fuzzing my own software and that bugs in Rust programs could be quite easily found with the combo of cargo fuzz and [arbitrary](https://github.com/rust-fuzz/arbitrary), I thought: “hey, why not?”.

# [The Target, and figuring out how to test it](#the-target-and-figuring-out-how-to-test-it)

[Solana](https://solana.com/), as several of you likely know, “is a decentralized blockchain built to enable scalable, user-friendly apps for the world”. They primarily are known for their cryptocurrency, SOL, but also are a blockchain which operates really any form of smart contract.

[rBPF](https://github.com/solana-labs/rbpf) in particular is a self-described “Rust virtual machine and JIT compiler for eBPF programs”. Notably, it implements both an interpreter *and* a JIT compiler for BPF programs. In other words: two different implementations of the same program, which theoretically exhibited the same behaviour when executed.

I was lucky enough to both take a software testing course in university and to have been part of a research group doing fuzzing (admittedly, we were fuzzing hardware, not software, but the concepts translate). A concept that I had hung onto in particular is the idea of [test oracles](https://en.wikipedia.org/wiki/Test_oracle) – a way to distinguish what is “correct” behaviour and what is not in a design under test.

In particular, something that stood out to me about the presence of both an interpreter and a JIT compiler in rBPF is that we, in effect, had a perfect pseudo-oracle; [as Wikipedia puts it](https://en.wikipedia.org/wiki/Test_oracle#Derived):

> a separately written program which can take the same input as the program or system under test so that their outputs may be compared to understand if there might be a problem to investigate.

Those of you who have more experience in fuzzing will recognise this concept as [differential fuzzing](https://en.wikipedia.org/wiki/Differential_testing), but I think we can often overlook that differential fuzzing is just another face of a pseudo-oracle.

In this particular case, we can execute the interpreter, one implementation of rBPF, and then execute the JIT compiled version, another implementation, with the same inputs (i.e., memory state, entrypoint, code, etc.) and see if their outputs are different. If they are, one of them must *necessarily* be incorrect per the description of the rBPF crate: two implementations of exactly the same behaviour.

# [Writing a fuzzer](#writing-a-fuzzer)

To start off, let’s try to throw a bunch of inputs at it without really tuning to anything in particular. This allows us to sanity check that our basic fuzzing implementation actually works as we expect.

## [The dumb fuzzer](#the-dumb-fuzzer)

First, we need to figure out how to execute the interpreter. Thankfully, there are several examples of this readily available in a variety of tests. I referenced the `test_interpreter_and_jit` macro present in [ubpf\_execution.rs](https://github.com/solana-labs/rbpf/blob/main/tests/ubpf_execution.rs#L30) as the basis for how [my so-called “dumb” fuzzer](https://github.com/solana-labs/rbpf/blob/main/fuzz/fuzz_targets/dumb.rs) executes.

I’ve provided a sequence of components you can look at one chunk at a time before moving onto the whole fuzzer. Just click on the dropdowns to view the code relevant to that step. You don’t necessarily need to to understand the point of this post.

  Step 1: Defining our inputs

We must define our inputs such that it’s actually useful for our fuzzer. Thankfully, [arbitrary](https://github.com/rust-fuzz/arbitrary) makes it near trivial to derive an input from raw bytes.

```
#[derive(arbitrary::Arbitrary, Debug)]
struct DumbFuzzData {
    template: ConfigTemplate,
    prog: Vec<u8>,
    mem: Vec<u8>,
}
```

If you want to see the definition of ConfigTemplate, you can check it out in [common.rs](https://github.com/solana-labs/rbpf/blob/main/fuzz/fuzz_targets/common.rs), but all you need to know is that its purpose is to test the interpreter under a variety of different execution configurations. It’s not particularly important to understand the fundamental bits of the fuzzer.

   Step 2: Setting up the VM

Setting up the fuzz target and the VM comes next. This will allow us to not only execute our test, but later to actually check if the behaviour is correct.

```
fuzz_target!(|data: DumbFuzzData| {
    let prog = data.prog;
    let config = data.template.into();
    if check(&prog, &config).is_err() {
        // verify please
        return;
    }
    let mut mem = data.mem;
    let registry = SyscallRegistry::default();
    let mut bpf_functions = BTreeMap::new();
    register_bpf_function(&config, &mut bpf_functions, &registry, 0, "entrypoint").unwrap();
    let executable = Executable::<UserError, TestInstructionMeter>::from_text_bytes(
        &prog,
        None,
        config,
        SyscallRegistry::default(),
        bpf_functions,
    )
    .unwrap();
    let mem_region = MemoryRegion::new_writable(&mut mem, ebpf::MM_INPUT_START);
    let mut vm =
        EbpfVm::<UserError, TestInstructionMeter>::new(&executable, &mut [], vec![mem_region]).unwrap();

    // TODO in step 3
});
```

You can find the details for how `fuzz_target` works from the [Rust Fuzz Book](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) which goes over how it works in higher detail than would be appropriate here.

   Step 3: Executing our input and comparing output

In this step, we just execute the VM with our provided input. In future iterations, we’ll compare the output of interpreter vs JIT, but in this version, we’re just executing the interpreter to see if we can induce crashes.

```
fuzz_target!(|data: DumbFuzzData| {
    // see step 2 for this bit

    drop(black_box(vm.execute_program_interpreted(
        &mut TestInstructionMeter { remaining: 1024 },
    )));
});
```

I use black\_box here but I’m not entirely convinced that it’s necessary. I added it to ensure that the result of the interpreted program’s execution isn’t simply discarded and thus the execution marked unnecessa...