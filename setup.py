import os

def create_folders_and_files():
    folders = ["data", "notebooks", "src", "tests", "docs", ".github/workflows"]
    
    files_to_create = [
        "README.md", ".gitignore", "requirements.txt", "setup.py", "Dockerfile", "app.py",
        "src/data_loader.py", "src/sampling.py", "src/visualization.py",
        "tests/test_sampling.py", "tests/test_visualization.py",
        "docs/project_overview.md", ".github/workflows/ci.yml"
    ]
    
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Create files
    for file in files_to_create:
        file_path = file
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                if file == "README.md":
                    f.write("# Confidence Interval Dashboard\n\nAn interactive dashboard to visualize confidence intervals.")
                elif file == "requirements.txt":
                    f.write("dash\npandas\nplotly\nkaggle\nnumpy\nscipy\npytest")
                elif file == ".gitignore":
                    f.write("__pycache__/\n.env\nkaggle.json")
                elif file == "Dockerfile":
                    f.write("FROM python:3.9\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"python\", \"app.py\"]")
                elif file == ".github/workflows/ci.yml":
                    f.write("""
name: CI Pipeline
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest tests/
""")
                else:
                    f.write("")  # Empty files for now
    
    print("Project structure initialized successfully!")

if __name__ == "__main__":
    create_folders_and_files()
