def greet(name):
    """Returns a greeting message"""
    return f"Hello, {name}!"

def add(a, b):
    """Adds two numbers"""
    return a + b

# Tests
def test_greet():
    assert greet("World") == "Hello, World!"
    print("✓ greet test passed")

def test_add():
    assert add(2, 3) == 5
    print("✓ add test passed")

if __name__ == "__main__":
    print("Running tests...")
    test_greet()
    test_add()
    print("All tests passed!")