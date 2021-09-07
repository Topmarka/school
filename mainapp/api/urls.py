from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    AllStudentsViewSet,
    AllTeachersViewSet,
    PersonalProfileView,
    ProfileCreateView,
    AllCoursesViewSet,
    LessonsDetailView,
    TimetableViewSet,
    CertificateViewSet,
    AcademicPerformanceViewSet,
)


router = routers.SimpleRouter()
router.register('students', AllStudentsViewSet, basename='students')
router.register('teachers', AllTeachersViewSet, basename='teachers')
router.register('courses', AllCoursesViewSet, basename='courses')
router.register('timetable', TimetableViewSet, basename='timetable')
router.register('certificates', CertificateViewSet, basename='certificates')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', PersonalProfileView.as_view(), name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='create_profile'),
    path('courses/<int:course_pk>/lessons/<int:pk>', LessonsDetailView.as_view())
]
urlpatterns += router.urls
