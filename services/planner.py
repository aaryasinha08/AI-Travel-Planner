from services.llm_service import ask_ai

def generate_travel_plan(city, days, budget, travel_style, interests):
    """
    Takes user travel preferences and generates a smart travel plan using AI.
    """

    prompt = f"""
You are a student-friendly AI travel planner.

Plan a {days}-day trip for:

City: {city}
Budget: {budget}
Travel Style: {travel_style}
Interests: {interests}

Rules:
1. Keep it budget-friendly.
2. Mention city name clearly.
3. Make it day-wise.
4. Add food suggestions.
5. Add transport tips.
6. Avoid expensive hotels.
7. Make it realistic for students.

Give output in simple, clear language.
"""

    response = ask_ai(prompt)
    return response
