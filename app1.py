def process_data(user_input):
    # Security risk: eval() allows arbitrary code execution
    result = eval(user_input)
    return result

try:
    print(process_data("2 + 2"))
except Exception:
    # Bad practice: silently swallowing all exceptions
    pass
