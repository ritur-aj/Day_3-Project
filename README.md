# 🍕 Welcome to Pizza Delivery

A beginner-friendly Python command-line project that combines a colorful terminal startup animation with a simple pizza-ordering and bill-calculation program.

## ✨ Features

- Animated project welcome screen and loading bar.
- Colored terminal output using ANSI escape codes.
- Pizza size selection: Small, Medium, or Large.
- Optional pepperoni and extra cheese.
- Automatic total calculation and bill display.
- Uses only Python's built-in modules; no third-party packages are required.

## 💵 Menu and Pricing

The menu displayed by the program is:

| Item | Price |
|---|---:|
| Small pizza (S) | $8 |
| Medium pizza (M) | $10 |
| Large pizza (L) | $12 |
| Pepperoni | +$2 |
| Extra cheese | +$1 |

**Important:** The current code's calculation section uses `$20` for Medium and `$25` for Large, even though the menu displays `$10` and `$12`. To make the bill match the menu, change `price += 20` to `price += 10` in the Medium branch and `price += 25` to `price += 12` in the Large branch.

## 🧰 Requirements

- Python 3.8 or newer (a recent Python 3 version is recommended).
- A terminal or command prompt.

No additional libraries need to be installed. The startup animation uses Python's built-in `os`, `sys`, and `time` modules; the pizza calculator itself uses standard Python input, conditionals, and arithmetic.

## 🚀 Getting Started

1. Save the Python code in a file named `pizza_delivery.py`.
2. Open a terminal in the folder containing that file.
3. Run the program:

   **Windows**
   ```bash
   python pizza_delivery.py
   ```

   **Linux / macOS**
   ```bash
   python3 pizza_delivery.py
   ```

4. After the welcome animation, enter the pizza size and answer the add-on questions.

## 🧾 Example Order

For a Small pizza with pepperoni and extra cheese:

```text
Enter size of pizza. S / M / L  : S
Do you want papperoni on your pizza ? Y or N  : Y
Do you wnat extra chease ? y or N  : Y
Your total bill is = $11
```

Calculation: `$8` + `$2` for pepperoni + `$1` for extra cheese = **$11**.

## 🕹️ How to Use It

1. Choose a size: `S`, `M`, or `L`.
2. Enter `Y` or `N` for pepperoni.
3. Enter `Y` or `N` for extra cheese.
4. Read the displayed total.

Inputs are converted to title case, so lowercase answers such as `s`, `y`, and `n` are accepted too. The current program does not validate unexpected answers; it may calculate an incorrect or zero total if an invalid option is entered.

## 📁 Project Structure

```text
pizza-delivery/
└── pizza_delivery.py
```

## 🧠 Concepts Practiced

- Variables and constants
- `input()` and `print()`
- Conditional logic with `if`, `elif`, and `else`
- Arithmetic and running totals
- Functions
- String formatting
- Basic terminal animation and ANSI colors

## 🔧 Possible Improvements

- Correct the Medium and Large price calculations.
- Validate pizza size and `Y`/`N` answers.
- Simplify the add-on pricing logic to avoid repeating the same conditions for each size.
- Fix spelling in prompts, such as “pepperoni” and “cheese.”
- Add order summaries and support multiple pizzas in one order.

## 👨‍💻 Developer

**Ritu Raj**  
**Role:** Data Science & AI Developer  
**Version:** v1.0.0

---

*Code • Learn • Build • Improve • Repeat* 🚀
