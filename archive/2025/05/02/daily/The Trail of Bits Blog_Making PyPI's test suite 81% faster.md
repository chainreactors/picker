---
title: Making PyPI's test suite 81% faster
url: https://blog.trailofbits.com/2025/05/01/making-pypis-test-suite-81-faster/
source: The Trail of Bits Blog
date: 2025-05-02
fetch_date: 2025-10-06T22:27:36.587690
---

# Making PyPI's test suite 81% faster

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Making PyPI's test suite 81% faster

[Alexis Challande](https://bsky.app/profile/darkamaul.bsky.social)

May 01, 2025

[supply-chain](/categories/supply-chain/), [ecosystem-security](/categories/ecosystem-security/), [engineering-practice](/categories/engineering-practice/), [open-source](/categories/open-source/)

Page content

* [The beast: Warehouse’s testing suite](#the-beast-warehouses-testing-suite)
* [Parallelizing test execution for massive gains](#parallelizing-test-execution-for-massive-gains)
  + [Challenge: database fixtures](#challenge-database-fixtures)
  + [Challenge: coverage reporting](#challenge-coverage-reporting)
  + [Challenge: test output readability](#challenge-test-output-readability)
  + [Results](#results)
* [Optimizing coverage with Python 3.12’s `sys.monitoring`](#optimizing-coverage-with-python-312s-sysmonitoring)
  + [Changes in Warehouse](#changes-in-warehouse)
  + [Change impact](#change-impact)
* [Accelerating pytest’s test discovery phase](#accelerating-pytests-test-discovery-phase)
  + [Understanding test collection overhead](#understanding-test-collection-overhead)
  + [Strategic optimization with `testpaths`](#strategic-optimization-with-testpaths)
  + [Impact analysis](#impact-analysis)
* [Removing unnecessary import overhead](#removing-unnecessary-import-overhead)
* [The database migration squashing experiment](#the-database-migration-squashing-experiment)
  + [Quantifying migration overhead](#quantifying-migration-overhead)
  + [Prototyping a solution](#prototyping-a-solution)
  + [Deciding not to merge](#deciding-not-to-merge)
* [Test performance as a security practice](#test-performance-as-a-security-practice)
  + [Quick wins to accelerate your test suite](#quick-wins-to-accelerate-your-test-suite)
  + [Security loves speed](#security-loves-speed)
  + [Acknowledgments](#acknowledgments)

Trail of Bits has collaborated with [PyPI](https://pypi.org/) for several years to add
features and improve security defaults across the Python packaging ecosystem.

Our previous posts have focused on features like [digital attestations](/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/)
and [Trusted Publishing](/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/), but today we’ll look at a equally critical aspect
of holistic software security: test suite performance.

A robust testing suite is essential to the security and reliability of a complex
codebase. However, as test coverage grows, so does execution time, creating
friction in the development process and disincentivizing frequent and meaningful
(i.e., deep) testing. In this post, we’ll detail how we methodically optimized
the test suite for [Warehouse](https://github.com/pypi/warehouse) (the back end that powers PyPI), **reducing
execution time from 163 seconds to 30 seconds** while the **test count grew
from 3,900 to over 4,700**.

![Testing time over the last year on Warehouse](/img/pypi-test-improvements-results.png)

Figure 1: Warehouse test execution time over a 12-month period (March 2024 to April 2025).

We achieved a **81% performance improvement** through several steps:

* Parallelizing test execution with [`pytest-xdist`](https://github.com/pytest-dev/pytest-xdist) (67% relative reduction)
* Using Python 3.12’s [`sys.monitoring`](https://docs.python.org/3.12/library/sys.monitoring.html) for more efficient coverage
  instrumentation (53% relative reduction)
* Optimizing test discovery with strategic testpaths configuration
* Eliminating unnecessary imports that added startup overhead

These optimizations are directly applicable to many Python projects,
particularly those with growing test suites that have become a
bottleneck in development workflows. By implementing even a subset of
these techniques, you can dramatically improve your own test performance
without any costs.

*All times reported in this blog post are from running the Warehouse test suite
at the specified date, on a [n2-highcpu-32](https://cloud.google.com/compute/docs/machine-types#n2-highcpu-32) machine. While not intended as
formal benchmarking results, these measurements provide clear evidence of the
impact of our optimizations.*

## The beast: Warehouse’s testing suite

PyPI is a critical component of the Python ecosystem: it serves over one
billion distribution downloads per day, and developers worldwide depend on
its reliability and integrity for the software artifacts that they
integrate into their stacks.

This criticality makes comprehensive testing non-negotiable, and Warehouse
correspondingly demonstrates exemplary testing practices: 4,734 tests (as of
April 2025) provide 100% branch coverage across the combination of unit and
integration suites. These tests are implemented using the `pytest` framework and
run on every pull request and merge as part of a robust CI/CD pipeline, which
additionally enforces 100% coverage as an acceptance requirement. On our
benchmark system, the current suite execution time is approximately 30 seconds.

This performance represents a dramatic improvement from March 2024, when the test suite:

* Contained approximately 3,900 tests (17.5% fewer tests)
* Required 161 seconds to execute (5.4× longer)
* Created significant friction in the development workflow

Below, we’ll explore the systematic approach we took to achieve these
improvements, starting with the highest-impact changes and working through to
the finer optimizations that collectively transformed the testing experience for
PyPI contributors.

## Parallelizing test execution for massive gains

The most significant performance improvement came from a foundational computing
principle: parallelization. Tests are frequently well-suited for parallel
execution because well-designed test cases are isolated and have no side effects
or globally observable behavior. Warehouse’s unit and integration
tests were already well-isolated, making parallelization an obvious first
target for our optimization efforts.

We implemented parallel test execution using [`pytest-xdist`](https://github.com/pytest-dev/pytest-xdist), a popular plugin
that distributes tests across multiple CPU cores.

`pytest-xdist` configuration is straightforward: this single line change is enough!

```
# In pyproject.toml
[tool.pytest.ini_options]
addopts = [
 "--disable-socket",
 "--allow-hosts=localhost,::1,notdatadog,stripe",
 "--durations=20",
+  "--numprocesses=auto",
]
```

Figure 2: Configuring pytest to run with pytest-xdist.

With this simple configuration, `pytest` automatically uses all available CPU
cores. On our 32-core test machine, this immediately yielded dramatic
improvements while *also* revealing several challenges that required careful
solutions.

### Challenge: database fixtures

Each test worker needed its isolated database instance to prevent cross-test contamination.

```
@pytest.fixture(scope="session")
- def database(request):
+ def database(request, worker_id):
 config = get_config(request)
 pg_host = config.get("host")
 pg_port = config.get("port") or os.environ.get("PGPORT", 5432)
 pg_user = config.get("user")
-   pg_db = f"tests"
+   pg_db = f"tests-{worker_id}"
 pg_version = config.get("version", 16.1)

 janitor = DatabaseJanitor(
```

Figure 3: Changes to the database fixture.

This change made each worker use its own database instance, preventing any
cross-contamination between different workers.

### Challenge: coverage reporting

Test parallelization broke our coverage reporting since each worker process collected coverage data independently. Fortunately, this issue was covered in the [coverage documentation](https://coverage.readthedocs.io/en/latest/subprocess.html#implicit-coverage). We solved the issue by adding a `sitecustomize.py` file.

```
try:
    import coverage
    coverage.process_startup()
except ImportError:
    pass
```

Figur...