import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

def main():
    from server import run_server
    run_server()

if __name__ == "__main__":
    main()
