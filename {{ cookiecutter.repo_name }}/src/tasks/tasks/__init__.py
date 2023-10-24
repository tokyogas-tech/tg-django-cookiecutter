import invoke

from . import backend, frontend, local

namespace = invoke.Collection()
namespace.add_collection(invoke.Collection.from_module(backend))
namespace.add_collection(invoke.Collection.from_module(frontend))
namespace.add_collection(invoke.Collection.from_module(local))
