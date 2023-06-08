"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import pynecone as pc
import asyncio

async def set_state_mdtext(mdtext:str):
    keys = list(app.state_manager.states) #convert the keys of dict into the list
    ret_mdtext: int = mdtext
    for token in keys: # change state.count for all current running frontend
        state = app.state_manager.get_state(token)
        state.mdtext = mdtext
        app.state_manager.set_state(token, state)
    return {"state_mdtext":ret_mdtext}

class State(pc.State):
    """The app state."""
    mdtext: str = "Type markdown in left"
    async def mdtext_change(self, new_mdtext:str):
        self.mdtext = new_mdtext
        await set_state_mdtext(self.mdtext)
        
    async def tick(self):
        # run tick for update frontend ui for updating count
        if self.is_run_tick:
            await asyncio.sleep(0.5)
            return self.tick
        
    async def onload(self):
        self.is_run_tick = True
        return self.tick
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

print("Hint:You can open http://localhost:8000/state_mdtext/33 to set mdtext value as 33")

# Add state and page to the app.
app = pc.App(state=State)
app.api.add_api_route("/state_mdtext/{mdtext}", set_state_mdtext)
app.add_page(
    index,
    title = "Collaborative Markdown App",
    description = "A collaborative markdown app",
    meta = [
        {"name": "theme_color", "content": "#FFFFFF"},
        {"char_set": "UTF-8"},
        {"property": "og:url", "content": "url"},
    ],    
    on_load = State.onload,
)
app.compile()
