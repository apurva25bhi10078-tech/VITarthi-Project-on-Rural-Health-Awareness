def show_menu():
    print("\n========== Rural Health Support System ==========")
    print("1. Diarrhea")
    print("2. Malaria")
    print("3. Dengue")
    print("4. Typhoid")
    print("5. Anemia")
    print("6. Skin Infections")
    print("7. Respiratory Infection (Cold/Cough)")
    print("8. Exit Application")
    print("=================================================")


def show_details(name, causes, symptoms, precautions, medicines):
    print(f"\n====== {name.upper()} ======")

    print("\nCauses:")
    for c in causes:
        print("- " + c)

    print("\nSymptoms:")
    for s in symptoms:
        print("- " + s)

    print("\nPrecautions:")
    for p in precautions:
        print("- " + p)

    print("\nSuggested Medicines (Basic):")
    for m in medicines:
        print("- " + m)

    print("\n⚠ NOTE: Visit the nearest health center if symptoms continue.\n")


# ----------- DISEASE FUNCTIONS ----------------

def diarrhea():
    show_details(
        "Diarrhea",
        causes=[
            "Contaminated water", 
            "Poor sanitation",
            "Bacterial or viral infection"
        ],
        symptoms=[
            "Loose stools", 
            "Dehydration", 
            "Weakness"
        ],
        precautions=[
            "Drink clean or boiled water",
            "Wash hands regularly",
            "Avoid street food"
        ],
        medicines=[
            "ORS solution", 
            "Zinc tablets", 
            "Paracetamol for fever"
        ]
    )


def malaria():
    show_details(
        "Malaria",
        causes=[
            "Mosquito bite (Anopheles)"
        ],
        symptoms=[
            "High fever", 
            "Chills", 
            "Headache"
        ],
        precautions=[
            "Use mosquito nets",
            "Avoid stagnant water",
            "Keep surroundings clean"
        ],
        medicines=[
            "Chloroquine (if prescribed)",
            "Artemisinin combination therapy (ACT)"
        ]
    )


def dengue():
    show_details(
        "Dengue",
        causes=["Aedes mosquito bite"],
        symptoms=["High fever", "Joint pain", "Headache"],
        precautions=[
            "Remove stagnant water",
            "Use mosquito repellent",
            "Wear full-sleeve clothes"
        ],
        medicines=[
            "Paracetamol (NOT aspirin)",
            "Hydration fluids"
        ]
    )


def typhoid():
    show_details(
        "Typhoid",
        causes=["Contaminated food or water"],
        symptoms=["Prolonged fever", "Vomiting", "Weakness"],
        precautions=[
            "Eat properly cooked food",
            "Drink boiled water",
            "Maintain hygiene"
        ],
        medicines=[
            "Ciprofloxacin (only if prescribed)",
            "Paracetamol for fever"
        ]
    )


def anemia():
    show_details(
        "Anemia",
        causes=["Iron deficiency", "Poor nutrition"],
        symptoms=["Fatigue", "Pale skin", "Weakness"],
        precautions=[
            "Eat iron-rich foods",
            "Green leafy vegetables",
            "Regular checkups"
        ],
        medicines=[
            "Iron tablets",
            "Folic acid tablets"
        ]
    )


def skin_infections():
    show_details(
        "Skin Infections",
        causes=["Fungal infection", "Poor hygiene"],
        symptoms=["Itching", "Rashes", "Redness"],
        precautions=[
            "Keep skin clean",
            "Avoid sharing clothes",
            "Wear loose cotton clothes"
        ],
        medicines=[
            "Antifungal cream",
            "Medicated soap"
        ]
    )


def respiratory_infection():
    show_details(
        "Respiratory Infection (Cold/Cough)",
        causes=["Virus", "Dust pollution"],
        symptoms=["Runny nose", "Cough", "Throat pain"],
        precautions=[
            "Drink warm water",
            "Avoid cold drinks",
            "Wear mask in dust"
        ],
        medicines=[
            "Cough syrup",
            "Paracetamol",
            "Warm steam inhalation"
        ]
    )


# ---------------- MAIN PROGRAM -------------------

while True:
    show_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        diarrhea()
    elif choice == '2':
        malaria()
    elif choice == '3':
        dengue()
    elif choice == '4':
        typhoid()
    elif choice == '5':
        anemia()
    elif choice == '6':
        skin_infections()
    elif choice == '7':
        respiratory_infection()
    elif choice == '8':
        print("\nThank you for using the Rural Health Support System.\n")
        break
    else:
        print("\nInvalid input! Please choose between 1 to 8.\n")