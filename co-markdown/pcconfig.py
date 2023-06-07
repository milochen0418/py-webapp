import pynecone as pc

class ComarkdownConfig(pc.Config):
    pass

config = ComarkdownConfig(
    app_name="co_markdown",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)