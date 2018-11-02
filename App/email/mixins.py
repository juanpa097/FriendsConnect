import threading
from os import environ

from django.template import loader
from django.core.mail import EmailMessage

class EmailThread(threading.Thread):
    def __init__(self,
                 template,
                 data,
                 receivers=None,
                 sender=None,
    ):
        self.subject = template.get('subject', 'Error')
        self.receivers = \
            receivers or [environ.get('DEFAULT_RECEIVER_EMAIL', '')]
        template_path = template.get('path', 'error.html')
        self.content = self._render_template(template_path, data)
        self.sender = sender or environ.get('DEFAULT_SENDER_EMAIL', '')
        threading.Thread.__init__(self)

    def run(self):
        message = EmailMessage(
            subject=self.subject,
            body=self.content,
            from_email=self.sender,
            to=self.receivers
        )
        message.content_subtype = 'html'
        message.send()

    def _render_template(self, template_path, data):
        rendered = ""
        try:
            template = loader.get_template(template_path)
            rendered = template.render(data)
        except Exception:
            print('The template {0} could not be found'.format(template_path))
        return rendered
