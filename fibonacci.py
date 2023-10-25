# Run `python main.py` in the terminal

# Note: Python is lazy loaded so the first run will take a moment,
# But after cached, subsequent loads are super fast! ⚡️

def fibonacci(n):
  if n < 0:
    return None
  if n == 0:
    return 0
  if n <= 2:
    return 1

  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
