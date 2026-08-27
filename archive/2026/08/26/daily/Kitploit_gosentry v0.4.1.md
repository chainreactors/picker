---
title: gosentry v0.4.1
url: https://kitploit.com/en/posts/github-trailofbits-gosentry-041
source: Kitploit
date: 2026-08-26
fetch_date: 2026-08-27T12:12:40.128777
---

# gosentry v0.4.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/41918/7b1ea005996846c9ee4d7c0d42fee26731050d10b6b21d59c551e4b1b956923e.png)

New releaseAug 26, 2026

# gosentry v0.4.1

Security-oriented Go toolchain, focused on state-of-the-art fuzzing capabilities.

Share

# gosentry

[![integration tests](https://github.com/trailofbits/gosentry/actions/workflows/go.yml/badge.svg?branch=master)](https://github.com/trailofbits/gosentry/actions/workflows/go.yml)

gosentry is a security-focused fork of the Go toolchain, integrating numerous features for state-of-the-art fuzzing campaigns on Go codebases. If you were using `go test -fuzz` before, you should use gosentry as a replacement.
It comes with various fuzzing improvements and bug detectors that are not present natively in the Go toolchain. See TLDR; below. You can also read the associated blog article [here](https://blog.trailofbits.com/2026/05/12/go-fuzzing-was-missing-half-the-toolkit.-we-forked-the-toolchain-to-fix-it./).

**TLDR (features and options)**:

* Fuzz `struct` inputs directly (no custom parser needed). Add seeds with `f.Add(Input{N: 7, S: "hi"})` then `f.Fuzz(func(t *testing.T, in Input) { ... })`.
* Panic on integer overflow and detect arithmetic issues
* Fuzz with LibAFL for state-of-the-art fuzzing techniques like path constraints solving
* Generate/mutate inputs from a grammar to avoid useless mutations. Mutation generates valid maths operation like `X + Y - Z` can become `X / U + Z - 14` instead of `X + Yè - Z`
* Panic on selected functions (like critical errors loggers) and crash when it's called
* Focus the fuzzer on recently changed lines AND on new coverage to target new commits mainly
* Catch data races at fuzz-time
* Catch Go leaks at fuzz-time
* Catch stuck executions with timeouts at fuzz-time
* Generate a HTML coverage report from a fuzz campaign corpus with one CLI

## Table of Contents

* [Build](#build)
  + [Feature 1: Struct-aware fuzzing (fuzz structs as inputs)](#feature-1-struct-aware-fuzzing-fuzz-structs-as-inputs)
  + [Feature 2: Integer overflow and truncation issues detection](#feature-2-integer-overflow-and-truncation-issues-detection)
  + [Feature 3: Panic on selected functions](#feature-3-panic-on-selected-functions)
  + [Feature 4: LibAFL state-of-the-art fuzzing](#feature-4-libafl-state-of-the-art-fuzzing)
  + [Feature 5: Git-blame-oriented fuzzing (experimental)](#feature-5-git-blame-oriented-fuzzing-experimental)
  + [Feature 6: Detect race conditions, goroutine leaks, and hangs at fuzz-time](#feature-6-detect-race-conditions-goroutine-leaks-and-hangs-at-fuzz-time)
  + [Feature 7: Grammar-based fuzzing (Nautilus)](#feature-7-grammar-based-fuzzing-nautilus)
  + [Feature 8: Generate fuzzing coverage reports from campaign](#feature-8-generate-go-coverage-reports-from-fuzzing-campaign)
* [Trophies](#trophies)
* [Credits](#credits)

## Build

root@kitploit:~

```
cd src && ./make.bash # Produces `../bin/go`. See `GOFLAGS` below.
```

> [!TIP]
> Contributor docs: read `docs/gosentry/index.md` for a code map, recommended dev loop, CI entrypoints and benchmark scripts.
> This fork uses the Pull GitHub App to open and auto-merge PRs from `golang/go:master` into `master`, ensuring we never stay behind Go toolchain latest updates.

## Feature 1: Struct-aware fuzzing (fuzz structs as inputs)

#### Overview

Go’s native fuzzing (`go test -fuzz=...`) only supports a small set of scalar types as fuzz parameters (`[]byte`, `string`, numbers, ...). In gosentry, you can also fuzz **composite types** built from those scalars: structs, arrays, slices, and pointers.
This is useful when your code naturally takes structured inputs and you don’t want to build a custom encoder/decoder just to seed and mutate the corpus.
See `test/gosentry/examples/multiargs` and `test/gosentry/examples/composite` for examples.

#### Simple example

root@kitploit:~

```
type Input struct {
	Data []byte
	S    string
	N    int
	OK   bool
}

func FuzzStructInput(f *testing.F) {
	// Seed the initial corpus with a Go struct (gosentry feature).
	f.Add(Input{Data: []byte("A"), S: "B", N: 7, OK: true})

	f.Fuzz(func(t *testing.T, in Input) {
		if in.OK && in.N == 1337 && in.S == "BOOMMOOB" && bytes.Equal(in.Data, []byte("A")) {
			t.Fatalf("boom")
		}
	})
}
```

**How struct seeds (`f.Add`) and struct fuzzing work (the glue made)**

Go’s native fuzzer cannot fuzz a `struct` value directly (it only knows how to mutate a small list of scalar types). gosentry adds a small glue layer: when your fuzz target uses composite types (like `Input`), gosentry fuzzes a single `[]byte` behind the scenes. On every execution, it **decodes** those bytes into your struct (field-by-field, recursively for slices/arrays/pointers) and then calls your `f.Fuzz` callback with the decoded value. The same **encoding** is used for seeds, so `f.Add(Input{...})` becomes an encoded `[]byte` corpus entry that the fuzzer can reuse and mutate like any other seed.

Fuzzers (including LibAFL) mutate raw bytes, so we want a decoder that can turn **any** byte slice into "some" struct value and keep going. JSON/`gob` would reject most random inputs (bad for coverage), and they also don’t populate unexported fields, while fuzzing often benefits from breaking invariants. This custom format is small, fast, deterministic, and tolerant to malformed data.

Under the hood, this uses gosentry’s own simple binary format (not `gob`, not JSON). The code lives in `src/testing/libafl.go`:

* Encode: `libaflMarshalInputs` / `libaflAppendValue`
* Decode: `libaflUnmarshalArgs` / `libaflDecodeValue`

Encoding rules (high level):

* `bool`: 1 byte (`0` or `1`)
* Integers: little-endian bytes (`int`/`uint` are 8 bytes)
* Floats: IEEE-754 bits in little-endian (`float32` = 4 bytes, `float64` = 8 bytes)
* `string`: `uvarint(len)` then raw string bytes
* `[]byte`: `uvarint(len)` then raw bytes
* Other slices: `uvarint(len)` then each element encoded
* Structs: fields encoded in declaration order
* Pointers: 1 byte (`0` = nil, `1` = present) then the pointed value

## Feature 2: Integer overflow and truncation issues detection

#### Overview

This work is inspired from the previously developed [go-panikint](https://github.com/trailofbits/go-panikint). It adds overflow/underflow detection for integer arithmetic operations and (optionally) type truncation detection for integer conversions. When overflow or truncation is detected, a panic with a detailed error message is triggered, including the specific operation type and integer types involved.

*Arithmetic operations*: Handles addition `+`, subtraction `-`, multiplication `*`, and division `/` for both signed and unsigned integer types. For signed integers, covers `int8`, `int16`, `int32`. For unsigned integers, covers `uint8`, `uint16`, `uint32`, `uint64`. The division case specifically detects the `MIN_INT / -1` overflow condition for signed integers. `int64` and `uintptr` are not checked for arithmetic operations.

*Type truncation detection*: Detects potentially lossy integer type conversions. Covers all integer types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`. Excludes `uintptr` due to platform-dependent usage. This is disabled by default.

Overflow detection is enabled by default. To disable it, add `GOFLAGS='-gcflags=-overflowdetect=false'` before your `./make.bash`. You can also enable truncation issues checker with: `-gcflags=-truncationdetect=true`

#### How it works

This feature patches the compiler SSA generation so that integer arithmetic operations and integer conversions get extra runtime checks that call into the runtime to panic...