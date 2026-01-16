from services.planner import generate_travel_plan

plan = generate_travel_plan(
    city="Jaipur",
    days=3,
    budget="Low",
    travel_style="Cultural & Heritage",
    interests="Photography, History, Food"
)

print("\n🧭 Travel Plan:\n")
print(plan)
