import sanic
import routes

app = sanic.Sanic("backend")
app.config.FALLBACK_ERROR_FORMAT = "auto"
prefix = routes.routes_v1[0]

for route in routes.routes_v1[1]:
    app.add_route(
        handler=route[1],
        uri=f"/{prefix}{route[0]}",
    )
