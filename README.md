# todo_list

## 概要  
このプロジェクトは、Python と Tkinter を使って作られた「To‑Do リスト」アプリケーションです。GUI による操作を学ぶために作成しました。  
最初に CLI（CUI）版を実装・動作確認したのち、GUI 版として `tk.py` を追加しています。

## 特長  
- シンプルで直感的な UI を備えた To‑Do リストアプリ  
- タスクの追加、完了チェック、削除が可能  

## 動作環境  
- Python 3.x  
- Tkinter（通常、標準ライブラリで同梱）  
- Windows / macOS / Linux（Tkinter が動作する環境）  

## インストール & 実行方法  
1. 本リポジトリをクローンまたはダウンロード  
   ```bash
   git clone https://github.com/Tatsuzaki-Akio/todo_list.git
   cd todo_list
````

2. 必要であれば仮想環境を作成し、Python を有効化

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. GUI 版を実行

   ```bash
   python tk.py
   ```

   CLI 版を試したい場合は以下を実行

   ```bash
   python tasks.py
   ```

## ファイル構成

```
todo_list/
├── README.md        ← このファイル
├── tasks.txt        ← タスクデータ（CLI 版用）
├── tasks.py         ← CLI 版アプリケーション
└── tk.py            ← Tkinter GUI 版アプリケーション
```




