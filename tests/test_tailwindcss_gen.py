import pathlib
from render_engine import Site, Page
from render_engine_tailwindcss.plugins import TailwindCSS

def test_config_file_path_default():
    """Tests that the config file is generated if it doesn't already exist."""
    site = Site()
    site.register_plugins(TailwindCSS)

    assert site.plugin_manager.plugin_settings['TailwindCSS']['tailwindcss_config_file'] == "tailwind.config.js"


def test_config_file_gen(tmp_path):
    output_path = tmp_path / "output"
    config_path = tmp_path / "tailwind.config.js"
    
    site = Site()
    site.output_path = output_path
    site.register_plugins(TailwindCSS, TailwindCSS={"tailwindcss_config_file": config_path})
    assert site.plugin_manager.plugin_settings['TailwindCSS']['tailwindcss_config_file'] == config_path

    assert not config_path.exists()

    @site.page
    class Index(Page):
        template = "page.html"

    site.render()

    assert config_path.exists()