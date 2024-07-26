from sodium import __version__
def require(version):
    """
    Require function

    :param version: str
    :return: str
    """
    if __version__ != version:
        raise ImportError("Requires Sodium v" + version)
    return version