from pathlib import Path
import glob

class Eliminate_Duplicates:
    def __init__(self, root: Path):
        self.root = root

    def list_by_filename(self) -> dict:

        # Returns [str] of all files in root.
        files_located = glob.glob(f"{self.root}/**", recursive=True)

        print(Path(files_located[1]).stem)

        pass

    def list_by_content(self) -> dict:
        pass

    def list_by_filename_and_size(self) -> dict:
        pass

    def list_by_all(self) -> dict:
        pass

if __name__ == "__main__":
    el = Eliminate_Duplicates(Path("./tests/Test_Source"))
    el.list_by_filename()
