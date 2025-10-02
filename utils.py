#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""Utility functions for picker"""

from __future__ import annotations
import os
import pprint
import subprocess
from typing import Any, Optional

from colorama import Fore


class Color:
    """Terminal color output helper"""

    @staticmethod
    def print_focus(data: str) -> None:
        """Print focused message in yellow"""
        print(Fore.YELLOW + data + Fore.RESET)

    @staticmethod
    def print_success(data: str) -> None:
        """Print success message in green"""
        print(Fore.LIGHTGREEN_EX + data + Fore.RESET)

    @staticmethod
    def print_failed(data: str) -> None:
        """Print failure message in red"""
        print(Fore.LIGHTRED_EX + data + Fore.RESET)

    @staticmethod
    def print(data: Any) -> None:
        """Pretty print any data structure"""
        pprint.pprint(data)


def popen(cmd: str) -> str:
    """
    Execute shell command and return output

    Args:
        cmd: Shell command to execute

    Returns:
        Command output as string
    """
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).stdout as source:
        return source.read().decode(encoding="utf-8")


def getenv(key_name: str, pick: bool = False) -> Optional[str]:
    """
    Get environment variable with optional PICKER_ prefix

    Args:
        key_name: Environment variable name
        pick: If True, try PICKER_ prefixed version first

    Returns:
        Environment variable value or None
    """
    if pick:
        if key := os.getenv(f"PICKER_{key_name}"):
            return key
        return os.getenv(key_name)
    return os.getenv(key_name)
