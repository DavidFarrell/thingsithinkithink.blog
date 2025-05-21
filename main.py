from fasthtml.common import *
from starlette.staticfiles import StaticFiles

# Attempt to set MonsterUI theme
app,rt = fast_app(theme='monster-blue')

# Mount static files directory
app.mount('/static', StaticFiles(directory='static'), name='static')

# --- Layout Components ---

def render_header():
    return Header(
        Div(
            H1("My Migrated Blog"),
            Nav(
                A("Home", href="/"), " | ",
                A("About", href="/about/")
            ),
            # Assuming MonsterUI theme will style <hr> or provide classes for borders
            # For now, a simple Hr() or rely on theme.
            Hr() 
        )
    )

def render_footer():
    return Footer(
        Div(
            Hr(),
            P("© 2024 My Migrated Blog")
        )
    )

def render_layout(*page_content):
    # Using Div as a main container; if fasthtml.common has Main, that would be more semantic.
    # For MonsterUI, specific container classes might be needed, but theme should provide defaults.
    return Body(
        render_header(),
        Main(*page_content), # Using Main if available, otherwise Div
        render_footer(),
        # MonsterUI might inject styles/scripts here or via fast_app configuration.
        # For now, relying on the theme parameter in fast_app.
    )

import importlib.util
import sys
from pathlib import Path

# --- Route Handlers ---

@rt('/')
def get(): 
    content = Div(P('Hello World! (Homepage Content)'), hx_get="/change")
    # Potentially list posts here in the future
    return render_layout(content)

@rt('/change')
def get_change(): 
    content = P('Content has changed via HTMX!')
    return render_layout(content) # Or just return content if it's a true partial

def load_content_data(filepath: Path):
    """Loads POST_DATA or PAGE_DATA from a Python file."""
    if not filepath.exists():
        return None
    
    module_name = filepath.stem
    spec = importlib.util.spec_from_file_location(module_name, str(filepath))
    if spec is None or spec.loader is None:
        return None # Should not happen if file exists
        
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module # Optional: add to sys.modules
    spec.loader.exec_module(module)
    
    if hasattr(module, 'POST_DATA'):
        return module.POST_DATA
    elif hasattr(module, 'PAGE_DATA'):
        return module.PAGE_DATA
    return None

@rt('/posts/{slug_path:path}') # Using :path to capture everything, including potential slashes if slug contains them
def post_detail(slug_path:str):
    # Convert URL slug to a potential filename.
    # Original slugs: /12-05-things-i-think-i-think/ -> 12-05-things-i-think-i-think
    # We need to map the slug_path from URL to the python filename.
    # For simplicity, assuming slug_path matches the .py filename stem.
    # Example: /posts/things_i_think_i_think_big will try to load things_i_think_i_think_big.py
    
    # Remove leading/trailing slashes if any from slug_path for filename matching
    cleaned_slug = slug_path.strip('/') 
    
    # Construct the path to the Python data file
    # This assumes slugs in URLs directly map to filenames (without .py)
    # e.g. /posts/my-post-slug tries to load app_content/posts/my-post-slug.py
    data_file = Path("app_content/posts") / f"{cleaned_slug}.py"
    
    post_data = load_content_data(data_file)
    
    if post_data:
        # Using Div for body for now. Markdown component later.
        content = Div(
            H1(post_data.get('title', 'No Title')),
            P(f"Date: {post_data.get('date', 'No Date')}"),
            Figure(
                Img(src=post_data.get('image', ''), alt=post_data.get('title', 'Post image')) if post_data.get('image') else '',
                Figcaption(post_data.get('caption', '')) if post_data.get('caption') and post_data.get('image') else ''
            ) if post_data.get('image') else '',
            Hr(),
            Div(post_data.get('body', 'No content available.')) # Render body as is (plain text/markdown string)
        )
        # Update page title if possible (FastHTML might have a way to set <title>)
        # For now, the H1 serves as the main title on page.
        return render_layout(Title(post_data.get('title', 'Blog Post')), content)
    else:
        content = Div(H1("Post Not Found"), P(f"Could not find content for slug: {slug_path} or file {data_file}"))
        return render_layout(Title("Post Not Found"), content)


@rt('/about')
def about_page_route(): # Renamed function to be more specific
    data_file = Path("app_content/pages/about.py")
    page_data = load_content_data(data_file)
    
    if page_data:
        # Also display image for about page if available
        image_html = ''
        if page_data.get('image'):
            image_html = Figure(
                Img(src=page_data.get('image', ''), alt=page_data.get('title', 'Page image')),
                Figcaption(page_data.get('caption', '')) if page_data.get('caption') else ''
            )

        content = Div(
            H1(page_data.get('title', 'About Us')),
            image_html if page_data.get('image') else '',
            Hr(),
            Div(page_data.get('body', 'No content available.')) # Render body as is
        )
        return render_layout(Title(page_data.get('title', 'About Us')), content)
    else:
        content = Div(H1("About Page Not Found"), P("Could not load about page content."))
        return render_layout(Title("Page Not Found"), content)

serve()
