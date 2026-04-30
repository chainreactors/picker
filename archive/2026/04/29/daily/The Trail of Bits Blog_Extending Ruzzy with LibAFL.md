---
title: Extending Ruzzy with LibAFL
url: https://blog.trailofbits.com/2026/04/29/extending-ruzzy-with-libafl/
source: The Trail of Bits Blog
date: 2026-04-29
fetch_date: 2026-04-30T05:29:05.075979
---

# Extending Ruzzy with LibAFL

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Extending Ruzzy with LibAFL

[Matt Schwager](/authors/matt-schwager/)

April 29, 2026

[application-security](/categories/application-security/), [tool-release](/categories/tool-release/), [fuzzing](/categories/fuzzing/)

Page content

* [Building with libafl\_libfuzzer](#building-with-libafl_libfuzzer)
* [Fuzzing with LibAFL](#fuzzing-with-libafl)
* [Try out Ruzzy with LibAFL](#try-out-ruzzy-with-libafl)

LibAFL is all the rage in the fuzzing community these days, especially with LLVM’s libFuzzer being placed in [maintenance mode](https://llvm.org/docs/LibFuzzer.html#status). Written in Rust, [LibAFL claims](https://www.s3.eurecom.fr/docs/ccs22_fioraldi.pdf) improved performance, modularity, state-of-the-art fuzzing techniques, and [libFuzzer compatibility](https://github.com/AFLplusplus/LibAFL/tree/0.15.4/crates/libafl_libfuzzer). For these reasons, I set out to add LibAFL support to [Ruzzy](https://github.com/trailofbits/ruzzy), our coverage-guided fuzzer for pure Ruby code and Ruby C extensions. This gives Ruby developers and security researchers access to a more advanced and actively maintained fuzzing engine without changing how they write their fuzzing harnesses.

Ruzzy was [originally built](https://blog.trailofbits.com/2024/03/29/introducing-ruzzy-a-coverage-guided-ruby-fuzzer/) on top of LLVM’s libFuzzer, so using LibAFL’s compatibility layer should be easy enough. However, digging around in the internals of complex systems is never quite as simple as it seems. In this post, I will investigate some of the deep plumbing inside these fuzzing engines, take a detour into executable and linkable format (ELF) files, and ultimately add LibAFL support to Ruzzy.

## Building with libafl\_libfuzzer

Ruzzy currently supports Linux, so I use a [Dockerfile](https://github.com/trailofbits/ruzzy/blob/v0.7.0/Dockerfile) for development and for production fuzzing campaigns. To that end, using a similar Dockerfile for LibAFL support is the simplest integration point. LibAFL provides excellent [documentation](https://github.com/AFLplusplus/LibAFL/tree/0.15.4/crates/libafl_libfuzzer#usage-as-a-standalone-library-for-ccetc) and build scripts to use it as a standalone library. We need to build LibAFL as a standalone library because Ruzzy uses [libFuzzer as a library](https://llvm.org/docs/LibFuzzer.html#using-libfuzzer-as-a-library).

Following along with the standalone `libafl_libfuzzer` documentation, and with the [`build.sh`](https://github.com/AFLplusplus/LibAFL/blob/0.15.4/crates/libafl_libfuzzer_runtime/build.sh) script in hand, we can build `libFuzzer.a`. This is the archive that will ultimately be linked into Ruzzy’s C extension and used to fuzz our target. Here are the relevant lines from our new Dockerfile:

```
# Install Rust nightly via rustup
RUN wget -qO- https://sh.rustup.rs | sh -s -- \
    -y \
    --default-toolchain nightly \
    --component llvm-tools

ENV PATH="/root/.cargo/bin:${PATH}"

# Clone LibAFL
RUN git clone --depth 1 https://github.com/AFLplusplus/LibAFL /libafl

# Build libFuzzer.a from LibAFL's libfuzzer runtime
WORKDIR /libafl/crates/libafl_libfuzzer_runtime

RUN bash build.sh
```

Figure 1: Building LibAFL’s libFuzzer.a (Dockerfile.LibAFL)

This all goes smoothly and gives us our desired output: `libFuzzer.a`. Next, we need to make a slight tweak to Ruzzy’s mechanism for determining a `fuzzer_no_main` library. Using `fuzzer_no_main` and `-fsanitize=fuzzer-no-link` is libFuzzer’s [standard mechanism](https://llvm.org/docs/LibFuzzer.html#using-libfuzzer-as-a-library) for fuzzing code that provides its own `main` function. This makes sense for interpreted languages because the interpreter, well, brings its own `main`.

To accomplish the desired flexibility in Ruzzy, we simply need to prioritize an ENV variable, if present, that specifies the `fuzzer_no_main` library path, then fall back to Clang’s defaults if not:

```
FUZZER_NO_MAIN_LIB_ENV = 'FUZZER_NO_MAIN_LIB'
...
fuzzer_no_main_lib = ENV.fetch(FUZZER_NO_MAIN_LIB_ENV, nil)

if fuzzer_no_main_lib
  LOGGER.info("Using #{FUZZER_NO_MAIN_LIB_ENV}=#{fuzzer_no_main_lib}")
  unless File.exist?(fuzzer_no_main_lib)
    LOGGER.error("#{FUZZER_NO_MAIN_LIB_ENV} file does not exist: #{fuzzer_no_main_lib}")
    exit(1)
  end
else
  fuzzer_no_main_libs = [
    'libclang_rt.fuzzer_no_main.a',
    'libclang_rt.fuzzer_no_main-aarch64.a',
    'libclang_rt.fuzzer_no_main-x86_64.a'
  ]
  fuzzer_no_main_lib = fuzzer_no_main_libs.map { |lib| get_clang_file_name(lib) }.find(&:itself)

  unless fuzzer_no_main_lib
    LOGGER.error("Could not find fuzzer_no_main using #{CC}.")
    LOGGER.error("Please include #{CC} in your path or specify #{FUZZER_NO_MAIN_LIB_ENV} ENV variable.")
    exit(1)
  end
end
```

Figure 2: Allowing an ENV override for the fuzzing library (ext/cruzzy/extconf.rb)

Now, let’s build Ruzzy with LibAFL’s `libFuzzer.a`:

```
# Copy LibAFL's libFuzzer.a from builder stage
COPY --from=libafl-builder /libafl/crates/libafl_libfuzzer_runtime/ libFuzzer.a /usr/lib/libFuzzer.a

# Point Ruzzy at LibAFL's libFuzzer instead of clang's built-in
ENV FUZZER_NO_MAIN_LIB="/usr/lib/libFuzzer.a"

WORKDIR ruzzy/
COPY . .
RUN gem build
RUN RUZZY_DEBUG=1 gem install --development --verbose ruzzy-*.gem
```

Figure 3: Building Ruzzy with LibAFL using a custom FUZZER\_NO\_MAIN\_LIB (Dockerfile.LibAFL)

However, this produces the following error:

```
INFO -- : Using FUZZER_NO_MAIN_LIB=/usr/lib/libFuzzer.a
DEBUG -- : Search for libclang_rt.asan.a using clang-21: success=true exists=false
DEBUG -- : Search for libclang_rt.asan-aarch64.a using clang-21: success=true exists=true
DEBUG -- : Search for libclang_rt.asan-x86_64.a using clang-21: success=true exists=false
DEBUG -- : Creating /usr/lib/llvm-21/lib/clang/21/lib/linux/libclang_rt.asan-aarch64.a sanitizer archive at /tmp/20260320-20-683d0b
DEBUG -- : Merging sanitizer at /tmp/20260320-20-683d0b with libFuzzer at /usr/lib/libFuzzer.a to asan_with_fuzzer.so
/usr/bin/ld: /usr/lib/libFuzzer.a(libFuzzer.o): .preinit_array section is not allowed in DSO
/usr/bin/ld: failed to set dynamic section sizes: nonrepresentable section on output
clang++-21: error: linker command failed with exit code 1 (use -v to see invocation)
ERROR -- : The clang++-21 shared object merging command failed.
*** extconf.rb failed ***
```

Figure 4: Failure linking libFuzzer.a

The key error here is “`.preinit_array` section is not allowed in DSO.” This was a new one for me. What is a `.preinit_array` section, and what is this error trying to tell me? The relevant [ELF documentation](https://refspecs.linuxbase.org/elf/gabi4%2B/ch5.dynamic.html#init_fini) states the following:

> Finally, an executable file may have pre-initialization functions. These functions are executed after the dynamic linker has built the process image and performed relocations but before any shared object initialization functions. Pre-initialization functions are not permitted in shared objects.
> ...
> The DT\_PREINIT\_ARRAY table is processed only in an executable file; it is ignored if contained in a shared object.

So dynamic shared objects (DSOs) cannot contain a `.preinit_array` section. This is exactly what the error told us. `.init`, `.ctors`, `.init_array`, and `.preinit_array` are all mechanisms for running code before `main` starts in an ELF binary. Exploring each of these and the order in which they’re run is beyond the scope of this post (see [this explanation](https://maskray.me/blog/2021-11-07-init-ctors-init-array)), but suffice it to say we need to sidestep this `libafl_libfuzzer` implementation detail. Here’s how LibAFL and libFuzzer differ in this regard:

```
$ objdump -h /usr/lib/libFuzzer.a | grep 'init_array'
3100 .init_array   00000228  ...
5047 .preinit_array 00000008  ...
32136 .init_array.00099 00000008  ...
37083 .init_array.90 00000010  ...

$ o...