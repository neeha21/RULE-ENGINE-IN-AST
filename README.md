# RULE-ENGINE-IN-AST
This report provides an overview of the Rule-Based System application, which is designed to evaluate rules against a given dataset. The application uses a simple Abstract Syntax Tree (AST) to represent the rules and evaluates them using a recursive approach.

The application consists of the following components:

Rule Parser: The rule parser is responsible for parsing the rule strings into an AST. The parser uses a simple recursive descent approach to parse the rules.
AST Node: The AST node represents a single node in the AST. Each node has a type (operand or operator), a value, and optional left and right child nodes.
Evaluator: The evaluator is responsible for evaluating the AST against a given dataset. The evaluator uses a recursive approach to evaluate the AST.
Data: The data component represents the dataset against which the rules are evaluated.

The system flow is as follows:

Rule Creation: The user creates a rule string, which is then parsed into an AST using the rule parser.
AST Creation: The parsed AST is then created using the AST node component.
Evaluation: The evaluator evaluates the AST against the given dataset.
Result: The result of the evaluation is then returned to the user.

The application is implemented in Python and uses the following technical details:

AST Node: The AST node is implemented as a Python class with attributes for type, value, and left and right child nodes.
Evaluator: The evaluator is implemented as a recursive function that evaluates the AST against the given dataset.
Data: The data component is implemented as a Python dictionary that represents the dataset.

The application handles errors in the following ways:

Syntax Errors: The application raises a SyntaxError exception when a syntax error is encountered in the rule string.
Type Errors: The application raises a TypeError exception when a type error is encountered during evaluation.
