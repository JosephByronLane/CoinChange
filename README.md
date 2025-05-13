A project I did a while ago.

Its basically a Json that contains the amount of coins that a machine has, and based on that it calculates how many coins the machine should return given a certain input value (money).

# Coin Change Solver

A simple Python script that calculates the optimal way to give change using a limited number of coins. It reads and updates a JSON file (`coin-change.json`) containing the current coin inventory.

## Project Structure

* **main.py**: The main Python script with functions to load coin data, compute optimal change, and update inventory.
* **coin-change.json**: Stores the available number of coins for each denomination (keys are coin values, values are counts).

## Setup

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Ensure `main.py` and `coin-change.json` are in the same directory.

## Usage

By default, the script computes change for 6 units of currency (e.g., dollars) when you run it:

```bash
python main.py
```

To calculate change for a different amount, edit the last line of `main.py`:

```python
# Change the first argument to set the payment amount,
# and the second argument to set a maximum allowed change.
recursive(6, 1000)
```

* **First parameter (`amntpay`)**: The amount to return as change.
* **Second parameter (`maxchange`)**: A safety cap on the total change (not usually reached).

## JSON Inventory Format

The `coin-change.json` file should contain a JSON object mapping coin values to their available counts:

```json
{
  "1": 84,
  "2": 89,
  "5": 27
}
```

* **Keys**: Coin denominations (integers).
* **Values**: Number of coins available for that denomination.
