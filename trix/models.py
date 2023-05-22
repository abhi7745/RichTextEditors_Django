from django.db import models

# Create your models here.


class trix_data(models.Model):
    # description = models.TextField(db_collation="utf8mb4_general_ci") # In mysql - The error of [Incorrect string value: '\xE2\x82\xB960' is in some copy-pasted content from ckeditor]  - The solution is to add the db_collation argument "utf8mb4_General_ci" to the model field."
    description = models.TextField()