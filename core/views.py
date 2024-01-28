from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext


@login_required
def index(request):
    return render(request, 'index.html')


def mock_charts(request):
    return render(request, 'charts/chartjs.html')


def mock_forms(request):
    return render(request, 'forms/basic_elements.html')


def mock_icons(request):
    return render(request, 'icons/mdi.html')


def mock_tables(request):
    return render(request, 'tables/basic_table.html')


def mock_feature_button(request):
    return render(request, 'ui-features/buttons.html')


def mock_feature_dropdown(request):
    return render(request, 'ui-features/dropdowns.html')


def mock_feature_typography(request):
    return render(request, 'ui-features/typography.html')


def bad_req(request, exception):
    response = render(request, 'exceptions/400.html', {})
    response.status_code = 400

    return response


def permission_denied(request, exception):
    response = render(request, 'exceptions/403.html', {})
    response.status_code = 403

    return response


def page_not_found(request, exception):
    response = render(request, 'exceptions/404.html', {})
    response.status_code = 404

    return response


def server_err(request):
    response = render(request, 'exceptions/500.html', {})
    response.status_code = 500

    return response
