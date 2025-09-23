import base64
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat, Language

# Initialize the client
client = WorkspaceClient()

# Databricks workspace path
notebook_path = "/Shared/my_notebook"

# Read your notebook content
with open("resources/notebooks/etl_notebook.py", "r") as f:
    notebook_content = f.read()

# Encode content in base64
notebook_base64 = base64.b64encode(notebook_content.encode("utf-8")).decode("utf-8")

# Deploy notebook
client.workspace.import_(
    path=notebook_path,
    language=Language.PYTHON,
    content=notebook_base64,
    overwrite=True,
    format=ImportFormat.SOURCE
)

print("Notebook deployed successfully!")
