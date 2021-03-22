import cloudstorage
from google.appengine.api import app_identity
import os

# [END imports]

# [START retries]
cloudstorage.set_default_retry_params(
    cloudstorage.RetryParams(
        initial_delay=0.2, max_delay=5.0, backoff_factor=2, max_retry_period=15
        ))
# [END retries]


# [END write]

# [START read]
def read_file(filename):
    with cloudstorage.open(filename) as cloudstorage_file:
        cloudstorage_file.seek(-1024, os.SEEK_END)
        return (cloudstorage_file.read())

# [END read]


# [START delete_files]
def delete_files(filename):
    try:
        cloudstorage.delete(filename)
    except cloudstorage.NotFoundError:
        pass


# [END delete_files]




