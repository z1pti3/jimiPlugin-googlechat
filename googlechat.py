from core import plugin, model

class _googlechat(plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        model.registerModel("googlechatWebHook","_googlechatWebHook","_action","plugins.googlechat.models.action")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("googlechatWebHook","_googlechatWebHook","_action","plugins.googlechat.models.action")
        return True

    