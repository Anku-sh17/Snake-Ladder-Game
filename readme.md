### Assumptions
1. **Fixed Players**: The game is designed for two players: one human player and one CPU player.
2. **Game Flow**: Players take turns rolling a die, and their positions are updated based on the roll and the presence of snakes or ladders.
3. **Authentication**: A simple login system is used to authenticate players.
4. **Performance Measurement**: Performance will be measured in terms of response time for API calls and server resource utilization.

### API Design
1. **`POST /login`**: Authenticate a user.
2. **`GET /game`**: Get the current state of the game.
3. **`POST /play_turn`**: Play a turn for the current player.
4. **`POST /reset_game`**: Reset the game to its initial state.
5. **`GET /logout`**: Log out the user.

### Game Objects
1. **Player**: Represents a player in the game.
2. **CPU**: Represents the CPU player.
3. **GameBoard**: Represents the game board with snakes and ladders.
4. **Die**: Represents the die used to play the game.
5. **Game**: Manages the game state and logic.

### Code Implementation
1. Shown in code
2. Run the app.py file
3. sample for login is given in line number 10

### Performance Measurement

1. **Start the application**:

2. **Play the game**:
    Open a web browser and go to `http://127.0.0.1:5000/` to play the game. Observe the logs for response times.

3. **Collect response times**:
    The response times will be logged in the console. You can calculate the average, minimum, and maximum response times from these logs.

### Log Output
```
INFO:__main__:Request to play_turn took 0.0012 seconds
INFO:__main__:Request to play_turn took 0.0011 seconds
INFO:__main__:Request to play_turn took 0.0013 seconds
```

### Summary of Performance Numbers
- **Response Times**: From the logs, average time was (0.0012s), minimum time was (0.0011), and maximum time was (0.0013s) for the `/play_turn` API.
- **Response Times**: From the logs, the time for `/reset_game` was 0.0006s. 
