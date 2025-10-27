---
title: Plugin Spotlight: CoolSigMaker
url: https://binary.ninja/2024/10/01/plugin-spotlight-coolsigmaker.html
source: Binary Ninja
date: 2024-10-02
fetch_date: 2025-10-06T18:54:00.530281
---

# Plugin Spotlight: CoolSigMaker

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Plugin Spotlight: CoolSigMaker

* [unknowntrojan](https://github.com/unknowntrojan)
* 2024-10-01
* [plugin](/tag/plugin)

*EDITORâS NOTE: This guest-post was brought to you by [unknowntrojan](https://unknowntrojan.win/about/), shedding light on one of the lesser-known plugins, [coolsigmaker](https://github.com/unknowntrojan/binja_coolsigmaker).*

A common desire in reverse engineering is to match re-used code across multiple binaries. Whether youâre doing malware lineage tracking, identifying a statically compiled library, or any other use case about identifying similar code, there are multiple technologies that attempt to solve parts of this problem. Other tools for related problems include [SigKit](https://github.com/Vector35/sigkit) (Binary Ninjaâs [static library detection](https://docs.binary.ninja/dev/annotation.html?h=sigkit#signature-library)), IDAâs [FLIRT/FLAIR](https://docs.hex-rays.com/user-guide/signatures/flirt) and [Lumina](https://docs.hex-rays.com/user-guide/lumina) features, or even more advanced systems like [Diaphora](http://diaphora.re/) or [BinDiff](https://www.zynamics.com/bindiff.html).

Related to those, you might already be familiar with the âSigMakerâ style of plugins for various platforms[[1]](https://github.com/ajkhoury/SigMaker-x64) [[2]](https://github.com/apekros/binja_sigmaker) [[3]](https://github.com/Alex3434/Binja-SigMaker). These plugins generate patterns from code that can be used to find said code across different binaries or find the same function reliably between application updates. This is useful for malware classification and static-library identification among other purposes.

[binja\_coolsigmaker](https://github.com/unknowntrojan/binja_coolsigmaker) is just that: a fast and reliable âSigMakerâ plugin for Binary Ninja.

When I started using Binary Ninja, there were two plugins that did roughly the same thing. One was written in Python, and was very slow. The other was written in C++, but would often crash.

I decided to write this plugin in Rust, as it is my language of choice, and would provide me with an easier time extending functionality.

The name is a derivative of the previous plugins because, of course, itâs cool!

## Installation

*EDITORâS NOTE:*

```
Because the Binary Ninja plugin manager doesn't currently support native
plugins (though it's in-progress!), you'll need to manually install the plugin
yourself.

That said, as of the latest dev release today (builds >= 6135), the plugin
manager can now show native plugins and take you to the GitHub page for more
information.

In fact, this plugin is the very first example listed there.
```

### Prerequisites

#### Rust

To compile this plugin, you will need to install Rust via [rustup](https://rustup.rs/), if you havenât already.

This plugin requires the [`nightly` channel](https://rust-lang.github.io/rustup/concepts/channels.html). The channel can be selected in rustupâs installation dialog, or be installed at any time once rustup is installed.

#### LLVM

Compiling the plugin requires an installation of [LLVM](https://llvm.org/).

This is required by the Binary Ninja Rust API for the bindings generation process.

### Compiling

Clone the repository and checkout the branch corresponding to your Binary Ninja update channel.
`master` corresponds to stable builds and `dev` to development builds.

```
git clone https://github.com/unknowntrojan/binja_coolsigmaker.git

# If compiling for the development channel:
git checkout dev

# If compiling for the stable channel:
git checkout master
```

Due to a limitation with Cargo, it is required to delete the `Cargo.lock` file whenever the `binaryninja` dependency changes or is supposed to change. To be on the safe side, simply delete it every time before compiling.

```
rm Cargo.lock
cargo build --release
```

After the build has completed successfully, copy the resulting binary (`binja_coolsigmaker.dll` on Windows, `libbinja_coolsigmaker.dylib` on macOS, `libbinja_coolsigmaker.so` on Linux) into your Binary Ninja `plugins` folder (a sub-folder of your [user folder](https://docs.binary.ninja/guide/index.html#user-folder)).

### Troubleshooting

If the plugin doesnât load, check the Binary Ninja log for details.

If it complains about a mismatched API version, either update your Binary Ninja to the newest Stable/Dev and double-check that you are on the correct branch of CoolSigMaker, or add a version tag to the `binaryninja` dependency in `Cargo.toml`. (e.g. `v4.1.5747-stable`, see [Tags](https://github.com/Vector35/binaryninja-api/tags)). Note that you can find the correct version for your current install by looking for the [api\_REVISION.txt](https://docs.binary.ninja/dev/plugins.html?h=api_revision#project-setup) file inside of your Binary Ninja install path.

## Using the plugin

If everything went well, you are now ready to start using the plugin.

The plugin configuration is available under the `CoolSigMaker` category in the Binary Ninja Settings Menu.

The default settings will do just fine, although I recommend adjusting the `Signature Type` according to your preference.

The `Rust` signature type is for use with [coolfindpattern](https://github.com/unknowntrojan/coolfindpattern).

![Settings](/blog/images/coolsigmaker/settings2.png)

### Creating Signatures

To create a signature, navigate to the part of code you want to generate a signature for.

![Selecting](/blog/images/coolsigmaker/selecting.png)

Then open the `Plugins` menu and click `CSM - Create Signature from Address`.

![Creating](/blog/images/coolsigmaker/creating.png)

If the signature creation succeeded, the signature will now be in your clipboard and displayed in the log.

### Searching for Signatures

To search for a signature, copy the desired signature to your clipboard and click `CSM - Find Signature`.

The plugin will attempt to parse it according to the `Signature Type` selected in the Settings.

![Result](/blog/images/coolsigmaker/result.png)

*Log results when creating and searching for a signature*

## Practical Examples

### Patching a binary reliably across updates

You might want to patch (or hook into) a binary that gets regular updates. Simply hardcoding an address to patch wonât work here.

This is a good use-case for signatures.

Given this scenario, upon finding the place that you wish to patch/hook, like this function:

![Example 0](/blog/images/coolsigmaker/example0.png)

Create a signature for it:

![Example 1](/blog/images/coolsigmaker/example1.png)

And when the application updates, the signature will (hopefully) stay valid until the function itself is updated.

![Example 2](/blog/images/coolsigmaker/example2.png)

## Contributing/Issues

If you wish to improve CoolSigMaker, or are having issues, feel free to head to the [repository](https://github.com/unknowntrojan/binja_coolsigmaker) and open an issue.

## About Us

Binary Ninja is brought to you by Vector 35, a group of hackers who started to make games and reverse engineering tools. Or, maybe they're game developers who still think they can hack? Either way, they're having fun doing it.

Â© 2015-2025 Vector 35. All rights reserved.

Binary...