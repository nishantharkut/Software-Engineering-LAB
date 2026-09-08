(.venv) PS C:\N Drive\Acads\Software Engineering\Lab\labs\lab05_tasks> python -m task1_wallet.cli

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 1
User ID: U001
User Name: Nishant
Wallet ID: W001
Mobile Number: 7226047625
Wallet created successfully.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 1
User ID: U002
User Name: Rahul
Wallet ID: W002
Mobile Number: 9123456780
Wallet created successfully.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 4
Wallet ID: W001
Amount: 5000
Money added successfully.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 4
Wallet ID: W002
Amount: 3000
Money added successfully.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 5
Wallet ID: W001
Amount: 500
Money withdrawn successfully.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 6
Source Wallet ID: W001
Destination Wallet ID: W002
Amount: 1500
Transfer completed successfully.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 2
W001: User=Nishant, User ID=U001, Mobile=7226047625, Balance=₹3000.00, Status=Active
W002: User=Rahul, User ID=U002, Mobile=9123456780, Balance=₹4500.00, Status=Active

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 8
Wallet ID: W001
Transaction(transaction_id='TXN0001', transaction_type=<TransactionType.DEPOSIT: 'Deposit'>, source_wallet=None, destination_wallet='W001', amount=Decimal('5000.00'), updated_balance=Decimal('5000.00'))
Transaction(transaction_id='TXN0003', transaction_type=<TransactionType.WITHDRAWAL: 'Withdrawal'>, source_wallet='W001', destination_wallet=None, amount=Decimal('500.00'), updated_balance=Decimal('4500.00'))
Transaction(transaction_id='TXN0004', transaction_type=<TransactionType.TRANSFER: 'Transfer'>, source_wallet='W001', destination_wallet='W002', amount=Decimal('1500.00'), updated_balance=Decimal('3000.00'))

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 9
Wallet ID: W002
Wallet status updated.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 6
Source Wallet ID: W001
Destination Wallet ID: W002
Amount: 500
Error: Wallet 'W002' is blocked.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 9
Wallet ID: W002
Wallet status updated.

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 10
{'total_transactions': 4, 'deposits': Decimal('8000.00'), 'withdrawals': Decimal('500.00'), 'transfers': Decimal('1500.00'), 'total_wallets': 2}

=== Digital Wallet and Transaction Management ===
1. Create new user wallet
2. Display all wallet details
3. Search wallet by Wallet ID
4. Add money
5. Withdraw money
6. Transfer money
7. View current balance
8. View transaction history
9. Block/unblock wallet
10. Generate transaction summary
11. Exit
Enter choice: 11
Exiting...