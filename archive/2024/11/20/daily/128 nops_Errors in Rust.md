---
title: Errors in Rust
url: https://carstein.github.io/rust/2024/11/19/errors-in-rust.html
source: 128 nops
date: 2024-11-20
fetch_date: 2025-10-06T19:17:47.913907
---

# Errors in Rust

|  |  |  |
| --- | --- | --- |
| Errors in Rust | Date | 19 Nov 2024 |
| Category | Rust |

Error handling is one of the more important parts of any programming language. The more interactions with other entities your program has the more of error handling you will have to deal with. In some languages the task is, well, very error prone. In C, when the function return certain value like for example 1 it is actually quite difficult to figure out if this value represent success or error - at least without looking at documentation. The posix standard is trying to introduce some uniformity but occasionally you will get a nasty surprise. Sometimes you might actually assume that the returned error is a valid value and cause some nasty bug. Or interesting vulnerability - but I guess that depends on where you sit.

There are many schools of handling this - some languages use exceptions. Other, like Go return value and error separately and it’s the user job to handle it correctly. The smart Go programmer always have a macro bound to one of the keys to immediately output `if err != nil` because this is the most commonly typed line in many go programs. This approach however has one main problem - developer can still ignore or forget the returned error and continue with the flow like nothing has happened.

Rust, like many functional languages (and, some might be surprised - the Google style of C++) is using something called monadic types to bind return value and the error into one type. In simple terms - many functions in Rust return a `Result<V, E>` - an `enum` that must be “unpacked” before a value can be used. The full definition of said `enum` looks like this:

```
enum Result<T, E> {
	Ok(T),
	Err(E)
}
```

First time you encounter a situation where you cannot simply use the value that the function just returned is quite a teachable moment. The Rust book initially give you just two tools to handle that situation - `.unwrap()` and `.expect()`. As the name suggest they simply unwrap the value out of the container and allow you to use it. The `.expect()` allows you additionally specify the error message that will be displayed upon hitting that particular function. You might ask where exactly this message will be displayed and it is time I mention one important characteristics of the aforementioned methods. They make every error irrecoverable. Upon the call your program will just terminate.

Program stopping every time you encounter a tiniest of error might not be ideal but actually in many situations this might be desirable. First of all - you might want to treat certain errors as the end of the road for the program. Also - when you just prototype some functionality you don’t want to be bothered with some complex error handling routines.

When you learn a bit more about the Rust you will realize that, given we are working with the `enum` we might just use `match` to get some more flexibility. Code below demonstrates this:

```
match function() {
  Ok(v) => // handle normal situation,
  Error(e) => // handle error
}
```

The `match` expression forcing us to actually handle all `enum` cases makes sure we handle all the errors we encounter. We can even be smarter about it - if a function returns different kinds of errors (like `File::open()`) we can treat all of them separately by adding more arms to the expression.

The most common situation in Rust happens when we want to assigned a returned value in case of success and return an error in case we have encountered one. We can express this in code like this:

```
let something = match function() {
  Ok(value) => value,
  Error(error) => return Error(error)
}
```

This situation is actually so common that rust developers have decided to save us all some time typing this elaborate match and you can just replace it with one character added at the end of the function call - `?`. I think this is the best invention since keyboard shortcuts. That also helps you just to propagate all kinds of Errors up the call stack so you can handle them all at the level where you feel comfortable.

So far we haven’t learned anything that is not already covered by the Rust book and you might be slowly losing your patience. Trust me - this lengthy introduction was needed.

The reality of programming is that very often you won’t care about one or the other arm when handling the `Result`. For example - you have a function that change the internal state of some object - there will be no value to return but you still need to handle the error - for logging if nothing else. This can be done by a following pattern:

```
if let Err(e) = some_call() {
  // log error
}
```

Of course a opposite situation is also possible - it is less common but we might want to handle the situation where we might want to ignore the error and just get the value.

```
if let Ok(v) = some_call() {
  // log success
}
```

Truth be told the `if let` constructs is much more commonly used when handling the `Option<T>` type.

Rust has not shortage of tools that we might want to use when dealing with errors - one I am commonly using is the `.map_err(|e| ... )` expression. Typically, when writing a program that touches many different aspects or domains you want to make the error handling fairly uniform. The system functions will often not obey - each one of them will return different set of errors - IO ones, Network ones etc. When calling those functions you might just want to map them to your own type for easier handling later on.

Another interesting way is to defer to closures - not always you want to handle the error by writing an explicit `match`. Sometimes a `.unwrap_or_else(|err| ...)` might be exactly what you will need to simply log and bail out. Or, even better, provide a default value in the absence of the real one.

The great thing about those functions operating on `Result` and returning yet another result is that you can chain them to achieve the desired result. One thing is for sure - whatever scenario you might come up with Rust has you [covered](https://doc.rust-lang.org/std/result/).

---

by [@carstein](https://twitter.com/%40carste1n)