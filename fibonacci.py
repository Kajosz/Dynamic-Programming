# Run `python main.py` in the terminal

# Note: Python is lazy loaded so the first run will take a moment,
# But after cached, subsequent loads are super fast! ⚡️

def fibonacci(n, stored = {}):
  if n < 0:
    return None
  if n == 0:
    return 0
  if n <= 2:
    return 1


  result = stored.get(n)
  if not result is None:
    return result
  
  result = fibonacci(n - 1, stored) + fibonacci(n - 2, stored)
  stored[n] = result
  return result

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(150))

