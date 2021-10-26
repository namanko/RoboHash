# RoboHashpy
## An api wrapper for RoboHash, a cool service by @e1ven, which generates images from random text!

##Currently Available Functions
- get_im_hash(text: str,set: int[optional],size: str[optional])
- get_grav_hash(email/hash: str,gravatar: str)

**The set parameter can be an integer from 1 to 5**
The following list tells what each number, 1 to 5, represents
1. Robots
2. Monsters
3. Disembodied heads
4. Kittens
5. Humans

##Default values
- set:- 1
- size:- 200x200
- gravatar:- no

##Sample Usage
```python
from RoboHashpy import RoboHash

rb =  RoboHash()

print(rb.get_im_hash("hello there",5,"200x200"))
```
