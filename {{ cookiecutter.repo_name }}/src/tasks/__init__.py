import invoke
from . import backend
from . import local

namespace = invoke.Collection()
namespace.add_collection(invoke.Collection.from_module(backend))
namespace.add_collection(invoke.Collection.from_module(local))
