import logging

from crewai import Agent

from llm_model import chat_bot_llm

logging.basicConfig(level=logging.INFO)


def agent_planner():
    planner = Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory="You're working on planning a blog article "
        "about the topic: {topic}."
        "You collect information that helps the "
        "audience learn something "
        "and make informed decisions. "
        "Your work is the basis for "
        "the Content Writer to write an article on this topic.",
        allow_delegation=False,
        verbose=False,
        llm=chat_bot_llm(),
    )

    return planner
