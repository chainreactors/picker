---
title: Abolish Lock Poisoning
url: https://lucumr.pocoo.org/2026/11/25/poisoning/
source: Armin Ronacher's Thoughts and Writings
date: 2026-11-25
fetch_date: 2026-11-26T10:13:26.045692
---

# Abolish Lock Poisoning

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [talks](/talks/)* [about](/about/)

# Abolish Lock Poisoning

written on November 25, 2026

Rust has a curious feature that I don’t think the language would land today,
if it was not there for a long time: mutex poisoning. When some Rust code
panics while holding a `std::sync::Mutex`, the mutex is *poisoned*. That means
that any further call to `lock()` returns a `PoisonError`. The motivation for
this feature is that an object might have some internal invariants that need to
be upheld and panicking in the wrong moment might invalidate reasonable at and leave an
object behind in a broken state.

Personally I absolutely hate this feature as it has bitten me so many times and
I cannot once remember it helping me. The libs team is
[discussing](https://github.com/rust-lang/rust/issues/149359) making the
non-poisoning locks the default in the next edition but entirely expectedly it
has caused quite a few people to jump to the defence of the feature.

In this post I want to make my personal case why poisoned locks should either
be entirely removed or be made the exception.

Primarily this is because I have yet to come across code in the wild that
handles a poisoned lock correctly. On the other hand I have come across enough
code that mishandles it and as a result behaves worse than a
[parking\_lot](https://docs.rs/parking_lot) lock would which does not support
poisoning.

[Josh Triplett](https://news.ycombinator.com/item?id=46041342) put it quite
strongly in a hackernews comment: “In the entire history of the standard
library, we have never once seen a single report of anyone attempting to recover
from poison.”

When a panic happens with a lock held, there are two reasonable reactions: shut
the process down, or carry on and ignore the flag. With `panic = "abort"` you
get the former and poisoning never comes up. From all the evidence I have seen,
with unwinding, the idiomatic `lock().unwrap()` picks the worst option of all.

That’s because it neither stops the process nor lets it continue as it will turn
every further lock into a panic with sometimes disastrous effects. But that
is not the only issue with the system today. So here I want to share some of
the issues and with some references to real world code of how people got bitten.

## The Error Holds the Lock

One subtle aspect to the poisoning is that the `PoisonError` needs to hold the guard.
That’s because in order to ignore the poison flag, you need to fetch the guard
from the error object. Holding on to the error means holding on to the lock!

That can cause common code that does error wrapping / error conversions into a
deadlock hazard. The innocent looking `m.lock()?` in a function returning
`Box<dyn Error>` or similar keeps the mutex locked for as long as the error
lives ([#159930](https://github.com/rust-lang/rust/issues/159930)).

This can also happen with if let. For instance in
[cc-switch](https://github.com/farion1231/cc-switch/commit/43077f5539235f0255642ec9aab558d29f3f1b33)
you can see that they had a test hung because a `if let Ok(..) = lock() { .. } else { .. }` fallback locked the same mutex again while the unnamed
`PoisonError` from the condition still owned the guard.
[PC-AI](https://github.com/David-Martel/PC-AI/pull/273/changes) had the same bug
in a `match` arm. Another case can be found in
[ox-embed-server](https://github.com/anatolykoptev/ox-embed-server/issues/152).

## Panic To Outage

Deviously poisoning does not fail fast and done wrong, it fails forever. The
original panic happens once, on one thread, often somewhere unrelated from future
failures. Every later `lock().unwrap()` on that lock now however panics as
well, and because so much Rust code survives panics (thread pools, request
handlers, tokio tasks, FFI boundaries), the process stays up and becomes
useless:

* In RLS a failed cargo build panicked with `ENV_LOCK` held [which made any
  subsequent runs impossible](https://github.com/rust-lang/rls/pull/492).
* Mozilla’s
  [application-services](https://github.com/mozilla/application-services/issues/4661)
  saw `PoisonError` [rise to rank
  5](https://github.com/mozilla/application-services/issues/4658) in crash
  stats and [moved to
  parking\_lot](https://github.com/mozilla/application-services/pull/4663) after
  they concluded they did not benefit of poisoning handling.
* A [Neon safekeeper](https://github.com/neondatabase/neon/issues/2200) on
  staging failed every timeline lookup after a panic with a global lock held,
  and the original panic could not even be found in the logs.

While not live services, test suites show the same general issue. One failing
test poisons a shared static and every test after it fails with `PoisonError`.
This problem showed up for
[cargo](https://github.com/rust-lang/cargo/pull/12264),
[deno](https://github.com/denoland/deno/pull/6567),
[polars](https://github.com/pola-rs/polars/pull/26627) and
[rustc](https://github.com/rust-lang/rust/issues/43155#issuecomment-315535095)
itself.

## Attempt At Recovery

If you recover with `into_inner()`, the flag stays set and every later access
takes the recovery path again. And remember that for the first nine years of
Rust after the poisoning feature landed, you could not even clear it as
`clear_poison` arrived only in 1.77. Not clearing the flag means that potentially
expensive side effects will happen from that point onwards:

[goose-in-a-pond](https://github.com/jarida-io/goose-in-a-pond/commit/8c7e7fed06385d3dfd2958ba86ef0bb119d56688)
rebuilt its decoder state on every transcription after a single panic,
[librefang](https://github.com/librefang/librefang/commit/5edca0bfcf856324a6fc3701bf441d87ec7c9cca)
logged the same warning on every access, and a
[pool](https://github.com/anatolykoptev/ox-embed-server/issues/94) threw its
model away on every return.

## Nobody Relies on It, Not Even std

So who is handling poisonings? I’m really not sure, definitely not the standard library.
Every place where the standard library’s own code ignores it. Standard I/O has done so since [March
2015](https://github.com/rust-lang/rust/commit/2e8e8ab5648), two months before
1.0, because “any poison must have been the result of user code which the lock
isn’t protecting”. A common issue with a lot of poisoning errors that never
had anything to do with the mutex that was held.

Same with the [panic output
capture](https://github.com/rust-lang/rust/commit/72e96604c01), the [backtrace
lock](https://github.com/rust-lang/rust/commit/2d2c9e44939) and the [WASI
environment lock](https://github.com/rust-lang/rust/commit/9530ba0fe21). They
all do the same and unsurprisingly there is an [open
PR](https://github.com/rust-lang/rust/pull/148689) to move std’s internal
mutexes to `nonpoison`.

And I would argue the ecosystem has largely come to the same conclusion. Tokio’s own locks don’t poison.
Internally it wraps the std one in an [adapter that removes poison](https://github.com/tokio-rs/tokio/blob/master/tokio/src/loom/std/mutex.rs). When it landed Carl Lerche remarked “[I rather pretend lock poisoning isn’t a
thing](https://github.com/tokio-rs/tokio/pull/2814#discussion_r485760722).” In
one case Eliza Weisman [needed
`into_inner`](https://github.com/tokio-rs/tokio/pull/2828#discussion_r492350077)
to unlink a waiter during drop, or “we’ll leave the list with a potentially
dangling pointer”. I want to point to this in particular because this is a case where poisoning stood in the way of memory safety which is commonly argued as a reason you want poisoning.

Wasmtime, crossbeam-channel, tracing-subscriber always ignores lock poisoning.
rust-analyzer [switched to
parking\_lot](https://github.com/rust-lang/rust-analyzer/pull/1359) after
cancellation poisoned its solver like RLS did before. The parking\_lot maintainer
[described it](https://github.com/Amanieu/parking_lot/issues/324#issuecomment-1059616487)
as an anti-featu...