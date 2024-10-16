#!/usr/bin/env python
# coding: utf-8

# In[15]:


import json

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # left child
        self.right = right  # right child (for operators)
        self.value = value  # value for operand nodes

def parse_rule_string(rule_string):
    # Placeholder parsing logic; this should be replaced with actual parsing logic.
    # For simplicity, we will create a simple AST manually.
    if rule_string == "((age > 30 AND department = 'Sales'))":
        return Node("operator", 
                    Node("operand", value="age>30"), 
                    Node("operand", value="department=='Sales'"), 
                    value="AND")
    elif rule_string == "((age < 25 AND department = 'Marketing'))":
        return Node("operator", 
                    Node("operand", value="age<25"), 
                    Node("operand", value="department=='Marketing'"), 
                    value="AND")
    else:
        raise ValueError("Invalid rule string")

def create_rule(rule_string):
    try:
        ast = parse_rule_string(rule_string)
        return ast
    except Exception as e:
        raise ValueError("Invalid rule string") from e

def combine_rule_asts(rule_asts):
    # Combine multiple ASTs into a single AST
    # For simplicity, we'll just create a new operator node.
    return Node("operator", rule_asts[0], rule_asts[1], value="AND")

def combine_rules(rules):
    combined_ast = combine_rule_asts([create_rule(rule) for rule in rules])
    return combined_ast

def evaluate_ast(ast, data):
    # Evaluate the AST against the provided data
    if ast.type == "operand":
        return eval(ast.value, data)
    elif ast.type == "operator":
        left_result = evaluate_ast(ast.left, data)
        right_result = evaluate_ast(ast.right, data)
        if "AND" in ast.value:
            return left_result and right_result
        elif "OR" in ast.value:
            return left_result or right_result
    return False

def evaluate_rule(ast, data):
    result = evaluate_ast(ast, data)
    return result

# Sample rules
rule1 = "((age > 30 AND department = 'Sales'))"
rule2 = "((age < 25 AND department = 'Marketing'))"

# Create individual rules
ast1 = create_rule(rule1)
ast2 = create_rule(rule2)

# Combine rules
combined_ast = combine_rules([rule1, rule2])

# Sample data
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

# Evaluate rules
result1 = evaluate_rule(ast1, data)
result2 = evaluate_rule(ast2, data)
combined_result = evaluate_rule(combined_ast, data)

print(f"Result of Rule 1: {result1}")  # Should be True
print(f"Result of Rule 2: {result2}")  # Should be False
print(f"Combined Rule Result: {combined_result}")  # Evaluate combined logic


# In[ ]:




