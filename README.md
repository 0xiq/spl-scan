# SPL-Token Holder Scan 

Scans a Solana token's top holders and saves their wallet addresses to `wallets.txt`.

## What it does

- Connects to the Solana RPC.
- Fetches token holder accounts using the token mint.
- Sorts by balance and extracts the top `N` holders.
- Saves their wallet addresses to `wallets.txt`.

## Usage

1. Install dependencies:
   ```bash
    pip install requests
   ```


2.	Set up config.py:
   ```bash
    RPC = "https://your-rpc-url"
    MINT = "YourTokenMintAddress"
    TOP_N = 100
   ```

3. Run the script:
    ```bash
    python3 scan.py
    ```


