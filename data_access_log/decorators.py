from django.contrib.auth.models import AnonymousUser
from functools import wraps

from .utils import type_name, viewset_model


def data_access_log(viewset):
    """Add it to a ViewSet that you'd like to log."""
    dispatch = viewset.dispatch
    viewset_name = type_name(viewset)
    model_name = type_name(viewset_model(viewset))

    @wraps(dispatch)
    def wrapper(other, request, *args, **kwargs):
        from .models import DataAccessLog

        response = dispatch(other, request, *args, **kwargs)
        if response:
            if type(request.user) is AnonymousUser:
                username = '(anonymous user)'
            else:
                username = request.user.username
            if hasattr(response, 'rendered_content'):
                rendered_content = response.rendered_content
            else:
                rendered_content = response.getvalue()
            log = DataAccessLog(
                model=model_name,
                viewset=viewset_name,
                url=request.build_absolute_uri(),
                user=username,
                response=rendered_content,
            )
            log.save()
        return response

    viewset.dispatch = wrapper
    return viewset
