"""モジュール練習05

`module05/module06.py` は、最初から `__init__.py` の外部で開発を進めたファイル、という想定です。
"""

print("in module06.py")

def hello(caller=""):
    print("Hello, world! in module06 called by {}".format(caller))
