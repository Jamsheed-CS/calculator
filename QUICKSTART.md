# Quick Start Guide

## Get Started in 3 Steps

### 1. Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Start the Backend Server
```bash
python app.py
```

You should see:
```
============================================================
Calculator API Server
============================================================
Starting Flask server on http://localhost:5000
```

### 3. Open the Frontend

**Option A - Simple (may have CORS issues):**
- Open `frontend/index.html` directly in your browser

**Option B - Recommended:**
```bash
# In a new terminal
cd frontend
python -m http.server 8000
```

Then navigate to: `http://localhost:8000`

---

## Test It Out

Try these calculations:

### Basic Arithmetic
- `2 + 2`
- `10 - 5`
- `3 × 4`
- `15 ÷ 3`

### Scientific (click "Scientific" button first)
- `sin(30)` = 0.5
- `cos(60)` = 0.5
- `sqrt(16)` = 4
- `log(100)` = 2
- `5!` = 120

### Complex Expressions
- `sin(30) + cos(60)` = 1.0
- `sqrt(16) + log(100)` = 6
- `(2 + 3) × 4` = 20

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| 0-9 | Numbers |
| +, -, *, / | Operators |
| Enter | Calculate |
| Backspace | Delete |
| Escape | Clear |

---

## Features at a Glance

✓ **25+ Operations**: Arithmetic + Scientific
✓ **Expression Display**: See your full calculation
✓ **History Sidebar**: Latest 10 calculations
✓ **Memory Functions**: MC, MR, M+, M-
✓ **Keyboard Support**: Full keyboard control
✓ **Responsive Design**: Works on all screen sizes
✓ **Error Handling**: Clear error messages

---

## Troubleshooting

**Can't connect to backend?**
- Make sure `python app.py` is running in the backend folder
- Backend runs on port 5000

**CORS errors?**
- Use Python HTTP server: `python -m http.server 8000`
- Don't open HTML file directly

---

For full documentation, see [README.md](README.md)
