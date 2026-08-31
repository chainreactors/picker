---
title: WuppieFuzz v1.7.1
url: https://kitploit.com/en/posts/github-tno-s3-wuppiefuzz-v171
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:25.032106
---

# WuppieFuzz v1.7.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/48890/578d5dda66f01408cc41a008de6f648cd3509f459ace542c1af486a26982f2dc.png)

New releaseAug 30, 2026

# WuppieFuzz v1.7.1

A coverage-guided REST API fuzzer developed on top of LibAFL

Share

# WuppieFuzz v1.7.1

![Logo of WuppieFuzz.](https://raw.githubusercontent.com/tno-s3/wuppiefuzz/HEAD/assets/WuppieFuzz.svg)

TNO developed WuppieFuzz, a coverage-guided REST API fuzzer developed on top of
LibAFL, targeting a wide audience of end-users, with a strong focus on
ease-of-use, explainability of the discovered flaws and modularity. WuppieFuzz
supports all three settings of testing (black box, grey box and white box).

> [!NOTE]
> For a quick, follow-along guidance please follow the [tutorial](https://github.com/tno-s3/wuppiefuzz/blob/HEAD/tutorial)!

## Media coverage

WuppieFuzz has been featured in:

* [The ONE Conference e-magazine 2024](https://emagazine.one-conference.nl/2024/finally-validate-your-publicly-exposed-interfaces-with-ease/)
* [Test your APIs easily with TNO's new REST API fuzzer](https://www.tno.nl/en/newsroom/insights/2024/10/application-security-testing/)
* [OpenAPI.tools listing: WuppieFuzz](https://openapi.tools/tools/wuppiefuzz)
* [Automated REST API Vulnerability Detection with WuppieFuzz (Nordic APIs on YouTube)](https://www.youtube.com/watch?v=JcV9RUBvb2w)
* [Thoughtworks Technology Radar: WuppieFuzz](https://www.thoughtworks.com/radar/tools/wuppiefuzz)

### Scientific publication

If you want to cite WuppieFuzz in academic work, please use the preferred
publication listed in [CITATION.cff](https://github.com/tno-s3/wuppiefuzz/blob/HEAD/CITATION.cff):

Rooijakkers, T., Nijsten, A., Daniele, C., Weitenberg, E., Groenewegen, R., &
Melissen, A. (2026). *WuppieFuzz: Coverage-Guided, Stateful REST API Fuzzing*.
In *Proceedings of the 12th International Conference on Information Systems
Security and Privacy (ICISSP), Volume 2*, 221-231. SciTePress.
<https://doi.org/10.5220/0000217100004061>

## License

WuppieFuzz is licensed under Apache-2.0; see [LICENSE](https://github.com/tno-s3/wuppiefuzz/blob/HEAD/LICENSE).
Third-party license notices are listed in [THIRD\_PARTY\_NOTICES](https://github.com/tno-s3/wuppiefuzz/blob/HEAD/THIRD_PARTY_NOTICES).

## Quick install

For quick installation of WuppieFuzz for popular operating systems (MacOS,
Windows, Linux) see [releases](https://github.com/TNO-S3/WuppieFuzz/releases/) or use [`brew install wuppiefuzz`](https://formulae.brew.sh/formula/wuppiefuzz)

### Short how-to

[![How to use WuppieFuzz? - YouTube](https://raw.githubusercontent.com/tno-s3/wuppiefuzz/HEAD/assets/demo_video.png)](https://www.youtube.com/watch?v=-oR4d9aXrqo)

## Prerequisites for development

To build the project you need to install the following dependencies and tooling

* build-essential `sudo apt install build-essential`
* pkg-config `sudo apt install pkg-config`
* Rust `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

## Run

![WuppieFuzz in action.](https://raw.githubusercontent.com/tno-s3/wuppiefuzz/HEAD/assets/WuppieFuzz-action.jfif)

Before running WuppieFuzz, you have to start your (instrumented) target
application.

Additionally, you must supply WuppieFuzz with an **OpenAPI-specification** so it
knows how to generate and mutate its requests. For help on the command line
arguments, use the following:

root@kitploit:~

```
$ cargo run -- --help # shows help for required parameters and flags

Usage: wuppiefuzz [OPTIONS] [OPENAPI_SPEC.YAML]
...
```

For example, to run WuppieFuzz against a Java target with the JaCoCo agent
attached, you specify its OpenAPI file (containing the URL the target is running
on in the API specification). In addition, you specify that the coverage format
is JaCoCo, and give the classes directory as follows:

root@kitploit:~

```
cargo run -- fuzz openapi.yaml --coverage-format jacoco --jacoco-class-dir ../Targets/app/target/classes/
```

## Configuration file

If you want to use a configuration file instead of/in combination with command
line arguments, you can use the flag `--config <CONFIG_FILE>`. In case you use
command line arguments in combination with a configuration file, command line
arguments take precedence.

The configuration file should be a yaml file and contain a line for each command
line argument you want to specify, for example:

root@kitploit:~

```
coverage_format: jacoco
output_format: human-readable
source_dir: "/swagger-petstore/src/main/java"
jacoco_class_dir: "/swagger-petstore/target"
timeout: 20
```

An example run command could in this case be:

root@kitploit:~

```
$ cargo run -- fuzz --config=config.yaml --report --coverage-host=localhost:6300 --timeout=10 ./openapi.yaml
```

This line would combine the arguments from the command line and from the config
file. Since the flag `--timeout` is specified in both, the timeout specified in
the command line (10 seconds) will take precedence.

In the directory `example_configs/` you will find two example config files to
use for generating coverage reports with JaCoCo for Java code and for generating
coverage reports with LCOV for Python code.

## Reports

When you WuppieFuzz with the `--report` flag, a subdirectory is made inside
`reports/` with a timestamp as its name. All supported coverage report(s) are
written into this subdirectory. There are two types of coverage reports:

1. **endpoint coverage**: this can always be generated since it only requires
   the OpenAPI-spec.
2. **code coverage**: currently only supported for JaCoCo, but we aim to support
   more. The tricky part is that this requires a mapping from coverage to source
   files, and robust report generation that uses this.

On top of that a database is filled with all request information related to your
fuzzing campaign. This database can be visualised and explored through the
Grafana dashboard.

## Structure of this repository

* **assets**: logos, images, etc.
* **coverage\_agents**: code and instructions for coverage tracking to slap onto
  various targets
* **example\_configs**: example configuration files to configure WuppieFuzz
* **src**: source code of WuppieFuzz
* **tutorial**: an in-depth and low-level tutorial about how to fuzz a specific
  target and how to interpret fuzzing results
* **dashboard**: tooling to triage the fuzzing results and performance

For more information on each of these, see the READMEs in these directories.

## Development build

By default, WuppieFuzz vendors its C dependencies (OpenSSL, SQLite, Z3) so that
a regular `cargo build` works out of the box. For faster compilation during
development, you can disable all vendored dependencies and link against
system-installed libraries instead.

> [!NOTE]
> The `z3` crate requires Z3 4.15+, which is newer than the version shipped by
> most Linux distribution package managers. Install Z3 via
> [Homebrew](https://brew.sh/) (`brew install z3`) to get a compatible version.

### System dependencies

Install the following libraries on your system:

**Debian/Ubuntu:**

root@kitploit:~

```
sudo apt install libssl-dev libsqlite3-dev
brew install z3  # apt's libz3-dev is too old; use Homebrew instead
```

On Linux, Homebrew installs to a non-standard path. Add its library directory
to your environment so the compiler and runtime linker can find Z3:

root@kitploit:~

```
eval "$(brew shellenv)"
export LIBRARY_PATH="$(brew --prefix z3)/lib:$LIBRARY_PATH"
export LD_LIBRARY_PATH="$(brew --prefix z3)/lib:$LD_LIBRARY_PATH"
```

> [!TIP]
> Add the lines above to your `~/.bashrc` or `~/.zshrc` to make them permanent.

**Fedora (42+):**

root@kitploit:~

```
sudo dnf install opens...