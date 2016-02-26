from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account import models as amod
from catalog import models as cmod
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group


@permission_required('catalog.add_product', login_url='/homepage/index/')
@view_function
def process_request(request):
    '''Lists the Products in a table on the screen'''
    products = cmod.Product.objects.all().order_by('name')
    template_vars = {
    'products': products
    }
    return dmp_render_to_response(request, 'products.html', template_vars)


# Create a product
@permission_required('catalog.add_product', login_url='/homepage/index/')
@view_function
def create(request):
    '''Create a Product'''
    # process the form
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('ptype') == 'RentalProduct':
                product = cmod.RentalProduct()
                product.status = form.cleaned_data.get('status')
            elif form.cleaned_data.get('ptype') == 'IndividualProduct':
                product = cmod.IndividualProduct()
                product.creator = form.cleaned_data.get('creator')
            else:
                product = cmod.BulkProduct()
                product.quantity = form.cleaned_data.get('quantity')
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.image = form.cleaned_data.get('image')
            product.save()
            return HttpResponseRedirect('/catalog/products')
        print(form.errors)
    template_vars = {
    'form': form,
    }
    return dmp_render_to_response(request, 'products.create.html', template_vars)


PRODUCT_TYPE_CHOICES = (
    ('', 'Please select a product type.'),
    ('RentalProduct', 'Rental Product'),
    ('IndividualProduct', 'Individual Product'),
    ('BulkProduct', 'Bulk Product'),
)

class CreateForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ptype = forms.ChoiceField(label='Product Type', required=False, choices=PRODUCT_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='Status', required=False, choices=cmod.RENTAL_STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control RentalProductField'}))
    creator = forms.ModelChoiceField(label='Creator', required=False, queryset=amod.User.objects.order_by('first_name', 'last_name'), widget=forms.Select(attrs={'class': 'form-control IndividualProductField'}))
    quantity = forms.IntegerField(label='Quantity', required=False, widget=forms.NumberInput(attrs={'class': 'form-control BulkProductField' }))


@permission_required('catalog.change_product', login_url='/homepage/index/')
@view_function
def edit(request):
    '''Edits a product'''
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/products/')
    if isinstance(product, cmod.IndividualProduct):
        form = IndividualEditForm(initial=model_to_dict(product))
    elif isinstance(product, cmod.BulkProduct):
        form = BulkEditForm(initial=model_to_dict(product))
    else:
        form = RentalEditForm(initial=model_to_dict(product))
    if request.method == 'POST':
        if isinstance(product, cmod.IndividualProduct):
            form = IndividualEditForm(request.POST)
        elif isinstance(product, cmod.BulkProduct):
            form = BulkEditForm(request.POST)
        else:
            form = RentalEditForm(request.POST)
        if form.is_valid():
            if isinstance(product, cmod.IndividualProduct):
                product = cmod.IndividualProduct(id=request.urlparams[0])
                product.creator = form.cleaned_data.get('creator')
            elif isinstance(product, cmod.BulkProduct):
                product = cmod.BulkProduct(id=request.urlparams[0])
                product.quantity = form.cleaned_data.get('quantity')
            else:
                product = cmod.RentalProduct(id=request.urlparams[0])
                product.status = form.cleaned_data.get('status')
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.image = form.cleaned_data.get('image')
            product.save()
            return HttpResponseRedirect('/catalog/products')
    # show the edit form html
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'products.edit.html', template_vars)


class IndividualEditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    creator = forms.ModelChoiceField(label='Creator', required=False, queryset=amod.User.objects.order_by('first_name', 'last_name'), widget=forms.Select(attrs={'class': 'form-control IndividualProductField'}))


class BulkEditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='Quantity', required=False, widget=forms.NumberInput(attrs={'class': 'form-control BulkProductField' }))


class RentalEditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='Status', required=False, choices=cmod.RENTAL_STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control RentalProductField'}))


@permission_required('catalog.delete_product', login_url='/homepage/index/')
@view_function
def delete(request):
    '''Deletes a product'''
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/products/')
    # delete the product
    product.delete()
    return HttpResponseRedirect('/catalog/products/')


@permission_required('catalog.change_product', login_url='/homepage/index/')
@view_function
def get_quantity(request):
    try:
        products = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        pass
    return HttpResponse(products.quantity)
