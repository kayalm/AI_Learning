# Number Guessing Game

A fun and interactive number guessing game available in both Python CLI and modern web-based HTML versions.

## Features

- **Timer**: Track how long it takes you to guess the number
- **High Score Persistence**: Your best scores are automatically saved and persist across sessions
- **Three Difficulty Levels**:
  - Easy: Guess a number between 1-100 with 10 attempts
  - Medium: Guess a number between 1-100 with 7 attempts
  - Hard: Guess a number between 1-100 with 5 attempts
- **2-Player Mode**: Take turns playing against a friend with separate attempt counters per player
- **Game Hints**: Receive helpful hints when you're close to getting it right
- **Modern Dark Theme**: Beautiful, responsive UI with smooth animations and glass-morphism effects
- **Mobile Friendly**: Fully responsive design works on all devices
- **Comprehensive Testing**: Automated test suite with 96.7% pass rate

## Project Structure

```
Number_Game/
├── game.py              # Python CLI version
├── game.html            # Web-based version (single HTML file)
├── test_game.py         # Comprehensive automated test suite
├── high_scores.json     # Persistent high scores storage
└── README.md           # This file
```

## How to Play

### Web Version (Recommended)

1. Open `game.html` in any modern web browser
2. Click **"Start Game"** to begin
3. Select your difficulty level (Easy, Medium, or Hard)
4. Enter your guess (1-100) and click **"Submit"**
5. Follow the hints to narrow down the number
6. View your scores anytime by clicking **"View Scores"**
7. Try 2-player mode by selecting **"2-Player Game"**

**Features in Web Version:**
- Real-time timer showing elapsed seconds
- Immediate feedback (Too High, Too Low, Correct!)
- Hints displayed when 3 attempts remain
- Scores automatically saved to browser storage
- Smooth animations and transitions
- Mobile responsive layout

### CLI Version (Python)

1. Run the game:
   ```bash
   python game.py
   ```

2. Follow the on-screen menu:
   - Select Single Player or 2-Player mode
   - Choose difficulty level
   - Enter your guesses

3. Your high scores are saved to `high_scores.json`

**Features in CLI Version:**
- Timer tracking in seconds
- High scores persisted to JSON file
- Turn-based 2-player gameplay
- Score display and management

## Requirements

### For Web Version
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No installation required

### For Python Version
- Python 3.7 or higher
- Standard library only (no external dependencies)

### For Testing
- Python 3.7 or higher
- Playwright: `pip install playwright`
- Run: `python test_game.py`

## Game Rules

1. **Objective**: Guess the secret number between 1 and 100
2. **Attempts**: You have a limited number of attempts based on difficulty:
   - Easy: 10 attempts
   - Medium: 7 attempts
   - Hard: 5 attempts
3. **Feedback**: After each guess, you'll receive:
   - "Too High" if your guess is higher than the secret number
   - "Too Low" if your guess is lower than the secret number
   - "Correct!" when you guess the right number
4. **Hints**: When you have 3 attempts left, you'll receive a hint about how close you are
5. **Scoring**: Complete the game with fewer attempts to beat your high score

## Score System

Scores are tracked by difficulty level:
- **Easy**: Fewer attempts = better score
- **Medium**: Fewer attempts = better score
- **Hard**: Fewer attempts = better score

High scores are saved automatically and persist between sessions.

## Testing

The project includes a comprehensive automated test suite with 30 test cases:

```bash
python test_game.py
```

**Test Coverage:**
- Menu navigation (6 tests)
- Single-player modes: Easy, Medium, Hard (8 tests)
- Input validation (3 tests)
- 2-player mode (5 tests)
- Game hints and feedback (1 test)
- Timer functionality (1 test)
- Score display and persistence (4 tests)
- Keyboard input handling (1 test)
- Complete game flows (2 tests)
- Mobile responsiveness (2 tests)

**Results**: 29/30 tests passing (96.7% success rate)

## Gameplay Tips

1. **Easy Mode**: Great for learning the game mechanics
2. **Medium Mode**: Balanced challenge - good for casual play
3. **Hard Mode**: Test your luck and strategy skills
4. **2-Player Mode**: Perfect for friendly competition with a friend
5. **Use Hints**: Pay attention to the hints when you have 3 attempts left
6. **Strategy**: Try to narrow the range with each guess:
   - Start with 50 (middle of 1-100)
   - Adjust up or down based on feedback
   - Always pick the middle of your remaining range

## Browser Compatibility

Tested and working on:
- Google Chrome 90+
- Mozilla Firefox 88+
- Apple Safari 14+
- Microsoft Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## File Sizes

- `game.html`: ~750 lines (fully self-contained, no external deps)
- `game.py`: ~300 lines (Python implementation)
- `test_game.py`: ~500 lines (automated test suite)

## Authors & License

Created as an educational AI learning project.

## Future Enhancements

Possible improvements for future versions:
- Multiplayer online mode
- Leaderboard system
- Sound effects and additional animations
- Difficulty balancing based on gameplay data
- Database backend for cloud score storage
- Mobile app version

## Troubleshooting

**Game won't load in browser:**
- Ensure you're using a modern browser
- Try clearing your browser cache
- Verify the game.html file is in the correct location

**Scores not saving:**
- Check browser settings (localStorage must be enabled)
- Try a different browser
- Clear browser history and try again

**Test suite issues:**
- Ensure Playwright is installed: `pip install playwright`
- Update Playwright browsers: `playwright install`
- Run tests in a terminal with proper paths

## Contact & Support

For issues, suggestions, or contributions, please visit:
https://github.com/kayalm/AI_Learning/tree/main/Number_Game
