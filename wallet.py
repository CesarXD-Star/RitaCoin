import os
import json
import hashlib
import secrets

WALLET_FILE = "wallet.json"

def generate_wallet():
    private_key = secrets.token_hex(32)
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    address = "RITA" + public_key[:30]

    wallet = {
        "address": address,
        "public_key": public_key,
        "private_key": private_key,
        "balance": 0
    }

    with open(WALLET_FILE, "w") as f:
        json.dump(wallet, f, indent=4)

    print("Wallet creada")
    print("Address:", address)

def load_wallet():
    if not os.path.exists(WALLET_FILE):
        print("No existe wallet. Crea una primero.")
        return None

    with open(WALLET_FILE, "r") as f:
        return json.load(f)

def show_wallet():
    wallet = load_wallet()
    if wallet:
        print("Address:", wallet["address"])
        print("Balance:", wallet["balance"], "RITA")

def menu():
    print("\n=== RitaCoin Wallet ===")
    print("1. Crear wallet")
    print("2. Ver wallet")
    print("3. Salir")

    option = input(">>> ")

    if option == "1":
        generate_wallet()
    elif option == "2":
        show_wallet()
    elif option == "3":
        exit()
    else:
        print("Opción inválida")

while True:
    menu()
