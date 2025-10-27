---
title: A Better Way to Borrow in Rust: Stack Tokens
url: http://lucumr.pocoo.org/2022/11/23/stack-tokens
source: Armin Ronacher's Thoughts and Writings
date: 2022-11-24
fetch_date: 2025-10-03T23:37:45.812028
---

# A Better Way to Borrow in Rust: Stack Tokens

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# A Better Way to Borrow in Rust: Stack Tokens

written on November 23, 2022

As a Rust programmer you are probably quite familiar with how references
work in Rust. If you have a value of type `T` you can generally get
various references to it by using the ampersand (`&`) operator on it. In
the most trivial case `&T` gives you just that: a reference to `T`. There
are however cases where you can get something else. For instance `String`
implements `Deref<Target=&str>` which lets you also get a `&str` from
it and that system also can be extended to work with mutable references as
well.

This dereferencing system also lets one work *through* another type. For
instance mutexes in Rust are pretty convenient as a result:

```
let value: Mutex<u32> = Mutex::new(0);

// acquire the mutex into a guard object
let guard = value.lock()?;

// this "derefs" the guard into &mut u32
*guard += 42;
```

There are however cases where this neat system does not work: in
particular you probably ran into this limitation with thread locals. You
would expect a thread local to work this way:

```
thread_local! {
    static value: RefCell<u32> = RefCell::new(0);
}

// borrow the cell and write into it.
*value.borrow_mut() += 42;
```

However unfortunately a thread local (called a `LocalKey`) does not
implement `Deref`. Instead you have to do this:

```
thread_local! {
    static value: RefCell<u32> = RefCell::new(0);
}

// borrow the cell and write into it.
value.with(|value| {
    *value.borrow_mut() += 42;
});
```

And it annoys me a lot. It’s annoying not only with thread locals but
also many other situations where you really would like to be able to deref
but it’s not possible. But why is that? And is there a better way?

## The Leakage Problem

I maintain a crate called [fragile](https://github.com/mitsuhiko/fragile). The purpose of this crate is
allow you to do something that Rust doesn’t want you to do: to send a
non `Send`-able type safely to other threads. That sounds like a terrible
idea, but there are legitimate reasons for doing this and there are
benefits to it.

There are lots of interfaces that through abstractions require that your
types are `Send` and `Sync` which means that it needs to be send-able to
another thread and self synchronized. In that case you are required to
provide a type that fulfills this purpose. But what if the type does not
actually cross a thread boundary or not in all cases?

A common use for this are errors. Most error interfaces require that
errors are `Send` and `Sync`. Yet sometimes auxiliary information that
you want to provide just doesn’t want to be this. My crates lets you put
a reference to that into your error anyways and you can at runtime safely
access the value for as long as you are on the same thread.

It accomplishes this in two ways with two different types:

* `Fragile` puts the value into type itself and lets you send a value into
  another thread and back. Crucially you need to send it back if your
  value has a destructor because if the value gets dropped on the wrong
  thread `fragile` will abort your process.
* `Sticky` is similar, but it puts the value into a thread local instead.
  For as long as you are on the same thread you can access your value just
  fine, on another thread it will error. Crucially though if the type
  gets dropped on the wrong thread it will temporarily leak until the
  originating thread shuts down and clears up the value. Not great, but
  quite useful for some cases.

For `Fragile` you can do this:

```
let val = Fragile::new(true);
assert_eq!(*val.get(), true);
```

This works, because the value is implicitly constrained by the lifetime of
the encapsulating object. However for `Sticky` an issue arises and it has
to do with intentional leakage. Rust permits any object to live for as
long as the process does by explicit leakage with the `Box::leak` API.
In that case you get a `'static` lifetime. Because `Sticky` does not
directly own the data it points to, this means that through that API you
can make the lifetime of the `Sticky` outlast the backing data which is in
the thread. This means that if `Sticky` had the same API as `Fragile` you
could create a crash in no time:

```
// establish a channel to send data from the thread back
let (tx, rx) = std::sync::mpsc::channel();

std::thread::spawn(move || {
    // this creates a sticky
    let sticky = Box::new(Sticky::new(Box::new(true)));

    // leaks it
    let static_sticky = Box::leak(sticky);

    // and sets the now &'static lifetime to the contained value back
    tx.send(static_sticky.get()).unwrap();
})
.join()
.unwrap();

// debug printing will crash, because the thread shut down and the
// reference points to invalid memory in the former thread's TLS
dbg!(rx.recv().unwrap());
```

This *obviously* is a problem and embarassingly that [was missed entirely
when the API was first created](https://github.com/mitsuhiko/fragile/issues/26).

This is the same reason why thread locals won’t let you deref something.
Because you could put something in there which gets leaked to `'static`
lifetime and then the thread comes in and cleans up.

## Lifetime Reduction

The reason `with()` gets around this is that it can guarantee that a
reference that it passes to the closure, cannot escape it. This works,
but it’s incredibly inconvenient. Here an [example from MiniJinja](https://github.com/mitsuhiko/minijinja/blob/202fc880df5d90bcbb3f8276a48bfa408ebc78c3/minijinja/src/key/mod.rs#L228)
about how annoying this API really can be:

```
pub(crate) fn with<R, F: FnOnce() -> R>(f: F) -> R {
    STRING_KEY_CACHE.with(|cache| {
        STRING_KEY_CACHE_DEPTH.with(|depth| {
            // do something here
            f()
        })
    })
}
```

This is quite a lot of rightward drift. I need two nested functions to
access two thread locals. Incidently I also create a similar API
frustration to my caller because internally I need to do work that needs
cleaning up.

Surely there must be a better way? And I believe there is. We should be
able to let the user “prove” that their lifetime is not `'static`. For
that we just need to create a utility vehicle that can never be `'static`
and then that non static reference can be passed to all functions to
entangle the lifetimes accordingly.

## Introducing Stack Tokens

The solution in `fragile` uses zero sized token objects on the stack to
accomplish this. A `StackToken` is a value that cannot be safely
constructed, it can only be created through a macro on the stack which
immediately takes a reference:

```
pub struct StackToken {
    _marker: std::marker::PhantomData<*const ()>,
}

impl StackToken {
    #[doc(hidden)]
    pub unsafe fn __private_new() -> StackToken {
        StackToken {
            _marker: std::marker::PhantomData,
        }
    }
}

#[macro_export]
macro_rules! stack_token {
    ($name:ident) => {
        #[allow(unsafe_code)]
        let $name = &unsafe { $crate::StackToken::__private_new() };
    };
}
```

The stack token itself is zero sized so it occupies no space. It also
is `!Send` and `!Sync`. That it’s `!Sync` is important. There are
two things that matter: one is that this type cannot be safely constructed.
The only way to get one is the `stack_token!` macro:

```
stack_token!(scope);
```

This will create basically a `let &scope = StackToken { ... }` on the
stack safely. From that point onwards any function that receives a
`&StackToken` can be assured that this has a lifetime that is never static
and constrained to a stack frame. The token expresses basically that the
thread lifes for at least as long as the lifetime of that borrow. Since threads
won’t randomly shut down and clean up the stack while code still references it,
this lets us create safe borrowing APIs like this:

```
pub fn get<'stack>(&'stack self, _proof: ...