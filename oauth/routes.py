""" Route declarations """

from api.index import IndexView

routes_v1 = [
    "api/v1", # route prefix
    [
        # --- General ---
        ["/", IndexView.as_view()],
    ]
]