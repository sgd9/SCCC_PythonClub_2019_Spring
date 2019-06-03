from django.test import TestCase
from django.urls import reverse
import datetime 
from .forms import ProductForm
from .models import ProductType, Product, Review
from django.contrib.auth.models import User 


#test for models

class ProductTypeTest(TestCase):
    def test_string(self):
        type=ProductType(productname='Dell latitude 7490')
        self.assertEqual(str(type),type.productname)
    
    def test_table(self):
        self.assertEqual(str(ProductType._meta.db_table),'producttype')

class ProductTypeTest(TestCase):
    def setUp(self):
        self.type=ProductType(typename='Tablet')
        self.prod=Product(productname='Ipad',producttype=self.type, productprice=800.00)
    
    def test_string(self):
        self.assertEqual(str(self.prod),self.prod.productname)
    
    def test_type(self):
        self.assertEqual(str(self.prod.producttype),'Tablet')

    def test_discount(self):
        self.assertEqual(self.prod.memberDiscount(),40.00)
        
#tests for views

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=ProductType.objects.create(typename='Laptop')
        self.prod=Product.objects.create(productname='product1', producttype=self.type, user=self.u, 
        productprice=500.00,productentrydate='2019-04-02', productdescription="some kind of laptop")
    
    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetails', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/products.html')

class New_Product_Form_Test(TestCase):

    # Valid Form Data
    def test_product_is_valid(self):
        form=ProductForm(data={'productname' : "Surface", 'producttype' : "Laptop",
        'user' : "SamuelD", 'productentrydate' : "2019-05-28", 'productURL' :"http://www.microsoft.com",
        'productdescription':"lightweight laptop"})
        self.assertTrue(form.is_valid())

# valid Form Data
def test_UserForm_invalid(self):
    form = ProductForm(data={'productname' : "Surface", 'producttype' : "Laptop",
    'user': "SamuelD",'productentrydate' : "2019-05-28", 'productURL' : "http://www.microsoft.com",
    'productdescription' : "lightweight laptop"})
    self.assertTrue(form_is_valid())

class ProductFormTest(TestCase):
    def setUp(self):
        self.user2=User.objects.create(username='user1', password='P@ssw0rd1')
        self.type2=ProductType.objects.create(typename='type1')

    def test_productForm(self):
        data={
            'productname' : 'product1',
            'producttype' : self.type2,
            'user' : self.user2,
            'productprice' : 200.00,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid)

    def test_productFormInvalid(self):
        data={
            'productname' : 'product1',
            'producttype' : self.type2,
            'user' : self.user2,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid)

class New_Product_Form_Test(TestCase):

    # Valid Form Data Test

    def test_productForm_is_valid(self):
        form = ProductForm(data={'productname' : "Surface", 'producttype' : "Laptop",
        'user' : "u_andersen", 'productentrydate' : "2019-05-28",
        'productURL' : "http:microsoft.com", 'productdescription' : "lightweight laptop"})
        self.assertTrue(form.is_valid)

    # Invalid Fform Data Test

    def test_UserForm_invalid(self):
        form = ProductForm(data={'productname' : "Surface", 'producttype' : "Laptop",
        'user' : "u_andersen", 'productentrydate' : "2019-05-28",
        'productURL' : "http:microsoft.com", 'productdescription' : "lightweight laptop"})
        self.assertFalse(form.is_valid())

    
