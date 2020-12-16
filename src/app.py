from core import app
from config import port, is_debug


if __name__ == '__main__':
    print(app.url_map)
    app.run(port=port, debug=is_debug)
