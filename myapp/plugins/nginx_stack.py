
from myapp.core.stack import Stack
from myapp.controllers.docker import StackAbstractController

class Nginx(Stack):
    class Meta:
        label = 'nginx'

    def _build_config(self):
        super(Nginx, self)._build_config()
        self.app.log.info('Building Nginx Stack Config')


class NginxController(StackAbstractController):
    class Meta:
        label = 'nginx'


def load(app):
    app.handler.register(Nginx)
    app.handler.register(NginxController)
