from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

import os
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_NAME'] = "gpt-4-0125-preview"


# defining senior blog content researcher

blog_researcher = Agent(
    role='Blog researcher from youtube videos',
    goal="get the relavent video content for the given {topic} from youtube channels",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in data science, AI, machine learning and genai and provides suggestions."
    ),
    tools=[yt_tool],
    allow_delegation=True

)

# creating blog writer agent

blog_writer = Agent(
    role="Blog writer",
    goal="Narrate compelling tech stories about the video {topic} from youtube channel",
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=True
)
