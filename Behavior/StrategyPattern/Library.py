from abc import ABC, abstractmethod
from dataclasses import dataclass


class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, days_overdue):
        pass


class RegularFeeStrategy(FeeStrategy):
    def calculate_fee(self, days_overdue):
        return days_overdue * 1  # e.g., $1 per day overdue


class ChildrenFeeStrategy(FeeStrategy):
    def calculate_fee(self, days_overdue):
        return days_overdue * 0.5  # e.g., $0.50 per day overdue


# クライアント側は各種戦略間の違いを意識する必要がある
@dataclass
class FeeContext:
    strategy: FeeStrategy

    def execute_fee_strategy(self, days_overdue):
        return self.strategy.calculate_fee(days_overdue)


regular_fee_strategy = RegularFeeStrategy()
children_fee_strategy = ChildrenFeeStrategy()

fee_context = FeeContext(regular_fee_strategy)
print(fee_context.execute_fee_strategy(5))  # Outputs: 5

fee_context.strategy = children_fee_strategy
print(fee_context.execute_fee_strategy(5))  # Outputs: 2.5
