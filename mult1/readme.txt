
実行方法:
python simple_search.py
python BM.py

1. simple_search.py:
シンプルサーチのコード
Simple_searchというクラスに第１引数:検索文字列、第2引数:テキストを与える


2. BM.py:
BM法のコード
BM_searchというクラスに第１引数:検索文字列、第2引数:テキストを与える

3. simple_bm_graph.ipynb:
simple_search、BM_searchの比較グラフ作成
検索文字を
1文字
3文字
21文字
93文字
で検索し、速度比較を行っている
テキストは
https://arxiv.org/pdf/1703.06870.pdf
を使用
グラフを作成する際、テキストの長さを変更する必要があったためfor文で徐々に読み込む文字数を増やしていった
