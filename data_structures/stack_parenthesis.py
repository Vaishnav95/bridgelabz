"""Stack Parenthesis
Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.
"""
from data_structures_util import Stack

expression = input("Enter the expression: ")

expression_object = Stack()
result = expression_object.paren_balance(expression)
print(result)



