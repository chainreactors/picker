---
title: Your Node is Leaking Memory? setTimeout Could be the Reason
url: http://lucumr.pocoo.org/2024/6/5/node-timeout
source: Armin Ronacher's Thoughts and Writings
date: 2024-06-06
fetch_date: 2025-10-06T16:54:19.716426
---

# Your Node is Leaking Memory? setTimeout Could be the Reason

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Your Node is Leaking Memory? setTimeout Could be the Reason

written on June 05, 2024

This is mostly an FYI for node developers. The issue being discussed in
this post has caused [us](https://sentry.io)
[quite a bit of pain](https://github.com/getsentry/sentry-javascript/issues/12317).
It has to do with how node deals with timeouts. In short: you can
very easily create memory leaks [1](#fn-1) with the `setTimeout` API in node.
You’re probably familiar with that API since it’s one that browsers
provide for many, many years. The API is pretty straightforward: you
schedule a function to be called later, and you get a token back
that can be used to clear the timeout later. In short:

```
const token = setTimeout(() => {}, 100);
clearTimeout(token);
```

In the browser the token returned is just a `number`. If you do the same
thing in node however, the token ends up being an actual `Timeout` object:

```
> setTimeout(() => {})
Timeout {
  _idleTimeout: 1,
  _idlePrev: [TimersList],
  _idleNext: [TimersList],
  _idleStart: 4312,
  _onTimeout: [Function (anonymous)],
  _timerArgs: undefined,
  _repeat: null,
  _destroyed: false,
  [Symbol(refed)]: true,
  [Symbol(kHasPrimitive)]: false,
  [Symbol(asyncId)]: 78,
  [Symbol(triggerId)]: 6
}
```

This “leaks” out some of the internals of how the timeout is implemented
internally. For the last few years I think this has been just fine.
Typically you used this object primarily as a token similar to how you
would do that with a number. Might look something like this:

```
class MyThing {
  constructor() {
    this.timeout = setTimeout(() => { ... }, INTERVAL);
  }

  clearTimeout() {
    clearTimeout(this.timeout);
  }
}
```

For the lifetime of `MyThing`, even after `clearTimeout` has been called
or the timeout runs to completion, the object holds on to this timeout.
While on completion or cancellation, the timeout is marked as “destroyed”
in node terms and removed from it’s internal tracking. What however
happens is that this `Timeout` object is actually surviving until someone
overrides or deletes the `this.timeout` reference. That’s because the
actual `Timeout` object is held and not just some token. This further
means that the garbage collector won’t actually collect this thing at all
and everything that it references. This does not seem too bad as the
`Timeout` seems somewhat hefty, but not too hefty. The most problematic
part is most likely the `_onTimeout` member on it which might pull in a
closure, but it’s probably mostly okay in practice.

However the timeout object can act as a container for more state which is
not quite as obvious. Annew API that has been added over the last couple
of years called `AsyncLocalStorage` which is getting some traction is
attaching additional state onto all timeouts that fire. Async locals
storage is implemented in a way that timeouts (and promises and similar
constructs) carry forward hidden state until they run:

```
const { AsyncLocalStorage } = require('node:async_hooks');
const als = new AsyncLocalStorage();

let t;
als.run([...Array(10000)], () => {
  t = setTimeout(() => {
    //
    const theArray = als.getStore();
    assert(theArray.length === 10000);
  }, 100);
});

console.log(t);
```

When you run this, you will notice that the `Timeout` holds a reference to
this large array:

```
Timeout {
  _idleTimeout: 100,
  _idlePrev: [TimersList],
  _idleNext: [TimersList],
  _idleStart: 10,
  _onTimeout: [Function (anonymous)],
  _timerArgs: undefined,
  _repeat: null,
  _destroyed: false,
  [Symbol(refed)]: true,
  [Symbol(kHasPrimitive)]: false,
  [Symbol(asyncId)]: 2,
  [Symbol(triggerId)]: 1,
  [Symbol(kResourceStore)]: [Array] // reference to that large array is held here
}
```

That’s because every single async local storage that is created registers
itself with the timeout with a custom `Symbol(kResourceStore)` which even
remains on there after a timeout has been cleared or the timeout ran to
completion. This means that the more async local storage you use, the
more “stuff” you hold on if you don’t clear our the timeouts.

The fix seems obvious: rather than holding on to timeouts, hold on to the
underlying ID. That’s because you can convert a `Timeout` into a
primitive (with for instance the unary `+` operator). The primitive is
just a number like it would be in the browser which then can also be used
for clearing. Since a number holds no reference, this should resolve the
issue:

```
class MyThing {
  constructor() {
    // the + operator forces the timeout to be converted into a number
    this.timeout = +setTimeout(() => { ... }, INTERVAL);
  }

  clearTimeout() {
    // clearTimeout and other functions can resolve numbers back into
    // under internal timeout object
    clearTimeout(this.timeout);
  }
}
```

Except it doesn’t (today). In fact today doing this will cause an
unrecoverable memory leak because of a [bug in node](https://github.com/nodejs/node/issues/53335) [2](#fn-2). Once that will be
resolved however that should be a fine way to avoid problem.

Workaround for the leak with a Monkey-PatchSince the bug is only triggered when a timer manages to run to completion,
you could in theory forcefully clear the timeout or interval on completion
if node “allocated” a primitive ID for it like so:

```
const kHasPrimitive = Reflect
  .ownKeys(setInterval(() => {}))
  .find((x) => x.toString() === 'Symbol(kHasPrimitive)');

function invokeSafe(t, callable) {
  try {
    return callable();
  } finally {
    if (t[kHasPrimitive]) {
      clearTimeout(t);
    }
  }
}

const originalSetTimeout = global.setTimeout;
global.setTimeout = (callable, ...rest) => {
  const t = originalSetTimeout(() => invokeSafe(t, callable), ...rest);
  return t;
};

const originalSetInterval = global.setInterval;
global.setInterval = (callable, ...rest) => {
  const t = originalSetInterval(() => invokeSafe(t, callable), ...rest);
  return t;
};
```

This obviously makes a lot of assumptions about the internals of node, it
will slow down every timer slightly created via `setTimeout` and
`setInterval` but might help you in the interim if you do run into that
bug.

Until then the second best thing you can do for now is to just be very
aggressive in deleting these tokens manually the moment you no longer need
them:

```
class MyThing {
  constructor() {
    this.timeout = setTimeout(() => {
      this.timeout = null;
      ...
    }, INTERVAL);
  }

  clearTimeout() {
    if (this.timeout) {
      clearTimeout(this.timeout);
      this.timeout = null;
    }
  }
}
```

How problematic are timeouts? It’s hard for me to say, but there are a
lot of places where code holds on to timeouts and intervals in node for
longer than is healthy. If you are trying to make things such as hot code
reloading work, you are working with long lasting or recurring timeouts
it might be very easy to run into this problem. Due to how widespread
these timeouts are and the increased use of async local storage I can only
assume that this will become a more common issue people run into. It’s
also a bit devious because you might not even know that you use async
local storage as a user.

We’re not the first to run into issues like this. For instance Next.js is
trying to work around related issues by periodically patching `setTimeout`
and `setInterval` to [forcefully clearning out intervals](https://github.com/vercel/next.js/pull/57235) to avoid memory leakage
in the dev server. (Which unfortunately sometimes runs into the node bug
mentioned above due to it’s own use of `toPrimitive`)

How widespread is async local storage? It depends a bit on what you do.
For instance we (and probably all players in the observability space
including the OpenTelemetry project itself) use it to track tracing
information with the local flow of execution. Modern JavaSc...