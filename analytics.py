from collections import Counter, defaultdict
from datetime import datetime
import matplotlib.pyplot as plt # type: ignore

def analyze_symptom_frequency(records):
    counter = Counter()
    for rec in records:
        counter.update(rec["symptoms"])
    return counter.most_common()

def condition_age_distribution(records):
    condition_ages = defaultdict(list)
    for rec in records:
        for condition in rec["conditions"]:
            condition_ages[condition].append(rec["age"])
    return {cond: sum(ages) / len(ages) for cond, ages in condition_ages.items()}

def doctor_recommendation_stats(records):
    counter = Counter()
    for rec in records:
        counter[rec["recommended_doctor"]] += 1
    return counter.most_common()

def severity_distribution(records):
    counter = Counter(rec["severity"] for rec in records)
    return dict(counter)

def monthly_symptom_trend(records):
    trend = defaultdict(Counter)
    for rec in records:
        month = datetime.strptime(rec["timestamp"], "%Y-%m-%d").strftime("%Y-%m")
        for sym in rec["symptoms"]:
            trend[month][sym] += 1
    return trend

# For testing
if __name__ == "__main__":
    dummy_data = [
        {
            "user_id": "u1",
            "age": 65,
            "gender": "male",
            "conditions": ["asthma"],
            "symptoms": ["cough", "fever"],
            "recommended_doctor": "Pulmonologist",
            "severity": "high",
            "timestamp": "2025-06-01"
        },
        {
            "user_id": "u2",
            "age": 45,
            "gender": "female",
            "conditions": ["diabetes"],
            "symptoms": ["fatigue", "thirst"],
            "recommended_doctor": "Endocrinologist",
            "severity": "medium",
            "timestamp": "2025-06-02"
        },
        {
            "user_id": "u3",
            "age": 34,
            "gender": "male",
            "conditions": [],
            "symptoms": ["fever", "headache"],
            "recommended_doctor": "General Physician",
            "severity": "low",
            "timestamp": "2025-06-03"
        }
    ]

    print("Symptom Frequency:", analyze_symptom_frequency(dummy_data))
    print("Age by Condition:", condition_age_distribution(dummy_data))
    print("Doctor Stats:", doctor_recommendation_stats(dummy_data))
    print("Severity Distribution:", severity_distribution(dummy_data))
    print("Symptom Trend:", monthly_symptom_trend(dummy_data))
