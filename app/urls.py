from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('testimonial/', views.testimonial, name='team'),
    path('careers/', views.careers, name='career'),
    path('team/', views.team, name='team'),
    path('error404/', views.error404, name='error404'),
    path('', views.home, name='home'),
    # industries url paths
    path('industries/', views.industries, name='industries'),
    path('industries/consumer_industrial_market/', views.consumer_industrial_market, name='consumer_industrial_market'),
    path('industries/financial_service_industry/', views.financial_service_industry, name='financial_service_industry'),
    path('industries/energy_natural_resources', views.energy_natural_resources, name='energy_natural_resources'),
    path('industries/public_social_sector', views.public_social_sector, name='public_social_sector'),
    path('industries/real_estate_construction', views.real_estate_construction, name='real_estate_construction'),
    path('industries/technology_media_telecommunication', views.technology_media_telecommunication, name='technology_media_telecommunication'),
    path('industries/transport_logistics', views.transport_logistics, name='transport_logistics'),
    # services url paths
    path('services', views.services, name='services'),
    path('services/advisory', views.advisory, name='advisory'),
    path('services/audit_assurance', views.audit_assurance, name='audit_assurance'),
    path('services/consulting', views.consulting, name='consulting'),
    path('services/tax_regulatory_people_services', views.tax_regulatory_people_services, name='tax_regulatory_people_services'),
    

    path('insight', views.postslist.as_view(), name="posts"),
    path('<slug:slug>/', views.postdetail.as_view(), name="post_detail"),

]
 