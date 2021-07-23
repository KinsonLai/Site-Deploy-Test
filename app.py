from website import create_app
import sys

app = create_app()
freezer = Freezer(app)

if __name__ == '__main__':
    app.run(debug=True)
