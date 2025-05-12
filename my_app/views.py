from django.shortcuts import render

from django.http import HttpResponse

def first_views(request):
    html = """
    <h1> Assosiy bolim </h1>
    <h2> Men yoqtirgan mashinalar </h2>
    """
    return HttpResponse(html)


def second_views(request):
    html = """
    <h1> Toliq malumotlar </h1>
    <h2> Marka nomlari </h2>
    """
    return HttpResponse(html)


