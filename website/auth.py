from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

# @auth.route('/login')
# def login():
#     return "<p>Login<p> "

# @auth.route('/logout')
# def logout():
#     return "<p>Logout<p>"

# @auth.route('/sign-up')
# def log():
#     return "<p>sign-up<p>"

@auth.route('/account.html', methods=['GET','POST'])
def account():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    print(username)
    print(email)
    print(password)
    return render_template("account.html")

