#!/usr/bin/env python
import sys
import warnings
from pathlib import Path
from typing import List

from datetime import datetime

from legalassistant.crew import Legalassistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def _default_docx_inputs() -> dict:
    """Build a default inputs payload by discovering .docx files in the workspace `data` folder.

    Returns a dict with a `documents` list (absolute paths as strings). If no files found, returns an empty list.
    """

    data_dir = "../data"
    docx_files: List[str] = []
    if data_dir:
        docx_files = [str(p.resolve()) for p in data_dir.glob("*.docx")]
    return {
        "documents": docx_files,
        "current_year": str(datetime.now().year),
    }


def run():
    """Run the crew with discovered .docx documents (if any)."""
    inputs = _default_docx_inputs()
    try:
        Legalassistant().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         Legalassistant().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         Legalassistant().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
    
#     try:
#         Legalassistant().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
