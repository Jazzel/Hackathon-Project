from Score_calculator import Score_calculator as sc

def recomendation(Fatigue, Survey, Memory, Focus):
    severity = sc(Fatigue, Survey, Memory, Focus)[0]
    if severity == "Low":
        return ["Maintain a regular sleep schedule before traveling", "Stay hydrated by drinking plenty of water during the flight", "Adjust your sleep schedule gradually a few days before traveling, aligning it with the destinations time zone","Avoid excessive consumption of caffeine and alcohol, as they can disrupt sleep patterns." ,"Consider using natural remedies like melatonin supplements to help regulate sleep."]
    elif severity == "Mild":
        return ["Follow the precautions mentioned for low jet lag susceptibility.", "Upon arrival, expose yourself to natural daylight, as it can help regulate your internal clock.", "Engage in light physical activity or exercise to promote alertness and combat fatigue. ","Take short naps if needed, but avoid long and irregular sleep periods."]
    elif severity == "Moderate":
        return ["Implement the precautions for low and mild jet lag susceptibility."," Consider adjusting your sleep schedule a few days before traveling to gradually align with the destination's time zone."," Use sleep aids, such as eye masks or earplugs, to create a comfortable sleeping environment.", "Avoid heavy meals close to bedtime, as it can disrupt sleep patterns."]
    elif severity == "High":
        return ["Employ all the precautions mentioned above.", "Try to book flights that arrive at your destination during the daytime to align with the local schedule.", "Consider using prescribed medications or melatonin supplements to regulate sleep patterns.", "Give yourself ample time to adjust to the new time zone by arriving a day or two in advance.",  "Consult with a healthcare professional for personalized advice and possible prescription options."]

# print(recomendation(0.2, 0.2, 0.2, 0.2))