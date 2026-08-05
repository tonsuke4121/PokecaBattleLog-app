from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "battles.db"

# --- DB 初期化（超重要） ---
def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE battles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                my_deck TEXT,
                opp_deck TEXT,
                result TEXT,
                memo TEXT
            )
        """)
        conn.commit()
        conn.close()

init_db()


# --- 戦績一覧（勝率計算つき） ---
@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM battles ORDER BY id DESC")
    battles = c.fetchall()

    # デッキごとの勝率計算
    stats = {}
    for b in battles:
        deck = b[2]  # my_deck
        result = b[4]  # Win / Lose

        if deck not in stats:
            stats[deck] = {"win": 0, "lose": 0}

        if result == "Win":
            stats[deck]["win"] += 1
        else:
            stats[deck]["lose"] += 1

    winrates = {}
    for deck, s in stats.items():
        total = s["win"] + s["lose"]
        winrate = (s["win"] / total) * 100 if total > 0 else 0
        winrates[deck] = round(winrate, 1)

    conn.close()
    return render_template("index.html", battles=battles, winrates=winrates)


# --- 新規登録 ---
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        date = request.form['date']
        my_deck = request.form['my_deck']
        opp_deck = request.form['opp_deck']
        result = request.form['result']
        memo = request.form['memo']

        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO battles (date, my_deck, opp_deck, result, memo) VALUES (?, ?, ?, ?, ?)",
                  (date, my_deck, opp_deck, result, memo))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('new.html')


# --- 削除機能 ---
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM battles WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)