"""モジュール練習05
"""

print("in _module05.py")

def hello(caller: str = ""):
    """Hello world

    :param str caller: 呼び出し元
    """
    print("Hello, world! in _module05 called by {}".format(caller))
