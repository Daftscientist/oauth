""" The index view file """

""" Login with credentials """

from sanic import Request
from core.responses import Success
from sanic.views import HTTPMethodView

class CredsView(HTTPMethodView):
    """The index view."""

    async def post(self, request: Request):
        return await Success(request, 'I am async post method')
    