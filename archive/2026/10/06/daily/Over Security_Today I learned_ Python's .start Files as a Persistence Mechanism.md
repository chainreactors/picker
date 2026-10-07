---
title: Today I learned: Python's .start Files as a Persistence Mechanism
url: https://dfir.ch/posts/today_i_learned_python_start_files/
source: Over Security
date: 2026-10-06
fetch_date: 2026-10-07T07:55:29.035670
---

# Today I learned: Python's .start Files as a Persistence Mechanism

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Today I learned: Python's .start Files as a Persistence Mechanism

4 Oct 2026

**Table of Contents**

* [Introduction](#introduction)
* [From .pth to .start](#from-pth-to-start)
* [Fantastic .start Files and Where to Find Them](#fantastic-start-files-and-where-to-find-them)
* [Lab: Executing Code Through a .start File](#lab-executing-code-through-a-start-file)
* [Hunting for .start Files](#hunting-for-start-files)
* [Conclusion](#conclusion)

## Introduction

`Python 3.15` (the final release is currently scheduled for October 9, 2026) introduces a new interpreter-startup mechanism worth adding to the DFIR checklist: `.start files`.

A `.start` file placed in a Python `site-packages` directory contains one or more references in the form `package.module:callable`. During normal interpreter initialization, Python resolves those references, imports the corresponding modules, and invokes the callables before control reaches the first line of user-supplied Python code. The application itself does not need to import the module and does not need to know that the `.start` file exists.
From a security perspective, that makes `.start` files an interesting execution primitive. An attacker who can write to an applicable `site-packages` directory can arrange for code to execute whenever an affected Python interpreter starts. Depending on where the file is placed, this may affect a single virtual environment, a user’s Python installations, or a system-wide interpreter.

This is not an accidental Python feature. `.start` files were introduced deliberately by [PEP 829](https://peps.python.org/pep-0829/) as a more structured replacement for executable import lines in `.pth` files (see my article about `.pth` files [here](https://dfir.ch/posts/publish_python_pth_extension/)). The new design substantially improves auditability: the configuration file itself can no longer contain arbitrary Python statements. It does not, however, remove pre-start arbitrary code execution. The referenced module is imported and its callable runs with the privileges and environment of the Python process. See the official [Python documentation](https://docs.python.org/3.15/library/site.html#site-start-files) for details.

## From .pth to .start

Traditionally, Python’s `site` module processes `.pth` files from `site-packages` directories during interpreter initialization. Their original purpose is extending `sys.path`, but there is a second capability, `import something`. Lines beginning with `import` are executed. A package could effectively arrange for arbitrary Python statements to execute whenever an affected interpreter started.

Python 3.15 consequently begins deprecating executable `import` lines inside `.pth` files and introduces `.start` files as their structured replacement. A `.start` file does not contain arbitrary statements. Instead, it contains references such as `foo.submod:initialize`. Python resolves `foo.submod`, obtains the `initialize` object and calls it without arguments.

The important point from a security perspective is that this is still code execution during interpreter startup. [PEP 829](https://peps.python.org/pep-0829/) deliberately makes this execution path easier to identify and audit, which is a substantial improvement over arbitrary one-line Python inside `.pth`. But if an attacker can modify an applicable `site-packages` directory, a `.start` file can still arrange execution every time the affected Python environment starts. The PEP itself explicitly notes that the pre-start execution attack surface is not eliminated; entry points remain capable of arbitrary execution once their module is imported and their callable invoked.

There is also an important migration detail: if a `.start` file and a `.pth` file share the same base name, executable import lines in the corresponding `.pth file` are ignored. From a forensic perspective, this matters when reconstructing startup behavior because the presence of both artifacts does not necessarily mean that both execution mechanisms were active.

## Fantastic .start Files and Where to Find Them

`.start` files live in the same `site-packages` directories Python already inspects for `.pth` files. On a typical Linux installation, these might include paths resembling:

```
/usr/lib/python3.15/site-packages/
/usr/local/lib/python3.15/site-packages/
~/.local/lib/python3.15/site-packages/
```

Or use:

```
python3.15 -m site
```

However, there is a slight forensic problem with doing that. If the interpreter is compromised through a `.start` file, simply starting it may already execute the code we are trying to investigate. For examination, using `-S` is therefore much safer:

```
python3.15 -S -c 'import site; print(site.getsitepackages())'
```

The `-S` option suppresses automatic initialization through `site`. Merely importing the `site` module afterwards does not retroactively perform the normal site modifications unless `site.main()` is explicitly called. A `.start` entry point executes **before the first line of the program the user actually intended to run**. Python’s documentation explicitly states that the startup entry points are executed regardless of whether the associated module would otherwise have been used by the program. `-S`, which disables `site` processing entirely, prevents them from executing.

## Lab: Executing Code Through a .start File

The following test intentionally uses a harmless payload. It writes information about the Python process into `/tmp/python315-start-lab.log` and sets an environment variable that we can inspect from the Python program afterward. First, create an isolated virtual environment:

```
python3.15 -m venv /tmp/py315-start-lab
PY=/tmp/py315-start-lab/bin/python
```

Verify the interpreter:

```
"$PY" --version
```

At the time of writing, this should return something similar to:

```
Python 3.15.0rc3
```

Next, determine the virtual environment’s `site-packages` directory:

```
SITE="$("$PY" -c 'import site; print(site.getsitepackages()[0])')"
echo "$SITE"
```

For this lab, it should resemble:

```
/tmp/py315-start-lab/lib/python3.15/site-packages
```

Now create the module which will contain our startup callable. Python processes `.pth` and `.start` files in alphabetical filename order within each `site-packages` directory. The `00-` prefix used here is therefore intentional and causes this entry point to be encountered early among startup files in the same directory.

```
cat > "$SITE/startup_probe.py" <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import os
import sys

def initialize():
    os.environ["PYTHON_START_LAB"] = "executed"

    event = (
        f"time={datetime.now(timezone.utc).isoformat()} "
        f"pid={os.getpid()} "
        f"ppid={os.getppid()} "
        f"uid={os.getuid()} "
        f"executable={sys.executable!r} "
        f"argv={sys.argv!r}\n"
    )

    with Path("/tmp/python315-start-lab.log").open("a") as f:
        f.write(event)
PY
```

So far nothing special has happened. `startup_probe.py` is simply another Python module.

Now create the startup entry point:

```
cat > "$SITE/00-startup-probe.start" <<'EOF'
startup_probe:initialize
EOF
```

The contents of our site-packages directory now include:

```
startup_probe.py
00-startup-probe.start
```

Remove any previous marker file:

```
rm -f /tmp/python315-start-lab.log
```

Then launch Python with an otherwise completely unrelated command:

```
"$PY" -c 'import os; print("main:", os.getenv("PYTHON_START_LAB"))'
```

The output should be:

```
main: executed
```

Our `-c` expression never imported `startup_probe`. Nevertheless, by the time our expression began executing, `startup_probe.initialize()` had already run. Examining the marker file from the shell:

```
cat /tmp/python315-start-lab.log
```

should produce something resembling:

```
...