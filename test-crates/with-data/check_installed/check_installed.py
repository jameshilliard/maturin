import sys
from pathlib import Path

import with_data

assert with_data.lib.one() == 1
assert with_data.ffi.string(with_data.lib.say_hello()).decode() == "hello"

venv_root = Path(sys.prefix)

try:
    installed_data = (
        venv_root.joinpath("data_subdir").joinpath("hello.txt").read_text().strip()
    )
    assert installed_data == "Hi! 😊"
    header_file = (
        venv_root.joinpath("include")
        .joinpath("site")
        .joinpath(f"python{sys.version_info.major}.{sys.version_info.minor}")
        .joinpath("with-data")
        .joinpath("empty.h")
    )
    assert header_file.is_file(), header_file
except (AssertionError, FileNotFoundError):
    print("__file__", __file__)
    print("venv_root", venv_root)
    # Debugging help
    for i in sorted(venv_root.glob("**/*")):
        print(i)
    raise
print("SUCCESS")
