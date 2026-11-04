def process_data(user_input):
    result = eval(user_input)
    return result
try:
    print(process_data("2 + 2"))
except Exception:
    pass
