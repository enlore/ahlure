from ahlure import create_app

app = create_app()
app.debug = True
app.run(port=9001)
