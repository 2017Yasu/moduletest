"""モジュール練習03

`__all__` を定義するのは、ディレクトリ名を名前空間とするモジュールを `*` で `import` したときに参照可能とするオブジェクトを定義しているにすぎません。

"""

__all__ = ["hello1", "hello2"]

def hello1():
    print("Hello, this is hello1")

def hello2():
    print("Hello, this is hello2")

def hello3():
    print("Hello, this is hello3")
