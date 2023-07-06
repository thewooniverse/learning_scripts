You can copy an existing file in Python using the `shutil` module. Here's a simple example:

```python
import shutil

# specify the original file and destination file path
original = r'original_path/original_file.txt'
target = r'target_path/target_file.txt'

# copy the file
shutil.copyfile(original, target)
```

In this example, replace `original_path/original_file.txt` with the path to the file you want to copy, and replace `target_path/target_file.txt` with the path and name you want for the copied file. The `r` before the file path is to ensure any escape sequences in the file path are treated as raw strings.

The `shutil.copyfile()` function will copy the contents of the original file into the target file. If the target file already exists, it will be overwritten. If it doesn't exist, it will be created.

This will only copy the file contents, not metadata like file permissions. If you also want to copy file metadata, you can use `shutil.copy2()` instead.