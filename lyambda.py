my_lambda_function = lambda x: len(x) / 5 if isinstance(x, str) else x / 5 if isinstance(x, (int, float)) else None

# Приклади використання лямбди:
result1 = my_lambda_function(10)          # Результат: 
print(result1)