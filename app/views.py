from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html' )
def about(request):
    return render(request, 'about.html' )
def contact(request):
    return render(request, 'contact.html' )
def service(request):
    return render(request, 'service.html' )
def testimonial(request):
    return render(request, 'testimonial.html' )
def team(request):
    return render(request, 'team.html' )
def error404(request):
    return render(request, '404.html' )
def home(request):
    return render(request, 'home.html' )
def careers(request):
    return render(request, 'career.html' )
def insight(request):
    return render(request, 'insight.html' )

# industires links
def industries(request):
    return render(request, 'industries.html' )
def consumer_industrial_market(request):
    return render(request, 'consumer-industrial-markets.html' )
def financial_service_industry(request):
    return render(request, 'finanacial-service-industry.html' )
def energy_natural_resources(request):
    return render(request, 'energy-natural-resources.html' )
def public_social_sector(request):
    return render(request, 'public-social-sector.html' )
def real_estate_construction(request):
    return render(request, 'real-estate-construction.html' )
def technology_media_telecommunication(request):
    return render(request, 'technology-media-telecommunication.html' )
def transport_logistics(request):
    return render(request, 'transport-logistics.html' )

# services link
def services(request):
    return render(request, 'services.html' )
def advisory(request):
    return render(request, 'advisory.html' )
def audit_assurance(request):
    return render(request, 'audit-assurance.html' )
def consulting(request):
    return render(request, 'consulting.html' )
def tax_regulatory_people_services(request):
    return render(request, 'tax-regulatory-people-services.html' )