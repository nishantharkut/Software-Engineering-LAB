"""Convenience launcher for either laboratory task."""


def main():
    print("Software Engineering Lab 5")
    print("1. Digital Wallet")
    print("2. Project Task & Sprint Tracking")
    choice = input("Select task: ").strip()
    if choice == "1":
        from task1_wallet.cli import main as wallet_main
        wallet_main()
    elif choice == "2":
        from task2_project.cli import main as project_main
        project_main()
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
