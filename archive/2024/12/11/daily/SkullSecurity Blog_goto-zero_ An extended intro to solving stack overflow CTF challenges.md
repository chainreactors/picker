---
title: goto-zero: An extended intro to solving stack overflow CTF challenges
url: https://www.skullsecurity.org/2024/goto-zero-a-fake-ctf-challenge-to-show-off-something
source: SkullSecurity Blog
date: 2024-12-11
fetch_date: 2025-10-06T19:37:30.157535
---

# goto-zero: An extended intro to solving stack overflow CTF challenges

[![SkullSecurity](/assets/skullsecurity.jpg "SkullSecurity")](/)

[SkullSecurity](/)

* [Blog](/)
* [About](/about)
* [Ron's CV](/cv)
* [Wiki (archive)](/wiki)
* [Mastodon](https://infosec.exchange/%40iagox86)

### Post Navigation

[BSidesSF 2024 Writeups: Turing Complete (Reversing / exploitation)](/2024/bsidessf-2024-writeups-turing-complete-reversing-exploitation-)

[BSidesSF 2025: bug-me (hard reversing challenge)](/2025/bsidessf-2025-bug-me-hard-reversing-challenge-)

# goto-zero: An extended intro to solving stack overflow CTF challenges

Hey all!

My husband’s company recently did an internal (commercial) CTF, and as a CTF nerd I got suckered into helping him. I thought one of the challenges had a pretty interesting solution - at least, something I hadn’t done before - and I thought I’d do a little write-up!

Because it’s a commercial CTF, I wrote my own vulnerability binary, which you can grab [here](/blogdata/goto-zero). It’s much, much simpler, but has all the components I wanted. They also provided `libc.so`, but since I’m not actually running the challenge, you can just use your own copy.

(Note that I’m running the BSidesSF CTF again this spring, and will probably gussy up this challenge a bit and throw it in - don’t let a good challenge go unwasted!)

## The challenge

The CTF challenge was a binary that listens on a network port with a pretty straight-forward stack buffer overflow in a call to `fgets()`.

The difficult part (for me) is that the binary is very simple - there aren’t a lot of libc imports. When I design a CTF challenge, I usually find an excuse to call `popen` or `system` or something so the player has access to that address. But nothing like that in this one!

So we we have is:

* A simple binary
* A bit of randomness to make simple exploits difficult
* A provided copy of `libc.so`
* The overflow is in `fgets()` (which allows NUL bytes - see [my recent rant about NUL bytes](https://www.labs.greynoise.io/grimoire/2024-11-20-null-problem/)
* The binary has no stack-overflow protection (ie, compiled with `-fno-stack-protector` or a time machine)
* The binary is not compiled as a position-independent executable (PIE) - that means there’s no ASLR in the main binary and we can rely on static addresses (but there IS ASLR in the `libc.so` library) - we’ll talk about why that matters
* The binary has symbols, so we know what functions are called

Let’s see how I approached it!

## De-randomizing

(If you don’t care about how to disable the randomness for local testing, skip to the next section!)

If you run the binary I made, it asks you to type in a certain number of characters:

```
$ ./goto-zero
Enter 11 characters then press enter!
^C

$ ./goto-zero
Enter 14 characters then press enter!
```

I hate randomness when I’m hacking! If possible, I want to be able to test without having to fuss with that sorta thing. So one of the first things I did was find the code that randomizes the number. To do that, you can use Ghidra, IDA, `objdump -D`. I used `objdump -D`, which is the worst option, but is quick and free and easy to demonstrate (I also use `-M intel` because I prefer Intel syntax).

Basically, disassemble the binary and search for the word “rand”, and it’ll lead you to the top of the `main()` function:

```
$ objdump -M intel -D goto-zero
[...]
  4011e1:       bf 00 00 00 00          mov    edi,0x0
  4011e6:       e8 95 fe ff ff          call   401080 <time@plt>
  4011eb:       89 c7                   mov    edi,eax
  4011ed:       e8 5e fe ff ff          call   401050 <srand@plt>
  4011f2:       e8 a9 fe ff ff          call   4010a0 <rand@plt>
```

Seeing `time()` and `srand()` called like that tells me they’re seeding the random number generator with the current time. The register `edi` is the first argument to a function and `eax` is the return value, so what you’re seeing is essentially `srand(time(0));`.

What we’d like to do is get rid of all that. The easiest thing is to patch the executable to get rid of the `time()` call altogether, and just do `srand(0)`. You can do that by finding the sequence of raw bytes in the binary (the middle column in that listing), and “removing” the ones you don’t want (by replacing them with `90 90 90 ...` which is `nop nop nop ...`).

In this case, we want to remove `call 401080` (which corresponds to the bytes `e8 95 fe ff ff`) and the following `mov edi, eax` (`e9 c7`). That way, instead of passing 0 into `time()`, it’ll pass 0 into the following function, `srand()`, and therefore always call `srand(0)`, which means we’ll always get the same random sequence (a lot of what we do when modifying binaries is finding ways to use the tools we have to do something a little differently - we’ll see that more later).

Open the binary in a hex editor of your choice (I’m using `xxd -g1 < goto-zero > goto-zero.hex`), search for that sequence, and replace it with `90 90 90 90 90 90 90`).

So:

```
000011e0: ff bf 00 00 00 00 e8 95 fe ff ff 89 c7 e8 5e fe  ..............^.
000011f0: ff ff e8 a9 fe ff ff 89 c2 89 d0 c1 f8 1f c1 e8  ................
```

Becomes:

```
000011e0: ff bf 00 00 00 00 90 90 90 90 90 90 90 e8 5e fe  ..............^.
000011f0: ff ff e8 a9 fe ff ff 89 c2 89 d0 c1 f8 1f c1 e8  ................
```

Then save it as a binary file again, if your hex editor doesn’t automatically do that (with `xxd`, you can use `xxd -g1 -r < goto-zero.hex > goto-zero.patched`). You’ll probably want a different name, because you’ll eventually need the old version. Also, don’t forget to `chmod +x` the new binary!

If you do all that, then objdump `goto-hex.patched`, you will see that the code has changed:

```
$ objdump -M intel -D goto-zero.patched
[...]
  4011e1:       bf 00 00 00 00          mov    edi,0x0
  4011e6:       90                      nop
  4011e7:       90                      nop
  4011e8:       90                      nop
  4011e9:       90                      nop
  4011ea:       90                      nop
  4011eb:       90                      nop
  4011ec:       90                      nop
  4011ed:       e8 5e fe ff ff          call   401050 <srand@plt>
  4011f2:       e8 a9 fe ff ff          call   4010a0 <rand@plt>
```

And when you run it, it should always pick the same number:

```
$ ./goto-zero.patched
Enter 14 characters then press enter!
^C

$ ./goto-zero.patched
Enter 14 characters then press enter!
^C

$ ./goto-zero.patched
Enter 14 characters then press enter!
```

Note that this won’t work against a remote server, because it won’t be disabled on their end. So you either have to *eventually* deal with the randomness, or run your payload over and over till it doesn’t crash. :)

I find that removing little annoyances (like randomization) while reverse engineering or exploit dev can save you a TON of mental anguish, and I always suggest looking for ways to make your working environment nicer!

## Stack overflow

The first thing I do when I’m allowed to input text is to input a lot of text!

Let’s try:

```
$ ./goto-zero.patched
Enter 14 characters then press enter!
AAAAAAAAAAAAAA
What is your name?

BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
Good job, BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
fish: Job 1, './goto-zero.patched' terminated by signal SIGSEGV (Address boundary error)
```

Usually that’s a darn good indicator that you have an overflow - likely a stack overflow, particularly if it’s a CTF :)

We can verify, though! We’re going to use `gdb` - the GNU debugger! Here’s my config file, the important part is to use `intel` syntax:

```
$ cat ~/.gdbinit
set disassembly-flavor intel
set pagination off
set confirm off
```

Here’s how you’d run `goto-zero.patched` in `gdb` (the `-q` is just for less output, and I added some newlines for easier reading):

```
$ gdb -q ./goto-zero.patched
Reading symbols from ./goto-zero.patched...
(No debugging symbols found in ./goto-zero.patched)

(gdb) run
Starting program: /home/ron/projects/ctf/goto-...