import importlib
import sys
from collections.abc import Generator
from contextlib import contextmanager
from io import StringIO


class ModuleRunner:
    """
    A utility class for executing and testing Python modules, specifically 
    designed for initial homework assignments (TPs) in programming courses.

    This class is particularly useful in scenarios where students are required 
    to solve exercises without using functions, as functions are not introduced 
    at the beginning of the course. Students typically need to write programs 
    that interact solely through inputs and outputs. ModuleRunner facilitates 
    the automated testing of such programs by managing the standard input/output 
    streams during the module's execution and capturing the output for 
    verification.

    Author: Laurent Bourgon

    Attributes:
        module_to_run_name (str): Name of the module to be run.

    Methods:
        run(stdin_input: str = ""): Executes the module, capturing its output.
        __run_module(): Handles the actual execution of the module.
        __catch_io(stdin_input: str = ""): Context manager for IO redirection.
    """

    def __init__(self, module_to_run_name: str) -> None:
        self.module_to_run_name = module_to_run_name

    def run(self, stdin_input: str = "") -> str:
        with self.__catch_io(stdin_input) as output:
            self.__run_module()
            return output.getvalue()

    def __run_module(self) -> None:
        module = sys.modules.get(self.module_to_run_name)

        if module is not None:
            importlib.reload(module)
        else:
            importlib.import_module(self.module_to_run_name)

    @contextmanager
    def __catch_io(self, stdin_input: str = "") -> Generator[StringIO, None, None]:
        old_stdout = sys.stdout
        old_stdin = sys.stdin

        try:
            sys.stdout = StringIO()
            sys.stdin = StringIO(stdin_input)

            yield sys.stdout
        finally:
            sys.stdout = old_stdout
            sys.stdin = old_stdin
