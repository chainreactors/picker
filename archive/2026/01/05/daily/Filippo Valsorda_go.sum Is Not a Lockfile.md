---
title: go.sum Is Not a Lockfile
url: https://words.filippo.io/gosum/
source: Filippo Valsorda
date: 2026-01-05
fetch_date: 2026-01-06T03:26:44.261236
---

# go.sum Is Not a Lockfile

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

5 Jan 2026

# go.sum Is Not a Lockfile

I need everyone to stop looking at `go.sum`, *especially* to analyze dependency graphs. It is not a “lockfile,” and it has zero semantic effects on version resolution. There is truly no use case for ever parsing it outside of cmd/go.

`go.sum` is only a local cache for the [Go Checksum Database](https://go.dev/ref/mod#checksum-database). It’s a map of module versions to their cryptographic hashes. Those versions may or may not be in use; it doesn’t matter to package resolution.

`go.sum` was not even enabled by default in the original modules design, precisely because it has no observable effect on builds![1](#fn:default) Its (important) purpose is exclusively tightening the security story: the Checksum Database ensures the whole ecosystem shares the same contents for a given module version, regardless of how it is downloaded, and `go.sum` makes that guarantee local and self-contained.

Instead, just look at `go.mod`. It lists the precise version at which all dependencies are built. [Since Go 1.17](https://go.dev/ref/mod#go-mod-file-go) (released August 2021), it includes all transitive dependencies needed to build the main module and its tests.[2](#fn:other)

You can either parse `go.mod` with [golang.org/x/mod/modfile](https://golang.org/x/mod/modfile), run `go mod edit -json` to get its JSON representation,[3](#fn:all) or parse it according to [its specification](https://go.dev/ref/mod#go-mod-file).

This is the end of the Public Service Announcement. Read on for some `go.mod` nerdery.

## Manifests and lockfiles

The enduring confusion around `go.mod` and `go.sum` is due to the fact that most other languages also have two package-related files, but theirs *both* matter to version resolution. These two files are usually called manifest and lockfile.

The manifest (e.g. `pyproject.toml`, `package.json`, `Cargo.toml`) usually lists *some* dependencies along with potentially complex rules for which versions are supported. These rules usually apply transitively to dependents, making version resolution extremely hard and/or slow in the general case, and sometimes unsolvable. The manifest is not always guaranteed to list all direct dependencies, and no automated mechanism ensures your code actually works with e.g. the minimum allowed manifest version of its dependencies.

The lockfile (e.g. `uv.lock`, `package-lock.json`, `Cargo.lock`) is a relatively recent innovation in some ecosystems, and it lists the actual versions used in the most recent build. It is not really human-readable, and usually doesn’t apply recursively to dependents, allowing [the rapid spread of supply-chain attacks](https://research.swtch.com/npm-colors).

I honestly find the manifest version ranges essentially useless, and get endlessly confused trying to remember which commands modify the lockfile (and when/why) and which ones respect it.

In Go, `go.mod` serves as both manifest and lockfile, and more: it lists all dependencies, direct and transitive, and their exact version to be used when the module is the main module. Semantic versioning is assumed, and those versions are also the [minimum versions](https://go.dev/ref/mod#minimal-version-selection) applied to dependents’ module graphs. Different major versions of the same module are considered essentially separate modules.

Notice how there is no way to accidentally use a feature introduced in a version that your dependents won’t have. Also, when adding a dependency, you don’t automatically get the latest—potentially untested/compromised—version of all *its* dependencies. Finally, there can’t be diamond dependency conflicts.

All that with a single, human-readable file: `go.mod`.

All `go` commands take a `-mod` flag. If set to `mod`, missing dependencies can be added to `go.mod` automatically if necessary, and partial manual changes are reconciled. If set to `readonly`, those are errors. `go mod tidy` and (effectively) `go get` default to `mod`; all other commands default to `readonly`.

Go modules truly don’t get enough credit for how much simpler they are compared to the alternatives. In other ecosystems, package resolution time going down below 1s is celebrated (and is indeed an impressive technical achievement given the design’s requirements!). In Go, no one ever noticed package resolution happening, so there is nothing to celebrate.

For more ecosystem feature appreciation posts, follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo).

## The picture

I had a great time at [39c3](https://events.ccc.de/congress/2025/infos/startpage.html) during the holidays. The Chaos Communication Congress is a magical place with a very strict photo policy, so it’s pretty hard to convey its atmosphere. This is the best I could do without recognizable humans in the frame. *In Fairy Dust we trust!*

![The "Fairy Dust" rocket installation at the Chaos Communication Congress (39C3), showing a large black rocket sculpture with disco "rings" behind its tip emitting dramatic light beams in all directions. The main hall of the convention center surrounds it with banners including "CHAOS", "ALL CREATURES WELCOME", "OpenWrt", and "TRANS RIGHTS ARE HUMAN RIGHTS".](https://assets.buttondown.email/images/9dee32df-d645-4828-a59b-63c73524e3af.jpg)

My work is made possible by [Geomys](https://geomys.org), an organization of professional Go maintainers, which is funded by [Smallstep](https://smallstep.com/), [Ava Labs](https://www.avalabs.org/), [Teleport](https://goteleport.com/), [Tailscale](https://tailscale.com/), and [Sentry](https://sentry.io/). Through our retainer contracts, they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the [Geomys announcement](https://words.filippo.io/geomys).)
Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing. [Teleport Identity](https://goteleport.com/platform/identity/?utm=filippo) is designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We at [Ava Labs](https://www.avalabs.org), maintainer of [AvalancheGo](https://github.com/ava-labs/avalanchego) (the most widely used client for interacting with the [Avalanche Network](https://www.avax.network)), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.

---

1. I still think it’s important and it was the first thing I remember advocating for when I joined the Go team, because it makes the module cryptographically self-contained, and because the Go Checksum Database transparency story is not great in ephemeral environments like CI. These are security effects, though, not semantic ones. [↩](#fnref:default "Jump back to footnote 1 in the text")
2. These are the only dependencies you care about, even for security. If the main module imports `example.com/mod1/pkg1` and a separate `example.com/mod1/pkg2` imports `example.com/mod2`, there is no way for `example.com/mod2` to affect the build or run code on the developer’s machine, so you don’t need to consider it a dependency. This is actually very powerful, allowing libraries to segregate dependencies (e.g. the AWS SDK) in optional...