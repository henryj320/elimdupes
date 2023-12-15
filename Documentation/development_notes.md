# elimdupes

Last update: 2023-12-14 14:28
<br><br>

## Development Notes for elimdupes

1. Set up the repository.
2. To do:
    - Backend
        - Write a method to list all duplicates **by filename**.
        - Write a method to list all duplicates **by content**.
        - Write a method to list all duplicates **by filename and size**.
        - Write a method to list all duplicates **by filename, content and size**.
        - Compare the efficiencies of each.
        - Set up testing for each method.
        - Set up endpoints for each option.
    - Set up the Git runners
    - Frontend
        - Create a React frontend which calls each method
        - Add toggle switches for "Delete?", "List?" (disabled), "Verbose output"
        - Output a log of the number of duplicates in the frontend.
3. Created the initial files and folders.
4. Wrote ` list_by_filename() `
5. Wrote ` convert_to_tree() `
    - Had to adapt ` print(self._reader.encode("utf-8")) ` to ` print(self._reader) ` in *tree.py* of treelib.
    - So that it outputs the tree correctly.
