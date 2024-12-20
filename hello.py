# test_script.py

# Hardcoded sensitive information (to trigger secrets detection)
API_KEY = "12345-abcdef-67890"

# Vulnerable dependency (to test dependency checks)
import yaml  # Avoid loading untrusted YAML (simulated issue)

def insecure_function(password="12345"):  # Hardcoded password
    print(f"The password is {password}")

# Simulated security vulnerability (to test SAST)
def eval_user_input(user_input):
    eval(user_input)  # Using eval is a security risk!

if __name__ == "__main__":
    user_input = input("Enter some code to execute: ")
    eval_user_input(user_input)