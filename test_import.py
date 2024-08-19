import sys
print("Python executable:", sys.executable)
print("Python path:", sys.path)

try:
    from langchain.vectorstores import Chroma
    print("Chroma imported successfully")
except ModuleNotFoundError as e:
    print(f"Import failed: {e}")

