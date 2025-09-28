class LoanCalculator:
    def __init__(self, loan_amount, loan_term, loan_type, risk_factor):
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.risk_factor = risk_factor

    def calculate_interest_rate(self):
        base_rate = 5  # Базовая ставка

        # Если кредит долгосрочный, ставка растёт
        if self.loan_term > 10:
            base_rate += 2

        # Учитываем риск
        if self.risk_factor > 0.5:
            base_rate += 1
        elif self.risk_factor < 0.2:
            base_rate -= 1

        # Добавляем дополнительную ставку в зависимости от типа кредита
        if self.loan_type == "personal":
            base_rate += 3
        elif self.loan_type == "mortgage":
            base_rate += 1
        elif self.loan_type == "car":
            base_rate += 0.5

        # Множество лишних условий для дополнительной корректировки ставки
        if self.loan_amount > 1000000:
            base_rate -= 0.5

        if self.loan_term < 5:
            base_rate += 0.5

        return base_rate



class LoanCalculator:
    def __init__(self, loan_amount, loan_term, loan_type, risk_factor):
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.risk_factor = risk_factor

    def calculate_interest_rate(self):
        base_rate = 5  # Базовая ставка

        # Если кредит долгосрочный, ставка растёт
        if self.loan_term > 10:
            base_rate += 2

        # Учитываем риск
        if self.risk_factor > 0.5:
            base_rate += 1
        elif self.risk_factor < 0.2:
            base_rate -= 1

        # Добавляем дополнительную ставку в зависимости от типа кредита
        # ЛУЧШЕ ИСПОЛЬЗОВАТЬ СЛОВАРЬ
        if self.loan_type == "personal":
            base_rate += 3
        elif self.loan_type == "mortgage":
            base_rate += 1
        elif self.loan_type == "car":
            base_rate += 0.5

        return base_rate

