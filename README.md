# Full Speed Python
#### 1- read json file
```Python
import json
# read json file
with open('data/person.json') as f:
    data = json.load(f)

print(data)
# output 
{'name': 'Anwar', 'languages': ['English', 'Arabic']}
```
<a href="https://youtu.be/hoCrOl6FSGY">link video</a>
-----------------------------------------------------------
#### 2- Flatten a list of lists
```Python
# Flatten a list of lists
data = [
        [1, 2 ], [3, 5], [8, 10]]
result = []
for x in data:
    for y in x:
        result.append(y)

print(result)
# output 
[1, 2, 3, 5, 8, 10]
```
<a href="https://youtu.be/ZUDsA3fOBpY">link video</a>