# from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool with a specific YouTube channel handle to target your search
# yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@moshhamedani')

# ## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()
