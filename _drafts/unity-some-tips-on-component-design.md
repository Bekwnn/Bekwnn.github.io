---
layout: post
title: Unity - Some Tips on Components
tags: [unity, gamedev, code-design]
---
This post was prompted by an online argument I saw over the best way to default values for
game object components in Unity. One side argued to use the `Awake()` function (occurs during
runtime the first time the object is loaded) while the other side argued to simply assign values
through the inspector. Both had valid points:

## Tip #1: Default Values

#### Arguments for Awake():
* You shouldn't rely on (relatively) unreliable scene data to assign components.
* Assigning programmatically allows you to perform other checks and ensure components
are properly set every time.
* Manually assigning values for multiple components across multiple objects via the inspector
is tedious.

#### Arguments for Inspector:
* Assigning in code isn't accessible to artists and designers (`Awake()` will override
inspector-assigned values).
* Using Awake() potentially increases load/initialization times.
* May change values on a per-instance basis.

Yet despite these valid points, both are less than ideal methods. `Reset()` is defined in the
[Unity documentation](https://docs.unity3d.com/ScriptReference/MonoBehaviour.Reset.html) as:

> ### Description
>
> Reset to default values.
>
> Reset is called when the user hits the Reset button in the Inspector's context menu or when adding 
the component the first time. This function is only called in editor mode. Reset is most commonly 
used to give good default values in the inspector.

The documentation even mentions default values. *Twice.* This allows you to programmatically set values
when components are created, occurs during edit time, and allows artists and designers to replace the
default values with their own if they choose to do so. `Reset()` has all the positives
listed in the above arguments and none of the negatives.

```c#
class RollingForce : MonoBehaviour
{
    public Rigidbody rBody;

    void Reset()
    {
        rBody = GetComponent<Rigidbody>();
    }
}
```

Anytime we add `RollingForce` to an object, it will automatically try to fetch and assign a reference to
that object's Rigidbody. The `Reset()` function can also be called any time by clicking "Reset" from the
gear-shaped icon which has a drop-down of a component options.

## Tip #2: Component Dependencies

That's one piece of advice. But what if we *always* want a Rigidbody component in addition to a RollingForce
component, no exceptions? Furthermore if we had an object which always wanted 3 or more other components, it
would be a pain to set them up every time, even with the use of `Reset()`. We have a component which depends
on others to function.

That's where `[RequireComponent()]` comes in:
```c#
[RequireComponent(typeof(Rigidbody))]
class RollingForce : MonoBehaviour
{
    public Rigidbody rBody;

    void Reset()
    {
        rBody = GetComponent<Rigidbody>();
    }
}
```

Now when RollingForce is added to an object, it will not only try to fetch a Rigidbody reference from that
object, but if the object does not have a Rigidbody component, one will be automatically added before `Reset()`
runs and so it will get assigned by `Reset()`. Additionally, Unity will prevent you from removing the Rigidbody
before removing all components which require it.

I'd only recommend using this when one component is truly dependent on another, but if you have for example some
`Hero` class which you always want to have `Movement`, `Health`, `Attack`, and `Magic` components, you can make
them required by the `Hero` component and perform assignments with `Reset()` to save yourself some headaches caused
by inconsistencies that can often happen when assigning values in the inspector. Especially if you have a couch co-op
game with upward of 4 Heroes per scene.

## Tip #3: An Outward Interface

This brings us to something that's not so much an engine feature, but more a stylistic preference of mine which I'm
going to make an argument for: using a singular component as an object's interface.

In the case of other game engines, this is where and how I'd typically use inheritance. See, some objects are totally
content to be a faceless bundle of components: a moving or spinning piece of level geometry, a door—simple stuff with
2-3 components. In reality though, you usually have objects which are of a special type. It can be a hero, a hazard,
or a projectile. You usually come across these cases when you have a collision event which something like

```c#
Hero otherHero = other.GetComponent<Hero>();
if (otherHero)
{
    //logic
}
```

The idea is to create one class which acts as an "umbrella" for all the components it has. There's probably going to
be a fair bit of logic specifically targetting objects which are heroes. By creating one class which acts as both an
identifier and a way to access its various sub components, you can change a spell effect from this:

```c#
//spell effect deals 120 damage and slows and
//reduces spell power by 30% for 2 seconds
Movement otherMove = other.GetComponent<Movement>();
if (otherMove)
{
    otherMove.MoveSpeedMod(-0.3f, 2f);
}
Health otherHealth = other.GetComponent<Health>();
if (otherHealth)
{
    otherHealth.Damage(120);
}
Magic otherMagic = other.GetComponent<Magic>();
if (otherMagic)
{
    otherMagic.SpellPowerMod(-0.3f, 2f);
}
```

To this:

```c#
Hero otherHero = other.GetComponent<Hero>();
if (otherHero)
{
    otherHero.move.MoveSpeedMod(-0.3f, 2f);
    otherHero.health.Damage(120);
    otherHero.magic.SpellPowerMod(-0.3f, 2f);
}
//Assuming Hero requires those components,
//otherwise we may want to null check them.
```

Both the above could be shortened with C# 6's `?.` operator when Unity upgrades to that version of C#, such as
`other.GetComponent<Hero>()?.health?.Damage(120);` Either way, the first version has to fetch three components while the
second only fetches one.

The point is, whether you're using components or inheritance, you want to keep the class relatively light on
functionality, and mainly use it as an interface to the bundle of components hiding behind it. With the assistance
of some helper functions in `Hero`, you can access your components easier. Most significantly, by having one
main access point to all the components on your Hero game object, you create a situation with lower coupling and
higher cohesion. Outside objects need to know about fewer components and you can rearrange things internally within
the hero object by changing the interface of the `Hero` class.

Of course, other designs can achieve similar effects and I'm not suggesting this to be some sort of 'best practice'.
There are very few cases in programming where 'one size fits all'. But if you've had trouble before with managing
complex objects with many components, maybe consider this as an approach.

Lastly, when it comes to other game engines and inheritance: I think most people are aware of its evils, though I
generally believe it's better to have it than not have it. If you try to keep the bulk of your functionality in components
and use inheritance primarily as a means to manage components, then you probably won't find yourself having to
move or copy paste code around.

## Tip#4: Create Your Own Component Base Type

```c#
class MonoBase : MonoBehaviour
{
    //just leave it blank until you need it!
}
```
This step is usually not necessary in smaller games. Often, however, you'll find yourself wanting to add some sort
of basic functionality to *all* of your objects. By creating a class which extends MonoBehaviour at the very
start, you can leave it empty until you decide to add that functionality. For example, if later on you want to add an
alternative version of `AddComponent<>()` or `GetComponent<>()` which performs extra steps or debug logging, you
easily can.

If you decide to do this, you can also change the default script that gets created when you make a new class by editing
`<Unity install folder>/Editor/Data/Resources/NewBehaviourScript.cs` to inherit from your own base class. Then you'll
also have a reminder to make this base class every time you start a new project.

This is a pretty straight-forward tip and I'm not going to get into all the ways it might be useful, but it's definitely
something that's easier to do at the start than it is to do later on.
