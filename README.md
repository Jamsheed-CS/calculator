# Scientific Calculator App

A full-stack scientific calculator with arithmetic and scientific operations, server-side calculation validation, and SQLite-based history storage.

## Features

### Calculator Operations
- **Arithmetic**: Addition (+), Subtraction (-), Multiplication (×), Division (÷), Modulo (%)
- **Scientific**:
  - Trigonometric (Degrees): sin, cos, tan, asin, acos, atan
  - Logarithmic: log (base 10), ln (natural log)
  - Exponential: x², x³, x^y, √x, ∛x, e^x
  - Constants: π (pi), e (Euler's number)
  - Other: n! (factorial), |x| (absolute), 1/x (reciprocal)
- **Memory Functions**: MC (clear), MR (recall), M+ (add), M- (subtract)
- **History**: View, reuse, and delete past calculations (latest 10 displayed)

### User Interface
- Clean, light-themed design
- Expression display shows full calculation as you type
- Toggle between Basic and Scientific modes
- Right sidebar with calculation history
- Keyboard support for quick input
- Responsive design (works on desktop and mobile)

## Technology Stack

### Frontend
- HTML5
- CSS3 (Light theme)
- Vanilla JavaScript

### Backend
- Python 3.x
- Flask (REST API)
- SQLite3 (Database)

## Project Structure

```
calculator/
├── backend/
│   ├── app.py              # Flask REST API
│   ├── calculator.py       # Mathematical operations engine
│   ├── database.py         # SQLite database operations
│   ├── requirements.txt    # Python dependencies
│   └── calculator.db       # SQLite database (created on first run)
├── frontend/
│   ├── index.html         # Main HTML structure
│   ├── styles.css         # Styling (light theme)
│   ├── app.js            # Calculator logic
│   └── api.js            # API communication
├── README.md             # This file
├── REQUIREMENTS.md       # Detailed requirements
├── DESIGN.md            # UI/UX specifications
└── IMPLEMENTATION_PLAN.md # Development roadmap
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd calculator
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# The database will be created automatically when you run the app
```

### 3. Start the Backend Server

```bash
# From the backend directory
python app.py
```

You should see:
```
============================================================
Calculator API Server
============================================================
Starting Flask server on http://localhost:5000

Available endpoints:
  POST   /api/calculate
  GET    /api/history
  DELETE /api/history/<id>
  DELETE /api/history

Press Ctrl+C to stop the server
============================================================
```

The backend will run on `http://localhost:5000`

### 4. Open the Frontend

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Option 1: Open directly in browser (may have CORS issues)
# Just open index.html in your browser

# Option 2: Use Python's built-in HTTP server (recommended)
python -m http.server 8000
```

Then open your browser and navigate to:
- `http://localhost:8000` (if using Python HTTP server)
- Or directly open `frontend/index.html` in your browser

## Usage Guide

### Basic Mode

1. Click number buttons (0-9) to enter numbers
2. Click operators (+, -, ×, ÷) to perform operations
3. Click `=` or press `Enter` to calculate
4. Use `C` to clear all, `CE` to clear entry, `DEL` to delete last character

### Scientific Mode

1. Click the "Scientific" button to reveal scientific functions
2. Available functions:
   - **Trigonometric**: sin(30), cos(60), tan(45) - all in degrees
   - **Logarithmic**: log(100), ln(2.718)
   - **Powers**: Use x², x³, or x^y buttons
   - **Roots**: √x for square root
   - **Constants**: π, e buttons
   - **Other**: n!, |x|, 1/x, e^x

### Memory Functions

1. Perform a calculation to get a result
2. Click `M+` to add result to memory
3. Click `M-` to subtract result from memory
4. Click `MR` to recall memory value
5. Click `MC` to clear memory

### History

- All calculations are automatically saved
- Latest 10 calculations appear in the right sidebar
- Click any history item to reuse that calculation
- Click the `×` button on an item to delete it
- Click "Clear All" to delete entire history

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| 0-9 | Number input |
| +, -, *, / | Operators |
| Enter or = | Calculate |
| Backspace | Delete last character |
| Escape | Clear all |
| . | Decimal point |
| ( ) | Parentheses |

## API Endpoints

### POST /api/calculate
Calculate a mathematical expression

**Request:**
```json
{
  "expression": "sin(30) + 5",
  "operation_type": "scientific"
}
```

**Response:**
```json
{
  "success": true,
  "expression": "sin(30) + 5",
  "result": 5.5,
  "operation_type": "scientific",
  "id": 1
}
```

### GET /api/history
Get calculation history (latest 10)

**Response:**
```json
{
  "success": true,
  "calculations": [
    {
      "id": 1,
      "expression": "2 + 2",
      "result": 4.0,
      "operation_type": "arithmetic",
      "timestamp": "2026-01-11 14:30:00"
    }
  ],
  "count": 1
}
```

### DELETE /api/history/:id
Delete a specific calculation

### DELETE /api/history
Clear all history

## Examples

### Arithmetic
```
2 + 2 = 4
10 - 5 = 5
3 × 4 = 12
15 ÷ 3 = 5
```

### Scientific
```
sin(30) = 0.5
cos(60) = 0.5
tan(45) = 1.0
log(100) = 2
ln(2.718281828) ≈ 1
sqrt(16) = 4
2^3 = 8
5! = 120
```

### Complex Expressions
```
sin(30) + cos(60) = 1.0
sqrt(16) + log(100) = 6
(2 + 3) × 4 = 20
```

## Troubleshooting

### Backend Not Starting
- Ensure Python 3.7+ is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Check if port 5000 is available

### Frontend Can't Connect to Backend
- Ensure backend is running on `http://localhost:5000`
- Check browser console for CORS errors
- Try using Python HTTP server instead of opening HTML directly

### Calculations Not Working
- Check browser console for JavaScript errors
- Ensure backend is running and accessible
- Verify the expression syntax is correct

### Database Issues
- The database file `calculator.db` is created automatically
- If issues persist, delete `calculator.db` and restart the backend

## Development

### Running Tests

Backend calculator engine:
```bash
cd backend
python calculator.py
```

This will run test cases for all mathematical operations.

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

## Future Enhancements

- Unit conversion
- Graph plotting
- Dark theme toggle
- Export history to CSV
- Advanced scientific functions (matrices, complex numbers)
- User authentication
- Mobile app version

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues or questions, please open an issue in the repository