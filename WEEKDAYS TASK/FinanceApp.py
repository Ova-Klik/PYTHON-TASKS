loanAmount = float(input("Kindly enter Loan Amount: "))
numberOfYears = int(input("Kindly enter Number of Years: "))

numberOfPayments = numberOfYears * 12

print(f"\n{'':4}{'Interest Rate':<18}{'Monthly Payment':<20}{'Total Payment'}")
print("=" * 60)

annualInterestRate = 5.0

while annualInterestRate <= 10.0:
    monthlyRate = annualInterestRate / 100 / 12
    monthlyPayment = (loanAmount * monthlyRate) / (1 - (1 + monthlyRate) ** (-numberOfPayments))
    totalPayment = monthlyPayment * numberOfPayments

    print(f"{'':4}{annualInterestRate:.3f}% {monthlyPayment:21.2f} {totalPayment:20.2f}")

    annualInterestRate += 0.25
