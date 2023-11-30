class TitleMixin: # Добавление заголовка
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data( **kwargs)
        context['title'] = self.title
        return context
