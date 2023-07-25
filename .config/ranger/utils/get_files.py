def get_files(selected_files):
    for file in selected_files:
        if not file.basename.endswith(('.png', '.jpeg', '.jpg', '.webp')):
            raise Exception(f"File {file.basename} is not a supported image")

    return selected_files[0], selected_files[1]

