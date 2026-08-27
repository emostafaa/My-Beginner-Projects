# 📝 Terminal To-Do List App

A clean, lightweight command-line To-Do List manager built with Python. This application provides a distraction-free environment to track, add, and remove your daily tasks directly from your terminal.

The app focuses on simplicity and clean user interaction by keeping the terminal window organized and updated after every single action.

---

## ✨ Core Features

* **Duplication Prevention:** Automatically checks your list before adding a new item. It handles case-insensitive inputs, meaning you cannot add duplicate tasks like "Buy Milk" if "buy milk" already exists.
* **Smart Input Validation:** Protects the app from errors by verifying your list state. The app prevents users from trying to delete tasks from an empty list and alerts you if you type a task name that doesn't exist.
* **Clean Interface:** Wipes away old terminal clutter instantly after you submit an option, ensuring you only see the menu or your current list.

---

## 🕹️ How It Works

The app operates on a simple 4-option menu structure:
1. **Show Tasks:** Displays your current list with custom bullet formatting. If your list is empty, it lets you know immediately.
2. **Add Task:** Prompts you for a task name, runs a duplication check, and appends it to your active list.
3. **Remove Task:** Safely deletes a completed or unwanted task from your list by matching the name.
4. **Exit Program:** Clears the screen, prints a farewell message, and safely shuts down the application.

---

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.x installed on your machine.

### Running the App
1. Download the `todolist.py` file to your computer.
2. Open your terminal application.
3. Navigate to the folder where the file is saved and execute:

```bash
python todolist.py
```

---

## 📋 Future Roadmap
Planned updates for upcoming versions of the application:
- [ ] **Persistent Storage:** Integrate file handling (`.json` or `.txt`) to save tasks locally so they don't disappear when the app closes.
- [ ] **Task Statuses:** Add a feature to toggle tasks between "Pending" and "Completed" instead of deleting them entirely.
- [ ] **Prioritization:** Allow sorting of tasks by high, medium, or low priority levels.



Note: this README is wriiten by AI but the code by me
