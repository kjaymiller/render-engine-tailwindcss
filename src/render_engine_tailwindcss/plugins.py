from render_engine.hookspecs import hook_impl
import pytailwindcss
import pathlib

class TailwindCSS:
    @hook_impl
    def post_build_site(site: "Site"):
        print("Running TailwindCSS")
        for file in pathlib.Path(site.static_path).glob("**/*.css"):
            print(f"Running TailwindCSS on {file}")
            pytailwindcss.run(
                auto_install=True,
                tailwindcss_cli_args=[
                    "--input",
                    f"{file.absolute()}",
                    "--output",
                    f"{pathlib.Path(site.output_path / file).absolute()}",
                ],
            )