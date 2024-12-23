from crewai import Crew,Process 
from tasks import research_task,write_task
from agents import news_researcher,news_writer

# Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

# from crewai import Crew, Process  # Importing Crew to define the group of agents and Process for task execution flow
# from agents import blog_researcher, blog_writer  # Importing the agents for specific roles in the crew
# from tasks import research_task, write_task  # Importing the tasks to be performed by the agents

# # Forming the tech-focused crew with some enhanced configurations
# crew = Crew(
#     agents=[blog_researcher, blog_writer],  # Assigning the researcher and writer agents to the crew
#     tasks=[research_task, write_task],  # Assigning the tasks to be performed sequentially
#     process=Process.sequential,  # Ensuring tasks execute in sequence
#     memory=True,  # Enabling memory for the agents
#     cache=True,  # Enabling caching for task results
#     max_rpm=100,  # Limiting the rate of task execution per minute
#     share_crew=True  # Allowing the crew to be shared across different workflows
# )



## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
# result = crew.kickoff(inputs={'topic': 'AI vs ML vs DL vs Data Science'})
print(result)