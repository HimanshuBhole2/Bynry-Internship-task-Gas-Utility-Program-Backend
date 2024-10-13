from django.db import models

# Customer model to store user information
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# ServiceRequest model to store service requests
class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='service_requests')
    request_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} request by {self.customer.name}"
