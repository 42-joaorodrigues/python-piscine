from ft_filter import ft_filter

# subject
print(list(ft_filter(lambda x: x % 2 == 0, range(10))))

print("--- checks: ft_filter vs filter ---")
print(list(ft_filter(None, [0, 1, "", "a", None, [2]])))
print(list(filter(None, [0, 1, "", "a", None, [2]])))

print(list(ft_filter(str.isupper, "aBcD")))
print(list(filter(str.isupper, "aBcD")))

print(list(ft_filter(lambda x: x > 100, [1, 2, 3])))
print(list(filter(lambda x: x > 100, [1, 2, 3])))

print("--- docstring ---")
print(ft_filter.__doc__ == filter.__doc__)

print("--- lazy ---")
print(ft_filter(lambda x: x > 0, [1, -1, 2]))
