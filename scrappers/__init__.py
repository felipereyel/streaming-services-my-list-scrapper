from . import netflix
from . import primevideo

runners = {
    "netflix": netflix.run,
    "primevideo": primevideo.run,
}
