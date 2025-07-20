
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from student_tools import answer_academic_question, get_study_tip, summarize_text_content

# Load environment variables
load_dotenv()

# Create the Gemini-compatible client (using OpenAI-like wrapper)
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Configure the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Create run configuration
config = RunConfig(
    model=model,
    tracing_disabled=True
)

# Define the student assistant agent
student_agent = Agent(
    name="Smart Student Assistant",
    instructions="""
You are a helpful and intelligent assistant for students. Your tasks:
- Answer academic questions in a simple, friendly way.
- Provide study tips tailored to different subjects.
- Summarize short texts clearly and concisely.
""",
    model=model,
    tools=[answer_academic_question, get_study_tip, summarize_text_content]
)

# Main execution loop
def main():
    print("🎓 Smart Student Agent Assistant\n")

    while True:
        query = input("Ask me anything (or type 'exit' to quit):\n> ")
        if query.strip().lower() == "exit":
            print("Goodbye! 👋")
            break

        try:
            result = Runner.run_sync(student_agent, query, run_config=config)
            print("\n🤖 Answer:\n", result.final_output)
        except Exception as e:
            print("❌ Error while processing your request:", str(e))

        print("-" * 40)

# Corrected entry point
if __name__ == "__main__":
    main()
