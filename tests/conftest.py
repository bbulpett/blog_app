import os
import tempfile

import pytest

from blog.models import Article


@pytest.fixture(autouse=True)  # Automatically use for each test by default
def database():
    # These lines run before the test
    _, file_name = tempfile.mkstemp()  # Create and call unique temp file
    os.environ['DATABASE_NAME'] = file_name
    Article.create_table(database_name=file_name)
    
    yield  # Test runs here

    # These lines run after the test
    os.unlink(file_name)
