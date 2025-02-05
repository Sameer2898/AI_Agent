from crewai import Task

from agent import agent_editor


def task_edit():
    edit = Task(
        description=(
            "Proofread the given blog post for "
            "grammatical errors and "
            "alignment with the brand's voice."
        ),
        expected_output="A well-written blog post in markdown format, "
        "ready for publication, "
        "each section should have 2 or 3 paragraphs.",
        agent=agent_editor(),
    )

    return edit
