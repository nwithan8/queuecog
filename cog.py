from arcacog.utils import DynamicClassCreator
from cogs.queuecog.configuration import Config
from cogs.queuecog.queues.items import Items
from cogs.queuecog.queues.users import Users

queue_types_to_classes = {
    "user": Users,
    "item": Items
}


def setup(bot):
    config = Config(config_files=["config.yaml"])

    queue_classes = []
    for queue_type in config.queue_types:
        queue_class = queue_types_to_classes.get(queue_type, None)
        if queue_class is None:
            raise ValueError(f"Queue type {queue_type} is not supported")
        queue_classes.append(queue_class)

    creator = DynamicClassCreator()
    cog_class = creator(queue_classes)
    bot.add_cog(cog_class(bot))
