---
title: ABI compatibility in Python: How hard could it be?
url: https://blog.trailofbits.com/2022/11/15/python-wheels-abi-abi3audit/
source: Trail of Bits Blog
date: 2022-11-16
fetch_date: 2025-10-03T22:52:27.823920
---

# ABI compatibility in Python: How hard could it be?

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# ABI compatibility in Python: How hard could it be?

[William Woodruff](https://infosec.exchange/%40yossarian)

November 15, 2022

[audits](/categories/audits/)

**TL;DR:** *Trail of Bits has developed [abi3audit](https://github.com/trailofbits/abi3audit), a new Python tool for checking Python packages for CPython application binary interface (ABI) violations. We’ve used it to discover hundreds of inconsistently and incorrectly tagged package distributions, each of which is a potential source of crashes and exploitable memory corruption due to undetected ABI differences. It’s publicly available under a permissive open source license, so you can use it today!*

Python is one of the most popular programming languages, with a correspondingly large package ecosystem: over 600,000 programmers use [PyPI](https://pypi.org/) to distribute over 400,000 unique packages, powering much of the world’s software.

The age of Python’s packaging ecosystem also sets it apart: among general-purpose languages, it is predated only by Perl’s [CPAN](https://www.cpan.org/). This, combined with the mostly independent development of packaging tooling and standards, has made Python’s ecosystem among the more complex of the major programming language ecosystems. Those complexities include:

* Two major current packaging formats (source distributions and wheels), as well as a smattering of domain-specific and legacy formats (zipapps, Python Eggs, [conda’s own format](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html), &c.);
* A constellation of different packaging tools and package specification files: [setuptools](https://pypi.org/project/setuptools/), [flit](https://flit.pypa.io/), [poetry](https://python-poetry.org/), and [PDM](https://github.com/pdm-project/pdm), as well as [pip](https://pip.pypa.io/), [pipx](https://github.com/pypa/pipx), and [pipenv](https://pipenv.pypa.io/) for actually installing packages;
* …and a corresponding constellation of package and dependency specification files: [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) (PEP 518-style), [pyproject.toml (Poetry-style)](https://python-poetry.org/docs/pyproject/), setup.py, setup.cfg, Pipfile, requirements.txt, MANIFEST.in, and so forth.

This post will cover just one tiny piece of Python packaging’s complexity: the CPython stable ABI. We’ll see what the stable ABI is, why it exists, how it’s integrated into Python packaging, and how **each piece goes terribly wrong** to make accidental ABI violations easy.

## The CPython stable API and ABI

Not unlike many other reference implementations, Python’s reference implementation (CPython) is written in C and provides two mechanisms for native interaction:

* A C Application Programming Interface (API), allowing C and C++ programmers to compile against CPython’s public headers and use any exposed functionality;
* An Application Binary Interface (ABI), allowing any language with C ABI support (like Rust or Golang) to link against CPython’s runtime and use the same internals

Developers can use the CPython API and ABI to write [CPython extensions](https://docs.python.org/3/extending/extending.html). These extensions behave exactly like ordinary Python modules but interact directly with the interpreter’s implementation details rather than the “high-level” objects and APIs exposed in Python itself.

CPython extensions are a cornerstone of the Python ecosystem: they provide an “escape hatch” for performance-critical tasks in Python, as well as enable code reuse from native languages (like the broader C, C++, and Rust packaging ecosystems).

At the same time, extensions pose a problem: CPython’s APIs change between releases (as the implementation details of CPython change), meaning that **it is unsound, by default**, to load a CPython extension into an interpreter of a different version. The implications of this unsoundness vary: a user might get lucky and have no problems at all, might experience crashes due to missing functions or, worst of all, **experience memory corruption** due to changes in function signatures and structure layouts.

To ameliorate the situation, CPython’s developers created the [stable API and ABI](https://docs.python.org/3/c-api/stable.html): a set of macros, types, functions, and data objects that are guaranteed to remain available and forward-compatible between minor releases. In other words: a CPython extension built for CPython 3.7’s stable API will also load and function correctly on CPython 3.8 and forwards, but is **not** guaranteed to load and function with CPython 3.6 or earlier.

At the ABI level, this compatibility is referred to as “`abi3`”, and is *optionally* tagged in the extension’s filename: `mymod.abi3.so`, for example, designates a loadable stable-ABI-compatible CPython extension module named `mymod`. Critically, the Python interpreter does not *do* anything with this tag — it’s simply ignored.

This is the first strike: CPython has no notion of whether an extension is **actually** stable-ABI-compatible. We’ll now see how this compounds with the state of Python packaging to produce even more problems.

## CPython extensions and packaging

On its own, a CPython extension is just a bare Python module. To be useful to others, it needs to be *packaged and distributed* like all other modules.

With [source distributions](https://packaging.python.org/specifications/source-distribution-format/), packaging a CPython extension is straightforward (for some definitions of straightforward): the source distribution’s build system (generally `setup.py`) describes the compilation steps needed to produce the native extension, and the package installer runs these steps during installation.

For example, here’s how we define [microx’s](https://github.com/lifting-bits/microx) native extension (microx\_core) using `setuptools`:

[![](/img/wpdump/6bcaf24119a574fb51d118f270d6a4aa.png)](/img/wpdump/6bcaf24119a574fb51d118f270d6a4aa.png)

Distributing a CPython extension via source distribution has advantages (✅) and disadvantages (❌):

✅API and ABI stability are **non-issues**: the package either builds during installation or it doesn’t and, when it does build, it runs against the same interpreter that it built against.

✅Source builds are **burdensome for users**: they require end-users of Python software to install the CPython development headers, as well as maintain a native toolchain corresponding to the language or ecosystem that the extension targets. That means requiring a C/C++ (and increasingly, Rust) toolchain on every deployment machine, adding size and complexity.

❌Source builds are **fundamentally fragile**: compilers and native dependencies are in constant flux, leaving end users (who are Python experts at best, not compiled language experts) to debug compiler and linker errors.

The Python packaging ecosystem’s solution to these problems is [wheels](https://packaging.python.org/en/latest/specifications/binary-distribution-format/). Wheels are a *binary distribution format*, which means that they can (but are not required to) provide **pre-compiled** binary extensions and other shared objects that can be installed as-is, without custom build steps. This is where ABI compatibility is **absolutely essential**: binary wheels are loaded blindly by the CPython interpreter, so any mismatch between the actual and expected interpreter ABIs can cause crashes (or worse, exploitable memory corruption).

Because wheels can contain pre-compiled extensions, they need to be tagged for the version(s) of Python that they support. This tagging is done with [PEP 425-style](https://peps.python.org/pep-0425/) “compatibility” tags: `microx-1.4.1-cp37-cp37m-macosx_10_15_x86_64.whl` designates a wheel that was built for CPython 3.7 on macOS 10.15 for x86-6...