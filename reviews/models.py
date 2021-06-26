from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)  # 유저를 삭제하면 리뷰도 삭제
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE
    )  # ROOM를 삭제하면 리뷰도 삭제

    def __str__(self):
        return f"{self.review} - {self.room}"
