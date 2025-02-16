# `loading`
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

## Installation
Because our module is compatible with most operating systems, we have one simple method of installing.

### Step 1:
Clone the repository via *git*:
```bash
# In terminal:
$ git clone git@github.com:ValidIdiot/loading-v1
```
Alternatively, if you have not set up *ssh* with *git* (which I would recommend), you can run:
```bash
$ git clone https://github.com/ValidIdiot/loading-v1
```
Lastly, we *cd* into the cloned repo:
```bash
$ cd loading-v1
```

### Step 2:
The only required dependency is [`colorama`](https://github.com/tartley/colorama). It is a great module for ANSI color-coding in compatible terminals.
```bash
# In terminal:
$ pip install colorama 
```
In our module, `colorama` is used for formatting of the loading bar (if enabled upon class initialization).

### Step 3:
Now, we can actually install `loading`.
```bash
# In terminal:
$ pip install .
```
This will now install `loading` as a Python module on your machine.