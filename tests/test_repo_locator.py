import pytest
from pathlib import Path, WindowsPath
from dp_path_util.repo_locator import CouldNotLocateRepositoryDirException
from dp_path_util.repo_locator import RepositoryDirLocator


@pytest.fixture(scope="module")
def repo_dir_locator()-> RepositoryDirLocator:
    return RepositoryDirLocator()

def test_repository_locator_finds_correct_repository_directory(repo_dir_locator):
    assert repo_dir_locator.repo_dir.resolve() == Path(__file__).parent.parent.resolve()

def test_repository_locator_raises_exception_if_repository_cannot_be_found():
    with pytest.raises(CouldNotLocateRepositoryDirException):
        RepositoryDirLocator(start_dir=Path('/'))
