def generate_patient_summary(profile, symptoms):
    age = profile.get("age")
    gender = profile.get("gender")
    conditions = ", ".join(profile.get("conditions", [])) or "no chronic conditions"
    symptom_text = ", ".join(symptoms)
    return f"Patient is a {age}-year-old {gender} with {conditions} experiencing {symptom_text}."

def predict_severity(symptoms, profile):
    severe_symptoms = {"chest pain", "difficulty breathing", "unconscious", "confusion"}
    risk_factors = profile.get("age", 0) >= 60 or "asthma" in profile.get("conditions", [])

    if any(sym in severe_symptoms for sym in symptoms) or risk_factors:
        return "high"
    elif len(symptoms) >= 3:
        return "medium"
    else:
        return "low"

def recommend_doctor(symptoms):
    symptom_map = {
        "cough": "Pulmonologist",
        "chest pain": "Cardiologist",
        "skin rash": "Dermatologist",
        "anxiety": "Psychiatrist",
        "fever": "General Physician",
        "headache": "Neurologist",
        "joint pain": "Orthopedic"
    }

    for symptom in symptoms:
        if symptom in symptom_map:
            return symptom_map[symptom]
    return "General Physician"

def suggest_follow_up(severity):
    return {
        "low": "Follow-up in 3-5 days",
        "medium": "Follow-up in 1-2 days",
        "high": "Immediate follow-up or emergency visit"
    }[severity]

def generate_doctor_collab_output(profile, symptoms):
    summary = generate_patient_summary(profile, symptoms)
    severity = predict_severity(symptoms, profile)
    doctor = recommend_doctor(symptoms)
    follow_up = suggest_follow_up(severity)

    return {
        "summary": summary,
        "severity": severity,
        "recommended_doctor": doctor,
        "follow_up": follow_up
    }

def get_user_input():
    """Collect user profile and symptoms interactively"""
    print("\nWelcome to Doctor Collaboration Hub")
    print("Please provide your information:\n")
    
    profile = {}
    profile["age"] = int(input("Your age: "))
    profile["gender"] = input("Your gender (male/female/other): ").lower()
    
    conditions = input("Any chronic conditions? (comma separated, leave blank if none): ")
    profile["conditions"] = [c.strip() for c in conditions.split(",")] if conditions else []
    
    print("\nNow please describe your symptoms:")
    symptoms = input("List your symptoms (comma separated, e.g. 'cough, fever'): ")
    symptoms = [s.strip() for s in symptoms.split(",")] if symptoms else []
    
    return profile, symptoms

if __name__ == "__main__":
    profile, symptoms = get_user_input()
    
    if not symptoms:
        print("\nNo symptoms provided. Please consult a doctor if you're feeling unwell.")
    else:
        result = generate_doctor_collab_output(profile, symptoms)
        
        print("\nDoctor Collaboration Hub Output:\n")
        for key, value in result.items():
            print(f"{key.capitalize()}: {value}")
        
        if result["severity"] == "high":
            print("\nWARNING: Based on your symptoms and profile, you should seek medical attention immediately!")
