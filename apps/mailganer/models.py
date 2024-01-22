from django.db import models

from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


# Create your models here.
class EmailTemplate(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    template = models.TextField(_("Template"))

    class Meta:
        verbose_name = _("Email Template")
        verbose_name_plural = _("Email Templates")

    def __str__(self):
        return self.name


class EmailDistribution(BaseModel):
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    user = models.ManyToManyField(
        User, verbose_name=_("Users"), related_name="email_distribution", blank=True, null=True
    )
    send_to_all = models.BooleanField(_("Send to all"), default=False)

    class Meta:
        verbose_name = _("Email distribution")
        verbose_name_plural = _("Email distributions")

    def __str__(self):
        return f"{self.id}"


class UserEmailDistribution(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_email_distribution')
    email_distribution = models.ForeignKey(
        EmailDistribution,
        on_delete=models.CASCADE,
        related_name=_("user_email_distribution"),
        verbose_name=_("Email distribution"))

    is_read = models.BooleanField(_("Is read"), default=False)
    tracking_pixel_url = models.URLField(_("Tracking pixel URL"), blank=True, null=True)

    class Meta:
        verbose_name = _("User email distribution")
        verbose_name_plural = _("User email distributions")

    def __str__(self):
        return f"{self.user}"
