from render_engine.hookspecs import hook_impl
from render_engine.site import Site
import logging
import pytailwindcss
import pathlib


def parse_css_files(
        static_path: str | pathlib.Path,
        output_path: str|pathlib.Path,
        ) -> None:

    """Parses CSS files in directory and create a file for each in the output_path"""
    print(list(pathlib.Path(static_path).rglob("**/*.css")))
    for file in pathlib.Path(static_path).rglob("**/*.css"):
        logging.info(f"Running Tailwind on {file}")
        output_file = pathlib.Path(output_path) \
            .joinpath(static_path) \
            .joinpath(file.relative_to(static_path)) \
            .absolute()
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
    def post_build_site(site: Site) -> None:
        print("running_post_build_site")
        parse_css_files(site.static_path, site.output_path)
