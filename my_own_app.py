from flask import Flask, render_template, request, redirect, url_for, flash
from database import SessionLocal
from models import User, Task
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/status')
def status():
    return "<h2>All systems are operational.</h2>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method ==  'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        session = SessionLocal()
        user = session.query(User).filter_by(username=username).first()

        if user:
            if user.password == password:
                session.close()
                #print(f"Welcome back, {username}!")
                return redirect(url_for('dashboard'))
        
        session.close()
        return "Invalid credentials!\nNote: if you've never created an account before click 'Register' down below!" 
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        if password != confirm_password:
            return "Passwords do not match"
        
        session = SessionLocal()

        user_exists = session.query(User).filter_by(username=username).first()
        if user_exists:
            session.close()
            return "Username already taken!"
        
        new_user = User(username=username, password=password)
        
        try:
            session.add(new_user)
            session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            session.rollback()
            return f"An error occurred: {e}"
        finally:
            session.close()
    
    return render_template("register.html")


@app.route('/add', methods=["POST"])
def add_task():
    content = request.form.get("content")
    priority = request.form.get("priority")
    due_date = request.form.get("due_date")

    if not content:
        return "Task content cannot be empty!", 400
    
    with SessionLocal() as session:
        try:
            new_task = Task(content=content, priority=int(priority) if priority else 1, due_date=due_date, user_id=1)
            
            session.add(new_task)
            session.commit()
        except Exception as e:
            session.rollback()
            return f"An error occurred: {e}"
    
    return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    session = SessionLocal()
    tasks = session.query(Task).filter_by(user_id=1).all()
    session.close()
    return render_template('dashboard.html', tasks=tasks)


#@app.route('complete-task/<int:task-id>')


if __name__ == "__main__":
    app.run(debug=True)