# Warning control
import warnings
warnings.filterwarnings('ignore')
# Importing the libraries
from crewai import Agent, Crew, Task
import os
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from pydantic import BaseModel
import json
from pprint import pprint



os.environ["OPENAI_MODEL_NAME"] = 'gpt-4-turbo'
os.environ["OPENAI_API_KEY"]="sk-xx"
os.environ["SERPER_API_KEY"] = ""

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Agent 1: Venue Coordinator
venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Identify and book an appropriate venue "
    "based on event requirements",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "With a keen sense of space and "
        "understanding of event logistics, "
        "you excel at finding and securing "
        "the perfect venue that fits the event's theme, "
        "size, and budget constraints."
    )
)

# Agent 2: Logistics Manager
logistics_manager = Agent(
    role='Logistics Manager',
    goal=(
        "Manage all logistics for the event "
        "including catering and equipment"
    ),
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Organized and detail-oriented, "
        "you ensure that every logistical aspect of the event "
        "from catering to equipment setup "
        "is flawlessly executed to create a seamless experience."
    )
)

# Agent 3: Marketing and Communications Agent
marketing_communications_agent = Agent(
    role="Marketing and Communications Agent",
    goal="Effectively market the event and "
         "communicate with participants",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Creative and communicative, "
        "you craft compelling messages and "
        "engage with potential attendees "
        "to maximize event exposure and participation."
    )
)


# Define a Pydantic model for venue details
# (demonstrating Output as Pydantic)
class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str
    



venue_task = Task(
    description="Find a venue in {event_city} "
                "that meets criteria for {event_topic}.",
    expected_output="All the details of a specifically chosen"
                    "venue you found to accommodate the event.",
    human_input=True,
    output_json=VenueDetails,
    output_file="venue_details.json",
     
      # Outputs the venue details as a JSON file
    agent=venue_coordinator
)

logistics_task = Task(
    description="Coordinate catering and "
                 "equipment for an event "
                 "with {expected_participants} participants "
                 "on {tentative_date}.",
    expected_output="Confirmation of all logistics arrangements "
                    "including catering and equipment setup.",
    human_input=True,
    async_execution=True,
    agent=logistics_manager
)


marketing_task = Task(
    description="Promote the {event_topic} "
                "aiming to engage at least"
                "{expected_participants} potential attendees.",
    expected_output="Report on marketing activities "
                    "and attendee engagement formatted as markdown.",
    async_execution=True,
    output_file="marketing_report.md",  # Outputs the report as a text file
    agent=marketing_communications_agent
)
#Since you set async_execution=True for logistics_task and marketing_task tasks, now the order for them does not matter in the tasks list.
# The order of tasks in the list does not affect the execution order when using async_execution=True.

# Define the crew with agents and tasks
event_management_crew = Crew(
    agents=[venue_coordinator,
            logistics_manager,
            marketing_communications_agent],

    tasks=[venue_task,
           logistics_task,
           marketing_task],

    verbose=True
)

# Define the event details

event_details = {
    'event_topic': " CampusX Tech Innovation Conference",
    'event_description': "A gathering of tech innovators "
                         "and industry leaders "
                         "to explore future technologies.",
    'event_city': "New Delhi",
    'tentative_date': "2025-06-30",
    'expected_participants': 500,
    'budget': 20000,
    'venue_type': "Conference Hall"
}

#result = event_management_crew.kickoff(inputs=event_details)

''''Since you set human_input=True for some tasks, the execution will ask for your input before it finishes running.
When it asks for feedback, use your mouse pointer to first click in the text box before typing anything.'''



