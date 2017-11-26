from typing import Dict

class Solution:
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        return self.eval_with_env(expression, {})

    def match_parenthesis(self, expression : str) -> Dict[int, int]:
        parenthesis = {}
        stack = []
        for i in range(len(expression)):
            if expression[i] == '(':
                stack.append(i)
            elif expression[i] == ')':
                j = stack.pop()
                parenthesis[j] = i
        return parenthesis

    def eval_with_env(self, expr : str, env : Dict[str, int]) -> int:
        if expr.startswith('('):
            parenthesis = self.match_parenthesis(expr)
            if expr.startswith("add", 1): # (add operand1 operand2)
                if expr[5].isalpha() or expr[5].isnumeric() or expr[5] == '-':
                    sub_expr = expr[5:-1] # type: str
                    operand_1, operand_2 = sub_expr.split(" ", 1)
                    return self.eval_with_env(operand_1, env.copy()) + self.eval_with_env(operand_2, env.copy())
                elif expr[5] == '(':
                    operand_1 = expr[5:parenthesis[5]+1]
                    operand_2 = expr[parenthesis[5]+2:-1]
                    return self.eval_with_env(operand_1, env.copy()) + self.eval_with_env(operand_2, env.copy())
            elif expr.startswith("mult", 1): # (mult operand1 operand2)
                if expr[6].isalpha() or expr[6].isnumeric() or expr[6] == '-':
                    sub_expr = expr[6:-1] # type: str
                    operand_1, operand_2 = sub_expr.split(" ", 1)
                    return self.eval_with_env(operand_1, env.copy()) * self.eval_with_env(operand_2, env.copy())
                elif expr[6] == '(':
                    operand_1 = expr[6:parenthesis[6]+1]
                    operand_2 = expr[parenthesis[6]+2:-1]
                    return self.eval_with_env(operand_1, env.copy()) * self.eval_with_env(operand_2, env.copy())
            elif expr.startswith("let", 1): # (let identifier expr ... expr)
                rest = expr[5:-1]
                while True:

                    identifier, rest = rest.split(" ", 1) # type: str, str

                    if rest[0].isnumeric() or rest[0] == '-':
                        value, rest = rest.split(" ", 1)
                        env[identifier] = int(value)
                    elif rest[0].isalpha():
                        sub_expr, rest = rest.split(" ", 1)
                        env[identifier] = self.eval_with_env(sub_expr, env.copy())
                    elif rest[0] == '(':
                        close_parenthesis_pos = self.match_parenthesis(rest)[0]
                        sub_expr = rest[:close_parenthesis_pos+1]
                        rest = rest[close_parenthesis_pos+2:]
                        env[identifier] = self.eval_with_env(sub_expr, env.copy())

                    if rest[0] == '(' or rest[0].isnumeric() or  rest[0] == '-' or \
                            (rest[0].isalpha() and rest.find(" ") == -1):
                        return self.eval_with_env(rest, env.copy())

        elif expr[0].isnumeric() or expr[0] == '-':
            return int(expr)
        elif expr[0].isalpha():
            expr = expr.strip()
            return env[expr]


if __name__ == '__main__':
    test = Solution()
    print(test.evaluate("(add 1 2)")) # 3
    print(test.evaluate("(mult 3 (add 2 3))")) # 15
    print(test.evaluate("(let x 2 (mult x 5))")) # 10
    print(test.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")) # 14
    print(test.evaluate("(let x 3 x 2 x)")) # 2
    print(test.evaluate("(let x 1 y 2 x (add x y) (add x y))")) # 5
    print(test.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))")) # 6
    print(test.evaluate("(let a1 3 b2 (add a1 1) b2)")) # 4
    print(test.evaluate("(let x 7 -12)")) # -12
    print(test.evaluate("(let x -2 y x y)")) # -2