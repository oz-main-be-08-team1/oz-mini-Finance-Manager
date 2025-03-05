from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "nickname", "phone_number", "is_active", "is_staff")
    list_filter = (
        "is_active",
        "is_staff",
    )  # 'is_staff'를 제거하고, 필터링할 수 있는 필드만 설정
    search_fields = ("email", "nickname", "phone_number")
    ordering = ("email", "nickname")

    def get_fieldsets(self, request, obj=None):
        # 슈퍼유저만 is_admin 보이게 설정
        if request.user.is_superuser:
            return (
                (None, {"fields": ("email", "password")}),
                ("개인 정보", {"fields": ("nickname", "name", "phone_number")}),
                ("권한 설정", {"fields": ("is_active", "is_staff", "is_admin")}),
                ("최근 로그인", {"fields": ("last_login",)}),
            )
        elif request.user.is_staff:  # 스태프일 경우
            return (
                (None, {"fields": ("email", "password")}),
                ("개인 정보", {"fields": ("nickname", "name", "phone_number")}),
                ("권한 설정", {"fields": ("is_active", "is_staff")}),
                ("최근 로그인", {"fields": ("last_login",)}),
            )
        else:  # 일반 사용자일 경우
            return (
                (None, {"fields": ("email", "password")}),
                ("개인 정보", {"fields": ("nickname", "name", "phone_number")}),
                ("권한 설정", {"fields": ("is_active",)}),
                ("최근 로그인", {"fields": ("last_login",)}),
            )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    filter_horizontal = ()
