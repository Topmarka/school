from django.contrib.auth import views
from django.urls import path

from management import views as management


urlpatterns = [
    path('', management.MainView.as_view(), name='home'),
    path('auth/', management.ProfileLoginView.as_view(), name='auth'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('clients/', management.ClientsListView.as_view(), name='clients'),
    path('clients/<int:pk>/', management.ClientDetailView.as_view(), name='client_detail'),
    path('clients/create', management.CreateClientView.as_view(), name='create_client'),
    path('online-requests/', management.RequestListView.as_view(), name='requests'),
    path('out-calls/', management.OutCallListView.as_view(), name='out_calls'),
    path('in-calls/', management.InCallListView.as_view(), name='in_calls'),
    path('visits/', management.VisitListView.as_view(), name='visits'),
    path('requests/<int:pk>/', management.RequestDetailView.as_view(), name='requests_detail'),
    path('requests/create/', management.CreateRequestView.as_view(), name='create_request'),
    path('contracts/', management.ContractListView.as_view(), name='contracts'),
    path('contracts/<int:pk>/', management.ContractDetailView.as_view(), name='contracts_detail'),
    path('contracts/create/', management.CreateContractView.as_view(), name='create_contract'),
    path('orders/', management.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', management.OrderDetailView.as_view(), name='orders_detail'),
    path('orders/create/', management.CreateOrderView.as_view(), name='create_order'),
    path('vacancy/', management.VacancyListView.as_view(), name='vacancy'),
    path('vacancy/<int:pk>/', management.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/create/', management.CreateVacancyView.as_view(), name='create_vacancy'),
    path('interview/', management.InterviewListView.as_view(), name='interview'),
    path('interview/<int:pk>/', management.InterviewDetailView.as_view(), name='interview_detail'),
    path('interview/create/', management.CreateInterviewView.as_view(), name='create_interview'),
    path('courses/', management.CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>/', management.CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', management.CreateCourseView.as_view(), name='create_course'),
    path('courses/lessons/create/', management.CreateLessonView.as_view(), name='create_lesson'),
    path('academic-performance/', management.AcademicPerformanceListView.as_view(), name='academic_performance'),
    path(
        'academic-performance/create/',
        management.CreateAcademicPerformanceView.as_view(),
        name='create_academic_performance'
    ),
    path('timetable/', management.TimeTableListView.as_view(), name='timetable'),
    path('timetable/create/', management.CreateTimeTableView.as_view(), name='create_timetable'),
    path('teachers/', management.TeacherListView.as_view(), name='teachers'),
    path('teachers/<int:pk>/', management.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/create/', management.CreateTeacherView.as_view(), name='create_teacher'),
    path('staffs/', management.StaffListView.as_view(), name='staffs'),
    path('staffs/<int:pk>/', management.StaffDetailView.as_view(), name='staff_detail'),
    path('staffs/create/', management.CreateStaffView.as_view(), name='create_staff'),
    path('groups/', management.GroupListView.as_view(), name='groups'),
    path('groups/<int:pk>/', management.GroupDetailView.as_view(), name='group_detail'),
    path('groups/create/', management.CreateGroupView.as_view(), name='create_group'),
]
