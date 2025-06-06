# doctor_collab.py

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


# For testing the module independently
if __name__ == "__main__":
    profile = {
        "age": 65,
        "gender": "male",
        "conditions": ["asthma"]
    }
    symptoms = ["cough", "fever"]

    result = generate_doctor_collab_output(profile, symptoms)

    print("\nDoctor Collaboration Hub Output:\n")
    for key, value in result.items():
        print(f"{key.capitalize()}: {value}")
