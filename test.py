import kagglehub

# Download latest version
path = kagglehub.dataset_download("sakshisatre/titanic-dataset")

print("Path to dataset files:", path)