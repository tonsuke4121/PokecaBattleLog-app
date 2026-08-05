# PokecaBattleLog-app

ポケモンカードの対戦結果を記録・管理するための Web アプリケーションです。  
対戦日、使用デッキ、相手デッキ、勝敗、メモを登録し、一覧で確認できます。  
さらに、デッキごとの勝率を自動集計し、戦績の削除も可能です。  
Docker コンテナとして動作するため、環境に依存せず同じ状態で実行できます。

---

## システム概要

**PokecaBattleLog-app** は、ポケモンカードの対戦記録を管理するための簡易 Web アプリです。  
Flask（Python）と SQLite を使用しており、ローカル環境でも Docker コンテナでも動作します。

### 主な用途
- 自分のデッキの勝率を把握する
- 対戦履歴を記録する
- デッキごとの傾向を分析する
- 誤って登録した戦績を削除する

---

## 主な機能

### 1. 戦績の新規登録
- 対戦日
- 自分のデッキ
- 相手のデッキ
- 勝敗（Win / Lose）
- メモ

### 2. 戦績一覧表示
登録した戦績を一覧で確認できます。

### 3. デッキごとの勝率表示
登録された戦績をもとに、  
**自分のデッキごとの勝率（%）を自動計算**して表示します。

### 4. 戦績の削除機能
誤って登録した戦績を削除できます。

### 5. Docker 対応
Docker コンテナとして実行できるため、  
環境差異なく同じ状態でアプリを動かせます。

---

## 使用技術

- **Python 3.14**
- **Flask**
- **SQLite3**
- **HTML / Jinja2**
- **Docker**

---

## ローカルでの実行方法

### 1. 必要ファイルを配置

app.py
Dockerfile
templates/
├── index.html
└── new.html

### 2. アプリを起動


python app.py

### 3. ブラウザでアクセス

http://localhost:5000

---

## 動作例

### 戦績一覧画面
<img width="2879" height="1662" alt="image" src="https://github.com/user-attachments/assets/f2e9c80b-6f92-45a0-9d9f-332ec2ab29bc" />

### 新規戦績登録画面
<img width="2869" height="1577" alt="image" src="https://github.com/user-attachments/assets/f1f2c576-8889-4ef9-8da3-e7fb5b642086" />

### デッキごとの勝率表示
<img width="2867" height="1577" alt="image" src="https://github.com/user-attachments/assets/cd9971ca-7af4-4afb-920c-c23e400a6907" />

## 使い方

1. トップページの「新規登録」をクリック

2. 対戦情報を入力して「登録」

3. 戦績一覧に追加されたことを確認

4. 不要な戦績は「削除」リンクから削除

5. デッキごとの勝率を確認してデッキの傾向を分析

## リポジトリ URL
https://github.com/tonsuke4121/PokecaBattleLog-app
