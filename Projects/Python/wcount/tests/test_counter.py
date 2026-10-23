from collections import Counter

from wcount.engine.counter import (
    CounterResult,
    build_tally,
    line_counter,
    run_counter,
    word_counter,
)


# Line Counter Tests
def test_line_counter_counts_three_lines() -> None:
    text = "first line\nsecond line\nthird line"
    assert line_counter(text) == 3


def test_line_counter_empty_string_returns_zero() -> None:
    text = ""
    assert line_counter(text) == 0


def test_line_counter_trailing_newline_does_not_add_a_line() -> None:
    text = "hello\n"
    assert line_counter(text) == 1


def test_line_counter_blank_line_in_middle_counts_as_a_line() -> None:
    text = "hello\n\nworld"
    assert line_counter(text) == 3


# Word Counter Tests
def test_word_counter_counts_words_across_lines() -> None:
    text = "one two\nthree four five"
    assert word_counter(text) == 5


def test_word_counter_empty_string_returns_zero() -> None:
    text = ""
    assert word_counter(text) == 0


# Build Tally Tests
def test_build_tally_counts_repeated_words() -> None:
    text = "the cat saw the dog and the bird"
    tally = build_tally(text)
    assert tally["the"] == 3
    assert tally["cat"] == 1


def test_build_tally_treats_different_capitalization_as_same_word() -> None:
    text = "The cat saw the dog and THE bird"
    assert build_tally(text)["the"] == 3


def test_build_tally_keys_are_lowercase() -> None:
    text = "Hello HELLO hello"
    assert build_tally(text) == Counter({"hello": 3})


# Run Counter Tests
def test_run_counter_combines_all_three_results() -> None:
    text = "the cat\nthe dog\nthe bird"
    result = run_counter(text)
    assert result == CounterResult(
        line_count=3,
        word_count=6,
        word_tally=Counter({"the": 3, "cat": 1, "dog": 1, "bird": 1}),
    )
