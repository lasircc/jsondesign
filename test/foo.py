import jsonschema as j  


def las_uri_handler():
    pass

_resolver = j.RefResolver(base_uri="", handlers={"las": las_uri_handler}, referrer=None, cache_remote=True)


