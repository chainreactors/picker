---
title: Abusing Go's infrastructure
url: https://reverse.put.as/2024/05/24/abusing-go-infrastructure/
source: Reverse Engineering
date: 2024-05-25
fetch_date: 2025-10-06T17:17:41.239881
---

# Abusing Go's infrastructure

[![](https://reverse.put.as/images/logo.png)](https://reverse.put.as/ "  (Alt + H)")

* [Home](https://reverse.put.as/ "Home")
* [About](https://reverse.put.as/about/ "About")
* [Archives](https://reverse.put.as/archives/ "Archives")
* [Crackmes](https://reverse.put.as/crackmes/ "Crackmes")
* [Patches](https://reverse.put.as/patches/ "Patches")
* [Tags](https://reverse.put.as/tags/ "Tags")
* [Papers](https://papers.put.as "Papers")

# Abusing Go's infrastructure

May 24, 2024 Â· 10 min Â· 1918 words Â· fG!

I apologize if this information is already known, but I couldn’t find any references about it and I wanted to understand what was going on and share with you because I think there is some value doing it.

In case this wasn’t known, I apologize to the Go team for not talking to them first and jumping the full disclosure gun (I don’t think it’s that severe). I really like Go! Thanks for all your great work.

### The problem[#](#the-problem)

Last night, I was exploring the contents of Go’s [checksum database](https://sum.golang.org), and I noticed a curious result:

```
sqlite> select path, count(path) from modules group by path order by count(path) desc;
github.com/homebrew/homebrew-core|39438
github.com/Homebrew/homebrew-core|30896
github.com/concourse/concourse|25372
github.com/openshift/release|24065
github.com/cilium/cilium|22138
```

The homebrew/Homebrew case divergence is explained by Go’s [documentation](https://go.dev/ref/mod#checksum-database) (thanks to Filippo Valsorda!):

> To avoid ambiguity when serving from case-insensitive file systems, the $module and $version elements are case-encoded by replacing every uppercase letter with an exclamation mark followed by the corresponding lower-case letter. This allows modules example.com/M and example.com/m to both be stored on disk, since the former is encoded as example.com/!m.

Anyway, this caught my attention because Homebrew is known to use Ruby, and so I went to check the [repository](https://github.com/homebrew/homebrew-core) contents.

GitHub language stats confirm it:

![language stats](/2024/05/24/abusing-go-infrastructure/images/language.png)

This result seems unexpected, since there are no traces of Go and there are more than 70,000 entries in Go’s checksum database. To be sure, I cloned the repository and tried to find any Go-related files such as `go.mod` or Go source files; however, nothing exists.

So I posted a tweet (technically a toot on Mastodon), got no reply and moved on.

While continuing to explore the database, I noticed another unusual case in `github.com/Edu4rdSHL/rust-headless-chrome`. It’s just a fork of [rust-headless-chrome](https://github.com/rust-headless-chrome/rust-headless-chrome), and there is nothing remarkable about the fork or the original except that they are both Rust repositories, and once again, no connection to Go.

Now my curiosity is piqued and the evil mode kicks in. It feels like arbitrary data can be pushed to the checksum database without a connection to Go. Why is the data being pushed? And how is it being pushed? I go to bed thinking about this, which is the most dangerous moment for security research. As I try to fall asleep, I come up with tons of ideas, but I’m usually too tired or lazy to take notes, and so, quite frequently, I can’t remember them in the morning. But this one wasn’t forgotten!

### Research[#](#research)

A new day and a curious mind demands answers. Why, how and, what if are the most dangerous questions in this field. If a Git repository has nothing to do with Go code, how does it appear in the Go checksum database?

From previous documentation readings, I knew that `proxy.golang.org` was the default modules proxy, and `sum.golang.org` for the checksum database. A couple of `ripgrep` searches in Go source code return nothing interesting, so it was time to read Go’s documentation, which is usually quite good.

Where to start? [Go Modules Reference](https://go.dev/ref/mod) was a great candidate and I finally found the answer to my question:

> If the go command consults the checksum database, then the first step is to retrieve the record data through the /lookup endpoint. If the module version is not yet recorded in the log, the checksum database will try to fetch it from the origin server before replying.

Okay, this was easy! If the module doesn’t exist in the checksum database (and proxy), it will be downloaded by the checksum and proxy infrastructure. One of my questions was: how did the checksum database retrieve the modules since they can be anywhere? I couldn’t find anything in the Go code that was responsible for that (which wouldn’t explain at all how Ruby and Rust code ended up in the database).

So, the next logical step is easy. Can I get the Go checksum server to download arbitrary data?

According to the [documentation](https://go.dev/ref/mod#checksum-database), the endpoint to try this is `$base/lookup/$module@$version`:

> Returns the log record number for the entry about $module at $version, followed by the data for the record (that is, the go.sum lines for $module at $version) and a signed, encoded tree description that contains the record.

First, let’s test it with a known record to see if and how it works:

```
$ curl https://sum.golang.org/lookup/github.com/homebrew/homebrew-core@v0.0.0-20240524162643-646fe2715a1c
26235981
github.com/homebrew/homebrew-core v0.0.0-20240524162643-646fe2715a1c h1:U32osaj3vZGypOtq7tsIHhZAYNOmiShiXJysIFGTqyM=
github.com/homebrew/homebrew-core v0.0.0-20240524162643-646fe2715a1c/go.mod h1:TM9a6pxWZJZZWuMzxESXhb6yaBaH9JAKDM4wpIzJsDE=

go.sum database tree
26238433
TQyXJYWJL6Z1OnKk5JXLAb9xfWrtHKjAUXKx5UQCa9Q=

â sum.golang.org Az3grm+I35+HBcG+YvxlX+nzkXah3cWlBac/4EytsG24bEHFLrJNvyz5SphrKAHSS0EeDKJXpnb3cvdUtqVSiaNLVAY=
```

Since the repository doesn’t seem to have any version tag the pseudo-version is used instead. Go [documentation](https://go.dev/ref/mod#pseudo-versions) explains the logic behind pseudo-versions.

The next step is to verify wheter a new Go module repository will be added to the checksum database and proxy if we call the `lookup` endpoint, as described.

After creating a simple new Go module and uploading to my GitHub account I have tried to issue the `lookup` command in two different forms, one not totally according to documentation, the other one also incorrect but trying to follow documentation. Both return errors, although different.

```
$ curl https://sum.golang.org/lookup/github.com/gdbinit/fluxmatter@latest
bad request: version "latest" is not canonical (wanted "")

$ curl https://sum.golang.org/lookup/github.com/gdbinit/fluxmatter@v0.0.0
not found: github.com/gdbinit/fluxmatter@v0.0.0: invalid version: unknown revision v0.0.0
```

The errors are kind of expected since I haven’t versioned the module and wasn’t using the correct pseudo-version. But we can verify if the new module was fetched as described by the documentation. The easiest way would be to generate the correct pseudo-version and make another query to the checksum database. If the module was indeed downloaded, then the entry would exist and returned as in the `homebrew-core` test.

Another way would be to resync my copy of the checksum database and query it for my module:

```
sqlite> select * from modules where path = 'github.com/gdbinit/fluxmatter';
github.com/gdbinit/fluxmatter|v0.0.0-20240524163826-a7e64ffd69f2|2024-05-24T16:40:51.203837Z
```

Finally we can query the proxy and use the `latest` query to return the latest known version of a module. And then download the module `zip` and prove that we just stored our arbitrary data in the Go infrastructure.

```
$ curl https://proxy.golang.org/github.com/gdbinit/fluxmatter/@latest
{"Version":"v0.0.0-20240524163826-a7e64ffd69f2","Time":"2024-05-24T16:38:26Z","Origin":{"VCS":"git","URL":"https://github.com/gdbinit/fluxmatter","Hash":"a7e64ffd69f2d0751a52736e832a8d77a21059e7"}}

$ curl -O https://proxy.golang.org/github.com/gdbinit/fl...