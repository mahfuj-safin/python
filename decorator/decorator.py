def dashboard():
  print("Welcome to website")


def login_required(func):

  def wrapper():
    print("Checking login...............")
    func()

  return wrapper

dashboard = login_required(dashboard)
dashboard()