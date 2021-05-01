from django.shortcuts import render



def report_ecommerce(request):
    return render(request, 'retail_report.html', {})

def report_marketing(request):
    return render(request, 'marketing_report.html', {})

