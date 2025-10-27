---
title: How to Hack Web Assembly
url: https://www.hahwul.com/sec/how-to-hack/web-assembly/
source: HAHWUL
date: 2025-09-13
fetch_date: 2025-10-02T20:05:52.383147
---

# How to Hack Web Assembly

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/sec/how-to-hack/web-assembly/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/sec/how-to-hack/web-assembly/)

[한국어](https://www.hahwul.com/ko/sec/how-to-hack/web-assembly/)

SEPTEMBER 12, 2025

# How to Hack Web Assembly

WebAssembly is a low-level assembly language that can process binary formats on the web. It runs on the web but feels like native execution, and can work together with JavaScript to achieve both high-performance processing and rapid implementation.

This document outlines methods for testing and finding security vulnerabilities in WebAssembly applications.

### Structure

#### WebAssembly Overview

WebAssembly is a low-level assembly language that can process binary formats on the web. It works together with JavaScript and has the following characteristics:

* Near-native performance
* Interoperability with JavaScript
* Safe execution in browser sandbox environments
* Compilable from various languages like C, C++, Rust, etc.

![WebAssembly Structure](https://3.bp.blogspot.com/-XnKxEJq5EeU/W7j6RNjT7pI/AAAAAAAADdI/mcfmbNwF03YaaSWyfDBEzSnQi71sGtY-ACLcBGAs/s1600/1415.png)

#### Basic Example

```
#include <stdio.h>
#include <sys/uio.h>

#define WASM_EXPORT __attribute__((visibility("default")))

WASM_EXPORT
int main(void) {
  printf("Hello World\n");
}

/* External function that is implemented in JavaScript. */
extern void putc_js(char c);

/* Basic implementation of the writev sys call. */
WASM_EXPORT
size_t writev_c(int fd, const struct iovec *iov, int iovcnt) {
  size_t cnt = 0;
  for (int i = 0; i < iovcnt; i++) {
    for (int j = 0; j < iov[i].iov_len; j++) {
      putc_js(((char *)iov[i].iov_base)[j]);
    }
    cnt += iov[i].iov_len;
  }
  return cnt;
}
```

### API Documents

* WebAssembly: <https://webassembly.org/docs/>
* MDN WebAssembly: <https://developer.mozilla.org/en-US/docs/WebAssembly>
* WebAssembly Text Format: <https://webassembly.github.io/spec/core/text/index.html>

## Hack Mechanism

WebAssembly operates the same way in each browser, creating an environment where both traditional binary attacks and web hacking techniques can be applied.

### Security Testing Points

WebAssembly applications have the following security testing points:

* **Traditional binary-related attacks**: Known techniques like BOF, FSB, OOB can be applied, but WebAssembly has built-in security logic making techniques like ROP difficult.
* **Web attacks**: The difference from existing web attacks is that web payloads or attack code can pass through the C layer.
* **Indirect function calls**: When gaining JS control through XSS, the attack vectors expand significantly.

### Code audit

WebAssembly files typically have a `.wasm` extension and are provided in binary format. For analysis, you need to decompile them and examine the related JavaScript code together.

#### Find WASM files

Methods to find WebAssembly files:

1. **Finding WebAssembly instances in JavaScript**: Like SWF and ActiveX, since they're ultimately handled in JS, function or address information remains in the code.
2. **Tracking WebAssembly loading functions**:

```
// Using instantiateStreaming
WebAssembly.instantiateStreaming(fetch('simple.wasm'), importObject)
.then(results => {
  // Do something with the results!
});

// Using XMLHttpRequest
request = new XMLHttpRequest();
request.open('GET', 'simple.wasm');
request.responseType = 'arraybuffer';
request.send();

request.onload = function() {
  var bytes = request.response;
  WebAssembly.instantiate(bytes, importObject).then(results => {
    results.instance.exports.exported_func();
  });
};
```

3. **Browser Developer Tools**: You can directly check wasm files in the Sources tab.

#### WASM File Structure

WASM file headers start with `.asm`:

```
hexdump -C fail.wasm
00000000  00 61 73 6d 01 00 00 00  01 85 80 80 80 00 01 60  |.asm...........`|
00000010  00 01 7f 03 82 80 80 80  00 01 00 06 81 80 80 80  |................|
00000020  00 00 07 8b 80 80 80 00  01 07 66 61 69 6c 5f 6d  |..........fail_m|
00000030  65 00 00 0a 8d 80 80 80  00 01 87 80 80 80 00 00  |e...............|
00000040  41 01 41 00 6d 0b                                 |A.A.m.|
00000046
```

#### Decompile WASM & find info

Installing tools for WASM decompilation:

```
git clone --recursive https://github.com/WebAssembly/wabt
apt install clang     # (if clang is not available)
make
```

**Object dump**:

```
./wasm-objdump -xd fail.wasm

fail.wasm:    file format wasm 0x1

Section Details:

Type[1]:
- type[0] () -> i32
Function[1]:
- func[0] sig=0 <fail_me>
Global[0]:
Export[1]:
- func[0] <fail_me> -> "fail_me"

Code Disassembly:

00003a <fail_me>:
000040: 41 01                      | i32.const 1
000042: 41 00                      | i32.const 0
000044: 6d                         | i32.div_s
000045: 0b                         | end
```

**Decompile to C**:

```
./wasm2c fail.wasm
```

### Live audit

#### Test with devtools

You can access WebAssembly objects in the browser's developer tools:

```
// Check WebAssembly object
WebAssembly
// CompileError: function CompileError()
// Global: function Global()
// Instance: function Instance()
// LinkError: function LinkError()
// Memory: function Memory()
// Module: function Module()
// RuntimeError: function RuntimeError()
// Table: function Table()
// compile: function compile()
// compileStreaming: function compileStreaming()
// instantiate: function instantiate()
// instantiateStreaming: function instantiateStreaming()
// validate: function validate()
```

#### Function testing

You can directly call WASM functions from JavaScript for testing. This is identical to SWF or ActiveX analysis methods.

![Function testing](https://4.bp.blogspot.com/-8-VATL857N8/W7j6bL8UhWI/AAAAAAAADdM/6L4q2M1SdBQZDlNEIMQ5om9H3eiFDYVoACLcBGAs/s1600/Selection_026.png)

### A major weakness

#### Memory Safety Issues

While WebAssembly provides memory safety, the following vulnerabilities can still occur:

* Buffer overflow in linear memory
* Integer overflow/underflow
* Out-of-bounds memory access

#### JavaScript Interface Vulnerabilities

Vulnerabilities that can occur at the interface between WASM and JavaScript:

* Type confusion in parameter passing
* Improper input validation
* Memory corruption through shared memory

#### SOP (Same-Origin Policy) Issues

When fetching WASM files using fetch, etc., the browser's SOP is forcibly applied:

```
fetch('https://www.hahwul.com')
// Cross-origin request blocked: Same-origin policy blocks remote resources
```

However, since WASM can pass data to JavaScript:

* Check CORS application scope for potential SOP bypass
* Verify if file upload is possible on the same domain (possibility of loading attacker-reconstructed WASM files)

## 🛠 Environment

### Essential Tools

**WABT (WebAssembly Binary Toolkit)**:

```
git clone --recursive https://github.com/WebAssembly/wabt
make
```

Included tools:

* `wasm-objdump`: WASM file structure analysis
* `wasm2c`: Decompile WASM to C code
* `wasm2wat`: Convert WASM to text format
* `wat2wasm`: Convert text format to WASM

**Emscripten**:

```
git clone https://github.com/emscripten-core/emsdk.git
cd emsdk
./emsdk install latest
./emsdk activate latest
```

**Browser DevTools**: All major browsers support WebAssembly debugging

### Testing Methodology

1. **Static Analysis**: WASM file analysis using WABT tools
2. **Dynamic Analysis**: Runtime analysis through browser developer tools
3. **Interface Testing**: Data flow analysis between JavaScript-WASM
4. **Memory Analysis**: Linear memory access pattern verification

## Articles

* [How to analyze security vulnerabilities in WebAssembly?](https://www.hahwul.com/2018/10/06/hacking-security-analysis-web-assembly/)

## References

* [WebAssembly Security](https://webassembly.org/docs/security/)
* [BlackHat WebAssembly Paper](ht...