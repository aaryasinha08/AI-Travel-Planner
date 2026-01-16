"""
test_llm.py
------------------
This file is used to test the LLM connection
and verify that Hugging Face API is working properly.
"""

from services.llm_service import ask_ai  # <-- IMPORT ask_ai

def main():
    print("🧠 Testing AI Travel Planner...\n")

    user_prompt = "Create a detailed 5-day travel plan for Rishikesh"

    print("📩 Sending prompt to AI:")
    print(user_prompt)
    print("\n⏳ Waiting for AI response...\n")

    reply = ask_ai(user_prompt)

    print("✅ AI Response:\n")
    print(reply)


if __name__ == "__main__":
    main()
