from abc import ABC, abstractmethod
class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass


class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)


class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")


class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)

a = HtmlFormatted()
report = Report('заголовок отчета', 'это текст отчета, его тут много', TextFormatted())
report = Report('заголовок отчета', 'это текст отчета, его тут много', a)

report.docPrinter()