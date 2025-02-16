`loading.py`
-------------
is a module that contains functions for creating and managing loading bars.

Here is a basic implementation of a loading bar:

```python
from loading import LoadingBar
import time

# Make a default function to be called when the loading is complete
def on_finish():
    print("Loading complete!")
# Create a loading bar with a length of 50, a total of 100, and using the default characters
total = 100
bar = LoadingBar(50, total, on_finish)

for i in range(total):
    bar.update(i+1)
    time.sleep(0.1)

# Output:
#[██████████████████████████████████████████████████] 100/100 (100%)
```
