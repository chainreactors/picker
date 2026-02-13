---
title: Inspecting the Source of Go Modules
url: https://words.filippo.io/go-source/
source: Filippo Valsorda
date: 2026-02-12
fetch_date: 2026-02-13T04:16:46.441028
---

# Inspecting the Source of Go Modules

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

12 Feb 2026

# Inspecting the Source of Go Modules

Go has indisputably the best package integrity story of any programming language ecosystem. The [Go Checksum Database](https://golang.org/design/25530-sumdb) guarantees that every Go client in the world is using the same source for a given Go module and version, forever.

It works despite the decentralized nature of Go modules, which can be fetched directly from their origin based on the import path. (For example, you can fetch v1.2.3 of `github.com/example/mod` by cloning the git repository and exporting the v1.2.3 tag. `GOPROXY=direct` forces this.[1](#fn:direct))

The Checksum Database stores the cryptographic hash of a module version the first time it is used across the ecosystem, and then provides that same checksum to every Go client going forward. If e.g. a git tag were force-pushed or a code host were to try to serve targeted versions to some clients, the `go` tool would notice the mismatch and fail the fetch.

This is vastly more practical than requiring module authors to manage keys, but provides comparable security, because the author themselves can verify the checksum in the Checksum Database matches the one they developed. Moreover, the Checksum Database is a [transparency log](https://research.swtch.com/tlog), which prevents even the database operator (i.e. Google) from falsifying or hiding entries.

However, any time we **read code directly from the code host** we introduce a weak link in this chain. For example, there is no guarantee that the code displayed at `https://github.com/example/mod/blob/v1.2.3/exp.go` is the actual contents of `exp.go` from v1.2.3 of module `github.com/example/mod`: GitHub allows force-pushing git tags and even built its recommended GitHub Actions workflows on top of mutable tags.

Last year this was taken advantage of to make a classic [typosquatting](https://en.wikipedia.org/wiki/Typosquatting) attack harder to identify. [A fake BoltDB module was published with malicious code](https://www.heise.de/en/news/Typosquatting-in-the-Go-ecosystem-Fake-BoltDB-package-discovered-10270367.html), and then innocent code was force-pushed to GitHub. Some commenters described this as exploiting the Go Modules Mirror’s cache, but it is better understood as exploiting the natural lack of verification in the GitHub web interface, which doesn’t show the authentic (and in this case malicious) source of a module version, as used by actual Go tooling.

The solution when reviewing modules locally is to use a command like

```
cd $(go mod download -json filippo.io/age@v1.3.1 | jq -r .Dir)
```

to fetch the correct source.[2](#fn:agent) We are also [working on a `go mod verify -tag` command](https://github.com/golang/go/issues/68669#issuecomment-2755906892) to verify the contents of a local git repository against the Go Checksum Database, which can also be used by module authors to check that the contents of the Checksum Database are correct.

However, pkg.go.dev still links to unverified code hosts, and clicking on pkg.go.dev source links is very convenient.

Russ Cox made a simple service to view the source of a Go module at [go-mod-viewer.appspot.com](https://go-mod-viewer.appspot.com/).

[pkg.geomys.dev](https://pkg.geomys.dev) is a new similar service with optional syntax highlighting, line and [line range linking](https://pkg.geomys.dev/filippo.io/age%40v1.3.1/tag/tag.go#L105-L109), multiple fonts, automatic dark mode, and a [file tree](https://pkg.geomys.dev/filippo.io/age%40v1.3.1) and [module versions](https://pkg.geomys.dev/filippo.io/age) browser.

You can use it manually by replacing `go.dev` with `geomys.dev` in any pkg.go.dev URL, or you can install the companion browser extension for Chrome and Firefox, which replaces links to code hosts in pkg.go.dev pages with links to pkg.geomys.dev.

[![Available in the Chrome Web Store](https://pkg.geomys.dev/assets/chrome-web-store-badge.png)](https://chromewebstore.google.com/detail/pkggeomysdev-source-links/kehcbeihpiighnghampfaiapahlbjlgl)
[![Get the Add-on for Firefox](https://pkg.geomys.dev/assets/firefox-addon-badge.svg)](https://addons.mozilla.org/en-US/firefox/addon/geomys-source-links/)

The service works by making [HTTP Range requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Range_requests) directly to the module version’s zip file, and decompressing the file in the browser, without having to fetch the whole archive. Once [proxy.golang.org fixes their CORS configuration](https://github.com/golang/go/issues/77496) it will work without any Geomys backend.

Currently, it trusts the Google Modules Proxy to serve the correct zip files, without checking the transparency log proof. I plan to implement optional proof checking once proxy.golang.org CORS is fixed, including [third-party gossip](https://sourcespotter.com/sumdb/). Unfortunately, checking the proof does require fetching the whole module version’s zip archive to compute the dirhash, which is included in the Checksum Database (and in go.sum).

For updates, follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo).

## The picture

I recently went to Paris and found the Tour Eiffel elevator to be more fascinating than the tower itself. Whatever that says about me.

![A shot of the Tour Eiffel from the inside, looking up. A web of metal with the yellow elevator and its rails in the middle.](https://assets.buttondown.email/images/0c2a763b-ba3a-4d2c-8ecf-263871d7b4b6.jpeg?w=960&fit=max)

My work is made possible by [Geomys](https://geomys.org), an organization of professional Go maintainers, which is funded by [Ava Labs](https://www.avalabs.org/), [Teleport](https://goteleport.com/), [Tailscale](https://tailscale.com/), and [Sentry](https://sentry.io/). Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the [Geomys announcement](https://words.filippo.io/geomys).)
Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing. [Teleport Identity](https://goteleport.com/platform/identity/?utm=filippo) is designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We at [Ava Labs](https://www.avalabs.org), maintainer of [AvalancheGo](https://github.com/ava-labs/avalanchego) (the most widely used client for interacting with the [Avalanche Network](https://www.avax.network)), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.

---

1. I generally recommend against `GOPROXY=direct` and actually configure `GOPROXY=proxy.golang.org` to remove the direct fallback and reduce the attack surface of running git clone on potentially adversarial repositories. That’s besides the point of this article, though: whether you fetch direct or through a proxy, you will still always get the same contents authenticated by the sumdb (or an error). [↩](#fnref:direct "Jump back to footnote 1 in the text")
2. If you use a code agent, you can add the following line to your AGENTS.md or CLAUDE.md:
   `` To see source files from a dependency, or to answer questions about a dependency, run `go mod download -json MO...