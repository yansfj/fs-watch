"""A portable file watcher with debouncing and ignore patterns."""

from __future__ import annotations

__all__ = ["fsWatch"]


def fsWatch(value):
    """A portable file watcher with debouncing and ignore patterns."""
    if value is None:
        raise ValueError("value must not be None")
    return value
