from screen import *
from graph import *

if __name__ == '__main__':
    graph = Graph(4)
    app = QApplication(sys.argv)
    ex = Widget(graph)

    ex.resize(1920, 1080)
    ex.show()
    sys.exit(app.exec_())
