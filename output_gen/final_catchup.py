import logging

from crewai import Crew
from IPython.display import Markdown

from agent import agent_editor, agent_planner, agent_writer
from task import task_edit, task_plan, task_write

logging.basicConfig(level=logging.INFO)


def final_response(topic: str):
    crew = Crew(
        agents=[agent_planner(), agent_writer(), agent_editor()],
        tasks=[task_plan(), task_write(), task_edit()],
        verbose=1,
    )
    # crew = Crew(agents=[planner, writer, editor], tasks=[plan, write, edit], verbose=2)
    result = crew.kickoff(inputs={"topic": topic})
    return result
    # return Markdown(result)
