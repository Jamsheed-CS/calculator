# Calculator App - UI Design Specification

## Visual Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Calculator App                                │
├─────────────────────────────────────────┬───────────────────────────┤
│                                         │   HISTORY (Latest 10)     │
│  ┌───────────────────────────────────┐  │  ┌─────────────────────┐ │
│  │ Expression: 2 + 3 × 5             │  │  │ sin(30) + 5         │ │
│  │ Result: 17                        │  │  │ = 5.5               │ │
│  └───────────────────────────────────┘  │  │ 14:30:00        [×] │ │
│                                         │  ├─────────────────────┤ │
│  [Basic] [Scientific]  [MC][MR][M+][M-] │  │ 10 + 20             │ │
│                                         │  │ = 30                │ │
│  ┌─────────────────────────────────┐   │  │ 14:28:15        [×] │ │
│  │ [ 7 ]  [ 8 ]  [ 9 ]  [ ÷ ]  [DEL]│   │  ├─────────────────────┤ │
│  │ [ 4 ]  [ 5 ]  [ 6 ]  [ × ]  [ C ]│   │  │ sqrt(16)            │ │
│  │ [ 1 ]  [ 2 ]  [ 3 ]  [ - ]  [CE ]│   │  │ = 4                 │ │
│  │ [ 0 ]  [ . ]  [±]   [ + ]  [ = ]│   │  │ 14:25:03        [×] │ │
│  └─────────────────────────────────┘   │  ├─────────────────────┤ │
│                                         │  │ ...                 │ │
│  SCIENTIFIC MODE (when toggled):        │  │                     │ │
│  ┌─────────────────────────────────┐   │  │                     │ │
│  │ [sin] [cos] [tan] [π]  [e]      │   │  │                     │ │
│  │ [asin][acos][atan][log][ln]     │   │  │                     │ │
│  │ [ √ ] [x²] [x³] [x^y][1/x]      │   │  │                     │ │
│  │ [ ! ] [abs] [ ( ] [ ) ] [e^x]   │   │  │                     │ │
│  └─────────────────────────────────┘   │  │                     │ │
│                                         │  │  [Clear All]        │ │
│                                         │  └─────────────────────┘ │
└─────────────────────────────────────────┴───────────────────────────┘
```

---

## Color Scheme (Light Theme)

### Primary Colors
- **Background**: #f5f5f5 (light gray)
- **Calculator Body**: #ffffff (white)
- **Display**: #f9f9f9 (very light gray)
- **Text**: #333333 (dark gray)

### Button Colors
- **Number Buttons**: #ffffff with #e0e0e0 border
- **Operator Buttons**: #f0f0f0 with #2196F3 text (blue)
- **Special Buttons (C, CE, DEL)**: #ffebee with #d32f2f text (red)
- **Equals Button**: #2196F3 with white text (blue)
- **Scientific Buttons**: #e3f2fd with #1976D2 text (light blue)

### Accents
- **Hover State**: Lighten by 10%
- **Active State**: Darken by 10%
- **Border**: #e0e0e0 (light gray)
- **Shadow**: 0 2px 4px rgba(0,0,0,0.1)

---

## Component Breakdown

### 1. Display Area
```
┌─────────────────────────────────────┐
│ Expression: 2 + 3 × 5               │ ← Expression being built
│ Result: 17                          │ ← Calculated result
└─────────────────────────────────────┘

- Height: 80px
- Padding: 15px
- Font: Monospace (Consolas, Monaco)
- Expression font-size: 18px
- Result font-size: 32px (bold)
- Right-aligned text
```

### 2. Mode Switcher
```
[Basic Mode] [Scientific Mode]

- Toggle buttons
- Active mode highlighted
- Basic mode: default
- Scientific mode: shows extra buttons
```

### 3. Memory Buttons
```
[MC] [MR] [M+] [M-]

- Small buttons (40px × 30px)
- Grouped separately
- Gray background
```

### 4. Basic Button Pad (4×5 grid)
```
Row 1: 7    8    9    ÷    DEL
Row 2: 4    5    6    ×    C
Row 3: 1    2    3    -    CE
Row 4: 0    .    ±    +    =

- Button size: 60px × 60px
- Spacing: 8px gap
- Rounded corners: 4px
```

### 5. Scientific Button Pad (5×4 grid)
```
Row 1: sin   cos   tan   π     e
Row 2: asin  acos  atan  log   ln
Row 3: √     x²    x³    x^y   1/x
Row 4: !     abs   (     )     e^x

- Button size: 60px × 50px
- Only visible in Scientific Mode
- Light blue theme
```

### 6. History Sidebar
```
┌───────────────────────┐
│   HISTORY             │
├───────────────────────┤
│ Expression            │
│ = Result              │
│ Timestamp        [×]  │ ← Delete button
├───────────────────────┤
│ ...                   │
│                       │
│                       │
│  [Clear All]          │ ← Bottom button
└───────────────────────┘

- Width: 300px
- Fixed right position
- Scrollable if > 10 entries
- Each entry:
  - White background
  - Gray border
  - Hover effect
  - Clickable to reuse
```

---

## Responsive Behavior

### Desktop (>1200px)
- Calculator: 600px wide
- History sidebar: 300px wide
- Side-by-side layout

### Tablet (768px - 1200px)
- Calculator: 500px wide
- History sidebar: 250px wide
- Side-by-side layout (compact)

### Mobile (<768px)
- Calculator: Full width
- History: Below calculator OR collapsible panel
- Stacked layout

---

## Button Interactions

### Hover States
- Slight background color change
- Cursor: pointer
- Subtle scale (1.02)

### Active/Click States
- Darker background
- Scale down slightly (0.98)
- Quick transition (100ms)

### Disabled States
- Opacity: 0.5
- Cursor: not-allowed

---

## Typography

### Fonts
- **Display Numbers**: 'Courier New', Consolas, monospace
- **Buttons**: 'Segoe UI', Arial, sans-serif
- **History**: 'Arial', sans-serif

### Sizes
- Display Expression: 18px
- Display Result: 32px (bold)
- Button Text: 16px
- History Text: 14px
- History Timestamp: 12px (gray)

---

## Animations & Transitions

### Button Clicks
```css
transition: all 0.1s ease;
```

### Mode Switch
```css
transition: opacity 0.3s ease;
/* Fade in/out scientific buttons */
```

### History Updates
```css
/* New entry slides in from top */
animation: slideDown 0.3s ease;
```

### Error Display
```css
/* Display shakes on error */
animation: shake 0.5s ease;
```

---

## Error Display

### Error States
```
┌─────────────────────────────────────┐
│ Expression: 5 / 0                   │
│ Error: Division by zero             │ ← Red text
└─────────────────────────────────────┘

- Result area turns red (#ffebee background)
- Error text in red (#d32f2f)
- Shake animation
- Auto-clear on next input
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| 0-9 | Number input |
| + - * / | Operators |
| Enter | Calculate (=) |
| Backspace | Delete last |
| Escape | Clear |
| . | Decimal point |

---

## Accessibility

- **Tab Navigation**: All buttons focusable
- **Focus Indicators**: Clear blue outline
- **ARIA Labels**: All buttons labeled
- **Keyboard Support**: Full keyboard control
- **Contrast Ratio**: WCAG AA compliant (4.5:1)

---

## Loading States

### On History Load
```
┌───────────────────────┐
│   HISTORY             │
├───────────────────────┤
│   Loading...          │
│   [spinner]           │
└───────────────────────┘
```

### On Calculation
- Button shows loading state
- Prevents double-submission

---

## Example Screenshots (Text Representation)

### Basic Mode
```
┌────────────────────────────────────────────────────┐
│              CALCULATOR                            │
│                                                    │
│  Expression: 15 + 25                               │
│  Result: 40                                        │
│                                                    │
│  [Basic ✓] [Scientific]    [MC][MR][M+][M-]       │
│                                                    │
│    7     8     9     ÷    DEL                      │
│    4     5     6     ×     C                       │
│    1     2     3     -    CE                       │
│    0     .     ±     +     =                       │
│                                                    │
└────────────────────────────────────────────────────┘
```

### Scientific Mode
```
┌────────────────────────────────────────────────────┐
│              CALCULATOR                            │
│                                                    │
│  Expression: sin(30) + 10                          │
│  Result: 10.5                                      │
│                                                    │
│  [Basic] [Scientific ✓]    [MC][MR][M+][M-]       │
│                                                    │
│   sin   cos   tan    π     e                       │
│   asin  acos  atan  log   ln                       │
│    √     x²    x³   x^y  1/x                       │
│    !    abs    (     )   e^x                       │
│                                                    │
│    7     8     9     ÷    DEL                      │
│    4     5     6     ×     C                       │
│    1     2     3     -    CE                       │
│    0     .     ±     +     =                       │
│                                                    │
└────────────────────────────────────────────────────┘
```

---

**Design Version**: 1.0
**Last Updated**: 2026-01-11
**Status**: Ready for Implementation
