from django.views import View
from django.shortcuts import render


class DemoView(View):

    template_name = 'websockets/demo.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {})
