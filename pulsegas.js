const axios = require('axios');
const readline = require('readline');

// Function to fetch gas prices from the PulseChain API
async function fetchGasPrice() {
    try {
        const response = await axios.get('https://beacon.pulsechain.com/api/v1/execution/gasnow');
        const data = response.data;
        
        if (data && data.data) {
            const { rapid, fast, standard, slow } = data.data;
            return {
                rapid: rapid / 1e9,   // Convert from wei to Gwei
                fast: fast / 1e9,
                standard: standard / 1e9,
                slow: slow / 1e9
            };
        }
    } catch (error) {
        console.error('Error fetching gas prices:', error);
    }
    return null;
}

// Function to update the displayed gas prices
function updateDisplay(gasPrices) {
    readline.cursorTo(process.stdout, 0, 0);  // Move cursor to top left of the terminal
    readline.clearScreenDown(process.stdout); // Clear everything below the cursor
    console.log("PulseChain Gas Prices:");
    console.log("----------------------");
    console.log(`Rapid:    ${gasPrices.rapid.toFixed(2)} Gwei`);
    console.log(`Fast:     ${gasPrices.fast.toFixed(2)} Gwei`);
    console.log(`Standard: ${gasPrices.standard.toFixed(2)} Gwei`);
    console.log(`Slow:     ${gasPrices.slow.toFixed(2)} Gwei`);
}

// Function to continually fetch and update gas prices every 10 seconds
async function main() {
    console.clear();  // Clear the terminal
    console.log("Fetching PulseChain Gas Prices...");
    
    while (true) {
        const gasPrices = await fetchGasPrice();
        
        if (gasPrices) {
            updateDisplay(gasPrices);
        }
        
        // Wait for 10 seconds before updating again
        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

main();
