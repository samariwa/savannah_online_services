from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField,\
     SelectField, IntegerField, DateField, DecimalField, FileField,\
     TextAreaField, HiddenField, RadioField, DateTimeField, TimeField
from wtforms.validators import Length, EqualTo, Email, DataRequired,\
     ValidationError, Regexp
from flask_wtf.file import FileRequired
from app.models import User
from app.general_functions import datetime
from app.response import respond


class RegisterForm(FlaskForm):
    # each function name below matters
    # function name is used for automatic validation
    csrf_token = HiddenField()
    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(
            email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError(
                "Email Address already exists. Login or Recover Password")

    def validate_phone_number(self, phone_no_to_check):
        phone_no = User.query.filter_by(
            phone_no=phone_no_to_check.data).first()
        if phone_no:
            raise ValidationError(
                "Phone number exists, Login or Recover Account")

    first_name = StringField(
        label="First Name",
        render_kw={
            "placeholder": "e.g Christine",
            "class": "input100"
        },
        validators=[
            Length(min=2, max=30, message=respond('SK014')),
            DataRequired(message=respond('SF016'))
        ]
    )

    last_name = StringField(
        label="Last Name",
        render_kw={
            "placeholder": "e.g Washiali",
            "class": "input100"
        },
        validators=[
            Length(min=2, max=30, message=respond('SK015')),
            DataRequired(message=respond('SJ009'))
        ]
    )

    address = StringField(
        label="Physical Address",
        render_kw={
            "placeholder": "&#xf041; Lang'ata, Nairobi, Kenya",
            "class": "input100"
        },
        validators=[
            Length(min=2, max=80, message=respond('SK013')),
            DataRequired(message=respond('SJ010'))
        ]
    )

    email_address = StringField(
        label="Email Address",
        render_kw={
            "placeholder": "&#xf0e0; you@example.com",
            "class": "input100",
            "style": "font-family:Arial,FontAwesome"
        },
        validators=[
            Email(check_deliverability=True, message=respond('SK010')),
            DataRequired(message=respond('SJ011'))
        ]
    )

    phone_no = StringField(
        label="Mobile Number",
        render_kw={
            "placeholder": "&#xf095; format:0700123123",
            "class": "input100",
            "style": "font-family:Arial,FontAwesome"
        },
        validators=[
            Length(min=10, max=16, message=respond('SK011')),
            Regexp('^(0|\+)?\d{3}(-|\s)?\d{3}(-|\s)?\d{3}(-|\s)?\d{0,3}$',
                   message=respond('SK011')),
            DataRequired(message=respond('SJ012'))
        ]
    )

    password1 = PasswordField(
        label='Password',
        render_kw={
            "placeholder": "********",
            "class": "input100",
            "type": "password"
        },
        validators=[
            Length(min=8, message=respond('SJ015')),
            DataRequired(message=respond('SJ013'))]
    )

    password2 = PasswordField(
        label='Confirm password',
        render_kw={
            "placeholder": "********",
            "class": "input100",
            "type": "password"
        },
        validators=[
            EqualTo('password1', message=respond('SK009')),
            DataRequired(message=respond('SJ014'))]
    )

    terms_and_conditions = BooleanField(
        label=Markup(
            "I agree to the <a href='#' style='color: inherit;text-decoration: underline;'>Terms and Conditions</a>"),
        render_kw={
            "class": "input-checkbox100",
            "type": "checkbox",
            "id": "ckb1"
        },
        validators=[DataRequired(message=respond('SK012'))]
    )

    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):
    csrf_token = HiddenField()
    email_address = StringField(
        label='Email Address',
        validators=[DataRequired(message=respond('SJ011'))]
    )

    password = PasswordField(
        label='Password',
        validators=[DataRequired(message=respond('SJ013'))]
    )

    """ remember_me = BooleanField(
       'Remember Me'
    )"""

    remember_me = BooleanField(
        label='Remember Me',
        false_values=(False, 'false', 0, '0', '',),
        default=False,
        render_kw={
            "class": "input-checkbox100",
            "id": "ckb1",
        }
    )

    submit = SubmitField(
        label='Sign In'
    )

class AddCustomerForm(FlaskForm):
    firstname = StringField(
        render_kw={
            "placeholder": "First Name...",
            "class": "form-control col-md-10 ml-3",
            "id": "firstname",
            "style": "padding:15px"
        },
        validators=[DataRequired()]
    )

    lastname = StringField(
        render_kw={
            "placeholder": "Last Name...",
            "class": "form-control col-md-10 ml-3",
            "id": "lastname",
            "style": "padding:15px"
        },
        validators=[DataRequired()]
    )

    phonenumber = StringField(
        label="Phone Number",
        render_kw={
            "placeholder": "Phone Number...",
            "class": "form-control col-md-10 ml-3",
            "id": "phonenumber",
            "style": "padding:15px"
        },
        validators=[DataRequired()]
    )

    close = SubmitField(
        label='Close',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-link btn-simple",
            "data-dismiss": "modal"
        }
    )

    submit = SubmitField(
        label='Add Customer',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-link btn-simple",
            "id": "addCustomer"
        }
    )

class AdminActionForm(FlaskForm):
    actions = RadioField('admin_action', 
               choices=[('active','Activate Account'),
                        ('suspended','Suspend Account'),
                        ('revoked','Revoke Admin Rights')],
                render_kw={
            'default': 'active',
        }       
                        )
    close = SubmitField(
        label='Close',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-link btn-simple",
            "data-dismiss": "modal"
        }
    )

    submit = SubmitField(
        label='Apply',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-link btn-simple apply_admin_action"
        }
    )

class ForgotPasswordForm(FlaskForm):
    csrf_token = HiddenField()
    email_address = StringField(
        label='Email Address',
        validators=[DataRequired(message=respond('SJ011'))]
    )

    submit = SubmitField(
        label='Send Request'
    )


class ResetPasswordForm(FlaskForm):
    csrf_token = HiddenField()
    password1 = PasswordField(
        label='Password',
        validators=[
            Length(min=8, message=respond('SJ015')),
            DataRequired(message=respond('SJ016'))])

    password2 = PasswordField(
        label='Confirm password',
        validators=[
            EqualTo('password1', message=respond('SK009')),
            DataRequired(message=respond('SJ014'))])

    submit = SubmitField(
        label='Reset'
    )


class AddOrderForm(FlaskForm):
    customer = SelectField(
        choices=[("", "Customer...")],
        render_kw={
            "class": "form-control col-md-10 ml-3",
            "id": "customer",
            "onfocus": "this.size=5;",
            "onblur": "this.size=1;",
            "onchange": "this.size=1; this.blur();",
            "style": "padding-left:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    order_cost = DecimalField(
        render_kw={
            "placeholder": "Order Cost...",
            "class": "form-control col-md-10 ml-3",
            "id": "amount",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    delivery_time = TimeField(
        label="Delivery Time...",
        format='%Y-%m-%d %H:%M:%S',
        default=datetime.today(),
        render_kw={
            "class": "form-control col-md-10 ml-3",
            "id": "session_date",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    close = SubmitField(
        label='Close',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-link btn-simple",
            "data-dismiss": "modal"
        }
    )

    submit = SubmitField(
        label='Add Order',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-link btn-simple",
            "id": "addOrder"
        }
    )

class AddProductForm(FlaskForm):
    category = SelectField(
        choices=[("", "Category...")],
        render_kw={
            "class": "form-control col-md-9",
            "id": "category",
            "onfocus": "this.size=3;",
            "onblur": "this.size=1;",
            "onchange": "this.size=1; this.blur();",
            "style": "padding-right:15px;padding-left:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    name = StringField(
        render_kw={
            "placeholder": "Product Name...",
            "class": "form-control col-md-9",
            "id": "name",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    description = TextAreaField(
        render_kw={
            "placeholder": "Product Description...",
            "class": "form-control col-md-9",
            "id": "description",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired(),
                    Length(max=512)]
    )

    unit = SelectField(
        choices=[("", "Unit...")],
        render_kw={
            "class": "form-control col-md-9",
            "id": "unit",
            "onfocus": "this.size=3;",
            "onblur": "this.size=1;",
            "onchange": "this.size=1; this.blur();",
            "style": "padding-right:15px;padding-left:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    contains = IntegerField(
        render_kw={
            "placeholder": "Contains...",
            "class": "form-control col-md-4",
            "id": "contains",
            "style": "padding:15px;margin-left: 60px",
            "oninput": "replenishDisable()"
            },
        validators=[DataRequired()]
    )

    subunit = SelectField(
        choices=[("", "Sub-Units...")],
        render_kw={
            "class": "form-control col-md-4",
            "id": "subunit",
            "onfocus": "this.size=3;",
            "onblur": "this.size=1;",
            "onchange": "this.size=1; this.blur();",
            "style": "padding-right:15px;padding-left:15px;margin-left: 40px"
            },
        validators=[DataRequired()]
    )

    replenish = IntegerField(
        render_kw={
            "placeholder": "Sub-Unit Replenish Quantity...",
            "class": "form-control col-md-9",
            "id": "replenish",
            "style": "padding:15px;margin-left: 60px",
            "oninput": "subunitsDisable()"
            },
        validators=[DataRequired()]
    )

    supplier = SelectField(
        choices=[("", "Supplier...")],
        render_kw={
            "class": "form-control col-md-9",
            "id": "supplier",
            "onfocus": "this.size=3;",
            "onblur": "this.size=1;",
            "onchange": "this.size=1; this.blur();",
            "style": "padding-right:15px;padding-left:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    product_image = FileField(
        label='Upload product image',
        render_kw={
            "id": "upload",
            "style": "padding:15px;margin-left: 50px",
            "onchange": "displayname(this,$(this))"
            },
        validators=[
            FileRequired('File required')
        ]
    )

    received = DateField(
        label="Date Received",
        format='%d-%m-%Y',
        default=datetime.today(),
        render_kw={
            "class": "form-control col-md-9",
            "id": "received",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    expiry = DateField(
        label="Expiration Date",
        format='%d-%m-%Y',
        default=datetime.today(),
        render_kw={
            "class": "form-control col-md-9",
            "id": "expiry",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    buying_price = DecimalField(
        render_kw={
            "placeholder": "Buying Price...",
            "class": "form-control col-md-9",
            "id": "buying_price",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    discount = DecimalField(
        render_kw={
            "placeholder": "Discount...",
            "class": "form-control col-md-9",
            "id": "discount",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )
    
    selling_price = DecimalField(
        render_kw={
            "placeholder": "Selling Price...",
            "class": "form-control col-md-9",
            "id": "selling_price",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    quantity = DecimalField(
        render_kw={
            "placeholder": "Quantity...",
            "class": "form-control col-md-9",
            "id": "quantity",
            "style": "padding:15px;margin-left: 60px",
            "min": "0",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    restock_level = DecimalField(
        render_kw={
            "placeholder": "Restock Level...",
            "class": "form-control col-md-9",
            "id": "restock_level",
            "style": "padding:15px;margin-left: 60px",
            "min": "0",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Add Stock',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary",
            "id": "addProduct"
            }
    )

class AddSupplierForm(FlaskForm):
    name = StringField(
        render_kw={
            "placeholder": "Supplier Name...",
            "class": "form-control col-md-9",
            "id": "name",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    contact = StringField(
        render_kw={
            "placeholder": "Supplier Contact...",
            "class": "form-control col-md-9",
            "id": "contact",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Add Supplier',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary",
            "id": "addSupplier"
        }
    )

class RestockProductForm(FlaskForm):
    received = DateField(
        label="Date Received",
        format='%d-%m-%Y',
        default=datetime.today(),
        render_kw={
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    supplier = SelectField(
        choices=[("", "Supplier...")],
        render_kw={
            "class": "form-control col-md-9",
            "onfocus": "this.size=3;",
            "onblur": "this.size=1;",
            "onchange": "this.size=1; this.blur();",
            "style": "padding-right:15px;padding-left:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    quantity = DecimalField(
        render_kw={
            "placeholder": "Quantity...",
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
            "min": "0",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    buying_price = DecimalField(
        render_kw={
            "placeholder": "Buying Price...",
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    discount = DecimalField(
        render_kw={
            "placeholder": "Discount...",
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )
    
    selling_price = DecimalField(
        render_kw={
            "placeholder": "Selling Price...",
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    expiry = DateField(
        label="Expiration Date",
        format='%d-%m-%Y',
        default=datetime.today(),
        render_kw={
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Make Restock',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary addPurchase"
            }
    )

class ProductUnitSettingForm(FlaskForm):
    name = StringField(
        label='Stock Name',
        render_kw={
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
            "disabled": "true"
            },
        validators=[DataRequired()]
    )

    unit = SelectField(
        label='Unit',
        choices=[]
    )

    contains = IntegerField(
        label='Contains',
        render_kw={
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
            "min": "0",
            "step": "1"
            },
        validators=[DataRequired()]
    )

    subunit = SelectField(
        label='Sub-Units',
        choices=[]
    )
    
    replenish = IntegerField(
    label='Sub-Unit Replenish Quantity',
    render_kw={
        "class": "form-control col-md-9",
        "style": "padding:15px;margin-left: 60px",
        "min": "0",
        "step": "1"
        },
    validators=[DataRequired()]
    )

    restock_level = DecimalField(
        label='Restock/Replenish Level',
        render_kw={
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
            "min": "0",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Edit Automation',
        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary editAutomation"
            }
    )

class AddProductUnitForm(FlaskForm):
    name = StringField(
        render_kw={
            "placeholder": "Unit Name...",
            "class": "form-control col-md-9",
            "id": "unit",
            "style": "padding:15px;margin-left: 60px"
        },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Add Unit',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary",
            "id": "addUnit"
        }
    )

class AddExpenseForm(FlaskForm):
    category = SelectField(
        choices=[("", "Expense Category...")],
        render_kw={
            "class": "form-control col-md-9",
            "id": "category",
            "onfocus": "this.size=3;",
            "onblur": "this.size=1;",
            "onchange": "this.size=1; this.blur();",
            "style": "padding-right:15px;padding-left:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    particular = StringField(
        render_kw={
            "placeholder": "Expense Particular...",
            "class": "form-control col-md-9",
            "id": "particular",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    party = StringField(
        render_kw={
            "placeholder": "Party Name...",
            "class": "form-control col-md-9",
            "id": "party",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )
    
    total = DecimalField(
        render_kw={
            "placeholder": "Total Amount...",
            "class": "form-control col-md-9",
            "id": "total",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    paid = DecimalField(
        render_kw={
            "placeholder": "Paid Amount...",
            "class": "form-control col-md-9",
            "id": "paid",
            "style": "padding:15px;margin-left: 60px",
            "min": "0.01",
            "step": "0.01"
            },
        validators=[DataRequired()]
    )

    date = DateField(
        label="Payment Date",
        format='%d-%m-%Y',
        default=datetime.today(),
        render_kw={
            "class": "form-control col-md-9",
            "id": "received",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )


    submit = SubmitField(
        label='Add Expense',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary",
            "id": "addExpense"
            }
    )

class AddExpenseCategoryForm(FlaskForm):
    category = StringField(
        render_kw={
            "placeholder": "Expense Category...",
            "class": "form-control col-md-9",
            "id": "category",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Add Expense Category',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary",
            "id": "addExpenseCategory"
            }
    )

class AddReclassCategoryForm(FlaskForm):
    category = StringField(
        render_kw={
            "placeholder": "Reclass Category Name...",
            "class": "form-control col-md-9",
            "id": "category",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    parent_product = StringField(
        render_kw={
            "placeholder": "Parent Product Search...",
            "class": "form-control col-md-9 parent_product",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Add Reclass Category',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary",
            "id": "addReclassCategory"
            }
    )

class AddReclassItemForm(FlaskForm):
    reclass_category = StringField(
        render_kw={
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px",
        }
    )

    child_product = StringField(
        render_kw={
            "placeholder": "Child Product Search...",
            "class": "form-control col-md-9 child_product",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Add Reclass Item',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary",
            "id": "addReclassItem"
            }
    )

class ForceAttributionForm(FlaskForm):
    transaction_code = StringField(
        render_kw={
            "placeholder": "Transaction Code...",
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    msisdn = StringField(
        render_kw={
            "placeholder": "Last 3 digits of MSISDN",
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    amount = IntegerField(
    render_kw={
        "placeholder": "Amount Paid...",
        "class": "form-control col-md-9",
        "style": "padding:15px;margin-left: 60px",
        "min": "0",
        "step": "1"
        },
    validators=[DataRequired()]
    )

    name = StringField(
        render_kw={
            "placeholder": "Customer Name...",
            "class": "form-control col-md-9",
            "style": "padding:15px;margin-left: 60px"
            },
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Force Attribution',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary forcePaymentAttribution"
            }
    )

class RefundForm(FlaskForm):
    refund_amount = IntegerField(
    render_kw={
        "placeholder": "Refund Amount...",
        "class": "form-control col-md-9",
        "style": "padding:15px;margin-left: 60px",
        "min": "0",
        "step": "1"
        },
    validators=[DataRequired()]
    )

    submit = SubmitField(
        label='Add Refund',

        render_kw={
            "style": "margin-right: 50px",
            "class": "btn btn-primary addRefund"
            }
    )