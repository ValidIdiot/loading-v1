"""
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
# [██████████████████████████████████████████████████] 100/100 (100%)
```

"""
from colorama import Fore as fg, Style as st

class LoadingBar:
    def __init__(self, length, total, func_on_finish, empty_char=' ', fill_char='█', uses_formatting=True, print_on_update=True):
        self.length = length
        self.emptyChar = empty_char
        self.fillChar = fill_char
        self.usesFormatting = uses_formatting
        self.printOnUpdate = print_on_update
        self.total = total
        self.progress = 0
        self.finishFunc = func_on_finish

    def update(self, progress):
        self.progress = progress
        n = (self.progress / self.total) * self.length
        self.currBar = (self.fillChar * int(n)) + (self.emptyChar * (self.length - int(n)))

        percentage = (self.progress / self.total) * 100

        if self.printOnUpdate:
            color = fg.RED if percentage <= 25 else fg.YELLOW if percentage <= 50 else fg.CYAN if percentage < 100 else fg.GREEN
            formatted_bar = f"{color}[{self.currBar}]{fg.RESET} {self.progress}/{self.total} ({percentage:.2f}%)"
            print(formatted_bar, end='\r', flush=True)
        if percentage == 100:
            print("\n")
            self.finishFunc()
        return self.currBar

    def get_status(self):
        return {
            "percentage": (self.progress / self.total) * 100,
            "progress": self.progress,
            "total": self.total,
        }
