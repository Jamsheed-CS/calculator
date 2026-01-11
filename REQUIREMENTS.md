# Calculator App - Requirements Document

## Project Overview
A full-stack calculator application with scientific operations, server-side calculation validation, and SQLite-based history storage.

---

## Technology Stack

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (light theme)
- **Vanilla JavaScript** - Logic and interactions

### Backend
- **Python 3.x** - Runtime
- **Flask** - Web framework
- **SQLite3** - Database

### Development Environment
- Local development only
- No authentication required
- No testing framework (for now)

---

## Functional Requirements

### 1. Arithmetic Operations
- Addition (+)
- Subtraction (-)
- Multiplication (×)
- Division (÷)
- Modulo (%)
- Percentage calculations

### 2. Scientific Operations
- **Trigonometric** (Degrees mode):
  - sin(x), cos(x), tan(x)
  - asin(x), acos(x), atan(x)
- **Logarithmic**:
  - log(x) - base 10
  - ln(x) - natural logarithm
- **Exponential**:
  - x² - square
  - x³ - cube
  - x^y - power
  - √x - square root
  - ∛x - cube root
  - e^x - exponential
- **Constants**:
  - π (pi) - 3.14159...
  - e (Euler's number) - 2.71828...
- **Other**:
  - n! - factorial
  - |x| - absolute value
  - 1/x - reciprocal

### 3. Memory Functions
- MC - Memory Clear
- MR - Memory Recall
- M+ - Add to memory
- M- - Subtract from memory

### 4. Display Features
- **Expression Display**: Show the full expression being built (e.g., "2 + 3 × 5")
- **Result Display**: Show the calculated result
- **Error Messages**: Clear error display for invalid operations

### 5. History Management
- Save all calculations to database
- Display latest 10 entries in right sidebar
- Each entry shows: expression, result, timestamp
- Click to reuse previous calculation
- Delete individual entries
- Clear all history

### 6. User Interface
- **Theme**: Light theme (clean, professional)
- **Layout**:
  - Main calculator in center/left
  - History sidebar on right
  - Toggle between Basic/Scientific modes
- **Responsive**: Works on desktop (mobile optimization optional)

### 7. Input Methods
- Mouse clicks on buttons
- Keyboard support (numbers, operators, Enter for equals)

### 8. Error Handling
- Division by zero
- Invalid mathematical operations
- Domain errors (e.g., sqrt of negative, log of zero)
- Clear error messages to user

---

## Technical Specifications

### Database Schema

```sql
CREATE TABLE calculations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expression TEXT NOT NULL,
    result REAL NOT NULL,
    operation_type TEXT CHECK(operation_type IN ('arithmetic', 'scientific')),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### API Endpoints

#### POST /api/calculate
Calculate an expression
```json
Request:
{
  "expression": "sin(30) + 5",
  "operation_type": "scientific"
}

Response:
{
  "success": true,
  "expression": "sin(30) + 5",
  "result": 5.5,
  "id": 1
}

Error Response:
{
  "success": false,
  "error": "Division by zero"
}
```

#### GET /api/history
Get calculation history (latest 10)
```json
Response:
{
  "success": true,
  "calculations": [
    {
      "id": 5,
      "expression": "2 + 2",
      "result": 4,
      "operation_type": "arithmetic",
      "timestamp": "2026-01-11 14:30:00"
    },
    ...
  ]
}
```

#### DELETE /api/history/:id
Delete specific calculation
```json
Response:
{
  "success": true,
  "message": "Calculation deleted"
}
```

#### DELETE /api/history
Clear all history
```json
Response:
{
  "success": true,
  "message": "All history cleared",
  "deleted_count": 10
}
```

---

## Project Structure

```
calculator/
├── backend/
│   ├── app.py              # Flask application & routes
│   ├── calculator.py       # Calculation engine logic
│   ├── database.py         # SQLite database operations
│   ├── requirements.txt    # Python dependencies
│   └── calculator.db       # SQLite database (created on first run)
│
├── frontend/
│   ├── index.html         # Main HTML structure
│   ├── styles.css         # Styling (light theme)
│   ├── app.js            # Calculator logic
│   └── api.js            # API communication
│
├── README.md             # Setup and usage instructions
├── REQUIREMENTS.md       # This file
└── .gitignore           # Git ignore file
```

---

## Implementation Details

### Calculator Display
- **Expression Line**: Shows "2 + 3 × 5" as user builds it
- **Result Line**: Shows "17" after calculation
- Both lines visible simultaneously

### Scientific Mode
- Toggle button switches between Basic/Scientific layouts
- Basic mode: 0-9, +, -, ×, ÷, =, C, CE, ±
- Scientific mode: Adds sin, cos, tan, log, ln, √, x², x^y, π, e, etc.

### Trigonometry
- All trigonometric functions operate in **DEGREES**
- sin(30) = 0.5
- cos(60) = 0.5
- tan(45) = 1.0

### History Sidebar
- Fixed right sidebar (300px width)
- Shows latest 10 calculations
- Most recent at top
- Each entry clickable to reuse
- Delete button (×) on each entry
- "Clear All" button at bottom

---

## Python Dependencies

```
Flask==3.0.0
Flask-CORS==4.0.0
```

---

## Development Phases

### Phase 1: Backend Development
1. Setup Flask project structure
2. Create SQLite database schema
3. Implement calculator.py (all math operations)
4. Build REST API endpoints
5. Test API with curl

### Phase 2: Frontend Development
6. Create HTML structure
7. Style with CSS (light theme, responsive)
8. Implement JavaScript calculator logic
9. Add API integration
10. Build history sidebar

### Phase 3: Integration & Polish
11. Connect frontend to backend
12. Add keyboard support
13. Error handling and validation
14. Final UI/UX improvements

---

## Non-Functional Requirements

### Performance
- Calculations should respond in < 100ms
- UI should be responsive and smooth

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- No IE11 support needed

### Code Quality
- Clean, readable code
- Comments for complex logic
- Modular structure

---

## Future Enhancements (Not in Scope)
- User authentication
- Multiple user sessions
- Graph plotting
- Unit conversion
- Dark theme toggle
- Mobile app version
- Export history to CSV
- Advanced scientific functions (matrices, complex numbers)

---

## Success Criteria

The project will be considered complete when:
1. ✓ All arithmetic operations work correctly
2. ✓ All scientific operations work correctly (in degrees)
3. ✓ History saves to database and displays latest 10
4. ✓ UI is clean, functional, and light-themed
5. ✓ Backend API handles all requests correctly
6. ✓ Error handling works for common edge cases
7. ✓ Keyboard input works for basic operations
8. ✓ Memory functions work correctly

---

**Document Version**: 1.0
**Last Updated**: 2026-01-11
**Status**: Ready for Development
