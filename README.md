# PulseChain Gas Price CLI

This is a simple command-line interface (CLI) tool that fetches and displays the real-time gas prices (in Gwei) on the PulseChain network. The data is fetched from the PulseChain Gas API and is updated every 10 seconds.

## Features
- Fetches gas prices (rapid, fast, standard, slow) from PulseChain.
- Automatically updates the prices every 10 seconds.
- Displays gas prices in Gwei in an easy-to-read CLI format.

## Prerequisites
- Node.js installed on your system.
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

Install dependencies:
```bash
npm install
```

## Usage

Run the CLI:
```bash
node gasPriceCli.js
```

The gas prices will be fetched and displayed in your terminal, and they will automatically update every 10 seconds.

## Example Output
```yaml
PulseChain Gas Prices:
----------------------
Rapid:    13.45 Gwei
Fast:     10.87 Gwei
Standard: 8.45 Gwei
Slow:     5.32 Gwei
```

## How It Works
- The script uses `axios` to make an HTTP request to the PulseChain gas price API.
- It converts the gas prices from Wei to Gwei for readability.
- The terminal output is updated every 10 seconds with the latest prices.

## Customization

### Update Interval:
By default, the gas prices are updated every 10 seconds. You can change this by modifying the interval in the script:
```javascript
await new Promise(resolve => setTimeout(resolve, 10000)); // Change 10000 (10 seconds) to your desired interval
```

## Dependencies
- `axios`: Promise-based HTTP client for making API requests.
- Node.js built-in `readline`: For handling terminal output updates.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page or open a pull request.
