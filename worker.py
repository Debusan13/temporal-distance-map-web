import os

def work():
    with open("warpAnimation.py") as f:
        code = compile(f.read(), "warpAnimation.py", 'exec')
        exec(code)
    with open("makeAnimation.py") as f:
        code = compile(f.read(), "makeAnimation.py", 'exec')
        exec(code)