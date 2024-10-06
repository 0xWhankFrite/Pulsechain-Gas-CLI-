import requests
import time
from collections import deque

# PulseChain RPC URL
rpc_url = "https://rpc-pulsechain.g4mm4.io"

# JSON-RPC payload to get the gas price
payload = {
    "jsonrpc": "2.0",
    "method": "eth_gasPrice",
    "params": [],
    "id": 1
}

# Lists to store gas prices for averaging
gas_prices = deque(maxlen=720)  # For hourly average (720 * 5 seconds = 1 hour)
five_min_prices = deque(maxlen=60)  # For 5-minute average (60 * 5 seconds = 5 minutes)

def get_gas_price():
    response = requests.post(rpc_url, json=payload)
    if response.status_code == 200:
        gas_price_wei = int(response.json().get('result', '0'), 16)
        gas_price_gwei = gas_price_wei / 10**9  # Convert to Gwei
        return gas_price_gwei
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def calculate_average(prices):
    if len(prices) == 0:
        return 0
    return sum(prices) / len(prices)

# Calculate different gas speeds
def calculate_gas_speeds(base_price):
    speeds = {
        'rapid': base_price * 2,         # 2x for rapid
        'fast': base_price * 1.5,        # 1.5x for fast
        'standard': base_price,          # base price for standard
        'slow': base_price * 0.8         # 0.8x for slow
    }
    return speeds

# Main loop
while True:
    gas_price = get_gas_price()
    if gas_price is not None:
        gas_prices.append(gas_price)
        five_min_prices.append(gas_price)

        # Calculate averages (standard price)
        five_min_avg = calculate_average(five_min_prices)
        one_hour_avg = calculate_average(gas_prices)

        # Calculate different gas speeds for current price
        speeds = calculate_gas_speeds(gas_price)

        # Clear screen and display the table
        print("\033c", end="")  # Clear the terminal screen
        print(f"{'Time':<20}{'Current Gas Price (Gwei)':<30}{'5-Minute Avg (Standard, Gwei)':<35}{'1-Hour Avg (Standard, Gwei)':<35}")
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S'):<20}{speeds['standard']:<30}{five_min_avg:<35}{one_hour_avg:<35}")
        print("\nGas Price Tiers (Current):")
        print(f"Rapid:    {speeds['rapid']:.2f} Gwei")
        print(f"Fast:     {speeds['fast']:.2f} Gwei")
        print(f"Standard: {speeds['standard']:.2f} Gwei")
        print(f"Slow:     {speeds['slow']:.2f} Gwei")

    time.sleep(5)
