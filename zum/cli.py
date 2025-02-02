"""
A module to route the zum CLI traffic.
"""

from argparse import ArgumentParser
from typing import Any, List, Optional

import zum
from zum.engine import Engine


def dispatcher(*args: Any, **kwargs: Any) -> None:
    """
    Main CLI method, recieves the command line action and dispatches it to
    the corresponding method.
    """
    engine = Engine()

    parser = generate_parser(engine.actions)
    parsed_args = parser.parse_args(*args, **kwargs)

    engine.execute(parsed_args.action[0], parsed_args.params)  # pragma: nocover
    log(engine.output)  # pragma: nocover


def generate_parser(actions_list: List[str]) -> ArgumentParser:
    """Generates the action parser."""
    warning = "Beware! No config file was found!" if not actions_list else ""

    # Create parser
    parser = ArgumentParser(
        description="Command line interface tool for zum.", epilog=warning
    )

    # Add version command
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"zum version {zum.__version__}",
    )

    if actions_list:
        # Add action argument
        parser.add_argument("action", choices=actions_list, nargs=1)

        # Add params
        parser.add_argument("params", nargs="*")

    return parser


def log(data: Optional[str]) -> None:
    """Logs a string to the console."""
    print(data)
