from rsserpent.models import Persona, Plugin

from . import route


plugin = Plugin(
    name="rsserpent-plugin-fulltext",
    author=Persona(
        name="wuzhongyi1105",
        link="https://github.com/wuzhongyi1105",
        email="dw@watelier.cn",
    ),
    prefix="/fulltext",
    repository="https://github.com/wuzhongyi1105/rsserpent-plugin-fulltext",
    routers={route.path: route.provider},
)
