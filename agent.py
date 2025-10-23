"""
Book Generation Agent using OpenAI Agents SDK.
Creates educational content following a 5-stage teaching methodology.
"""

import asyncio
import os
import sys
import argparse
import re
from dotenv import load_dotenv

from agents import Agent, Runner
from system_prompt import SYSTEM_PROMPT


load_dotenv()


def print_utf8(text: str) -> None:
    """Print text safely, handling potential UnicodeEncodeError on some consoles."""
    try:
        sys.stdout.write(text)
        sys.stdout.write("\n")
    except UnicodeEncodeError:
        sys.stdout.buffer.write((text + "\n").encode("utf-8", errors="replace"))


async def main() -> int:
    """Run the minimal book_generation_agent from the command line."""
    if not os.getenv("OPENAI_API_KEY"):
        sys.stderr.write("ERROR: OPENAI_API_KEY is not set\n")
        sys.stderr.write("\nWindows (PowerShell): $env:OPENAI_API_KEY=\"sk-...\"\n")
        sys.stderr.write("Linux/Mac: export OPENAI_API_KEY=\"sk-...\"\n\n")
        return 1

    parser = argparse.ArgumentParser(description="Run book_generation_agent")
    parser.add_argument("request", nargs="?", help="User request or topic to generate")
    args = parser.parse_args()

    request: str
    if args.request:
        request = args.request
    else:
        try:
            request = input("Enter your request: ").strip()
        except EOFError:
            sys.stderr.write("ERROR: No input provided\n")
            return 1

    if not request:
        sys.stderr.write("ERROR: Empty request provided\n")
        return 1

    try:
        agent = Agent(name="book_generation_agent", instructions=SYSTEM_PROMPT)
        result = await Runner.run(agent, request)
        output = getattr(result, "final_output", None) or ""

        # Ensure output directory exists
        books_dir = os.path.join(os.getcwd(), "books")
        os.makedirs(books_dir, exist_ok=True)

        # Create a safe filename from the topic/request
        def make_filename_from_topic(topic: str) -> str:
            base = topic.strip().lower()
            slug = re.sub(r"[^a-z0-9]+", "_", base)
            slug = slug.strip("_") or "output"
            return f"{slug}.md"

        filepath = os.path.join(books_dir, make_filename_from_topic(request))

        # Write output to file using UTF-8
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(output)

        # Print only the saved path
        print_utf8(filepath)
        return 0
    except KeyboardInterrupt:
        sys.stderr.write("\nCancelled.\n")
        return 130
    except Exception as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
