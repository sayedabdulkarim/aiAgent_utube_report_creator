from crewai import Task
from tools import tool
# from tools import yt_tool
from agents import news_researcher,news_writer, blog_writer, blog_researcher

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='3 lines report based AI trends.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)

## Research Task
# research_task = Task(
#     description=(
#         "Identify the video {topic}."
#         "Get detailed information about the video from the channel."
#     ),
#     expected_output='3 lines report based on the {topic} of video content.',
#     tools=[yt_tool],
#     agent=blog_researcher,
# )

# # Writing task with language model configuration
# write_task = Task(
#     description=(
#         "Get the info from the YouTube channel on the topic {topic}."
#     ),
#     expected_output='Summarize the info from the YouTube channel video on the topic {topic}, and write a short blog post.',
#     tools=[yt_tool],
#     agent=blog_writer,
#     output_file='new-blog-post.md'  # Example of output customization
# )

    # NOTE: async_execution=False, // This is to make sure that the task is executed in a synchronous manner
