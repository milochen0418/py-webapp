"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import pynecone as pc


class State(pc.State):
    """The app state."""
    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Collaborative Markdown", font_size="2em", w="100%"),
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
                    bg="#ededed",
                    margin="0em",
                    padding="1em",
                    border_radius="0.5em",
                    shadow="lg",
                    w="100%",
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
                    bg="#ededed",
                    margin="0em",
                    padding="1em",
                    border_radius="0.5em",
                    shadow="lg",
                    w="100%",
                ),
                spacing="0.5em",
                w="100%",
                
            ),
            spacing="1.5em",
            font_size="2em",
            w="100%",
            margin="0.5em",
        ),
        w="100%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
