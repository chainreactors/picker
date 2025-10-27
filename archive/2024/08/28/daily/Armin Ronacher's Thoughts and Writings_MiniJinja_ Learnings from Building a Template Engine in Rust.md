---
title: MiniJinja: Learnings from Building a Template Engine in Rust
url: http://lucumr.pocoo.org/2024/8/27/minijinja
source: Armin Ronacher's Thoughts and Writings
date: 2024-08-28
fetch_date: 2025-10-06T18:01:42.660511
---

# MiniJinja: Learnings from Building a Template Engine in Rust

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# MiniJinja: Learnings from Building a Template Engine in Rust

written on August 27, 2024

Given that I can’t stop creating template engines, I figured I might write
a bit about my learnings of creating [MiniJinja](https://github.com/mitsuhiko/minijinja/) which is an implementation of
my Jinja2 template engine for Rust. Disclaimer: this post might be a bit
more technical.

There is a good chance you have come across Jinja2 templates before as
they became quite common place in various places over the years. They
look a bit like this:

```
{% extends "layout.html" %}
{% block body %}
  <p>Hello {{ name }}!</p>
{% endblock %}
```

If you want to play around it yourself, here are some links:

* The [MiniJinja playground](https://mitsuhiko.github.io/minijinja-playground/)
  lets you play with a WASM compiled version of MiniJinja.
* The [API Documentation](https://docs.rs/minijinja/) documents all
  APIs, functionality and syntax.
* The [GitHub Project](https://github.com/mitsuhiko/minijinja/) for all
  the code including lots of examples.
* [minijinja](https://crates.io/crates/minijinja) and
  [minijinja-cli](https://crates.io/crates/minijinja-cli) on crates.io

## Why MiniJinja?

Maybe we start with the initial question of why I wrote MiniJinja. It’s
the year 2024 and people don’t create a ton of HTML with server side
rendered template engines any more. While there is some resurgence of
that model thanks to HTMX, hotwire and livewire, I personally use [SolidJS](https://www.solidjs.com/) for my internal UI needs. There is however
always a need to generate some form of text and so somehow Jinja2’s need
never really went away. When I originally created it, it was clearly
meant for generating HTML with some JavaScript sprinkled on top, but in
the years since I have encountered Jinja templates in many more places,
primarily for generating YAML and similar formats. Lately it comes up for
LLM prompt generation.

My personal need for MiniJinja came out of an experiment I built for
infrastructure automation. Since the templates had to be loaded
dynamically I could not use a system like Askama. Askama has type-safe
templates that just generate Rust code. On the other hand most Jinja
inspired template engines that are dynamic in Rust really do not try very
hard to be Jinja compatible. Because writing template engines is also fun,
I figured I might give it another try.

Over the last two years I kept adding to the engine until it got to the
point where it’s at almost feature parity with Jinja2 and quite enjoyable
to use.

## Runtime Values

When building a template engine for Rust you end up building a little
dynamic programming language that is optimized for text generation.
Consequently you pull in most of the challenges of building a dynamic
language. Particularly when working in Rust the immediate challenge is
memory management and exposing native Rust objects to the embedded
language. So the interesting bit here is how to create a system that
allows interactions between the template engine and the Rust world around
it.

MiniJinja, unlike Jinja2 does not use code generation but has a basic
stack based VM and a AST based bytecode compiler. Since MiniJinja follows
Jinja2 it inherits a lot of the realities of the underlying object system
that Jinja2 inherits from Python. For instance macros (functions) are
first class objects and they can have closures. This has challenges
because it’s easy to create cycles and Rust has no garbage collector that
can help with this problem.

The core object model in MiniJinja is a `Value` type which is represented
by an enum that looks as follows (some less important variants removed):

```
#[derive(Clone)]
pub struct Value(ValueRepr);

#[derive(Clone)]
pub(crate) enum ValueRepr {
    Undefined,
    None,
    Bool(bool),
    U64(u64),
    I64(i64),
    F64(f64),
    String(Arc<str>, StringType),
    SmallStr(SmallStr),
    Invalid(Arc<Error>),
    Object(DynObject),
}
```

Externaly everything is a `Value`. If you `Clone` it, you usually bump a
reference count or you make a cheap memcopy. Values are either primitives
such as strings, numbers etc. or objects.

For objects MiniJinja provides a tait called `Object` which can be
implemented by most Rust types. The engine provides a `DynObject` wrapper
is a fancy `Arc<dyn Object>` which supports borrowing and object safety.
[I wrote about this before](/2024/5/16/macro-vtable-magic/). What you
will notice is that quite a few of the types involved have an `Arc`.
That’s because these values are for the most part reference counted.
Since values here are really fat (they are 24 bytes in memory) a
`SmallStr` type is used to hold up to 22 bytes of string data inline. One
byte is used to encode the length of the string, and another byte is then
used by the `ValueRepr` to mark which enum variant is in use. In pure
theory this is all wrong. We never use weak references, so the weak count
in the `Arc` is not used and clever bit hackery could be used to greatly
reduce the size of the value type. I think one could get the whole thing
down to 16 bytes trivially or even 8 bytes with NaN tagging. However I
did not want to walk into the world of unsafe code more than feels
appropriate.

MiniJinjia is also [plenty fast](https://github.com/mitsuhiko/minijinja/tree/main/benchmarks).

One variant that is worth calling out is `Invalid`. That’s a value that
can exist in the system but it carries an error. When you’re trying to
interact with it in most cases it will propagate this error. That’s used
in the engine in places where the API assumes infallability (particularly
during iteration) but it needs a way to emit an error. This concept is
quite common when writing an engine in C though typically the actual error
is carried out of bounds. For instance in QuickJS there is a marker value
that indicates a failure, but the actual error is held on the interpreter
runtime.

The trait definition for objects looks like this:

```
pub trait Object: Debug + Send + Sync {
    fn repr(self: &Arc<Self>) -> ObjectRepr { ... }
    fn get_value(self: &Arc<Self>, key: &Value) -> Option<Value> { ... }
    fn enumerate(self: &Arc<Self>) -> Enumerator { ... }
    fn enumerator_len(self: &Arc<Self>) -> Option<usize> { ... }
    fn is_true(self: &Arc<Self>) -> bool { ... }
    fn call(
        self: &Arc<Self>,
        state: &State<'_, '_>,
        args: &[Value],
    ) -> Result<Value, Error> { ... }
    fn call_method(
        self: &Arc<Self>,
        state: &State<'_, '_>,
        method: &str,
        args: &[Value],
    ) -> Result<Value, Error> { ... }
    fn render(self: &Arc<Self>, f: &mut Formatter<'_>) -> Result
       where Self: Sized + 'static { ... }
}
```

Some of these methods are implemented automatically. For instance many of
the methods such as `is_true` or `enumerator_len` have a default
implementation that is based on object `repr` and the return value from
`enumerate`. But they can be overridden to change the default behavior or
to add some potential optimizations.

One of the most important types in Jinja is a map as it holds the template
context. They are implemented as you can imagine as `Object`. The
implementation is in fact pretty trivial:

```
impl<V> Object for BTreeMap<Value, V>
where
    V: Into<Value> + Clone + Send + Sync + fmt::Debug + 'static,
{
    fn get_value(self: &Arc<Self>, key: &Value) -> Option<Value> {
        self.get(key).cloned().map(|v| v.into())
    }

    fn enumerate(self: &Arc<Self>) -> Enumerator {
        self.mapped_enumerator(|this| Box::new(this.keys().cloned()))
    }
}
```

This reveals two interesting aspects of the object model: First that
`Value` implements `Hash`. That means any value can be used as the key in
a value. While this is untypical for Rust and even not what happens in
Python, it simplifie...