---
title: Constraints are Good: Python's Metadata Dilemma
url: http://lucumr.pocoo.org/2024/11/26/python-packaging-metadata
source: Armin Ronacher's Thoughts and Writings
date: 2024-11-27
fetch_date: 2025-10-06T19:12:11.907504
---

# Constraints are Good: Python's Metadata Dilemma

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Constraints are Good: Python’s Metadata Dilemma

written on November 26, 2024

There is currently an effort underway to build a new universal lockfile
standard for Python, most of which is taking place on the Python
discussion forum. This initiative has highlighted the difficulty of
creating a standard that satisfies everyone. It has become clear that
different Python packaging tools are having slightly different ideas in
mind of what a lockfile is supposed to look like or even be used for.

In those discussions however also a small other aspect re-emerged: Python
has a metadata problem. Python’s metadata system is too complex and
suffers from what I would call “lack of constraints”.

## JavaScript: Example of Useful Constraints

JavaScript provides an excellent example of how constraints can simplify
and improve a system. In JavaScript, metadata is straightforward.
Whether you develop against a package locally or if you are using a
package from npm, metadata represents itself the same way. There is a
single `package.json` file that contains the most important metadata of a
package such as `name`, `version` or `dependencies`. This simplicity
imposes significant but beneficial constraints:

* There is a 1:1 relationship between an npm package and its metadata.
  Every npm package has a single `package.json` file that is the source of
  truth of metadata. Metadata is trivially accessible, even
  programmatically, via `require('packageName/package.json')`.
* Dependencies (and all other metadata) are consistent across platforms
  and architectures. Platform-specific binaries are handled via a filter
  mechanism (`os` and `cpu`) paired with `optionalDependencies`. [1](#fn-1)
* All metadata is static, and updates require explicit changes to
  `package.json` prior to distribution or installation. Tools are
  provided to manipulate that metadata such as `npm version patch`
  which will edit the file in-place.

These constraints offer several benefits:

* Uniform behavior regardless of whether a dependency is installed locally
  or from a remote source. There is not even a filesystem layout difference
  between what comes from git or npm. This enables things like replacing
  an installed dependency with a local development copy, without change in
  functionality.
* There is one singular source of truth for all metadata. You can edit
  `package.json` and any consumer of that metadata can just monitor that
  file for changes. No complex external information needs to be
  consulted.
* Resolvers can rely on a single API call to fetch dependency metadata for
  a version, improving efficiency. Practically this also means that the
  resolver only needs to hit a single URL to retrieve all possible
  dependencies of a dependency. [2](#fn-2)
* It makes auditing much easier because there are fewer moving parts and
  just one canonical location for metadata.

## Python: The Cost of Too Few Constraints

In contrast, Python has historically placed very few constraints on
metadata. For example, the old `setup.py` based build system essentially
allowed arbitrary code execution during the build process. At one point
it was at least strongly suggested that the `version` produced by that
build step better match what is uploaded to PyPI. However, in practice,
if you lie about the version that is okay too. You could upload a source
distribution to PyPI that claims it’s `2.0` but will in fact install
`2.0+somethinghere` or a completely different version entirely.

What happens is that both before a package is published to PyPI and when a
package is installed locally after downloading, the metadata is generated
from scratch. Not only does that mean the metadata does not have to
match, it also means that it’s allowed to be completely different. It’s
absolutely okay for a package to claim it depends on `cool-dependency` on
your machine, but on `uncool-dependency` on my machine. Or to dependent
on different packages depending on the time of the day of the phase of the
moon.

Editable installs and caching are particularly problematic since metadata
could become invalid almost immediately after being written. [3](#fn-3)

Some of this has been somewhat improved because the new `pyproject.toml`
standard encourages static metadata. However build systems are entirely
allowed to override that by falling back to what is called “dynamic
metadata” and this is something that is commonly done.

In practice this system incurs a tremendous tax to everybody that can be
easily missed.

* **Disjointed and complex metadata access:** there is no clear
  relationship of PyPI package name and the installed Python modules.
  If you know what the PyPI package name is, you can access metadata via
  `importlib.metadata`. Metadata is not read from `pyproject.toml`,
  even if it’s static, instead it takes the package name and it accesses
  the metadata from the `.dist-info` folder (most specifically the
  `METADATA` file therein) installed into `site-packages`.
* **Mandatory metadata re-generation:** As a consequence if you edit
  `pyproject.toml` to edit a piece of metadata, you need to re-install the
  package for that metadata to be updated in the `.dist-info`. People
  commonly forget doing that, so desynchronized metadata is very common.
  This is true even for static metadata today!
* **Unclear cache invalidation:** Because metadata can be dynamic, it’s not
  clear when you should automatically re-install a package. It’s not
  enough to just track `pyproject.toml` for changes when dynamic metadata
  is used. `uv` for instance has a really complex, explicit [cache
  management system](https://docs.astral.sh/uv/concepts/cache/#dynamic-metadata) so one
  can help uv detect outdated metadata. This obviously is
  non-standardized, requires uv to understand version control systems and
  is also not shared with other tools. For instance if you know that the
  version information incorporates the git hash, you can tell uv to pay
  attention to git commits.
* **Fragmented metadata storage:** even where generated metadata is stored
  is complex. Different systems have slightly different behavior for
  storing that metadata.

  + When working locally (eg: editable installs) what happens depends
    on the build system:

    - If `setuptools` is used, metadata written into two locations.
      The legacy
      `<PACKAGE_NAME>.egg-info/PKG-INFO` file. Additionally it’s placed
      in the new location for metadata inside `site-packages` in a
      `<PACKAGE_NAME>.dist-info/METADATA` file.
    - If `hatch` and most other modern build systems are used, metadata is
      only written into `site-packages`. (into
      `<PACKAGE_NAME>.dist-info/METADATA`)
    - If no build system is configured it depends a bit on the
      installer. pip will even for an editable install build a
      wheel with `setuptools`, `uv` will only build a wheel and make
      the metadata available if one runs `uv build`. Otherwise the
      metadata is not available (in theory it could be found in
      `pyproject.toml` for as long as it’s not dynamic).
  + For source distributions (`sdist`) first the build step happens as
    in the section before. Afterwards the metadata is thrown into a
    `PKG-INFO` file. It’s currently placed in two locations in the
    `sdist`: `PKG-INFO` in the root and `<PACKAGE_NAME>.egg-info/PKG-INFO`.
    That metadata however I believe is only used for PyPI, when
    installing the `sdist` locally the metadata is regenerated from
    `pyproject.toml` (or if setuptools is used `setup.py`). That’s
    also why metadata can change from what’s in the sdist to what’s
    there after installation.
  + For wheels the metadata is placed in
    `<PACKAGE_NAME>.dist-info/METADATA` exclusively. Wheels have
    static metadata, so no build step is taking place....