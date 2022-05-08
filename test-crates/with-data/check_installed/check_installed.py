from pathlib import Path

import with_data

assert with_data.lib.one() == 1
assert with_data.ffi.string(with_data.lib.say_hello()).decode() == "hello"
venv_root = Path(with_data.__file__).parent.parent.parent.parent.parent
installed_data = (
    venv_root.joinpath("data_subdir").joinpath("hello.txt").read_text().strip()
)
assert installed_data == "Hi! 😊"
assert (
    venv_root.joinpath("include")
    .joinpath("site")
    .joinpath("python3.8")
    .joinpath("with-data")
    .joinpath("empty.h")
    .is_file()
)
print("SUCCESS")
