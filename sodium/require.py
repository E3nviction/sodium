from sodium import __version__, VERSION_LATEST
def require(version):
    """
    Require function

    :param version: str
    :return: str
    """
    if __version__ != version and version != VERSION_LATEST:
        raise ImportError("Requires Sodium v" + version)
    return version