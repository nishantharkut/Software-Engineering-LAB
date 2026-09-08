from decimal import Decimal

from .exceptions import WalletError
from .service import WalletService


class WalletCLI:
    def __init__(self, service: WalletService | None = None):
        self.service = service or WalletService()

    @staticmethod
    def _money(value: Decimal) -> str:
        return f"₹{value:.2f}"

    def display_menu(self) -> None:
        print("\n=== Digital Wallet and Transaction Management ===")
        options = [
            "Create new user wallet", "Display all wallet details", "Search wallet by Wallet ID",
            "Add money", "Withdraw money", "Transfer money", "View current balance",
            "View transaction history", "Block/unblock wallet", "Generate transaction summary", "Exit",
        ]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

    def run_once(self, choice: str) -> bool:
        try:
            choice = int(choice)
        except (TypeError, ValueError):
            print("Invalid menu choice. Please enter a number.")
            return True
        if choice == 1:
            self._create()
        elif choice == 2:
            self._display_all()
        elif choice == 3:
            self._search()
        elif choice == 4:
            self._add()
        elif choice == 5:
            self._withdraw()
        elif choice == 6:
            self._transfer()
        elif choice == 7:
            self._balance()
        elif choice == 8:
            self._history()
        elif choice == 9:
            self._toggle()
        elif choice == 10:
            self._summary()
        elif choice == 11:
            print("Exiting...")
            return False
        else:
            print("Invalid menu choice. Please choose 1-11.")
        return True

    def _create(self):
        self._call(lambda: self.service.create_wallet(input("User ID: "), input("User Name: "), input("Wallet ID: "), input("Mobile Number: ")), "Wallet created successfully.")

    def _display_all(self):
        wallets = self.service.list_wallets()
        if not wallets:
            print("No wallets found.")
        for w in wallets:
            print(f"{w.wallet_id}: User={w.user_name}, User ID={w.user_id}, Mobile={w.mobile_number}, Balance={self._money(w.balance)}, Status={w.status.value}")

    def _search(self):
        self._call(lambda: print(self.service.search_wallet(input("Wallet ID: "))), None)

    def _add(self):
        self._call(lambda: self.service.add_money(input("Wallet ID: "), input("Amount: ")), "Money added successfully.")

    def _withdraw(self):
        self._call(lambda: self.service.withdraw_money(input("Wallet ID: "), input("Amount: ")), "Money withdrawn successfully.")

    def _transfer(self):
        self._call(lambda: self.service.transfer_money(input("Source Wallet ID: "), input("Destination Wallet ID: "), input("Amount: ")), "Transfer completed successfully.")

    def _balance(self):
        self._call(lambda: print(f"Balance: {self._money(self.service.current_balance(input('Wallet ID: ')))}"), None)

    def _history(self):
        def action():
            for tx in self.service.transaction_history(input("Wallet ID: ")):
                print(tx)
        self._call(action, None)

    def _toggle(self):
        self._call(lambda: self.service.toggle_block(input("Wallet ID: ")), "Wallet status updated.")

    def _summary(self):
        print(self.service.transaction_summary())

    @staticmethod
    def _call(action, success_message):
        try:
            action()
            if success_message:
                print(success_message)
        except WalletError as exc:
            print(f"Error: {exc}")

    def run(self):
        while True:
            self.display_menu()
            if not self.run_once(input("Enter choice: ")):
                break


def main():
    WalletCLI().run()


if __name__ == "__main__":
    main()
