"""
Flask REST API for Calculator App
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import calculator
import database

app = Flask(__name__)
# Enable CORS for all routes (allow frontend to communicate)
CORS(app)

# Initialize database on startup
database.init_db()

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Calculator API',
        'version': '1.0',
        'endpoints': {
            'POST /api/calculate': 'Calculate an expression',
            'GET /api/history': 'Get calculation history',
            'DELETE /api/history/<id>': 'Delete specific calculation',
            'DELETE /api/history': 'Clear all history'
        }
    })

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """
    Calculate a mathematical expression

    Request body:
    {
        "expression": "2 + 2",
        "operation_type": "arithmetic"  (optional)
    }

    Response:
    {
        "success": true,
        "expression": "2 + 2",
        "result": 4.0,
        "id": 1
    }
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400

        expression = data.get('expression', '').strip()

        if not expression:
            return jsonify({
                'success': False,
                'error': 'Expression is required'
            }), 400

        # Calculate the result
        result = calculator.evaluate_expression(expression)

        # Determine operation type (or use provided one)
        operation_type = data.get('operation_type')
        if not operation_type:
            operation_type = calculator.determine_operation_type(expression)

        # Save to database
        calculation_id = database.save_calculation(expression, result, operation_type)

        return jsonify({
            'success': True,
            'expression': expression,
            'result': result,
            'operation_type': operation_type,
            'id': calculation_id
        })

    except calculator.CalculatorError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """
    Get calculation history (latest 10 by default)

    Query parameters:
    - limit: Number of records to retrieve (default: 10)

    Response:
    {
        "success": true,
        "calculations": [
            {
                "id": 5,
                "expression": "2 + 2",
                "result": 4.0,
                "operation_type": "arithmetic",
                "timestamp": "2026-01-11 14:30:00"
            },
            ...
        ]
    }
    """
    try:
        limit = request.args.get('limit', default=10, type=int)

        # Limit maximum to 100
        if limit > 100:
            limit = 100

        calculations = database.get_history(limit)

        return jsonify({
            'success': True,
            'calculations': calculations,
            'count': len(calculations)
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/api/history/<int:calculation_id>', methods=['DELETE'])
def delete_calculation(calculation_id):
    """
    Delete a specific calculation by ID

    Response:
    {
        "success": true,
        "message": "Calculation deleted"
    }
    """
    try:
        deleted = database.delete_calculation(calculation_id)

        if deleted:
            return jsonify({
                'success': True,
                'message': 'Calculation deleted'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Calculation not found'
            }), 404

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/api/history', methods=['DELETE'])
def clear_history():
    """
    Clear all calculation history

    Response:
    {
        "success": true,
        "message": "All history cleared",
        "deleted_count": 15
    }
    """
    try:
        count = database.clear_history()

        return jsonify({
            'success': True,
            'message': 'All history cleared',
            'deleted_count': count
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("=" * 60)
    print("Calculator API Server")
    print("=" * 60)
    print("Starting Flask server on http://localhost:5000")
    print("\nAvailable endpoints:")
    print("  POST   /api/calculate")
    print("  GET    /api/history")
    print("  DELETE /api/history/<id>")
    print("  DELETE /api/history")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)

    app.run(host='0.0.0.0', port=5000, debug=True)
