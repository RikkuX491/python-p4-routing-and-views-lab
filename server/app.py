#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    count_string = ""
    for i in range(parameter):
        count_string += f"{i}\n"
    
    return count_string

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    
    # num1 = int(num1)
    # num2 = int(num2)
    
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        # if num2 == 0:
        #     abort(400, "Division by zero not allowed")
        return f'{num1 / num2}'
    elif operation == '%':
        # if num2 == 0:
            # abort(400, "Division by zero not allowed")
            # return {"error": "Division by zero not allowed"}, 400
        return f'{num1 % num2}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)