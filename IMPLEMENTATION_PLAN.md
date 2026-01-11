# Calculator App - Implementation Plan

## Overview
This document outlines the step-by-step implementation plan for building the calculator app.

---

## File Structure

```
calculator/
│
├── backend/
│   ├── app.py                 # Flask app, routes, CORS setup
│   ├── calculator.py          # Mathematical operations engine
│   ├── database.py            # SQLite database operations
│   ├── requirements.txt       # Flask, Flask-CORS
│   └── calculator.db          # Created automatically on first run
│
├── frontend/
│   ├── index.html            # HTML structure
│   ├── styles.css            # Light theme styling
│   ├── app.js               # Calculator UI logic
│   └── api.js               # Backend API calls
│
├── README.md                 # Setup and usage guide
├── REQUIREMENTS.md           # Functional requirements
├── DESIGN.md                 # UI/UX specifications
├── IMPLEMENTATION_PLAN.md    # This file
└── .gitignore               # Git ignore
```

---

## Implementation Steps

### Phase 1: Backend Development

#### Step 1.1: Database Setup (`backend/database.py`)
```python
Functions to implement:
- init_db()              # Create tables
- save_calculation()     # Insert calculation
- get_history()          # Get latest 10
- delete_calculation()   # Delete by ID
- clear_history()        # Delete all
- close_db()            # Close connection
```

**Database Schema:**
```sql
CREATE TABLE calculations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expression TEXT NOT NULL,
    result REAL NOT NULL,
    operation_type TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### Step 1.2: Calculator Engine (`backend/calculator.py`)
```python
Functions to implement:
- evaluate_expression(expr)  # Main evaluation function
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)
- power(a, b)
- square(a)
- cube(a)
- sqrt(a)
- cbrt(a)
- sin_deg(a)             # Sin in degrees
- cos_deg(a)             # Cos in degrees
- tan_deg(a)             # Tan in degrees
- asin_deg(a)            # Arcsin in degrees
- acos_deg(a)            # Arccos in degrees
- atan_deg(a)            # Arctan in degrees
- log10(a)
- ln(a)
- factorial(n)
- absolute(a)
- reciprocal(a)
- exp(a)
```

**Error Handling:**
- Division by zero
- Domain errors (sqrt of negative, log of zero)
- Invalid expressions
- Return structured error responses

#### Step 1.3: Flask API (`backend/app.py`)
```python
Routes to implement:

1. POST /api/calculate
   - Receive: { "expression": "...", "operation_type": "..." }
   - Calculate using calculator.py
   - Save to database
   - Return: { "success": true, "result": ..., "id": ... }

2. GET /api/history
   - Get latest 10 from database
   - Return: { "success": true, "calculations": [...] }

3. DELETE /api/history/<id>
   - Delete specific calculation
   - Return: { "success": true }

4. DELETE /api/history
   - Clear all history
   - Return: { "success": true, "deleted_count": ... }

Setup:
- Flask app initialization
- CORS configuration (allow localhost:8000 or file://)
- Error handlers (404, 500)
- Run on port 5000
```

#### Step 1.4: Dependencies (`backend/requirements.txt`)
```
Flask==3.0.0
Flask-CORS==4.0.0
```

---

### Phase 2: Frontend Development

#### Step 2.1: HTML Structure (`frontend/index.html`)
```html
Structure:
- <head> with meta tags, title, CSS link
- <body>
  - Main container
    - Left section (calculator)
      - Display area
        - Expression display
        - Result display
      - Mode toggle buttons
      - Memory buttons
      - Basic button pad
      - Scientific button pad (hidden by default)
    - Right section (history sidebar)
      - History title
      - History list
      - Clear all button
  - Script tags (api.js, app.js)
```

**Buttons needed:**
- Numbers: 0-9
- Operators: +, -, ×, ÷
- Functions: =, C, CE, DEL, ±, .
- Scientific: sin, cos, tan, asin, acos, atan, log, ln, √, x², x³, x^y, 1/x, !, abs, (, ), π, e, e^x
- Memory: MC, MR, M+, M-
- Mode: Basic, Scientific

#### Step 2.2: Styling (`frontend/styles.css`)
```css
Sections:
1. CSS Reset & Base Styles
2. Layout (Grid/Flexbox)
   - Main container
   - Calculator section (70%)
   - History sidebar (30%)
3. Display Area
   - Expression line styling
   - Result line styling
   - Error state styling
4. Buttons
   - Base button styles
   - Number buttons
   - Operator buttons
   - Special buttons (C, CE, DEL)
   - Equals button
   - Scientific buttons
   - Memory buttons
   - Mode toggle buttons
5. History Sidebar
   - History item cards
   - Delete button
   - Clear all button
   - Hover effects
6. Responsive Media Queries
7. Animations
   - Button clicks
   - Error shake
   - History slide-in
```

**Color Palette:**
```css
:root {
  --bg-color: #f5f5f5;
  --calculator-bg: #ffffff;
  --display-bg: #f9f9f9;
  --text-color: #333333;
  --button-bg: #ffffff;
  --button-border: #e0e0e0;
  --operator-color: #2196F3;
  --equals-bg: #2196F3;
  --equals-text: #ffffff;
  --delete-color: #d32f2f;
  --delete-bg: #ffebee;
  --scientific-bg: #e3f2fd;
  --scientific-text: #1976D2;
}
```

#### Step 2.3: API Communication (`frontend/api.js`)
```javascript
Functions:
- const API_BASE = 'http://localhost:5000/api'

- async calculate(expression, operationType)
  - POST /api/calculate
  - Return result or error

- async getHistory()
  - GET /api/history
  - Return array of calculations

- async deleteCalculation(id)
  - DELETE /api/history/:id
  - Return success

- async clearHistory()
  - DELETE /api/history
  - Return success

Error handling:
- Network errors
- Server errors
- Timeout handling
```

#### Step 2.4: Calculator Logic (`frontend/app.js`)
```javascript
State Management:
- currentExpression = ""
- currentResult = ""
- isScientificMode = false
- memoryValue = 0
- isError = false

Functions:

1. Display Management
   - updateDisplay()
   - showError(message)
   - clearError()

2. Input Handling
   - handleNumberClick(num)
   - handleOperatorClick(op)
   - handleFunctionClick(func)
   - handleDecimalClick()
   - handleNegateClick()
   - handleClearClick()
   - handleClearEntryClick()
   - handleDeleteClick()
   - handleEqualsClick()

3. Scientific Functions
   - handleSin()
   - handleCos()
   - handleTan()
   - handleLog()
   - handleLn()
   - handleSqrt()
   - handleSquare()
   - handlePower()
   - handleFactorial()
   - handleAbsolute()
   - handlePi()
   - handleE()
   - ... etc

4. Memory Functions
   - handleMemoryClear()
   - handleMemoryRecall()
   - handleMemoryAdd()
   - handleMemorySubtract()

5. Mode Switching
   - toggleScientificMode()
   - showScientificButtons()
   - hideScientificButtons()

6. History Management
   - loadHistory()
   - displayHistory(calculations)
   - handleHistoryItemClick(calculation)
   - handleHistoryDelete(id)
   - handleHistoryClearAll()

7. Keyboard Support
   - handleKeyPress(event)
   - Map keys to functions

8. API Integration
   - calculateExpression()
     - Call api.calculate()
     - Update display
     - Reload history

9. Initialization
   - initializeApp()
   - attachEventListeners()
   - loadHistory()
```

---

### Phase 3: Integration & Testing

#### Step 3.1: Backend Testing
```bash
# Test each endpoint with curl:

# Test calculate
curl -X POST http://localhost:5000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{"expression": "2 + 2", "operation_type": "arithmetic"}'

# Test history
curl http://localhost:5000/api/history

# Test delete
curl -X DELETE http://localhost:5000/api/history/1

# Test clear all
curl -X DELETE http://localhost:5000/api/history
```

#### Step 3.2: Frontend-Backend Integration
- Start Flask server (port 5000)
- Open index.html in browser
- Test all operations
- Verify history updates
- Check error handling

#### Step 3.3: Edge Cases to Test
- Division by zero: `5 / 0`
- Square root of negative: `sqrt(-1)`
- Log of zero: `log(0)`
- Factorial of large number: `100!`
- Very long expressions
- Rapid clicking
- Invalid syntax
- Empty expression calculation

---

### Phase 4: Polish & Documentation

#### Step 4.1: README.md
```markdown
Sections:
- Project description
- Features list
- Technology stack
- Prerequisites
- Installation steps
  - Backend setup
  - Frontend setup
- Running the application
- Usage guide
- API documentation
- File structure
- Contributing
- License
```

#### Step 4.2: Final Touches
- Code comments
- Console.log cleanup
- Error message refinement
- UI polish
- Cross-browser testing

#### Step 4.3: .gitignore
```
# Python
__pycache__/
*.pyc
*.pyo
*.db
venv/
env/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

## Development Order (Recommended)

### Day 1: Backend Foundation
1. Create backend/ directory structure
2. Write requirements.txt
3. Implement database.py
4. Implement calculator.py
5. Test calculator functions in Python REPL

### Day 2: Backend API
6. Implement app.py (Flask routes)
7. Test with curl
8. Verify database operations
9. Test error handling

### Day 3: Frontend Structure
10. Create frontend/ directory
11. Write index.html (complete structure)
12. Write styles.css (complete styling)
13. Write api.js
14. Test API calls in browser console

### Day 4: Frontend Logic
15. Write app.js (core calculator logic)
16. Implement basic mode
17. Test arithmetic operations
18. Implement scientific mode
19. Test scientific operations

### Day 5: Integration & History
20. Connect to backend API
21. Implement history sidebar
22. Test full workflow
23. Add keyboard support
24. Bug fixes

### Day 6: Polish
25. Error handling improvements
26. UI refinements
27. Write README.md
28. Final testing
29. Documentation review

---

## Testing Checklist

### Backend Tests
- [ ] Database creates successfully
- [ ] Calculations save to database
- [ ] History retrieves latest 10
- [ ] Delete works for single entry
- [ ] Clear all works
- [ ] All math operations correct
- [ ] Error handling works
- [ ] CORS configured properly

### Frontend Tests
- [ ] All buttons clickable
- [ ] Display updates correctly
- [ ] Mode toggle works
- [ ] Scientific functions work
- [ ] Memory functions work
- [ ] History loads on page load
- [ ] History items clickable
- [ ] Delete history item works
- [ ] Clear all history works
- [ ] Keyboard shortcuts work
- [ ] Responsive design works

### Integration Tests
- [ ] Calculate and save works
- [ ] History updates after calculation
- [ ] Errors display properly
- [ ] Network errors handled
- [ ] Server errors handled
- [ ] All scientific operations in degrees
- [ ] Expression building works correctly
- [ ] Result displays correctly

---

## Known Challenges & Solutions

### Challenge 1: Expression Parsing
**Problem**: User builds "2 + 3 × 5", needs to maintain order of operations
**Solution**: Use Python's `eval()` with safety checks OR implement expression parser

### Challenge 2: Degrees vs Radians
**Problem**: Math libraries use radians by default
**Solution**: Convert degrees to radians before calculation, convert back after

### Challenge 3: CORS Issues
**Problem**: Browser blocks API calls from file://
**Solution**:
- Configure Flask-CORS to allow all origins (development)
- OR serve HTML with simple HTTP server (python -m http.server)

### Challenge 4: Button Layout
**Problem**: Scientific mode adds many buttons, layout can break
**Solution**: Use CSS Grid for fixed layout, show/hide sections

---

## Success Metrics

Project is complete when:
- ✅ Backend runs without errors
- ✅ Frontend loads without console errors
- ✅ All 20+ operations work correctly
- ✅ History saves and loads
- ✅ UI matches design specification
- ✅ Keyboard support works
- ✅ Error handling graceful
- ✅ Code is clean and documented
- ✅ README is complete

---

**Plan Version**: 1.0
**Estimated Lines of Code**: ~1500
**Estimated Time**: 6-8 hours (experienced developer)
**Last Updated**: 2026-01-11
