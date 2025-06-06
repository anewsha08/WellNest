# personalized_care.py

def generate_personalized_plan(symptoms, profile=None):
    """
    Returns a personalized care plan based on symptoms and user profile.
    """
    care_plan = []

    if "fever" in symptoms:
        care_plan.append("Take rest and stay hydrated.")
        care_plan.append("Monitor temperature every 4 hours.")

    if "headache" in symptoms:
        care_plan.append("Avoid screen time and rest in a dark room.")
        care_plan.append("Consider using a cold compress.")

    if "cough" in symptoms:
        care_plan.append("Drink warm fluids and avoid cold foods.")
        care_plan.append("Consider using a humidifier.")

    if profile:
        if profile.get("age") and profile["age"] > 60:
            care_plan.append("Schedule a teleconsultation with a doctor due to age risk.")
        if "asthma" in profile.get("conditions", []):
            care_plan.append("Keep an inhaler nearby and avoid allergens.")

    return care_plan


# For testing
if __name__ == "__main__":
    test_symptoms = ["fever", "cough"]
    test_profile = {"age": 65, "conditions": ["asthma"]}
    plan = generate_personalized_plan(test_symptoms, test_profile)
    print("\nPersonalized Care Plan:")
    for step in plan:
        print("-", step)

