"""
Regression tests for initial SQL insertion.
"""

from django.db import models

class Simple(models.Model):
    name = models.CharField(max_length = 50)

# NOTE: The format of the included SQL file for this test suite is important.
# It must end with a trailing newline in order to test the fix for #2161.
