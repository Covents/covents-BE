from application import create_app
config_name = "development"
app = create_app(config_name)
if __name__ == "__main__":
    app.run()