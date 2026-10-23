from collections import Counter
from dataclasses import dataclass


@dataclass
class CounterResult:
    """Represent the result of the counter"""

    line_count: int
    word_count: int
    word_tally: Counter[str]


def word_counter(content: str) -> int:
    return len(content.split())


def line_counter(content: str) -> int:
    return len(content.splitlines())


def build_tally(content: str) -> Counter[str]:
    content = content.lower()
    return Counter(content.split())


def run_counter(content: str) -> CounterResult:
    return CounterResult(
        line_count=line_counter(content),
        word_count=word_counter(content),
        word_tally=build_tally(content),
    )
