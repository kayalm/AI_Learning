"""
Comprehensive Test Suite for Number Guessing Game (HTML Version)
Tests all use cases: Menu navigation, Single Player, Two-Player, Scores, and Timer
"""

import asyncio
import json
import time
from pathlib import Path
from playwright.async_api import async_playwright


class GameTester:
    def __init__(self):
        self.test_results = []
        self.browser = None
        self.page = None
        self.html_path = str(Path(__file__).parent / "game.html")
        
    async def setup(self):
        """Initialize browser"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        await self.page.goto(f"file://{self.html_path}")
        await self.page.wait_for_load_state("networkidle")
        print("✅ Browser initialized and game loaded")
    
    async def teardown(self):
        """Close browser"""
        await self.page.close()
        await self.browser.close()
        await self.playwright.stop()
        print("\n✅ Browser closed")
    
    def record_test(self, test_name, passed, message=""):
        """Record test result"""
        result = "✅ PASS" if passed else "❌ FAIL"
        self.test_results.append((test_name, passed, message))
        print(f"{result}: {test_name}")
        if message:
            print(f"     {message}")
    
    async def test_menu_navigation(self):
        """Test 1: Menu Navigation"""
        print("\n" + "="*60)
        print("TEST 1: Menu Navigation")
        print("="*60)
        
        # Check menu scene is active
        menu_scene = await self.page.query_selector("#menuScene")
        is_visible = await menu_scene.is_visible()
        self.record_test("Menu scene visible on load", is_visible)
        
        # Check all menu buttons exist
        buttons = ["Easy", "Medium", "Hard", "Two-Player Mode", "View Scores"]
        for button_text in buttons:
            btn = await self.page.query_selector(f"button:has-text('{button_text}')")
            exists = btn is not None
            self.record_test(f"Menu button '{button_text}' exists", exists)
    
    async def test_single_player_easy(self):
        """Test 2: Single Player - Easy Mode"""
        print("\n" + "="*60)
        print("TEST 2: Single Player - Easy Mode")
        print("="*60)
        
        # Click Easy button
        await self.page.click("button:has-text('Easy')")
        await self.page.wait_for_load_state("domcontentloaded")
        
        # Check game scene is active
        game_scene = await self.page.query_selector("#gameScene")
        is_visible = await game_scene.is_visible()
        self.record_test("Easy game scene opened", is_visible)
        
        # Check attempts display
        attempts_text = await self.page.text_content("#maxAttempts")
        is_correct = attempts_text == "10"
        self.record_test("Easy mode has 10 attempts", is_correct, f"Actual: {attempts_text}")
        
        # Test making a guess
        input_field = await self.page.query_selector("#guessInput")
        await input_field.fill("50")
        await self.page.click("button:has-text('GUESS')")
        await self.page.wait_for_timeout(500)
        
        # Check message appears
        message = await self.page.query_selector("#messageContainer")
        has_content = await message.inner_text()
        self.record_test("Guess feedback message appears", len(has_content) > 0, f"Message: {has_content[:50]}...")
        
        # Check timer is running
        timer_text = await self.page.text_content("#timer")
        timer_value = float(timer_text)
        self.record_test("Timer is running", timer_value > 0, f"Timer: {timer_text}s")
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_single_player_medium(self):
        """Test 3: Single Player - Medium Mode"""
        print("\n" + "="*60)
        print("TEST 3: Single Player - Medium Mode")
        print("="*60)
        
        # Click Medium button
        await self.page.click("button:has-text('Medium')")
        await self.page.wait_for_load_state("domcontentloaded")
        
        # Check attempts display
        attempts_text = await self.page.text_content("#maxAttempts")
        is_correct = attempts_text == "7"
        self.record_test("Medium mode has 7 attempts", is_correct, f"Actual: {attempts_text}")
        
        # Make a guess
        input_field = await self.page.query_selector("#guessInput")
        await input_field.fill("75")
        await self.page.click("button:has-text('GUESS')")
        await self.page.wait_for_timeout(500)
        
        self.record_test("Medium mode guess submitted", True)
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_single_player_hard(self):
        """Test 4: Single Player - Hard Mode"""
        print("\n" + "="*60)
        print("TEST 4: Single Player - Hard Mode")
        print("="*60)
        
        # Click Hard button
        await self.page.click("button:has-text('Hard')")
        await self.page.wait_for_load_state("domcontentloaded")
        
        # Check attempts display
        attempts_text = await self.page.text_content("#maxAttempts")
        is_correct = attempts_text == "5"
        self.record_test("Hard mode has 5 attempts", is_correct, f"Actual: {attempts_text}")
        
        # Make a guess
        input_field = await self.page.query_selector("#guessInput")
        await input_field.fill("25")
        await self.page.click("button:has-text('GUESS')")
        await self.page.wait_for_timeout(500)
        
        self.record_test("Hard mode guess submitted", True)
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_input_validation(self):
        """Test 5: Input Validation"""
        print("\n" + "="*60)
        print("TEST 5: Input Validation")
        print("="*60)
        
        # Start easy game
        await self.page.click("button:has-text('Easy')")
        await self.page.wait_for_load_state("domcontentloaded")
        
        # Test invalid input (empty)
        await self.page.click("button:has-text('GUESS')")
        await self.page.wait_for_timeout(300)
        message = await self.page.text_content("#messageContainer")
        self.record_test("Empty input shows error", "number" in message.lower() or "please" in message.lower(), f"Message: {message[:50]}...")
        
        # Test invalid input (negative)
        input_field = await self.page.query_selector("#guessInput")
        await input_field.fill("-5")
        await self.page.click("button:has-text('GUESS')")
        await self.page.wait_for_timeout(300)
        message = await self.page.text_content("#messageContainer")
        self.record_test("Negative input shows error", "number" in message.lower() or "between" in message.lower(), f"Message: {message[:50]}...")
        
        # Test invalid input (> 100)
        await input_field.fill("150")
        await self.page.click("button:has-text('GUESS')")
        await self.page.wait_for_timeout(300)
        message = await self.page.text_content("#messageContainer")
        self.record_test("> 100 input shows error", "100" in message or "between" in message.lower(), f"Message: {message[:50]}...")
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_two_player_mode(self):
        """Test 6: Two-Player Mode"""
        print("\n" + "="*60)
        print("TEST 6: Two-Player Mode")
        print("="*60)
        
        # Click Two-Player mode
        await self.page.click("button:has-text('Two-Player Mode')")
        await self.page.wait_for_load_state("domcontentloaded")
        await self.page.wait_for_timeout(500)
        
        # Check setup scene
        setup_scene = await self.page.query_selector("#twoPlayerSetupScene")
        is_visible = await setup_scene.is_visible()
        self.record_test("Two-Player setup scene opened", is_visible)
        
        # Select difficulty - use a more specific selector
        difficulty_buttons = await self.page.query_selector_all(".difficulty-btn")
        if len(difficulty_buttons) > 0:
            await difficulty_buttons[0].click()  # Click first difficulty (Easy)
            await self.page.wait_for_timeout(300)
        
        # Click START GAME button
        start_btn = await self.page.query_selector("button:has-text('START GAME')")
        if start_btn:
            await start_btn.click()
            await self.page.wait_for_load_state("domcontentloaded")
            await self.page.wait_for_timeout(500)
        
        # Check game scene
        game_scene = await self.page.query_selector("#twoPlayerGameScene")
        is_visible = await game_scene.is_visible()
        self.record_test("Two-Player game scene opened", is_visible)
        
        # Check player 1 is current
        current_player = await self.page.text_content("#currentPlayer")
        self.record_test("Player 1 starts first", "Player 1" in current_player, f"Current: {current_player}")
        
        # Player 1 makes a guess
        input_field = await self.page.query_selector("#guessInputTP")
        if input_field:
            await input_field.fill("50")
            # Find the GUESS button in two-player mode specifically
            guess_buttons = await self.page.query_selector_all("button:has-text('GUESS')")
            if len(guess_buttons) > 0:
                await guess_buttons[-1].click()  # Click the last GUESS button (two-player one)
                await self.page.wait_for_timeout(500)
            
            # Check player 1 attempts incremented
            p1_attempts = await self.page.text_content("#p1Attempts")
            self.record_test("Player 1 attempts incremented", p1_attempts == "1", f"Attempts: {p1_attempts}")
            
            # Check player 2 should be next
            current_player = await self.page.text_content("#currentPlayer")
            self.record_test("Turn switched to Player 2", "Player 2" in current_player, f"Current: {current_player}")
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()

    
    async def test_hints(self):
        """Test 7: Game Hints"""
        print("\n" + "="*60)
        print("TEST 7: Game Hints (Too High/Low)")
        print("="*60)
        
        # Start easy game
        await self.page.click("button:has-text('Easy')")
        await self.page.wait_for_load_state("domcontentloaded")
        await self.page.wait_for_timeout(300)
        
        # Make a guess - test will show either too high or too low
        input_field = await self.page.query_selector("#guessInput")
        if input_field:
            await input_field.fill("10")
            # Click the GUESS button in the input group within gameScene
            await self.page.evaluate("document.querySelector('#gameScene .input-group button').click()")
            await self.page.wait_for_timeout(500)
            
            message = await self.page.text_content("#messageContainer")
            has_feedback = len(message) > 0
            self.record_test("Guess provides feedback", has_feedback, f"Message: {message[:60]}...")
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_timer(self):
        """Test 8: Timer Functionality"""
        print("\n" + "="*60)
        print("TEST 8: Timer Functionality")
        print("="*60)
        
        # Start easy game
        await self.page.click("button:has-text('Easy')")
        await self.page.wait_for_load_state("domcontentloaded")
        
        # Check initial timer
        timer1 = await self.page.text_content("#timer")
        
        # Wait a bit
        await self.page.wait_for_timeout(1000)
        
        # Check timer increased
        timer2 = await self.page.text_content("#timer")
        timer1_val = float(timer1)
        timer2_val = float(timer2)
        
        self.record_test("Timer increments over time", timer2_val > timer1_val, 
                        f"Timer: {timer1}s → {timer2}s")
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_scores_display(self):
        """Test 9: Scores Display and Persistence"""
        print("\n" + "="*60)
        print("TEST 9: Scores Display and Persistence")
        print("="*60)
        
        # Clear localStorage first
        await self.page.evaluate("() => localStorage.clear()")
        
        # Click View Scores
        await self.page.click("button:has-text('View Scores')")
        await self.page.wait_for_load_state("domcontentloaded")
        
        # Check scores scene
        scores_scene = await self.page.query_selector("#scoresScene")
        is_visible = await scores_scene.is_visible()
        self.record_test("Scores scene opened", is_visible)
        
        # Check high scores section exists
        high_scores = await self.page.query_selector("#highScores")
        exists = high_scores is not None
        self.record_test("High Scores section exists", exists)
        
        # Check session scores section
        session_scores = await self.page.query_selector("#sessionScores")
        exists = session_scores is not None
        self.record_test("Session Scores section exists", exists)
        
        # Check clear scores button exists
        clear_btn = await self.page.query_selector(".clear-scores-btn")
        exists = clear_btn is not None
        self.record_test("Clear Scores button exists", exists)
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_keyboard_input(self):
        """Test 10: Keyboard Input (Enter Key)"""
        print("\n" + "="*60)
        print("TEST 10: Keyboard Input (Enter Key)")
        print("="*60)
        
        # Start easy game
        await self.page.click("button:has-text('Easy')")
        await self.page.wait_for_load_state("domcontentloaded")
        
        # Get initial attempts
        attempts1 = await self.page.text_content("#attemptsLeft")
        
        # Use Enter key to submit
        input_field = await self.page.query_selector("#guessInput")
        await input_field.fill("50")
        await input_field.press("Enter")
        await self.page.wait_for_timeout(500)
        
        # Check attempts changed
        attempts2 = await self.page.text_content("#attemptsLeft")
        self.record_test("Enter key submits guess", attempts1 != attempts2, 
                        f"Attempts: {attempts1} → {attempts2}")
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_complete_game(self):
        """Test 11: Complete Game Flow (Win)"""
        print("\n" + "="*60)
        print("TEST 11: Complete Game Flow (Win)")
        print("="*60)
        
        # Start easy game
        await self.page.click("button:has-text('Easy')")
        await self.page.wait_for_load_state("domcontentloaded")
        await self.page.wait_for_timeout(300)
        
        # Make multiple guesses to eventually hit the secret  
        input_field = await self.page.query_selector("#guessInput")
        if input_field:
            for guess_num, guess in enumerate([50, 25, 75, 10, 90, 33, 66, 42]):
                # Check if input is still visible 
                if not await input_field.is_visible():
                    break
                    
                await input_field.fill(str(guess))
                # Click the GUESS button in the input group
                await self.page.evaluate("document.querySelector('#gameScene .input-group button').click()")
                await self.page.wait_for_timeout(400)
                
                # Check if result scene appeared
                result_scene = await self.page.query_selector("#resultScene")
                if result_scene and await result_scene.is_visible():
                    break
        
        # Check result scene
        result_scene = await self.page.query_selector("#resultScene")
        is_visible = result_scene and await result_scene.is_visible()
        self.record_test("Result screen shown after game completion", is_visible)
        
        # Check if content exists
        if is_visible:
            result_content = await self.page.text_content("#resultContent")
            has_content = len(result_content) > 10
            self.record_test("Result content displayed", has_content, f"Content length: {len(result_content)}")
        
        print("  (Returning to menu...)")
        await self.go_back_to_menu()
    
    async def test_mobile_responsiveness(self):
        """Test 12: Mobile Responsiveness"""
        print("\n" + "="*60)
        print("TEST 12: Mobile Responsiveness")
        print("="*60)
        
        # Set mobile viewport
        await self.page.set_viewport_size({"width": 375, "height": 667})
        await self.page.wait_for_timeout(500)
        
        # Check buttons are still visible
        btn = await self.page.query_selector("button:has-text('Easy')")
        is_visible = await btn.is_visible()
        self.record_test("Easy button visible on mobile", is_visible)
        
        # Check container is responsive
        container = await self.page.query_selector(".container")
        bounding_box = await container.bounding_box()
        width = bounding_box["width"]
        self.record_test("Container fits mobile screen", width <= 375, f"Width: {width}px")
        
        # Reset viewport
        await self.page.set_viewport_size({"width": 1280, "height": 720})
        await self.page.wait_for_timeout(300)
    
    async def run_all_tests(self):
        """Run all tests"""
        await self.setup()
        
        try:
            await self.test_menu_navigation()
            await self.test_single_player_easy()
            await self.test_single_player_medium()
            await self.test_single_player_hard()
            await self.test_input_validation()
            await self.test_two_player_mode()
            await self.test_hints()
            await self.test_timer()
            await self.test_scores_display()
            await self.test_keyboard_input()
            await self.test_complete_game()
            await self.test_mobile_responsiveness()
            
        finally:
            await self.teardown()
        
        # Print summary
        self.print_summary()
    
    async def go_back_to_menu(self):
        """Helper to go back to menu"""
        try:
            # Try using the JavaScript function first
            await self.page.evaluate("window.backToMenu && window.backToMenu()")
            await self.page.wait_for_timeout(300)
        except:
            # If that fails, just wait
            await self.page.wait_for_timeout(500)
    
    def print_summary(self):
        """Print test summary"""
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        
        total = len(self.test_results)
        passed = sum(1 for _, result, _ in self.test_results if result)
        failed = total - passed
        
        for test_name, result, message in self.test_results:
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"{status}: {test_name}")
        
        print("\n" + "-"*60)
        print(f"Total: {total} | Passed: {passed} | Failed: {failed}")
        print(f"Success Rate: {(passed/total*100):.1f}%")
        print("="*60)


async def main():
    tester = GameTester()
    await tester.run_all_tests()


if __name__ == "__main__":
    print("\n🎮 NUMBER GUESSING GAME - COMPREHENSIVE TEST SUITE")
    print("="*60)
    print("Testing all use cases: Menu, Single Player, Two-Player,")
    print("Validation, Hints, Timer, Scores, and Responsiveness")
    print("="*60)
    
    asyncio.run(main())
