
from cement import Controller, ex

class Docker(Controller):
    class Meta:
        label = 'docker'
        stacked_on = 'base'
        stacked_type = 'nested'

class StackAbstractController(Controller):
    class Meta:
        stacked_on = 'docker'
        stacked_type = 'nested'

    def _get_stack_handler(self):
        return self.app.handler.get('stack', self._meta.label, setup=True)

    @ex(help='build stack config')
    def build_config(self):
        s = self._get_stack_handler()
        s.build_config()

    @ex(help='start stack')
    def start(self):
        s = self._get_stack_handler()
        s.start()

    @ex(help='stop stack')
    def stop(self):
        s = self._get_stack_handler()
        s.stop()

    @ex(help='restart stack')
    def restart(self):
        s = self._get_stack_handler()
        s.restart()
