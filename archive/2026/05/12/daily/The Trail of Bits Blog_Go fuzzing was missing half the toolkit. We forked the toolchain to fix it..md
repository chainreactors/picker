---
title: Go fuzzing was missing half the toolkit. We forked the toolchain to fix it.
url: https://blog.trailofbits.com/2026/05/12/go-fuzzing-was-missing-half-the-toolkit.-we-forked-the-toolchain-to-fix-it./
source: The Trail of Bits Blog
date: 2026-05-12
fetch_date: 2026-05-13T05:46:09.336254
---

# Go fuzzing was missing half the toolkit. We forked the toolchain to fix it.

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Go fuzzing was missing half the toolkit. We forked the toolchain to fix it.

[Kevin Valerio](/authors/kevin-valerio/)

May 12, 2026

[tool-release](/categories/tool-release/), [fuzzing](/categories/fuzzing/), [go](/categories/go/), [vulnerabilities](/categories/vulnerabilities/), [research-practice](/categories/research-practice/)

Page content

* [Why we built gosentry](#why-we-built-gosentry)
* [Same harness, stronger engine](#same-harness-stronger-engine)
* [More bugs become visible](#more-bugs-become-visible)
* [Better inputs](#better-inputs)
  + [Struct-aware fuzzing](#struct-aware-fuzzing)
  + [Grammar-based fuzzing](#grammar-based-fuzzing)
* [What it has found already](#what-it-has-found-already)

Go’s native fuzzing is useful, but it stands far behind state-of-the-art tooling that the Rust, C, and C++ ecosystems offer with LibAFL and AFL++. Path constraints are hard to solve. Structured inputs usually need handmade parsing. It doesn’t even detect several common bug classes, such as integer overflows, goroutine leaks, data races, and execution timeouts. So to make it better, we built [gosentry](https://github.com/trailofbits/gosentry), a fuzzing-oriented fork of the Go toolchain that keeps the standard `testing.F` workflow while using a stronger fuzzing stack underneath to tackle those issues.

With gosentry, `go test -fuzz` uses LibAFL by default. It can fuzz structs natively, run grammar-based fuzzing with Nautilus, detect bug classes that it couldn’t detect before, and create a fuzzing campaign coverage report in one command.

If you already have Go fuzz harnesses, you don’t need to rewrite them. Point them at gosentry’s binary and you get all of the above through the same `go test -fuzz` interface, with a few new flags:

```
./bin/go test -fuzz=FuzzHarness --focus-on-new-code=false --catch-races=true --catch-leaks=true
```

Figure 1: Basic gosentry usage

gosentry keeps the harness API and changes the engine and the surrounding tooling — you just tweak the CLI.

You can also generate coverage reports from an existing campaign with `--generate-coverage`. Run it from the same package with the same `-fuzz` target, and no corpus path is needed; gosentry stores the campaign state under Go’s fuzz cache index by package and fuzz target, so restarting the campaign resumes from the existing corpus.

## Why we built gosentry

We started this project after we released [go-panikint](https://blog.trailofbits.com/2025/12/31/detect-gos-silent-arithmetic-bugs-with-go-panikint/) to improve Go fuzzing’s integer overflow detection. We realized that integer overflow detection wasn’t enough. Go’s fuzzing ecosystem was still missing techniques that Rust, C, and C++ researchers already use every day.

We often faced these gaps in our own security work using Go’s vanilla fuzzer:

* Program comparisons (path constraints) were impossible to solve: one complex `if` branch, and the Go fuzzer could stay stuck forever.
* Grammar-based fuzzing was never an option.
* Structure-aware fuzzing required additional manual work.
* Several Go bug classes would not crash by default or would depend on external libraries, so the fuzzer could reach insecure target behaviors without reporting them.
* Generating coverage reports from a fuzzing campaign was cumbersome.
* Making the fuzzer crash on critical error logs required manual code changes.

## Same harness, stronger engine

Gosentry keeps the parts Go developers already know:

* Write a fuzz target with `testing.F`, as usual.
* Create your initial corpus with `f.Add`.
* Pass the input into `f.Fuzz`.

Under the hood, gosentry captures the fuzz callback, builds a Go archive with libFuzzer-style entry points, and runs it in-process through a Rust-based LibAFL runner. The API stays familiar, but gosentry enhances the engine, scheduling, detectors, and much more.

We designed it this way to avoid friction for developers and security researchers adopting a new tool. Existing Go harnesses do not need to be ported to a new framework. And since the Go toolchain documentation and usage are already widely integrated into LLM pre-training datasets, an agent can easily use gosentry, as it is a fork of the Go toolchain.

## More bugs become visible

Another added value of gosentry is its capacity to turn more bad behaviors into failures that the vanilla Go fuzzer wouldn’t report.

It includes compiler-inserted integer overflow checks by default and optional truncation checks through the [go-panikint](https://blog.trailofbits.com/2025/12/31/detect-gos-silent-arithmetic-bugs-with-go-panikint/) integration. It also lets you choose function calls that should stop the fuzzer. For example, you can use the `--panic-on` flag to stop fuzzing when `log.Fatal` is called. This flag is useful for codebases that log critical errors and keep going instead of panicking and reporting the bug to the user.

It can also catch data race issues using the native Go race detector (`--catch-races`), and goroutine leaks through its [goleak](https://github.com/uber-go/goleak) integration (`--catch-leaks`). Finally, timeouts can be caught at fuzz-time to help detect issues like infinite loops.

## Better inputs

Gosentry improves input quality in two different ways, which solve different problems.

### Struct-aware fuzzing

Go’s native fuzzing accepts only a small set of parameter types, which doesn’t include composite types, such as structs, slices, arrays, and pointers. Gosentry supports fuzzing of these types.

```
type Input struct {
	Data []byte
	S    string
	N    int
}

func FuzzStructInput(f *testing.F) {
	f.Add(Input{Data: []byte("hello"), S: "world", N: 42})
	f.Fuzz(func(t *testing.T, in Input) {
		Process(in)
	})
}
```

Figure 2: Supported gosentry harness with structured input

Under the hood, gosentry still mutates bytes. The difference is that it encodes and decodes the composite value for you in a proper way, so you don’t have to invent a custom wire format just to fuzz typed Go inputs.

### Grammar-based fuzzing

In this mode, gosentry uses [Nautilus](https://github.com/nautilus-fuzz/nautilus) to generate and mutate grammar-valid inputs while LibAFL still drives the coverage-guided loop.

Let’s imagine you want to fuzz a homemade JSON parser. Without a grammar, most of the time you would generate junk input that wouldn’t even pass the first branches. For example, the fuzzer would mutate `{"postOfficeBox": 123}` to `{postOfficeBox"": """"&%}`, while a more interesting generated input of `postOfficeBox` would be a much larger number like `u64.MAX`, giving `{"postOfficeBox": 18446744073709551615}`. In that case, you need grammar-based fuzzing. You define what the structure should be, and the fuzzer generates inputs accordingly. You could write a harness like this:

```
func FuzzGrammarJSON(f *testing.F) {
f.Add(`{"postOfficeBox":123}`)
 	f.Fuzz(func(t *testing.T, jsonInput string) {
  		ParseJSONFromString(jsonInput)
  	})
}
```

Figure 3: Grammar-based harness for our JSON parser

The grammar format is a JSON array of rules:

```
  [
    ["Json", "\\{\"postOfficeBox\":{Number}\\}"],

    ["Number", "{Digit}"],
    ["Number", "{Digit}{Number}"],

    ["Digit", "0"],
    ["Digit", "1"],
    ["Digit", "2"],
    ["Digit", "3"],
    ["Digit", "4"],
    ["Digit", "5"],
    ["Digit", "6"],
    ["Digit", "7"],
    ["Digit", "8"],
    ["Digit", "9"]
  ]
```

Figure 4: Definition of our postOfficeBox JSON grammar

Just note that grammar mode still feeds bytes or strings to the harness. So your target needs to be able to parse either strings or bytes.

## What it has found already

We’ve been running gosentry on a bunch of targets using grammar-based differential fuzzing campaigns and found a number of bugs. We have disclosed some of these issues to Optimism and Revm:

* [Unknown batch type panics and causes denial of service...