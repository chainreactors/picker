---
title: Deser: Rethinking Rust Serialization
url: https://lucumr.pocoo.org/2026/9/29/deser/
source: Armin Ronacher's Thoughts and Writings
date: 2026-09-29
fetch_date: 2026-09-30T07:40:32.143478
---

# Deser: Rethinking Rust Serialization

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Deser: Rethinking Rust Serialization

written on September 29, 2026

[Serde](https://serde.rs/) is an amazing serialization library for Rust and it
has been a huge reason why I felt productive with it for years. However already
while at Sentry I got quite frustrated with some of the limitations with it but
actually replacing Serde is tricky because of the might that it has in the
ecosystem. Also because it’s quite hard to actually do better without also
making some potentially painful compromises.

Here are three examples of Serde corner cases that show poor interactions of
Serde features or unexpected limitations:

A number that is a map

An internally tagged enum, with `serde_json`‘s `arbitrary_precision` feature
turned on:

```
#[derive(Deserialize)]
#[serde(tag = "type")]
enum Shape {
    Circle { radius: f64 },
}

serde_json::from_str::<Shape>(r#"{"type": "Circle", "radius": 1.5}"#)
// error: invalid type: map, expected f64
```

Serde’s data model has no place for arbitrary precision numbers, so `serde_json`
uses in-band signalling with a map with a magic key. The enum has to buffer the
fields until it has seen the tag, and the buffer does not know about the magic
key. Because Cargo features are unified, it’s enough for any crate in your
dependency graph to turn the feature on.

Flattening breaks integer keys

```
#[derive(Deserialize)]
struct Stats {
    scores: HashMap<u32, u32>,
}

#[derive(Deserialize)]
struct Report {
    name: String,
    #[serde(flatten)]
    stats: Stats,
}

serde_json::from_str::<Report>(r#"{"name": "x", "scores": {"42": 23}}"#)
// error: invalid type: string "42", expected u32 at line 1 column 35
```

`Stats` on its own parses `{"scores": {"42": 23}}` just fine. JSON keys are
always strings, and `serde_json` only turns them into integers if the type asks
for one. However once `flatten` buffers the value, `"42"` is just a string.
The error also points at the end of the document rather than at the key.

Adapters do not compose

```
fn from_hex<'de, D: Deserializer<'de>>(d: D) -> Result<u32, D::Error> { ... }

#[derive(Deserialize)]
struct Theme {
    #[serde(deserialize_with = "from_hex")]
    primary: u32,
    #[serde(deserialize_with = "from_hex")]
    accent: Option<u32>,
}

//error[E0308]: `?` operator has incompatible types
//  |
//  |     #[serde(deserialize_with = "from_hex")]
//  |                                ^^^^^^^^^^ expected `Option<u32>`, found `u32`
//  |
//help: try wrapping the expression in `Some`
//  |
//  |     #[serde(deserialize_with = Some("from_hex"))]
//  |                                +++++          +
```

A function cannot be passed as a type parameter, so there is no way to apply
`from_hex` to the inside of an `Option`, a `Vec` or a map. You write another
function for every wrapper, and once you have `from_opt_hex` the field is no
longer optional unless you also remember to add `#[serde(default)]`.

None of these are bugs that are easy to fix in Serde. They fall out of its
design, and that design is protected by Serde’s stability guarantees.

Back in 2022 I started an experiment called
[Deser](https://github.com/mitsuhiko/deser). It’s a serialization library for
Rust that takes the user experience of [Serde](https://serde.rs/) and puts it on
top of a completely different architecture inspired by
[miniserde](https://github.com/dtolnay/miniserde). I never really finished it
and it sat around for a few years. I picked it back up, and it has now reached
a point where I think it’s worth looking at. Even just to inspire others to
see if they want to explore the space.

## The Name And Idea

The name is Serde with its two halves swapped. Deser is Serde but the other way
around. In Serde, a type drives the deserialization process: a `Deserialize`
impl asks the deserializer for the kind of value it expects, the format calls
back into a visitor. Every nested value is handled by recursion which makes
Serde deserialization inherently grow the stack with each level of nesting.

Deser on the other hand turns this around and the format tells the type of the
next value and pushes events into a sink. When a sink hits the start of a
nested value, it doesn’t call into it but hands back a new sink to a driver,
which keeps all state on the heap (in fact, in an arena). On the way out,
emitters return their nested values instead of recursing into them.

That also means that Deser cannot support formats like protobuf that are not
self describing. They are in fact quite intentionally left out of the design
entirely. Which is one way to say: if you want to “fix” Serde, you need to
make some other compromises.

Most of the reasons for Deser’s ideas go back to [Sentry
Relay](https://github.com/getsentry/relay), which processes enormous amounts of
untrusted JSON. Over the years when I was at Sentry we ran into the same set of
problems again and again, and many of them are not really bugs in Serde but
consequences of its design. Serde’s stability guarantees mean that a lot of
them cannot be fixed without breaking every format and every hand written
implementation. Most of these problems come from three decisions:

1. **One set of traits for all formats.** Serde serves both self describing
   formats (JSON, YAML, TOML, …) and formats where the reader has to know the
   type upfront (postcard, bincode, protobuf, …). That is incredibly useful,
   but it means that some features only work with some formats, and you find out
   at runtime. In case of Serde it also has some odd wrinkles where a derived
   struct quietly accepts an array in place of an object in JSON for instance.
2. **A fixed data model that loses information when buffering.** Internally
   tagged enums, untagged enums and `flatten` need to buffer values before
   they know what to do with them. The buffer can’t hold everything the format
   knew, errors lose their location and extensions to the ecosystem rely on
   in-band signalling to express things such as arbitrary precision numbers.
3. **Recursion on the call stack.** Every level of nesting uses stack space.
   Formats protect against this with a recursion limit, but the moment you go
   through a code path that doesn’t have one (writing, dynamic values), deeply
   nested data can take down your process. It also means that a
   deserialization cannot be paused while you wait for more input.

Many of the corresponding Serde issues have been open for years, and I wrote
about [abusing Serde](/2021/11/14/abusing-serde/) before. People have tried
different angles on this over the years. Some went minimal and dropped most
features to get fast compiles and no recursion. dtolnay’s own
[miniserde](https://github.com/dtolnay/miniserde) is the best example of that,
and deser’s trait design was originally modelled after it. Other recent
attempts went for runtime reflection, or for a new data model with a focus on
binary formats.

If you want to read up on all of the collected challenges with Serde’s design,
I maintain [a lengthy list here](https://github.com/mitsuhiko/deser/blob/main/SERDE.md).

## Dethroning Serde

First of all I don’t think it’s likely that one can replace Serde. [The orphan
rule](https://smallcultfollowing.com/babysteps/blog/2022/04/17/coherence-and-crate-level-where-clauses/)
entrenches Serde incredibly well in the ecosystem. But some things are within
the reach of a crate author’s control. In case of Deser it’s completeness.

Deser today implements all important self describing formats from YAML, JSON,
TOML, CBOR, JSON5 and the likes, but also XML and plist to really close the gap.
XML in particular is something Serde has declined to support, and it shows
(more on that below). At the very least format support should not be the
reason not to use Deser.

The second problem usually is that actually solving Serde’s issues comes a...