---
title: Continuously fuzzing Python C extensions
url: https://blog.trailofbits.com/2024/02/23/continuously-fuzzing-python-c-extensions/
source: Trail of Bits Blog
date: 2024-02-24
fetch_date: 2025-10-04T12:06:08.527341
---

# Continuously fuzzing Python C extensions

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Continuously fuzzing Python C extensions

Matt Schwager

February 23, 2024

[fuzzing](/categories/fuzzing/), [open-source](/categories/open-source/)

Deserializing, decoding, and processing untrusted input are telltale signs that your project would benefit from fuzzing. Yes, even Python projects. Fuzzing helps reduce bugs in high-assurance software developed in all programming languages. Fortunately for the Python ecosystem, Google has released [Atheris](https://github.com/google/atheris), a coverage-guided fuzzer for both pure Python code and Python C extensions. When it comes to Python projects, Atheris is really the only game in town if you’re looking for a mature fuzzer. Fuzzing pure Python code typically uncovers unexpected exceptions, which can ultimately lead to denial of service. Fuzzing Python C extensions may uncover memory errors, data races, undefined behavior, and other classes of bugs. Side effects include: memory corruption, remote code execution, and, more generally, all the headaches we’ve come to know and love about C. This post will focus on fuzzing Python C extensions.

We’ll walk you through using Atheris to fuzz Python C extensions, adding a Python project to OSS-Fuzz, and setting up continuous fuzzing through OSS-Fuzz’s integrated CIFuzz tool. OSS-Fuzz is Google’s continuous fuzzing service for open-source projects, making it a valuable tool for open-source developers; as of August 2023, it has helped find and fix over [10,000 vulnerabilities](https://google.github.io/oss-fuzz/#trophies) and 36,000 bugs. We will target the `[cbor2](https://github.com/agronholm/cbor2)` Python library in our fuzzing campaign. This library is the perfect target because it performs serialization and deserialization of a JSON-like, binary format and has an optional C extension implementation for improved performance. Additionally, Concise Binary Object Representation (CBOR) is used heavily within the [blockchain community](https://www.blockchaincommons.com/introduction/Why-CBOR/), which tends to have high assurance and security requirements.

In the end, we found [multiple memory corruption bugs](https://github.com/agronholm/cbor2/issues/198#issuecomment-1869630196) in `cbor2` that could become security vulnerabilities under the right circumstances.

## Fuzzing Python C extensions

Under the hood, Atheris uses libFuzzer to perform its fuzzing. Since [libFuzzer](https://llvm.org/docs/LibFuzzer.html) is built on top of [LLVM and Clang](https://clang.llvm.org/), we will need a Clang installation to fuzz our target. To simplify the installation process, I wrote a Dockerfile to package up all the necessary components into a single Docker image. This creates a repeatable process for fuzzing the current target and an easily extensible artifact for fuzzing future targets. The resulting Docker image includes a Python fuzzing harness to initiate the fuzzing process.

First, we’ll discuss some interesting parts of this Dockerfile, then we’ll investigate the `fuzz.py` fuzzing harness, and finally we’ll build and run the Docker image and find some memory corruption bugs!

### Fuzzing environment

Dockerfiles are a great way to create a self-documenting, reproducible environment. Since fuzzing can often be more art than science, this section will also include some discussion on interesting and non-obvious bits in the Dockerfile. The following Dockerfile was used to fuzz `cbor2`:

```
FROM debian:12-slim

RUN apt update && apt install -y \
    git \
    python3-full \
    python3-pip \
    wget \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

RUN python3 --version

ENV APP_DIR "/app"
ENV CLANG_DIR "$APP_DIR/clang"
RUN mkdir $APP_DIR
RUN mkdir $CLANG_DIR
WORKDIR $APP_DIR

ENV VIRTUAL_ENV "/opt/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

ARG CLANG_URL=https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.6/clang+llvm-17.0.6-aarch64-linux-gnu.tar.xz
ARG CLANG_CHECKSUM=6dd62762285326f223f40b8e4f2864b5c372de3f7de0731cb7cd55ca5287b75a

ENV CLANG_FILE clang.tar.xz
RUN wget -q -O $CLANG_FILE $CLANG_URL && \
    echo "$CLANG_CHECKSUM  $CLANG_FILE" | sha256sum -c - && \
    tar xf $CLANG_FILE -C $CLANG_DIR --strip-components 1 && \
    rm $CLANG_FILE

# https://github.com/google/atheris#building-from-source
RUN LIBFUZZER_LIB=$($CLANG_DIR/bin/clang -print-file-name=libclang_rt.fuzzer_no_main.a) \
    python3 -m pip install --no-binary atheris atheris

# https://github.com/google/atheris/blob/master/native_extension_fuzzing.md#step-1-compiling-your-extension
ENV CC "$CLANG_DIR/bin/clang"
ENV CFLAGS "-fsanitize=address,undefined,fuzzer-no-link"
ENV CXX "$CLANG_DIR/bin/clang++"
ENV CXXFLAGS "-fsanitize=address,undefined,fuzzer-no-link"
ENV LDSHARED "$CLANG_DIR/bin/clang -shared"

ARG BRANCH=master

# https://github.com/agronholm/cbor2
ENV CBOR2_BUILD_C_EXTENSION "1"
RUN git clone --branch $BRANCH https://github.com/agronholm/cbor2.git
RUN python3 -m pip install cbor2/

# Allow Atheris to find fuzzer sanitizer shared libs
# https://github.com/google/atheris/blob/master/native_extension_fuzzing.md#option-a-sanitizerlibfuzzer-preloads
ENV LD_PRELOAD "$VIRTUAL_ENV/lib/python3.11/site-packages/asan_with_fuzzer.so"

# Subject to change by upstream, but it's just a sanity check
RUN nm $(python3 -c "import _cbor2; print(_cbor2.__file__)") | grep asan \
    && echo "Found ASAN" \
    || echo "Missing ASAN"

# 1. Skip allocation failures and memory leaks for now, they are common, and low impact (DoS)
# 2. https://github.com/google/atheris/blob/master/native_extension_fuzzing.md#leak-detection
# 3. Provide the symbolizer to turn virtual addresses to file/line locations
ENV ASAN_OPTIONS "allocator_may_return_null=1,detect_leaks=0,external_symbolizer_path=$CLANG_DIR/bin/llvm-symbolizer"

COPY fuzz.py fuzz.py

ENTRYPOINT ["python3", "fuzz.py"]
CMD ["-help=1"]
```

The following bits of the Dockerfile are relevant for customizations or future projects and are worth discussing further:

1. Installing Clang from the `llvm-project` repository
2. Customizing the image at build-time using Docker [build arguments](https://docs.docker.com/build/guide/build-args/) (e.g., `ARG`)
3. Installing the `cbor2` project
4. Sanity checking the compiled `cbor2` C extension for [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html) (ASan) symbols using `nm`
5. Using `ASAN_OPTIONS` to customize the fuzzing process

First, installing Clang from the `llvm-project` repository:

```
ENV APP_DIR "/app"
ENV CLANG_DIR "$APP_DIR/clang"
...
RUN mkdir $CLANG_DIR
...
ARG CLANG_URL=https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.6/clang+llvm-17.0.6-aarch64-linux-gnu.tar.xz
ARG CLANG_CHECKSUM=6dd62762285326f223f40b8e4f2864b5c372de3f7de0731cb7cd55ca5287b75a
...
ENV CLANG_FILE clang.tar.xz
RUN wget -q -O $CLANG_FILE $CLANG_URL && \
    echo "$CLANG_CHECKSUM  $CLANG_FILE" | sha256sum -c - && \
    tar xf $CLANG_FILE -C $CLANG_DIR --strip-components 1 && \
    rm $CLANG_FILE
```

This code installs the `17.0.6-aarch64-linux-gnu` tarball of Clang. There is nothing particularly special about this tarball other than the fact that it is built for AArch64 and Linux. If you are running this Docker container on a different architecture, you will need to use the corresponding [release tarball](https://github.com/llvm/llvm-project/releases). You can then specify the `CLANG_URL` and `CLANG_CHECKSUM` build arguments as necessary or simply modify the Dockerfile according to your system’s requirements.

The Dockerfile also provides a `BRANCH` build argument. This allows the builder to specify a Git branch or tag that they would like to fuzz against. For example, if you’re working on a pull request and want to fuzz its corresponding branch, you can use this build argument to do so.

Next up, installing the `cbor2` project:

``...