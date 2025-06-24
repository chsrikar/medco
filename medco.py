# ======================== MEDCO CLI Assistant ========================

BORDER = "*" * 100
TITLE = "MEDCO - Your Personal Medical Assistant".center(100)

print(BORDER)
print(TITLE)
print(BORDER)

# ---------------------- User Login ----------------------

username = input("Enter your Username: ")
password = input("Enter your Password (min 8 characters): ")

while len(password) < 8:
    print("Password should be at least 8 characters long.")
    password = input("Re-enter your Password: ")

print("Password is valid.")
print(f"\nHello {username}, how can I assist you today, sir?")

# ---------------------- Disease Check ----------------------

has_disease = input("\nDo you have any symptoms or health issues? (yes/no): ").lower()

if has_disease == "yes":
    # Define problem-solution pairs
    disease_dict = {
        "cold": "Take Dolo 650 and rest.",
        "cough": "Drink warm water with turmeric.",
        "headache": "Take a nap and stay hydrated.",
        "fever": "Take Paracetamol and consult a doctor if it persists.",
        "stomach pain": "Try a light diet and take Cyclopam.",
        "body pain": "Apply pain relief balm and rest.",
        "acidity": "Take Eno or Gelusil after meals."
    }

    def suggest_medicine(problem):
        problem = problem.lower()
        if problem in disease_dict:
            return f"Problem: {problem.title()} \nSuggested Treatment: {disease_dict[problem]}"
        else:
            return f"Sorry, no solution found for '{problem}'. Please consult a doctor."

    while True:
        user_problem = input("\nEnter your problem (type 'exit' to quit): ").strip()
        if user_problem.lower() == "exit":
            print("Thank you for using MEDCO. Stay healthy.")
            break
        print(suggest_medicine(user_problem))

else:
    print("Glad to hear you're healthy, sir. Stay safe and take care.")

print(BORDER)
