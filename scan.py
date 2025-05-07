import requests
from config import MINT, RPC, TOP_N

TOKEN_PID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
OUTFILE = "wallets.txt"

def rpc(method: str, params: list):
    return requests.post(
        RPC,
        json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params},
        timeout=30
    ).json()["result"]

def main() -> None:
    accounts = rpc("getProgramAccounts",
                   [TOKEN_PID,
                    {"encoding": "jsonParsed",
                     "filters":[{"dataSize":165},
                                {"memcmp":{"offset":0,"bytes":MINT}}]}])

    top = sorted(accounts,
                 key=lambda a: a["account"]["data"]["parsed"]["info"]
                                  ["tokenAmount"]["uiAmount"],
                 reverse=True)[:TOP_N]

    wallets = [a["account"]["data"]["parsed"]["info"]["owner"] for a in top]

    open(OUTFILE, "w").write("\n".join(wallets))
    print(f"{len(wallets)} wallet addresses ➜ {OUTFILE}")

if __name__ == "__main__":
    main()
