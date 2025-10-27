---
title: Go Assembly Mutation Testing
url: https://words.filippo.io/assembly-mutation/
source: Filippo Valsorda
date: 2025-08-01
fetch_date: 2025-10-07T00:15:11.553996
---

# Go Assembly Mutation Testing

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

31 Jul 2025

# Go Assembly Mutation Testing

While maintaining and developing the Go cryptography standard library, we often spend significantly more time on [testing](https://www.youtube.com/watch?v=lkEH3V3PkS0) than on implementation. That’s good and an important part of how we achieve our excellent [security track record](https://go.dev/blog/tob-crypto-audit).

Ideally, this would be especially true for the *least safe* parts of the library. However, testing assembly cores presents unique challenges, due to their constant-time nature. This has been a long-standing issue.

For Go 1.26, I am working on introducing a mutation testing framework for assembly, which will effectively act as enhanced code coverage. This will not improve tests by itself, but it will let us see what assembly code and data paths are not covered by our test suite, so we can improve it.

## #20040, my white whale

Cryptographic assembly is sort of my “origin story” as a Go maintainer. Back in 2017, a colleague at Cloudflare found a certificate that failed to validate with Go’s crypto/x509. The bug was [a mishandled carry in the amd64 assembly implementation of P-256 modular subtraction](https://github.com/golang/go/commit/9294fa2749ffee7edbbb817a0ef9fe633136fa9c#diff-85772c71438acb5fb01065a6aacca9411f81a807b13230d3592bc5fb498fda9a). It had escaped all testing because that carry flag had a 1 in 2³² chance of being set when operating on random inputs.

Adam Langley commented that exploiting it was unlikely and [“would be a cool paper”](https://github.com/golang/go/issues/20040#issue-222804725). Then Sean Devlin and I hid in a Starbucks in Paris for a whole day while the yellow jackets set fire to cop cars outside, and figured out how to turn it into a [Hollywood-looking key recovery attack](https://www.youtube.com/watch?v=aIFiaCcKfW8). That was fun, but it’s [a different story](https://www.youtube.com/watch?v=zPj5tTFDql0).

Fast forward one year, and it was now my job to stop this from happening again. Finding a robust countermeasure to this bug class has been my white whale ever since.

> “Filippo, normal, well-adjusted people don’t have white whales.”
> “Well, we have learned nothing new, have we?”

The [Assembly Policy](https://go.dev/wiki/AssemblyPolicy) has (hopefully) helped reduce the risk of introducing new manually-written assembly bugs, if anything because it made it harder to introduce new manually written assembly, but a fundamental problem is that we don’t know how well our assembly is tested , because code coverage doesn’t work for cryptographic assembly.

Most cryptographic code has to operate in constant time, meaning it executes the same instructions regardless of the inputs, to avoid leaking secrets through timing side-channels. To achieve that, we often compute both “branches” of an operation (e.g. both `a - b` and `a - b + p`, for `a - b mod p`), and then discard one of the results with constant-time select instructions. The problem is that if you run code coverage, you’ll see all “branches” light up, even if all tests actually discard the result of one of them. We could have other untested paths like #20040 and not know about it.

At some point in 2019 I tried instrumenting binaries at runtime with DynamoRIO to capture the flags before each flag-consuming instruction, to feed a more comprehensive coverage report. It almost worked. “Almost” being dispositive.

## Mutation testing

Enter mutation testing. Mutation tests modify the program, for example by turning a `!=` into a `==`, and check that tests *fail* for each “mutation.” If they don’t, that line is not—effectively—tested.

This is actually more accurate than regular test coverage because it doesn’t just check that code is executed, but also that the result influences the success of the tests, such that producing a different result would cause the tests to fail.

It’s also a great match for constant time assembly!

For example, if we turn an [add-with-carry](https://retrocomputing.stackexchange.com/a/29806) into a regular add, and tests still pass, we are not actually testing the case in which the carry is set.

## Mutating assembly

The next question is how to programmatically mutate assembly. I was going to do it at the source level, but Russ Cox suggested modifying the assembler instead, to avoid having to deal with macros and parsing.

cmd/asm assigns a virtual program counter to instructions right after parsing, before encoding them. [CL 665375](https://go.dev/cl/665375)[1](#fn:pending) adds a `-mutlist` flag to print the listing at that point to standard error, and a `-mut` flag that allows replacing any instruction by its program counter with one or more other instructions. Implementing it was fairly easy, reusing the parser and patching the instructions linked list.

```
$ GOARCH=amd64 go test crypto/ed25519 -asmflags=crypto/internal/fips140/edwards25519/field=-mutlist -c
# crypto/internal/fips140/edwards25519/field
asm: mutlist: $GOROOT/src/crypto/internal/fips140/edwards25519/field/fe_amd64.s:8: 00001 TEXT   crypto/internal/fips140/edwards25519/field.feMul(SB), NOSPLIT, $0-24
[...]
asm: mutlist: $GOROOT/src/crypto/internal/fips140/edwards25519/field/fe_amd64.s:23: 00012 ADDQ  AX, DI
asm: mutlist: $GOROOT/src/crypto/internal/fips140/edwards25519/field/fe_amd64.s:24: 00013 ADCQ  DX, SI
asm: mutlist: $GOROOT/src/crypto/internal/fips140/edwards25519/field/fe_amd64.s:27: 00014 MOVQ  16(CX), DX
[...]

$ GOARCH=amd64 go test crypto/ed25519 -asmflags=crypto/internal/fips140/edwards25519/field='"-mut=$GOROOT/src/crypto/internal/fips140/edwards25519/field/fe_amd64.s:13=STC;ADCQ DX, SI"'
--- FAIL: TestGenerateKey (0.00s)
panic: runtime error: invalid memory address or nil pointer dereference [recovered, repanicked]
[signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x5a900de]
```

These assembler flags can be enabled for a specific package during `go test` with `-asmflags=PACKAGE="-mut=..."`. Thankfully cmd/go already knows to fold the `-asmflags` argument into the cache key of assembler artifacts, and it even caches the stderr output, so `-mutlist` output is available even when using a cached result.

## The test framework

Driving these tests is [relatively straightforward](https://go.dev/cl/666395).

First, we run `go test -c -asmflags=PACKAGE=-mutlist` to obtain the listing of potential targets.

Then, for each mutation of each target instruction, we run `go test -failfast -asmflags=PACKAGE="-mut=file.s:123=MUTATION"`, and make sure it fails. To speed things up, we run first with `-short` and then without only if short tests pass. Also, we first run with `-c` to ensure our mutation compiles.

## The mutations

Finally, we need to decide which target instructions we mutate and how. Mutations turn an instruction that behaves differently based on a flag, into an equivalent instruction that behaves as if the flag was always or never set. They need not to change anything else, to avoid accidentally breaking the test run and causing a mutation testing false negative. In particular, we can’t use any register and we need to leave the final flags untouched.

Let’s look at a few arm64 examples.

#### ADCS and SBCS

[ADCS](https://developer.arm.com/documentation/ddi0602/2025-06/Base-Instructions/ADCS--Add-with-carry--setting-flags-?lang=en) adds two registers and the carry, and sets output flags.

```
// Xd = Xn + Xm + C
ADCS Xn, Xm, Xd
```

Mutating it into an instruction that ignores the carry flag is easy, we just turn it into a [ADDS](https://developer.arm.com/documentation/ddi0602/2025-06/Base-Instructions/ADDS--immediate---Add-immediate-value--setting-flags-?lang=en).

```
// Xd = Xn + Xm
ADDS Xn, Xm, Xd
```

To mutate in the other direction, we prepend an instruction that sets the C flag. We don’t care about smashing the other flags, because ADCS will reset them anyway....