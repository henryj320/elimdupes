from pathlib import Path
import glob
from treelib import Node, Tree, exceptions
from alive_progress import alive_bar
from time import sleep


class Eliminate_Duplicates:
    def __init__(self, root: Path):
        self.root: Path = root
        self.duplicates: list = []
        self.files = self.get_files()
    
    def get_files(self):
        """Returns a list of all files in the directory"""
        print(f"\rFinding files and directories...", end='', flush=True)
        return glob.glob(f"{self.root}/**", recursive=True)

    def list_by_filename(self) -> list:
        """Finds all duplicate files by name alone.

        Returns:
            list: A list of lists containing all duplicates.
        """
        # Returns [str] of all files in root.
        # print("Finding files and directories...")
        # files_located = glob.glob(f"{self.root}/**", recursive=True)
        print("\r                                                               ", end='')
        print(f"\rRemoving directories...", end='', flush=True)

        # Removes all directories.
        for f in self.files:
            if Path(f).is_dir():
                self.files.remove(f)
                # print(f)

        # print("Finding duplicates...")
        print("\r", end='')
        print(f"\rFinding duplicates...", flush=True)
        with alive_bar(len(self.files), bar="filling") as progress_bar:
            
            filenames = []
            duplicates = []
            for f in self.files:
                filename =  str(Path(f).name)

                # If the file is a duplicate.
                if filename in filenames:
                    # Add both the file and its original to duplicates[].

                    # Adds the duplicate to the appropriate duplicates[] list.
                    added_to_dupes = False
                    for group_of_dupes in duplicates:

                        # Already added, so exit.
                        if f in group_of_dupes:
                            break

                        # Adds the duplicate to its relevant duplicates[] list.
                        name = Path(group_of_dupes[0]).name
                        if name == filename:
                            group_of_dupes.append(f)
                            added_to_dupes = True
                            break
                    
                    # Makes a new group in duplicates[] if it does not exist.
                    if not added_to_dupes:
                        location = [i for i, x in enumerate(filenames) if x == filename][0]
                        duplicates.append([f, self.files[location]])

                else:
                    filenames.append(filename)

                progress_bar() # pylint: disable=not-callable

        self.duplicates = duplicates
        return duplicates

    def list_by_content(self) -> dict:
        pass

    def list_by_filename_and_size(self) -> dict:
        pass

    def list_by_all(self) -> dict:
        pass

    def convert_to_tree(self) -> None:
        """Converts self.duplicates into a tree and prints it."""
        tree = Tree()
        tree.create_node("Duplicates", "root")  # Root node.

        # Adds a node to the tree for each duplicate.
        for group_of_dupes in self.duplicates:

            for index, dupes in enumerate(group_of_dupes):

                if index == 0:

                    tree.create_node(dupes, dupes, "root")
                    continue

                try:
                    tree.create_node(dupes, dupes, group_of_dupes[0])
                except exceptions.DuplicatedNodeIdError:
                    continue


        print("\nTree:")
        print(tree.show())

if __name__ == "__main__":
    el = Eliminate_Duplicates(Path("./tests/Test_Source"))
    # el = Eliminate_Duplicates(Path("/mnt/SharedFolder/Henry/Backups/Media/Artwork (2023-11-11)/"))
    el.list_by_filename()
    el.convert_to_tree()

    print(f"Duplicates found: {len(el.duplicates)}")
