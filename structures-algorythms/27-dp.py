# Динамическое программирование
def fibonacci_no_dp(n):
    if n <= 1:
        return n
    return fibonacci_no_dp(n-1) + fibonacci_no_dp(n-2)

print(fibonacci_no_dp(10)) # 55

# Мемоизация - сохранение результатов подзадач
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print(fib_memo(10)) # 55