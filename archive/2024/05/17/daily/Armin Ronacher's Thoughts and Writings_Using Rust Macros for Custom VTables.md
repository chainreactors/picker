---
title: Using Rust Macros for Custom VTables
url: http://lucumr.pocoo.org/2024/5/16/macro-vtable-magic
source: Armin Ronacher's Thoughts and Writings
date: 2024-05-17
fetch_date: 2025-10-06T17:15:10.196671
---

# Using Rust Macros for Custom VTables

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Using Rust Macros for Custom VTables

written on May 16, 2024

Given that building programming languages and interpreters is the
developer’s most favorite hobby, I will never stop writing templating
engines. About three years ago I first wanted to see if I can make an
implementation of my [Jinja2 template engine](https://jinja.palletsprojects.com/) for Rust. It’s called [MiniJinja](https://github.com/mitsuhiko/minijinja/) and very close in behavior to
Jinja2. Close enought that I have seen people pick it up more than I
thought they would. For instance the Hugging Face [Text Generation
Inference uses it](https://github.com/huggingface/text-generation-inference/blob/d8402eaf6723818eec2d8abf7715b9dc42da07df/router/src/infer.rs)
for chat templates.

I wrote it primarily just to see how you would introduce dynamic things
into a language that doesn’t have much of a dynamic runtime. A few weeks
ago I released a major new version of the engine that has a very different
internal object model for values and in this post I want to share a bit
how it works, and what you can learn from it. At the heart of it is a
`type_erase!` macro originally contributed by Sergio Benitez. This post
goes into the need and usefulness of that macro.

## Runtime Values

To understand the problem you first need to understand that a template
engine like Jinja2 has requirements for runtime types that are a bit
different from how Rust likes to think about data. The runtime is
entirely dynamic and requires a form of garbage collection for those
values. In case of a simple templating engine like Jinja2 you can largely
get away with reference counting. The way this works in practice is that
MiniJinja has a type called [Value](https://docs.rs/minijinja/latest/minijinja/value/struct.Value.html)
which can be cloned to increment the refcount, and when it’s dropped the
refcount is decremented. The value is the basic type that can hold all
kinds of things (integers, strings, functions, sequences, etc.). In
MiniJinja you can thus do something like this:

```
use minijinja::Value;

// primitives
let int_val = Value::from(42);
let str_val = Value::from("Maximilian");
let bool_val = Value::from(true);

// complex objects
let vec_val = Value::from(vec![1, 2, 3]);

// reference counting
let vec_val2 = vec_val.clone();   // refcount = 2
drop(vec_val);                    // refcount = 1
drop(vec_val2);                   // refcount = 0 -> gone
```

Inside the engine these objects have all kinds of behaviors to make
templates like this work:

Cannot analyze code. No Pygments lexer found for “jinja2”.

```
.. sourcecode:: jinja2

    {{ int_val }}
        42
    {{ str_val|upper }}
        MAXIMILIAN
    {{ not bool_val }}
        false
    {{ vec_val }}
        [1, 2, 3]
    {{ vec_val|reverse }}
        [3, 2, 1]
```

Some of that functionality is also exposed via Rust APIs. So for instance
you can iterate over values if they contain sequences:

```
let vec_val = Value::from(vec![1, 2, 3]);
for value in vec_val.try_iter()? {
    println!("{} ({})", value, value.kind());
}
```

If you run this, this will print the following:

```
1 (number)
2 (number)
3 (number)
```

So each value in this object has itself been “boxed” in a value. As far
as the engine is concerned, everything is a value.

## Objects

But how do you get something interesting into these values that is not
just a basic type that could be hardcoded (such as a vector)? Imagine you
have a custom object that you want to efficently expose to the engine.
This is in fact even something the engine itself needs to do internally.
For instance Jinja has first class functions in the form of macros so it
needs to expose that into the engine as well. Additionally Rust functions
passed to the engine also need to be represented.

This is why a `Value` type can hold objects internally. These objects
also support downcasting:

```
// box a vector in a value
let value = Value::from_object(vec![1i32, 2, 3]);
println!("{} ({})", value, value.kind());

// downcast it back into a reference of the original object
let v: &Vec<i32> = value.downcast_object_ref().unwrap();
println!("{:?}", value);
```

In order to do this, MiniJinja provides a trait called [Object](https://docs.rs/minijinja/latest/minijinja/value/trait.Object.html)
which if a type implements can be boxed into a value. All the dynamic
operations of the value are forwarded into the internal `Object`. These
operations are the following:

* `repr()`: returns the “representation” of the object. The
  representation define is how the object is represented (serialized) and
  how it behaves. Valid representations are `Seq` (the object is a list or
  sequence), `Map` (the object is a struct or map), `Iterable` (the object
  can be iterated over but not indexed), `Plain` (the object is just a plain
  object, for instance used for functions)
* `get_value(key)`: looks up a key in the object
* `enumerate()`: returns the contents of the object if there are any

Additionally there is quite a few extra API (to render them to strings, to
make them callable etc.) but we can ignore this for now. In addition
there are a few more but some of them just have default implementations.
For instance the “length” of an object by default comes from the length of
the enumerator returned by `enumerate()`.

So how would one design a trait like this? For sake of keeping this post
brief let’s pretend there is only `repr`, `get_value` and `enumerate`.
Remember that we need to reference count, so we might be encouraged to
make a trait like the following:

```
pub trait Object: Debug + Send + Sync {
    fn repr(self: &Arc<Self>) -> ObjectRepr {
        ObjectRepr::Map
    }

    fn get_value(self: &Arc<Self>, key: &Value) -> Option<Value> {
        None
    }

    fn enumerate(self: &Arc<Self>) -> Enumerator {
        Enumerator::NonEnumerable
    }
}
```

This trait looks pretty appealing. The `self` receiver type is reference
counted (thanks to `&Arc<Self>`) and the interface is pretty minimal. [1](#fn-1)
`Enumerator` maybe needs a bit of explanation before we go further. In
Rust usually when you iterate over an object you have something called an
`Iterator`. Iterators usually borrow and you use traits to give the
iterator additional functionality. For instance a `DoubleEndedIterator`
can be reversed. In a template engine like Jinja we however need to do
everything dynamically **and** we also need to ensure that we do not end
up borrowing with lifetimes from the object. The engine needs to be able
to hold on to the iterator independent of the object that you iterate. To
simplify this process the engine uses this `Enumerator` type internally.
It looks a bit like the following:

```
#[non_exhaustive]
pub enum Enumerator {
    // object cannot be enumerated
    NonEnumerable,
    // object is empty
    Empty,
    // iterate over static strings
    Str(&'static [&'static str]),
    // iterate over an actual dynamic iterator
    Iter(Box<dyn Iterator<Item = Value> + Send + Sync>),
    // iterate by calling `get_value` in senquence from 0 to `usize`
    Seq(usize),
}
```

There are many more versions (for instance for `DoubleEndedIterators`
and a few more) but again, let’s keep it simple.

## Why Arc Receiver?

So why do you need an `&Arc<Self>` as receiver? Because in a lot of cases
you really need to bump your own refcount to do something useful. For
instance here is how the iteration of an object is implemented for
sequences:

```
fn try_iter(self: &Arc<Self>) -> Option<Box<dyn Iterator<Item = Value> + Send + Sync>>
where
    Self: 'static,
{
    match self.enumerate() {
        Enumerator::Seq(l) => {
            let self_clone = self.clone();
            Some(Box::new((0..l).map(move |idx| {
                self_clone.get_value(&Value::from(idx)).unwrap_or_default()
  ...