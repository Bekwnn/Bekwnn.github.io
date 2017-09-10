---
layout: post
title: An Understated Value of Source Access
date: 2017-09-09 17:15:00 -0700
tags: [ue4, gamedev, api]
---
One of the biggest 'pros' of Unreal Engine 4 in my mind is source access to the engine.
I've cleared hurdles and problems which I otherwise wouldn't have thanks to the ability
to take a peek at the engine's code. For those of you who haven't worked with it,
UE4's C++ doesn't really resemble the C++ most people are familiar with after all the
macros and custom container types.

### AMyActor.h
```c++
UCLASS(Blueprintable)
class AMyActor : public AActor
{
    GENERATED_BODY()
public:
    AMyActor();
    
    UFUNCTION(BlueprintCallable, Category="Misc" /*etc*/)
    void SomeFunction();

    UPROPERTY(BlueprintReadWrite, Replicated, Transient /*etc*/)
    bool bDirtyFlag;
};
```

Just to give an example: classes deriving from Actor (base class of anything placed in the scene)
must start with 'A'. The code guidelines from epic say bools should start with 'b'. You can see both
in action above, but both are [Hungarian Notation.](https://en.wikipedia.org/wiki/Hungarian_notation)
I've seen people argue in the UE4 discord that hungarian notation is bad (and seeing some examples in
that wikipedia article, I'd agree), but I think the engine uses it tastefully.

Still, I learned about this term from working with UE4's code. A large part of the value of source access
is being exposed to new ideas. Even more veteran game developers who I've spoken to have learned things
and picked up techniques from being exposed to the engine's code base. After all, it's a 2 million line
code base created and maintained by some of the best developers in the field, and its used in a number
of massive titles.

Unreal Engine 4's code has been analyzed by [3rd parties](https://www.unrealengine.com/en-US/blog/how-pvs-studio-team-improved-unreal-engines-code)
and is generally considered high quality or "extremely high quality" (quote from the prior link)
for a project of its size.

Alongside the source code, you can reference the documentation and use those two to not only see the designs
used, but also to understand *why* they were used. Pages such as [Slate Architecture](https://docs.unrealengine.com/latest/INT/Programming/Slate/Architecture/index.html)
contain not just documentation, but breakdowns of different techniques and a discussion
of their pros and cons.

I got compelled to write this because a lot of the time when I see people talk about source access and how
it's valuable, they don't mention the value of being exposed to a large code base full of new designs and
techniques. Then again, maybe part of the reason for that is the level of quality present in UE4's code
base in particular. I don't think I've had as strong an experience in this way working with other tools
which have source access.

A non-UE4 example of this was working with [OpenGP](http://opengp.github.io/tutorial.html), which makes use of
a half-edge mesh data structure in order to traverse the mesh easily when writing algorithms. This notion is
also used in Blender and no doubt a number of other mesh editing software. Admitedly, I first learned about the data
structure while taking a course from OpenGP's creator, Andrea Tagliasacchi, but poking around the source of
OpenGP further cemented my understanding of it and some of the ways it can be used.

Here's a short list of some interesting nuggets either buried away in documentation or ideas present in the engine.
These are notions I've adopted and implemented when working on things outside of UE4.

* [Hungarian Notation (When Used Tastefully)](https://en.wikipedia.org/wiki/Hungarian_notation)
* [Slate Architecture - Motivation](https://docs.unrealengine.com/latest/INT/Programming/Slate/Architecture/index.html#motivation)
* [String Encoding - Pros and Cons of Formats](https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/StringHandling/CharacterEncoding/index.html#thecaseforbinary)
* [Abstraction of Pawns and Controllers](https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Controller/)
* [Game Mode and Game State Abstraction in Networked Play](https://docs.unrealengine.com/latest/INT/Gameplay/Framework/GameMode/)
