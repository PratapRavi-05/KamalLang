"""
KamalLang Interpreter - A Python-based educational programming language
inspired by the legendary actor Kamal Haasan.

Syntax Features:
- KAMAL.SPEAK for print statements
- INTELLECT for variable declaration
- IF/THEN for conditionals
- Uses Tamil cinema references and Kamal's philosophy
"""

import re
import sys

class KamalInterpreter:
    def __init__(self):
        self.variables = {}
        self.kamal_quotes = [
            "Life is beautiful, keep learning!",
            "Art is freedom, programming is art!",
            "Intha world-ula enna panna mudiyum!",
            "Hey Ram! Let's code with wisdom.",
            "Thug Life means Thinking, Understanding, Growing!"
        ]
    
    def interpret(self, code):
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            self.execute_line(line)
    
    def execute_line(self, line):
        # Handle KAMAL.SPEAK
        if line.startswith('KAMAL.SPEAK'):
            self.handle_print(line)
        # Handle INTELLECT (variable declaration)
        elif line.startswith('INTELLECT'):
            self.handle_variable(line)
        # Handle IF/THEN
        elif line.startswith('IF'):
            self.handle_if(line)
        else:
            print(f"KamalError: Unrecognized command - '{line}'")
    
    def handle_print(self, line):
        # Extract text between quotes
        match = re.search(r'KAMAL\.SPEAK\s+"([^"]+)"', line)
        if match:
            text = match.group(1)
            print(text)
        else:
            print("KamalError: Proper syntax is KAMAL.SPEAK \"message\"")
    
    def handle_variable(self, line):
        # Parse INTELLECT name = value
        parts = line.split()
        if len(parts) != 4 or parts[2] != '=':
            print("KamalError: Proper syntax is INTELLECT name = value")
            return
        
        var_name = parts[1]
        value_expr = parts[3]
        
        try:
            # Evaluate the expression (simple version)
            value = eval(value_expr, {}, self.variables)
            self.variables[var_name] = value
        except:
            print(f"KamalError: Could not evaluate {value_expr}")
    
    def handle_if(self, line):
        # Parse IF condition THEN
        if 'THEN' not in line:
            print("KamalError: IF statements must end with THEN")
            return
        
        condition_part = line[2:line.index('THEN')].strip()
        statement_part = line[line.index('THEN')+4:].strip()
        
        try:
            # Evaluate the condition
            condition_met = eval(condition_part, {}, self.variables)
            if condition_met:
                self.execute_line(statement_part)
        except:
            print(f"KamalError: Could not evaluate condition {condition_part}")
    
    def random_kamal_quote(self):
        import random
        return random.choice(self.kamal_quotes)

def run_file(filename):
    interpreter = KamalInterpreter()
    try:
        with open(filename, 'r') as file:
            code = file.read()
        interpreter.interpret(code)
    except FileNotFoundError:
        print(f"KamalError: File '{filename}' not found. Hey Ram!")
    except Exception as e:
        print(f"KamalError: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python kamal_interpreter.py script.kamal")
        print("Example:")
        print('INTELLECT age = 70')
        print('IF age > 60 THEN KAMAL.SPEAK "Still evolving as an actor and thinker!"')
        return
    
    filename = sys.argv[1]
    if not filename.endswith('.kamal'):
        print("KamalLang files must have .kamal extension")
        return
    
    run_file(filename)

if __name__ == "__main__":
    main()