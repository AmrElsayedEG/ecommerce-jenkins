from utils import APITestCase, reverse, mixer, status
from datetime import datetime, timedelta

class CreateOrderTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('orders:create-order')
        self.address = mixer.blend('users.Address', location={})
        self.customer = mixer.blend('users.User', address=self.address)

    def test_unauthorized(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'detail': 'Authentication credentials were not provided.'})

    def test_method_not_allowed(self):
        self.client.force_authenticate(self.customer)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_no_data(self):
        self.client.force_authenticate(self.customer)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), ["This field is required."])

    def test_no_shipping_fees(self):
        data = {
                "order" : {
                    "address" : self.address.id,
                    "phone" : "011211",
                    "notes" : "No",
                },
                "items" : [
                ]
            }
        self.client.force_authenticate(self.customer)
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"shipping_fees":["This field is required."]})

    def test_no_items(self):
        data = {
                "order" : {
                    "address" : self.address.id,
                    "phone" : "011211",
                    "shipping_fees" : None,
                    "notes" : "No",
                },
                "items" : [
                ]
            }
        self.client.force_authenticate(self.customer)
        response = self.client.post(self.url, data=data, format='json')
        error = {
            'error' : ['There is no items in your order'],
            'error_ar' : ['لا توجد منتجات فى الطلب']
        }
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), error)

    def test_insufficient_quantity(self):
        product = mixer.blend('products.Product', quantity=10)
        data = {
                "order" : {
                    "address" : self.address.id,
                    "phone" : "011211",
                    "shipping_fees" : None,
                    "notes" : "No",
                },
                "items" : [
                    {
                        "product" : product.id,
                        "quantity" : 11
                    }
                ]
            }
        self.client.force_authenticate(self.customer)
        response = self.client.post(self.url, data=data, format='json')
        error = {'error': [f"These items above the in stock number, ['{product.title}']"], 
                'error_ar': [f"['{product.title}'] ,الكمية المطلوبة من هذه المنتجات أكبر من الكمية المتاحة"]}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), error)

    def test_expired_coupon_code(self):
        product = mixer.blend('products.Product', quantity=10)
        coupon = mixer.blend('main.Coupon', end_date=datetime.now() - timedelta(days=1))
        data = {
                "order" : {
                    "address" : self.address.id,
                    "phone" : "011211",
                    "shipping_fees" : None,
                    "notes" : "No",
                    "coupon" : coupon.id
                },
                "items" : [
                    {
                        "product" : product.id,
                        "quantity" : 1
                    }
                ]
            }
        self.client.force_authenticate(self.customer)
        response = self.client.post(self.url, data=data, format='json')
        error = {
            'error' : ['A coupon you are using is invalid or expired'],
            'error_ar' : ['الكوبون المستخدم ربما منتهي الصلاحية أو لم تستوفي الشروط']
        }
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), error)

    def test_coupon_used_before(self):
        product = mixer.blend('products.Product', quantity=10)
        coupon = mixer.blend('main.Coupon', end_date=datetime.now() + timedelta(days=1))
        order = mixer.blend('orders.Order', customer=self.customer, coupon=coupon)
        data = {
                "order" : {
                    "address" : self.address.id,
                    "phone" : "011211",
                    "shipping_fees" : None,
                    "notes" : "No",
                    "coupon" : coupon.id
                },
                "items" : [
                    {
                        "product" : product.id,
                        "quantity" : 1
                    }
                ]
            }
        self.client.force_authenticate(self.customer)
        response = self.client.post(self.url, data=data, format='json')
        error = {
            'error' : ['A coupon you are using is invalid or expired'],
            'error_ar' : ['الكوبون المستخدم ربما منتهي الصلاحية أو لم تستوفي الشروط']
        }
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), error)