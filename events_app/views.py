from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventForm
from .models import Category, Event


def event_list(request):
    events = Event.objects.filter(is_approved=True).select_related("category")
    return render(request, "events_app/event_list.html", {"events": events})


def event_detail(request, event_id):
    event = get_object_or_404(
        Event.objects.select_related("category"),
        pk=event_id,
        is_approved=True
    )
    return render(request, "events_app/event_detail.html", {"event": event})


def category_list(request):
    categories = Category.objects.all()
    return render(request, "events_app/category_list.html", {"categories": categories})


def category_events(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    events = category.events.filter(is_approved=True)
    return render(
        request,
        "events_app/category_events.html",
        {"category": category, "events": events}
    )


def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your event has been submitted successfully and is now pending admin approval."
            )
            return redirect("event_create")
    else:
        form = EventForm()

    return render(request, "events_app/event_create.html", {"form": form})


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)