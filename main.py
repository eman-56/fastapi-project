

# main.py
from fastapi import FastAPI
from Agents import Agent, Runner
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello! FastAPI is running."}

# LLM API endpoint
@app.post("/LLM")
async def llm(prompt: str):
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant that can answer questions and help with tasks."
    )
    result = await Runner.run(
        starting_agent=agent,
        input=prompt
    )
    return {"response": result.final_output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
