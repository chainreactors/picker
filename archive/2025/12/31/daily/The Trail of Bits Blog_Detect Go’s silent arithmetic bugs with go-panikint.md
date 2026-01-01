---
title: Detect Go’s silent arithmetic bugs with go-panikint
url: https://blog.trailofbits.com/2025/12/31/detect-gos-silent-arithmetic-bugs-with-go-panikint/
source: The Trail of Bits Blog
date: 2025-12-31
fetch_date: 2026-01-01T03:35:26.257092
---

# Detect Go’s silent arithmetic bugs with go-panikint

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Detect Go’s silent arithmetic bugs with go-panikint

[Kevin Valerio](/authors/kevin-valerio/)

December 31, 2025

[tool-release](/categories/tool-release/), [go](/categories/go/), [compilers](/categories/compilers/)

Page content

* [The sound of silence](#the-sound-of-silence)
* [How go-panikint works](#how-go-panikint-works)
* [Finding a real-world bug](#finding-a-real-world-bug)
* [Use cases for researchers and developers](#use-cases-for-researchers-and-developers)

Go’s arithmetic operations on standard integer types are silent by default, meaning overflows “wrap around” without panicking. This behavior has hidden an entire class of security vulnerabilities from fuzzing campaigns. Today we’re changing that by releasing [go-panikint](https://github.com/trailofbits/go-panikint), a modified Go compiler that turns silent integer overflows into explicit panics. We used it to find a live integer overflow in the Cosmos SDK’s RPC pagination logic, showing how this approach eliminates a major blind spot for anyone fuzzing Go projects. (The issue in the Cosmos SDK has not been fixed, but a [pull request](https://github.com/cosmos/cosmos-sdk/pull/25049) has been created to mitigate it.)

## The sound of silence

In Rust, debug builds are designed to panic on integer overflow, a feature that is highly valuable for fuzzing. Go, however, takes a different approach. In Go, arithmetic overflows on standard integer types are silent by default. The operations simply “wrap around,” which can be a risky behavior and a potential source of serious vulnerabilities.

This is not an oversight but a deliberate, long-debated [design choice](https://github.com/golang/go/issues/30613) in the Go community. While Go’s memory safety prevents entire classes of vulnerabilities, its integers are not safe from overflow. Unchecked arithmetic operations can lead to logic bugs that bypass critical security checks.

Of course, static analysis tools can identify potential integer overflows. The problem is that they often produce a high number of false positives. It’s difficult to know if a flagged line of code is truly reachable by an attacker or if the overflow is actually harmless due to mitigating checks in the surrounding code. Fuzzing, on the other hand, provides a definitive answer: if you can trigger it with a fuzzer, the bug is real and reachable. However, the problem remained that Go’s default behavior wouldn’t cause a crash, letting these bugs go undetected.

## How go-panikint works

To solve this, we forked the Go compiler and modified its backend. The [core](https://github.com/trailofbits/go-panikint/blob/eb29f694a03fbe38df5ab618acdd0f8b75d4ddd8/src/cmd/compile/internal/ssagen/ssa.go#L5320-L5987) of go-panikint’s functionality is injected during the compiler’s conversion of code into [Static Single Assignment](https://en.wikipedia.org/wiki/Static_single-assignment_form) (SSA) form, a lower-level intermediate representation (IR). At this stage, for every mathematical operation, our compiler inserts additional checks. If one of these checks fails at runtime, it triggers a panic with a detailed error message. These runtime checks are compiled directly into the final binary.

In addition to arithmetic overflows, go-panikint can also detect integer truncation issues, where converting a value to a smaller integer type causes data loss. Here’s an example:

```
var x uint16 = 256
result := uint8(x)
```

Figure 1: Conversion leading to data loss due to unsafe casting

While this feature is functional, we found that it generated false positives during our fuzzing campaigns. For this reason, we will not investigate further and will focus on arithmetic issues.

Let’s analyze the checks for a program that adds up two numbers. If we compile this program and then decompile it, we can clearly see how these checks are inserted. Here, the `if` condition is used to detect signed integer overflow:

* Case 1: Both operands are negative. The result should also be negative. If instead the result (`sVar23`) becomes larger (less negative or even positive), this indicates signed overflow.
* Case 2: Both operands are non-negative. The result should be greater than or equal to each operand. If instead the result becomes smaller than one operand, this indicates signed overflow.
* Case 3: Only one operand is negative. In this case, signed overflow cannot occur.

```
if (*x_00 == '+') {
  val = (uint32)*(undefined8 *)(puVar9 + 0x60);
  sVar23 = val + sVar21;
  puVar17 = puVar9 + 8;
  if (((sdword)val < 0 && sVar21 < 0) && (sdword)val < sVar23 ||
      ((sdword)val >= 0 && sVar21 >= 0) && sVar23 < (sdword)val) {
    runtime.panicoverflow(); // <-- panic if overflow caught
  }
  goto LAB_1000a10d4;
}
```

Figure 2: Example of a decompiled multiplication from a Go program

Using go-panikint is straightforward. You simply compile the tool and then use the resulting Go binary in place of the official one. All other commands and build processes remain exactly the same, making it easy to integrate into existing workflows.

```
git clone https://github.com/trailofbits/go-panikint
cd go-panikint/src && ./make.bash
export GOROOT=/path/to/go-panikint # path to the root of go-panikint
./bin/go test -fuzz=FuzzIntegerOverflow # fuzz our harness
```

Figure 3: Installation and usage of go-panikint

Let’s try with a very simple program. This program has no fuzzing harness, only a main function to execute for illustration purposes.

```
package main
import "fmt"

func main() {
    var a int8 = 120
    var b int8 = 20
    result := a + b
    fmt.Printf("%d + %d = %d\n", a, b, result)
}
```

Figure 4: Simple integer overflow bug

```
$ go run poc.go # native compiler
120 + 20 = -116

$ GOROOT=$pwd ./bin/go run poc.go # go-panikint
panic: runtime error: integer overflow in int8 addition operation

goroutine 1 [running]:
main.main()
	./go-panikint/poc.go:8 +0xb8
exit status 2
```

Figure 5: Running poc.go with both compilers

However, not all overflows are bugs; some are intentional, especially in low-level code like the Go compiler itself, used for randomness or cryptographic algorithms. To handle these cases, we built two filtering mechanisms:

1. Source-location-based filtering: This allows us to ignore known, intentional overflows within the Go compiler’s own source code by whitelisting some given file paths.
2. In-code comments: Any arithmetic operation can be marked as a non-issue by adding a simple comment, like `// overflow_false_positive` or `// truncation_false_positive`. This prevents `go-panikint` from panicking on code that relies on wrapping behavior.

## Finding a real-world bug

To validate our tool, we used it in a fuzzing campaign against the Cosmos SDK and discovered an [integer overflow vulnerability](https://github.com/cosmos/cosmos-sdk/issues/25006) in the RPC pagination logic. When the sum of the offset and limit parameters in a query exceeded the maximum value for a `uint64`, the query would return an empty list of validators instead of the expected set.

```
// Paginate does pagination of all the results in the PrefixStore based on the
// provided PageRequest. onResult should be used to do actual unmarshaling.
func Paginate(
	prefixStore types.KVStore,
	pageRequest *PageRequest,
	onResult func(key, value []byte) error,
) (*PageResponse, error) {
...
end := pageRequest.Offset + pageRequest.Limit
...
```

Figure 6: end can overflow uint64 and return an empty validator list if user provides a large Offset

This finding demonstrates the power of combining fuzzing with runtime checks: `go-panikint` turned the silent overflow into a clear panic, which the fuzzer reported as a crash with a reproducible test case. A [pull request](https://github.com/cosmos/cosmos-sdk/pull/25049) has been created to mitigate the issue.

## Use cases for researchers and developers

We ...