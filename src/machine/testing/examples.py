from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


@dataclass
class ExampleStore:
    path: Path

    def iter_valid_syntax(self) -> Iterator[tuple[Path, str]]:
        """
        Iterate over all pairs of (path, str) for file sources with no syntax errors in the 
        examples.
        """
        raise NotImplementedError

    def iter_paths(self) -> Iterator[Path]:
        """
        Iterate over all file paths with .lm or .ꟛ files.
        """
        for root, dirs, files in self.path.walk(on_error=self._on_walk_path_error):
            for filename in files:
                if filename.endswith(".lm") or filename.endswith(".ꟛ"):
                    yield root / filename
                
    def _on_walk_path_error(self, err):
        print(err)

    