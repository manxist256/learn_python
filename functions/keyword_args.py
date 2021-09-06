def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome!")


# keyword arguments improves readability
greet_user(last_name="Smith", first_name="John")
# we can mix keyword and positional arguments but makes sure positional always comes first
greet_user("John", last_name = "Smith")

