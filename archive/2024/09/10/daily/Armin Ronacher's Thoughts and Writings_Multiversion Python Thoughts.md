---
title: Multiversion Python Thoughts
url: http://lucumr.pocoo.org/2024/9/9/multiversion-python
source: Armin Ronacher's Thoughts and Writings
date: 2024-09-10
fetch_date: 2025-10-06T18:25:07.191483
---

# Multiversion Python Thoughts

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Multiversion Python Thoughts

written on September 09, 2024

Now that [uv](https://docs.astral.sh/uv/) is rapidly advancing I have
started to dive back into making multi-version imports for Python work.
The goal here is to enable multiple resolutions from the solver in uv so
that two incompatible versions of a library can be installed and used
simultaniously.

Simplified speaking it should be possible for a library to depend on both
pydantic 1.x and 2.x simultaniously.

I have not made it work yet, but I have I think found all of the pieces
that stand in the way. This post mostly exists to share how it could be
done with the least amount of changes to Python.

## Basic Operation

Python’s import system places modules in a module cache. This cache is
exposed via `sys.modules`. Every module that is imported is placed in that
container prior to initialization. The key is the import path of the
module. This in some ways presents the first issue.

Note on Terms for Packages, Modules and
DistributionsPython’s terms for packages are super confusing. Here is what I will use
in this article:

* `foo.py`: this is a python “module”. It gets registered in
  `sys.modules` as `'foo'` and has an attribute `__name__` set to
  `'foo'`.
* `foo/__init__.py`: declares also a Python “module” named `'foo'` but
  it is simultaniously a “package”. Unlike a normal module it also has
  two extra attributes: `__path__` which is set to `['./foo']` so that
  sub modules can be found and it has an attribute `__package__` which
  is also set to `'foo'` which marks it as package.
* Additionally on PyPI one can register things. These things were called
  packages at one point and are now mostly called “projects”. Within
  Python however they are not called Projects but “distribution packages”.
  For instance this is what you see when you try to use the
  [importlib.metadata](https://docs.python.org/3/library/importlib.metadata.html)
  API. For now I will just call this a “distribution”.

Note that a distribution can ship both modules and multiple at once. You
could have a package called `whatever` and it reports a `foo.py` file and
a `bar/baz.py` file which in turn would make `foo` and `bar.baz` be
importable.

Say you have two Python distributions both of which provide the same
toplevel package. In that case they are going to clash in `sys.modules`.
As there is actually relationship of the distribution name to the entry in
`sys.modules` this is a problem that does not \*just\* exist with multi
version imports but it’s one that does not happen all that much.

So let’s say we have two distributions: `foo@1.0.0` and `foo@2.0.0`. Both
expose a toplevel module called `foo` which is a true Python package with
a single `__init__.py` file. The installer would already fail to place
these because one fully overrides the other.

So step 1 would be to place these modules in different places. So where
they normally would be in `site-packages`, in this case we might want to
not have these packages there. That solves us the file system clashes.

So we might place them in some extra cache that looks like this:

```
.venv/
    multi-version-packages/
        foo@1.0.0/
            foo/
                __init__.py
        foo@2.0.0/
            foo/
                __init__.py
```

Now that package is entirely non-importable since nothing looks at
`multi-version-packages`. We will need a custom import hook to get them
imported. That import hook will also need to change the name of what’s
stored in `sys.modules`.

So instead of registering `foo` as `sys.modules['foo']` we might want to
try to register it as `sys.modules['foo@1.0.0']` and
`sys.modules['foo@2.0.0']` instead. There is however a catch and that
is this very common pattern:

```
import sys

def import_module(name):
    __import__(name)
    return sys.modules[name]
```

That poses a bit of a problem because someone is probably going to call
this as `import_module('foo')` and now we would not find the entry in
`sys.modules`.

This means that in addition to the new entries in `sys.modules` we would
also need to register some proxies that “redirect” us to the real names.
These proxies however would need to know if they point to `1.0.0` or
`2.0.0`.

## Metadata

So let’s deal with this problem first. How do we know if we need `1.0.0`
or `2.0.0`? The answer is most likely a package’s dependenices. Instead
of allowing a package to depend simultaniously on two different versions
of the same dependency we can start with a much simpler problem and say
that each package can only depend on one version. So that means if I
have a `myapp` package it would have to pick between `foo@1.0.0` or
`foo@2.0.0`. However if it were to depended on another package (say
`slow-package`) that one could depend on a different version of `foo` than
`myapp`:

```
myapp v0.1.0
├── foo v2.0.0
└── slow-package v0.1.0
    └── foo v1.0.0
```

In that case when someone tries to import `foo` we would be consulting the
package metadata of the calling package to figure out which version is
attempted.

There are two challenges with this today and they come from the history of
Python:

1. the import hook does not (always) know which module triggered the
   import
2. python modules do not know their distribution package

Let’s look at these in detail.

## Import Context

The goal is that when `slow_package/__init__.py` imports `foo` we get
`foo@1.0.0` version, when `myapp/__init__.py` improts `foo` we get the
`foo@2.0.0` version. What is needed for this to work is that the import
system understands not just what is imported, but who is importing. In
some sense Python has that. That’s because `__import__` (which is the
entry point to the import machinery) gets the module globals. Here is
what an import statement roughly maps to:

```
# highlevel import
from foo import bar

# under the hood
_rv = __import__('foo', globals(), locals(), ['bar'])
bar = _rv.bar
```

The name of the package that is importing can be retrieved by inspecting
the `globals()`. So in theory for instance the import system could
utilize this information. `globals()['__name__']` would tell us
`slow_package` vs `myapp`. There however is a catch and that is that the
import name is not the distribution name. The PyPI package could be
called `mycompany-myapp` and it exports a python package just called
`myapp`. This happens very commonly in all kinds of ways. For instance
on PyPI one installs `Scikit-learn` but the python package installed is
`sklearn`.

There is however another problem and that is interpreter internals and
C/Rust extensions. We have already established that Python packages will
pass `globals` and `locals` when they import. But what do C extensions
do? The most common internal import API is called
`PyImport_ImportModule` and only takes a module name. Is this a
problem? Do C extensions even import stuff? Yes they do. Here is an
example from pygame:

```
MODINIT_DEFINE (color)
{
     PyObject *colordict;

     colordict = PyImport_ImportModule ("pygame.colordict");

     if (colordict)
     {
         PyObject *_dict = PyModule_GetDict (colordict);
         PyObject *colors = PyDict_GetItemString (_dict, "THECOLORS");
         /* TODO */
     }
     else
     {
         MODINIT_ERROR;
     }

     /* snip */
 }
```

And that makes sense. A sufficiently large python package will have
inter dependencies between the stuff written in C and Python. It’s also
complicated by the fact that the C module does initialize a module, but it
does not have a natural module scope. The way the C extension initializes
the module is with the `PyModule_Create` API:

```
static struct PyModuleDef module_def = {
    PyModuleDef_HEAD_INIT,
    "foo", /* name of module */
    NULL,
    -1,
    SpamMethods
};

PyMODINIT_FUNC
PyInit_foo(void)
{
    return PyModule_C...