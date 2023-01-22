# Render Engine TailwindCSS Plugin

Add tailwindcss to your Render Engine site.

[TailwindCSS](https://tailwindcss.com) is a utility-first CSS framework for rapidly building custom designs.

The [pytailwindcss](https://pypi.org/project/pytailwindcss/) package is used to install compile the tailwindcss stylesheets without the need of npm.

This plugin installs builds a tailwindcss file from the default configuration and adds a `tailwind.css` file to your static files.

> ***Warning***: This is in early development.

## Installation

Install the extension with pip:

    pip install render-engine-tailwindcss

## Usage

1. Import the plugin.

    ```python
    # app.py

    from render_engine import Site
    from render_engine_tailwindcss import TailwindCSS
    ```

2. Add the plugin to your site.

    ```python
    # app.py

    class site(Site):

        static_path = 'static'
        plugins=[
            TailwindCSS(),
        ]

    )
    ```

3. In your 'static_path', add your pre-tailwindcss stylesheets.

    ```css
    # static/styles.css

    @tailwind base;
    @tailwind components;
    @tailwind utilities; 
    ```

You can add multiple CSS files to the static path and they will all converted into their own files.