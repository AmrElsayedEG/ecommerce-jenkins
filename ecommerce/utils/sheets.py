from django.http import HttpResponse
import csv

class ProductsExcel:
    @classmethod
    def export_as_csv(self, queryset):
        field_names = ['title', 'big_unit', 'big_unit_price', 'big_unit_price_discount', 'big_unit_discount_max_quantity', 'small_unit', 'small_unit_price', 'small_unit_price_discount', 'live', 'in_big_items', 'in_stock_items', 'ordered_times']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format("products-report")
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

class OrdersExcel:
    @classmethod
    def export_as_csv(self, queryset):
        field_names = ['order_no', 'customer', 'payment_option', 'created', 'status']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format("all-orders")
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) if not field == 'status' else obj.get_status_display() for field in field_names])

        return response

class CustomersExcel:
    @classmethod
    def export_as_csv(self, queryset):
        field_names = ['first_name', 'last_name', 'email', 'phone', 'last_order', 'registered']

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format("all-customers")
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response