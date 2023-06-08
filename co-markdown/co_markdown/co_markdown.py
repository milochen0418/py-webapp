"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import pynecone as pc


class State(pc.State):
    """The app state."""
    mdtext: str = "Type markdown in left"
    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Collaborative Markdown", font_size="2em", w="100%"),
            pc.hstack(
                pc.vstack(
                    pc.text_area(
                        on_change=State.set_mdtext,
                        default_value="# Markdown Two  ## Document Test ![](https://user-images.githubusercontent.com/12568287/239189051-fb2ddd86-8bc4-49c8-8bbb-f7be3040b1fe.png)",
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
                    pc.markdown(State.mdtext),
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
