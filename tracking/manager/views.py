from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Employee, Device

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'manager/device_list.html', {'devices': devices})

def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'manager/device_detail.html', {'device': device})

def device_new(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.save()
            return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm()
    return render(request, 'manager/device_edit.html', {'form': form})

def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            device = form.save(commit=False)
            device.save()
            return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'manager/device_edit.html', {'form': form})

def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    return redirect('device_list')