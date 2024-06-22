from flask import Flask, request, jsonify, render_template

# Password strength checking logic
def check_password_strength(password):
    score = 0
    feedback = []

    # Password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Special character check
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Length score for longer passwords
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    return score, feedback

# Flask application setup
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('project.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data['password']
    score, feedback = check_password_strength(password)
    return jsonify(score=score, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
