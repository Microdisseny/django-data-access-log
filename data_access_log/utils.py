def type_name(cls):
    """Get the name of a class."""
    if not cls:
        return '(none)'
    return '{}.{}'.format(cls.__module__, cls.__name__)


def viewset_model(serializer):
    """Get the model of a serializer."""
    if hasattr(serializer, 'serializer_class'):
        return serializer.serializer_class.Meta.model
    else:
        return None
