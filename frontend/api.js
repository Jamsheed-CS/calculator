/**
 * API communication module for Calculator App
 * Handles all backend requests
 */

const API_BASE = 'http://localhost:5000/api';

/**
 * Calculate a mathematical expression
 * @param {string} expression - The expression to calculate
 * @param {string} operationType - 'arithmetic' or 'scientific'
 * @returns {Promise<Object>} Result object with success, result, id
 */
async function calculate(expression, operationType = null) {
    try {
        const response = await fetch(`${API_BASE}/calculate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                expression: expression,
                operation_type: operationType
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Calculation failed');
        }

        return data;
    } catch (error) {
        if (error.message.includes('fetch')) {
            throw new Error('Cannot connect to server. Make sure the backend is running on port 5000.');
        }
        throw error;
    }
}

/**
 * Get calculation history
 * @param {number} limit - Number of records to retrieve (default: 10)
 * @returns {Promise<Object>} Object with calculations array
 */
async function getHistory(limit = 10) {
    try {
        const response = await fetch(`${API_BASE}/history?limit=${limit}`);

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch history');
        }

        return data;
    } catch (error) {
        if (error.message.includes('fetch')) {
            throw new Error('Cannot connect to server. Make sure the backend is running on port 5000.');
        }
        throw error;
    }
}

/**
 * Delete a specific calculation from history
 * @param {number} id - The calculation ID to delete
 * @returns {Promise<Object>} Success response
 */
async function deleteCalculation(id) {
    try {
        const response = await fetch(`${API_BASE}/history/${id}`, {
            method: 'DELETE'
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to delete calculation');
        }

        return data;
    } catch (error) {
        if (error.message.includes('fetch')) {
            throw new Error('Cannot connect to server. Make sure the backend is running on port 5000.');
        }
        throw error;
    }
}

/**
 * Clear all calculation history
 * @returns {Promise<Object>} Success response with deleted count
 */
async function clearHistory() {
    try {
        const response = await fetch(`${API_BASE}/history`, {
            method: 'DELETE'
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to clear history');
        }

        return data;
    } catch (error) {
        if (error.message.includes('fetch')) {
            throw new Error('Cannot connect to server. Make sure the backend is running on port 5000.');
        }
        throw error;
    }
}
