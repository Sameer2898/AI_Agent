from crewai import Task

from agent import agent_writer


def task_write():
    write = Task(
        description=(
            "1. Use the content plan to craft a compelling "
            "blog post on {topic}.\n"
            "2. Incorporate SEO keywords naturally.\n"
            "3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
            "4. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
            "5. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
        ),
        expected_output="A well-written blog post "
        "in markdown format, ready for publication, "
        "each section should have 2 or 3 paragraphs.",
        agent=agent_writer(),
    )

    return write
