---
title: Why I hate ModelForm & ModelSerializer
url: https://0xda.de/blog/2024/02/why-i-hate-modelform-modelserializer/
source: Blogs on dade
date: 2024-02-24
fetch_date: 2025-10-04T12:06:03.919468
---

# Why I hate ModelForm & ModelSerializer

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/02/why-i-hate-modelform-modelserializer/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

8 minutes

# [Why I hate ModelForm & ModelSerializer](https://0xda.de/blog/2024/02/why-i-hate-modelform-modelserializer/)

---

* [Footgun No. 1: fields vs exclude](#footgun-no-1-fields-vs-exclude)
  + [Example](#example)
* [Footgun No. 2: \_\_all\_\_](#footgun-no-2-__all__)
* [Footgun No. 3: depth](#footgun-no-3-depth)
* [Models should always be internal.](#models-should-always-be-internal)
* [Paving the Road](#paving-the-road)

---

I’ve been having a lot of conversations recently about Django `ModelForm` and Django Rest Framework (DRF) `ModelSerializer`, and to a lesser extent, DRF `ModelViewSet`. I think, perhaps maybe a little too zealously, that they are bad patterns and have no place in any reasonably large software project.

Now, I absolutely understand the appeal of them. It makes it much easier to write code quickly, and lots of times, our views are pretty tightly coupled to individual models in our database. If you’re in the know, you see one of these and think “wow, that’s so efficient”. You’re like “Yeah I can crank out this feature in like 30 minutes because it’s just a model and a form, easy peasy.” Long live developer productivity.

But if you’re not in the know, then you see one of these and think “How in the hell does this work?” and then you end up spending a bunch of time reading various docs, inspecting the parent classes to find out where the ✨ magic ✨ happens. Eventually, you’ll probably figure it out long enough to understand how to change the thing you need to change, and then you’ll be on your way. Don’t worry, you won’t forget how any of the magic happens by the next time you need to modify this code, right? RIGHT?

But the Zen of Python is that explicit is better than implicit, and I think these *technically*-explicit, tightly coupled tools introduce more problems in your code base than they are worth, and it’s easier to not use them at all than it is to make sure everyone is using them safely.

## Footgun No. 1: fields vs exclude

In both `ModelForm` and `ModelSerializer`, you are given the option to define `fields` or `exclude`. If you define `fields`, it’s an explicit list of the model fields that you want to expose in the form/serializer. This isn’t where the problem lies. On the flip side, if you define `exclude`, it’s an explicit list of model fields that you don’t want included, everything else gets included by default. But, perhaps most important, `ModelForm` doesn’t enforce that one of these values be set – the **default** behavior is to expose the entire model. `ModelSerializer`, at least, has made a change to make `fields` or `exclude` mandatory, they removed the implicit default of all fields on the model.

In the short term, you write a new model and you write a form to submit or edit data on that model. You don’t declare all the fields, because you know the fields on the model and they are exactly what has to be returned to the browser. You get the feature out the door and move on. Or *maybe* you think you’re getting ahead of the problem by adding `exclude = ['id']` because you know you don’t want to ship the internal database ID to the browser.

But the problem happens later, maybe months or years later, when another developer is tasked with modifying the model to include more information. Information that is meant for internal use. They update the model and hook up this new information to whatever they are using. But unless they explicitly know about the patterns in use and the complete context of everything using that model, they aren’t likely to realize that their new fields are automatically, implicitly included. They don’t know they need to make sure to exclude it from every `ModelForm` or `ModelSerializer` that might reference this model.

### Example

Let’s say we have a User model in our application, it represents a user that signs in to our application. An overly simplified, extremely insecure version of this might look like this:

```
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
```

Now you need to make your sign up page, so you reach for the Django-provided mechanism to do so. The `ModelForm`. You’ll even make a separate form to allow the user to change their email address.

```
class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User

class UserChangeEmailForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ["password"] # it's not secure to show people their password when they want to change their email
```

Two years later, you get harassed by your security-conscious users for not offering two-factor authentication. Your business is booming and you’ve moved on, but your new developer is going to add 2FA support for your customers.

```
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    totp_seed = models.CharField(max_length=255)
```

This simple change to just the Model file has unexpected repercussions elsewhere in the system, because the `UserChangeEmailForm` will now automatically include the `totp_seed` value when it is rendered.

This problem is explicitly called out in the Django documentation, “[Selecting the fields to use](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#selecting-the-fields-to-use)”. It “strongly recommends” explicitly setting all fields using the `fields` attribute, and it acknowledges there are potential security problems with not doing so. But even then, this same section of documentation goes on to tell you about a special value made specifically to include all fields, just in case you want explicit.

## Footgun No. 2: \_\_all\_\_

In case you’re told that you need to include `fields` in your `ModelForm` or `ModelSerializer`, but you insist that you want the whole model included in the form, Django has you covered. Simply use `fields = "__all__"`. Now your form will automatically include the whole model. Easy to write, easy to ship your feature today.

This footgun doesn’t need much more coverage. It’s bad for the same reason not including a `fields` value is bad, and bad for the same reason only using `exclude` is bad.

## Footgun No. 3: depth

This footgun is unique to DRF’s `ModelSerializer`. No good deed goes unpunished, I suppose. They removed the implicit behavior of not defining fields, but they also offer a way to automatically serialize relationships. Again, a very handy feature that enables developers to quickly write functional code. But consider the following scenario:

We’re working on a new book review feature, which allows people to submit reviews for books, and then displays information about the reviews and the book. A simplified example of this follows.

```
class Book(models.Model):
    author_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class BookReview(models.Model):
    review_body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['id', 'review_body', 'book']
        depth = 1
```

This works great. As our site gains popularity, authors are reaching out to us and they want to get reviews automatically emailed to them in a daily digest. Thinking of the ways we can...