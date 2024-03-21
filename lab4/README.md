# Algorithm
- Use main.py to generate input.txt and output.txt which are in the Verilog folder.
DEBUG mode prints of the selected PAT_NUM infos. Which is the intermediate result of the algorithm.
- Need to install python extension and numpy to generate debug.log
```
    $ pip install icecream
```
- Algorithm might not be perfected, please report the bug to me.

## Pattern Generation
- Set PAT_GEN = True to generate new pattern. And set it False if you dont want to regenerate the pattern.
- Set the DEBUG = True to print out CNN intermediate result which appears in the debug.log

```python
def main():
  random.seed(1234)
  PAT_NUM = 10000
  PAT_GEN = False
  DEBUG   = True
  PAT_TO_DEBUG = 1221
```

## CNN.py
- This is the algorithm that generates output.txt, you can add additional info into the py file.

## Debug.log
- This file has the info of the correct value.
