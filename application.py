from locate_chrome import get_path
from subprocess import Popen
from local_server import local_server

class Application():
    def __init__(self):
        pass

    def quit(self):
        for window in self.window_array:
            window.exit()

    class Window():
        def __init__(self):
            self.window_width = 1040
            self.window_height = 1080
            self.launch_as_app = True
            self.window_html = ''
            self.no_gpu = True

        def create(self, *args, **kwargs):
            # ------------------------------ #
            # Launches Google Chrome and navigates to Flask server
            # ------------------------------ #

            for arg in kwargs:
                if arg == "height":
                    self.window_height = kwargs[arg]
                elif arg == "width":
                    self.window_width = kwargs[arg]
                elif arg == "html":
                    self.window_html = kwargs[arg]

            local_server().create(8081, self.window_html)
            args = [get_path(), '--app=http://localhost:8081']

            Popen(args, shell=False)

if __name__ == "__main__":
    Application().Window().create(html='<title>My first app</title><p>Hello, world</p>')
