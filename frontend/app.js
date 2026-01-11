/**
 * Calculator App - Main Logic
 */

// State Management
let currentExpression = '';
let currentResult = '';
let isScientificMode = false;
let memoryValue = 0;
let isError = false;
let lastResult = null;

// DOM Elements
const expressionDisplay = document.getElementById('expressionDisplay');
const resultDisplay = document.getElementById('resultDisplay');
const scientificPad = document.getElementById('scientificPad');
const historyList = document.getElementById('historyList');

// Initialize app on load
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    updateDisplay();
    loadHistory();
    setupKeyboardSupport();
    console.log('Calculator initialized');
}

// ==================== Display Management ====================

function updateDisplay() {
    expressionDisplay.textContent = currentExpression || '0';
    resultDisplay.textContent = currentResult;

    // Remove error state if expression changed
    if (isError && currentExpression !== '') {
        clearError();
    }
}

function showError(message) {
    isError = true;
    currentResult = 'Error: ' + message;
    document.querySelector('.display').classList.add('error');
    document.querySelector('.display').classList.add('shake');

    updateDisplay();

    // Remove shake animation after it completes
    setTimeout(() => {
        document.querySelector('.display').classList.remove('shake');
    }, 500);
}

function clearError() {
    isError = false;
    document.querySelector('.display').classList.remove('error');
}

// ==================== Input Handling ====================

function numberClick(num) {
    if (isError) {
        clearAll();
    }
    currentExpression += num;
    updateDisplay();
}

function operatorClick(op) {
    if (isError) {
        clearAll();
    }

    // Prevent double operators
    const lastChar = currentExpression.slice(-1);
    if (['+', '-', '×', '÷', '^'].includes(lastChar)) {
        currentExpression = currentExpression.slice(0, -1);
    }

    currentExpression += op;
    updateDisplay();
}

function decimalClick() {
    if (isError) {
        clearAll();
    }

    // Check if current number already has a decimal
    const parts = currentExpression.split(/[\+\-×÷]/);
    const lastPart = parts[parts.length - 1];

    if (!lastPart.includes('.')) {
        currentExpression += '.';
        updateDisplay();
    }
}

function negateClick() {
    if (currentExpression) {
        // Simple implementation: wrap in parentheses with negative
        if (currentExpression.startsWith('-')) {
            currentExpression = currentExpression.substring(1);
        } else {
            currentExpression = '-' + currentExpression;
        }
        updateDisplay();
    }
}

function clearClick() {
    clearAll();
}

function clearAll() {
    currentExpression = '';
    currentResult = '';
    isError = false;
    clearError();
    updateDisplay();
}

function clearEntryClick() {
    // Clear only the current entry (last number/operator)
    currentExpression = currentExpression.slice(0, -1);
    updateDisplay();
}

function deleteClick() {
    currentExpression = currentExpression.slice(0, -1);
    updateDisplay();
}

// ==================== Scientific Functions ====================

function functionClick(func) {
    if (isError) {
        clearAll();
    }

    // Special handling for 1/x
    if (func === '1/') {
        currentExpression += '1/';
    } else {
        currentExpression += func;
    }

    updateDisplay();
}

function appendOperator(op) {
    if (isError) {
        clearAll();
    }
    currentExpression += op;
    updateDisplay();
}

function insertConstant(constant) {
    if (isError) {
        clearAll();
    }
    currentExpression += constant;
    updateDisplay();
}

// ==================== Memory Functions ====================

function memoryClick(operation) {
    switch(operation) {
        case 'MC':
            memoryValue = 0;
            console.log('Memory cleared');
            break;
        case 'MR':
            if (memoryValue !== 0) {
                currentExpression += memoryValue.toString();
                updateDisplay();
            }
            console.log('Memory recall:', memoryValue);
            break;
        case 'M+':
            if (lastResult !== null) {
                memoryValue += lastResult;
                console.log('Memory add:', memoryValue);
            }
            break;
        case 'M-':
            if (lastResult !== null) {
                memoryValue -= lastResult;
                console.log('Memory subtract:', memoryValue);
            }
            break;
    }
}

// ==================== Mode Switching ====================

function switchMode(mode) {
    if (mode === 'scientific') {
        isScientificMode = true;
        scientificPad.style.display = 'grid';
        document.getElementById('scientificModeBtn').classList.add('active');
        document.getElementById('basicModeBtn').classList.remove('active');
    } else {
        isScientificMode = false;
        scientificPad.style.display = 'none';
        document.getElementById('basicModeBtn').classList.add('active');
        document.getElementById('scientificModeBtn').classList.remove('active');
    }
}

// ==================== Calculation ====================

async function calculateClick() {
    if (!currentExpression || isError) {
        return;
    }

    try {
        // Show calculating state
        resultDisplay.textContent = 'Calculating...';

        // Call backend API
        const response = await calculate(currentExpression);

        if (response.success) {
            currentResult = '= ' + response.result;
            lastResult = response.result;
            updateDisplay();

            // Reload history to show new calculation
            await loadHistory();
        } else {
            showError(response.error || 'Calculation failed');
        }
    } catch (error) {
        showError(error.message);
    }
}

// ==================== History Management ====================

async function loadHistory() {
    try {
        const response = await getHistory(10);

        if (response.success && response.calculations) {
            displayHistory(response.calculations);
        }
    } catch (error) {
        console.error('Failed to load history:', error.message);
        // Don't show error to user, just log it
    }
}

function displayHistory(calculations) {
    if (!calculations || calculations.length === 0) {
        historyList.innerHTML = '<p class="history-empty">No calculations yet</p>';
        return;
    }

    historyList.innerHTML = '';

    calculations.forEach(calc => {
        const historyItem = createHistoryItem(calc);
        historyList.appendChild(historyItem);
    });
}

function createHistoryItem(calc) {
    const item = document.createElement('div');
    item.className = 'history-item';
    item.onclick = () => reuseCalculation(calc);

    const header = document.createElement('div');
    header.className = 'history-item-header';

    const expression = document.createElement('div');
    expression.className = 'history-expression';
    expression.textContent = calc.expression;

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'history-delete';
    deleteBtn.innerHTML = '×';
    deleteBtn.onclick = (e) => {
        e.stopPropagation();
        deleteHistoryItem(calc.id);
    };

    header.appendChild(expression);
    header.appendChild(deleteBtn);

    const result = document.createElement('div');
    result.className = 'history-result';
    result.textContent = '= ' + calc.result;

    const timestamp = document.createElement('div');
    timestamp.className = 'history-timestamp';
    timestamp.textContent = formatTimestamp(calc.timestamp);

    item.appendChild(header);
    item.appendChild(result);
    item.appendChild(timestamp);

    return item;
}

function reuseCalculation(calc) {
    currentExpression = calc.expression;
    currentResult = '= ' + calc.result;
    lastResult = calc.result;
    updateDisplay();
}

async function deleteHistoryItem(id) {
    try {
        await deleteCalculation(id);
        await loadHistory();
    } catch (error) {
        console.error('Failed to delete calculation:', error.message);
        showError('Failed to delete history item');
    }
}

async function clearAllHistory() {
    if (confirm('Are you sure you want to clear all history?')) {
        try {
            await clearHistory();
            await loadHistory();
        } catch (error) {
            console.error('Failed to clear history:', error.message);
            showError('Failed to clear history');
        }
    }
}

function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const calcDate = new Date(date.getFullYear(), date.getMonth(), date.getDate());

    const time = date.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
    });

    if (calcDate.getTime() === today.getTime()) {
        return 'Today ' + time;
    } else {
        return date.toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric'
        }) + ' ' + time;
    }
}

// ==================== Keyboard Support ====================

function setupKeyboardSupport() {
    document.addEventListener('keydown', function(event) {
        const key = event.key;

        // Prevent default for calculator keys
        if (/^[0-9\+\-\*\/\.\=\(\)]$/.test(key) ||
            key === 'Enter' ||
            key === 'Backspace' ||
            key === 'Escape') {
            event.preventDefault();
        }

        // Number keys
        if (/^[0-9]$/.test(key)) {
            numberClick(key);
        }
        // Operators
        else if (key === '+') {
            operatorClick('+');
        }
        else if (key === '-') {
            operatorClick('-');
        }
        else if (key === '*') {
            operatorClick('×');
        }
        else if (key === '/') {
            operatorClick('÷');
        }
        // Decimal point
        else if (key === '.') {
            decimalClick();
        }
        // Parentheses
        else if (key === '(') {
            appendOperator('(');
        }
        else if (key === ')') {
            appendOperator(')');
        }
        // Calculate
        else if (key === 'Enter' || key === '=') {
            calculateClick();
        }
        // Delete
        else if (key === 'Backspace') {
            deleteClick();
        }
        // Clear
        else if (key === 'Escape') {
            clearClick();
        }
    });
}

// ==================== Utility Functions ====================

console.log('Calculator app loaded successfully');
