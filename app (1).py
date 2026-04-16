from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
users = {}

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/chatpage')
def chatpage():
    return render_template("chat.html")

@app.route('/register_user', methods=['POST'])
def register_user():
    users[request.form['username']] = request.form['password']
    return redirect('/')

@app.route('/login_user', methods=['POST'])
def login_user():
    u = request.form['username']
    p = request.form['password']
    if u in users and users[u] == p:
        return redirect('/chatpage')
    return "Invalid Login ❌"

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get("message").lower()

    if "exam" in msg:
        res = "📅 Exams:\nMaths - 20 April\nPhysics - 22 April"
    elif "placement" in msg:
        res = "💼 Placement:\nTCS - 30 April"
    else:
        res = "Try: exam / placement"

    return jsonify({"response": res})

if __name__ == "__main__":
    app.run(debug=True)