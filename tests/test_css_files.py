import pathlib
import dataclasses

import pytest

from render_engine_tailwindcss.plugins import parse_css_files

css_text = """
@tailwind base;
@tailwind components;
@tailwind utilities;
"""


def test_each_file_modified(tmp_path):
    """Tests that each .css file creates a corresponding .css file in the output directory."""
    static_path = tmp_path.joinpath("static")
    static_path.mkdir()

    static_path.joinpath("style1.css").write_text(css_text)
    static_path.joinpath("style2.css").write_text(css_text)

    # Create an output folder
    output_path = tmp_path.joinpath("output")

    # Create a site object
    parse_css_files(static_path, output_path) 
    assert len(list(output_path.iterdir())) == 2


def test_files_are_recursive(tmp_path):
    """Tests that each .css file creates a corresponding .css file in the output directory."""
    static_path = tmp_path.joinpath("static")
    static_path2 = static_path.joinpath("pre")
    static_path.mkdir()
    static_path2.mkdir()

    static_path.joinpath("style1.css").write_text(css_text)
    static_path2.joinpath("style2.css").write_text(css_text)

    # Create an output folder
    output_path = tmp_path.joinpath("output")
    
    # Create a site object
    parse_css_files(static_path, output_path) 
    assert len(list(output_path.glob("*.css"))) == 1
    assert len(list(pathlib.Path(output_path / "pre").glob("*.css"))) == 1


def test_non_css_files_are_ignored(tmp_path):
    """Tests that non .css files are ignored."""
    static_path = tmp_path.joinpath("static")
    output_path = tmp_path.joinpath("output")

    static_path.mkdir()
    static_path.joinpath("style1.css").write_text(css_text)
    static_path.joinpath("other_file.txt").write_text("No File")
    # Create a site object
    parse_css_files(static_path, output_path) 
    assert len(list(output_path.iterdir())) == 1