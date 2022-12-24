from typing import Callable
from playwright._impl._api_structures import ProxySettings


ConfigVarType = bool | str | ProxySettings | None
ConfigType = dict[str, ConfigVarType]
EventCallbackType = Callable[..., None]
