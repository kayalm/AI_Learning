# To-Do List Application

A modern, feature-rich to-do list app with dark/light theme support, priority levels, due dates, and smart filtering.

## Features

- **Dark & Light Mode**: Toggle between sleek dark theme and clean light theme with persistent preference
- **Priority Levels**: Assign tasks as High, Medium, or Low priority (color-coded for easy identification)
- **Due Dates**: Set and track due dates for each task to manage deadlines
- **Smart Filtering**: View All, Active, or Completed tasks with one click
- **Priority Sorting**: Sort tasks by priority to focus on what matters most
- **Task Statistics**: See at a glance how many tasks you have and how many are completed
- **Persistent Storage**: Your tasks are automatically saved to browser storage and restored on reload
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Beautiful, intuitive interface with smooth animations and transitions

## Project Structure

```
ToDo_app/
├── index.html       # Complete to-do app (single HTML file)
└── README.md       # This file
```

## How to Use

### Getting Started

1. Open `index.html` in any modern web browser
2. The app loads with any saved tasks from your previous session
3. Start adding your tasks!

### Adding Tasks

1. **Type your task** in the text input field
2. **Select a due date** (optional) using the date picker
3. **Choose a priority level** from the dropdown (High, Medium, Low)
4. **Click "Add Task"** to add it to your list

### Managing Tasks

**Complete a Task:**
- Click the checkbox next to a task to mark it as done
- Completed tasks appear with a strikethrough and darker background

**Delete a Task:**
- Click the trash icon button on the right side of any task

**Edit Task Details:**
- Tasks can be edited by clicking on them (if feature is enabled)
- Re-select priority or due date as needed

### Filtering & Sorting

**Filter Tasks:**
- Click **"All"** to see every task
- Click **"Active"** to see only incomplete tasks
- Click **"Done"** to see only completed tasks

**Sort by Priority:**
- Click **"Sort by Priority"** button to arrange tasks by urgency
- Order: High → Medium → Low

### Theme Toggle

- Click the moon/sun icon in the header to switch between dark and light modes
- Your preference is saved automatically

### View Statistics

- **Total Tasks**: Shows the total number of tasks you have
- **Completed**: Shows how many tasks are marked as done
- **Progress**: Visual indication of completion status

## Features Explained

### Priority System

- **High Priority** (Red): Urgent tasks that need immediate attention
- **Medium Priority** (Orange): Important tasks with moderate urgency
- **Low Priority** (Green): Tasks that can wait or are nice-to-haves

Color-coded badges make it easy to see at a glance which tasks are most important.

### Due Dates

- Set due dates to remind yourself of deadlines
- Dates are displayed alongside each task
- Use the date picker for easy selection
- Tasks with due dates help you plan ahead

### Local Storage

- All your tasks are saved in your browser's local storage
- No account or internet connection needed (once loaded)
- Data persists even after closing the browser
- Works completely offline

### Responsive Design

The app adapts beautifully to any screen size:
- **Desktop**: Full width with all features visible
- **Tablet**: Optimized layout for medium screens
- **Mobile**: Touch-friendly interface that works great on phones

## Design

### Color Scheme

**Dark Mode (Default):**
- Background: #0f0f0f (Nearly black)
- Cards: #1a1a1a (Dark gray)
- Accent: #c8f135 (Neon yellow-green)
- Secondary: #f1c135 (Golden yellow)
- Text: Light gray

**Light Mode:**
- Background: #fafafa (Off-white)
- Cards: #ffffff (White)
- Accent: #7cb342 (Sage green)
- Secondary: #f57f17 (Orange)
- Text: Dark gray

### Typography

- **Headers**: Syne font (bold, geometric)
- **Body**: DM Sans font (clean, readable)
- Modern, minimal design aesthetic

### UI Elements

- Rounded corners (12px border radius) for a modern feel
- Smooth transitions and hover effects
- Touch-friendly buttons and controls
- Clean, uncluttered layout

## Browser Compatibility

Tested and working on:
- Google Chrome 90+
- Mozilla Firefox 88+
- Apple Safari 14+
- Microsoft Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)
- Any browser with ES6 JavaScript support and localStorage

## Technical Details

**Technology Stack:**
- Pure HTML5
- CSS3 (Grid, Flexbox, Custom Properties, Transitions)
- Vanilla JavaScript (ES6+)
- localStorage API for data persistence
- No external dependencies or frameworks

**File Size:** Single HTML file (~15-20 KB)

**Performance:**
- Instant load time
- Smooth animations and interactions
- Optimized for all devices

## Usage Tips

1. **Organize by Priority**: Use the priority sort to focus on high-priority tasks first
2. **Set Due Dates**: Never miss a deadline by setting due dates on important tasks
3. **Regular Cleanup**: Delete completed tasks to keep your list focused
4. **Check Progress**: Watch your completion percentage grow as you finish tasks
5. **Theme Preference**: Switch to light mode if you work in bright environments

## Data Management

### How Data is Stored

- Tasks are stored in browser's localStorage
- Each task includes: title, due date, priority, completion status
- Data is automatically saved when you make changes
- Data persists across browser sessions

### Clearing Data

To clear all tasks:
1. Open browser Developer Tools (F12)
2. Go to Application → Local Storage
3. Find the entry for your domain
4. Delete it
5. Refresh the page

Or use the browser's "Clear Browsing Data" option and select "Cookies and other site data"

## Troubleshooting

**Tasks not saving:**
- Ensure localStorage is enabled in your browser
- Check browser settings for data storage permissions
- Try a different browser to verify the issue

**App not loading:**
- Clear browser cache and reload
- Try opening in incognito/private mode
- Verify JavaScript is enabled

**Tasks disappearing:**
- Check if you've cleared browser data/cache recently
- Ensure you're using the same browser
- Try a different browser to test

## Future Enhancement Ideas

- Cloud sync with multiple devices
- Recurring tasks and subtasks
- Task categories or tags
- Collaboration features
- Mobile app versions
- Integration with calendar apps
- Notifications for upcoming due dates
- Dark mode auto-detection based on system settings
- Export tasks to CSV or PDF
- Undo/Redo functionality

## Accessibility

The app includes:
- Keyboard navigation support
- Clear color contrast for readability
- Semantic HTML structure
- Form labels and input descriptions
- Touch-friendly interface for mobile users

## Privacy

- All data is stored locally on your device
- No data is sent to any servers
- No tracking or analytics
- No external API calls
- Completely private and offline-capable

## License

Created as an educational AI learning project.

## Contact & Support

For issues, suggestions, or contributions, please visit:
https://github.com/kayalm/AI_Learning/tree/main/ToDo_app

---

**Version:** 1.0  
**Last Updated:** March 5, 2026  
**Created with:** HTML5, CSS3, Vanilla JavaScript
