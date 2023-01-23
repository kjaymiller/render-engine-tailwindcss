from render_engine.hookspecs import hook_impl
import pytailwindcss
import pathlib


def parse_css_files(
        static_path: str | pathlib.Path,
        output_path: str|pathlib.Path,
        ) -> None:

    """Parses the CSS files in the directory and creates a file for each in the output_path"""
    for file in pathlib.Path(static_path).glob("**/*.css"):
        output_file = pathlib.Path(output_path / file.relative_to(static_path)).absolute()
        pytailwindcss.run(
            auto_install=True,
            tailwindcss_cli_args=[
                "--input",
                f"{file.absolute()}",
                "--output",
                output_file,
            ],
        )

class TailwindCSS:
    @hook_impl
    def post_build_site(site: "Site"):
        parse_css_files(site.static_path, site.output_path)
