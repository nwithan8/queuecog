from arcacog import ArcaFilePath


def get_queue_cog_file_path(file_path: str) -> str:
    return ArcaFilePath(cog_name="queuecog", file_path=file_path).path
