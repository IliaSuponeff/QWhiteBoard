import sys, os
from argparse import ArgumentParser, Namespace
from typing import Dict


def load_runtime_namespace(*args) -> Namespace:
    """
    Load the runtime namespace using the given arguments.

    :param args: The command line arguments to parse.
    :return: The parsed command line arguments as a Namespace object.
    """
    parser = ArgumentParser(
        "UI Templates Converter",
        description="Program to converting *.ui files of QT framework to python scripts files",
    )
    parser.add_argument("--verbose", "-v", action="store_true", default=False,
                        help="set flag of verbose execution as true")
    parser.add_argument("--version", action='version', version='%(prog)s 1.0')

    return parser.parse_args(args)


def init_dirs() -> dict[str, str]:
    """
    Initialize the required directories for the application.

    Returns:
        A dictionary containing the paths to the required directories.
        The keys are the names of the directories and the values are
        the corresponding paths.

    Raises:
        None.
    """
    return {
        "TEMLPATESDIR": os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "files"
        ),
        "CONVERTDIR": os.path.join(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            ),
            "src",
            "views"
        )
    }


def main(ns: Namespace) -> int:
    """
    The main function that initializes the program, finds all *.ui templates, converts them to Python scripts,
    and closes the program.

    Parameters:
    - ns (Namespace): The Namespace object containing the command-line arguments and options.

    Returns:
    - int: The exit code of the program. Returns 0 if the program executes successfully, -1 otherwise.
    """
    print("Initialize program")
    DIRS = init_dirs()

    for dir_type in DIRS:
        if ns.verbose:
            print(f"\tInit {DIRS[dir_type]} directory")

        if not os.path.exists(DIRS[dir_type]):
            os.makedirs(DIRS[dir_type])

    print("Find all *.ui templates")
    templates = os.listdir(DIRS["TEMLPATESDIR"])
    for template in templates.copy():
        templates.remove(template)
        template_path = os.path.join(DIRS["TEMLPATESDIR"], template)
        if not os.path.isfile(template_path):
            continue

        if not template.endswith(".ui") and len(template.strip()) >= 4:
            continue

        templates.append(template_path)
        if ns.verbose:
            print(f"\tFind template: {template_path}")

    if len(templates) == 0:
        print("\tError: Not found *.ui templates", file=sys.stderr)
        return -1

    print("Converting UI-templates to Python-scripts")
    for template in templates:
        template_filename = os.path.basename(template)
        result_path = os.path.join(
            DIRS["CONVERTDIR"], f"ui_{template_filename.replace('.ui', '.py')}"
        )
        if ns.verbose:
            print(f"\tConvert {template} to {result_path}")

        os.system(
            f"pyside6-uic {template} -o {result_path}"
        )

        if not os.path.exists(result_path):
            continue

        data = []
        with open(result_path, "r", encoding="UTF-8") as f:
            data = f.readlines()

        data = [line.replace("    ", "\t") for line in data]
        with open(result_path, "w", encoding="UTF-8") as f:
            for line in data:
                f.write(line)

    print("Closing program")
    return 0


if __name__ == "__main__":
    sys.exit(
        main(
            load_runtime_namespace(*sys.argv[1:])
        )
    )
