try:
    import sys
    import os

    print("Installing the python modules required for the tools:")

    if sys.platform.startswith("win"):
        os.system("pip install -r requirements.txt")
        os.system("python main.py")

    elif sys.platform.startswith("linux"):
        os.system("python3 -m pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        os.system("python3 main.py")

except Exception as e:
    print(e)
    os.system("pause")
