# PulseChain Gas Price CLI

This is a command-line interface (CLI) tool that fetches and displays real-time gas prices (in Gwei) on the PulseChain network. It calculates and shows the current, 5-minute, and hourly averages. The data updates every 5 seconds using G4MM4's PulseChain RPC endpoint (https://www.g4mm4.io/).

## Features
- Fetches the current gas price from PulseChain.
- Calculates 5-minute and 1-hour averages.
- Displays prices in Gwei in a live updating table format.

## Prerequisites
- Python 3 installed on your system.
- Basic knowledge of the terminal/command line.

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/pulsechain-gas-cli.git
```

Navigate to the project directory:
```bash
cd pulsechain-gas-cli
```

Install dependencies (e.g., requests library):
```bash
pip install -r requirements.txt
```

## Usage

Run the CLI:
```bash
python gas_price_cli.py
```

The gas prices will be fetched and displayed in the terminal, updating every 5 seconds with both the current price and rolling averages.

## Example Output
```bash
Time                 Current Gas Price (Gwei)    5-Minute Avg (Gwei)    1-Hour Avg (Gwei)
2024-10-06 12:34:56  10.45                      9.89                   10.02
2024-10-06 12:35:01  10.87                      10.12                  10.04
```

## How It Works
- The script uses Python's `requests` library to make JSON-RPC requests to G4MM4's PulseChain RPC API (https://www.g4mm4.io/).
- Gas prices are fetched, stored, and averages are calculated in Gwei.
- The terminal table is refreshed every 5 seconds with the latest values.

## Customization

### Update Interval:
To change the update interval, modify the sleep time in the script:
```python
time.sleep(5)  # Change 5 (seconds) to your desired interval
```

## Dependencies
- `requests`: HTTP library for API calls.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
