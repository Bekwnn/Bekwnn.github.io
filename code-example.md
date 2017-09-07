---
layout: default
---

Here you go, Nick:
```c++
#include <string>
#include <iostream>
 
using namespace std;
 
int main()
{
	int const Size = 5;
	string Array[] = { "First", "Second", "Third", "Fourth", "Fifth" };
 
 
	for( string* Start = Array; Start < Array + Size; ++Start )
	{
		cout << *Start << endl;
	}
}
```
