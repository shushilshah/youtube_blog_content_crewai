from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task
research_task = Task(
    description=(
        "identify the video {topic}."
        "get the detailed information about the video from the channel"
    ),
    expected_output="A comprhensive 3 paragraphs long report based on the {topic} of video content from youtube channel",
    tools=[yt_tool],
    agent=blog_researcher
)

# Writing task with language model
write_task = Task(
    description=(
        "get the info from the youtube channel on the{topic}"
    ),
    expected_output="Summarize the info from the youtube channel on the {topic} and create the content for the blog",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)
