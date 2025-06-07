# モジュール練習

以下のQiita記事を参考

<https://qiita.com/msi/items/d91ea3900373ff8b09d7>

## まとめ (抜粋)

`__init__.py` の役割

* ディレクトリにより階層化されたモジュールを `import` するために必要。
* モジュールの初期化処理を記載
  * 名前空間の初期化
  * ワイルドカード `import` の対象の定義 (`__all__` の定義)
  * 同じディレクトリにある他のモジュールの名前空間の定義

モジュール内に記載された実行文は最初の `import` 時に一度だけ実行される。

その他参考

* [Python チュートリアル - モジュール](https://docs.python.org/3/tutorial/modules.html)
