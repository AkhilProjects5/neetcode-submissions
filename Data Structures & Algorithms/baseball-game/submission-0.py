class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            try:
                scores.append(int(operation))
            except ValueError:
                if operation == "+":
                    scores.append(scores[-1]+scores[-2])
                elif operation == "C":
                    scores.pop()
                elif operation == "D":
                    scores.append(scores[-1]*2)
            
        return sum(scores)
