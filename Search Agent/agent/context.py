import os
import json

# context.py: Loads and formats local context data for the agent
# Retrieves household pets information from pets.json and formats it for agent prompts.

def load_pets_context() -> str:
    """
    Loads household pets data from pets.json and formats it as context for the agent.

    Returns:
        str: Formatted context string listing each pet and its description.
    """
    pets_path = os.path.join(os.path.dirname(__file__), "../data/pets.json")
    with open(pets_path, "r") as f:
        pets = json.load(f)

    # Format each pet as 'Name: Description' for context
    context = "\n".join(
        [f"{pet['name']}: {pet['description']}" for pet in pets]
    )
    return context
