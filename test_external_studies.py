import shutil
import sys
import tarfile
from fnmatch import fnmatch
from pathlib import Path
from urllib.request import urlopen

# These tests specify dataset definitions in other repositories which we want to ensure
# we don't accidentally break. In order to keep tests hermetic and deterministic, we
# copy the study code into the repo and commit it (taking care to copy just the files we
# need to evalute the dataset definition). This module can also be used as a script
# which ensures our vendored copy of the code is up-to-date. Usage is:
#
#     python -m tests.acceptance.test_external_studies update
#
# Or via just as:
#
#     just update-external-studies
#
# This is run automatically by a scheduled action which will create a PR if there are
# any changes to be made.
EXTERNAL_STUDIES = {
    "test-age-distribution": dict(
        repo="opensafely/test-age-distribution",
        branch="main",
        file_globs=[
            "analysis/dataset_definition.py",
        ],
        dataset_definition="analysis/dataset_definition.py",
    ),
}

STUDY_DIR = Path(__file__).parent / "external_studies"


# SCRIPT TO UPDATE EXTERNAL STUDIES
#


def update_external_studies():  # pragma: no cover
    if STUDY_DIR.exists():
        shutil.rmtree(STUDY_DIR)
    for name, config in EXTERNAL_STUDIES.items():
        target_dir = STUDY_DIR / name
        tarball_url = f"https://github.com/{config['repo']}/tarball/{config['branch']}"
        download_files(target_dir, tarball_url, config["file_globs"])


def download_files(target_dir, tarball_url, file_globs):  # pragma: no cover
    for name, read_bytes in get_files_from_remote_tarball(tarball_url):
        # Strip the arbitrary leading directory from the tar path
        path = name.partition("/")[2]
        if any(fnmatch(path, pattern) for pattern in file_globs):
            out_path = target_dir / path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(read_bytes())


def get_files_from_remote_tarball(url):  # pragma: no cover
    with urlopen(url) as stream:
        with tarfile.open(fileobj=stream, mode="r:gz") as tarobj:
            while tar_info := tarobj.next():
                if tar_info.isfile():
                    yield tar_info.name, lambda: tarobj.extractfile(tar_info).read()


if __name__ == "__main__":
    if sys.argv[1:] != ["update"]:
        sys.exit("Usage: python -m tests.acceptance.test_external_studies update")
    update_external_studies()
