"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""
    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.hstack(
        
                pc.vstack(
                    pc.markdown("""
                    # Markdown One
                    ## Document Test
                    - This is a book
                    - This is book 2
                    - This is item 3
                    """
                    ),
                    align_items="left",
                ),
                pc.vstack(
                    pc.markdown("""
                    # Markdown Two
                    ## Document Test
                    - This is a book
                    - This is book 2
                    - This is item 3
                    ## Document Test 2
                    - This is a book A
                    - This is book B
                    - This is item C
                    """
                    ),
                    align_items="left",
                ),
                spacing="1em",
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
