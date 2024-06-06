from flask import Flask, render_template, request, redirect, url_for, session, g
import random
import time
import logging

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a more secure key in production

# Sample user for login
users = {'test': 'test123'}


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    if request.endpoint == 'play_turn':
        duration = time.time() - g.start_time
        logger.info(f"Request to {request.endpoint} took {duration:.4f} seconds")
    return response

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('game'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('game'))
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/game')
def game():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template('game.html')

# Snake and Ladder positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initial player and CPU positions
player_position = 0
cpu_position = 0

@app.route('/play_turn', methods=['POST'])
def play_turn():
    global player_position, cpu_position

    def move(position):
        roll = random.randint(1, 6)
        position += roll
        if position in snakes:
            position = snakes[position]
        elif position in ladders:
            position = ladders[position]
        if position > 100:
            position = 100
        return position

    player_position = move(player_position)
    cpu_position = move(cpu_position)

    winner = None
    if player_position == 100:
        winner = 'Player'
    elif cpu_position == 100:
        winner = 'CPU'

    print("Player at: ",player_position)
    print("Cpu at: ",cpu_position)

    return {
        'player_position': player_position,
        'cpu_position': cpu_position,
        'winner': winner
    }

@app.route('/reset_game', methods=['POST'])
def reset_game():
    global player_position, cpu_position
    player_position = 0
    cpu_position = 0
    return {
        'player_position': player_position,
        'cpu_position': cpu_position,
    }

if __name__ == '__main__':
    app.run(debug=True)
