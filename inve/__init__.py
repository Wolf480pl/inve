import os
from virtualenv.activation.via_template import ViaTemplateActivator

class InveActivator(ViaTemplateActivator):
    def templates(self):
        yield "inve.sh"

    def as_name(self, template):
        return "inve"

    def generate(self, creator):
        generated = super().generate(creator)
        for f in generated:
            os.chmod(f, 0o755)
