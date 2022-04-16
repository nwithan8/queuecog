from discord.ext.commands import Context

from arcacog import ArcaCogConfig, ArcaCog, SlashCommandGroup


class Base(ArcaCog):
    # slash command groups
    queue_group = SlashCommandGroup(name="queue", description="Commands related to general queuing.")

    def __init__(self, bot):
        super().__init__(bot=bot, config=ArcaCogConfig(folder="queuecog", name="queues", config_files=["config.yaml"]))

    @queue_group.command(name="ping")
    async def queue_ping(self, ctx: Context):
        """
        Test command to check if the bot is working.
        """
        await ctx.send("Pong!")
