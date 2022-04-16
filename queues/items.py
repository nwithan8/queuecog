from typing import Union, Optional

import discord
from discord.ext.bridge import bridge_command, BridgeContext

from arcacog import discord_decorators, discord_utils, SlashCommandGroup, ArcaFilePath

from cogs.queuecog.database import QueueDatabase, ItemQueueEntry
from cogs.queuecog.queues.base import Base

from cogs.queuecog.utils import get_queue_cog_file_path


class Items(Base):
    items_group = SlashCommandGroup(name="item-queue", description="Commands related to queuing items.")

    def __init__(self, bot):
        super().__init__(bot=bot)
        self.items_queue_database = QueueDatabase(
            sqlite_file=get_queue_cog_file_path(file_path="queue.db"), table_schemas=[ItemQueueEntry])

    @items_group.command(name="export")
    @discord_decorators.is_admin
    async def queue_export(self, ctx: BridgeContext):
        """
        Export the queue to a CSV.
        """
        if not self.users_queue_database.export_item_queue_to_csv(
                get_queue_cog_file_path(file_path="item_queue.csv")):
            await discord_utils.send_error(ctx=ctx)
            return
        await ctx.send(file=discord.File(
            get_queue_cog_file_path(file_path="item_queue.csv")))
