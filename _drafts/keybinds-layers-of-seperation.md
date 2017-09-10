---
layout: post
title: Keybinds - Layers of Separation
tags: [gamedev, code-design]
---
Doing keybinds properly is something I see a lot of developers skip over or put off
until much later when making a game. In this post I'll be explaining a framework
for handling keybinds which is flexible and just generally makes sense from an
object-based perspective.

Let's start with the type of keybinds everyone's probably familiar with:

## No Layers of Separation
```c#
//inside of an actor tick or update function:
if (Input.GetKeyDown(Key::Space))
{
    //jump, shoot, etc
}
```

This method runs into a few problems, but the most glaring problem with this method is
that it's impossible for the player to change their controls. So let's add 1 degree of
separation so that we can rebind controls later.

## 1 Degree of Separation
### Separating the Key and the Binding
```c#
//inside the Character class:
if (Input.GetButtonDown("Jump"))
{
    //jump
}
```

```c#
//inside the Input class:
bool GetButtonDown(string button)
{
    return GetKeyDown(bindingsMap[button]);
}
```

By storing a map of actions and their corresponding keybinds, we can change the keybinds
later without having to alter any gameplay code. You're probably familiar with this method
as well. Up until now has been review, so what I want to get into is a slightly more
complicated method, but with a whole lot more flexiblity.

## 2 Degrees of Separation
### Separating the Binding and the Action
```c#
//inside the Character class:
void BeginPlay()
{
    Input.BindAction("Jump", this, Jump);
}

void Jump()
{
    //jump
}
```

```c#
//inside the Input class:
void Tick()
{
    for (bind in actionBindings)
    {
        if (GetButtonDown(bind.button))
            bind.action();
    }
}
```
*(Note: code in these examples emphasizes simplicity and brevity over performance.)*

This 2nd degree of separation allows us to change the functionality of an action. Say your
character gets grabbed by an enemy and you have to mash the jump button to escape. You
could do something with `if` statements, but it would be much better if you could just
rebind the functionality of the jump action to some `BreakFree()` function.

In a game with contextual actions you're going to want to reassign the actions associated
with bindings. You can also achieve this with the [state pattern](http://gameprogrammingpatterns.com/state.html),
but the state pattern can be used in conjunction with this action binding system so that
you can use one or the other where appropriate.

With that said, let's stop briefly and look at our motivation: to be honest most games can
make do with 1 degree of separation and maybe the use of a state pattern. So Why all this work?
Well, this is code that you can use from game to game to game, so long as you're working in the
same language/engine. Even if you aren't, translating already written code is easy. The merit of
doing this extra work will show itself if you either work on a long project or work on multiple
shorter ones.

## 3 Degrees of Separation
### Separating the Binding and the Actor Who Performs the Action
```c#
//new Controller class:
public Pawn possessedPawn;

void Tick()
{
    //controller bindings
    for (bind in controllerBinds)
    {
        if (Input.GetButtonDown(bind.button))
            bind.action();
    }
    //if a pawn is possessed, call its actions
    if (possessedPawn)
    {
        for (bind in possessedPawn.bindings)
        {
            if (Input.GetButtonDown(bind.button))
                bind.action();
        }
    }
}
```

We've decentralized the bindings from a single list in the Input class to a list owned by
the controller and the pawn it possesses. This 3rd degree of separation allows us to bind
actions specific to the controller (pause menu, etc) and actions specific to an actor. But
mainly, it allows us to take our controller and have it freely possess different actors
with a `Pawn` component in a very clean way.

Furthermore, we can take this pattern and extend the notion of controller to represent
multiple physical players playing your game. Couch co-op would have 4 controllers in
the game scene, each capable of possessing different pawns. Imagine how easy it would be to
implement some kind of drop-in/drop-out feature like that? Or a game mechanic that involves
swapping characters?

UE4 even takes this pattern further by having "AIControllers" which can possess a pawn the
same way human controllers do. Player disconnected? Swap in an AIController to possess
their pawn.

It's a really strong pattern, but I see most people stop at 1 or 2 degrees of separation
and instead build states with the state pattern that are maybe a lot more complicated than
they need to be, and they could simplify them if they had access to an abstraction like this
one. Alternatively they might use some mechanism involving swapping behavior components per the
[strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern).

## An Important Note:

The examples shown here don't cover some of the challenges introduced by this abstraction.
Notably, what happens when multiple actions are queued up during one frame? The flow of the
program becomes more unpredictable. This example also doesn't cover the addition of CTRL,
SHIFT, and ALT as modifier keys, though adding some sort of bitmask enum to the binding for
those shouldn't be difficult.

One method to counteract this might be to associate a priority value with each binding and
sort the list by that priority value, allowing you to define which action bindings have a
higher or lower priority when a conflict between them arises. Then if both inputs are pressed
during the same frame, the higher priority action will execute first, and if need be, raise
a flag to disable the lower priority action when it attempts to execute afterwards.

Overall there are a lot of intricacies to input handling and it's a very finnicky business that
I don't plan to cover here. Our assumption in this case is that handling that stuff is the Input
class's job and making that class behave correctly is a different topic. If you're working with
a game engine or some kind of framework, this stuff is likely already done for you.

That's all I have to say on this subject for now. I do think that, generally speaking, implementing
something like this will save you time in the long run as you keep developing and wind up making
use of the features the different layers of abstraction provide. At the very least, hopefully there
are some ideas in here you can take and implement in your own games.
