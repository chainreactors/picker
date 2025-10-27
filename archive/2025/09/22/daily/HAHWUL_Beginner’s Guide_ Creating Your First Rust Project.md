---
title: Beginner’s Guide: Creating Your First Rust Project
url: https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/
source: HAHWUL
date: 2025-09-22
fetch_date: 2025-10-02T20:30:03.742608
---

# Beginner’s Guide: Creating Your First Rust Project

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/dev/rust/noob-beginners-guide-in-rust/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/)

[한국어](https://www.hahwul.com/ko/dev/rust/noob-beginners-guide-in-rust/)

SEPTEMBER 21, 2025

# Beginner’s Guide: Creating Your First Rust Project

A step-by-step tutorial to install Rust and create, run, test, and build your first project using Cargo.

Getting started with Rust is quick if you follow a few simple steps. In this guide, you’ll install Rust, scaffold a new project, write a tiny program, run tests, and produce a release build.

I’ll keep it minimal and practical so you can get productive fast.

## 1) Install Rust

* Official installer (works on all platforms):

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

* Verify

```
rustc --version
cargo --version
```

## 2) Create a new project

Rust uses `cargo` for building, testing, and dependency management.

* Binary app (recommended for CLI apps and services):

```
cargo new hello_rust
cd hello_rust
```

This creates a basic structure:

```
hello_rust/
├─ Cargo.toml
└─ src/
   └─ main.rs
```

## 3) Write your first program

Open `src/main.rs` and print a greeting:

```
fn main() {
    println!("Hello, Rust!");
}
```

Run it:

```
cargo run
```

## 4) Manage dependencies (when you need them)

If you add dependencies to `Cargo.toml`, build to install them:

```
cargo build
```

You generally won’t need this for the very first “hello world,” but it’s essential once you pull in crates like HTTP clients or web frameworks.

## 5) Format your code

Rust ships a formatter:

```
cargo fmt
```

Run it from the project root to format all sources.

## 6) Add a simple test

For a beginner-friendly pattern, wrap your code in a module and test it:

```
// src/main.rs
mod hello_rust {
    pub fn greet(name: &str) -> String {
        format!("Hello, {}!", name)
    }
}

fn main() {
    println!("{}", hello_rust::greet("Rust"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greet_default() {
        assert_eq!(hello_rust::greet("Rust"), "Hello, Rust!");
    }

    #[test]
    fn test_greet_custom() {
        assert_eq!(hello_rust::greet("World"), "Hello, World!");
    }
}
```

Run tests:

```
cargo test
# or verbose:
cargo test -- --nocapture
```

## 7) Build a binary

Two common ways to build:

* Debug build:

```
cargo build
```

* Release build:

```
cargo build --release
```

Run your binary:

```
./target/debug/hello_rust  # debug
./target/release/hello_rust  # release
```

## 8) Check dependencies graph (nice debugging tool)

```
cargo tree
```

## 9) Optional: Lint with Clippy

Clippy is Rust’s official linter.

* Lint:

```
cargo clippy
```

* Auto-fix:

```
cargo clippy --fix
```

## Visual overview

Here’s a simple flow of your first project:

```
 flowchart LR
  A[Install Rust] --> B[cargo new hello_rust]
  B --> C[Edit src/main.rs]
  C --> D[cargo run]
  D --> E[cargo test]
  E --> F[cargo fmt]
  F --> G[cargo build --release]
  G --> H[Run ./target/release/hello_rust]
```

## What’s next?

* Explore popular crates:
  + Web frameworks: Rocket, Actix-Web
  + CLI: clap
  + HTTP client: reqwest
* Build a CLI tool, a web service, or a small library and publish it on crates.io.

You’ve just created, tested, and built your first Rust project. Keep it small, iterate quickly, and enjoy the safety and performance of Rust.

[#rust](https://www.hahwul.com/tags/rust/)
[#dev](https://www.hahwul.com/tags/dev/)
[#beginner](https://www.hahwul.com/tags/beginner/)
[#tutorial](https://www.hahwul.com/tags/tutorial/)

* Scroll to Top
* Copy URL
* Comments
* Table of Contents
* [Share on X](https://twitter.com/intent/tweet?url=https%3A//www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/&text=Beginner%E2%80%99s%20Guide%3A%20Creating%20Your%20First%20Rust%20Project)

[ ]

[ ]

### Table of Contents

[1) Install Rust](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#1-install-rust)

[2) Create a new project](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#2-create-a-new-project)

[3) Write your first program](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#3-write-your-first-program)

[4) Manage dependencies (when you need them)](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#4-manage-dependencies-when-you-need-them)

[5) Format your code](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#5-format-your-code)

[6) Add a simple test](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#6-add-a-simple-test)

[7) Build a binary](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#7-build-a-binary)

[8) Check dependencies graph (nice debugging tool)](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#8-check-dependencies-graph-nice-debugging-tool)

[9) Optional: Lint with Clippy](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#9-optional-lint-with-clippy)

[Visual overview](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#visual-overview)

[What’s next?](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/#what-s-next)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  + [ENGLISH](https://www.hahwul.com/dev/rust/noob-beginners-guide-in-rust/)
  + [한국어](https://www.hahwul.com/ko/dev/rust/noob-beginners-guide-in-rust/)